"""Real ledger transitions must not become delivery evidence for another state."""
import copy
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from drawing_workflow import delivery_evidence, validate_brief
from drawing_entry import diagram_type
from review_ledger import ReviewLedger

CHECKS = {key: "pass" for key in ("content", "readability", "occlusion", "connections", "hierarchy_style")}


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.ledger = ReviewLedger("context", str(Path(self.temp.name) / "review.json"), acceptance_level="high")
        self.record = {"file": "diagram.excalidraw.md"}
        self.scene = {"file": "diagram.excalidraw.md", "revision": "r1"}
        self.receipt = {"file": "diagram.excalidraw.md", "revision": "r1", "previewId": "p1", "complete": True, "scope": "all"}

    def test_geometry_pass_without_visual_review_cannot_be_delivered(self):
        self.ledger.record_round("r1", "p1", False, check_result={"status": "pass"}, visual_checks=CHECKS)
        with self.assertRaisesRegex(ValueError, "DELIVERY_REVIEW_REQUIRED"):
            delivery_evidence(self.record, self.scene, self.receipt, self.ledger)

    def test_current_completed_review_allows_only_its_own_full_preview(self):
        self.ledger.record_round("r1", "p1", True, check_result={"status": "pass"}, visual_checks=CHECKS)
        last = delivery_evidence(self.record, self.scene, self.receipt, self.ledger)
        self.assertEqual(last["status"], "completed")
        for changed, code in (({"revision": "r0"}, "STALE_DELIVERY"), ({"file": "other.excalidraw.md"}, "STALE_DELIVERY"),
                              ({"previewId": "unreviewed"}, "DELIVERY_REVIEW_REQUIRED"), ({"scope": "ids"}, "INCOMPLETE_DELIVERY"),
                              ({"complete": False}, "INCOMPLETE_DELIVERY")):
            with self.subTest(changed=changed), self.assertRaisesRegex(ValueError, code):
                delivery_evidence(self.record, self.scene, {**self.receipt, **changed}, self.ledger)
        with self.assertRaisesRegex(ValueError, "STALE_DELIVERY"):
            delivery_evidence(self.record, {**self.scene, "revision": "r2"}, self.receipt, self.ledger)

    def test_later_failed_review_revokes_the_previous_completion(self):
        self.ledger.record_round("r1", "p1", True, check_result={"status": "pass"}, visual_checks=CHECKS)
        self.ledger.record_round("r2", "p2", True, check_result={"status": "fail", "issues": [{"code": "REQUIREMENT_NOT_VERIFIED", "severity": "error"}]}, visual_checks=CHECKS)
        with self.assertRaisesRegex(ValueError, "DELIVERY_REVIEW_REQUIRED"):
            delivery_evidence(self.record, self.scene, self.receipt, self.ledger)

    def test_hardware_routing_cannot_be_downgraded_by_general_type(self):
        self.assertEqual(diagram_type("Draw CPU datapath", "general"), "microarchitecture")
        self.assertEqual(diagram_type("画实际逻辑门电路"), "circuit")
        self.assertEqual(diagram_type("矩阵与转置"), "math")
        value = {"task_id": "cpu", "preferences": {key: {"value": "high" if key == "review" else "chosen", "source": "user", "evidence": "explicit user choice"}
                 for key in ("style", "review", "palette", "background", "font")},
                 "requirements": [{"id": "datapath", "description": "CPU ALU data path"}], "diagram_type": "general"}
        with self.assertRaisesRegex(ValueError, "REPRESENTATION_REQUIRED"):
            validate_brief(value)


if __name__ == "__main__":
    unittest.main()
