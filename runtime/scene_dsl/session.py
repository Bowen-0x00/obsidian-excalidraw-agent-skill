"""Managed scene reconciliation. Native IDs are discovered, not authored by DSL."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from .model import DslError, canonical

# Ignore engine caches, timestamps and version bookkeeping; protect actual user edits.
FIELDS = ("type", "x", "y", "width", "height", "angle", "points", "strokeColor", "backgroundColor", "strokeWidth", "strokeStyle", "roughness", "fillStyle", "opacity", "roundness", "startArrowhead", "endArrowhead", "startBinding", "endBinding", "boundElements", "groupIds", "frameId", "containerId", "text", "originalText", "fontFamily", "fontSize", "textAlign", "verticalAlign", "customData", "locked", "fileId", "link")


def fingerprint(element):
    values = {k: element.get(k) for k in FIELDS}
    # Some native save versions strip default focus/gap and nudge the fixed-point
    # representation. A change is a conflict, never silently 'fixed' by the DSL.
    return hashlib.sha256(canonical(values).encode()).hexdigest()


def index_scene(scene, document):
    result = {}
    for element in scene["elements"]:
        meta = (element.get("customData") or {}).get("dsl", {})
        if meta.get("document") != document or element.get("isDeleted"):
            continue
        key = meta.get("key")
        if key in result:
            raise DslError("identity." + key, "duplicate logical element on canvas; refuse ambiguous update")
        result[key] = element
    return result


def save_state(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def resolve_op(op, ids):
    value = copy.deepcopy(op)
    def ref(v):
        if isinstance(v, str) and v.startswith("@"):
            return ids[v[1:]] if v[1:] in ids else v
        return v
    for k in ("target", "from", "to", "arrow", "startTarget", "endTarget"):
        if k in value:
            value[k] = ref(value[k])
    if "targets" in value:
        value["targets"] = [ref(v) for v in value["targets"]]
    return value


def plan_update(plan, state, scene):
    if state and (state["document"] != plan["document"] or state["file"] != scene["file"]):
        raise DslError("state", "state belongs to another document/file")
    current = index_scene(scene, plan["document"])
    if not state and current:
        raise DslError("state", "managed scene already exists; recover its state instead of duplicating it")
    oldspec = state.get("entities", {}) if state else {}
    if state:
        if set(current) != set(state["snapshots"]):
            raise DslError("conflict", "managed elements were deleted/added externally; read/adopt explicitly")
        for key, element in current.items():
            if element["id"] != state["ids"].get(key) or fingerprint(element) != state["snapshots"][key]:
                raise DslError("conflict." + key, "managed content changed outside this state; do not overwrite user edits")
    ids = {key: element["id"] for key, element in current.items()}
    ops, created, updated, deleted = [], [], [], []
    newspec = plan["entities"]
    removed = set(oldspec) - set(newspec)
    # Drop owned obsolete edges before nodes; native executor repairs reciprocity.
    removals = []
    for key in sorted(removed, key=lambda k: not k.startswith("edge.")):
        removals.append(ids[key])
        if key + ":label" in ids:
            removals.append(ids[key + ":label"])
        deleted.append(key)
    if removals:
        ops.append({"op": "delete", "targets": list(dict.fromkeys(removals))})
    for key, spec in newspec.items():
        if key not in oldspec:
            ops.append(resolve_op(spec, ids))
            created.append(key)
            continue
        old = oldspec[key]
        if spec == old:
            continue
        op_type = spec["op"]
        if old["op"] != op_type or old.get("type") != spec.get("type") or (op_type in ("create_image", "create_latex", "create_embeddable") and any(old.get(k) != spec.get(k) for k in ("source", "tex"))):
            raise DslError("update." + key, "resource/kind replacement requires deleting the old item and using a new logical id")
        target = ids[key]
        if op_type == "connect":
            from_key, to_key = spec["from"][1:], spec["to"][1:]
            ops.append({"op": "rebind_arrow", "arrow": target, "startTarget": ids.get(from_key, "@" + from_key), "endTarget": ids.get(to_key, "@" + to_key), "start": spec["start"], "end": spec["end"], "preservePoints": True})
            route = plan["routes"][key.removeprefix("edge.")]
            x, y = route[0]
            ops.append({"op": "patch_element", "target": target, "patch": {"x": x, "y": y, "points": [[px - x, py - y] for px, py in route], "elbowed": False, "startArrowhead": spec["startArrowhead"], "endArrowhead": spec["endArrowhead"], **spec["style"]}})
        elif op_type == "create_text":
            ops.append({"op": "set_text", "target": target, "text": spec["text"], "style": spec["style"]})
            ops.append({"op": "patch_element", "target": target, "patch": {"x": spec["x"], "y": spec["y"]}})
        else:
            patch = {k: spec[k] for k in ("x", "y", "width", "height", "points", "polygon") if k in spec}
            if spec.get("polygon") and spec.get("closed") and patch.get("points") and patch["points"][-1] != patch["points"][0]:
                patch["points"] = [*patch["points"], list(patch["points"][0])]
            patch.update(spec.get("style", {}))
            ops.append({"op": "patch_element", "target": target, "patch": patch})
        if spec.get("label") != old.get("label") or (spec.get("label") and op_type != "create_text"):
            newlabel = spec.get("label")
            labelid = ids.get(key + ":label")
            if newlabel and labelid:
                ops.append({"op": "set_text", "target": labelid, "text": newlabel["text"], "style": newlabel["style"]})
            elif not newlabel and labelid:
                ops.append({"op": "delete", "targets": [labelid]})
            else:
                raise DslError("update." + key + ".label", "adding a previously absent bound label requires a new logical id")
        if spec["customData"] != old["customData"] or op_type == "connect":
            ops.append({"op": "patch_custom_data", "target": target, "merge": spec["customData"],
                        "remove": sorted(set(old["customData"]) - set(spec["customData"]))})
        if op_type == "connect":
            ops.append({"op": "set_arrow_style", "targets": [target], "arrowHeadSize": spec["arrowHeadSize"]})
        updated.append(key)
    for op in plan["post"]:
        if not state or op not in state.get("post", []):
            ops.append(resolve_op(op, ids))
    previous_features = state.get("features", []) if state else []
    for op in plan["features"]:
        if op not in previous_features:
            ops.append(resolve_op(op, ids))
    for op in previous_features:
        if any(target[1:] in removed or target[1:].removesuffix(":label") in removed for target in op["targets"]):
            continue
        if not any(new["feature"] == op["feature"] and new["targets"] == op["targets"] for new in plan["features"]):
            ops.append(resolve_op({"op": "clear_feature", "feature": op["feature"], "targets": op["targets"]}, ids))
    if len(ops) > 500:
        raise DslError("update", "transaction exceeds backend limit; split the scene")
    return {"operations": ops, "created": created, "updated": updated, "deleted": deleted, "unchanged": len(newspec) - len(created) - len(updated)}


def reconcile(client, token, plan, state_path):
    state_path = Path(state_path)
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else None
    scene = client.read(token, detail="full")
    if scene["revision"] != plan["baseRevision"]:
        raise DslError("revision", "canvas changed after compile; no mutation performed")
    diff = plan_update(plan, state, scene)
    receipt = None
    if diff["operations"]:
        # A single existing staged native transaction; no claimed cross-request atomicity.
        receipt = client.apply(token, scene["revision"], diff["operations"], acceptance_level=plan["acceptance"])
    try:
        after = client.read(token, detail="full")
        expected_revision = receipt["revision"] if receipt else scene["revision"]
        if after["revision"] != expected_revision:
            raise DslError("revision", "canvas changed before readback; state not adopted; inspect the committed receipt")
        owned = index_scene(after, plan["document"])
        next_state = {"version": 1, "document": plan["document"], "file": after["file"], "contextToken": token, "revision": after["revision"],
                      "ids": {k: e["id"] for k, e in owned.items()}, "snapshots": {k: fingerprint(e) for k, e in owned.items()},
                      "entities": plan["entities"], "post": plan["post"], "features": plan["features"]}
        # Persist before diagnostics/export; an inspection failure must not replay drawing.
        save_state(state_path, next_state)
    except Exception as error:
        error.committed_receipt = receipt
        raise
    return {"file": after["file"], "contextToken": token, "revision": after["revision"], "nativeCount": len(owned), "transaction": receipt,
            "diff": {k: v for k, v in diff.items() if k != "operations"}, "operationCount": len(diff["operations"]), "state": str(state_path)}
