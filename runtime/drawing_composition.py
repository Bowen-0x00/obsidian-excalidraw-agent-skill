"""Native library composition and multi-frame presentation orchestration.

Each native import commits separately. Failures retain an explicit receipt of prior commits;
this is intentionally not a fictitious atomic multi-library transaction.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from diagram_layout import Metrics, PORTS, _point, _route, plan_diagram
from drawing_styles import resolve_style


class CompositionError(RuntimeError):
    def __init__(self, message: str, stage: str, applied: list[dict], cause: Exception):
        super().__init__(message)
        self.stage, self.applied, self.cause = stage, applied, cause


def _current(client: Any, token: str) -> dict:
    return client.request("POST", "/v3/context", {"contextToken": token, "includeElements": False})


def compose_diagram(client: Any, token: str, base_revision: str, diagram: dict) -> dict:
    graph = deepcopy(diagram)
    library_nodes = [node for node in graph.get("nodes", []) if node.get("library")]
    if not library_nodes:
        plan = plan_diagram(client, token, graph)
        if plan["baseRevision"] != base_revision:
            raise ValueError("Canvas changed before composition")
        return client.apply(token, base_revision, plan["operations"])
    initial = _current(client, token)
    if initial["revision"] != base_revision:
        raise ValueError("Canvas changed before native library composition")
    source_items = {}
    for node in library_nodes:
        library = node["library"]
        if not isinstance(library, dict) or not library.get("source") or not library.get("item"):
            raise ValueError(f"Node {node['id']} library requires source and exact item ID or unique name")
        item = client.library("get", token, library=library["source"], item=library["item"], detail="full")["item"]
        scale = float(library.get("scale", 1))
        if not 0 < scale <= 20:
            raise ValueError("Library scale must be positive and at most 20")
        source_items[node["id"]] = {"item": item, "scale": scale, "library": library}
        node.pop("library")
        node["size"] = {"minWidth": item["bounds"]["width"] * scale, "minHeight": item["bounds"]["height"] * scale}
    plan = plan_diagram(client, token, graph)
    if plan["baseRevision"] != base_revision:
        raise ValueError("Canvas changed while reading library content")
    diagram_id = plan["diagramId"]
    library_ids = set(source_items)
    profile = resolve_style(diagram.get("style"))
    metrics = Metrics(client, token, profile["fontFamily"])
    applied: list[dict] = []
    inserted, refs = {}, {}
    revision = base_revision
    stage = "library_import"
    try:
        for node in library_nodes:
            name = node["id"]
            source = source_items[name]
            box = plan["layout"]["nodes"][name]
            natural = source["item"]["bounds"]
            x = box["x"] + (box["width"] - natural["width"] * source["scale"]) / 2
            y = box["y"] + (box["height"] - natural["height"] * source["scale"]) / 2
            result = client.library("insert", token, library=source["library"]["source"], item=source["item"]["id"],
                                    position={"x": x, "y": y, "anchor": "top-left"}, scale=source["scale"],
                                    base_revision=revision, create_anchor_proxy=True,
                                    trusted_local_library=bool(source["library"].get("trustedLocalLibrary", False)),
                                    logical_id=name, diagram_id=diagram_id)
            if not result.get("anchorElementId"):
                raise ValueError(f"Library {name} did not produce its requested bindable anchor")
            inserted[name] = result
            refs["node:" + name] = result["anchorElementId"]
            revision = result["revision"]
            applied.append({"stage": stage, "logicalId": name, "revision": revision,
                            "elementIds": result["insertedElementIds"], "sourceIdMap": result["sourceIdMap"]})
        stage = "native_shapes"
        ops = []
        for operation in plan["operations"]:
            ref = operation.get("ref", "")
            if operation["op"] in ("connect", "group") or ref.startswith("edge:"):
                continue
            if operation["op"] == "patch_custom_data" and str(operation.get("target", "")).startswith("@edge:"):
                continue
            if any(ref == f"node:{name}" or ref.startswith(f"node:{name}:") or operation.get("target") == f"@node:{name}" for name in library_ids):
                continue
            ops.append(operation)
        if ops:
            result = client.apply(token, revision, ops)
            revision = result["revision"]
            refs.update(result["refs"])
            applied.append({"stage": stage, "revision": revision, "transactionId": result.get("transactionId"), "elementIds": result["created"]})
        stage = "native_connections"
        exact = client.read(token, detail="full")
        if exact["revision"] != revision:
            raise ValueError("Canvas changed after import; do not overwrite concurrent edits")
        by_id = {element["id"]: element for element in exact["elements"]}
        boxes = {node["id"]: by_id[refs["node:" + node["id"]]] for node in diagram["nodes"]}
        final_ops, captions = [], {}
        for node in library_nodes:
            if not node.get("label"):
                continue
            name, box = node["id"], boxes[node["id"]]
            text, size = metrics.wrap(str(node["label"]), max(box["width"], 180), profile["fontSize"])
            ref = "caption:" + name
            captions[name] = "@" + ref
            final_ops.append({"op": "create_text", "ref": ref, "x": box["x"] + (box["width"] - size["width"]) / 2,
                              "y": box["y"] + box["height"] + 12, "text": text,
                              "style": {**profile["text"], "fontFamily": profile["fontFamily"], "fontSize": profile["fontSize"]},
                              "customData": {"agentDiagram": {"diagramId": diagram_id, "logicalId": name, "role": "caption", "originalLabel": node["label"]}}})
            final_ops.append({"op": "group", "targets": [*inserted[name]["insertedElementIds"], "@" + ref]})
        horizontal = plan["layout"]["direction"] == "LR"
        for edge in diagram.get("edges", []):
            start_port = edge.get("fromPort", "right" if horizontal else "bottom")
            end_port = edge.get("toPort", "left" if horizontal else "top")
            if start_port not in PORTS or end_port not in PORTS:
                raise ValueError("Use an explicit supported port for native library relationships")
            route = _route(_point(boxes[edge["from"]], start_port, edge.get("fromFixedPoint")), _point(boxes[edge["to"]], end_port, edge.get("toFixedPoint")),
                           start_port, end_port, list(boxes.values()))
            operation = {"op": "connect", "ref": "edge:" + edge["id"],
                         "from": refs["node:" + edge["from"]], "to": refs["node:" + edge["to"]],
                         "start": {"anchor": start_port, "mode": "orbit", **({"fixedPoint": edge["fromFixedPoint"]} if "fromFixedPoint" in edge else {})},
                         "end": {"anchor": end_port, "mode": "orbit", **({"fixedPoint": edge["toFixedPoint"]} if "toFixedPoint" in edge else {})},
                         "waypoints": route[1:-1], "elbowed": True, "endArrowhead": edge.get("endArrowhead", "arrow"),
                         "startArrowhead": edge.get("startArrowhead"), "style": {**profile["edge"], **edge.get("style", {})},
                         "customData": {"agentDiagram": {"diagramId": diagram_id, "logicalId": edge["id"], "role": "edge"}}}
            if edge.get("label"):
                operation["label"] = {"text": edge["label"], "style": {**profile["text"], "fontFamily": profile["fontFamily"],
                                      "fontSize": 16, "labelPosition": edge.get("labelPosition", 0.5)}}
            final_ops.append(operation)
        for group in diagram.get("groups", []):
            targets = []
            for member in group["members"]:
                if member in inserted:
                    targets.extend(inserted[member]["insertedElementIds"])
                    if member in captions:
                        targets.append(captions[member])
                else:
                    targets.append(refs["node:" + member])
                    if "node:" + member + ":label" in refs:
                        targets.append(refs["node:" + member + ":label"])
            final_ops.append({"op": "group", "targets": targets})
        if final_ops:
            result = client.apply(token, revision, final_ops)
            revision = result["revision"]
            refs.update(result["refs"])
            applied.append({"stage": stage, "revision": revision, "transactionId": result.get("transactionId"), "elementIds": result["created"]})
        return {"ok": True, "contextToken": token, "file": initial["file"], "revision": revision,
                "diagramId": diagram_id, "refs": refs, "insertions": inserted, "appliedStages": applied,
                "commitSemantics": "Each native library insertion and each operation batch commits separately; no cross-stage atomicity.",
                "next": "Read final state, check exact geometry, export and inspect PNG before completion."}
    except Exception as error:
        raise CompositionError(str(error), stage, applied, error) from error


def create_presentation(client: Any, token: str, base_revision: str, presentation: dict) -> dict:
    if _current(client, token)["revision"] != base_revision:
        raise ValueError("Canvas changed before presentation creation")
    library = presentation.get("library")
    pages = presentation.get("pages", [])
    if not library or not pages:
        raise ValueError("Presentation requires a real library and at least one page")
    profile = resolve_style(presentation.get("style", "presentation"))
    metrics = Metrics(client, token, profile["fontFamily"])
    source_pages = []
    for page in pages:
        item = client.library("get", token, library=library, item=page["template"], detail="full")["item"]
        frames = [element for element in item["elements"] if element["type"] == "frame"]
        if len(frames) != 1:
            raise ValueError(f"Page template {page['template']} must contain exactly one frame; choose an exact item")
        source_pages.append((page, item, frames[0]))
    revision, x, applied, output = base_revision, float(presentation.get("x", 0)), [], []
    stage = "page_import"
    try:
        for index, (page, item, source_frame) in enumerate(source_pages):
            imported = client.library("insert", token, library=library, item=item["id"], base_revision=revision,
                                      position={"x": x, "y": float(presentation.get("y", 0)), "anchor": "top-left"},
                                      create_anchor_proxy=False, scale=float(presentation.get("scale", 1)),
                                      trusted_local_library=bool(presentation.get("trustedLocalLibrary", False)),
                                      logical_id=f"page-{index + 1}", diagram_id=str(presentation.get("diagramId", "presentation")))
            revision = imported["revision"]
            applied.append({"stage": stage, "page": index + 1, "revision": revision, "elementIds": imported["insertedElementIds"]})
            frame_id = imported["sourceIdMap"][source_frame["id"]]
            scene = client.read(token, ids=imported["insertedElementIds"], detail="full")
            by_id = {element["id"]: element for element in scene["elements"]}
            frame = by_id[frame_id]
            texts = [element for element in scene["elements"] if element["type"] == "text"]
            placeholders = [element for element in texts if "title" in str(element.get("text", "")).lower() or "presentation" in str(element.get("text", "")).lower()]
            if not placeholders:
                raise ValueError(f"Template {item['name']} has no title placeholder; pass an explicit text ID mapping instead of guessing")
            title_target = sorted(placeholders, key=lambda element: (-float(element.get("fontSize", 0)), element["y"]))[0]
            title = str(page.get("title", ""))
            title_size = min(float(title_target.get("fontSize", 28)), 32)
            title_text, title_metrics = metrics.wrap(title, frame["width"] - 80, title_size)
            operations = [{"op": "set_text", "target": title_target["id"], "text": title_text,
                           "style": {**profile["text"], "fontFamily": profile["fontFamily"], "fontSize": title_size}},
                          {"op": "patch_element", "target": title_target["id"], "patch": {
                              "x": frame["x"] + (frame["width"] - title_metrics["width"]) / 2,
                              "y": frame["y"] + 32, "width": title_metrics["width"], "height": title_metrics["height"]}}]
            content = page.get("body", [])
            body_lines = [str(line) for line in content] if content else ([str(page["subtitle"])] if page.get("subtitle") else [])
            bullets = sorted([element for element in scene["elements"]
                              if element["type"] == "ellipse" and element["width"] < 24 and element["height"] < 24], key=lambda element: element["y"])
            body_y = frame["y"] + max(110, title_metrics["height"] + 70)
            body_x = frame["x"] + (76 if bullets and content else 50)
            for line_index, line in enumerate(body_lines):
                text, text_metrics = metrics.wrap(line, frame["width"] - (body_x - frame["x"]) - 50, 20)
                if body_y + text_metrics["height"] > frame["y"] + frame["height"] - 32:
                    raise ValueError(f"Page {index + 1} body exceeds real frame; split rather than truncate")
                ref = f"page:{index + 1}:body:{line_index}"
                operations.extend([
                    {"op": "create_text", "ref": ref, "x": body_x, "y": body_y, "text": text,
                     "style": {**profile["text"], "fontFamily": profile["fontFamily"], "fontSize": 20},
                     "customData": {"agentDiagram": {"role": "page-body", "logicalId": f"page-{index + 1}", "originalLabel": line}}},
                    {"op": "add_to_frame", "frame": frame_id, "targets": ["@" + ref]},
                ])
                if bullets and content:
                    bullet = bullets[min(line_index, len(bullets) - 1)]
                    bullet_y = body_y + 12 - bullet["height"] / 2
                    if line_index < len(bullets):
                        operations.append({"op": "patch_element", "target": bullet["id"], "patch": {"y": bullet_y}})
                    else:
                        bullet_ref = f"page:{index + 1}:bullet:{line_index}"
                        operations.extend([
                            {"op": "create_shape", "type": "ellipse", "ref": bullet_ref, "x": bullet["x"], "y": bullet_y,
                             "width": bullet["width"], "height": bullet["height"],
                             "style": {key: bullet[key] for key in ("strokeColor", "backgroundColor", "fillStyle", "roughness", "strokeWidth")},
                             "customData": {"agentLibrary": {**(bullet.get("customData") or {}).get("agentLibrary", {}), "sourceElementId": "generated-page-bullet"}}},
                            {"op": "add_to_frame", "frame": frame_id, "targets": ["@" + bullet_ref]},
                        ])
                body_y += text_metrics["height"] + 14
            for text in texts:
                if text["id"] == title_target["id"]:
                    continue
                # Only known source placeholders are replaced; decorative library elements remain intact.
                source_text = str(text.get("text", "")).strip().lower()
                if any(word in source_text for word in ("subtitle", "author", "content", "text here", "full name", "presentation", "title")):
                    operations.append({"op": "set_text", "target": text["id"], "text": ""})
            stage = "page_text"
            result = client.apply(token, revision, operations)
            revision = result["revision"]
            all_ids = [*imported["insertedElementIds"], *result["created"]]
            grouping = client.apply(token, revision, [{"op": "group", "targets": all_ids}])
            revision = grouping["revision"]
            output.append({"page": index + 1, "frameId": frame_id, "elementIds": all_ids, "titleId": title_target["id"], "title": title,
                           "template": item["name"], "bounds": {key: frame[key] for key in ("x", "y", "width", "height")}})
            applied.append({"stage": stage, "page": index + 1, "revision": revision,
                            "transactionId": result.get("transactionId"), "groupTransactionId": grouping.get("transactionId")})
            x = frame["x"] + frame["width"] + float(presentation.get("pageGap", 120))
            stage = "page_import"
        return {"ok": True, "contextToken": token, "revision": revision, "pages": output, "appliedStages": applied,
                "format": "Native Excalidraw frames; editable source, not a PPTX export", "next": "Export each page by its elementIds plus an all-canvas overview; inspect every page."}
    except Exception as error:
        raise CompositionError(str(error), stage, applied, error) from error
