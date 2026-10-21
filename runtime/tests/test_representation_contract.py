"""Declared topology must agree with actual native bodies and saved routes."""
import copy
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from representation_contract import check_representation, validate_contract
from acceptance import triage


def example():
    contract = {"components": [{"id": "alu", "role": "compute", "types": ["rectangle"]}, {"id": "rf", "role": "storage", "types": ["rectangle"]}],
                "ports": [{"id": "result", "component": "alu", "side": "right", "offset": 0.5, "direction": "output"},
                          {"id": "write", "component": "rf", "side": "left", "offset": 0.5, "direction": "input"}],
                "signals": [{"id": "writeback", "source": "result", "target": "write", "orthogonal": True}]}
    elements = [{"id": "a", "type": "rectangle", "x": -100, "y": -20, "width": 100, "height": 60},
                {"id": "b", "type": "rectangle", "x": 100, "y": 20, "width": 80, "height": 60},
                {"id": "w", "type": "line", "x": 0, "y": 10, "width": 100, "height": 40,
                 "points": [[0, 0], [50, 0], [50, 40], [100, 40]], "angle": 0}]
    return contract, elements, {"alu": ["a"], "rf": ["b"], "writeback": ["w"]}


class RepresentationTests(unittest.TestCase):
    def codes(self, contract, elements, bindings):
        return {i["code"] for i in check_representation(elements, contract, bindings)}

    def test_real_native_topology_passes_not_a_label_count(self):
        contract, elements, bindings = example()
        self.assertEqual(check_representation(elements, contract, bindings), [])
        text = [{**el, "type": "text", "text": "ALU plus storage plus writeback"} for el in elements]
        codes = self.codes(contract, text, bindings)
        self.assertIn("REPRESENTATION_BODY_TYPE", codes)
        self.assertIn("REPRESENTATION_SIGNAL_TYPE", codes)

    def test_invisible_proxy_alone_is_not_a_body_but_composite_outline_is(self):
        contract, elements, bindings = example()
        elements[0].update(strokeColor="transparent", backgroundColor="transparent")
        self.assertIn("REPRESENTATION_BODY_INVISIBLE", self.codes(contract, elements, bindings))
        elements.append({"id": "outline", "type": "line", "x": -100, "y": -20, "width": 100, "height": 60,
                         "points": [[0, 0], [100, 0], [100, 60], [0, 60], [0, 0]], "polygon": True})
        contract["components"][0]["types"].append("line")
        bindings["alu"].append("outline")
        self.assertEqual(check_representation(elements, contract, bindings), [])
        elements[2]["strokeColor"] = "transparent"
        self.assertIn("REPRESENTATION_SIGNAL_TYPE", self.codes(contract, elements, bindings))

    def test_missing_port_route_and_moving_body_are_hard_failures(self):
        contract, elements, bindings = example()
        self.assertIn("REPRESENTATION_BODY_MISSING", self.codes(contract, elements, {"rf": ["b"]}))
        elements[1]["x"] += 20
        issues = check_representation(elements, contract, bindings)
        self.assertIn("REPRESENTATION_ENDPOINT", {i["code"] for i in issues})
        with self.assertRaises(ValueError):
            triage(issues, "high", [{"issue_id": __import__("acceptance").issue_id(issues[0]), "decision": "intentional", "element_ids": ["w"], "preview_id": "png", "reason": "Ignore routing"}])

    def test_diagonal_or_reversed_direction_cannot_be_declared_orthogonal(self):
        contract, elements, bindings = example()
        elements[2]["points"] = [[0, 0], [100, 40]]
        self.assertIn("REPRESENTATION_DIAGONAL", self.codes(contract, elements, bindings))
        contract["signals"][0]["source"], contract["signals"][0]["target"] = "write", "result"
        with self.assertRaises(ValueError):
            validate_contract(contract, "microarchitecture")

    def test_actual_binding_targets_cannot_contradict_named_ports(self):
        contract, elements, bindings = example()
        elements[2]["endBinding"] = {"elementId": "a"}
        self.assertIn("REPRESENTATION_BINDING", self.codes(contract, elements, bindings))
        elements[2]["endBinding"] = {"elementId": "b"}
        self.assertEqual(check_representation(elements, contract, bindings), [])

    def test_negative_local_points_and_quarter_turns_use_world_geometry(self):
        contract, elements, bindings = example()
        wire = elements[2]
        wire.update(x=100, y=50, points=[[0, 0], [-50, 0], [-50, -40], [-100, -40]])
        contract["signals"][0].update(source="write", target="result")
        contract["ports"][0]["direction"], contract["ports"][1]["direction"] = "input", "output"
        self.assertEqual(check_representation(elements, contract, bindings), [])
        contract, elements, bindings = example()
        elements[0].update(angle=math.pi/2, x=-90, y=-10, width=80, height=40)
        # rotated world box is x=-70..-30, y=-30..50, right midpoint=(-30,10)
        elements[2].update(x=-30, width=130, points=[[0, 0], [80, 0], [80, 40], [130, 40]])
        self.assertEqual(check_representation(elements, contract, bindings), [])
        elements[0]["angle"] = 0.3
        self.assertIn("REPRESENTATION_GEOMETRY_UNSUPPORTED", self.codes(contract, elements, bindings))

    def test_declarations_cannot_substitute_text_or_drop_hardware_network(self):
        contract, elements, bindings = example()
        with self.assertRaises(ValueError):
            validate_contract(None, "circuit")
        broken = copy.deepcopy(contract)
        broken["components"][0]["types"] = ["text"]
        with self.assertRaises(ValueError):
            validate_contract(broken, "microarchitecture")
        broken = copy.deepcopy(contract)
        broken["ports"][0]["component"] = "unknown"
        with self.assertRaises(ValueError):
            validate_contract(broken, "microarchitecture")
        self.assertIsNone(validate_contract(None, "general"))


if __name__ == "__main__":
    unittest.main()
