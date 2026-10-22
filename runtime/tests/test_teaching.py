"""Consumer-visible design/encoding failures and state transitions, not source snapshots."""

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from teaching_geometry import plan_teaching
from teaching_contract import (
    validate_teaching,
    check_teaching,
    expression_issues,
    design_options,
)
from drawing_entry import diagram_type
from acceptance import triage


def plan():
    return {
        "objective": "See retained tokens",
        "candidates": [
            {
                "id": "mask",
                "label": "Mask",
                "approach": "mechanism",
                "description": "Show token rows and visible cells",
            },
            {
                "id": "states",
                "label": "States",
                "approach": "mechanism",
                "description": "Show successive retained states",
            },
        ],
        "recommended": "mask",
        "selected": "mask",
        "reason": "Position explains visibility",
        "choice": {
            "source": "answer",
            "evidence": "User selected mask in the choice UI",
        },
        "goals": [
            {
                "id": "range",
                "requirement_id": "R1",
                "question": "Which tokens are visible?",
                "method": "sequence_window",
                "components": ["window"],
            }
        ],
    }


def native(item):
    construction = plan_teaching(item)
    rows = []
    for source in construction["operations"]:
        e = {
            k: copy.deepcopy(v)
            for k, v in source.items()
            if k not in ("op", "ref", "style", "kind")
        }
        e.update(source["style"])
        e["id"] = source["ref"]
        e["type"] = source.get("type", source.get("kind"))
        if e.get("points"):
            e.update(
                width=max(p[0] for p in e["points"]) - min(p[0] for p in e["points"]),
                height=max(p[1] for p in e["points"]) - min(p[1] for p in e["points"]),
            )
        rows.append(e)
    for label in construction["labels"]:
        rows.append(
            {
                "id": label["ref"],
                "type": "text",
                "text": label["text"],
                "customData": {
                    "teaching": {
                        "component": item["id"],
                        "kind": item["kind"],
                        "part": label["ref"][len(item["id"]) + 1 :],
                        "spec": construction["operations"][0]["customData"]["teaching"][
                            "spec"
                        ],
                    }
                },
            }
        )
    return rows


class TeachingTests(unittest.TestCase):
    def test_general_does_not_skip_teaching_design_and_choice(self):
        self.assertEqual(
            diagram_type("为每个Markdown画一个KV Cache图解", "general"), "teaching"
        )
        requirements = [{"id": "R1", "description": "画出注意力掩码与缓存保留范围"}]
        with self.assertRaisesRegex(ValueError, "TEACHING_PLAN_REQUIRED"):
            validate_teaching(None, requirements, True)
        proposal = plan()
        proposal.pop("selected")
        proposal.pop("choice")
        self.assertEqual(design_options(proposal)["recommended"], 0)
        with self.assertRaisesRegex(ValueError, "DESIGN_CHOICE_REQUIRED"):
            validate_teaching(proposal, requirements, True)
        validate_teaching(plan(), requirements, True)
        wrong = plan()
        wrong["goals"][0]["method"] = "flow"
        with self.assertRaises(ValueError):
            validate_teaching(wrong, requirements, True)
        empty_evidence = plan()
        empty_evidence["choice"]["evidence"] = "   "
        with self.assertRaises(ValueError):
            validate_teaching(empty_evidence, requirements, True)

    def test_paragraph_claiming_mask_is_not_mask_geometry(self):
        elements = [
            {
                "id": "paragraph",
                "type": "text",
                "text": "下三角 → 对角带；4个sink + 最近窗口",
            },
            {
                "id": "box",
                "type": "rectangle",
                "x": 0,
                "y": 0,
                "width": 500,
                "height": 100,
                "customData": {"agentDiagram": {"logicalId": "window"}},
            },
        ]
        issues = check_teaching(elements, plan())
        self.assertEqual(issues[0]["code"], "TEACHING_ENCODING_MISSING")
        self.assertEqual(
            check_teaching(elements, None, required=True)[0]["code"],
            "TEACHING_PLAN_REQUIRED",
        )
        self.assertEqual(check_teaching(elements, None), [])
        with self.assertRaises(ValueError):
            triage(
                issues,
                "high",
                [
                    {
                        "issue_id": __import__("acceptance").issue_id(issues[0]),
                        "decision": "intentional",
                        "element_ids": ["box"],
                        "reason": "Ignore diagram choice",
                        "preview_id": "p",
                    }
                ],
            )

    def test_window_state_mask_and_invisible_or_missing_parts_fail(self):
        item = {
            "kind": "sequence_window",
            "id": "window",
            "x": 0,
            "y": 0,
            "tokens": ["0", "1", "2", "3"],
            "window": 2,
            "sinks": 1,
            "step": 3,
            "show_mask": True,
        }
        rows = native(item)
        self.assertEqual(check_teaching(rows, plan()), [])
        token = next(e for e in rows if e["id"] == "window:token:1")
        old = token["backgroundColor"]
        token["backgroundColor"] = "#d8e8dc"
        self.assertIn(
            "TEACHING_ENCODING_CHANGED",
            {i["code"] for i in check_teaching(rows, plan())},
        )
        token["backgroundColor"] = old
        token["opacity"] = 0
        self.assertIn(
            "TEACHING_ENCODING_CHANGED",
            {i["code"] for i in check_teaching(rows, plan())},
        )
        rows = [e for e in rows if e["id"] != "window:mask:3:3"]
        self.assertIn(
            "TEACHING_PART_MISSING", {i["code"] for i in check_teaching(rows, plan())}
        )

    def test_matrix_groups_change_axis_not_values_and_bit_lengths_scale(self):
        values = [[1, 12], [2, 14]]
        column = plan_teaching(
            {"kind": "matrix_groups", "id": "m", "values": values, "group_by": "column"}
        )
        row = plan_teaching(
            {"kind": "matrix_groups", "id": "m", "values": values, "group_by": "row"}
        )
        self.assertEqual(
            [o["style"]["backgroundColor"] for o in column["operations"][:4]],
            [o["style"]["backgroundColor"] for o in row["operations"][:4]],
        )
        self.assertNotEqual(
            [
                (o["x"], o["y"], o["width"], o["height"])
                for o in column["operations"][4:]
            ],
            [(o["x"], o["y"], o["width"], o["height"]) for o in row["operations"][4:]],
        )
        bits = plan_teaching(
            {"kind": "bitwidth_compare", "id": "b", "count": 2, "bits": [16, 4]}
        )
        a = [o for o in bits["operations"] if ":bits:0:" in o["ref"]]
        b = [o for o in bits["operations"] if ":bits:1:" in o["ref"]]
        self.assertEqual(sum(o["width"] for o in a), 4 * sum(o["width"] for o in b))

    def test_mapping_rewire_and_token_reuse_are_observable(self):
        item = {
            "kind": "memory_map",
            "id": "pages",
            "mapping": [4, 1, 6],
            "physical_count": 8,
            "block_tokens": 4,
        }
        rows = native(item)
        p = plan()
        p["goals"][0].update(method="memory_map", components=["pages"])
        self.assertEqual(check_teaching(rows, p), [])
        wire = next(e for e in rows if e["id"] == "pages:map:0")
        wire["points"][-1][1] -= 20
        self.assertIn(
            "TEACHING_ENCODING_CHANGED", {i["code"] for i in check_teaching(rows, p)}
        )
        with self.assertRaises(ValueError):
            plan_teaching({**item, "mapping": [9]})
        with self.assertRaises(ValueError):
            plan_teaching(
                {
                    "kind": "time_steps",
                    "id": "t",
                    "tokens": ["A", "B"],
                    "steps": [{"id": "t1", "active": [0], "reused": [0]}],
                }
            )

    def test_expression_review_requires_encoded_ids_and_each_goal(self):
        item = {
            "kind": "sequence_window",
            "id": "window",
            "tokens": ["0", "1", "2"],
            "window": 2,
            "sinks": 1,
        }
        rows = native(item)
        self.assertEqual(
            expression_issues(plan(), None, rows)[0]["code"],
            "TEACHING_EXPRESSION_NOT_VERIFIED",
        )
        check = {
            "goal_id": "range",
            "outcome": "pass",
            "element_ids": ["window:token:0"],
            "observation": "Blue first cell and green suffix are separate",
            "without_prose": "Position shows a fixed prefix and moving suffix",
        }
        self.assertEqual(expression_issues(plan(), [check], rows), [])
        check["element_ids"] = ["window:token:0:label"]
        with self.assertRaisesRegex(ValueError, "actual native encoded objects"):
            expression_issues(plan(), [check], rows)


if __name__ == "__main__":
    unittest.main()
