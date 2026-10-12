"""Consumer-visible geometry and review-budget regressions; no Obsidian mocks."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

_RUNTIME_DIR = str(Path(__file__).resolve().parents[1])
if _RUNTIME_DIR not in sys.path:
    sys.path.insert(0, _RUNTIME_DIR)

from geometry_diagnostics import run_geometry_diagnostics
from review_ledger import ReviewLedger
from diagram_layout import _point


class GeometryRegressionTests(unittest.TestCase):
    def test_bound_arrow_label_is_not_fitted_into_zero_height_arrow(self):
        elements = [
            {"id": "arrow", "type": "arrow", "x": 0, "y": 40, "width": 180, "height": 0,
             "points": [[0, 0], [180, 0]], "boundElements": [{"id": "label", "type": "text"}]},
            {"id": "label", "type": "text", "x": 65, "y": 28, "width": 50, "height": 24,
             "text": "处理", "containerId": "arrow"},
        ]
        result = run_geometry_diagnostics(elements)
        self.assertEqual(result["status"], "pass")
        self.assertFalse(any(issue["code"] == "TEXT_OUTSIDE_CONTAINER" for issue in result["issues"]))

    def test_native_relationship_failure_prevents_passing_geometry(self):
        result = run_geometry_diagnostics([], structural_validation={
            "valid": False, "errors": [{"code": "ORPHAN_FRAME_CHILD", "elementId": "child", "relatedId": "missing"}],
        })
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["issues"][0]["elementIds"], ["child", "missing"])

    def test_orthogonal_arrow_reports_actual_obstacle_not_generic_unknown(self):
        elements = [
            {"id": "arrow", "type": "arrow", "x": 0, "y": 20, "width": 100, "height": 80,
             "elbowed": True, "points": [[0, 0], [100, 0], [100, 80]]},
            {"id": "obstacle", "type": "rectangle", "x": 40, "y": 0, "width": 30, "height": 40},
        ]
        result = run_geometry_diagnostics(elements)
        self.assertEqual(result["status"], "fail")
        self.assertTrue(any(issue["code"] == "ARROW_CROSSES_NODE" for issue in result["issues"]))
        self.assertEqual(result["unsupportedChecks"], [])

    def test_required_branch_label_is_checked_not_only_edge_direction(self):
        elements = [
            {"id": "start", "type": "rectangle", "x": 0, "y": 0, "width": 80, "height": 40,
             "boundElements": [{"id": "edge", "type": "arrow"}]},
            {"id": "end", "type": "rectangle", "x": 180, "y": 0, "width": 80, "height": 40,
             "boundElements": [{"id": "edge", "type": "arrow"}]},
            {"id": "edge", "type": "arrow", "x": 80, "y": 20, "width": 100, "height": 0,
             "points": [[0, 0], [100, 0]], "startBinding": {"elementId": "start"}, "endBinding": {"elementId": "end"}},
        ]
        expected = [{"type": "edge_label", "from": "start", "to": "end", "text": "通过"}]
        before = run_geometry_diagnostics(elements, expected=expected)
        self.assertEqual(before["status"], "fail")
        elements[2]["boundElements"] = [{"id": "label", "type": "text"}]
        elements.append({"id": "label", "type": "text", "x": 120, "y": 8, "width": 40, "height": 24,
                         "text": "通过", "containerId": "edge"})
        after = run_geometry_diagnostics(elements, expected=expected)
        self.assertEqual(after["status"], "pass")

    def test_wrapping_preserves_full_label_content_but_truncation_fails(self):
        text = {"id": "label", "type": "text", "text": "身份真实性、权限范围\n与资源使用条件"}
        expected = [{"type": "label_equals", "id": "label", "text": "身份真实性、权限范围与资源使用条件"}]
        self.assertEqual(run_geometry_diagnostics([text], expected=expected)["status"], "pass")
        text["text"] = "身份真实性、权限范围..."
        self.assertEqual(run_geometry_diagnostics([text], expected=expected)["status"], "fail")

    def test_library_internal_overlay_is_legal_but_external_overlap_is_not(self):
        elements = [
            {"id": "base", "type": "rectangle", "x": 0, "y": 0, "width": 100, "height": 80,
             "customData": {"agentLibrary": {"instanceId": "item-one"}}},
            {"id": "decoration", "type": "rectangle", "x": 10, "y": 10, "width": 80, "height": 60,
             "customData": {"agentLibrary": {"instanceId": "item-one"}}},
        ]
        self.assertEqual(run_geometry_diagnostics(elements)["status"], "pass")
        elements.append({"id": "unrelated", "type": "rectangle", "x": 30, "y": 20, "width": 50, "height": 50,
                         "customData": {"agentLibrary": {"instanceId": "another-item"}}})
        diagnostics = run_geometry_diagnostics(elements)
        self.assertTrue(any(issue["code"] == "BODY_OVERLAP" and "unrelated" in issue["elementIds"] for issue in diagnostics["issues"]))

    def test_shared_group_does_not_make_body_overlap_intentional(self):
        elements = [
            {"id": "a", "type": "rectangle", "x": 0, "y": 0, "width": 80, "height": 60, "groupIds": ["group"]},
            {"id": "b", "type": "rectangle", "x": 20, "y": 10, "width": 80, "height": 60, "groupIds": ["group"]},
        ]
        self.assertEqual(run_geometry_diagnostics(elements)["status"], "fail")

    def test_endpoint_ratio_preserves_negative_scene_coordinates_and_separate_ports(self):
        box = {"x": -100, "y": -30, "width": 80, "height": 40}
        self.assertEqual(_point(box, "left", [0, 0.25]), (-100, -20))
        self.assertEqual(_point(box, "left", [0, 0.75]), (-100, 0))
        with self.assertRaises(ValueError):
            _point(box, "left", [0, float("nan")])


class ReviewBudgetRegressionTests(unittest.TestCase):
    def make_ledger(self, directory, rounds=5):
        return ReviewLedger("ctx-isolated-regression", str(Path(directory) / "review.json"), max_rounds=rounds)

    def test_complete_requires_real_visual_and_hard_check_attestations(self):
        with tempfile.TemporaryDirectory() as directory:
            ledger = self.make_ledger(directory)
            first = ledger.record_round("r1", "p1", False, check_result={"status": "pass"})
            self.assertEqual(first["status"], "continue")
            second = ledger.record_round("r1", "p2", True, check_result={"status": "pass"})
            self.assertEqual(second["status"], "completed")
            with self.assertRaises(ValueError):
                ledger.record_round("r1", "p2", True, check_result={"status": "pass"})

    def test_unknown_or_incomplete_cannot_bypass_round_limit(self):
        for check, complete in (({"status": "unknown"}, True), ({"status": "pass"}, False)):
            with self.subTest(check=check, complete=complete), tempfile.TemporaryDirectory() as directory:
                ledger = self.make_ledger(directory, rounds=2)
                self.assertEqual(ledger.record_round("r1", "p1", True, check_result=check, preview_complete=complete)["status"], "continue")
                self.assertEqual(ledger.record_round("r2", "p2", True, check_result=check, preview_complete=complete)["status"], "needs_attention")
                with self.assertRaises(ValueError):
                    ledger.record_round("r3", "p3", True, check_result=check, preview_complete=complete)

    def test_two_non_improving_transitions_stop_and_survive_reload(self):
        with tempfile.TemporaryDirectory() as directory:
            ledger = self.make_ledger(directory)
            issues = [{"code": "LABEL_COLLISION", "elementIds": ["a", "b"], "severity": "warning"}]
            for index in range(2):
                self.assertEqual(ledger.record_round(str(index), str(index), True, issues, check_result={"status": "pass"})["status"], "continue")
            loaded = self.make_ledger(directory)
            result = loaded.record_round("r3", "p3", True, issues, check_result={"status": "pass"})
            self.assertEqual(result["status"], "needs_attention")
            self.assertEqual(result["round"], 3)
            with self.assertRaises(ValueError):
                loaded.record_round("r4", "p4", True, [], check_result={"status": "pass"})


if __name__ == "__main__":
    unittest.main()
