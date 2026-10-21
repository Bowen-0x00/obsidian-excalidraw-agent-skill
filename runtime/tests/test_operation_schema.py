"""Consumer-visible rejection and native-payload preservation regressions."""
import copy
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from operation_schema import validate_operations, operation_examples


class NativeOperationTests(unittest.TestCase):
    def test_historical_wrong_calls_fail_with_actionable_paths(self):
        bad = [
            {"op": "create_rectangle", "x": 0},
            {"type": "text", "text": "not an operation"},
            {"op": "create_text", "text": "ALU", "x": 0, "y": 0, "fontSize": 13},
            {"op": "create_text", "text": "ALU", "x": 0, "y": 0, "style": {"fontWeight": "bold"}},
            {"op": "create_shape", "type": "rectangle", "x": 0, "y": 0, "width": 100, "height": 50, "label": {"text": "ALU", "fontSize": 13}},
        ]
        for payload in bad:
            with self.subTest(payload=payload), self.assertRaisesRegex(ValueError, "committed=false"):
                validate_operations([payload])

    def test_native_points_resources_and_custom_extensions_are_preserved(self):
        operations = [
            {"op": "create_linear", "kind": "line", "x": -30, "y": 0, "points": [[0, 0], [-40, 0], [-40, 70]], "style": {"roundness": None}},
            {"op": "create_latex", "x": 0, "y": 10, "tex": r"W=\begin{bmatrix}1&2\\3&4\end{bmatrix}", "scaleX": 1.25},
            {"op": "set_feature", "feature": "echarts", "targets": ["chart"], "config": {"type": "custom", "options": {"series": [{"type": "bar", "data": [0, 3]}]}}},
            {"op": "patch_custom_data", "target": "body", "merge": {"shadow": True, "metadata": {"source": "retained"}}},
            {"op": "rotate", "groupId": "compound", "degrees": 90},
            {"op": "set_text_global_style", "targets": ["label"], "bold": True},
        ]
        self.assertEqual(validate_operations(operations), operations)

    def test_nonfinite_and_wrong_geometry_cannot_reach_native_commit(self):
        for value in (math.nan, math.inf, "20", True, 0, -1):
            payload = {"op": "create_shape", "type": "rectangle", "x": 0, "y": 0, "width": value, "height": 50}
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_operations([payload])
        for payload in ({"op": "rotate", "degrees": 90}, {"op": "connect", "from": "", "to": "b"},
                        {"op": "connect", "from": "a", "to": "b", "start": {"fixedPoint": [1.1, 0]}}):
            with self.assertRaises(ValueError):
                validate_operations([payload])

    def test_native_alignment_and_unbind_defaults_are_not_reinvented(self):
        operations = [{"op": "align", "targets": ["a", "b"], "alignment": "center-horizontal"},
                      {"op": "align", "targets": ["a", "b"], "alignment": "center-vertical"},
                      {"op": "unbind_arrow", "arrow": "wire"}]
        self.assertEqual(validate_operations(operations), operations)
        for alignment in ("center", "middle"):
            with self.assertRaises(ValueError):
                validate_operations([{"op": "align", "targets": ["a", "b"], "alignment": alignment}])
        for operation in ({"op": "create_linear", "points": [[0, 0], [10, 0]]},
                          {"op": "create_draw", "points": [[0, 0], [10, 0]]},
                          {"op": "create_table", "x": 0, "y": 0, "rows": 2, "cols": 2}):
            with self.assertRaises(ValueError):
                validate_operations([operation])

    def test_examples_are_native_inputs_not_compatibility_aliases(self):
        examples = list(operation_examples().values())
        self.assertEqual(validate_operations(examples), examples)
        before = copy.deepcopy(examples)
        validate_operations(examples)
        self.assertEqual(examples, before)


if __name__ == "__main__":
    unittest.main()
