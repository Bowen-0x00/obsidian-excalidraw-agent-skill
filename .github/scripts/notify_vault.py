"""Notify Example Vault repository when skill files are updated."""
import json
import os
import subprocess
import urllib.error
import urllib.request
from pathlib import Path

TARGET = "Bowen-0x00/obsidian-excalidraw-example-vault"
SOURCE = "Bowen-0x00/obsidian-excalidraw-agent-skill"


def request(method, path, payload=None):
    token = os.environ["GH_TOKEN"]
    req = urllib.request.Request(
        "https://api.github.com" + path,
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "vault-skill-notification",
        },
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            raw = response.read()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as error:
        message = json.loads(error.read()).get("message", "request failed")
        raise RuntimeError(f"GitHub {error.code}: {message}") from None


def main():
    if os.environ.get("GITHUB_REPOSITORY") != SOURCE:
        raise ValueError("Unexpected source repository")
    sha = os.environ.get("GITHUB_SHA")
    if not sha:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()

    request("POST", f"/repos/{TARGET}/dispatches", {
        "event_type": "skill-updated",
        "client_payload": {"repository": SOURCE, "sha": sha},
    })
    print(f"Notified {TARGET} of published Skill commit {sha}.")


if __name__ == "__main__":
    main()
