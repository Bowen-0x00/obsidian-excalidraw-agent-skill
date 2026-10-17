"""Safety boundaries of opt-in observations, not a simulated drawing engine."""

from __future__ import annotations

import json
import os
import sys
import tempfile
import threading
import unittest
import urllib.error
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cdp_readonly as cdp


class ReadOnlyCdpTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.environment = patch.dict(
            os.environ, {"EXCALIDRAW_AGENT_STATE_DIR": self.directory.name}
        )
        self.environment.start()

    def tearDown(self):
        self.environment.stop()
        self.directory.cleanup()

    def test_disabled_never_contacts_a_debugger_and_disable_revokes_future_reads(self):
        with patch.object(
            cdp, "_target", side_effect=AssertionError("Network not permitted")
        ):
            self.assertFalse(cdp.status()["enabled"])
            with self.assertRaises(cdp.DiagnosticError) as raised:
                cdp.inspect("Drawings/one.excalidraw.md")
            self.assertEqual(raised.exception.code, "CDP_DISABLED")
            cdp.configure(True, "http://127.0.0.1:19223", "D:/Lab/vault")
            self.assertTrue(cdp.status()["enabled"])
            cdp.configure(False)
            with self.assertRaises(cdp.DiagnosticError) as raised:
                cdp.inspect("Drawings/one.excalidraw.md")
            self.assertEqual(raised.exception.code, "CDP_DISABLED")

    def test_only_numeric_loopback_endpoint_without_credentials_or_path_is_accepted(
        self,
    ):
        for endpoint in (
            "http://example.com:9222",
            "http://localhost:9222",
            "https://127.0.0.1:9222",
            "http://127.0.0.1:9222/secret",
            "http://user:pass@127.0.0.1:9222",
            "http://127.0.0.1:9222/?next=http://example.com",
            "http://127.0.0.1:22",
        ):
            with (
                self.subTest(endpoint=endpoint),
                self.assertRaises(cdp.DiagnosticError),
            ):
                cdp.configure(True, endpoint, "D:/Lab/vault")
        self.assertEqual(cdp.endpoint_url("http://[::1]:9222/"), "http://[::1]:9222")
        self.assertFalse(cdp.config_path().exists())

    def test_inspect_requires_explicit_bounded_file_and_page_before_discovery(self):
        cdp.configure(True, "http://127.0.0.1:19223", "D:/Lab/vault")
        with patch.object(
            cdp,
            "_target",
            side_effect=AssertionError("Validation must precede discovery"),
        ):
            for path in (
                None,
                "",
                "../one.excalidraw.md",
                "/one.excalidraw.md",
                "D:/one.excalidraw.md",
                "notes.md",
            ):
                with self.subTest(path=path), self.assertRaises(cdp.DiagnosticError):
                    cdp.inspect(path)
            for options in (
                {"offset": -1},
                {"limit": 201},
                {"limit": True},
                {"ids": [""]},
                {"ids": ["a"] * 101},
            ):
                with (
                    self.subTest(options=options),
                    self.assertRaises(cdp.DiagnosticError),
                ):
                    cdp.inspect("Drawings/one.excalidraw.md", **options)

    def test_debugger_discovery_cannot_redirect_or_retarget_to_other_websocket(self):
        config = {"endpoint": "http://127.0.0.1:19223", "vault_path": "D:/Lab/vault"}
        target = {
            "id": "one",
            "type": "page",
            "url": "app://obsidian.md/index.html",
            "webSocketDebuggerUrl": "ws://127.0.0.1:19223/devtools/page/one",
        }
        with patch.object(
            cdp, "_read_json", return_value=[target, {**target, "id": "two"}]
        ):
            with self.assertRaises(cdp.DiagnosticError) as raised:
                cdp._target(config)
            self.assertEqual(raised.exception.code, "CDP_TARGET_REQUIRED")
        for url in (
            "ws://example.com:19223/devtools/page/one",
            "ws://127.0.0.1:9999/devtools/page/one",
            "ws://user:pass@127.0.0.1:19223/devtools/page/one",
            "ws://127.0.0.1:19223/private",
        ):
            with patch.object(
                cdp,
                "_read_json",
                return_value=[{**target, "webSocketDebuggerUrl": url}],
            ):
                with self.subTest(url=url), self.assertRaises(cdp.DiagnosticError):
                    cdp._target(config)
        requests = []

        class Redirect(BaseHTTPRequestHandler):
            def do_GET(self):
                requests.append(self.path)
                self.send_response(302)
                self.send_header("Location", "/must-not-follow")
                self.end_headers()

            def log_message(self, *args):
                pass

        with ThreadingHTTPServer(("127.0.0.1", 0), Redirect) as server:
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                with self.assertRaises(urllib.error.HTTPError):
                    cdp._read_json(f"http://127.0.0.1:{server.server_port}/json/list")
            finally:
                server.shutdown()
                thread.join()
        self.assertEqual(requests, ["/json/list"])

    def test_mutations_arbitrary_expressions_and_guard_removal_are_rejected_before_send(
        self,
    ):
        class NoSend:
            def send(self, packet):
                raise AssertionError("Forbidden packet escaped")

        session = cdp._Session(
            NoSend(), {"vault": "D:/Lab/vault", "file": "Drawings/one.excalidraw.md"}
        )
        for method in (
            "Input.dispatchMouseEvent",
            "Input.dispatchKeyEvent",
            "Page.navigate",
            "Page.reload",
            "Page.captureScreenshot",
            "Debugger.pause",
            "Runtime.callFunctionOn",
            "Runtime.terminateExecution",
        ):
            with (
                self.subTest(method=method),
                self.assertRaises(cdp.DiagnosticError) as raised,
            ):
                session.request(method, {})
            self.assertEqual(raised.exception.code, "CDP_OPERATION_FORBIDDEN")
        for expression in (
            "app.vault.delete(app.workspace.getActiveFile())",
            "window.x=1",
            session.snapshot_expression + ";app.workspace.activeLeaf.detach()",
        ):
            with (
                self.subTest(expression=expression),
                self.assertRaises(cdp.DiagnosticError),
            ):
                session.evaluate(expression)
        params = {
            "expression": cdp._IDENTITY,
            "throwOnSideEffect": False,
            "returnByValue": True,
            "timeout": 3000,
            "disableBreaks": True,
            "silent": True,
        }
        with self.assertRaises(cdp.DiagnosticError):
            session.request("Runtime.evaluate", params)

    def test_v8_rejection_has_no_unguarded_retry(self):
        class Rejected:
            def __init__(self):
                self.sent = []

            def send(self, packet):
                self.sent.append(json.loads(packet))

            def recv(self, timeout):
                return json.dumps(
                    {
                        "id": 1,
                        "result": {
                            "exceptionDetails": {"text": "Possible side effect"}
                        },
                    }
                )

        socket = Rejected()
        with self.assertRaises(cdp.DiagnosticError) as raised:
            cdp._Session(socket).evaluate(cdp._IDENTITY)
        self.assertEqual(raised.exception.code, "CDP_READ_REJECTED")
        self.assertEqual(len(socket.sent), 1)
        self.assertTrue(socket.sent[0]["params"]["throwOnSideEffect"])

    def test_malformed_or_non_boolean_configuration_fails_closed(self):
        for value in (
            "{",
            '["enabled"]',
            '{"enabled":"false"}',
            '{"enabled":true,"endpoint":"http://example.com:9222","vault_path":"/vault"}',
        ):
            cdp.config_path().write_text(value, encoding="utf-8")
            with (
                self.subTest(value=value),
                self.assertRaises((ValueError, cdp.DiagnosticError)),
            ):
                cdp.status()


if __name__ == "__main__":
    unittest.main()
