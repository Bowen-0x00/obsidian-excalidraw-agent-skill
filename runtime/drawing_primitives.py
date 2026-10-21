"""Typed native operation planning adapted from the user's Scripts2 geometry and Engines."""
from __future__ import annotations

import math
import uuid
from typing import Any

from diagram_layout import FONT, Metrics, PORTS, _number, _point, _route
from illustration_geometry import KINDS as ILLUSTRATION_KINDS, plan_geometry

SUPPORTED = ("draw", "polygon", "cuboid", "brace", "callout", "code", "checkbox", "connection", "text", *ILLUSTRATION_KINDS)


def _bounds(points: list[list[float]], x=0.0, y=0.0) -> dict:
    xs, ys = [point[0] + x for point in points], [point[1] + y for point in points]
    return {"x": min(xs), "y": min(ys), "width": max(xs) - min(xs), "height": max(ys) - min(ys)}


def _local(points: list[list[float]]) -> tuple[list[list[float]], float, float]:
    origin_x, origin_y = points[0]
    return [[point[0] - origin_x, point[1] - origin_y] for point in points], origin_x, origin_y


def plan_primitives(client: Any, context_token: str, items: list[dict], style: dict | None = None) -> dict:
    if not isinstance(items, list) or not items:
        raise ValueError("items must be a nonempty list of typed primitives")
    context = client.request("POST", "/v3/context", {"contextToken": context_token, "includeElements": False})
    scene = client.read(context_token, detail="full")
    by_id = {element["id"]: element for element in scene["elements"]}
    common = {"strokeColor": "#334155", "backgroundColor": "transparent", "fillStyle": "solid", "strokeWidth": 2, "roughness": 0, **(style or {})}
    font = str(common.get("fontFamily", FONT))
    font_size = float(common.get("fontSize", 20))
    metrics = Metrics(client, context_token, font)
    operations, measured, refs, notes = [], {}, {}, []
    anchors, manifests = {}, {}
    names = set()
    features = client.request("GET", "/v3/runtime-capabilities").get("features", {})
    for index, item in enumerate(items):
        if not isinstance(item, dict) or item.get("kind") not in SUPPORTED:
            raise ValueError(f"items[{index}].kind must be one of {', '.join(SUPPORTED)}")
        kind, name = item["kind"], str(item.get("id", f"{item['kind']}-{index + 1}"))
        if name in names:
            raise ValueError(f"Duplicate primitive ID: {name}")
        names.add(name)
        unit = "primitive-" + uuid.uuid4().hex[:12]
        x = _number(item.get("x", 0), f"{name}.x")
        y = _number(item.get("y", index * 220), f"{name}.y")
        visual = {**common, **item.get("style", {})}
        text_style = {"fontFamily": str(visual.get("fontFamily", font)), "fontSize": float(visual.get("fontSize", font_size)),
                      "strokeColor": visual.get("strokeColor", "#1e293b"), "lineHeight": 1.2}
        geometry_style = {key: value for key, value in visual.items() if key not in ("fontFamily", "fontSize", "textAlign", "verticalAlign", "lineHeight")}
        unit_ops, unit_refs = [], []

        def data(role: str, box: dict | None = None) -> dict:
            return {"agentPrimitive": {"instanceId": unit, "kind": kind, "role": role, **({"compoundBounds": box} if box else {})},
                    "agentDiagram": {"logicalId": name, "role": "primitive-" + role}}

        def linear(ref: str, points: list[list[float]], *, closed=False, local_style=None, role="decoration") -> None:
            local_points, px, py = _local(points)
            unit_ops.append({"op": "create_linear", "kind": "line", "ref": ref, "x": px, "y": py,
                             "points": local_points, "closed": closed, "polygon": closed,
                             "style": {**geometry_style, **(local_style or {})}, "customData": data(role)})
            unit_refs.append("@" + ref)

        def require_feature(feature: str) -> None:
            if not features.get(feature, {}).get("callable"):
                raise ValueError(f"Feature {feature} is not callable in the running instance")

        if kind in ILLUSTRATION_KINDS:
            construction = plan_geometry({**item, "id": name}, geometry_style)
            unit_ops.extend(construction["operations"])
            unit_refs.extend("@" + op["ref"] for op in unit_ops)
            box = construction["bounds"]
            anchors[name] = construction["anchors"]
            manifests[name] = construction["manifest"]
            notes.extend(construction["notes"])
            unit = unit_ops[0]["customData"]["agentPrimitive"]["instanceId"]
        elif kind == "text":
            allowed = {"kind", "id", "x", "y", "text", "width", "style", "objectId", "viewId"}
            if set(item) - allowed or not isinstance(item.get("text"), str):
                raise ValueError("text primitive needs text, x/y and optional width/style/objectId/viewId")
            text, size = metrics.wrap(item["text"], _number(item.get("width", 600), "text.width", 1), text_style["fontSize"])
            box = {"x": x, "y": y, **size}
            unit_ops.append({"op": "create_text", "ref": name, "x": x, "y": y, "text": text, "style": text_style,
                             "customData": data("caption")})
            if item.get("objectId"):
                unit_ops[-1]["customData"]["technicalIllustration"] = {"viewId": item.get("viewId","main"),
                    "objectId": item["objectId"], "role": "label"}
            unit_refs.append("@" + name)
        elif kind == "draw":
            points = item.get("points")
            if not isinstance(points, list) or len(points) < 2:
                raise ValueError("draw needs at least two explicit local stroke points")
            points = [[_number(point[0], "draw.x"), _number(point[1], "draw.y")] for point in points]
            box = _bounds(points, x, y)
            operation = {"op": "create_draw", "ref": name, "x": x, "y": y, "points": points,
                         "style": geometry_style, "customData": data("stroke", box)}
            for key in ("pressures", "simulatePressure"):
                if key in item:
                    operation[key] = item[key]
            unit_ops.append(operation)
            unit_refs.append("@" + name)
        elif kind == "polygon":
            if "sideLengths" in item:
                raise ValueError("Arbitrary side lengths are not equivalent to an equiangular closure; supply explicit vertices or a regular polygon")
            if "points" in item:
                points = [[_number(point[0], "polygon.x"), _number(point[1], "polygon.y")] for point in item["points"]]
                if len(points) < 3:
                    raise ValueError("Polygon needs at least three vertices")
            else:
                sides = item.get("sides", 6)
                if isinstance(sides, bool) or not isinstance(sides, int) or not 3 <= sides <= 200:
                    raise ValueError("Regular polygon sides must be an integer from 3 to 200")
                length = _number(item.get("sideLength", 80), "sideLength", 0.001)
                radius = length / (2 * math.sin(math.pi / sides))
                angle = math.radians(_number(item.get("rotation", -90), "rotation"))
                points = [[radius * math.cos(angle + i * 2 * math.pi / sides), radius * math.sin(angle + i * 2 * math.pi / sides)] for i in range(sides)]
                raw = _bounds(points)
                points = [[px - raw["x"], py - raw["y"]] for px, py in points]
            if points[0] != points[-1]:
                points.append(points[0].copy())
            absolute = [[x + px, y + py] for px, py in points]
            box = _bounds(absolute)
            linear(name, absolute, closed=True, role="body")
        elif kind == "cuboid":
            width = _number(item.get("width", 160), "width", 1)
            height = _number(item.get("height", 100), "height", 1)
            depth = _number(item.get("depth", 55), "depth", 1)
            angle = math.radians(_number(item.get("angle", 35), "angle"))
            dx, dy = depth * math.cos(angle), depth * math.sin(angle)
            if dx < 0 or dy < 0:
                raise ValueError("Cuboid uses the verified upper-right projection; angle must project to nonnegative depth offsets")
            front_y = y + dy
            box = {"x": x, "y": y, "width": width + dx, "height": height + dy}
            unit_ops.append({"op": "create_shape", "type": "rectangle", "ref": name, "x": x, "y": front_y,
                             "width": width, "height": height, "style": {**geometry_style, "edge": "sharp"}, "customData": data("body", box)})
            unit_refs.append("@" + name)
            linear(name + ":top", [[x, front_y], [x + width, front_y], [x + width + dx, y], [x + dx, y], [x, front_y]], closed=True)
            linear(name + ":side", [[x + width, front_y], [x + width, front_y + height], [x + width + dx, y + height], [x + width + dx, y], [x + width, front_y]], closed=True)
            if item.get("dottedBack"):
                corner = [x + dx, y + height]
                for number, endpoints in enumerate(([[x + dx, y], corner], [corner, [x + width + dx, y + height]], [corner, [x, front_y + height]])):
                    linear(f"{name}:back:{number}", endpoints, local_style={"strokeStyle": "dotted"})
        elif kind == "brace":
            require_feature("svg_path_shape")
            side = item.get("side", "bottom")
            if side not in ("top", "bottom", "left", "right"):
                raise ValueError("Brace side must be top/bottom/left/right")
            target_box = item.get("box")
            if item.get("targets"):
                targets = [by_id.get(target) for target in item["targets"]]
                if any(target is None for target in targets):
                    raise ValueError("Brace target is missing; use exact current IDs")
                left, top = min(target["x"] for target in targets), min(target["y"] for target in targets)
                right, bottom = max(target["x"] + target["width"] for target in targets), max(target["y"] + target["height"] for target in targets)
                target_box = {"x": left, "y": top, "width": right - left, "height": bottom - top}
            horizontal = side in ("top", "bottom")
            length = _number(item.get("length", item.get("width" if horizontal else "height", 240)), "brace length", 1)
            if target_box:
                length = float(target_box["width" if horizontal else "height"])
            arm, tip, q = min(20, length * 0.15), min(15, length * 0.1), min(25, length * 0.2)
            thickness, middle = arm + tip, length / 2
            # The source Action scripts use negative coordinates for top/left; translate the entire path to a normalized viewBox.
            if horizontal:
                baseline, shoulder, cusp = (0, arm, thickness) if side == "bottom" else (thickness, tip, 0)
                path = f"M 0 {baseline} Q 0 {shoulder} {q} {shoulder} L {middle-q} {shoulder} Q {middle} {shoulder} {middle} {cusp} Q {middle} {shoulder} {middle+q} {shoulder} L {length-q} {shoulder} Q {length} {shoulder} {length} {baseline}"
                width, height = length, thickness
            else:
                baseline, shoulder, cusp = (0, arm, thickness) if side == "right" else (thickness, tip, 0)
                path = f"M {baseline} 0 Q {shoulder} 0 {shoulder} {q} L {shoulder} {middle-q} Q {shoulder} {middle} {cusp} {middle} Q {shoulder} {middle} {shoulder} {middle+q} L {shoulder} {length-q} Q {shoulder} {length} {baseline} {length}"
                width, height = thickness, length
            if target_box:
                gap = float(item.get("gap", 10))
                x = target_box["x"] - width - gap if side == "left" else target_box["x"] + target_box["width"] + gap if side == "right" else target_box["x"]
                y = target_box["y"] - height - gap if side == "top" else target_box["y"] + target_box["height"] + gap if side == "bottom" else target_box["y"]
            box = {"x": x, "y": y, "width": width, "height": height}
            unit_ops.append({"op": "create_svg_path", "ref": name, **box, "path": path,
                             "viewBox": {"width": width, "height": height}, "closed": False,
                             "style": {**geometry_style, "backgroundColor": "transparent", "roughness": 0}, "customData": data("brace", box)})
            unit_refs.append("@" + name)
        elif kind == "callout":
            require_feature("callout")
            title, body = str(item.get("title", "")), str(item.get("body", item.get("text", "")))
            width = _number(item.get("width", 400), "callout width", 80)
            body_text, size = metrics.wrap(body, width - 42, text_style["fontSize"])
            height = max(float(item.get("height", 0)), size["height"] + 70)
            box = {"x": x, "y": y, "width": width, "height": height}
            unit_ops.extend([
                {"op": "create_shape", "type": "rectangle", "ref": name, **box, "style": {**geometry_style, "strokeColor": "#000000", "backgroundColor": "transparent"},
                 "customData": data("body", box), "label": {"text": body_text, "style": {**text_style, "textAlign": "left", "verticalAlign": "top"}}},
                {"op": "set_feature", "feature": "callout", "targets": ["@" + name], "config": {"type": item.get("type", "note"), "colorType": item.get("colorType", "alpha"), "shadow": bool(item.get("shadow", False))}},
            ])
            if title:
                unit_ops.append({"op": "patch_custom_data", "target": "@" + name, "merge": {"callout": {"title": title}}})
            unit_refs.extend(["@" + name, "@" + name + ":label"])
        elif kind == "code":
            require_feature("code_highlight")
            theme = item.get("theme", "atom-one-light")
            if theme not in ("atom-one-light", "atom-one-dark"):
                raise ValueError("The installed highlight Engine supports atom-one-light or atom-one-dark")
            code_font = str(item.get("fontFamily", "Cascadia"))
            code_size = _number(item.get("fontSize", 18), "fontSize", 1)
            source = str(item.get("text", ""))
            if not source:
                raise ValueError("Code block requires source text")
            code_metrics = Metrics(client, context_token, code_font).size(source, code_size)
            # Do not change source with inserted line breaks. Wide code needs a wider canvas or explicit user-provided breaks.
            width = max(float(item.get("width", 0)), code_metrics["width"])
            height = code_metrics["height"]
            box = {"x": x, "y": y, "width": width, "height": height}
            unit_ops.extend([
                {"op": "create_text", "ref": name, "x": x, "y": y, "text": source,
                 "style": {**text_style, "fontFamily": code_font, "fontSize": code_size}, "customData": data("code", box)},
                {"op": "set_feature", "feature": "code_highlight", "targets": ["@" + name],
                 "config": {"language": str(item.get("language", "plaintext")), "theme": theme, "fontFamily": code_font, "fontSize": code_size, "embedFont": True}},
            ])
            unit_refs.append("@" + name)
        elif kind == "checkbox":
            require_feature("checkbox")
            text = str(item.get("text", ""))
            checked = bool(item.get("checked", False))
            source = ("- [x] " if checked else "- [ ] ") + text
            size = metrics.size(source, text_style["fontSize"])
            box = {"x": x, "y": y, **size}
            unit_ops.extend([
                {"op": "create_text", "ref": name, "x": x, "y": y, "text": text, "style": text_style, "customData": data("checkbox", box)},
                {"op": "set_feature", "feature": "checkbox", "targets": ["@" + name], "config": {"checked": checked, "addMarkdownPrefix": True}},
            ])
            unit_refs.append("@" + name)
        elif kind == "connection":
            source, target = by_id.get(item.get("from")), by_id.get(item.get("to"))
            if not source or not target:
                raise ValueError("Connection requires existing exact endpoint IDs")
            start, end = item.get("start", {}), item.get("end", {})
            start_port, end_port = start.get("anchor", "right"), end.get("anchor", "left")
            if start_port not in PORTS or end_port not in PORTS:
                raise ValueError("Connection anchors must be top/right/bottom/left")
            start_point, end_point = _point(source, start_port, start.get("fixedPoint")), _point(target, end_port, end.get("fixedPoint"))
            mode = item.get("routing", "orthogonal")
            if mode not in ("straight", "orthogonal", "curve"):
                raise ValueError("Connection routing must be straight/orthogonal/curve")
            if item.get("waypoints") is not None:
                route = [list(start_point), *item["waypoints"], list(end_point)]
            elif mode == "straight":
                route = [list(start_point), list(end_point)]
            else:
                obstacle_boxes = [element for element in scene["elements"] if element["type"] in ("rectangle", "ellipse", "diamond", "image", "embeddable")
                                  and (element.get("customData") or {}).get("agentDiagram", {}).get("role") not in ("container", "lane")]
                route = _route(start_point, end_point, start_port, end_port, obstacle_boxes)
            box = _bounds(route)
            operation = {"op": "connect", "ref": name, "from": source["id"], "to": target["id"],
                         "start": {"anchor": start_port, "mode": "orbit", **start}, "end": {"anchor": end_port, "mode": "orbit", **end},
                         "waypoints": route[1:-1], "elbowed": mode == "orthogonal", "style": {**geometry_style, "edge": "round" if mode == "curve" else "sharp"},
                         "startArrowhead": item.get("startArrowhead"), "endArrowhead": item.get("endArrowhead", "arrow"), "customData": data("connection", box)}
            if item.get("label"):
                operation["label"] = {"text": str(item["label"]), "style": {**text_style, "fontSize": 16, "labelPosition": float(item.get("labelPosition", 0.5))}}
            unit_ops.append(operation)
            unit_refs.append("@" + name)
            if mode == "curve":
                notes.append(f"{name}: spline collision checks remain unknown; inspect actual PNG and report limits")
        if item.get("label") and kind not in ("text", "connection", "callout", "code", "checkbox"):
            text, size = metrics.wrap(str(item["label"]), max(box["width"], 160), text_style["fontSize"])
            caption_ref = name + ":caption"
            unit_ops.append({"op": "create_text", "ref": caption_ref, "x": box["x"] + (box["width"] - size["width"]) / 2,
                             "y": box["y"] + box["height"] + 12, "text": text, "style": text_style, "customData": data("caption")})
            unit_refs.append("@" + caption_ref)
        if len(unit_refs) > 1:
            unit_ops.append({"op": "group", "targets": unit_refs})
        operations.extend(unit_ops)
        refs[name] = name
        measured[name] = {"kind": kind, "compoundBounds": box, "instanceId": unit}
    current = client.request("POST", "/v3/context", {"contextToken": context_token, "includeElements": False})
    if current["revision"] != context["revision"]:
        raise ValueError("Canvas changed while primitives were being measured")
    if len(operations) > 500:
        raise ValueError("Primitive plan exceeds the bridge operation limit; split explicit batches")
    return {"ok": True, "contextToken": context_token, "baseRevision": context["revision"], "operations": operations,
            "refs": refs, "measuredBounds": measured, "operationCount": len(operations), "notes": notes,
            "anchors": anchors, "manifests": manifests}
