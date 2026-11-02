"""Headless mode must never mutate host vault setup or attempt GUI startup."""
from __future__ import annotations

import json
import os
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "runtime"))
from setup_connection import connect_vault, discover_vaults, select_connection, setup_status, start_bridge


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

    def test_remote_registry_uses_authenticated_host_metadata_and_status_is_read_only(self):
        requests = []
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                requests.append((self.path, self.headers.get("Authorization")))
                result = ({"ok": True, "ready": False, "host": {"id": "host", "name": "Host", "platform": "win32"},
                           "vault": {"id": "vault", "name": "Host Vault", "path": "Z:/host-only/vault"},
                           "pluginVersion": "0.13.8", "openCanvases": [], "engines": {"native": True}}
                          if self.path == "/v3/status" else {"host": {"id": "host"}, "currentVaultId": "vault", "vaults": [
                              {"id": "vault", "name": "Host Vault", "path": "Z:/host-only/vault", "pluginEnabled": True, "running": True, "selected": True}]})
                body = json.dumps(result).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "connection.json"
                original = json.dumps({"mode": "remote", "bridge_url": f"http://127.0.0.1:{server.server_port}",
                                       "bridge_token": "private-remote-credential", "host_id": "host", "vault_id": "vault",
                                       "host_vault_path": "Z:/host-only/vault"})
                path.write_text(original, encoding="utf-8")
                environment = {k: v for k, v in os.environ.items() if not k.startswith("EXCALIDRAW_")}
                environment.update(EXCALIDRAW_AGENT_CONFIG=str(path), EXCALIDRAW_AGENT_STATE_DIR=directory)
                with patch.dict(os.environ, environment, clear=True), patch("setup_connection._local_vaults", side_effect=AssertionError("must not inspect client vaults")):
                    result = setup_status()
                    self.assertEqual(discover_vaults()[0]["path"], "Z:/host-only/vault")
                self.assertEqual(result["code"], "NO_CANVAS")
                self.assertTrue(result["connected"])
                self.assertFalse(result["ready"])
                self.assertEqual(result["host"]["id"], "host")
                self.assertEqual(result["plugin_version"], "0.13.8")
                self.assertNotIn("private-remote-credential", json.dumps(result))
                self.assertEqual(path.read_text(encoding="utf-8"), original)
                self.assertIn(("/v3/vaults", "Bearer private-remote-credential"), requests)
                self.assertTrue(all(auth == "Bearer private-remote-credential" for _, auth in requests))
        finally:
            server.shutdown()
            server.server_close()
            thread.join()

    def test_remote_use_selects_only_paired_remote_profiles_without_host_filesystem_access(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory)
            (state / "connection.json").write_text(json.dumps({"mode": "remote", "bridge_url": "http://127.0.0.1:28125", "bridge_token": "old"}), encoding="utf-8")
            (state / "connections").mkdir()
            for name, mode in (("paired", "remote"), ("local", "local")):
                (state / "connections" / (name + ".json")).write_text(json.dumps({
                    "mode": mode, "vault_name": name, "vault_id": name, "host_id": "host", "host_vault_path": "Z:/unavailable/host-vault",
                    "bridge_url": "http://127.0.0.1:28125", "bridge_token": name,
                }), encoding="utf-8")
            environment = {k: v for k, v in os.environ.items() if not k.startswith("EXCALIDRAW_")}
            environment.update(EXCALIDRAW_AGENT_CONFIG=str(state / "connection.json"), EXCALIDRAW_AGENT_STATE_DIR=directory)
            with patch.dict(os.environ, environment, clear=True), patch("setup_connection._bridge_probe", return_value={"connected": False, "ready": False, "code": "CONNECTION_FAILED"}), patch("setup_connection.bridge_get", side_effect=OSError("offline")), patch("runtime_config.default_state_directory", side_effect=AssertionError("must not inspect another host state")):
                result = connect_vault(vault_name="paired", open_uri=False)
                self.assertEqual(result["selected_connection_id"], "paired")
                self.assertEqual(result["mode"], "remote")
                with self.assertRaises(ValueError):
                    select_connection("local")
                with self.assertRaises(ValueError):
                    start_bridge()



if __name__ == "__main__":
    unittest.main()
