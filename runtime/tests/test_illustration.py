"""Behavioral projection, physical relationships, routing and identity regressions."""

import copy
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from drawing_entry import diagram_type
from illustration_geometry import plan_geometry, project
from illustration_contract import check_illustration, projected_overlap_pairs
from geometry_diagnostics import run_geometry_diagnostics
from operation_schema import validate_operations
from scene_dsl.session import plan_update, fingerprint


def native(operations):
    rows = []
    for op in operations:
        if op["op"] == "group":
            continue
        e = {
            k: copy.deepcopy(v)
            for k, v in op.items()
            if k not in ("op", "ref", "style", "kind", "closed")
        }
        e.update(op.get("style", {}))
        e["id"] = op["ref"]
        e["type"] = op.get("type", op.get("kind", "line"))
        if "points" in e:
            e["width"] = max(p[0] for p in e["points"]) - min(p[0] for p in e["points"])
            e["height"] = max(p[1] for p in e["points"]) - min(
                p[1] for p in e["points"]
            )
        rows.append(e)
    return rows


def spec():
    return {
        "purpose": "Understand layers",
        "views": [{"id": "v", "method": "oblique", "description": "oblique stack"}],
        "objects": [
            {"id": "base", "role": "support", "views": ["v"]},
            {"id": "die", "role": "compute", "views": ["v"]},
        ],
        "relations": [{"kind": "supported_by", "source": "die", "target": "base"}],
        "illustrative_limits": ["Not to scale"],
    }


def solids(die_z=10):
    base = plan_geometry(
        {
            "kind": "projected_box",
            "id": "base",
            "viewId": "v",
            "x": -100,
            "y": 200,
            "width": 200,
            "depth": 100,
            "height": 10,
        },
        {},
    )
    die = plan_geometry(
        {
            "kind": "projected_box",
            "id": "die",
            "viewId": "v",
            "x": -100,
            "y": 200,
            "u": 40,
            "v": 20,
            "z": die_z,
            "width": 80,
            "depth": 50,
            "height": 20,
        },
        {},
    )
    return native(base["operations"] + die["operations"])


class IllustrationTests(unittest.TestCase):
    def test_physical_view_not_subject_decides_contract(self):
        for request in (
            "硬件封装结构爆炸图",
            "CPU封装剖面讲解图",
            "FOWLP 2.5D封装分层与剖面讲解图",
        ):
            self.assertEqual(diagram_type(request), "physical_structure")
        self.assertEqual(
            diagram_type("CPU ALU datapath", "general"), "microarchitecture"
        )
        self.assertEqual(diagram_type("逻辑门电路 PPT", "explanatory_page"), "circuit")
        self.assertEqual(diagram_type("PPT 对比讲解页"), "explanatory_page")

    def test_projection_and_stable_layer_identity(self):
        self.assertEqual(project([-100, 200], [0.6, -0.4], 40, 50, 30), [-30, 150])
        item = {
            "kind": "layer_stack",
            "id": "hbm",
            "view": "oblique",
            "x": -100,
            "y": 200,
            "width": 80,
            "depth": 50,
            "layers": [{"id": "d0", "height": 10}, {"id": "d1", "height": 10}],
        }
        a = plan_geometry(item, {})
        b = plan_geometry(
            {
                **item,
                "layers": [
                    {"id": "d0", "height": 15},
                    {"id": "d1", "height": 10},
                    {"id": "d2", "height": 10},
                ],
            },
            {},
        )
        self.assertEqual(
            {op["ref"] for op in a["operations"]},
            {op["ref"] for op in b["operations"] if ":d2:" not in op["ref"]},
        )
        self.assertEqual(b["manifest"]["objects"][1]["model"]["z"], 15)
        self.assertEqual(validate_operations(a["operations"]), a["operations"])

    def test_invalid_constructions_fail_instead_of_silent_truncation(self):
        for height in (0, -1, math.nan, True):
            with self.assertRaises(ValueError):
                plan_geometry(
                    {
                        "kind": "projected_box",
                        "id": "x",
                        "width": 10,
                        "depth": 10,
                        "height": height,
                    },
                    {},
                )
        with self.assertRaises(ValueError):
            plan_geometry(
                {
                    "kind": "layer_stack",
                    "id": "s",
                    "width": 10,
                    "layers": [{"id": "d", "height": 5}, {"id": "d", "height": 8}],
                },
                {},
            )
        with self.assertRaises(ValueError):
            plan_geometry(
                {
                    "kind": "grid_array",
                    "id": "a",
                    "rows": 201,
                    "cols": 1,
                    "pitch": [20, 20],
                    "size": [10, 10],
                },
                {},
            )
        with self.assertRaises(ValueError):
            plan_geometry(
                {
                    "kind": "grid_array",
                    "id": "a",
                    "rows": 2,
                    "cols": 2,
                    "projection": [0.1, -0.1],
                    "pitch": [10, 10],
                    "size": [8, 8],
                },
                {},
            )
        with self.assertRaises(ValueError):
            plan_geometry(
                {
                    "kind": "leader",
                    "id": "l",
                    "points": [[0, 0], [10, 10]],
                    "target": [15, 15],
                },
                {},
            )

    def test_legal_projection_overlap_not_model_interpenetration_or_text_waiver(self):
        rows = solids()
        self.assertEqual(check_illustration(rows, spec()), [])
        pairs = projected_overlap_pairs(rows, spec())
        self.assertTrue(
            any("die" in str(pair) and "base" in str(pair) for pair in pairs)
        )
        bad = solids(5)
        self.assertIn(
            "ILLUSTRATION_INTERPENETRATION",
            {i["code"] for i in check_illustration(bad, spec())},
        )
        self.assertIn(
            "ILLUSTRATION_PHYSICAL_RELATION",
            {i["code"] for i in check_illustration(bad, spec())},
        )
        rows.extend(
            [
                {
                    "id": "text-a",
                    "type": "text",
                    "x": 0,
                    "y": 0,
                    "width": 100,
                    "height": 20,
                    "fontSize": 20,
                    "text": "Label",
                },
                {
                    "id": "text-b",
                    "type": "text",
                    "x": 0,
                    "y": 0,
                    "width": 100,
                    "height": 20,
                    "fontSize": 20,
                    "text": "Other",
                },
            ]
        )
        self.assertIn(
            "TEXT_TEXT_OVERLAP",
            {
                i["code"]
                for i in run_geometry_diagnostics(rows, visual_plan=spec())["issues"]
            },
        )
        rows[3]["x"] += 30
        self.assertIn(
            "ILLUSTRATION_GEOMETRY_CHANGED",
            {i["code"] for i in check_illustration(rows, spec())},
        )

    def test_incremental_layer_addition_patches_old_ids_and_external_edits_conflict(
        self,
    ):
        def plan(height, layers):
            ops = plan_geometry(
                {
                    "kind": "layer_stack",
                    "id": "s",
                    "view": "section",
                    "x": 0,
                    "y": 100,
                    "width": 100,
                    "layers": [
                        {"id": f"d{i}", "height": height} for i in range(layers)
                    ],
                },
                {},
            )["operations"]
            entities = {}
            for op in ops:
                op["customData"]["dsl"] = {"document": "example", "key": op["ref"]}
                entities[op["ref"]] = op
            return {
                "document": "example",
                "entities": entities,
                "post": [],
                "features": [],
                "routes": {},
            }

        old = plan(10, 2)
        elements = native(list(old["entities"].values()))
        state = {
            "document": "example",
            "file": "canvas",
            "ids": {e["id"]: e["id"] for e in elements},
            "snapshots": {e["id"]: fingerprint(e) for e in elements},
            "entities": old["entities"],
            "post": [],
            "features": [],
        }
        changed = plan_update(
            plan(12, 3), state, {"file": "canvas", "elements": elements}
        )
        self.assertEqual(changed["created"], ["s:d2"])
        self.assertEqual(set(changed["updated"]), {"s:d0", "s:d1"})
        self.assertFalse(changed["deleted"])
        self.assertFalse(any(op["op"] == "delete" for op in changed["operations"]))
        elements[0]["x"] += 1
        with self.assertRaises(ValueError):
            plan_update(plan(12, 3), state, {"file": "canvas", "elements": elements})

    def test_removed_array_member_and_single_row_spacing(self):
        array = plan_geometry(
            {
                "kind": "grid_array",
                "id": "vias",
                "objectId": "base",
                "viewId": "v",
                "rows": 1,
                "cols": 3,
                "pitch": [20, 5],
                "size": [4, 30],
            },
            {},
        )
        rows = native(array["operations"])
        plan = spec()
        plan["objects"] = plan["objects"][:1]
        plan["relations"] = []
        self.assertEqual(check_illustration(rows, plan), [])
        self.assertIn(
            "ILLUSTRATION_CONSTRUCTION_MISSING",
            {i["code"] for i in check_illustration(rows[:-1], plan)},
        )

    def test_invisible_native_bodies_do_not_satisfy_required_view_objects(self):
        rows = solids()
        for element in rows:
            element["opacity"] = 0
        self.assertIn(
            "ILLUSTRATION_OBJECT_MISSING",
            {i["code"] for i in check_illustration(rows, spec())},
        )
        for element in rows:
            element.update(
                opacity=100, strokeColor="transparent", backgroundColor="transparent"
            )
        self.assertIn(
            "ILLUSTRATION_OBJECT_MISSING",
            {i["code"] for i in check_illustration(rows, spec())},
        )

    def test_annotation_supports_do_not_waive_unrelated_body_or_text(self):
        from illustration_contract import annotation_object_ids

        rows = solids()
        allowed = annotation_object_ids(rows, "v", "die")
        self.assertIn("base:top", allowed)
        other = plan_geometry(
            {
                "kind": "projected_box",
                "id": "other",
                "viewId": "v",
                "x": -100,
                "y": 200,
                "u": 140,
                "v": 20,
                "z": 10,
                "width": 40,
                "depth": 50,
                "height": 20,
            },
            {},
        )
        rows.extend(native(other["operations"]))
        rows.append(
            {
                "id": "text",
                "type": "text",
                "customData": {
                    "technicalIllustration": {
                        "viewId": "v",
                        "objectId": "base",
                        "role": "label",
                    }
                },
            }
        )
        allowed = annotation_object_ids(rows, "v", "die")
        self.assertNotIn("other:top", allowed)
        self.assertNotIn("text", allowed)

    def test_polygon_crossing_uses_original_local_origin_and_visible_face(self):
        from geometry_diagnostics import (
            check_arrow_crossing,
            _segment_intersects_polygon,
        )

        body = {
            "id": "p",
            "type": "line",
            "x": 0,
            "y": 100,
            "width": 100,
            "height": 50,
            "points": [[0, 0], [100, 0], [100, -50], [0, -50], [0, 0]],
            "polygon": True,
        }
        outside = {
            "id": "out",
            "type": "arrow",
            "x": 10,
            "y": 30,
            "points": [[0, 0], [60, 0]],
        }
        inside = {**outside, "id": "in", "y": 75}
        self.assertEqual(
            check_arrow_crossing([body, outside], {"p": body, "out": outside}), []
        )
        self.assertEqual(
            check_arrow_crossing([body, inside], {"p": body, "in": inside})[0]["code"],
            "ARROW_CROSSES_NODE",
        )
        square = [(0, 0), (100, 0), (100, 100), (0, 100)]
        self.assertTrue(_segment_intersects_polygon((-10, 50), (110, 50), square))
        self.assertFalse(
            _segment_intersects_polygon((-10, 50), (110, 50), square, [square])
        )


if __name__ == "__main__":
    unittest.main()
