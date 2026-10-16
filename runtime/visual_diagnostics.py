"""Conservative, paint-order-aware text legibility risks, not glyph/pixel proofs.

Text line boxes deliberately use native dimensions, never character-count widths.
Rotated/spline/image-alpha cases remain candidates for actual PNG adjudication.
"""
from __future__ import annotations

import math
from typing import Any


def is_visible(element: dict) -> bool:
    return (not element.get("isDeleted") and float(element.get("opacity", 100)) > 0
            and not (element.get("customData") or {}).get("hide"))


def _box(e: dict, inset: float = 0) -> tuple[float, float, float, float]:
    x, y = float(e.get("x", 0)), float(e.get("y", 0))
    w, h = float(e.get("width", 0)), float(e.get("height", 0))
    a = float(e.get("angle", 0))
    rw, rh = abs(w * math.cos(a)) + abs(h * math.sin(a)), abs(w * math.sin(a)) + abs(h * math.cos(a))
    return x + w / 2 - rw / 2 + inset, y + h / 2 - rh / 2 + inset, x + w / 2 + rw / 2 - inset, y + h / 2 + rh / 2 - inset


def _contains(outer, inner) -> bool:
    return outer[0] <= inner[0] and outer[1] <= inner[1] and outer[2] >= inner[2] and outer[3] >= inner[3]


def _overlap(a, b) -> bool:
    return min(a[2], b[2]) - max(a[0], b[0]) > 1.5 and min(a[3], b[3]) - max(a[1], b[1]) > 1.5


def _crosses(a, b, box) -> bool:
    lo, hi = 0.0, 1.0
    for origin, delta, minimum, maximum in ((a[0], b[0] - a[0], box[0], box[2]), (a[1], b[1] - a[1], box[1], box[3])):
        if abs(delta) < 1e-9:
            if origin <= minimum or origin >= maximum:
                return False
        else:
            first, last = sorted(((minimum - origin) / delta, (maximum - origin) / delta))
            lo, hi = max(lo, first), min(hi, last)
            if lo >= hi:
                return False
    return True


def _points(e: dict) -> list[tuple[float, float]]:
    points = [(float(e.get("x", 0)) + p[0], float(e.get("y", 0)) + p[1]) for p in e.get("points", [])]
    if not points:
        return []
    cx, cy = (min(p[0] for p in points) + max(p[0] for p in points)) / 2, (min(p[1] for p in points) + max(p[1] for p in points)) / 2
    c, s = math.cos(float(e.get("angle", 0))), math.sin(float(e.get("angle", 0)))
    return [(cx + (x - cx) * c - (y - cy) * s, cy + (x - cx) * s + (y - cy) * c) for x, y in points]


def _solid(e: dict) -> bool:
    color = str(e.get("backgroundColor", "transparent")).lower().strip()
    return (e.get("type") == "rectangle" and not e.get("angle") and float(e.get("opacity", 100)) >= 99
            and e.get("fillStyle", "solid") == "solid" and color not in ("", "transparent", "none")
            and not color.startswith(("rgba", "hsla")) and len(color) not in (5, 9)
            and not (e.get("customData") or {}).get("gradient"))


def _bands(text: dict) -> list[tuple]:
    if not str(text.get("text", "")).strip() or float(text.get("width", 0)) <= 2 or float(text.get("height", 0)) <= 2:
        return []
    if text.get("angle"):
        return [_box(text, 1)]
    lines = str(text["text"]).split("\n")
    line_height = float(text["height"]) / len(lines)
    x, y, right, _ = _box(text)
    inset = min(2.0, line_height * 0.12)
    return [(x + 1, y + i * line_height + inset, right - 1, y + (i + 1) * line_height - inset)
            for i, line in enumerate(lines) if line.strip()]


def _risk(code: str, ids: list[str], message: str, hint: str, *, severity: str = "warning", **extra) -> dict:
    return {"code": code, "severity": severity, "elementIds": ids, "message": message, "repairHint": hint,
            "evidence": "paint_order_and_native_geometry", "confidence": "candidate", "visualReviewRequired": True, **extra}


def inspect_visual_conflicts(elements: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Find text/text, painted-over text and visible shaft/border-through-text risks.

    A background underneath text is legal. An unrelated line behind text is not
    automatically safe: glyphs do not make the whole text rectangle opaque.
    """
    active = [e for e in elements if is_visible(e)]
    text_rows = [(i, e, _bands(e)) for i, e in enumerate(active) if e.get("type") == "text"]
    opaque_panels = [(i, _box(e, 2)) for i, e in enumerate(active) if _solid(e)]
    issues = []
    for position, (ti, text, bands) in enumerate(text_rows):
        if not bands:
            continue
        for _, other, other_bands in text_rows[position + 1:]:
            if any(_overlap(a, b) for a in bands for b in other_bands):
                issues.append(_risk("TEXT_TEXT_OVERLAP", [text["id"], other["id"]],
                    "Native text line boxes intersect; inspect actual glyph legibility, not only element containment.",
                    "Separate the text, remeasure/wrap it, or resize the owning layout; do not delete required content.", severity="error"))
        for oi, obj in enumerate(active):
            if obj is text or obj.get("type") in ("text", "frame"):
                continue
            kind = obj.get("type")
            if kind in ("rectangle", "image", "embeddable") and oi > ti:
                if (_solid(obj) or kind in ("image", "embeddable")) and any(_overlap(_box(obj), band) for band in bands):
                    issues.append(_risk("TEXT_PAINTED_OVER", [text["id"], obj["id"]],
                        "A later painted object overlaps earlier text; z-order may hide its glyphs.",
                        "Put the background below its text or move the unrelated object; inspect image alpha and rounded corners.",
                        severity="error" if _solid(obj) else "warning"))
            segments = []
            if kind in ("line", "arrow"):
                # Bound labels are deliberately masked by their own native arrow.
                own_label = text.get("containerId") == obj.get("id") and any(b.get("id") == text["id"] and b.get("type") == "text" for b in obj.get("boundElements") or [])
                if own_label:
                    continue
                points = _points(obj)
                segments = list(zip(points, points[1:]))
            elif kind == "rectangle" and not obj.get("angle") and str(obj.get("strokeColor", "#000")).lower() != "transparent":
                left, top, right, bottom = _box(obj)
                segments = [((left, top), (right, top)), ((right, top), (right, bottom)), ((right, bottom), (left, bottom)), ((left, bottom), (left, top))]
            if not segments:
                continue
            stroke = max(0.0, float(obj.get("strokeWidth", 1))) / 2
            if kind == "arrow" and any(str(obj.get(k) or "").startswith("block_arrow") for k in ("startArrowhead", "endArrowhead")):
                shaft = (obj.get("customData") or {}).get("blockArrowWidth") or max(16, float(obj.get("strokeWidth", 1)) * 6)
                stroke = max(stroke, float(shaft) / 2)
            for band in bands:
                expanded = (band[0] - stroke, band[1] - stroke, band[2] + stroke, band[3] + stroke)
                if not any(_crosses(a, b, expanded) for a, b in segments):
                    continue
                # Only actual crossing candidates need the paint-mask scan.
                if oi < ti and any(oi < pi < ti and _contains(bounds, band) for pi, bounds in opaque_panels):
                    continue
                code = "LINE_THROUGH_TEXT" if kind in ("line", "arrow") else "BORDER_THROUGH_TEXT"
                issues.append(_risk(code, [obj["id"], text["id"]],
                    "A visible shaft or shape border intersects a text line region; check actual PNG for unreadable words.",
                    "Reroute the line or reposition/remeasure the text. A common group or container tag is not an occlusion exemption."))
                break
    return issues


def output_readability(elements: list[dict], scale: float | None) -> list[dict]:
    if scale is None:
        return []
    if not math.isfinite(scale) or scale <= 0:
        raise ValueError("Output scale must be positive and finite")
    small = [e for e in elements if is_visible(e) and e.get("type") == "text" and str(e.get("text", "")).strip() and float(e.get("fontSize", 20)) * scale < 10]
    if not small:
        return []
    return [_risk("SMALL_OUTPUT_TEXT", [e["id"] for e in small],
        "Some output text is below the 10px review trigger; this is not an automatic illegibility verdict.",
        "Inspect readable detail previews or adjust layout/output size; do not shrink text to hide collisions.",
        actual={"minimumOutputFontPx": round(min(float(e.get("fontSize", 20)) * scale for e in small), 2), "scale": scale})]
