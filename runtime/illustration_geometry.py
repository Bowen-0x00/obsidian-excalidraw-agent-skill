"""Small deterministic construction helpers; output is ordinary native operations."""

from __future__ import annotations

import math
from copy import deepcopy

KINDS = ("projected_box", "layer_stack", "grid_array", "leader")


def number(value, name, minimum=None):
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
    ):
        raise ValueError(f"{name} must be finite")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    return float(value)


def pair(value, name):
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError(f"{name} needs two coordinates")
    return [number(v, name) for v in value]


def project(origin, projection, u, v, z):
    return [origin[0] + u + projection[0] * v, origin[1] + projection[1] * v - z]


def plan_geometry(item: dict, geometry_style: dict) -> dict:
    kind, identity = item.get("kind"), item.get("id")
    common = {
        "kind",
        "id",
        "x",
        "y",
        "style",
        "label",
        "objectId",
        "viewId",
        "z",
        "u",
        "v",
    }
    fields = {
        "projected_box": {"width", "depth", "height", "projection", "faceColors"},
        "layer_stack": {"width", "depth", "view", "projection", "layers", "gap"},
        "grid_array": {"rows", "cols", "pitch", "size", "shape", "projection"},
        "leader": {"points", "target", "targetObject", "endArrowhead"},
    }
    if kind not in KINDS or not isinstance(identity, str) or not identity:
        raise ValueError("technical primitive needs a supported kind and nonempty id")
    if set(item) - common - fields[kind]:
        raise ValueError(
            f"{identity}: unsupported fields {sorted(set(item) - common - fields[kind])}"
        )
    origin = [number(item.get("x", 0), "x"), number(item.get("y", 0), "y")]
    projection = pair(item.get("projection", [0.65, -0.45]), "projection")
    if kind in ("projected_box", "layer_stack") and (
        projection[0] <= 0 or projection[1] >= 0
    ):
        raise ValueError(
            "oblique projection requires positive rightward x and negative upward y depth axes"
        )
    operations, anchors, objects = [], {}, []
    all_points = []
    style = {
        "roughness": 0,
        "strokeWidth": 1.2,
        "strokeColor": "#475569",
        "backgroundColor": "#cbd5e1",
        "fillStyle": "solid",
        "roundness": None,
        **geometry_style,
    }
    unit = "illustration:" + str(item.get("viewId", "main")) + ":" + identity

    def emit(ref, op, points, obj, model=None, role="body"):
        all_points.extend(points)
        expected = {
            k: deepcopy(op[k])
            for k in ("x", "y", "width", "height", "points")
            if k in op
        }
        meta = {
            "itemId": identity,
            "objectId": obj,
            "viewId": item.get("viewId", "main"),
            "role": role,
            "expected": expected,
            "model": model,
            "origin": origin,
            "projection": projection,
        }
        op.update(
            ref=ref,
            customData={
                "agentPrimitive": {"instanceId": unit, "kind": kind, "role": "face"},
                "agentDiagram": {"logicalId": obj, "role": "physical-" + role},
                "technicalIllustration": meta,
            },
        )
        operations.append(op)

    def polygon(ref, points, color, obj, model):
        points = [*points, points[0]]
        x, y = points[0]
        emit(
            ref,
            {
                "op": "create_linear",
                "kind": "line",
                "x": x,
                "y": y,
                "points": [[px - x, py - y] for px, py in points],
                "polygon": True,
                "closed": True,
                "style": {**style, "backgroundColor": color},
            },
            points,
            obj,
            model,
        )

    def box(ref, width, depth, height, base, obj, colors, view="oblique"):
        u, v = number(item.get("u", 0), "u"), number(item.get("v", 0), "v")
        model = {
            "u": u,
            "v": v,
            "z": base,
            "width": width,
            "depth": depth,
            "height": height,
        }
        p = lambda a, b, c: project(origin, projection, u + a, v + b, base + c)
        if view == "section":
            x, y = origin[0] + u, origin[1] - base - height
            emit(
                ref,
                {
                    "op": "create_shape",
                    "type": "rectangle",
                    "x": x,
                    "y": y,
                    "width": width,
                    "height": height,
                    "style": {
                        **style,
                        "backgroundColor": colors.get(
                            "front", style["backgroundColor"]
                        ),
                    },
                },
                [[x, y], [x + width, y + height]],
                obj,
                model,
            )
            a = {
                "top": [x + width / 2, y],
                "front": [x + width / 2, y + height / 2],
                "right": [x + width, y + height / 2],
                "center": [x + width / 2, y + height / 2],
            }
        else:
            polygon(
                ref + ":front",
                [p(0, 0, 0), p(width, 0, 0), p(width, 0, height), p(0, 0, height)],
                colors.get("front", style["backgroundColor"]),
                obj,
                model,
            )
            polygon(
                ref + ":side",
                [
                    p(width, 0, 0),
                    p(width, depth, 0),
                    p(width, depth, height),
                    p(width, 0, height),
                ],
                colors.get("side", style["backgroundColor"]),
                obj,
                model,
            )
            polygon(
                ref + ":top",
                [
                    p(0, 0, height),
                    p(width, 0, height),
                    p(width, depth, height),
                    p(0, depth, height),
                ],
                colors.get("top", style["backgroundColor"]),
                obj,
                model,
            )
            a = {
                "top": p(width / 2, depth / 2, height),
                "front": p(width / 2, 0, height / 2),
                "right": p(width, depth / 2, height / 2),
                "center": p(width / 2, depth / 2, height / 2),
            }
        for name, point in a.items():
            anchors[ref + ":" + name] = point
        objects.append({"id": obj, "ref": ref, "model": model, "anchors": a})

    if kind == "projected_box":
        width, depth, height = [
            number(item.get(k), k, 0.001) for k in ("width", "depth", "height")
        ]
        colors = item.get("faceColors", {})
        if not isinstance(colors, dict) or set(colors) - {"front", "side", "top"}:
            raise ValueError("faceColors supports top/front/side")
        box(
            identity,
            width,
            depth,
            height,
            number(item.get("z", 0), "z"),
            item.get("objectId", identity),
            colors,
        )
    elif kind == "layer_stack":
        view = item.get("view", "section")
        if view not in ("section", "oblique"):
            raise ValueError("layer_stack view must be section or oblique")
        width = number(item.get("width"), "width", 0.001)
        depth = number(
            item.get("depth", 1 if view == "section" else None), "depth", 0.001
        )
        layers = item.get("layers")
        if not isinstance(layers, list) or not layers:
            raise ValueError("layers is a nonempty bottom-to-top list")
        ids = set()
        z = number(item.get("z", 0), "z")
        gap = number(item.get("gap", 0), "gap", 0)
        for layer in layers:
            if (
                not isinstance(layer, dict)
                or set(layer) - {"id", "height", "color", "faceColors", "objectId"}
                or not isinstance(layer.get("id"), str)
                or not layer["id"]
                or layer["id"] in ids
            ):
                raise ValueError(
                    "each layer needs a unique id, height, optional color/faceColors/objectId"
                )
            ids.add(layer["id"])
            h = number(layer.get("height"), "layer.height", 0.001)
            color = layer.get("color", style["backgroundColor"])
            box(
                identity + ":" + layer["id"],
                width,
                depth,
                h,
                z,
                layer.get("objectId", layer["id"]),
                {
                    "front": color,
                    "top": color,
                    "side": color,
                    **layer.get("faceColors", {}),
                },
                view,
            )
            z += h + gap
        expected_refs = [op["ref"] for op in operations]
        for op in operations:
            op["customData"]["technicalIllustration"]["constructionRefs"] = (
                expected_refs
            )
    elif kind == "grid_array":
        rows, cols = item.get("rows"), item.get("cols")
        if any(type(v) is not int or v < 1 for v in (rows, cols)) or rows * cols > 200:
            raise ValueError(
                "rows/cols must be positive integers with at most 200 cells"
            )
        px, py = pair(item.get("pitch"), "pitch")
        w, h = pair(item.get("size"), "size")
        if min(px, py, w, h) <= 0 or (cols > 1 and px < w) or (rows > 1 and py < h):
            raise ValueError(
                "positive pitch/size and non-overlapping repeated rows/columns required"
            )
        shape = item.get("shape", "ellipse")
        if shape not in ("rectangle", "ellipse"):
            raise ValueError("grid shape must be rectangle or ellipse")
        for row in range(rows):
            for col in range(cols):
                x, y = (
                    project(origin, projection, col * px, row * py, 0)
                    if "projection" in item
                    else [origin[0] + col * px, origin[1] + row * py]
                )
                emit(
                    f"{identity}:{row}:{col}",
                    {
                        "op": "create_shape",
                        "type": shape,
                        "x": x,
                        "y": y,
                        "width": w,
                        "height": h,
                        "style": style,
                    },
                    [[x, y], [x + w, y + h]],
                    item.get("objectId", identity),
                    role="detail",
                )
                for previous in operations[:-1]:
                    if (
                        abs(x - previous["x"]) < w - 0.001
                        and abs(y - previous["y"]) < h - 0.001
                    ):
                        raise ValueError(
                            "projected array cells overlap; increase pitch or reduce cell size"
                        )
                anchors[f"{row}:{col}"] = [x + w / 2, y + h / 2]
        expected_refs = [op["ref"] for op in operations]
        for op in operations:
            op["customData"]["technicalIllustration"]["constructionRefs"] = (
                expected_refs
            )
        objects.append(
            {"id": item.get("objectId", identity), "rows": rows, "cols": cols}
        )
    else:
        points = [pair(p, "leader.points") for p in item.get("points", [])]
        if (
            len(points) < 2
            or sum(math.dist(a, b) for a, b in zip(points, points[1:])) < 0.001
        ):
            raise ValueError("leader requires a nonzero path with at least two points")
        target = pair(item.get("target", points[-1]), "target")
        if math.dist(points[-1], target) > 1:
            raise ValueError("leader endpoint misses its declared target")
        x, y = points[0]
        emit(
            identity,
            {
                "op": "create_linear",
                "kind": "arrow",
                "x": x,
                "y": y,
                "points": [[px - x, py - y] for px, py in points],
                "endArrowhead": item.get("endArrowhead", "arrow"),
                "startArrowhead": None,
                "elbowed": False,
                "style": {**style, "backgroundColor": "transparent"},
            },
            points,
            item.get("objectId", identity),
            role="annotation",
        )
        operations[-1]["customData"]["technicalIllustration"].update(
            target=target, targetObject=item.get("targetObject")
        )
        anchors.update(start=points[0], end=points[-1])
    if len(operations) > 500:
        raise ValueError("technical primitive exceeds 500 native operations")
    xs, ys = [p[0] for p in all_points], [p[1] for p in all_points]
    return {
        "operations": operations,
        "bounds": {
            "x": min(xs),
            "y": min(ys),
            "width": max(xs) - min(xs),
            "height": max(ys) - min(ys),
        },
        "anchors": anchors,
        "manifest": {
            "kind": kind,
            "objects": objects,
            "layerOrder": [o["id"] for o in objects] if kind == "layer_stack" else [],
        },
        "notes": [
            "2D schematic projection; thickness and repeated counts are illustrative unless sourced"
        ],
    }
