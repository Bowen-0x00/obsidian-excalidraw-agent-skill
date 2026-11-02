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
from setup_connection import PLUGIN_ID, connect_vault, select_connection, setup_status
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
        default_scope = patch("runtime_config.default_state_directory", return_value=self.base / "host-state")
        default_scope.start()
        self.addCleanup(default_scope.stop)

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

    def test_vault_name_is_a_registry_selector_not_a_relabel(self):
        with patch("setup_connection.discover_vaults", return_value=[]):
            with self.assertRaises(ValueError):
                connect_vault(str(self.vault), vault_name="arbitrary replacement", open_uri=False)
        self.assertFalse((self.base / "state/connection.json").exists())
        self.assertFalse((self.vault / "Excalidraw/Scripts/Agent-Drawing").exists())

    def test_pathless_connect_uses_single_eligible_registered_vault(self):
        choices = [{"id": "eligible", "name": self.vault.name, "path": str(self.vault), "pluginEnabled": True},
                   {"id": "disabled", "name": "disabled", "path": str(self.base / "disabled"), "pluginEnabled": False}]
        with patch("setup_connection.discover_vaults", return_value=choices), patch("setup_connection.start_bridge", return_value={"connected": False}):
            result = connect_vault(open_uri=False)
        self.assertEqual(result["vault_path"], str(self.vault.resolve()))
        self.assertEqual(load_connection()["vault_name"], self.vault.name)

    def test_pathless_connect_refreshes_selected_local_bundle_without_registry_fallback(self):
        with patch("setup_connection.start_bridge", return_value={"connected": False}):
            first = self.connect()
            token = load_connection()["bridge_token"]
            with patch("setup_connection.discover_vaults", side_effect=AssertionError("selected path needs no registry")):
                refreshed = connect_vault(open_uri=False)
        self.assertEqual(refreshed["script_directory"], first["script_directory"])
        self.assertEqual(refreshed["deployed_scripts"], first["deployed_scripts"])
        self.assertEqual(load_connection()["bridge_token"], token)

    def test_environment_binding_is_not_replaced_by_pathless_connect(self):
        os.environ["EXCALIDRAW_BRIDGE_TOKEN"] = "explicit-env-credential"
        choices = [{"id": "eligible", "name": self.vault.name, "path": str(self.vault), "pluginEnabled": True}]
        with patch("setup_connection.discover_vaults", return_value=choices), patch("setup_connection.start_bridge", side_effect=AssertionError("must not deploy")):
            result = connect_vault(open_uri=False)
        self.assertEqual(result["code"], "NOT_CONFIGURED")
        self.assertFalse((self.base / "state/connection.json").exists())
        self.assertFalse((self.vault / "Excalidraw/Scripts/Agent-Drawing").exists())

    def test_multiple_registered_candidates_are_returned_without_deployment(self):
        choices = [{"id": name, "name": name, "path": str(self.base / name), "pluginEnabled": True} for name in ("a", "b")]
        with patch("setup_connection.discover_vaults", return_value=choices):
            result = connect_vault(open_uri=False)
        self.assertEqual(result["code"], "SELECTION_REQUIRED")
        self.assertEqual(result["available_vaults"], choices)
        self.assertFalse((self.base / "state/connection.json").exists())

    def test_explicit_wrong_vault_is_diagnosed_not_replaced(self):
        state = self.base / "state"
        state.mkdir()
        config = {"bridge_url": "http://127.0.0.1:28199", "bridge_token": "private-credential",
                  "vault_id": "selected-vault", "host_id": "selected-host", "bridge_script": "shared/script.md"}
        original = json.dumps(config)
        (state / "connection.json").write_text(original, encoding="utf-8")
        observed = {"ok": True, "ready": True, "scriptPath": "shared/script.md", "host": {"id": "selected-host"},
                    "vault": {"id": "other-vault", "name": "Other", "path": "/host/other"}}
        with patch("runtime_config.bridge_get", return_value=observed), patch("setup_connection.discover_vaults", return_value=[]):
            result = connect_vault(open_uri=False)
        self.assertEqual(result["code"], "IDENTITY_MISMATCH")
        self.assertEqual(result["vault"]["id"], "other-vault")
        self.assertFalse(result["connected"])
        self.assertEqual((state / "connection.json").read_text(encoding="utf-8"), original)
        self.assertNotIn("private-credential", json.dumps(result))

    def test_use_requires_unique_name_and_accepts_exact_profile_id(self):
        profiles = self.base / "state/connections"
        profiles.mkdir(parents=True)
        for name in ("first", "second"):
            (profiles / (name + ".json")).write_text(json.dumps({
                "bridge_url": "http://127.0.0.1:28199", "bridge_token": name, "vault_id": name, "vault_name": "Shared name",
            }), encoding="utf-8")
        with patch("runtime_config.probe_connection", return_value={"connected": False}), patch("setup_connection._bridge_probe", return_value={"connected": False, "ready": False, "code": "CONNECTION_FAILED"}), patch("setup_connection.discover_vaults", return_value=[]):
            with self.assertRaises(ValueError):
                select_connection("Shared name")
            result = select_connection("second")
            self.assertEqual(result["selected_connection_id"], "second")
            self.assertEqual(load_connection()["vault_id"], "second")
            rotated = profiles / "second.json"
            updated = json.loads(rotated.read_text(encoding="utf-8"))
            updated["bridge_url"] = "http://127.0.0.1:28200"
            updated["bridge_token"] = "rotated-credential"
            rotated.write_text(json.dumps(updated), encoding="utf-8")
            self.assertEqual(load_connection()["bridge_url"], "http://127.0.0.1:28200")
            self.assertEqual(load_connection()["bridge_token"], "rotated-credential")

    def test_private_connection_cannot_be_placed_in_vault(self):
        os.environ["EXCALIDRAW_AGENT_CONFIG"] = str(self.vault / "leaked-connection.json")
        with self.assertRaises(ValueError):
            self.connect()
        self.assertFalse((self.vault / "leaked-connection.json").exists())
        self.assertFalse((self.vault / "Excalidraw/Scripts/Agent-Drawing").exists())


if __name__ == "__main__":
    unittest.main()
