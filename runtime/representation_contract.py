"""Check declared drawing topology against saved native elements, not prose claims."""
from __future__ import annotations

import math
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator
from geometry_diagnostics import _scene_box, _scene_points
from visual_diagnostics import is_visible

Identity = Annotated[str, Field(min_length=1)]
BodyType = Literal["rectangle", "ellipse", "diamond", "line", "freedraw", "image", "embeddable"]
PORT_TOLERANCE = 1.0  # scene units; export scale never changes this tolerance


class ContractModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)


class Component(ContractModel):
    id: Identity
    role: Identity
    types: Annotated[list[BodyType], Field(min_length=1)]

    @model_validator(mode="after")
    def formula_resource(self):
        if self.role == "formula" and self.types != ["image"]:
            raise ValueError("formula components require a native image resource, not text/outline simulation")
        return self


class Port(ContractModel):
    id: Identity
    component: Identity
    side: Literal["left", "right", "top", "bottom"]
    offset: Annotated[float, Field(ge=0, le=1)]
    direction: Literal["input", "output", "control"]


class Signal(ContractModel):
    id: Identity
    source: Identity
    target: Identity
    orthogonal: bool = True


class RepresentationContract(ContractModel):
    components: Annotated[list[Component], Field(min_length=1)]
    ports: list[Port]
    signals: list[Signal]

    @model_validator(mode="after")
    def topology(self):
        all_ids = [item.id for items in (self.components, self.ports, self.signals) for item in items]
        if len(all_ids) != len(set(all_ids)):
            raise ValueError("component, port and signal IDs must be globally unique")
        bodies = {item.id for item in self.components}
        ports = {item.id: item for item in self.ports}
        for port in self.ports:
            if port.component not in bodies:
                raise ValueError(f"port {port.id} references an undeclared component")
        for signal in self.signals:
            if signal.source not in ports or signal.target not in ports:
                raise ValueError(f"signal {signal.id} must reference declared named ports")
            if ports[signal.source].direction == "input" or ports[signal.target].direction == "output":
                raise ValueError(f"signal {signal.id} reverses the declared port direction")
            if signal.source == signal.target:
                raise ValueError(f"signal {signal.id} cannot connect a port to itself")
        return self


def validate_contract(contract: dict | None, diagram_type: str) -> dict | None:
    if contract is None:
        if diagram_type in ("microarchitecture", "circuit"):
            raise ValueError("REPRESENTATION_REQUIRED: declare components, named ports and signals before creating hardware; prose labels are not bodies")
        return None
    result = RepresentationContract.model_validate(contract).model_dump()
    if diagram_type in ("microarchitecture", "circuit") and (not result["ports"] or not result["signals"]):
        raise ValueError("REPRESENTATION_REQUIRED: hardware needs named ports and signal topology, not a count of labels")
    return result


def check_representation(elements: list[dict], contract: dict | None, bindings: dict[str, list[str]] | None) -> list[dict]:
    if contract is None:
        return []
    spec = RepresentationContract.model_validate(contract)
    by_id = {el["id"]: el for el in elements if el.get("id") and not el.get("isDeleted")}
    bindings = bindings or {}
    issues = []

    def fail(code, logical, ids, actual, message, repair):
        issues.append({"code": "REPRESENTATION_" + code, "severity": "error", "elementIds": ids,
                       "logicalId": logical, "actual": actual, "message": message, "repairHint": repair})

    expected_ids = {item.id for item in (*spec.components, *spec.signals)}
    for logical in bindings.keys() - expected_ids:
        fail("UNKNOWN_BINDING", logical, [], None, "Binding is not declared in this task", "Use a declared component or signal ID; ports derive from their component")
    used, boxes, body_ids = {}, {}, {}
    for component in spec.components:
        ids = bindings.get(component.id)
        if not isinstance(ids, list) or not ids or any(not isinstance(i, str) for i in ids):
            fail("BODY_MISSING", component.id, [], ids, "No native body mapped to the component", "Map its actual body/outline IDs, not a label")
            continue
        valid = []
        painted = False
        body_ids[component.id] = set(ids)
        for identity in ids:
            element = by_id.get(identity)
            if identity in used:
                fail("REUSED_ELEMENT", component.id, [identity], used[identity], "Independent components cannot share one body", "Map distinct native bodies")
                continue
            used[identity] = component.id
            if not element or element.get("type") not in component.types or not is_visible(element):
                fail("BODY_TYPE", component.id, [identity], element.get("type") if element else None, "Missing, invisible or wrong native body type", "Draw the declared editable body; text does not satisfy a hardware component")
                continue
            if not _quarter_turn(element):
                fail("GEOMETRY_UNSUPPORTED", component.id, [identity], element.get("angle"), "Port checks do not support arbitrary body rotations", "Use a quarter-turn body or explicitly redesign the declared component geometry")
                continue
            points = _scene_points(element) if element.get("points") else None
            if points:
                if not (element.get("polygon") or element.get("customData", {}).get("svgShape") or math.dist(points[0], points[-1]) <= PORT_TOLERANCE):
                    fail("BODY_OPEN", component.id, [identity], None, "An open wire is not a component outline", "Use a closed native polygon/shape or a real library body")
                    continue
                box = (min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points))
            else:
                b = _scene_box(element)
                box = (b["x"], b["y"], b["x"] + b["width"], b["y"] + b["height"])
            valid.append(box)
            painted = painted or _paints(element)
        if valid:
            if not painted:
                fail("BODY_INVISIBLE", component.id, ids, None, "Only invisible binding proxies are mapped, not a visible body", "Include the real native outline/body along with its proxy")
            box = (min(b[0] for b in valid), min(b[1] for b in valid), max(b[2] for b in valid), max(b[3] for b in valid))
            if box[2] <= box[0] or box[3] <= box[1]:
                fail("BODY_EMPTY", component.id, ids, box, "Body has no usable two-dimensional bounds", "Draw the actual component outline")
            else:
                boxes[component.id] = box
    ports = {p.id: p for p in spec.ports}
    anchors = {}
    for port in spec.ports:
        if port.component not in boxes:
            fail("PORT_MISSING", port.id, [], port.component, "Port has no valid native component bounds", "Repair/map the component body first")
            continue
        x0, y0, x1, y1 = boxes[port.component]
        # side/offset are WORLD AABB coordinates, including for quarter-turn bodies.
        anchors[port.id] = {"left": (x0, y0 + (y1-y0)*port.offset), "right": (x1, y0 + (y1-y0)*port.offset),
                            "top": (x0 + (x1-x0)*port.offset, y0), "bottom": (x0 + (x1-x0)*port.offset, y1)}[port.side]
    for signal in spec.signals:
        ids = bindings.get(signal.id)
        if not isinstance(ids, list) or len(ids) != 1 or not isinstance(ids[0], str):
            fail("SIGNAL_MISSING", signal.id, [], ids, "Signal must map to one native line/arrow", "Map the saved continuous polyline ID for this named signal")
            continue
        identity = ids[0]
        element = by_id.get(identity)
        if identity in used:
            fail("REUSED_ELEMENT", signal.id, ids, used[identity], "A wire cannot replace another body/signal", "Create/map the independently declared signal")
        used[identity] = signal.id
        if not element or element.get("type") not in ("line", "arrow") or element.get("polygon") or not _paints(element):
            fail("SIGNAL_TYPE", signal.id, ids, element.get("type") if element else None, "Signal is not a visible native wire", "Use a native line/arrow with the declared endpoints")
            continue
        if not _quarter_turn(element) or element.get("customData", {}).get("curveArrow") or element.get("roundness") and not element.get("elbowed"):
            fail("GEOMETRY_UNSUPPORTED", signal.id, ids, element.get("angle"), "Exact topology checks require straight/orthogonal native segments", "Use an unsmoothed polyline or square elbow; do not waive this as a visual overlap")
            continue
        points = _scene_points(element) if element.get("points") else []
        if len(points) < 2 or sum(math.dist(a, b) for a, b in zip(points, points[1:])) <= PORT_TOLERANCE:
            fail("SIGNAL_EMPTY", signal.id, ids, points, "Signal has no usable path", "Draw the actual connection")
            continue
        for end, port_id, point in (("start", signal.source, points[0]), ("end", signal.target, points[-1])):
            anchor = anchors.get(port_id)
            if anchor is not None and math.dist(point, anchor) > PORT_TOLERANCE:
                fail("ENDPOINT", signal.id, ids, {"end": end, "point": point, "expected": anchor, "port": port_id}, "Wire misses the declared named port", "Repair this route endpoint; keep the body and contract identity")
            binding = element.get(end + "Binding")
            if binding and binding.get("elementId") not in body_ids.get(ports[port_id].component, set()):
                fail("BINDING", signal.id, ids, binding.get("elementId"), "Native binding targets a different component", "Reconnect to the declared native body, not an unrelated node")
        if signal.orthogonal:
            for index, (a, b) in enumerate(zip(points, points[1:])):
                if abs(a[0]-b[0]) > 1e-5 and abs(a[1]-b[1]) > 1e-5:
                    fail("DIAGONAL", signal.id, ids, {"segment": index, "points": [a, b]}, "A declared orthogonal signal contains a diagonal segment", "Add explicit horizontal/vertical waypoints and read back the saved route")
    return issues


def _paints(element: dict) -> bool:
    if not is_visible(element):
        return False
    if element.get("type") in ("image", "embeddable"):
        return True  # resource completeness/pixels are checked separately
    transparent = {"transparent", "none", ""}
    return ((element.get("strokeWidth", 1) > 0 and str(element.get("strokeColor", "#1e1e1e")).lower() not in transparent)
            or str(element.get("backgroundColor", "transparent")).lower() not in transparent)


def _quarter_turn(element: dict) -> bool:
    angle = element.get("angle", 0)
    return isinstance(angle, (int, float)) and math.isfinite(angle) and abs(angle / (math.pi/2) - round(angle / (math.pi/2))) < 1e-7
