"""Shared DSL execution for MCP and CLI; native drawing remains in DrawingClient."""
from __future__ import annotations

import base64
import copy
import hashlib
import json
import os
import re
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from drawing_client import DrawingClient
from runtime_config import load_connection, state_directory

from .compiler import Compiler
from .model import DslError, canonical, validate
from .session import plan_update, reconcile, save_state

_STATE_ID = re.compile(r"[A-Za-z_][A-Za-z0-9_-]{0,95}\Z")


def state_path(client: DrawingClient, state_id: str) -> Path:
    """Scope managed identities to the connection's host/vault, never its token."""
    if not _STATE_ID.fullmatch(state_id):
        raise DslError("state_id", "use an ASCII identifier of at most 96 characters")
    connection = load_connection()
    scope = {"bridge": client.bridge_url,
             "vault": connection.get("host_vault_path") or connection.get("vault_path"),
             "name": connection.get("vault_name")}
    key = hashlib.sha256(canonical(scope).encode("utf-8")).hexdigest()[:16]
    return state_directory() / "scene-dsl" / key / (state_id + ".json")


@contextmanager
def _locked(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_suffix(".lock")
    try:
        descriptor = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError as error:
        raise DslError("state_id", "another operation owns this scene state; inspect its process before removing a stale lock") from error
    try:
        os.write(descriptor, str(os.getpid()).encode("ascii"))
        yield
    finally:
        os.close(descriptor)
        lock.unlink()


def _assets(document: dict[str, Any], source_directory: Path | None) -> None:
    for name, node in document["nodes"].items():
        source = node.get("source", "")
        if node.get("shape") != "image" or not source.startswith("asset:"):
            continue
        if source_directory is None:
            raise DslError("nodes." + name + ".source", "asset: references require a CLI source file; MCP accepts data URLs or host resources")
        directory = source_directory.resolve()
        asset = (directory / source.removeprefix("asset:")).resolve()
        if not asset.is_relative_to(directory) or asset.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            raise DslError("nodes." + name + ".source", "asset must be a PNG/JPEG beneath the source directory")
        if asset.stat().st_size > 2_000_000:
            raise DslError("nodes." + name + ".source", "local asset exceeds the 2 MB upload budget")
        raw = asset.read_bytes()
        mime = "image/png" if asset.suffix.lower() == ".png" else "image/jpeg"
        node["source"] = "data:" + mime + ";base64," + base64.b64encode(raw).decode("ascii")


def execute(
    client: DrawingClient,
    action: str,
    document: dict[str, Any],
    *,
    font_family: str | None = None,
    state_id: str | None = None,
    filename: str | None = None,
    foldername: str | None = None,
    file_path: str | None = None,
    scale: str | float = "auto",
    acceptance_level: str | None = None,
    source_directory: Path | None = None,
    output_path: Path | None = None,
    brief: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Plan without scene mutation, or reconcile then check/export one exact revision.

    A render is not visual approval. Returns the actual preview bytes for the MCP
    wrapper; CLI removes them after the native client has written the PNG.
    """
    if action not in ("plan", "render"):
        raise DslError("action", "choose plan or render")
    doc = copy.deepcopy(document)
    validate(doc)
    if acceptance_level is not None:
        if acceptance_level not in ("low", "medium", "high"):
            raise DslError("acceptance_level", "low, medium or high")
        doc["acceptance"] = acceptance_level
    font = font_family or doc.get("style", {}).get("font")
    if not font:
        raise DslError("font_family", "select an exact current host family using discovery/fonts; there is no machine-specific default")
    description_bytes = len(canonical(doc).encode("utf-8"))
    _assets(doc, source_directory)
    identity = state_id or doc["id"]
    path = state_path(client, identity)
    started = time.perf_counter()
    with _locked(path):
        state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
        if state:
            if state["document"] != doc["id"]:
                raise DslError("state_id", "this state belongs to a different document")
            if file_path is not None and state["file"] != file_path:
                raise DslError("file_path", "this state already owns a different canvas")
            token = state["contextToken"]
            try:
                client.read(token)
            except Exception as error:
                if getattr(error, "code", None) not in ("CONTEXT_NOT_FOUND", "INVALID_CONTEXT", "CONTEXT_EXPIRED"):
                    raise
                token = client.context("bind", file_path=state["file"], brief=brief)["contextToken"]
            if brief is not None:
                token = client.context("bind", file_path=state["file"], brief=brief)["contextToken"]
        elif file_path:
            context = client.context("bind", file_path=file_path, brief=brief)
            token = context["contextToken"]
        elif action == "plan":
            raise DslError("file_path", "read-only planning needs existing managed state or an explicit existing canvas for native measurement")
        elif not filename:
            raise DslError("filename", "first render needs a unique filename or an explicit existing file_path")
        else:
            context = client.context("create", filename=filename, foldername=foldername or "Agent-Diagrams", brief=brief)
            token = context["contextToken"]
            # Keep the empty target identity even if compilation fails. A retry
            # must not silently create a second canvas.
            state = {"version": 1, "document": doc["id"], "file": context["file"],
                     "contextToken": token, "revision": context["revision"],
                     "ids": {}, "snapshots": {}, "entities": {}, "post": [], "features": []}
            save_state(path, state)
        if action == "render":
            settings = client.review_settings(token, doc.get("acceptance"))
            doc["acceptance"] = settings.acceptance_level
        plan = Compiler(client, token, doc, font).compile()
        scene = client.read(token, detail="full")
        if scene["revision"] != plan["baseRevision"]:
            raise DslError("revision", "canvas changed after compilation; no mutation performed")
        common = {"file": scene["file"], "contextToken": token, "revision": scene["revision"],
                  "stateId": identity, "compiledEntities": len(plan["entities"]),
                  "descriptionBytes": description_bytes, "font": font,
                  "acceptanceLevel": plan["acceptance"], "limits": plan["limits"],
                  "layout": {"boxes": plan["boxes"], "routes": plan["routes"]}}
        if action == "plan":
            diff = plan_update(plan, state, scene)
            return {**common, "status": "planned", "operations": diff["operations"],
                    "operationCount": len(diff["operations"]), "expected": plan["expected"],
                    "diff": {key: value for key, value in diff.items() if key != "operations"}}
        receipt = None
        try:
            receipt = reconcile(client, token, plan, path)
            checked = client.check(token, expected=plan["expected"], acceptance_level=plan["acceptance"])
            if checked["revision"] != receipt["revision"]:
                raise DslError("revision", "canvas changed before inspection; drawing was already committed")
            preview = client.preview(token, base_revision=checked["revision"], scale=scale,
                                     out_path=str(output_path.with_suffix(".png")) if output_path else None)
            checked = client.check(token, preview_id=preview["previewId"])
        except Exception as error:
            if not hasattr(error, "committed_receipt"):
                error.committed_receipt = receipt
            raise
        return {**common, **receipt, "stateId": identity, "check": checked, "preview": preview,
                "visualReviewed": False,
                "status": "rendered_needs_visual_review" if checked["status"] == "pass" and preview["complete"] else "needs_attention",
                "timings": {"totalMs": (time.perf_counter() - started) * 1000}}
