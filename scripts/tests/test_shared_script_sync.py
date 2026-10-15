"""Consumer-visible boundaries for shared Engine snapshot synchronization."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("shared_script_importer", Path(__file__).resolve().parents[2] / "scripts/sync_shared_scripts.py")
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class SharedScriptSyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "package"
        self.source = Path(self.temp.name) / "source"
        self.root.mkdir()
        self.source.mkdir()
        self.run_git("init", "-q")
        self.run_git("config", "user.email", "test@example.invalid")
        self.run_git("config", "user.name", "Sync Test")
        files = []
        records = {}
        for name in ["one", "two"]:
            relative = f"{name}/Feature-{name}-Engine.md"
            raw = f"---\nversion: 1.0.0\n---\nconst value = '{name}';\n".encode()
            src, dst = "Scripts/" + relative, "bridge/Scripts/" + relative
            for base, path in [(self.source, src), (self.root, dst)]:
                target = base / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(raw)
            files.append({"source": src, "target": dst})
            records[dst] = {"source": src, "sha256": sync.digest(raw), "version": "1.0.0"}
        self.write_json(sync.MANIFEST, {"schemaVersion": 1, "source": {"repository": "owner/scripts", "branch": "main"}, "files": files})
        self.write_json(sync.LOCK, {"schemaVersion": 1, "repository": "owner/scripts", "sourceCommit": None, "files": records})
        self.write_json("bridge/bundle.json", {"scripts": ["mcp/Agent.md", *[f["source"].removeprefix("Scripts/") for f in files]]})
        agent = self.root / "bridge/Scripts/mcp/Agent.md"
        agent.parent.mkdir()
        agent.write_text("Agent-only source", encoding="utf-8")
        self.commit()

    def run_git(self, *args):
        return subprocess.run(["git", "-C", str(self.source), *args], check=True, capture_output=True, encoding="utf-8").stdout.strip()

    def commit(self):
        self.run_git("add", ".")
        self.run_git("commit", "-qm", "fixture")
        return self.run_git("rev-parse", "HEAD")

    def write_json(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def update_one(self):
        path = self.source / "Scripts/one/Feature-one-Engine.md"
        # Same declared version: detection must use content, not semver.
        path.write_text("---\nversion: 1.0.0\n---\nconst changed = true;\n", encoding="utf-8")
        return self.commit()

    def test_only_declared_files_change_and_second_apply_is_noop(self):
        commit = self.update_one()
        report = sync.synchronize(self.root, self.source, commit, apply=True)
        self.assertEqual([c["target"] for c in report["changes"]], ["bridge/Scripts/one/Feature-one-Engine.md"])
        self.assertIn("changed = true", (self.root / report["changes"][0]["target"]).read_text())
        self.assertEqual((self.root / "bridge/Scripts/mcp/Agent.md").read_text(), "Agent-only source")
        lock = (self.root / sync.LOCK).read_bytes()
        self.assertEqual(json.loads(lock)["sourceCommit"], commit)
        self.assertFalse(sync.synchronize(self.root, self.source, commit, apply=True)["changed"])
        self.assertEqual((self.root / sync.LOCK).read_bytes(), lock)

    def test_unrelated_source_change_does_not_churn_lock(self):
        lock = (self.root / sync.LOCK).read_bytes()
        (self.source / "README.md").write_text("not bundled")
        commit = self.commit()
        self.assertFalse(sync.synchronize(self.root, self.source, commit, apply=True)["changed"])
        self.assertEqual((self.root / sync.LOCK).read_bytes(), lock)

    def test_deleted_input_prevents_partial_copy(self):
        self.update_one()
        (self.source / "Scripts/two/Feature-two-Engine.md").unlink()
        commit = self.commit()
        before = (self.root / "bridge/Scripts/one/Feature-one-Engine.md").read_bytes()
        with self.assertRaisesRegex(ValueError, "deleted, renamed"):
            sync.synchronize(self.root, self.source, commit, apply=True)
        self.assertEqual((self.root / "bridge/Scripts/one/Feature-one-Engine.md").read_bytes(), before)

    def test_local_edit_is_not_overwritten(self):
        commit = self.update_one()
        target = self.root / "bridge/Scripts/two/Feature-two-Engine.md"
        target.write_text("---\nversion: 1.0.0\n---\nuser change\n")
        with self.assertRaisesRegex(ValueError, "drifted"):
            sync.synchronize(self.root, self.source, commit, apply=True)
        self.assertIn("user change", target.read_text())

    def test_uses_requested_commit_not_dirty_source_worktree(self):
        commit = self.run_git("rev-parse", "HEAD")
        (self.source / "Scripts/one/Feature-one-Engine.md").write_text("uncommitted script")
        self.assertFalse(sync.synchronize(self.root, self.source, commit, apply=True)["changed"])

    def test_line_endings_are_not_script_drift(self):
        target = self.root / "bridge/Scripts/one/Feature-one-Engine.md"
        target.write_bytes(target.read_bytes().replace(b"\n", b"\r\n"))
        sync.load_contract(self.root)
        self.assertFalse(sync.synchronize(self.root, self.source, self.run_git("rev-parse", "HEAD"), apply=True)["changed"])

    def test_agent_owned_and_traversal_paths_are_rejected(self):
        manifest = json.loads((self.root / sync.MANIFEST).read_text())
        manifest["files"][0]["target"] = "bridge/Scripts/mcp/Agent.md"
        self.write_json(sync.MANIFEST, manifest)
        with self.assertRaisesRegex(ValueError, "Agent-owned"):
            sync.load_contract(self.root)
        with self.assertRaises(ValueError):
            sync.relative_file("Scripts/../private.md", "Scripts/")
        with self.assertRaises(ValueError):
            sync.synchronize(self.root, self.source, "main", apply=True)


if __name__ == "__main__":
    unittest.main()
