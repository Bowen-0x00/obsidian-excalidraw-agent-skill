"""Measured scene -> native operation plan; no custom renderer or JSON scene dump."""
from __future__ import annotations

import copy
import math

from .model import DslError, port


class Compiler:
    def __init__(self, client, token, document, font):
        from diagram_layout import Metrics
        self.client, self.token, self.doc = client, token, document
        self.font = font
        self.metrics_class = Metrics
        self.metrics = {}
        self.entities, self.boxes, self.sizes, self.texts = {}, {}, {}, {}
        self.group_members, self.routes, self.expected = {}, {}, []
        self.port_labels = []
        discovery = client.context("discover")["capabilities"]
        self.fonts = discovery["fonts"]
        if self.fonts.get("error") or not self.fonts.get("registered"):
            raise DslError("style.font", "current backend font discovery unavailable")
        self.available = self.fonts["registered"]
        if font not in self.available:
            raise DslError("style.font", f"{font!r} is not in the current host list; run fonts first")
        self.base = {"stroke": "#475569", "fill": "#f8fafc", "text": "#16324f", "font_size": 20, "stroke_width": 1.5, "roughness": 0, **document.get("style", {}), "font": font}
        self.native_features = discovery.get("features", {})
        self.plan_revision = client.read(token, detail="full")["revision"]

    def visual(self, item):
        result = {**self.base, **self.doc.get("classes", {}).get(item.get("class"), {}), **item.get("style", {})}
        if result["font"] not in self.available:
            raise DslError("style.font", f"unavailable family {result['font']!r}")
        return result

    def native_style(self, item):
        v = self.visual(item)
        return {"strokeColor": v["stroke"], "backgroundColor": v["fill"], "fillStyle": "solid", "strokeWidth": v["stroke_width"], "strokeStyle": v.get("dash", "solid"), "roughness": v["roughness"], "roundness": {"type": 3, "value": 5, "roundType": "arc"}}

    def text_style(self, item, size=None):
        v = self.visual(item)
        return {"fontFamily": v["font"], "fontSize": size or v["font_size"], "strokeColor": v["text"], "lineHeight": 1.25}

    def measure(self, text, item, width=None, size=None):
        st = self.text_style(item, size)
        font = st["fontFamily"]
        if font not in self.metrics:
            self.metrics[font] = self.metrics_class(self.client, self.token, font)
        m = self.metrics[font]
        if width is None:
            return text, m.size(text, st["fontSize"], 1.25)
        return m.wrap(text, width, st["fontSize"], 1.25)

    def metadata(self, key, role="body", unit=None, **extra):
        return {"dsl": {"document": self.doc["id"], "key": key},
                "agentDiagram": {"diagramId": "dsl:" + self.doc["id"], "logicalId": key, "role": role},
                **({"agentPrimitive": {"instanceId": self.doc["id"] + ":" + unit, "role": "decoration"}} if unit else {}), **extra}

    def emit(self, key, op, role="body", unit=None, **metadata):
        if key in self.entities:
            raise DslError(key, "compiler produced duplicate identity")
        custom = self.metadata(key, role, unit, **metadata)
        op = {"ref": key, **op, "customData": custom}
        if isinstance(op.get("label"), dict):
            labelkey = key + ":label"
            op["label"]["customData"] = self.metadata(labelkey, "label", unit)
        self.entities[key] = op

    def size_node(self, name):
        n = self.doc["nodes"][name]
        kind = n.get("shape", "box")
        label = n.get("label", "")
        size = self.visual(n)["font_size"]
        width_limit = n.get("wrap", 230)
        wrapped, textsize = self.measure(label, n, width_limit)
        self.texts[name] = wrapped
        w, h = max(140, textsize["width"] + 36), max(68, textsize["height"] + 28)
        details = {}
        if kind == "diamond":
            h = max(132, (textsize["height"] + 30) * 2.2)
            w = max(210, (textsize["width"] + 32) / (1 - (textsize["height"] + 30) / h))
        elif kind == "ellipse":
            w = max(150, (textsize["width"] + 32) * 1.42)
            h = max(75, (textsize["height"] + 28) * 1.42)
        elif kind == "text":
            w, h = max(1, textsize["width"]), max(1, textsize["height"])
        elif kind in ("mux", "alu", "polygon"):
            w, h = max(w, 150), max(h, 125)
        elif kind == "table":
            rows = [[str(c) if c is not None else "" for c in row] for row in [n["columns"], *n["rows"]]]
            cellfont = min(size, 17)
            widths = []
            for c in range(len(rows[0])):
                widths.append(max(48, max(self.measure(row[c], n, size=cellfont)[1]["width"] for row in rows) + 20))
            heights = [max(34, max(self.measure(t, n, size=cellfont)[1]["height"] for t in row) + 14) for row in rows]
            titleh = textsize["height"] + 16 if label else 0
            w, h = sum(widths), sum(heights) + titleh
            w = max(w, textsize["width"] + 12)
            details = {"rows": rows, "widths": widths, "heights": heights, "titleh": titleh, "cellfont": cellfont}
        elif kind in ("image", "formula", "embed", "chart"):
            if "size" not in n:
                raise DslError("nodes." + name + ".size", "resource nodes require a reserved [width,height]")
            w, h = n["size"]
            details["contentHeight"] = h
            if kind in ("image", "formula"):
                request = {"contextToken": self.token, "kind": "latex" if kind == "formula" else "image",
                    **({"tex": n["tex"]} if kind == "formula" else {"source": n["source"]})}
                try:
                    resource = self.client.request("POST", "/v3/content/measure", request)
                except Exception as error:
                    raise DslError("nodes." + name, str(error)) from None
                factor = min(w / resource["width"], h / resource["height"])
                details.update(resourceWidth=resource["width"] * factor, resourceHeight=resource["height"] * factor)
            h += textsize["height"] + 14 if label else 0
        if "size" in n and kind not in ("image", "formula", "embed", "chart"):
            w, h = max(w, n["size"][0]), max(h, n["size"][1])
        self.sizes[name] = {"width": math.ceil(w), "height": math.ceil(h), **details}
        return w, h

    def layout_size(self, tree):
        if isinstance(tree, str):
            if tree in self.doc["nodes"]:
                if tree not in self.sizes:
                    self.size_node(tree)
                s = self.sizes[tree]
                return s["width"], s["height"]
            group = self.doc["groups"][tree]
            w, h = self.layout_size(group["layout"])
            padding = group.get("padding", 28)
            title, ms = self.measure(group.get("label", ""), group, max(w, 180), 22)
            header = ms["height"] + 34 if title else 8
            self.texts[tree] = title
            self.sizes[tree] = {"width": max(w + padding * 2, ms["width"] + padding * 2), "height": h + padding * 2 + header, "header": header}
            return self.sizes[tree]["width"], self.sizes[tree]["height"]
        gx, gy = self.gap(tree)
        if "flow" in tree:
            from diagram_layout import _layers
            nodes = {n: {} for n in self.doc["nodes"]}
            edges = [{"id": k, "from": v["from"].split(".")[0], "to": v["to"].split(".")[0]} for k, v in self.doc.get("edges", {}).items() if v.get("kind") not in ("feedback", "control")]
            layers, _ = _layers(nodes, edges)
            tree = {"column" if tree["flow"] == "down" else "row": [{"row" if tree["flow"] == "down" else "column": layer, "gap": [gx, gy]} for layer in layers], "gap": [gx, gy]}
            self.flow_tree = tree
        if "row" in tree:
            sizes = [self.layout_size(c) for c in tree["row"]]
            return sum(s[0] for s in sizes) + gx * (len(sizes) - 1), max(s[1] for s in sizes)
        if "column" in tree:
            sizes = [self.layout_size(c) for c in tree["column"]]
            return max(s[0] for s in sizes), sum(s[1] for s in sizes) + gy * (len(sizes) - 1)
        rows = tree["grid"]
        sizes = [[self.layout_size(c) if c else (0, 0) for c in row] for row in rows]
        widths = [max((row[i][0] if i < len(row) else 0) for row in sizes) for i in range(max(map(len, rows)))]
        heights = [max(s[1] for s in row) for row in sizes]
        return sum(widths) + gx * (len(widths) - 1), sum(heights) + gy * (len(heights) - 1)

    @staticmethod
    def gap(tree):
        g = tree.get("gap", [100, 90])
        return (g, g) if isinstance(g, (int, float)) else g

    def place(self, tree, x, y):
        if isinstance(tree, str):
            s = self.sizes[tree]
            if tree in self.doc["nodes"]:
                x, y = self.doc["nodes"][tree].get("at", [x, y])
                self.boxes[tree] = {"x": x, "y": y, "width": s["width"], "height": s["height"]}
                return [tree]
            g = self.doc["groups"][tree]
            self.boxes[tree] = {"x": x, "y": y, "width": s["width"], "height": s["height"]}
            children = self.place(g["layout"], x + g.get("padding", 28), y + g.get("padding", 28) + s["header"])
            self.group_members[tree] = children
            return [tree, *children]
        if "flow" in tree:
            tree = self.flow_tree
        gx, gy = self.gap(tree)
        allmembers = []
        if "row" in tree or "column" in tree:
            op = "row" if "row" in tree else "column"
            width, height = self.layout_size(tree)
            cx, cy = x, y
            for child in tree[op]:
                w, h = self.layout_size(child)
                allmembers.extend(self.place(child, cx + ((width - w) / 2 if op == "column" else 0), cy + ((height - h) / 2 if op == "row" else 0)))
                if op == "row":
                    cx += w + gx
                else:
                    cy += h + gy
        else:
            rows = tree["grid"]
            sizes = [[self.layout_size(c) if c else (0, 0) for c in row] for row in rows]
            widths = [max((row[i][0] if i < len(row) else 0) for row in sizes) for i in range(max(map(len, rows)))]
            heights = [max(s[1] for s in row) for row in sizes]
            cy = y
            for ri, row in enumerate(rows):
                cx = x
                for ci, child in enumerate(row):
                    if child:
                        w, h = sizes[ri][ci]
                        allmembers.extend(self.place(child, cx + (widths[ci] - w) / 2, cy + (heights[ri] - h) / 2))
                    cx += widths[ci] + gx
                cy += heights[ri] + gy
        return allmembers

    def emit_node(self, name):
        n, b, s = self.doc["nodes"][name], self.boxes[name], self.sizes[name]
        kind, label = n.get("shape", "box"), self.texts[name]
        key = "node." + name
        geom, textstyle = self.native_style(n), self.text_style(n)
        unit = "node:" + name
        shape = {"op": "create_shape", "type": {"box": "rectangle"}.get(kind, kind), **{k: b[k] for k in ("x", "y", "width", "height")}, "style": geom}
        content = kind in ("image", "formula", "embed", "chart")
        if kind == "text":
            self.emit(key, {"op": "create_text", "x": b["x"], "y": b["y"], "text": label, "style": textstyle}, "text")
        elif kind in ("mux", "alu", "polygon", "table"):
            # Invisible native rectangle is an editable binding anchor; not raster art.
            anchor = {**shape, "type": "rectangle", "style": {**geom, "strokeColor": "transparent", "backgroundColor": "transparent"}}
            self.emit(key, anchor, "container", unit, isContainer=True)
            if kind == "table":
                titleh = s["titleh"]
                if label:
                    self.emit(key + ":title", {"op": "create_text", "x": b["x"], "y": b["y"], "text": label, "style": textstyle}, "text", unit)
                y = b["y"] + titleh
                for ri, row in enumerate(s["rows"]):
                    x = b["x"]
                    for ci, cell in enumerate(row):
                        ckey = f"{key}:cell:{ri}:{ci}"
                        self.emit(ckey, {"op": "create_shape", "type": "rectangle", "x": x, "y": y, "width": s["widths"][ci], "height": s["heights"][ri],
                            "style": {**geom, "roundness": None, "backgroundColor": geom["strokeColor"] if ri == 0 else geom["backgroundColor"], "strokeWidth": 1},
                            "label": {"text": cell, "style": {**self.text_style(n, s["cellfont"]), **({"strokeColor": "#ffffff"} if ri == 0 else {})}, "padding": 5}}, "table-cell", unit)
                        x += s["widths"][ci]
                    y += s["heights"][ri]
            else:
                normalized = n.get("points") or ([[0, 0], [1, .16], [1, .84], [0, 1]] if kind == "mux" else [[0, 0], [1, .22], [1, .78], [0, 1], [0, .63], [.23, .5], [0, .37]])
                points = [[px * b["width"], py * b["height"]] for px, py in normalized]
                first = points[0]
                self.emit(key + ":outline", {"op": "create_linear", "kind": "line", "x": b["x"] + first[0], "y": b["y"] + first[1], "points": [[p[0] - first[0], p[1] - first[1]] for p in points], "polygon": True, "closed": True, "style": {**geom, "roundness": None}}, "body", unit)
                if label:
                    tx = b["x"] + (b["width"] - self.measure(label, n)[1]["width"]) / 2 + (b["width"] * .08 if kind == "alu" else 0)
                    self.emit(key + ":title", {"op": "create_text", "x": tx, "y": b["y"] + (b["height"] - self.measure(label, n)[1]["height"]) / 2, "text": label, "style": textstyle}, "text", unit)
        elif content:
            resourcebox = {**b, "height": s["contentHeight"]}
            if kind in ("image", "formula"):
                resourcebox = {**resourcebox, "x": b["x"] + (b["width"] - s["resourceWidth"]) / 2,
                    "y": b["y"] + (s["contentHeight"] - s["resourceHeight"]) / 2,
                    "width": s["resourceWidth"], "height": s["resourceHeight"]}
            if kind == "image":
                op = {"op": "create_image", "source": n["source"], **resourcebox}
            elif kind == "formula":
                op = {"op": "create_latex", "tex": n["tex"], "x": resourcebox["x"], "y": resourcebox["y"]}
            elif kind == "embed":
                op = {"op": "create_embeddable", "source": n["source"], **resourcebox}
            else:
                op = {**shape, "type": "rectangle", **resourcebox}
            self.emit(key, op, "body", unit)
            if label:
                self.emit(key + ":title", {"op": "create_text", "x": b["x"], "y": b["y"] + s["contentHeight"] + 12, "text": label, "style": textstyle}, "text", unit)
        else:
            if label:
                shape["label"] = {"text": label, "style": textstyle, "padding": 14}
            self.emit(key, shape, "body")
        if label and kind not in ("formula", "embed", "image", "chart", "table", "mux", "alu", "polygon"):
            self.expected.append({"type": "label_equals", "id": key if kind != "text" else key, "text": n.get("label", "")})
        for feature in n.get("features", {}):
            if not self.native_features.get(feature, {}).get("callable"):
                raise DslError("nodes." + name + ".features." + feature, "not callable on current host")
        if kind == "chart" and not self.native_features.get("echarts", {}).get("callable"):
            raise DslError("nodes." + name, "ECharts unavailable")
        for pname, pspec in n.get("ports", {}).items():
            side, ratio = port(pspec, "nodes." + name + ".ports." + pname)
            px = b["x"] + b["width"] * (0 if side == "left" else 1 if side == "right" else ratio)
            py = b["y"] + b["height"] * (0 if side == "top" else 1 if side == "bottom" else ratio)
            self.emit(key + ":port:" + pname, {"op": "create_shape", "type": "ellipse", "x": px - 2, "y": py - 2, "width": 4, "height": 4,
                "style": {**geom, "backgroundColor": geom["strokeColor"], "roundness": None}}, "message-port", unit)
            self.port_labels.append((key + ":port-label:" + pname, n, pname, side, px, py, unit))

    def edge_endpoint(self, value, default):
        bits = value.split(".")
        name, which = bits[0], bits[1] if len(bits) == 2 else default
        spec = self.doc["nodes"][name].get("ports", {}).get(which, which)
        side, ratio = port(spec, "endpoint." + value)
        fixed = {"left": [0, ratio], "right": [1, ratio], "top": [ratio, 0], "bottom": [ratio, 1]}[side]
        b = self.boxes[name]
        return name, side, fixed, [b["x"] + b["width"] * fixed[0], b["y"] + b["height"] * fixed[1]]

    def emit_edges(self):
        from diagram_layout import _route, _segment_clear
        obstacles = [self.boxes[name] for name in self.doc["nodes"]]
        # Container headers are real text obstacles; a container body is not.
        for name in self.doc.get("groups", {}):
            b = self.boxes[name]
            _, ms = self.measure(self.texts[name], self.doc["groups"][name], size=22)
            obstacles.append({"x": b["x"] + 20, "y": b["y"] + 14, "width": ms["width"], "height": ms["height"]})
        downward = self.doc.get("layout", {}).get("flow") == "down"
        for name, e in self.doc.get("edges", {}).items():
            source, ss, sf, sp = self.edge_endpoint(e["from"], "bottom" if downward else "right")
            target, ts, tf, tp = self.edge_endpoint(e["to"], "top" if downward else "left")
            try:
                if "via" in e:
                    route = [sp, *e["via"], tp]
                    if any(a[0] != b[0] and a[1] != b[1] for a, b in zip(route, route[1:])):
                        raise DslError("edges." + name + ".via", "all segments must be orthogonal")
                    boxes = [(b["x"] + 1, b["y"] + 1, b["x"] + b["width"] - 1, b["y"] + b["height"] - 1) for n, b in self.boxes.items() if n in self.doc["nodes"] and n not in (source, target)]
                    if any(not _segment_clear(tuple(a), tuple(b), boxes) for a, b in zip(route, route[1:])):
                        raise DslError("edges." + name + ".via", "explicit route crosses an unrelated node")
                else:
                    route = _route(tuple(sp), tuple(tp), ss, ts, obstacles, clearance=18)
            except ValueError as error:
                raise DslError("edges." + name, str(error)) from None
            self.routes[name] = route
            kind = e.get("kind", "data")
            defaults = {"stroke": "#2563eb", "fill": "transparent", "head": "triangle"}
            if kind == "control":
                defaults.update(stroke="#b45309", dash="dashed", head="arrow")
            elif kind == "feedback":
                defaults.update(stroke="#7c3aed")
            elif kind == "line":
                defaults.update(head="none")
            elif kind == "ppt":
                defaults.update(head="block_arrow_outline", shaft=18)
            v = {**defaults, **self.doc.get("classes", {}).get(e.get("class"), {}), **e.get("style", {})}
            head = None if v["head"] == "none" else v["head"]
            native_heads = self.client.request("GET", "/v3/capabilities")["styles"]["arrowheads"] if kind == "ppt" else None
            if native_heads is not None and head not in native_heads:
                raise DslError("edges." + name + ".style.head", "head not exposed by current Bridge")
            edgefont = {"style": {"font": v.get("font", self.base["font"]), "font_size": v.get("font_size", 16), "text": v.get("text", self.base["text"])}}
            op = {"op": "connect", "from": "@node." + source, "to": "@node." + target,
                "start": {"anchor": ss, "fixedPoint": sf, "mode": "inside"}, "end": {"anchor": ts, "fixedPoint": tf, "mode": "inside"},
                "waypoints": route[1:-1], "elbowed": False, "startArrowhead": None, "endArrowhead": head,
                "style": {"strokeColor": v["stroke"], "backgroundColor": v["fill"], "fillStyle": "solid", "strokeWidth": v.get("stroke_width", 2), "strokeStyle": v.get("dash", "solid"), "roughness": 0, "roundness": None}, "arrowHeadSize": v.get("head_scale", 1)}
            label = e.get("label", "")
            if label:
                _, ms = self.measure(label, edgefont)
                lengths = [math.dist(a, b) for a, b in zip(route, route[1:])]
                total = sum(lengths)
                candidate = max(range(len(lengths)), key=lambda i: lengths[i])
                pos = e.get("label_at", (sum(lengths[:candidate]) + lengths[candidate] / 2) / total if total else .5)
                op["label"] = {"text": label, "style": {**self.text_style(edgefont), "labelPosition": pos}}
                a, b = route[candidate], route[candidate + 1]
                obstacles.append({"x": (a[0] + b[0]) / 2 - ms["width"] / 2 - 8, "y": (a[1] + b[1]) / 2 - ms["height"] / 2 - 8, "width": ms["width"] + 16, "height": ms["height"] + 16})
            self.emit("edge." + name, op, "edge")
            self.entities["edge." + name]["customData"].update({"lineCrossings": "gap", **({"blockArrowWidth": v["shaft"]} if "shaft" in v else {})})
            self.expected.append({"type": "edge_label" if label else "edge_exists", "from": "node." + source, "to": "node." + target, **({"text": label} if label else {})})

    def emit_port_labels(self):
        from visual_diagnostics import _crosses
        occupied = []
        segments = [pair for route in self.routes.values() for pair in zip(route, route[1:])]
        for group in self.doc.get("groups", {}):
            b = self.boxes[group]
            x, y, r, d = b["x"], b["y"], b["x"] + b["width"], b["y"] + b["height"]
            segments.extend([((x, y), (r, y)), ((r, y), (r, d)), ((r, d), (x, d)), ((x, d), (x, y))])
        for name in self.doc["nodes"]:
            b = self.boxes[name]
            occupied.append((b["x"] - 3, b["y"] - 3, b["x"] + b["width"] + 3, b["y"] + b["height"] + 3))
        for spec in self.entities.values():
            if spec["op"] == "create_text":
                _, ms = self.measure(spec["text"], {"style": {"font": spec["style"]["fontFamily"], "font_size": spec["style"]["fontSize"]}})
                occupied.append((spec["x"], spec["y"], spec["x"] + ms["width"], spec["y"] + ms["height"]))
        for key, node, label, side, px, py, unit in self.port_labels:
            _, ms = self.measure(label, node, size=12)
            w, h = ms["width"], ms["height"]
            candidates = []
            for distance in (8, 30, 58, 90):
                if side in ("left", "right"):
                    x = px - w - distance if side == "left" else px + distance
                    candidates.extend((x, py + dy) for dy in (-h - 6, 6, -h - 28, 28, -h - 52, 52))
                else:
                    y = py - h - distance if side == "top" else py + distance
                    candidates.extend((px + dx, y) for dx in (8, -w - 8, 30, -w - 30, 60))
            selected = None
            for x, y in candidates:
                box = (x - 3, y - 2, x + w + 3, y + h + 2)
                overlap = any(min(box[2], b[2]) > max(box[0], b[0]) and min(box[3], b[3]) > max(box[1], b[1]) for b in occupied)
                if not overlap and not any(_crosses(a, b, box) for a, b in segments):
                    selected = (x, y, box)
                    break
            if selected is None:
                raise DslError(key, "no clear nearby port-label position; increase layout gap or shorten the port name")
            x, y, box = selected
            occupied.append(box)
            self.emit(key, {"op": "create_text", "x": x, "y": y, "text": label, "style": self.text_style(node, 12)}, "text", unit)

    def compile(self):
        tree = copy.deepcopy(self.doc.get("layout", {"flow": "right"}))
        width, height = self.layout_size(tree)
        ox, oy = tree.get("origin", [50, 100 if self.doc.get("title") else 50])
        self.place(tree, ox, oy)
        for name, group in self.doc.get("groups", {}).items():
            b = self.boxes[name]
            self.emit("group." + name, {"op": "create_shape", "type": "rectangle", **b, "style": {**self.native_style(group), "backgroundColor": self.visual(group).get("fill", "#f1f5f9")}}, "container", isContainer=True)
            if self.texts[name]:
                self.emit("group." + name + ":title", {"op": "create_text", "x": b["x"] + 20, "y": b["y"] + 14, "text": self.texts[name], "style": self.text_style(group, 22)}, "text")
        for name in self.doc["nodes"]:
            self.emit_node(name)
        if self.doc.get("title"):
            title, ms = self.measure(self.doc["title"], {}, max(width, 600), 28)
            self.emit("title", {"op": "create_text", "x": ox, "y": oy - ms["height"] - 30, "text": title, "style": self.text_style({}, 28)}, "text")
        self.emit_edges()
        self.emit_port_labels()
        features = []
        post = []
        for name, n in self.doc["nodes"].items():
            if n.get("shape") == "formula":
                b = self.boxes[name]
                post.append({"op": "resize", "target": "@node." + name, "width": self.sizes[name]["resourceWidth"], "height": self.sizes[name]["resourceHeight"]})
            configs = {**n.get("features", {})}
            if n.get("shape") == "chart":
                configs["echarts"] = {"type": "custom", "options": n["options"]}
            for feature, config in configs.items():
                target = "@node." + name
                if feature == "rich_text":
                    kind = n.get("shape", "box")
                    target += "" if kind == "text" else ":title" if kind in ("table", "mux", "alu", "polygon", "formula", "image", "embed", "chart") else ":label"
                features.append({"op": "set_feature", "feature": feature, "targets": [target], "config": config})
        for key, entity in self.entities.items():
            self.expected.append({"type": "node_exists", "id": key})
            text = entity.get("text") if entity["op"] == "create_text" else entity.get("label", {}).get("text")
            if text:
                assertion = {"type": "label_equals", "id": key, "text": text}
                if assertion not in self.expected:
                    self.expected.append(assertion)
        if self.client.read(self.token, detail="full")["revision"] != self.plan_revision:
            raise DslError("revision", "canvas changed during compilation; compile again")
        if len(self.entities) + len(features) + len(post) > 450:
            raise DslError("$", "plan exceeds the 450-operation single-transaction scene limit")
        return {"document": self.doc["id"], "baseRevision": self.plan_revision, "entities": self.entities, "post": post, "features": features, "boxes": self.boxes, "routes": self.routes, "expected": self.expected, "acceptance": self.doc.get("acceptance", "medium"), "font": self.font, "limits": ["Native geometric/visual checks still required; layout is not an aesthetic proof.", "Flows use existing layered ordering; compositions use measured nested boxes.", "Routing avoids node/header/prior-label boxes, not a global net/bus optimizer."]}
