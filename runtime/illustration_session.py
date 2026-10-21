"""Technical primitives share the existing scene reconciler, identities and conflicts."""

from __future__ import annotations

import copy
import json

from drawing_primitives import plan_primitives
from drawing_workflow import require_context
from illustration_geometry import KINDS
from scene_dsl.service import _locked, state_path
from scene_dsl.session import plan_update, reconcile


def execute(client, token, items, style, action, state_id, base_revision):
    if not state_id:
        raise ValueError("Managed technical primitives require a stable state_id")
    if not base_revision:
        raise ValueError(
            "Managed technical primitives require the current base_revision"
        )
    record = require_context(token)
    if not isinstance(style, dict) or not style.get("fontFamily"):
        raise ValueError(
            "Technical illustration requires an exact discovered style.fontFamily"
        )
    if any(item.get("kind") not in (*KINDS, "text") for item in items):
        raise ValueError(
            "Managed technical render supports projected_box/layer_stack/grid_array/leader/text; use ordinary plan/apply for other primitives"
        )
    document = "illustration-" + state_id
    # Same state store/lock/reconciler as existing source-driven scenes; no second ID system.
    path = state_path(client, document)
    with _locked(path):
        scene = client.read(token, detail="full")
        if scene["revision"] != base_revision:
            raise ValueError(
                "REVISION_CONFLICT: canvas changed before technical planning"
            )
        compiled = plan_primitives(client, token, items, style)
        entities, post = {}, []
        for source in compiled["operations"]:
            op = copy.deepcopy(source)
            if op["op"] == "group":
                post.append(op)
                continue
            key = op["ref"]
            if key in entities:
                raise ValueError("Duplicate technical logical reference: " + key)
            meta = op.setdefault("customData", {})
            primitive = meta.get("agentPrimitive")
            if primitive:
                # Existing caption/text planning uses a fresh unit; stabilize it for reconciliation.
                primitive["instanceId"] = (
                    "illustration:" + document + ":" + meta["agentDiagram"]["logicalId"]
                )
            meta["dsl"] = {"document": document, "key": key}
            entities[key] = op
        plan = {
            "document": document,
            "baseRevision": compiled["baseRevision"],
            "entities": entities,
            "post": post,
            "features": [],
            "acceptance": record["brief"]["preferences"]["review"]["value"],
            "routes": {},
        }
        state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
        diff = plan_update(plan, state, scene)
        common = {
            "stateId": state_id,
            "file": scene["file"],
            "contextToken": token,
            "revision": scene["revision"],
            "anchors": compiled["anchors"],
            "manifests": compiled["manifests"],
            "measuredBounds": compiled["measuredBounds"],
            "notes": compiled["notes"],
            "delivery_ready": False,
        }
        if action == "plan":
            return {
                **common,
                "status": "planned",
                "operations": diff["operations"],
                "operationCount": len(diff["operations"]),
                "diff": {k: v for k, v in diff.items() if k != "operations"},
            }
        receipt = reconcile(client, token, plan, path)
        try:
            inspected = client.inspect(token, receipt["revision"])
        except Exception as error:
            error.committed_receipt = receipt
            raise
        current = json.loads(path.read_text(encoding="utf-8"))
        return {
            **common,
            **receipt,
            **inspected,
            "ids": current["ids"],
            "visualReviewed": False,
            "status": "needs_repair"
            if inspected["check"]["status"] == "fail"
            else "rendered_needs_visual_review",
        }
