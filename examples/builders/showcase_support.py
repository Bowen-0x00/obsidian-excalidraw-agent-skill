"""Shared example authoring helpers; all construction/rendering uses DrawingClient.

This is not a scene language, renderer or automatic layout engine. Coordinates and
semantics belong to the individual authored examples. Fonts are host-discovered.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "runtime"))
from diagram_layout import Metrics


class Scene:
    def __init__(self, client, context, font, name):
        self.client, self.context, self.font, self.name = client, context, font, name
        self.ops, self.expected, self.details = [], [], {}
        self.tables = []
        self.metrics = Metrics(client, context["contextToken"], font)
        self._metrics = {font: self.metrics}
        self._units = {}
        self.description = ""
        self.scope = ""

    def meta(self, key, unit=None, container=False):
        result = {
            "agentDiagram": {
                "diagramId": self.name,
                "logicalId": key,
                "role": "container" if container else "body",
            }
        }
        if container:
            result["isContainer"] = True
        if unit:
            result["agentPrimitive"] = {
                "instanceId": self.name + ":" + unit,
                "role": "body",
            }
            self._units.setdefault(unit, []).append("@" + key)
        return result

    def text(
        self,
        key,
        value,
        x,
        y,
        size=24,
        color="#243443",
        *,
        font=None,
        center=None,
        bold=False,
        unit=None,
    ):
        family = font or self.font
        if family not in self._metrics:
            self._metrics[family] = Metrics(
                self.client, self.context["contextToken"], family
            )
        measured = self._metrics[family].size(value, size, 1.25)
        if center is not None:
            x = center - measured["width"] / 2
        self.ops.append(
            {
                "op": "create_text",
                "ref": key,
                "x": x,
                "y": y,
                "text": value,
                "style": {
                    "fontFamily": family,
                    "fontSize": size,
                    "lineHeight": 1.25,
                    "strokeColor": color,
                },
                "customData": self.meta(key, unit),
            }
        )
        if bold:
            self.ops.append(
                {"op": "set_text_global_style", "targets": ["@" + key], "bold": True}
            )
        self.expected.append({"type": "label_equals", "id": key, "text": value})
        return {"x": x, "y": y, **measured}

    def shape(
        self,
        key,
        kind,
        x,
        y,
        w,
        h,
        *,
        fill="transparent",
        stroke="#243443",
        width=2,
        roughness=0,
        fill_style="solid",
        radius=0,
        opacity=100,
        unit=None,
        container=False,
        angle=0,
    ):
        self.ops.append(
            {
                "op": "create_shape",
                "ref": key,
                "type": kind,
                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "style": {
                    "backgroundColor": fill,
                    "strokeColor": stroke,
                    "strokeWidth": width,
                    "roughness": roughness,
                    "fillStyle": fill_style,
                    "opacity": opacity,
                    "angle": angle,
                    "roundness": {"type": 3, "value": radius, "roundType": "arc"}
                    if radius
                    else None,
                },
                "customData": self.meta(key, unit, container),
            }
        )
        return key

    def rect(self, key, x, y, w, h, **style):
        return self.shape(key, "rectangle", x, y, w, h, **style)

    def ellipse(self, key, x, y, w, h, **style):
        return self.shape(key, "ellipse", x, y, w, h, **style)

    def path(
        self,
        key,
        points,
        *,
        color="#243443",
        width=2,
        fill="transparent",
        roughness=0,
        fill_style="solid",
        closed=False,
        curve=False,
        dashed=False,
        opacity=100,
        unit=None,
        arrow=False,
        end="triangle",
        start=None,
    ):
        x, y = points[0]
        op = {
            "op": "create_linear",
            "ref": key,
            "kind": "arrow" if arrow else "line",
            "x": x,
            "y": y,
            "points": [[px - x, py - y] for px, py in points],
            "polygon": closed,
            "closed": closed,
            "style": {
                "strokeColor": color,
                "backgroundColor": fill,
                "strokeWidth": width,
                "roughness": roughness,
                "fillStyle": fill_style,
                "strokeStyle": "dashed" if dashed else "solid",
                "opacity": opacity,
                "roundness": {"type": 2, "value": 18} if curve else None,
            },
            "customData": self.meta(key, unit),
        }
        if arrow:
            op.update(startArrowhead=start, endArrowhead=end, elbowed=False)
        self.ops.append(op)
        return key

    def line(self, key, points, **style):
        return self.path(key, points, **style)

    def polygon(self, key, points, **style):
        return self.path(key, points, closed=True, **style)

    def arrow(self, key, points, **style):
        return self.path(key, points, arrow=True, **style)

    def latex(self, key, tex, x, y, scale=1, unit=None):
        self.ops.append(
            {
                "op": "create_latex",
                "ref": key,
                "tex": tex,
                "x": x,
                "y": y,
                "scaleX": scale,
                "scaleY": scale,
                "customData": self.meta(key, unit),
            }
        )
        return key

    def table(
        self,
        key,
        x,
        y,
        rows,
        cols,
        cell_width,
        cell_height,
        cells,
        *,
        theme,
        border,
        column_widths=None,
    ):
        """Native table request; host manager owns palette, borders and reflow."""
        options = {
            "x": x,
            "y": y,
            "rows": rows,
            "cols": cols,
            "cellWidth": cell_width,
            "cellHeight": cell_height,
            "cells": cells,
            "style": {"fontFamily": self.font, "fontSize": 20, "lineHeight": 1.25},
        }
        if column_widths is not None:
            options["columnWidths"] = column_widths
        self.tables.append(
            {
                "action": "create",
                "ref": key,
                "options": options,
                "theme": theme,
                "border": border,
            }
        )
        return key

    def finish(self):
        for unit, targets in self._units.items():
            if len(targets) > 1:
                self.ops.append(
                    {"op": "group", "ref": "group:" + unit, "targets": targets}
                )
        return self.ops
