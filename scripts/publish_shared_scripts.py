"""Publish a validated shared-script snapshot as one reusable, reviewable PR."""
from __future__ import annotations

import json
import os
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from sync_shared_scripts import LOCK, MANIFEST, ROOT, git, load_contract, synchronize

BRANCH = "automation/shared-script-engines"
BOT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"


def api(method: str, path: str, payload=None):
    token = os.environ["GH_TOKEN"]
    request = urllib.request.Request("https://api.github.com" + path,
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "shared-script-sync"}, method=method)
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            body = response.read()
            return json.loads(body) if body else None
    except urllib.error.HTTPError as error:
        body = json.loads(error.read())
        raise RuntimeError(f"GitHub {error.code}: {body.get('message', 'request failed')}") from None


def run(*args: str):
    subprocess.run(args, cwd=ROOT, check=True)


def main():
    root = ROOT
    source = root / ".upstream-scripts"
    manifest, _ = load_contract(root)
    expected_repo = manifest["source"]["repository"]
    target_repo = os.environ["GITHUB_REPOSITORY"]
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    if os.environ["GITHUB_EVENT_NAME"] == "repository_dispatch":
        payload = event.get("client_payload", {})
        if payload.get("repository") != expected_repo or not payload.get("sha"):
            raise ValueError("Unexpected dispatch source")
        # Accept delayed notifications only from commits belonging to source main.
        requested = payload["sha"]
        if len(requested) != 40 or any(c not in "0123456789abcdef" for c in requested):
            raise ValueError("Dispatch SHA must be exact")
        git(source, "merge-base", "--is-ancestor", requested, "HEAD")
    # Coalesce rapid/delayed notifications to the current checked-out main tip.
    commit = git(source, "rev-parse", "HEAD")
    result = synchronize(root, source, commit, apply=True)
    if not result["changed"]:
        print("No declared shared Engine content changed; no PR or lock churn.")
        return
    # Checks precede branch writes. No upstream Engine code executes here.
    run("node", "scripts/check_shared_scripts.mjs")
    run("python", "-m", "unittest", "discover", "-s", "scripts/tests", "-v")
    run("uv", "run", "--frozen", "python", "-m", "unittest", "discover", "-s", "runtime/tests", "-v")
    run("git", "fetch", "origin", "main")
    if git(root, "rev-parse", "HEAD") != git(root, "rev-parse", "origin/main"):
        raise ValueError("Target main changed during validation; rerun sync on fresh main")
    prefix = f"/repos/{target_repo}"
    pulls = api("GET", prefix + "/pulls?state=open&head=" + urllib.parse.quote(target_repo.split('/')[0] + ':' + BRANCH))
    remote = git(root, "ls-remote", "--heads", "origin", "refs/heads/" + BRANCH)
    previous = remote.split()[0] if remote else ""
    allowed = {item["target"] for item in manifest["files"]} | {LOCK}
    if previous:
        git(root, "fetch", "origin", BRANCH)
        branch_tip = git(root, "rev-parse", "FETCH_HEAD")
        changed = set(git(root, "diff", "--name-only", "origin/main..." + branch_tip).splitlines())
        authors = set(git(root, "log", "--format=%ae", "origin/main.." + branch_tip).splitlines())
        if not changed <= allowed or not authors <= {BOT_EMAIL}:
            raise ValueError("Sync branch has non-bot or out-of-scope edits; refusing to overwrite")
        if not pulls:
            closed = api("GET", prefix + "/pulls?state=closed&head=" + urllib.parse.quote(target_repo.split('/')[0] + ':' + BRANCH))
            if not closed or not closed[0]["merged_at"] or closed[0]["head"]["sha"] != previous:
                raise ValueError("Sync branch belongs to a rejected/orphaned PR; resolve it explicitly")
        elif len(pulls) != 1:
            raise ValueError("Sync branch has no unique open PR")
        else:
            prior = json.loads(git(root, "show", branch_tip + ":" + LOCK))
            desired = json.loads((root / LOCK).read_text(encoding="utf-8"))
            targets = sorted(allowed - {LOCK})
            if (prior["files"] == desired["files"]
                    and not git(root, "diff", branch_tip, "--", *targets)):
                print("Open sync PR already contains this Engine content: " + pulls[0]["html_url"])
                return
    run("git", "config", "user.name", "github-actions[bot]")
    run("git", "config", "user.email", BOT_EMAIL)
    run("git", "add", "--", *result["paths"])
    staged = set(git(root, "diff", "--cached", "--name-only").splitlines())
    if not staged <= allowed or not staged:
        raise ValueError("Unexpected staged changes")
    run("git", "commit", "-m", f"chore: sync shared Engines from {commit[:12]}")
    run("gh", "auth", "setup-git")
    run("git", "push", f"--force-with-lease=refs/heads/{BRANCH}:{previous}", "origin", f"HEAD:refs/heads/{BRANCH}")
    rows = [f"| `{c['source']}` | {c['oldVersion']} | {c['newVersion']} |" for c in result["changes"]]
    run_url = f"https://github.com/{target_repo}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
    body = (f"Imported from [{expected_repo}@{commit[:12]}](https://github.com/{expected_repo}/commit/{commit}).\n\n"
            "Only the explicit shared-Engine manifest is imported; Agent Bridge/bootstrap stay unchanged.\n\n"
            "| Source | Previous | Imported |\n|---|---|---|\n" + "\n".join(rows) +
            f"\n\nValidation: [import integrity, nonexecuting JavaScript syntax and full existing Python suite]({run_url}).\n\n"
            "**Maintainer gate:** inspect API/Hook changes and exercise affected features in Obsidian before merge/release. "
            "CI is not a real GUI/interaction/PNG compatibility proof. Do not edit this bot branch; return shared Engine fixes upstream. "
            "This PR does not bump the package, deploy vault scripts, or reload running Engines.\n")
    title = "chore: update shared Engines from Scripts"
    if pulls:
        pull = api("PATCH", prefix + f"/pulls/{pulls[0]['number']}", {"title": title, "body": body})
    else:
        pull = api("POST", prefix + "/pulls", {"title": title, "body": body, "head": BRANCH, "base": "main"})
    print("Shared Engine update PR: " + pull["html_url"])
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as summary:
        summary.write(f"### Shared Engines\n{pull['html_url']}\n\nSource: `{commit}`\n")


if __name__ == "__main__":
    main()
