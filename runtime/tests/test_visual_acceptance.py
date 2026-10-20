"""Behavioral visual-conflict and acceptance transitions; no renderer mocks."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from acceptance import decorate, triage
from geometry_diagnostics import run_geometry_diagnostics
from review_ledger import ReviewLedger
from visual_diagnostics import inspect_visual_conflicts, output_readability

CHECKS = {name: "pass" for name in ("content", "readability", "occlusion", "connections", "hierarchy_style")}


def text(identity="t", x=20, y=20, **extra):
    return {"id": identity, "type": "text", "x": x, "y": y, "width": 100, "height": 24,
            "text": "Readable label", "fontSize": 20, **extra}


def panel(identity="p", **extra):
    return {"id": identity, "type": "rectangle", "x": 0, "y": 0, "width": 160, "height": 90,
            "backgroundColor": "#ffffff", "fillStyle": "solid", **extra}


def line(identity="l", y=32, **extra):
    return {"id": identity, "type": "line", "x": 0, "y": y, "width": 160, "height": 0,
            "points": [[0, 0], [160, 0]], "strokeWidth": 2, **extra}


class VisualConflictTests(unittest.TestCase):
    def codes(self, elements):
        return {i["code"] for i in inspect_visual_conflicts(elements)}

    def test_large_background_below_text_is_legal(self):
        self.assertEqual(inspect_visual_conflicts([panel(), text()]), [])

    def test_opaque_panel_after_text_is_not_a_legal_background(self):
        self.assertIn("TEXT_PAINTED_OVER", self.codes([text(), panel()]))

    def test_transparent_panel_does_not_paint_over_its_text(self):
        self.assertEqual(inspect_visual_conflicts([text(), panel(backgroundColor="transparent")]), [])

    def test_transparent_border_cutting_text_is_a_risk(self):
        self.assertIn("BORDER_THROUGH_TEXT", self.codes([panel(x=60, backgroundColor="transparent"), text()]))

    def test_text_collision_not_exempted_by_common_group(self):
        self.assertIn("TEXT_TEXT_OVERLAP", self.codes([text(groupIds=["same"]), text("other", x=60, groupIds=["same"])]))

    def test_native_line_through_unbound_text_is_detected(self):
        self.assertIn("LINE_THROUGH_TEXT", self.codes([line(), text()]))
        self.assertIn("LINE_THROUGH_TEXT", self.codes([text(), line()]))

    def test_real_opaque_panel_between_line_and_text_masks_crossing(self):
        self.assertEqual(inspect_visual_conflicts([line(), panel(), text()]), [])

    def test_translucent_panel_is_not_assumed_to_mask_line(self):
        self.assertIn("LINE_THROUGH_TEXT", self.codes([line(), panel(opacity=50), text()]))

    def test_own_arrow_label_mask_does_not_exempt_another_line(self):
        arrow = line("arrow", type="arrow", boundElements=[{"id": "t", "type": "text"}])
        label = text(containerId="arrow")
        self.assertEqual(inspect_visual_conflicts([arrow, label]), [])
        issues = inspect_visual_conflicts([arrow, line("unrelated"), label])
        self.assertEqual([i["elementIds"] for i in issues], [["unrelated", "t"]])

    def test_text_bands_leave_blank_lines_unoccupied(self):
        label = text(text="First\n\nThird", height=72)
        self.assertNotIn("LINE_THROUGH_TEXT", self.codes([line(y=55), label]))

    def test_touching_text_boxes_are_not_collisions(self):
        self.assertNotIn("TEXT_TEXT_OVERLAP", self.codes([text(), text("b", x=120)]))

    def test_hidden_or_deleted_elements_do_not_occlude(self):
        self.assertEqual(inspect_visual_conflicts([line(customData={"hide": True}), text(), panel(isDeleted=True)]), [])

    def test_group_and_container_flags_cannot_hide_line_text_risk(self):
        self.assertIn("LINE_THROUGH_TEXT", self.codes([line(customData={"isContainer": True}), text()]))

    def test_unbound_nonintersecting_arrows_are_legal_at_high(self):
        result = run_geometry_diagnostics([line(type="arrow", y=100), text()], acceptance_level="high")
        self.assertEqual(result["status"], "pass")

    def test_medium_and_high_block_line_text_but_low_discloses_it(self):
        for grade in ("medium", "high"):
            result = run_geometry_diagnostics([line(), text()], acceptance_level=grade)
            self.assertEqual(result["status"], "fail")
            self.assertTrue(next(i for i in result["issues"] if i["code"] == "LINE_THROUGH_TEXT")["blocking"])
        result = run_geometry_diagnostics([line(), text()], acceptance_level="low")
        self.assertEqual(result["status"], "pass")
        self.assertFalse(result["issues"][0]["blocking"])

    def test_output_font_trigger_uses_scale_and_does_not_invent_geometry(self):
        self.assertEqual(output_readability([text()], 1), [])
        issue = output_readability([text()], .3)[0]
        self.assertEqual(issue["actual"]["minimumOutputFontPx"], 6)
        blocking, advisory = triage([issue], "high")
        self.assertEqual(blocking, [])
        self.assertEqual(advisory[0]["code"], "SMALL_OUTPUT_TEXT")

    def test_structural_reference_error_never_waived_by_level(self):
        for grade in ("low", "medium", "high"):
            result = run_geometry_diagnostics([line(type="arrow", startBinding={"elementId": "absent"})], acceptance_level=grade)
            self.assertEqual(result["status"], "fail")

    def test_wide_arrow_shaft_can_intersect_text_without_centerline_crossing(self):
        arrow = line(type="arrow", y=50, endArrowhead="block_arrow", customData={"blockArrowWidth": 40})
        self.assertIn("LINE_THROUGH_TEXT", self.codes([arrow, text()]))

    def test_arrow_label_over_a_background_is_not_an_occlusion(self):
        arrow = line("arrow", type="arrow", y=100, boundElements=[{"id": "t", "type": "text"}])
        result = run_geometry_diagnostics([panel(), arrow, text(containerId="arrow")])
        self.assertFalse(any(i["code"] == "ARROW_LABEL_OCCLUSION" for i in result["issues"]))


class TieredReviewTests(unittest.TestCase):
    def ledger(self, directory, grade=None, rounds=None):
        return ReviewLedger("ctx-tier-regression", str(Path(directory) / "review.json"), max_rounds=rounds, acceptance_level=grade)

    def test_medium_default_needs_explicit_visual_checks(self):
        with tempfile.TemporaryDirectory() as directory:
            ledger = self.ledger(directory)
            first = ledger.record_round("r1", "p1", True, check_result={"status": "pass"})
            self.assertEqual(first["acceptanceLevel"], "medium")
            self.assertEqual(first["status"], "continue")
            self.assertEqual({i["check"] for i in first["unresolvedIssues"]}, {"content", "readability", "occlusion"})
            second = ledger.record_round("r1", "p2", True, check_result={"status": "pass"}, visual_checks=CHECKS)
            self.assertEqual(second["status"], "completed")

    def test_low_remains_light_but_requires_actual_visual_review(self):
        with tempfile.TemporaryDirectory() as directory:
            ledger = self.ledger(directory, "low")
            self.assertEqual(ledger.record_round("r1", "p1", False, check_result={"status": "pass"})["status"], "continue")
            self.assertEqual(ledger.record_round("r1", "p2", True, check_result={"status": "pass"})["status"], "completed")

    def test_high_choice_and_expectations_survive_reload(self):
        with tempfile.TemporaryDirectory() as directory:
            first = self.ledger(directory, "high")
            first.expected = [{"type": "node_exists", "id": "important"}]
            first.save()
            loaded = self.ledger(directory)
            self.assertEqual(loaded.acceptance_level, "high")
            self.assertEqual(loaded.expected, first.expected)
            result = loaded.record_round("r", "p", True, check_result={"status": "pass"}, visual_checks={k: "pass" for k in ("content", "readability", "occlusion")})
            self.assertEqual({i["check"] for i in result["unresolvedIssues"]}, {"connections", "hierarchy_style"})

    def test_specific_visual_false_positive_retains_original_finding(self):
        issue = {"code": "TEXT_TEXT_OVERLAP", "severity": "error", "elementIds": ["a", "b"]}
        identity = decorate([issue], "medium")[0]["issueId"]
        with tempfile.TemporaryDirectory() as directory:
            ledger = self.ledger(directory)
            result = ledger.record_round("r", "p", True, check_result={"status": "fail", "issues": [issue]}, visual_checks=CHECKS,
                detail_preview_ids=["detail"], dispositions=[{"issue_id": identity, "element_ids": ["a", "b"], "preview_id": "detail",
                "decision": "false_positive", "reason": "Label a's trailing blank box intersects b's left padding; the readable detail confirms the actual glyphs remain separate."}])
            self.assertEqual(result["status"], "completed")
            self.assertEqual(result["advisories"][0]["code"], "TEXT_TEXT_OVERLAP")
            self.assertEqual(ledger.rounds[0]["hardIssues"], [issue])

    def test_structural_or_semantic_failure_cannot_be_adjudicated(self):
        for code in ("DANGLING_START_BINDING", "SEMANTIC_ASSERTION_FAILED"):
            issue = {"code": code, "severity": "error", "elementIds": ["a"]}
            identity = decorate([issue], "high")[0]["issueId"]
            with tempfile.TemporaryDirectory() as directory:
                with self.assertRaises(ValueError):
                    self.ledger(directory, "high").record_round("r", "p", True, check_result={"status": "fail", "issues": [issue]}, visual_checks=CHECKS,
                        dispositions=[{"issue_id": identity, "element_ids": ["a"], "preview_id": "p",
                                       "decision": "intentional", "reason": "Not a geometry decision"}])

    def test_stale_or_global_disposition_does_not_silence_findings(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                self.ledger(directory).record_round("r", "p", True, check_result={"status": "pass"}, visual_checks=CHECKS,
                    dispositions=[{"issue_id": "all", "element_ids": ["a"], "preview_id": "p", "decision": "intentional", "reason": "Ignore all overlaps"}])

    def test_explicit_failed_visual_check_blocks_even_with_empty_issue_list(self):
        with tempfile.TemporaryDirectory() as directory:
            checks = {**CHECKS, "readability": "fail"}
            result = self.ledger(directory).record_round("r", "p", True, check_result={"status": "pass"}, visual_checks=checks)
            self.assertEqual(result["status"], "continue")
            self.assertEqual(result["unresolvedIssues"][0]["code"], "VISUAL_CHECK_FAILED")

    def test_present_text_cannot_skip_readability_as_not_applicable(self):
        check = run_geometry_diagnostics([text()], acceptance_level="medium")
        with tempfile.TemporaryDirectory() as directory:
            result = self.ledger(directory).record_round("r", "p", True, check_result=check,
                visual_checks={**CHECKS, "readability": "not_applicable"})
            self.assertNotEqual(result["status"], "completed")
            self.assertEqual(result["unresolvedIssues"][0]["check"], "readability")

    def test_precheck_settings_do_not_lock_out_explicit_smaller_budget(self):
        with tempfile.TemporaryDirectory() as directory:
            self.ledger(directory).save()
            ledger = self.ledger(directory, rounds=1)
            result = ledger.record_round("r", "p", True, check_result={"status": "unknown"}, visual_checks=CHECKS)
            self.assertEqual(result["status"], "needs_attention")
            self.assertEqual(result["maxRounds"], 1)

    def test_unknown_geometry_can_be_accepted_only_with_specific_visual_evidence(self):
        check = run_geometry_diagnostics([panel(angle=.3)], acceptance_level="high")
        candidate = check["unsupportedChecks"][0]
        with tempfile.TemporaryDirectory() as directory:
            ledger = self.ledger(directory, "high")
            result = ledger.record_round("r", "p", True, check_result=check, visual_checks=CHECKS,
                dispositions=[{"issue_id": candidate["issueId"], "element_ids": [candidate["elementId"]], "preview_id": "p",
                               "decision": "intentional", "reason": "The current PNG shows p as an isolated rotated decoration with no neighboring content."}])
            self.assertEqual(result["status"], "completed")
            self.assertEqual(result["advisories"][0]["code"], "UNSUPPORTED_GEOMETRY")

    def test_repeated_reason_cannot_waive_all_text_findings(self):
        issues = [{"code": "TEXT_TEXT_OVERLAP", "elementIds": ["a", other], "severity": "error"} for other in ("b", "c")]
        decisions = [{"issue_id": i["issueId"], "element_ids": i["elementIds"], "preview_id": "detail",
                      "decision": "false_positive", "reason": "All labels inspected and legible"} for i in decorate(issues, "medium")]
        with self.assertRaisesRegex(ValueError, "Repeated"):
            triage(issues, "medium", decisions)

    def test_text_conflict_cannot_be_intentional_even_with_specific_ids(self):
        issue = {"code": "LINE_THROUGH_TEXT", "elementIds": ["wire", "label"], "severity": "warning"}
        decision = {"issue_id": decorate([issue], "medium")[0]["issueId"], "element_ids": ["wire", "label"],
                    "preview_id": "detail", "decision": "intentional", "reason": "The wire intentionally crosses this label"}
        with self.assertRaisesRegex(ValueError, "not intentional"):
            triage([issue], "medium", [decision])

    def test_text_false_positive_requires_current_detail_evidence(self):
        issue = {"code": "TEXT_TEXT_OVERLAP", "elementIds": ["a", "b"], "severity": "error"}
        decision = {"issue_id": decorate([issue], "medium")[0]["issueId"], "element_ids": ["a", "b"],
                    "preview_id": "overview", "decision": "false_positive", "reason": "Only blank box padding intersects"}
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "detail PNG"):
                self.ledger(directory).record_round("r", "overview", True,
                    check_result={"status": "fail", "issues": [issue]}, visual_checks=CHECKS, dispositions=[decision])

    def test_disposition_cannot_substitute_unrelated_element_ids(self):
        issue = {"code": "BODY_OVERLAP", "elementIds": ["a", "b"], "severity": "error"}
        decision = {"issue_id": decorate([issue], "medium")[0]["issueId"], "element_ids": ["decoration"],
                    "preview_id": "p", "decision": "intentional", "reason": "An isolated layered decoration"}
        with self.assertRaisesRegex(ValueError, "exactly match"):
            triage([issue], "medium", [decision])


if __name__ == "__main__":
    unittest.main()
