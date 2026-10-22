"""Deterministic teaching encodings, emitted as ordinary editable native elements."""

from __future__ import annotations

from copy import deepcopy
from illustration_geometry import number

KINDS = (
    "sequence_window",
    "matrix_groups",
    "bitwidth_compare",
    "memory_map",
    "time_steps",
)
COLORS = {
    "ink": "#334155",
    "kept": "#d8e8dc",
    "new": "#f5d3a8",
    "sink": "#b9d9e8",
    "off": "#eef0f2",
    "outlier": "#e8b0a1",
}


def plan_teaching(item: dict, style: dict | None = None) -> dict:
    kind, identity = item.get("kind"), item.get("id")
    fields = {
        "sequence_window": {"tokens", "window", "sinks", "step", "show_mask"},
        "matrix_groups": {"values", "group_by", "outlier_threshold"},
        "bitwidth_compare": {"count", "bits"},
        "memory_map": {"mapping", "physical_count", "block_tokens"},
        "time_steps": {"tokens", "steps"},
    }
    if kind not in KINDS or not isinstance(identity, str) or not identity:
        raise ValueError("teaching primitive requires supported kind and nonempty id")
    unknown = (
        set(item) - {"id", "kind", "x", "y", "cell", "style", "label"} - fields[kind]
    )
    if unknown:
        raise ValueError(f"{identity}: unsupported teaching fields {sorted(unknown)}")
    x, y = number(item.get("x", 0), "x"), number(item.get("y", 0), "y")
    cell = number(item.get("cell", 38), "cell", 26)
    visual = {
        "roughness": 0,
        "strokeWidth": 1,
        "strokeColor": COLORS["ink"],
        "fillStyle": "solid",
        "roundness": None,
        **(style or {}),
    }
    spec = {k: deepcopy(v) for k, v in item.items() if k not in ("style", "label")}
    ops, labels = [], []
    points = []

    def integer(value, name, maximum=24):
        if type(value) is not int or value < 1 or value > maximum:
            raise ValueError(f"{name} must be an integer in 1..{maximum}")
        return value

    def strings(value, name):
        if (
            not isinstance(value, list)
            or not value
            or len(value) > 12
            or any(
                not isinstance(v, str) or not v.strip() or len(v) > 12 for v in value
            )
        ):
            raise ValueError(f"{name}: 1..12 short nonempty labels required")
        return value

    def label(part, text, px, py, width, center=False):
        labels.append(
            {
                "ref": identity + ":" + part,
                "text": str(text),
                "x": px,
                "y": py,
                "width": width,
                "center": center,
            }
        )

    def rect(part, px, py, width, height, state="off", label_text=None):
        op = {
            "op": "create_shape",
            "ref": identity + ":" + part,
            "type": "rectangle",
            "x": px,
            "y": py,
            "width": width,
            "height": height,
            "style": {**visual, "backgroundColor": COLORS[state]},
        }
        ops.append(op)
        points.extend([(px, py), (px + width, py + height)])
        if label_text is not None:
            label(
                part + ":label",
                label_text,
                px + width / 2,
                py + height / 2,
                width - 4,
                True,
            )

    def wire(part, vertices):
        px, py = vertices[0]
        ops.append(
            {
                "op": "create_linear",
                "ref": identity + ":" + part,
                "kind": "arrow",
                "x": px,
                "y": py,
                "points": [[a - px, b - py] for a, b in vertices],
                "startArrowhead": None,
                "endArrowhead": "arrow",
                "elbowed": False,
                "style": {
                    **visual,
                    "backgroundColor": "transparent",
                    "roundness": None,
                },
            }
        )
        points.extend(vertices)

    if kind == "sequence_window":
        tokens = strings(item.get("tokens"), "tokens")
        n = len(tokens)
        window = integer(item.get("window"), "window", n)
        sinks = item.get("sinks", 0)
        step = item.get("step", n - 1)
        if (
            type(sinks) is not int
            or not 0 <= sinks <= n
            or type(step) is not int
            or not 0 <= step < n
        ):
            raise ValueError("sinks/step must be valid token indices/counts")
        for i, token in enumerate(tokens):
            state = (
                "off"
                if i > step
                else "sink"
                if i < sinks
                else "kept"
                if i >= step - window + 1
                else "off"
            )
            rect(f"token:{i}", x + i * (cell + 5), y, cell, cell, state, token)
        label(
            "key",
            "sink / retained / discarded or future",
            x,
            y + cell + 12,
            n * (cell + 5),
        )
        if item.get("show_mask", True):
            if type(item.get("show_mask", True)) is not bool:
                raise ValueError("show_mask must be boolean")
            top = y + cell + 65
            label("mask-title", "Query rows × Key columns", x, top - 30, n * (cell + 5))
            for r in range(n):
                for c in range(n):
                    state = (
                        "sink"
                        if c <= r and c < sinks
                        else "kept"
                        if c <= r and c >= r - window + 1
                        else "off"
                    )
                    rect(
                        f"mask:{r}:{c}",
                        x + c * (cell + 3),
                        top + r * (cell + 3),
                        cell,
                        cell,
                        state,
                    )
        semantics = {"window": window, "sinks": sinks, "step": step}
    elif kind == "matrix_groups":
        values = item.get("values")
        if (
            not isinstance(values, list)
            or not values
            or len(values) > 8
            or not isinstance(values[0], list)
            or not values[0]
            or len(values[0]) > 8
        ):
            raise ValueError("values needs a 1..8 by 1..8 rectangular numeric matrix")
        cols = len(values[0])
        if any(not isinstance(row, list) or len(row) != cols for row in values):
            raise ValueError("matrix rows must have equal length")
        values = [[number(v, "matrix value") for v in row] for row in values]
        axis = item.get("group_by")
        if axis not in ("row", "column"):
            raise ValueError("group_by must be row or column")
        threshold = number(item.get("outlier_threshold", 8), "outlier_threshold", 0.001)
        stride = cell + 8
        for r, row in enumerate(values):
            for c, v in enumerate(row):
                rect(
                    f"value:{r}:{c}",
                    x + c * stride,
                    y + r * stride,
                    cell,
                    cell,
                    "outlier" if abs(v) >= threshold else "kept",
                    f"{v:g}",
                )
        if axis == "column":
            for c in range(cols):
                rect(f"group:{c}", x + c * stride, y - 16, cell, 6, "sink")
                label(f"scale:{c}", f"s{c}", x + c * stride, y - 45, cell)
        else:
            for r in range(len(values)):
                rect(f"group:{r}", x - 16, y + r * stride, 6, cell, "sink")
                label(f"scale:{r}", f"s{r}", x - 55, y + r * stride + 8, 32)
        semantics = {"group_by": axis, "outlier_threshold": threshold}
    elif kind == "bitwidth_compare":
        count = integer(item.get("count", 4), "count", 8)
        bits = item.get("bits")
        if (
            not isinstance(bits, list)
            or not 2 <= len(bits) <= 4
            or len(set(bits)) != len(bits)
        ):
            raise ValueError("bits needs 2..4 distinct bit widths")
        for i, bitsize in enumerate(bits):
            integer(bitsize, "bit width", 32)
            yy = y + i * (cell + 80)
            label(f"width:{i}", f"{bitsize} bit / value", x, yy - 27, 180)
            for v in range(count):
                for bit in range(bitsize):
                    rect(
                        f"bits:{i}:{v}:{bit}",
                        x + (v * bitsize + bit) * 6 + v * 8,
                        yy,
                        6,
                        cell,
                        "new" if i == 0 else "kept",
                    )
            label(
                f"total:{i}",
                f"{count} values = {count * bitsize} bits",
                x,
                yy + cell + 8,
                300,
            )
        semantics = {"count": count, "bits": bits}
    elif kind == "memory_map":
        mapping = item.get("mapping")
        physical_count = integer(item.get("physical_count"), "physical_count", 12)
        block_tokens = integer(item.get("block_tokens", 4), "block_tokens", 32)
        if (
            not isinstance(mapping, list)
            or not mapping
            or len(mapping) > 8
            or any(type(v) is not int or not 0 <= v < physical_count for v in mapping)
        ):
            raise ValueError("mapping needs valid physical block indices")
        stride = cell + 18
        label("logical-title", "Logical blocks", x, y - 32, 150)
        label("table-title", "Block Table", x + 180, y - 32, 150)
        label("pool-title", "Physical pool", x + 430, y - 32, 200)
        for p in range(physical_count):
            logical = [str(i) for i, v in enumerate(mapping) if v == p]
            rect(
                f"physical:{p}",
                x + 430,
                y + p * stride,
                170,
                cell,
                "kept" if logical else "off",
                f"P{p}" + (" ← L" + ",".join(logical) if logical else " free"),
            )
        for logical, p in enumerate(mapping):
            yy = y + logical * stride
            rect(f"logical:{logical}", x, yy, 125, cell, "sink", f"L{logical}")
            wire(
                f"lookup:{logical}",
                [(x + 125, yy + cell / 2), (x + 176, yy + cell / 2)],
            )
            rect(
                f"table:{logical}", x + 180, yy, 140, cell, "sink", f"L{logical} → P{p}"
            )
            wire(
                f"map:{logical}",
                [
                    (x + 320, yy + cell / 2),
                    (x + 350 + logical * 18, yy + cell / 2),
                    (x + 350 + logical * 18, y + p * stride + cell / 2),
                    (x + 426, y + p * stride + cell / 2),
                ],
            )
        label(
            "block-size",
            f"Each block holds {block_tokens} tokens (schematic)",
            x,
            y + physical_count * stride + 4,
            600,
        )
        semantics = {
            "mapping": mapping,
            "physical_count": physical_count,
            "block_tokens": block_tokens,
        }
    else:
        tokens = strings(item.get("tokens"), "tokens")
        steps = item.get("steps")
        if not isinstance(steps, list) or not steps or len(steps) > 8:
            raise ValueError("steps needs 1..8 named states")
        seen = set()
        for i, step in enumerate(steps):
            if (
                not isinstance(step, dict)
                or set(step) != {"id", "active", "reused"}
                or not isinstance(step["id"], str)
                or not step["id"]
                or step["id"] in seen
            ):
                raise ValueError("steps need unique id and active/reused index lists")
            seen.add(step["id"])
            active, reused = step["active"], step["reused"]
            if any(
                not isinstance(v, list)
                or len(set(v)) != len(v)
                or any(type(t) is not int or not 0 <= t < len(tokens) for t in v)
                for v in (active, reused)
            ) or set(active) & set(reused):
                raise ValueError(
                    "active/reused token indices must be valid, unique and disjoint"
                )
            label(
                f"step:{step['id']}", step["id"], x - 105, y + i * (cell + 14) + 8, 95
            )
            for t in range(len(tokens)):
                rect(
                    f"state:{step['id']}:{t}",
                    x + t * (cell + 5),
                    y + i * (cell + 14),
                    cell,
                    cell,
                    "new" if t in active else "kept" if t in reused else "off",
                )
        for i, token in enumerate(tokens):
            label(f"token:{i}", token, x + i * (cell + 5), y - 32, cell)
        semantics = {"steps": steps, "tokens": tokens}
    if len(ops) + len(labels) > 450:
        raise ValueError(
            "Teaching component exceeds bounded native operation size; split panels"
        )
    for op in ops:
        part = op["ref"][len(identity) + 1 :]
        op["customData"] = {
            "agentPrimitive": {
                "instanceId": "teaching:" + identity,
                "kind": kind,
                "role": "detail",
            },
            "agentDiagram": {"logicalId": identity, "role": "teaching-encoding"},
            "teaching": {
                "component": identity,
                "kind": kind,
                "part": part,
                "spec": spec,
            },
        }
    return {
        "operations": ops,
        "labels": labels,
        "semantics": semantics,
        "bounds": {
            "x": min(p[0] for p in points),
            "y": min(p[1] for p in points),
            "width": max(p[0] for p in points) - min(p[0] for p in points),
            "height": max(p[1] for p in points) - min(p[1] for p in points),
        },
    }
