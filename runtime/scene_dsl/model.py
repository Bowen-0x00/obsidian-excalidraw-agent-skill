"""Small, strict YAML scene contract. No eval, includes, expressions or raw ops."""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

import yaml


class DslError(ValueError):
    def __init__(self, path, message):
        self.path = path
        super().__init__(f"{path}: {message}")


class Loader(yaml.SafeLoader):
    def compose_node(self, parent, index):
        if self.check_event(yaml.events.AliasEvent):
            raise DslError("YAML", "aliases are not supported; use explicit scene members")
        depth = getattr(self, "_scene_depth", 0)
        if depth >= 64:
            raise DslError("YAML", "document nesting exceeds 64 levels")
        self._scene_depth = depth + 1
        try:
            return super().compose_node(parent, index)
        finally:
            self._scene_depth = depth

# Preserve common table strings while supporting explicit YAML booleans.
Loader.yaml_implicit_resolvers = {k: [(tag, rx) for tag, rx in rules if tag not in ("tag:yaml.org,2002:bool", "tag:yaml.org,2002:timestamp")]
                                  for k, rules in yaml.SafeLoader.yaml_implicit_resolvers.items()}
Loader.add_implicit_resolver("tag:yaml.org,2002:bool", re.compile(r"^(?:true|false|True|False|TRUE|FALSE)$"), list("tTfF"))


def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise DslError(f"line {key_node.start_mark.line + 1}", "mapping keys must be strings")
        if key in result:
            raise DslError(f"line {key_node.start_mark.line + 1}", f"duplicate key {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_-]*\Z")
SIDES = {"left", "right", "top", "bottom"}
SHAPES = {"box", "diamond", "ellipse", "text", "mux", "alu", "polygon", "table", "image", "formula", "embed", "chart"}
STYLE = {"stroke", "fill", "text", "font", "font_size", "stroke_width", "dash", "roughness", "head", "shaft", "head_scale"}
FEATURES = {"shadow", "gradient", "rich_text"}


def keys(obj, allowed, path):
    if not isinstance(obj, dict):
        raise DslError(path, "expected mapping")
    unknown = set(obj) - set(allowed)
    if unknown:
        raise DslError(path, f"unknown fields {sorted(unknown)}")


def number(value, path, minimum=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or (minimum is not None and value < minimum):
        raise DslError(path, f"expected finite number" + (f" >= {minimum}" if minimum is not None else ""))
    return value


def pair(value, path, minimum=None):
    if not isinstance(value, list) or len(value) != 2:
        raise DslError(path, "expected [x, y] pair")
    return [number(v, path, minimum) for v in value]


def style(value, path):
    keys(value, STYLE, path)
    for k in ("font_size", "stroke_width", "shaft", "head_scale"):
        if k in value:
            number(value[k], path + "." + k, .01)
    if "head_scale" in value and not .125 <= value["head_scale"] <= 8:
        raise DslError(path + ".head_scale", "backend supports 0.125..8")
    if "dash" in value and value["dash"] not in ("solid", "dashed", "dotted"):
        raise DslError(path + ".dash", "solid, dashed or dotted")
    for k in ("stroke", "fill", "text", "font", "head"):
        if k in value and not isinstance(value[k], str):
            raise DslError(path + "." + k, "expected string")
    if "roughness" in value:
        number(value["roughness"], path + ".roughness", 0)


def endpoint(value, nodes, path):
    if not isinstance(value, str):
        raise DslError(path, "expected node or node.port")
    bits = value.split(".")
    if len(bits) > 2 or bits[0] not in nodes:
        raise DslError(path, f"unknown endpoint {value!r}")
    node = nodes[bits[0]]
    if len(bits) == 2 and bits[1] not in SIDES | set(node.get("ports", {})):
        raise DslError(path, f"unknown port {value!r}")
    return bits[0]


def port(value, path):
    if isinstance(value, str):
        side, sep, pos = value.partition(":")
        try:
            ratio = float(pos) if sep else .5
        except ValueError:
            raise DslError(path, "port must be side or side:fraction") from None
    else:
        raise DslError(path, "port must be left/right/top/bottom[:fraction]")
    if side not in SIDES or not math.isfinite(ratio) or not 0 <= ratio <= 1:
        raise DslError(path, "port side/fraction invalid")
    return side, ratio


def load(path):
    raw = Path(path).read_text(encoding="utf-8")
    if len(raw.encode()) > 512_000:
        raise DslError("$", "document exceeds 512 KB")
    try:
        doc = yaml.load(raw, Loader=Loader)
    except yaml.YAMLError as e:
        raise DslError("YAML", str(e)) from None
    validate(doc)
    return doc


def validate(doc):
    try:
        size = len(json.dumps(doc, ensure_ascii=False, allow_nan=False).encode("utf-8"))
    except (TypeError, ValueError, RecursionError) as error:
        raise DslError("$", "expected finite, acyclic JSON-compatible scene data") from error
    if size > 512_000:
        raise DslError("$", "document exceeds 512 KB")
    keys(doc, {"version", "id", "title", "style", "classes", "nodes", "groups", "edges", "layout", "acceptance"}, "$")
    if type(doc.get("version")) is not int or doc["version"] != 1 or not isinstance(doc.get("id"), str) or not IDENT.fullmatch(doc["id"]):
        raise DslError("$", "version: 1 and a stable ASCII id are required")
    if "title" in doc and not isinstance(doc["title"], str):
        raise DslError("title", "expected string")
    if not isinstance(doc.get("nodes"), dict) or not doc["nodes"]:
        raise DslError("nodes", "nonempty mapping required")
    if doc.get("acceptance", "medium") not in ("low", "medium", "high"):
        raise DslError("acceptance", "low, medium or high")
    if "style" in doc:
        style(doc["style"], "style")
    classes = doc.get("classes", {})
    keys(classes, classes.keys() if isinstance(classes, dict) else (), "classes")
    for name, value in classes.items():
        style(value, "classes." + name)
    nodes = doc["nodes"]
    for name, value in list(nodes.items()):
        if isinstance(value, str):
            value = nodes[name] = {"label": value}
        p = "nodes." + name
        if not IDENT.fullmatch(name):
            raise DslError(p, "id must be ASCII identifier; labels may be any language")
        keys(value, {"label", "shape", "size", "wrap", "at", "class", "style", "ports", "columns", "rows", "points", "source", "tex", "options", "features"}, p)
        kind = value.get("shape", "box")
        if kind not in SHAPES:
            raise DslError(p + ".shape", f"supported shapes: {sorted(SHAPES)}")
        if not isinstance(value.get("label", ""), str):
            raise DslError(p + ".label", "expected string")
        for k in ("size", "at"):
            if k in value:
                pair(value[k], p + "." + k, 1 if k == "size" else None)
        if "wrap" in value:
            number(value["wrap"], p + ".wrap", 20)
        if "style" in value:
            style(value["style"], p + ".style")
        if "class" in value and value["class"] not in classes:
            raise DslError(p + ".class", "class does not exist")
        ports = value.get("ports", {})
        keys(ports, ports.keys() if isinstance(ports, dict) else (), p + ".ports")
        for key, spec in value.get("ports", {}).items():
            if not IDENT.fullmatch(key) or key in SIDES:
                raise DslError(p + ".ports", "port name must be identifier, not reserved side")
            port(spec, p + ".ports." + key)
        if kind == "table":
            columns, rows = value.get("columns"), value.get("rows")
            if not isinstance(columns, list) or not columns or not isinstance(rows, list) or not rows:
                raise DslError(p, "table requires columns and nonempty rows")
            if len(columns) > 12 or len(rows) > 20 or any(not isinstance(r, list) or len(r) != len(columns) for r in rows):
                raise DslError(p + ".rows", "consistent columns required (max 12 columns, 20 rows)")
            if any(isinstance(c, (dict, list)) for r in [columns, *rows] for c in r):
                raise DslError(p, "table cells must be scalar")
        if kind == "polygon":
            if not isinstance(value.get("points"), list) or len(value["points"]) < 3:
                raise DslError(p + ".points", "normalized polygon points required")
            for v in value["points"]:
                point = pair(v, p + ".points", 0)
                if max(point) > 1:
                    raise DslError(p + ".points", "polygon coordinates must be normalized 0..1")
        for kind_name, field in (("image", "source"), ("embed", "source"), ("formula", "tex")):
            if kind == kind_name and not isinstance(value.get(field), str):
                raise DslError(p + "." + field, "resource source required")
        if kind == "chart" and not isinstance(value.get("options"), dict):
            raise DslError(p + ".options", "ECharts JSON options required, not code")
        features = value.get("features", {})
        keys(features, FEATURES, p + ".features")
        for k, cfg in features.items():
            if not isinstance(cfg, dict):
                raise DslError(p + ".features." + k, "structured feature config required")
    groups = doc.get("groups", {})
    if not isinstance(groups, dict) or set(groups) & set(nodes):
        raise DslError("groups", "must be map with IDs distinct from nodes")
    for name, group in groups.items():
        if not IDENT.fullmatch(name):
            raise DslError("groups." + name, "invalid id")
        keys(group, {"label", "layout", "padding", "class", "style"}, "groups." + name)
        if "layout" not in group:
            raise DslError("groups." + name, "layout required")
        if "padding" in group:
            number(group["padding"], "groups." + name + ".padding", 16)
        if "style" in group:
            style(group["style"], "groups." + name + ".style")
        if "class" in group and group["class"] not in classes:
            raise DslError("groups." + name + ".class", "unknown class")
    edges = doc.get("edges", {})
    if not isinstance(edges, dict):
        raise DslError("edges", "mapping required for stable connection identity")
    for name, edge in edges.items():
        p = "edges." + name
        if not IDENT.fullmatch(name):
            raise DslError(p, "invalid edge id")
        keys(edge, {"from", "to", "label", "kind", "class", "style", "via", "label_at"}, p)
        endpoint(edge.get("from"), nodes, p + ".from")
        endpoint(edge.get("to"), nodes, p + ".to")
        if edge.get("kind", "data") not in ("data", "control", "feedback", "line", "ppt"):
            raise DslError(p + ".kind", "data/control/feedback/line/ppt")
        if "style" in edge:
            style(edge["style"], p + ".style")
        if "class" in edge and edge["class"] not in classes:
            raise DslError(p + ".class", "unknown class")
        if "label_at" in edge:
            number(edge["label_at"], p + ".label_at", 0)
            if edge["label_at"] > 1:
                raise DslError(p + ".label_at", "0..1 required")
        for point in edge.get("via", []):
            pair(point, p + ".via")
    seen, visiting = set(), set()
    def layout(tree, path):
        if isinstance(tree, str):
            if tree not in nodes and tree not in groups:
                raise DslError(path, f"unknown layout member {tree}")
            if tree in visiting:
                raise DslError(path, "group containment cycle")
            if tree in seen:
                raise DslError(path, f"member {tree} appears twice")
            seen.add(tree)
            if tree in groups:
                visiting.add(tree)
                layout(groups[tree]["layout"], "groups." + tree + ".layout")
                visiting.remove(tree)
            return
        keys(tree, {"row", "column", "grid", "flow", "gap", "origin"}, path)
        operators = set(tree) & {"row", "column", "grid", "flow"}
        if len(operators) != 1:
            raise DslError(path, "choose one of row/column/grid/flow")
        if "gap" in tree:
            pair(tree["gap"], path + ".gap", 24) if isinstance(tree["gap"], list) else number(tree["gap"], path + ".gap", 24)
        if "origin" in tree:
            if path != "layout":
                raise DslError(path + ".origin", "origin is root-only; use node.at for absolute positions")
            pair(tree["origin"], path + ".origin")
        op = next(iter(operators))
        if op == "flow":
            if path != "layout" or groups or tree[op] not in ("right", "down"):
                raise DslError(path, "flow is root-only right/down with no groups; use compositions for fixed regions")
            seen.update(nodes)
        else:
            children = tree[op]
            if not isinstance(children, list) or not children:
                raise DslError(path, "nonempty member list required")
            if op == "grid":
                if any(not isinstance(row, list) or not row for row in children):
                    raise DslError(path, "grid requires rows of members (null means empty cell)")
                children = [c for row in children for c in row if c is not None]
            for index, child in enumerate(children):
                layout(child, f"{path}.{op}[{index}]")
    layout(doc.get("layout", {"flow": "right"}), "layout")
    missing = (set(nodes) | set(groups)) - seen
    if missing:
        raise DslError("layout", f"members not placed: {sorted(missing)}")
    if len(nodes) + len(edges) > 100:
        raise DslError("$", "scene limit: 100 logical nodes/edges")
    # SafeLoader rejects custom tags; no executable strings are forwarded.
    def safe(value, path):
        if isinstance(value, dict):
            for k, v in value.items():
                if k.lower() in {"code", "script", "onclick", "eval", "function"}:
                    raise DslError(path + "." + k, "executable extension not permitted")
                safe(v, path + "." + k)
        elif isinstance(value, list):
            for i, v in enumerate(value):
                safe(v, f"{path}[{i}]")
    for n, node in nodes.items():
        safe(node.get("features", {}), "nodes." + n + ".features")
        safe(node.get("options", {}), "nodes." + n + ".options")
    return doc


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
