"""Consumer-visible configuration and credential regression tests."""
from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

_RUNTIME_DIR = str(Path(__file__).resolve().parents[1])
if _RUNTIME_DIR not in sys.path:
    sys.path.insert(0, _RUNTIME_DIR)

from drawing_client import resolve_bridge_credentials
from review_ledger import ReviewLedger
from runtime_config import ConnectionSelectionRequired, load_connection


class RuntimeConfigTests(unittest.TestCase):
    def setUp(self) -> None:
        self._orig_env = dict(os.environ)

    def tearDown(self) -> None:
        os.environ.clear()
        os.environ.update(self._orig_env)

    def test_explicit_missing_connection_fails_without_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            os.environ["EXCALIDRAW_AGENT_CONFIG"] = str(Path(tmp) / "nonexistent.json")
            with self.assertRaises(ValueError):
                load_connection()

    def test_load_connection_malformed_rejection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "connection.json"
            os.environ["EXCALIDRAW_AGENT_CONFIG"] = str(p)

            # Corrupted / invalid JSON must raise ValueError, not silently ignore
            p.write_text("{malformed", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_connection()

            # Non-dict payload must raise ValueError
            p.write_text(json.dumps(["not", "an", "object"]), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_connection()

    def test_resolve_bridge_credentials_precedence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "connection.json"
            payload = {
                "bridge_url": "http://127.0.0.1:28000",
                "bridge_token": "token-from-file",
                "bridge_timeout": 60.0,
            }
            p.write_text(json.dumps(payload), encoding="utf-8")
            os.environ["EXCALIDRAW_AGENT_CONFIG"] = str(p)

            # 1. Connection file values used when env vars are absent
            for key in ("EXCALIDRAW_BRIDGE_URL", "EXCALIDRAW_BRIDGE_TOKEN", "EXCALIDRAW_BRIDGE_TIMEOUT"):
                os.environ.pop(key, None)

            url, token, timeout = resolve_bridge_credentials()
            self.assertEqual(url, "http://127.0.0.1:28000")
            self.assertEqual(token, "token-from-file")
            self.assertEqual(timeout, 60.0)

            # 2. Environment variables override connection file values
            os.environ["EXCALIDRAW_BRIDGE_URL"] = "http://127.0.0.1:29000"
            os.environ["EXCALIDRAW_BRIDGE_TOKEN"] = "token-from-env"
            os.environ["EXCALIDRAW_BRIDGE_TIMEOUT"] = "120"

            url, token, timeout = resolve_bridge_credentials()
            self.assertEqual(url, "http://127.0.0.1:29000")
            self.assertEqual(token, "token-from-env")
            self.assertEqual(timeout, 120.0)

    def test_unbound_client_selects_only_unique_live_profile_across_state_roots(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            os.environ.pop("EXCALIDRAW_AGENT_CONFIG", None)
            os.environ.pop("EXCALIDRAW_BRIDGE_URL", None)
            os.environ.pop("EXCALIDRAW_BRIDGE_TOKEN", None)
            os.environ["EXCALIDRAW_AGENT_STATE_DIR"] = str(base / "client")
            for root, name, token in (("client", "offline", "offline"), ("host", "live", "live")):
                profiles = base / root / "connections"
                profiles.mkdir(parents=True)
                (profiles / (name + ".json")).write_text(json.dumps({
                    "bridge_url": "http://127.0.0.1:27124", "bridge_token": token, "vault_id": name,
                }), encoding="utf-8")
            def probe(config):
                return {"connected": config["bridge_token"] == "live"}
            with patch("runtime_config.default_state_directory", return_value=base / "host"), patch("runtime_config.probe_connection", side_effect=probe):
                self.assertEqual(load_connection()["vault_id"], "live")
                (base / "client/connection.json").write_text(json.dumps({"bridge_token": "explicit-offline"}), encoding="utf-8")
                self.assertEqual(load_connection()["bridge_token"], "explicit-offline")
                (base / "client/connection.json").write_text('{"connection_id":"unknown"}', encoding="utf-8")
                with self.assertRaises(ValueError):
                    load_connection()
                (base / "client/connection.json").unlink()
                with patch("runtime_config.probe_connection", return_value={"connected": True}):
                    with self.assertRaises(ConnectionSelectionRequired):
                        load_connection()

    def test_environment_binding_never_automatically_adopts_a_profile(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            os.environ.pop("EXCALIDRAW_AGENT_CONFIG", None)
            os.environ["EXCALIDRAW_AGENT_STATE_DIR"] = tmp
            os.environ["EXCALIDRAW_BRIDGE_TOKEN"] = "explicit-env"
            with patch("runtime_config.connection_profiles", side_effect=AssertionError("must not discover")):
                self.assertEqual(load_connection(), {})

    def test_review_ledger_survives_a_working_directory_change(self) -> None:
        with tempfile.TemporaryDirectory() as state_tmp, tempfile.TemporaryDirectory() as foreign_cwd:
            os.environ["EXCALIDRAW_AGENT_STATE_DIR"] = state_tmp
            ledger = ReviewLedger("ctx-stable-cwd-token")
            ledger.record_round("r1", "p1", False, check_result={"status": "pass"})
            orig_cwd = os.getcwd()
            try:
                os.chdir(foreign_cwd)
                loaded = ReviewLedger("ctx-stable-cwd-token")
                result = loaded.record_round("r2", "p2", True, check_result={"status": "pass"},
                                             visual_checks={"content": "pass", "readability": "pass", "occlusion": "pass"})
                self.assertEqual(result["round"], 2)
                self.assertEqual(result["status"], "completed")
            finally:
                os.chdir(orig_cwd)


if __name__ == "__main__":
    unittest.main()
