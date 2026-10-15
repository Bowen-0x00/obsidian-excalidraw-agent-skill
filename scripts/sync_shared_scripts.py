"""Import only declared shared Engine snapshots; never execute upstream scripts.

The source is a committed Git tree, not its possibly dirty working directory.
Hashes cover UTF-8 content with LF line endings, independent of checkout platform.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "bridge/shared-scripts.json"
LOCK = "bridge/shared-scripts.lock.json"


def git(directory: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(directory), *args], check=True,
                          capture_output=True, encoding="utf-8").stdout.strip()


def normalized(raw: bytes) -> bytes:
    if len(raw) > 2 * 1024 * 1024 or b"\0" in raw:
        raise ValueError("Shared script is binary or exceeds 2 MiB")
    return raw.decode("utf-8").replace("\r\n", "\n").encode("utf-8")


def digest(raw: bytes) -> str:
    return hashlib.sha256(normalized(raw)).hexdigest()


def version(raw: bytes) -> str:
    text = normalized(raw).decode("utf-8")
    header = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    found = re.search(r"^version:\s*(\S.*?)\s*$", header[1], re.M) if header else None
    if not found:
        raise ValueError("Shared script has no frontmatter version")
    return found[1]


def relative_file(value: str, prefix: str) -> str:
    path = PurePosixPath(value)
    if (not isinstance(value, str) or "\\" in value or ":" in value
            or path.is_absolute() or ".." in path.parts or str(path) != value
            or not value.startswith(prefix) or path.suffix != ".md"):
        raise ValueError(f"Invalid declared script path: {value!r}")
    return value


def local_file(root: Path, relative: str) -> Path:
    path = root / relative
    if path.is_symlink() or any(p.is_symlink() for p in path.parents if p != root.parent):
        raise ValueError(f"Symlink is not an import target: {relative}")
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Target escapes package: {relative}")
    return path


def load_contract(root: Path) -> tuple[dict, dict]:
    manifest = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
    lock = json.loads((root / LOCK).read_text(encoding="utf-8"))
    if manifest.get("schemaVersion") != 1 or lock.get("schemaVersion") != 1:
        raise ValueError("Unsupported shared-script contract version")
    source = manifest["source"]
    if (not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", source["repository"])
            or source["branch"] != "main" or lock["repository"] != source["repository"]):
        raise ValueError("Unexpected source repository or branch")
    sources, targets = set(), set()
    for item in manifest["files"]:
        src = relative_file(item["source"], "Scripts/")
        dst = relative_file(item["target"], "bridge/Scripts/")
        if (dst.startswith("bridge/Scripts/mcp/") or src in sources or dst in targets
                or src.removeprefix("Scripts/") != dst.removeprefix("bridge/Scripts/")):
            raise ValueError("Duplicate mapping or Agent-owned/mismatched path")
        sources.add(src)
        targets.add(dst)
        record = lock["files"].get(dst)
        if not record or record["source"] != src:
            raise ValueError(f"Missing or mismatched lock entry: {dst}")
        content = local_file(root, dst).read_bytes()
        if digest(content) != record["sha256"] or version(content) != record["version"]:
            raise ValueError(f"Shared copy drifted; return edits upstream before syncing: {dst}")
    bundle = json.loads((root / "bridge/bundle.json").read_text(encoding="utf-8"))
    required = {"bridge/Scripts/" + p for p in bundle["scripts"] if not p.startswith("mcp/")}
    if targets != required or set(lock["files"]) != targets:
        raise ValueError("Shared mapping, lock and bundle Engine inventory disagree")
    return manifest, lock


def synchronize(root: Path, source_dir: Path, source_commit: str, *, apply: bool = False) -> dict:
    manifest, old_lock = load_contract(root)
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise ValueError("Source commit must be an exact 40-character SHA")
    if git(source_dir, "rev-parse", source_commit + "^{commit}") != source_commit:
        raise ValueError("Source commit is not available")
    staged, records, changes = {}, {}, []
    # Validate the complete input before modifying any target, including deletes.
    for item in manifest["files"]:
        src, dst = item["source"], item["target"]
        tree = git(source_dir, "ls-tree", source_commit, "--", src).split()
        if len(tree) < 4 or tree[0] != "100644" or tree[1] != "blob":
            raise ValueError(f"Required upstream script deleted, renamed or not a regular file: {src}")
        raw = subprocess.run(["git", "-C", str(source_dir), "show", source_commit + ":" + src],
                             check=True, capture_output=True).stdout
        content = normalized(raw)
        sha, ver = digest(content), version(content)
        records[dst] = {"source": src, "sha256": sha, "version": ver}
        if sha != old_lock["files"][dst]["sha256"]:
            changes.append({"source": src, "target": dst,
                            "oldVersion": old_lock["files"][dst]["version"], "newVersion": ver})
            staged[dst] = content
    result = {"repository": manifest["source"]["repository"], "sourceCommit": source_commit,
              "changes": changes, "changed": bool(changes), "paths": list(staged)}
    if not changes:
        # A push to an unrelated script must not churn the lock commit or open a PR.
        return result
    new_lock = {"schemaVersion": 1, "repository": manifest["source"]["repository"],
                "sourceCommit": source_commit, "files": records}
    if apply:
        for dst, content in staged.items():
            local_file(root, dst).write_bytes(content)
        (root / LOCK).write_text(json.dumps(new_lock, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result["paths"].append(LOCK)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check", "plan", "apply"])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--source-commit")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    if args.command == "check":
        manifest, lock = load_contract(args.root)
        result = {"valid": True, "files": len(manifest["files"]), "sourceCommit": lock["sourceCommit"]}
    else:
        if not args.source_dir or not args.source_commit:
            parser.error("plan/apply require --source-dir and --source-commit")
        result = synchronize(args.root, args.source_dir, args.source_commit, apply=args.command == "apply")
    report = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.write_text(report, encoding="utf-8")
    print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
