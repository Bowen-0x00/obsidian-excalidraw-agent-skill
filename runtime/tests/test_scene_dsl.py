"""Behavioral contract tests; native rendering is separately smoke-exercised."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scene_dsl.model import DslError, load, validate
from scene_dsl.session import fingerprint, plan_update


class LanguageTests(unittest.TestCase):
    def doc(self):
        return {"version": 1, "id": "test", "nodes": {"a": {"label": "A", "ports": {"out": "right:0.3"}}, "b": "B"},
                "edges": {"ab": {"from": "a.out", "to": "b.left"}}, "layout": {"row": ["a", "b"]}}

    def test_unknown_field_is_not_silently_ignored(self):
        doc = self.doc()
        doc["layout"]["rankDir"] = "TB"
        with self.assertRaisesRegex(DslError, "rankDir"):
            validate(doc)

    def test_unknown_port_does_not_connect_to_default_center(self):
        doc = self.doc()
        doc["edges"]["ab"]["from"] = "a.typo"
        with self.assertRaisesRegex(DslError, "edges.ab.from"):
            validate(doc)

    def test_duplicate_and_unplaced_members_fail(self):
        for members in (["a", "a", "b"], ["a"]):
            doc = self.doc()
            doc["layout"] = {"row": members}
            with self.assertRaises(DslError):
                validate(doc)

    def test_group_cycle_is_not_recursively_expanded(self):
        doc = self.doc()
        doc["groups"] = {"g": {"layout": {"column": ["g"]}}}
        doc["layout"] = {"row": ["g", "a", "b"]}
        with self.assertRaisesRegex(DslError, "cycle"):
            validate(doc)

    def test_code_and_raw_feature_scripts_are_not_executed(self):
        doc = self.doc()
        doc["nodes"]["a"]["features"] = {"gradient": {"code": "throw new Error('not allowed')"}}
        with self.assertRaisesRegex(DslError, "executable"):
            validate(doc)

    def test_duplicate_yaml_keys_are_rejected_and_table_yes_remains_text(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "scene.yaml"
            path.write_text("version: 1\nid: test\nnodes: {a: one, a: two}\n", encoding="utf-8")
            with self.assertRaisesRegex(DslError, "duplicate"):
                load(path)
            path.write_text("version: 1\nid: test\nnodes:\n  a:\n    shape: table\n    columns: [Busy]\n    rows: [[Yes], [No]]\n", encoding="utf-8")
            self.assertEqual(load(path)["nodes"]["a"]["rows"], [["Yes"], ["No"]])

    def test_table_must_keep_columns_consistent(self):
        doc = self.doc()
        doc["nodes"]["a"] = {"shape": "table", "columns": ["x", "y"], "rows": [[1]]}
        with self.assertRaisesRegex(DslError, "rows"):
            validate(doc)

    def test_negative_scene_origin_is_valid(self):
        doc = self.doc()
        doc["layout"]["origin"] = [-200, -100]
        self.assertEqual(validate(doc)["layout"]["origin"], [-200, -100])

    def test_nested_origin_is_not_silently_ignored(self):
        doc = self.doc()
        doc["layout"] = {"column": [{"row": ["a", "b"], "origin": [400, 0]}]}
        with self.assertRaisesRegex(DslError, "origin is root-only"):
            validate(doc)

    def test_yaml_aliases_cannot_share_or_cycle_scene_members(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "scene.yaml"
            path.write_text("version: 1\nid: test\nnodes: {a: &shared {label: A}, b: *shared}\n", encoding="utf-8")
            with self.assertRaises(DslError) as error:
                load(path)
            self.assertEqual(error.exception.path, "YAML")

    def test_nonfinite_and_cyclic_programmatic_documents_are_rejected(self):
        for value in (float("nan"), float("inf")):
            doc = self.doc()
            doc["nodes"]["a"]["at"] = [value, 0]
            with self.assertRaises(DslError):
                validate(doc)
        doc = self.doc()
        doc["nodes"]["a"]["options"] = doc
        with self.assertRaises(DslError):
            validate(doc)

    def test_boolean_version_does_not_select_integer_schema(self):
        doc = self.doc()
        doc["version"] = True
        with self.assertRaises(DslError):
            validate(doc)


class ReconciliationTests(unittest.TestCase):
    def fixture(self):
        native = {"id": "native-a", "type": "rectangle", "x": 0, "y": 0, "width": 100, "height": 50,
                  "customData": {"dsl": {"document": "test", "key": "node.a"}}}
        spec = {"op": "create_shape", "ref": "node.a", "type": "rectangle", "x": 0, "y": 0, "width": 100, "height": 50,
                "style": {}, "customData": native["customData"]}
        plan = {"document": "test", "entities": {"node.a": spec}, "features": [], "post": [], "routes": {}}
        state = {"document": "test", "file": "draw.excalidraw.md", "entities": copy.deepcopy(plan["entities"]),
                 "ids": {"node.a": native["id"]}, "snapshots": {"node.a": fingerprint(native)}, "post": [], "features": []}
        scene = {"file": "draw.excalidraw.md", "elements": [native, {"id": "user", "type": "text", "text": "untouched"}]}
        return plan, state, scene

    def test_same_document_is_a_true_noop(self):
        plan, state, scene = self.fixture()
        result = plan_update(plan, state, scene)
        self.assertEqual(result["operations"], [])
        self.assertEqual(result["created"], [])

    def test_external_edit_is_a_conflict_not_an_overwrite(self):
        plan, state, scene = self.fixture()
        scene["elements"][0]["x"] = 40
        with self.assertRaisesRegex(DslError, "conflict.node.a"):
            plan_update(plan, state, scene)

    def test_update_preserves_identity_and_unowned_content(self):
        plan, state, scene = self.fixture()
        plan["entities"]["node.a"]["width"] = 160
        result = plan_update(plan, state, scene)
        self.assertEqual(result["updated"], ["node.a"])
        self.assertTrue(all(op.get("target") == "native-a" for op in result["operations"]))
        self.assertEqual(scene["elements"][1]["text"], "untouched")
        self.assertFalse(any(op["op"] == "delete" for op in result["operations"]))

    def test_duplicate_managed_identity_and_missing_state_refuse_replay(self):
        plan, state, scene = self.fixture()
        with self.assertRaisesRegex(DslError, "already exists"):
            plan_update(plan, None, scene)
        scene["elements"].append({**scene["elements"][0], "id": "copy"})
        with self.assertRaisesRegex(DslError, "duplicate"):
            plan_update(plan, state, scene)

    def test_delete_is_scoped_to_owned_element(self):
        plan, state, scene = self.fixture()
        plan["entities"] = {}
        result = plan_update(plan, state, scene)
        self.assertEqual(result["operations"], [{"op": "delete", "targets": ["native-a"]}])

    def test_native_version_and_cache_changes_are_not_user_edits(self):
        plan, state, scene = self.fixture()
        scene["elements"][0].update(version=200, versionNonce=333, updated=12345, _needsShadowRestore=True)
        self.assertEqual(plan_update(plan, state, scene)["operations"], [])

    def test_moved_polygon_keeps_a_closed_boundary(self):
        plan, state, scene = self.fixture()
        outline = {"op": "create_linear", "ref": "node.a", "kind": "line", "x": 0, "y": 0,
                   "points": [[0, 0], [100, 0], [50, 50]], "polygon": True, "closed": True,
                   "style": {}, "customData": scene["elements"][0]["customData"]}
        state["entities"]["node.a"] = copy.deepcopy(outline)
        plan["entities"]["node.a"] = {**outline, "x": 20}
        native = scene["elements"][0]
        native.update(type="line", points=[*outline["points"], [0, 0]], polygon=True)
        state["snapshots"]["node.a"] = fingerprint(native)
        changes = plan_update(plan, state, scene)
        patch = next(op["patch"] for op in changes["operations"] if op["op"] == "patch_element")
        moved = {**native, **patch}
        self.assertEqual(moved["points"][0], moved["points"][-1])
        self.assertEqual(moved["x"], 20)
        self.assertEqual(native["x"], 0)

    def test_deleting_featured_node_does_not_modify_its_deleted_label(self):
        plan, state, scene = self.fixture()
        label = {"id": "native-label", "type": "text", "containerId": "native-a",
                 "customData": {"dsl": {"document": "test", "key": "node.a:label"}}}
        scene["elements"].append(label)
        state["ids"]["node.a:label"] = label["id"]
        state["snapshots"]["node.a:label"] = fingerprint(label)
        state["features"] = [{"op": "set_feature", "feature": "rich_text",
                              "targets": ["@node.a:label"], "config": {"bold": True}}]
        plan["entities"] = {}
        changes = plan_update(plan, state, scene)
        self.assertEqual(changes["operations"], [{"op": "delete", "targets": ["native-a", "native-label"]}])

    def test_resizing_a_labeled_node_refreshes_its_bound_text(self):
        plan, state, scene = self.fixture()
        label = {"text": "Full label", "style": {"fontSize": 20}}
        plan["entities"]["node.a"]["label"] = copy.deepcopy(label)
        state["entities"]["node.a"]["label"] = copy.deepcopy(label)
        state["ids"]["node.a:label"] = "native-label"
        native_label = {"id": "native-label", "type": "text", "containerId": "native-a",
                        "customData": {"dsl": {"document": "test", "key": "node.a:label"}}}
        scene["elements"].append(native_label)
        state["snapshots"]["node.a:label"] = fingerprint(native_label)
        plan["entities"]["node.a"]["width"] = 180
        changes = plan_update(plan, state, scene)
        text_change = next(op for op in changes["operations"] if op["op"] == "set_text")
        self.assertEqual(text_change["target"], "native-label")
        self.assertEqual(text_change["text"], label["text"])
        self.assertFalse(any(op["op"] == "delete" for op in changes["operations"]))

    def test_removing_owned_arrow_width_does_not_leave_old_visual_override(self):
        plan, state, scene = self.fixture()
        scene["elements"][0]["customData"]["blockArrowWidth"] = 36
        state["entities"]["node.a"]["customData"]["blockArrowWidth"] = 36
        plan["entities"]["node.a"]["customData"] = {"dsl": {"document": "test", "key": "node.a"}}
        state["snapshots"]["node.a"] = fingerprint(scene["elements"][0])
        changes = plan_update(plan, state, scene)
        metadata = next(op for op in changes["operations"] if op["op"] == "patch_custom_data")
        effective = {**scene["elements"][0]["customData"], **metadata["merge"]}
        for key in metadata["remove"]:
            effective.pop(key, None)
        self.assertNotIn("blockArrowWidth", effective)
        self.assertEqual(effective["dsl"]["key"], "node.a")


if __name__ == "__main__":
    unittest.main()
