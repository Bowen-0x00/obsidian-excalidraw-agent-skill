"""Headless mode must never mutate host vault setup or attempt GUI startup."""
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
from setup_connection import connect_vault, setup_status, start_bridge


class RemoteModeTests(unittest.TestCase):
    def test_remote_connection_rejects_vault_deployment_and_gui_start(self):
        with tempfile.TemporaryDirectory() as directory:
            connection = Path(directory) / "connection.json"
            original = json.dumps({"mode": "remote", "vault_name": "Host Vault",
                                   "host_vault_path": "/host/vault", "bridge_url": "http://127.0.0.1:28125"})
            connection.write_text(original, encoding="utf-8")
            with patch.dict(os.environ, {"EXCALIDRAW_AGENT_CONFIG": str(connection)}):
                with self.assertRaises(ValueError):
                    connect_vault(str(Path(directory) / "invented-vault"))
                with self.assertRaises(ValueError):
                    start_bridge()
            self.assertEqual(connection.read_text(encoding="utf-8"), original)
            self.assertFalse((Path(directory) / "invented-vault").exists())

    def test_remote_status_reports_host_target_without_local_vaults(self):
        with tempfile.TemporaryDirectory() as directory:
            connection = Path(directory) / "connection.json"
            connection.write_text(json.dumps({"mode": "remote", "vault_name": "Host Vault",
                                             "host_vault_path": "/host/vault", "remote_host": "workstation"}), encoding="utf-8")
            with patch.dict(os.environ, {"EXCALIDRAW_AGENT_CONFIG": str(connection)}):
                status = setup_status()
            self.assertEqual(status["mode"], "remote")
            self.assertEqual(status["rendering_location"], "host")
            self.assertEqual(status["host_vault_path"], "/host/vault")
            self.assertIsNone(status["vault_path"])
            self.assertEqual(status["available_vaults"], [])
            self.assertNotIn("bridge_token", status)


if __name__ == "__main__":
    unittest.main()
