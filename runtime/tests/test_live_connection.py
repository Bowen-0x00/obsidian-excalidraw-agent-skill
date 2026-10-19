"""Long-lived MCP requests must follow private configuration, never historical tokens."""
from __future__ import annotations

import json
import os
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from drawing_client import BridgeError, DrawingClient


class LiveConnectionTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.path = Path(self.directory.name) / "connection.json"
        environment = {k: v for k, v in os.environ.items() if not k.startswith("EXCALIDRAW_")}
        environment["EXCALIDRAW_AGENT_CONFIG"] = str(self.path)
        self.scope = patch.dict(os.environ, environment, clear=True)
        self.scope.start()
        self.servers = []

    def tearDown(self):
        for server, thread in self.servers:
            server.shutdown()
            server.server_close()
            thread.join()
        self.scope.stop()
        self.directory.cleanup()

    def service(self, identity, token):
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                authorized = self.headers.get("Authorization") == "Bearer " + token
                body = json.dumps({"ok": True, "vault": identity} if authorized else {
                    "ok": False, "error": {"code": "UNAUTHORIZED", "message": "Invalid credential"}
                }).encode()
                self.send_response(200 if authorized else 401)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.servers.append((server, thread))
        return f"http://127.0.0.1:{server.server_port}"

    def save(self, url, token):
        temporary = self.path.with_suffix(".new")
        temporary.write_text(json.dumps({"bridge_url": url, "bridge_token": token}), encoding="utf-8")
        temporary.replace(self.path)

    def test_existing_client_follows_private_connection_rotation_before_next_request(self):
        old_url = self.service("old-vault", "old-test-credential")
        new_url = self.service("chosen-vault", "new-test-credential")
        self.save(old_url, "old-test-credential")
        client = DrawingClient()
        self.assertEqual(client.request("GET", "/v3/status")["vault"], "old-vault")
        self.save(new_url, "new-test-credential")
        self.assertEqual(client.request("GET", "/v3/status")["vault"], "chosen-vault")
        self.path.write_text('{"broken":', encoding="utf-8")
        with self.assertRaises(ValueError):
            client.request("GET", "/v3/status")

    def test_explicit_connection_and_environment_precedence_survive_disk_changes(self):
        pinned_url = self.service("pinned", "explicit-test-credential")
        configured_url = self.service("configured", "configured-test-credential")
        self.save(configured_url, "configured-test-credential")
        pinned = DrawingClient(pinned_url, "explicit-test-credential", timeout=2)
        configured = DrawingClient()
        self.save(configured_url, "wrong-test-credential")
        self.assertEqual(pinned.request("GET", "/v3/status")["vault"], "pinned")
        with self.assertRaises(BridgeError) as error:
            configured.request("GET", "/v3/status")
        self.assertEqual(error.exception.code, "UNAUTHORIZED")
        os.environ["EXCALIDRAW_BRIDGE_TOKEN"] = "configured-test-credential"
        self.assertEqual(configured.request("GET", "/v3/status")["vault"], "configured")
        self.assertEqual(pinned.request("GET", "/v3/status")["vault"], "pinned")


if __name__ == "__main__":
    unittest.main()
