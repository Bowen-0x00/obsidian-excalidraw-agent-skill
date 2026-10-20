"""Behavioral gates: user choices, task identity, content coverage and rebind budgets."""
from __future__ import annotations

import copy
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from drawing_client import DrawingClient
from drawing_workflow import (attach_context, for_context, require_context, requirement_issues,
                              reserve_create, validate_brief)


def brief(task="comparison"):
    return {"task_id": task, "preferences": {
        name: {"value": value, "source": "answer", "evidence": "Explicit user answer for " + name}
        for name, value in {"style": "professional", "review": "high", "palette": "blue/green",
                            "background": "white", "font": "clear body with emphasized titles"}.items()},
        "requirements": [{"id": "baseline", "description": "Baseline and proposed hardware shown separately"},
                         {"id": "precision", "description": "State the precision-preservation conditions"}]}


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.environment = patch.dict(os.environ, {"EXCALIDRAW_AGENT_STATE_DIR": self.directory.name,
                                                   "EXCALIDRAW_AGENT_CONFIG": str(Path(self.directory.name) / "connection.json")})
        self.environment.start()
        self.addCleanup(self.environment.stop)
        Path(self.directory.name, "connection.json").write_text(json.dumps({"mode": "remote", "host_vault_path": "host-vault"}))

    def attach(self, token="ctx-a", task="comparison", file="comparison.excalidraw.md"):
        value = brief(task)
        attach_context({"file": file, "contextToken": token}, value)
        return value

    def test_missing_review_cannot_be_inferred_from_style_choice(self):
        value = brief()
        del value["preferences"]["review"]
        with self.assertRaisesRegex(ValueError, "PREFERENCES_REQUIRED"):
            validate_brief(value)
        self.assertFalse((Path(self.directory.name) / "artifacts").exists())

    def test_unanswered_or_uncited_preference_is_not_a_resolved_choice(self):
        for field, value in (("source", "recommended"), ("evidence", ""), ("value", "")):
            proposal = brief()
            proposal["preferences"]["review"][field] = value
            with self.assertRaises(ValueError):
                validate_brief(proposal)

    def test_same_task_cannot_recreate_canvas_after_unknown_outcome(self):
        reserve_create(brief())
        with self.assertRaisesRegex(ValueError, "TASK_ALREADY_STARTED"):
            reserve_create(brief())

    def test_task_cannot_move_to_another_file_or_silently_replace_requirements(self):
        value = self.attach()
        with self.assertRaisesRegex(ValueError, "TASK_CANVAS_CONFLICT"):
            attach_context({"file": "new.excalidraw.md", "contextToken": "ctx-new"}, value)
        changed = copy.deepcopy(value)
        changed["requirements"] = changed["requirements"][:1]
        with self.assertRaises(ValueError):
            attach_context({"file": "comparison.excalidraw.md", "contextToken": "ctx-b"}, changed)

    def test_rebind_preserves_failed_review_budget_and_selected_level(self):
        self.attach()
        client = DrawingClient("http://127.0.0.1:1", "private", 1)
        first = client.review_settings("ctx-a", max_rounds=1)
        first.record_round("r1", "p1", True, check_result={"status": "unknown"},
                           visual_checks={name: "pass" for name in ("content", "readability", "occlusion", "connections", "hierarchy_style")})
        first.save()
        attach_context({"file": "comparison.excalidraw.md", "contextToken": "ctx-b"})
        loaded = client.review_settings("ctx-b")
        self.assertEqual(loaded.status, "needs_attention")
        self.assertEqual(loaded.max_rounds, 1)
        with self.assertRaises(ValueError):
            loaded.record_round("r2", "p2", True, check_result={"status": "pass"})
        with self.assertRaisesRegex(ValueError, "REVIEW_CHOICE_CONFLICT"):
            client.review_settings("ctx-b", "low")
        with self.assertRaisesRegex(ValueError, "CANVAS_TASK_CONFLICT"):
            self.attach("ctx-c", task="renamed-to-bypass")

    def test_completed_request_allows_explicit_new_edit_task_but_revokes_old_binding(self):
        self.attach()
        client = DrawingClient("http://127.0.0.1:1", "private", 1)
        ledger = client.review_settings("ctx-a")
        ledger.record_round("r1", "p1", True, check_result={"status": "pass"},
                            visual_checks={name: "pass" for name in ("content", "readability", "occlusion", "connections", "hierarchy_style")})
        ledger.save()
        self.attach("ctx-b", task="new-user-label-edit")
        self.assertIsNone(for_context("ctx-a"))
        self.assertEqual(require_context("ctx-b")["brief"]["task_id"], "new-user-label-edit")

    def test_requirement_coverage_needs_every_user_item_and_current_native_ids(self):
        required = brief()["requirements"]
        checks = [{"requirement_id": "baseline", "outcome": "pass", "element_ids": ["base", "ours"],
                   "evidence": "Separate left baseline and right proposed components"}]
        issues = requirement_issues(required, checks, {"base", "ours", "conditions"})
        self.assertEqual([i["requirementId"] for i in issues], ["precision"])
        checks.append({"requirement_id": "precision", "outcome": "pass", "element_ids": ["conditions"],
                       "evidence": "Conditions label states supported input range and rounding assumption"})
        self.assertEqual(requirement_issues(required, checks, {"base", "ours", "conditions"}), [])
        with self.assertRaisesRegex(ValueError, "current native"):
            requirement_issues(required, checks, {"base", "ours"})

    def test_tunnel_alias_change_does_not_reset_task_ownership(self):
        self.attach()
        config = Path(self.directory.name, "connection.json")
        config.write_text(json.dumps({"mode": "remote", "host_vault_path": "host-vault",
                                      "remote_host": "new-route", "bridge_url": "http://127.0.0.1:29000"}))
        attach_context({"file": "comparison.excalidraw.md", "contextToken": "ctx-b"})
        self.assertEqual(require_context("ctx-a")["brief"], require_context("ctx-b")["brief"])


if __name__ == "__main__":
    unittest.main()
