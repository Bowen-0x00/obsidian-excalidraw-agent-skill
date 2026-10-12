"""Measured diagram planning over the existing, native Obsidian bridge."""
from __future__ import annotations

import heapq
import math
import statistics
import unicodedata
import uuid
from collections import defaultdict, deque
from typing import Any

from drawing_styles import resolve_style

FONT = "Helvetica"
PORTS = {"top": (0.5, 0.0), "right": (1.0, 0.5), "bottom": (0.5, 1.0), "left": (0.0, 0.5)}
PALETTE = {
    "default": ("#334155", "#f1f5f9"),
    "primary": ("#2563eb", "#eff6ff"),
    "success": ("#15803d", "#f0fdf4"),
    "warning": ("#b45309", "#fffbeb"),
    "decision": ("#475569", "#f8fafc"),
}


def _number(value: Any, name: str, minimum: float | None = None) -> float:
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number")
    value = float(value)
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return value


def _unique(items: list[dict], name: str) -> dict[str, dict]:
    result = {}
    for index, item in enumerate(items):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"]:
            raise ValueError(f"{name}[{index}].id must be a nonempty string")
        if item["id"] in result:
            raise ValueError(f"Duplicate {name} id: {item['id']}")
        result[item["id"]] = item
    return result


def _graphemes(text: str) -> list[str]:
    clusters: list[str] = []
    join_next = False
    for char in text:
        continuation = unicodedata.category(char).startswith("M") or char in ("\ufe0e", "\ufe0f", "\u200d")
        if clusters and (continuation or join_next):
            clusters[-1] += char
        else:
            clusters.append(char)
        join_next = char == "\u200d"
    return clusters


class Metrics:
    def __init__(self, client: Any, context_token: str, font: str):
        self.client, self.token, self.font = client, context_token, font
        self.cache: dict[tuple[str, float, float], dict] = {}

    def size(self, text: str, font_size: float, line_height: float = 1.2) -> dict:
        key = (text, font_size, line_height)
        if key not in self.cache:
            result = self.client.request("POST", "/v3/text/measure", {
                "contextToken": self.token, "text": text,
                "style": {"fontFamily": self.font, "fontSize": font_size, "lineHeight": line_height},
            })
            self.cache[key] = {"width": float(result["width"]), "height": float(result["height"])}
        return self.cache[key]

    def wrap(self, text: str, max_width: float, font_size: float, line_height: float = 1.2) -> tuple[str, dict]:
        lines: list[str] = []
        for paragraph in text.split("\n"):
            if not paragraph:
                lines.append("")
                continue
            units = _graphemes(paragraph)
            cursor = 0
            while cursor < len(units):
                low, high = 1, len(units) - cursor
                while low <= high:
                    middle = (low + high) // 2
                    part = "".join(units[cursor:cursor + middle])
                    if self.size(part, font_size, line_height)["width"] <= max_width:
                        low = middle + 1
                    else:
                        high = middle - 1
                count = max(1, high)
                candidate = "".join(units[cursor:cursor + count])
                # Respect a word break if one exists; split an overlong word rather than truncate it.
                if cursor + count < len(units):
                    whitespace = [i for i, unit in enumerate(units[cursor:cursor + count]) if unit.isspace()]
                    if whitespace and whitespace[-1] >= count // 2:
                        count = whitespace[-1] + 1
                        candidate = "".join(units[cursor:cursor + count])
                    elif count > 1 and units[cursor + count] in "，。；：！？、)]）】":
                        count -= 1
                        candidate = "".join(units[cursor:cursor + count])
                lines.append(candidate.rstrip())
                cursor += count
                while cursor < len(units) and units[cursor].isspace():
                    cursor += 1
        wrapped = "\n".join(lines)
        return wrapped, self.size(wrapped, font_size, line_height)


def _layers(nodes: dict[str, dict], edges: list[dict]) -> tuple[list[list[str]], set[str]]:
    adjacency: dict[str, list[dict]] = defaultdict(list)
    for edge in edges:
        adjacency[edge["from"]].append(edge)
    colors: dict[str, int] = {}
    feedback = {edge["id"] for edge in edges if edge.get("feedback")}

    def visit(node: str) -> None:
        colors[node] = 1
        for edge in adjacency[node]:
            if edge["id"] in feedback:
                continue
            target = edge["to"]
            if colors.get(target) == 1:
                feedback.add(edge["id"])
            elif colors.get(target, 0) == 0:
                visit(target)
        colors[node] = 2

    for node in nodes:
        if not colors.get(node):
            visit(node)
    indegree = {node: 0 for node in nodes}
    parents: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        if edge["id"] not in feedback:
            indegree[edge["to"]] += 1
            parents[edge["to"]].append(edge["from"])
    queue = deque(node for node in nodes if not indegree[node])
    ranks = {node: 0 for node in nodes}
    while queue:
        node = queue.popleft()
        for edge in adjacency[node]:
            if edge["id"] in feedback:
                continue
            target = edge["to"]
            ranks[target] = max(ranks[target], ranks[node] + 1)
            indegree[target] -= 1
            if not indegree[target]:
                queue.append(target)
    layers: list[list[str]] = [[] for _ in range(max(ranks.values(), default=0) + 1)]
    for node in nodes:
        layers[ranks[node]].append(node)
    # Stable barycentric ordering reduces crossings without changing logical direction.
    for _ in range(3):
        positions = {node: index for layer in layers for index, node in enumerate(layer)}
        for layer in layers[1:]:
            layer.sort(key=lambda node: statistics.mean(positions[p] for p in parents[node]) if parents[node] else positions[node])
    return layers, feedback


def _point(box: dict, port: str, ratio: list[float] | tuple[float, float] | None = None) -> tuple[float, float]:
    ratio = PORTS[port] if ratio is None else ratio
    if len(ratio) != 2 or any(isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= 1 for value in ratio):
        raise ValueError("Fixed endpoint ratios must be two finite values between zero and one")
    return box["x"] + box["width"] * ratio[0], box["y"] + box["height"] * ratio[1]


def _segment_clear(a: tuple[float, float], b: tuple[float, float], obstacles: list[tuple[float, float, float, float]]) -> bool:
    epsilon = 1e-6
    for left, top, right, bottom in obstacles:
        if abs(a[0] - b[0]) <= epsilon:
            if left + epsilon < a[0] < right - epsilon and max(min(a[1], b[1]), top) < min(max(a[1], b[1]), bottom) - epsilon:
                return False
        elif abs(a[1] - b[1]) <= epsilon:
            if top + epsilon < a[1] < bottom - epsilon and max(min(a[0], b[0]), left) < min(max(a[0], b[0]), right) - epsilon:
                return False
        else:
            raise ValueError("Router only accepts orthogonal segments")
    return True


def _route(start: tuple[float, float], end: tuple[float, float], start_port: str, end_port: str, boxes: list[dict], clearance: float = 16) -> list[list[float]]:
    vectors = {"top": (0, -1), "right": (1, 0), "bottom": (0, 1), "left": (-1, 0)}
    start_vector, end_vector = vectors[start_port], vectors[end_port]
    source = (start[0] + start_vector[0] * clearance, start[1] + start_vector[1] * clearance)
    target = (end[0] + end_vector[0] * clearance, end[1] + end_vector[1] * clearance)
    obstacles = [(b["x"] - clearance, b["y"] - clearance, b["x"] + b["width"] + clearance, b["y"] + b["height"] + clearance) for b in boxes]
    xs = sorted({source[0], target[0], *(x for b in obstacles for x in (b[0], b[2]))})
    ys = sorted({source[1], target[1], *(y for b in obstacles for y in (b[1], b[3]))})
    xs = [xs[0] - clearance * 2, *xs, xs[-1] + clearance * 2]
    ys = [ys[0] - clearance * 2, *ys, ys[-1] + clearance * 2]
    sx, sy, tx, ty = xs.index(source[0]), ys.index(source[1]), xs.index(target[0]), ys.index(target[1])
    initial = (sx, sy, 0)
    best = {initial: 0.0}
    previous = {}
    heap = [(abs(source[0] - target[0]) + abs(source[1] - target[1]), 0.0, initial)]
    final = None
    while heap:
        _, cost, state = heapq.heappop(heap)
        if cost != best.get(state):
            continue
        x, y, direction = state
        if (x, y) == (tx, ty):
            final = state
            break
        for nx, ny, new_direction in ((x - 1, y, 1), (x + 1, y, 1), (x, y - 1, 2), (x, y + 1, 2)):
            if not (0 <= nx < len(xs) and 0 <= ny < len(ys)):
                continue
            a, b = (xs[x], ys[y]), (xs[nx], ys[ny])
            if not _segment_clear(a, b, obstacles):
                continue
            next_state = (nx, ny, new_direction)
            next_cost = cost + abs(a[0] - b[0]) + abs(a[1] - b[1]) + (clearance if direction and direction != new_direction else 0)
            if next_cost >= best.get(next_state, math.inf):
                continue
            best[next_state], previous[next_state] = next_cost, state
            heuristic = abs(b[0] - target[0]) + abs(b[1] - target[1])
            heapq.heappush(heap, (next_cost + heuristic, next_cost, next_state))
    if final is None:
        raise ValueError("No obstacle-free route; move the conflicting fixed nodes or increase spacing")
    path = []
    state = final
    while True:
        path.append((xs[state[0]], ys[state[1]]))
        if state == initial:
            break
        state = previous[state]
    path.reverse()
    points = [start, *path, end]
    compact = []
    for point in points:
        if compact and point == compact[-1]:
            continue
        if len(compact) >= 2:
            a, b = compact[-2], compact[-1]
            if (a[0] == b[0] == point[0]) or (a[1] == b[1] == point[1]):
                compact.pop()
        compact.append(point)
    return [[round(x, 6), round(y, 6)] for x, y in compact]


def plan_diagram(client: Any, context_token: str, diagram: dict) -> dict:
    """Create native operations and a layout, using measured rather than estimated text."""
    if not isinstance(diagram, dict):
        raise ValueError("diagram must be an object")
    kind = diagram.get("kind", "flowchart")
    if kind not in ("flowchart", "architecture", "swimlane", "freeform", "uml", "microarchitecture", "circuit"):
        raise ValueError("Unsupported diagram kind; use flowchart/architecture/swimlane/freeform/uml/microarchitecture/circuit")
    nodes = _unique(diagram.get("nodes", []), "nodes")
    if not nodes:
        raise ValueError("At least one node is required")
    edges = list(_unique(diagram.get("edges", []), "edges").values())
    containers = _unique(diagram.get("containers", []), "containers")
    lanes = _unique(diagram.get("lanes", []), "lanes")
    groups = _unique(diagram.get("groups", []), "groups")
    if set(nodes) & (set(containers) | set(lanes)) or set(containers) & set(lanes):
        raise ValueError("Node, container, and lane IDs must be distinct")
    for edge in edges:
        if edge.get("from") not in nodes or edge.get("to") not in nodes:
            raise ValueError(f"Edge {edge['id']} references a missing node")
    memberships: dict[str, str] = {}
    for name, box in {**containers, **lanes}.items():
        if not box.get("members"):
            raise ValueError(f"Container/lane {name} needs members")
        for member in box["members"]:
            if member not in nodes:
                raise ValueError(f"Container/lane {name} references missing node {member}")
            if member in memberships:
                raise ValueError(f"Node {member} belongs to multiple containers/lanes")
            memberships[member] = name
    for group in groups.values():
        if any(member not in nodes for member in group.get("members", [])):
            raise ValueError(f"Group {group['id']} references a missing node")
    if kind == "swimlane" and (not lanes or set(memberships) != set(nodes)):
        raise ValueError("Every swimlane node needs exactly one lane membership")
    layout = diagram.get("layout", {})
    direction = layout.get("direction", "LR" if kind in ("architecture", "uml", "microarchitecture", "circuit") else "TB")
    if direction not in ("TB", "LR"):
        raise ValueError("Planner directions are TB or LR; arbitrary geometry uses native operations")
    if lanes and direction != "TB":
        raise ValueError("The current swimlane engine uses top headers; use vertical lanes and TB flow")
    if lanes and containers:
        raise ValueError("Use either flat containers or swimlanes in one planned region")
    context = client.request("POST", "/v3/context", {"contextToken": context_token, "includeElements": False})
    revision = context["revision"]
    summary = client.request("POST", "/v3/elements/summary", {"contextToken": context_token})
    diagram_id = str(diagram.get("diagramId") or f"diagram-{uuid.uuid4().hex[:10]}")
    if any(element.get("features", {}).get("agentDiagram", {}).get("diagramId") == diagram_id for element in summary.get("elements", [])):
        raise ValueError("Diagram already exists; use incremental native operations instead of recreating IDs")
    profile = resolve_style(diagram.get("style"))
    font = str(diagram.get("fontFamily", profile["fontFamily"]))
    font_size = _number(diagram.get("fontSize", profile["fontSize"]), "fontSize", 1)
    line_height = _number(profile["text"].get("lineHeight", 1.2), "lineHeight", 0.1)
    padding = _number(layout.get("padding", 16), "layout.padding", 0)
    gap = _number(layout.get("nodeGap", 64), "layout.nodeGap", 32)
    rank_gap = _number(layout.get("rankGap", 72), "layout.rankGap", 40)
    metrics = Metrics(client, context_token, font)
    boxes: dict[str, dict] = {}
    wrapped_labels: dict[str, str] = {}
    text_sizes: dict[str, dict] = {}
    content_kinds: dict[str, str | None] = {}
    for name, node in nodes.items():
        content = node.get("content", {})
        content_kind = content.get("kind")
        content_kinds[name] = content_kind
        label = str(node.get("label", ""))
        shape = node.get("shape", "rectangle")
        requested = node.get("size", {})
        max_width = _number(node.get("text", {}).get("maxWidth", 176 if shape == "diamond" else 240), f"nodes.{name}.text.maxWidth", 1)
        wrapped, measured = metrics.wrap(label, max_width, font_size, line_height)
        wrapped_labels[name], text_sizes[name] = wrapped, measured
        width = max(220, measured["width"] + padding * 2)
        height = max(72, measured["height"] + padding * 2)
        if shape == "diamond":
            text_width = measured["width"] + padding * 2
            text_height = measured["height"] + padding * 2
            # Respect the diamond's inner width, but avoid a very wide, visually dominant decision.
            height = max(156, text_height * 2.2)
            width = max(300, text_width / (1 - text_height / height))
        elif shape == "ellipse":
            width = max(200, (measured["width"] + padding * 2) * math.sqrt(2))
            height = max(72, (measured["height"] + padding * 2) * math.sqrt(2))
        elif shape not in ("rectangle", "polygon"):
            raise ValueError(f"Unsupported node shape {shape}; use native operations for special geometry")
        if content_kind in ("image", "latex"):
            source = content.get("source")
            if isinstance(source, dict):
                source = source.get("vaultPath") or source.get("url") or source.get("dataUrl")
            resource = client.request("POST", "/v3/content/measure", {
                "contextToken": context_token, "kind": content_kind,
                "source": source, "tex": content.get("tex"),
                "scaleX": content.get("scaleX", 1), "scaleY": content.get("scaleY", 1),
            })
            width, height = float(resource["width"]), float(resource["height"])
            if requested.get("width") or requested.get("height"):
                fit = min(float(requested.get("width", width)) / width, float(requested.get("height", height)) / height)
                width, height = width * fit, height * fit
        elif content_kind in ("echarts", "embeddable"):
            width = _number(requested.get("width", 500), f"nodes.{name}.size.width", 1)
            height = _number(requested.get("height", 350), f"nodes.{name}.size.height", 1)
        elif content_kind:
            raise ValueError(f"Unsupported content kind: {content_kind}")
        else:
            width = max(width, _number(requested.get("minWidth", requested.get("width", 1)), f"nodes.{name}.size.width", 1))
            height = max(height, _number(requested.get("minHeight", requested.get("height", 1)), f"nodes.{name}.size.height", 1))
        boxes[name] = {"x": 0.0, "y": 0.0, "width": math.ceil(width), "height": math.ceil(height)}
    layers, feedback = _layers(nodes, edges)
    origin = layout.get("origin") or {"x": 0, "y": max((e.get("y", 0) + e.get("height", 0) for e in summary.get("elements", [])), default=-80) + 80}
    ox, oy = _number(origin.get("x", 0), "origin.x"), _number(origin.get("y", 0), "origin.y")
    if lanes:
        lane_order = list(lanes)
        lane_widths = {lane: max(boxes[n]["width"] for n in lanes[lane]["members"]) + 64 for lane in lanes}
        lane_x = {}
        cursor = ox
        for lane in lane_order:
            lane_x[lane] = cursor
            cursor += lane_widths[lane] + 32
        y = oy + 72
        for layer in layers:
            same_lane: dict[str, list[str]] = defaultdict(list)
            for name in layer:
                same_lane[memberships[name]].append(name)
            row_height = 0
            for lane, members in same_lane.items():
                local_y = y
                for name in members:
                    box = boxes[name]
                    box.update(x=lane_x[lane] + (lane_widths[lane] - box["width"]) / 2, y=local_y)
                    local_y += box["height"] + gap
                row_height = max(row_height, local_y - y - gap)
            y += row_height + rank_gap
    else:
        horizontal = direction == "LR"
        row_spans = [sum(boxes[n]["height" if horizontal else "width"] for n in layer) + gap * (len(layer) - 1) for layer in layers]
        total_span = max(row_spans)
        cursor = ox if horizontal else oy
        for layer, span in zip(layers, row_spans):
            cross = (oy if horizontal else ox) + (total_span - span) / 2
            depth = max(boxes[n]["width" if horizontal else "height"] for n in layer)
            for name in layer:
                box = boxes[name]
                box.update(x=cursor + (depth - box["width"]) / 2 if horizontal else cross,
                           y=cross if horizontal else cursor + (depth - box["height"]) / 2)
                cross += box["height" if horizontal else "width"] + gap
            cursor += depth + rank_gap
    for name, node in nodes.items():
        if node.get("position") is not None:
            boxes[name]["x"] = _number(node["position"]["x"], f"nodes.{name}.position.x")
            boxes[name]["y"] = _number(node["position"]["y"], f"nodes.{name}.position.y")
    operations: list[dict] = []
    refs = {name: f"node:{name}" for name in nodes}
    box_ids = {name: uuid.uuid4().hex[:12] for name in (*containers, *lanes)}
    region_boxes = {}

    def metadata(logical_id: str, role: str, label: str | None = None) -> dict:
        data = {"diagramId": diagram_id, "logicalId": logical_id, "role": role}
        if label is not None:
            data["originalLabel"] = label
        return {"agentDiagram": data}

    def label_style(size: float = font_size) -> dict:
        return {**profile["text"], "fontFamily": font, "fontSize": size, "lineHeight": line_height}

    for name, region in {**containers, **lanes}.items():
        members = [boxes[n] for n in region["members"]]
        left, top = min(b["x"] for b in members), min(b["y"] for b in members)
        right, bottom = max(b["x"] + b["width"] for b in members), max(b["y"] + b["height"] for b in members)
        region_label, region_text = metrics.wrap(str(region.get("label", name)), max(right - left, 160), 22)
        header_height = max(48, region_text["height"] + 16)
        if name in lanes:
            left, top = lane_x[name], oy
            right = left + lane_widths[name]
            bottom = max(b["y"] + b["height"] for b in boxes.values()) + 32
            width = right - left
        else:
            left -= 24
            top -= header_height + 24
            right += 24
            bottom += 24
            width = right - left
        region_box = {"x": left, "y": top, "width": width, "height": bottom - top}
        region_boxes[name] = region_box
        operation = {"op": "create_shape", "type": "rectangle", "ref": f"region:{name}", "id": box_ids[name], **region_box,
                     "style": {**profile["container"], "strokeColor": region.get("color", profile["container"]["strokeColor"])},
                     "customData": metadata(name, "lane" if name in lanes else "container")}
        if name in lanes:
            operation["label"] = {"text": region_label, "style": label_style(22), "customData": metadata(name, "header", str(region.get("label", name)))}
        operations.append(operation)
        if name in lanes:
            operations.append({"op": "set_feature", "feature": "swimlane", "targets": [f"@region:{name}"], "config": {"color": region.get("color", "auto"), "headerHeight": header_height}})
        else:
            operations.append({"op": "create_text", "ref": f"region:{name}:header", "x": left + 24, "y": top + 12, "text": region_label,
                               "style": label_style(22), "customData": metadata(name, "header", str(region.get("label", name)))})
    for name, node in nodes.items():
        box, content = boxes[name], node.get("content", {})
        content_kind = content_kinds[name]
        label = str(node.get("label", ""))
        stroke, background = PALETTE.get(node.get("variant", "decision" if node.get("shape") == "diamond" else "default"), PALETTE["default"])
        style = {"strokeColor": stroke, "backgroundColor": background, **profile["shape"],
                 **({"strokeColor": stroke, "backgroundColor": background} if node.get("variant") else {}),
                 **node.get("style", {})}
        data = metadata(name, "body", label)
        operation = {"ref": refs[name], **box}
        if content_kind == "image":
            source = content["source"]
            if isinstance(source, dict):
                source = source.get("vaultPath") or source.get("url") or source.get("dataUrl")
            operation.update(op="create_image", source=source, customData=data)
        elif content_kind == "latex":
            operation.update(op="create_latex", tex=content["tex"], scaleX=content.get("scaleX", 1), scaleY=content.get("scaleY", 1))
        elif content_kind == "embeddable":
            source = content["source"]
            if isinstance(source, dict):
                source = source.get("vaultPath") or source.get("url")
            operation.update(op="create_embeddable", source=source)
        elif node.get("shape") == "polygon":
            points = node.get("points")
            if not isinstance(points, list) or len(points) < 3:
                raise ValueError(f"Polygon {name} needs at least three explicit local points")
            operation.update(op="create_linear", kind="line", points=points, polygon=True, closed=True, style=style, customData=data)
            operation.pop("width")
            operation.pop("height")
        else:
            operation.update(op="create_shape", type=node.get("shape", "rectangle"), style=style, customData=data)
            if not content_kind and label:
                operation["label"] = {"text": wrapped_labels[name], "style": label_style(), "padding": padding, "customData": metadata(name, "label", label)}
        operations.append(operation)
        if content_kind in ("latex", "embeddable"):
            operations.append({"op": "patch_custom_data", "target": f"@{refs[name]}", "merge": data})
        if content_kind == "latex":
            operations.append({"op": "resize", "target": f"@{refs[name]}", "width": box["width"], "height": box["height"]})
        if content_kind == "echarts":
            operations.append({"op": "set_feature", "feature": "echarts", "targets": [f"@{refs[name]}"], "config": {"type": content.get("type", "custom"), "options": content["options"]}})
        if name in memberships and memberships[name] in lanes:
            parent = box_ids[memberships[name]]
            operations.append({"op": "patch_custom_data", "target": f"@{refs[name]}", "merge": {"parent": parent}})
            if not content_kind and label and node.get("shape") != "polygon":
                operations.append({"op": "patch_custom_data", "target": f"@{refs[name]}:label", "merge": {"parent": parent}})
        if (content_kind or node.get("shape") == "polygon") and label:
            operations.append({"op": "create_text", "ref": f"{refs[name]}:caption", "x": box["x"] + (box["width"] - text_sizes[name]["width"]) / 2,
                               "y": box["y"] + box["height"] + 12, "text": wrapped_labels[name], "style": label_style(), "customData": metadata(name, "caption", label)})
            operations.append({"op": "group", "targets": [f"@{refs[name]}", f"@{refs[name]}:caption"]})
        for feature in node.get("features", []):
            operations.append({"op": "set_feature", "feature": feature["name"], "targets": [f"@{refs[name]}"], "config": feature["config"]})
    for group in groups.values():
        targets = []
        for member in group.get("members", []):
            targets.append(f"@{refs[member]}")
            if str(nodes[member].get("label", "")):
                suffix = ":caption" if content_kinds[member] or nodes[member].get("shape") == "polygon" else ":label"
                targets.append(f"@{refs[member]}{suffix}")
        operations.append({"op": "group", "targets": targets})
    routes = {}
    for edge in edges:
        source, target = boxes[edge["from"]], boxes[edge["to"]]
        start_port = edge.get("fromPort", "right" if direction == "LR" else "bottom")
        end_port = edge.get("toPort", "left" if direction == "LR" else "top")
        if edge["id"] in feedback:
            start_port, end_port = edge.get("fromPort", "left"), edge.get("toPort", "left")
        if start_port not in PORTS or end_port not in PORTS:
            raise ValueError(f"Edge {edge['id']} ports must be top/right/bottom/left")
        route = _route(_point(source, start_port, edge.get("fromFixedPoint")), _point(target, end_port, edge.get("toFixedPoint")), start_port, end_port, list(boxes.values()))
        routes[edge["id"]] = route
        operation = {"op": "connect", "ref": f"edge:{edge['id']}", "from": f"@{refs[edge['from']]}", "to": f"@{refs[edge['to']]}",
                     "start": {"anchor": start_port, "mode": "orbit", **({"fixedPoint": edge["fromFixedPoint"]} if "fromFixedPoint" in edge else {})},
                     "end": {"anchor": end_port, "mode": "orbit", **({"fixedPoint": edge["toFixedPoint"]} if "toFixedPoint" in edge else {})}, "waypoints": route[1:-1],
                     "elbowed": True, "endArrowhead": edge.get("endArrowhead", "arrow"), "startArrowhead": edge.get("startArrowhead"),
                     "style": {**profile["edge"], **edge.get("style", {})}}
        if edge.get("label"):
            operation["label"] = {"text": str(edge["label"]), "style": {**label_style(16), "labelPosition": edge.get("labelPosition", 0.28)}, "customData": metadata(edge["id"], "edge-label", str(edge["label"]))}
        operations.append(operation)
        operations.append({"op": "patch_custom_data", "target": f"@edge:{edge['id']}", "merge": metadata(edge["id"], "edge")})
    if diagram.get("title"):
        title, size = metrics.wrap(str(diagram["title"]), max(600, max(b["x"] + b["width"] for b in boxes.values()) - min(b["x"] for b in boxes.values())), 28)
        top = min(b["y"] for b in (*boxes.values(), *region_boxes.values()))
        operations.append({"op": "create_text", "ref": "diagram:title", "x": min(b["x"] for b in (*boxes.values(), *region_boxes.values())),
                           "y": top - size["height"] - 36, "text": title, "style": label_style(28), "customData": metadata(diagram_id, "title", str(diagram["title"]))})
    final_context = client.request("POST", "/v3/context", {"contextToken": context_token, "includeElements": False})
    if final_context["revision"] != revision:
        raise ValueError("Canvas changed during measurement; read the new revision and plan again")
    if len(operations) > 500:
        raise ValueError(f"Plan has {len(operations)} operations; bridge limit is 500. Split into explicit dependent batches.")
    return {"ok": True, "contextToken": context_token, "file": context.get("file"), "baseRevision": revision,
            "diagramId": diagram_id, "operations": operations,
            "layout": {"direction": direction, "nodes": boxes, "regions": region_boxes, "routes": routes,
                       "wrappedLabels": wrapped_labels, "measuredLabels": text_sizes, "feedbackEdges": sorted(feedback), "fontFamily": font, "fontSize": font_size, "styleProfile": profile["name"]},
            "refs": refs, "operationCount": len(operations), "notes": ["Measured plan only; call drawing_apply then drawing_check and drawing_preview."]}
