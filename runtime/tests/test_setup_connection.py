"""Installer regressions for preserving vault edits and plugin permissions."""
from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "runtime"))
from setup_connection import PLUGIN_ID, connect_vault
from runtime_config import load_connection


class InstallerPreservationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.vault = self.base / "vault"
        plugin = self.vault / ".obsidian/plugins" / PLUGIN_ID
        plugin.mkdir(parents=True)
        (plugin / "manifest.json").write_text(json.dumps({"id": PLUGIN_ID, "version": "test"}), encoding="utf-8")
        (plugin / "main.js").write_text("filesystem fixture, never executed", encoding="utf-8")
        (plugin / "data.json").write_text(json.dumps({"scriptFolderPath": "Excalidraw/Scripts"}), encoding="utf-8")
        self.enabled = self.vault / ".obsidian/community-plugins.json"
        self.enabled.write_text(json.dumps([PLUGIN_ID]), encoding="utf-8")
        environment = {key: value for key, value in os.environ.items() if not key.startswith("EXCALIDRAW_")}
        environment["EXCALIDRAW_AGENT_STATE_DIR"] = str(self.base / "state")
        scope = patch.dict(os.environ, environment, clear=True)
        scope.start()
        self.addCleanup(scope.stop)

    def connect(self):
        return connect_vault(str(self.vault), port=28199, open_uri=False)

    def test_reconnect_keeps_credentials_and_refuses_user_edits(self):
        result = self.connect()
        token = load_connection()["bridge_token"]
        self.connect()
        self.assertEqual(load_connection()["bridge_token"], token)
        script = Path(result["script_directory"]) / "mcp/Engine-Agent-Bridge.md"
        script.write_text("user customized this script", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.connect()
        self.assertEqual(script.read_text(encoding="utf-8"), "user customized this script")
        self.assertEqual(load_connection()["bridge_token"], token)

    def test_disabled_plugin_is_not_enabled_or_deployed(self):
        self.enabled.write_text("[]", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.connect()
        self.assertEqual(json.loads(self.enabled.read_text(encoding="utf-8")), [])
        self.assertFalse((self.vault / "Excalidraw/Scripts/Agent-Drawing").exists())
        self.assertEqual(load_connection(), {})

    def test_private_connection_cannot_be_placed_in_vault(self):
        os.environ["EXCALIDRAW_AGENT_CONFIG"] = str(self.vault / "leaked-connection.json")
        with self.assertRaises(ValueError):
            self.connect()
        self.assertFalse((self.vault / "leaked-connection.json").exists())
        self.assertFalse((self.vault / "Excalidraw/Scripts/Agent-Drawing").exists())


if __name__ == "__main__":
    unittest.main()
