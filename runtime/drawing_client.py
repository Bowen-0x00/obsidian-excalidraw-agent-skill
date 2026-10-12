from __future__ import annotations

import argparse
import base64
import hashlib
import json
import math
import os
import re
import struct
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
from typing import Any

_RUNTIME_DIR = str(Path(__file__).resolve().parent)
if _RUNTIME_DIR not in sys.path:
    sys.path.insert(0, _RUNTIME_DIR)

from runtime_config import artifact_directory, load_connection

from geometry_diagnostics import run_geometry_diagnostics
from review_ledger import ReviewLedger
from diagram_layout import FONT, Metrics, plan_diagram
from drawing_templates import get_template, plan_template, template_catalog
from drawing_composition import CompositionError, compose_diagram, create_presentation
from drawing_styles import resolve_style


class BridgeError(RuntimeError):
    """Exception raised when an Excalidraw Bridge call fails."""

    def __init__(
        self,
        message: str,
        code: str = "BRIDGE_ERROR",
        status: int = 500,
        details: Any = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.status = status
        self.details = details

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": False,
            "error": {
                "code": self.code,
                "message": str(self),
                "status": self.status,
                "details": self.details,
            },
        }


def resolve_bridge_credentials() -> tuple[str, str, float]:
    """Resolve bridge URL, bearer token, and timeout from environment or private connection.

    Never logs or exposes the token.
    Credentials environment overrides private connection.
    No implicit .omp/mcp.json fallback in public runtime.
    """
    connection = load_connection()

    url = os.environ.get("EXCALIDRAW_BRIDGE_URL") or connection.get("bridge_url")
    token = os.environ.get("EXCALIDRAW_BRIDGE_TOKEN") or connection.get("bridge_token")
    timeout = os.environ.get("EXCALIDRAW_BRIDGE_TIMEOUT") or connection.get("bridge_timeout")

    bridge_url = (url or "http://127.0.0.1:27124").rstrip("/")
    bridge_token = token or ""
    try:
        bridge_timeout = float(timeout or "180.0")
    except (ValueError, TypeError):
        bridge_timeout = 180.0

    return bridge_url, bridge_token, bridge_timeout


class DrawingClient:
    """Client for controlling Obsidian Excalidraw through the local Bridge service."""

    def __init__(
        self,
        bridge_url: str | None = None,
        bridge_token: str | None = None,
        timeout: float | None = None,
    ) -> None:
        resolved_url, resolved_token, resolved_timeout = resolve_bridge_credentials()
        self.bridge_url = (bridge_url or resolved_url).rstrip("/")
        self.bridge_token = bridge_token if bridge_token is not None else resolved_token
        # Authenticated loopback traffic must never leave the machine through an environment proxy.
        host = urllib.parse.urlsplit(self.bridge_url).hostname
        self.opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({}) if host in ("127.0.0.1", "localhost", "::1") else urllib.request.ProxyHandler()
        )
        self.timeout = timeout if timeout is not None else resolved_timeout

    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
    ) -> Any:
        """Send an HTTP request to the local Bridge and return the unpacked response data.

        Raises BridgeError on failures.
        """
        if not self.bridge_token:
            raise BridgeError(
                "EXCALIDRAW_BRIDGE_TOKEN is not configured.",
                code="AUTH_MISSING",
                status=401,
            )

        target_url = f"{self.bridge_url}{path}"
        headers = {
            "Authorization": f"Bearer {self.bridge_token}",
            "Accept": "application/json",
        }

        body_bytes: bytes | None = None
        if payload is not None:
            body_bytes = json.dumps(
                payload,
                ensure_ascii=False,
                separators=(",", ":"),
            ).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = urllib.request.Request(
            target_url,
            data=body_bytes,
            headers=headers,
            method=method.upper(),
        )

        try:
            with self.opener.open(req, timeout=self.timeout) as resp:
                resp_bytes = resp.read()
                if not resp_bytes:
                    raise BridgeError("Bridge returned an empty response", code="INVALID_RESPONSE", status=502)
                data = json.loads(resp_bytes.decode("utf-8"))
                if isinstance(data, dict) and data.get("ok") is False:
                    err = data.get("error") or {}
                    raise BridgeError(
                        err.get("message", "Bridge operation failed"),
                        code=err.get("code", "BRIDGE_ERROR"),
                        status=resp.status,
                        details=err.get("details"),
                    )
                return data
        except urllib.error.HTTPError as e:
            err_msg = f"HTTP {e.code} error from Bridge"
            code = "HTTP_ERROR"
            details = None
            try:
                err_body = e.read().decode("utf-8")
                parsed = json.loads(err_body)
                if isinstance(parsed, dict) and "error" in parsed:
                    err_obj = parsed["error"]
                    err_msg = err_obj.get("message", err_msg)
                    code = err_obj.get("code", code)
                    details = err_obj.get("details")
            except Exception:
                pass
            raise BridgeError(err_msg, code=code, status=e.code, details=details) from e
        except urllib.error.URLError as e:
            raise BridgeError(
                f"Failed to connect to Excalidraw Bridge at {self.bridge_url}: {e.reason}",
                code="CONNECTION_FAILED",
                status=503,
            ) from e
        except TimeoutError as e:
            raise BridgeError(
                f"Bridge request timed out after {self.timeout}s",
                code="TIMEOUT",
                status=504,
            ) from e

    def context(
        self,
        action: str,
        filename: str | None = None,
        foldername: str | None = None,
        file_path: str | None = None,
    ) -> dict[str, Any]:
        """Manage canvas context: discover capabilities, create a new canvas, or bind an existing one."""
        action_lower = action.lower()
        if action_lower == "discover":
            status_data = self.request("GET", "/v3/status")
            cap_data = self.request("GET", "/v3/runtime-capabilities")
            return {
                "ok": True,
                "action": "discover",
                "status": status_data,
                "capabilities": cap_data,
            }

        elif action_lower == "create":
            payload: dict[str, Any] = {}
            if filename:
                payload["filename"] = filename
            if foldername:
                payload["foldername"] = foldername
            return self.request("POST", "/v3/canvases/create", payload)

        elif action_lower == "bind":
            payload = {}
            if file_path:
                payload["filePath"] = file_path
            return self.request("POST", "/v3/canvases/bind", payload)

        else:
            raise BridgeError(
                f"Unknown action '{action}'. Must be 'discover', 'create', or 'bind'.",
                code="INVALID_ARGUMENT",
                status=400,
            )

    def read(
        self,
        context_token: str,
        ids: list[str] | None = None,
        detail: str = "summary",
        offset: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        """Read canvas elements: specific IDs, paginated query, or complete summary."""
        detail = "style" if detail == "detail" else detail
        if ids is not None:
            pages = [
                self.request("POST", "/v3/elements/get", {
                    "contextToken": context_token, "ids": ids[start:start + 2000], "detail": detail,
                })
                for start in range(0, len(ids), 2000)
            ]
            if not pages:
                context = self.request("POST", "/v3/context", {"contextToken": context_token, "includeElements": False})
                return {"revision": context["revision"], "total": 0, "elements": [], "coverage": "complete"}
            revision = pages[0]["revision"]
            if any(page["revision"] != revision for page in pages):
                raise BridgeError("Canvas changed during ID traversal", code="REVISION_CONFLICT", status=409)
            elements = [element for page in pages for element in page["elements"]]
            return {"revision": revision, "total": len(elements), "elements": elements, "coverage": "complete"}
        if detail == "summary" and offset is None and limit is None:
            result = self.request("POST", "/v3/elements/summary", {"contextToken": context_token})
            return {**result, "coverage": "complete"}
        if offset is not None or limit is not None:
            result = self.request("POST", "/v3/elements/query", {
                "contextToken": context_token, "detail": detail, "offset": offset or 0, "limit": limit or 2000,
            })
            return {**result, "coverage": "page"}
        elements, revision, cursor = [], None, 0
        while True:
            page = self.request("POST", "/v3/elements/query", {
                "contextToken": context_token, "detail": detail, "offset": cursor, "limit": 2000,
            })
            revision = revision or page["revision"]
            if page["revision"] != revision:
                raise BridgeError("Canvas changed during complete traversal", code="REVISION_CONFLICT", status=409)
            elements.extend(page["elements"])
            if not page["truncated"]:
                return {"revision": revision, "total": page["total"], "elements": elements, "coverage": "complete"}
            if not page["elements"]:
                raise BridgeError("Incomplete element page", code="INVALID_RESPONSE", status=502)
            cursor += len(page["elements"])

    def measure(
        self,
        context_token: str,
        text: str | None = None,
        font_family: str | None = None,
        font_size: float = 20.0,
        line_height: float = 1.2,
        width: float | None = None,
        items: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """Measure text dimensions using native Bridge text measurement."""
        style: dict[str, Any] = {
            "fontSize": font_size,
            "lineHeight": line_height,
        }
        if font_family:
            style["fontFamily"] = font_family

        if items:
            measured_items = []
            for item in items:
                item_text = item.get("text", "")
                item_style = {
                    "fontSize": item.get("font_size", font_size),
                    "lineHeight": item.get("line_height", line_height),
                }
                if item.get("font_family") or font_family:
                    item_style["fontFamily"] = item.get("font_family") or font_family

                m_res = self.request(
                    "POST",
                    "/v3/text/measure",
                    {
                        "contextToken": context_token,
                        "text": item_text,
                        "style": item_style,
                    },
                )
                measured_items.append({
                    "text": item_text,
                    "width": m_res.get("width"),
                    "height": m_res.get("height"),
                    "style": item_style,
                })
            return {"ok": True, "items": measured_items}

        target_text = text or ""

        if width is not None:
            if not math.isfinite(width) or width <= 0:
                raise ValueError("width must be finite and positive")
            measured = Metrics(self, context_token, font_family or FONT)
            wrapped_text, size = measured.wrap(target_text, width, font_size, line_height)
            return {
                "ok": True, "text": wrapped_text, "originalText": target_text,
                "lines": wrapped_text.split("\n"), **size,
                "style": {**style, "fontFamily": measured.font},
            }

        res = self.request(
            "POST",
            "/v3/text/measure",
            {
                "contextToken": context_token,
                "text": target_text,
                "style": style,
            },
        )
        return {
            "ok": True,
            "text": target_text,
            "width": res.get("width"),
            "height": res.get("height"),
            "style": style,
        }


    def plan(self, context_token: str, diagram: dict[str, Any]) -> dict[str, Any]:
        """Plan native diagram operations with real measured content dimensions."""
        return plan_diagram(self, context_token, diagram)

    def apply(
        self,
        context_token: str,
        base_revision: str,
        operations: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Apply a batch of operations to the canvas."""
        return self.request(
            "POST",
            "/v3/operations/apply",
            {
                "contextToken": context_token,
                "baseRevision": base_revision,
                "operations": operations,
            },
        )

    def check(
        self,
        context_token: str,
        expected: list[dict[str, Any]] | None = None,
        scope: str = "all",
    ) -> dict[str, Any]:
        """Check the complete exact scene; a failed validator is not a successful check."""
        scene = self.read(context_token, detail="full")
        validation = self.request("POST", "/v3/scene/validate", {"contextToken": context_token, "scope": "all"})
        if validation["revision"] != scene["revision"]:
            raise BridgeError("Canvas changed between geometry and structural checks", code="REVISION_CONFLICT", status=409)
        diagnostics = run_geometry_diagnostics(scene["elements"], expected=expected, structural_validation=validation)
        diagnostics.update(revision=scene["revision"], contextToken=context_token, coverage="complete", expected=expected or [])
        return diagnostics

    def preview(
        self,
        context_token: str,
        base_revision: str | None = None,
        scope: str = "all",
        ids: list[str] | None = None,
        scale: str | float = "auto",
        padding: float = 20.0,
        out_path: str | None = None,
    ) -> dict[str, Any]:
        """Render the canvas to PNG, save the artifact, and return metadata."""
        payload: dict[str, Any] = {
            "contextToken": context_token,
            "scope": scope,
            "ids": ids or [],
            "padding": padding,
        }
        if base_revision:
            payload["baseRevision"] = base_revision
        if scale is not None:
            payload["scale"] = scale

        res = self.request("POST", "/v3/render", payload)

        image = res.get("image") or {}
        b64_str = image.get("base64", "")
        if b64_str.startswith("data:"):
            b64_str = b64_str.split(",", 1)[1]
        if not b64_str:
            raise BridgeError("Exporter returned no image", code="PNG_EXPORT_FAILED", status=502)
        png = base64.b64decode(b64_str, validate=True)
        if len(png) < 24 or png[:8] != b"\x89PNG\r\n\x1a\n":
            raise BridgeError("Exporter did not return a PNG", code="PNG_EXPORT_FAILED", status=502)
        width, height = struct.unpack(">II", png[16:24])
        if not width or not height:
            raise BridgeError("Exporter returned zero-sized PNG", code="PNG_EXPORT_FAILED", status=502)
        if "complete" not in res or not res.get("revision"):
            raise BridgeError("Exporter omitted completeness or state identity", code="INVALID_RESPONSE", status=502)
        preview_id = f"prev_{int(time.time())}_{uuid.uuid4().hex[:8]}"
        target_file = Path(out_path).resolve() if out_path else (artifact_directory() / "previews" / f"{preview_id}.png").resolve()
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_bytes(png)
        metadata = {
            "ok": True, "previewId": preview_id, "contextToken": context_token,
            "revision": res["revision"], "file": res.get("file"),
            "actualScale": res.get("actualScale"), "width": width, "height": height,
            "bounds": res.get("bounds"), "transform": res.get("transform"),
            "complete": res["complete"], "scope": scope, "resourceIssues": res.get("resourceIssues", []),
            "out_path": str(target_file), "sha256": hashlib.sha256(png).hexdigest(),
        }
        receipts = artifact_directory() / "previews"
        receipts.mkdir(parents=True, exist_ok=True)
        (receipts / f"{preview_id}.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
        return {**metadata, "_base64": b64_str}

    def review(
        self,
        context_token: str,
        revision: str,
        preview_id: str,
        visual_reviewed: bool = False,
        visual_issues: list[dict[str, Any]] | None = None,
        changes_summary: str | list[Any] | None = None,
        check_result: dict[str, Any] | None = None,
        max_rounds: int = 5,
    ) -> dict[str, Any]:
        """Review a registered, current PNG; re-run hard checks rather than trusting model-supplied results."""
        if not re.fullmatch(r"prev_[0-9]+_[0-9a-f]{8}", preview_id):
            raise BridgeError("Invalid preview ID", code="PREVIEW_NOT_FOUND", status=404)
        receipt_path = artifact_directory() / "previews" / f"{preview_id}.json"
        if not receipt_path.exists():
            raise BridgeError("Preview was not produced by this execution layer", code="PREVIEW_NOT_FOUND", status=404)
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        if receipt["contextToken"] != context_token or receipt["revision"] != revision:
            raise BridgeError("Preview belongs to a different canvas or state", code="STALE_PREVIEW", status=409)
        if receipt["scope"] != "all":
            raise BridgeError("Completion requires an all-canvas overview", code="INCOMPLETE_COVERAGE", status=422)
        png_file = Path(receipt["out_path"])
        if not png_file.is_file() or hashlib.sha256(png_file.read_bytes()).hexdigest() != receipt["sha256"]:
            raise BridgeError("Preview artifact changed or is missing", code="PREVIEW_CHANGED", status=409)
        fresh_check = self.check(context_token, expected=(check_result or {}).get("expected"))
        if fresh_check["revision"] != revision:
            raise BridgeError("Canvas changed after PNG export", code="STALE_PREVIEW", status=409)
        ledger = ReviewLedger(context_token, max_rounds=max_rounds)
        return ledger.record_round(
            revision=revision, preview_id=preview_id, visual_reviewed=visual_reviewed,
            visual_issues=visual_issues, changes_summary=changes_summary,
            check_result=fresh_check, preview_complete=receipt["complete"],
        )

    def revert(
        self,
        context_token: str,
        transaction_id: str | None = None,
    ) -> dict[str, Any]:
        """Undo the most recent transaction or a specific transaction ID."""
        payload: dict[str, Any] = {"contextToken": context_token}
        if transaction_id:
            payload["transactionId"] = transaction_id
        return self.request("POST", "/v3/transactions/undo", payload)

    def templates(self, action: str = "list", name: str | None = None, context_token: str | None = None,
                  data: dict | None = None, style: str | dict | None = None) -> dict:
        if action == "list":
            return template_catalog()
        if action == "get" and name:
            return get_template(name, style)
        if action == "plan" and name and context_token:
            return plan_template(self, context_token, name, data, style)
        raise ValueError("Use template action list/get/plan; get/plan require name, plan requires context_token")

    def primitives(self, context_token: str, items: list[dict], style: str | dict | None = None) -> dict:
        from drawing_primitives import plan_primitives
        if isinstance(style, str) or isinstance(style, dict) and "profile" in style:
            profile = resolve_style(style)
            style = {**profile["shape"], "fontFamily": profile["fontFamily"], "fontSize": profile["fontSize"],
                     "strokeColor": profile["text"]["strokeColor"]}
        return plan_primitives(self, context_token, items, style)

    def library(self, action: str, context_token: str, library: str | None = None, item: str | None = None,
                position: str | dict = "center", scale: float = 1, base_revision: str | None = None,
                offset: int = 0, limit: int = 100, text: str | None = None, detail: str = "summary",
                create_anchor_proxy: bool = True, trusted_local_library: bool = False,
                logical_id: str | None = None, diagram_id: str | None = None, out_path: str | None = None) -> dict:
        paths = {"list": "/v3/libraries/list", "query": "/v3/libraries/items/query",
                 "get": "/v3/libraries/items/get", "preview": "/v3/libraries/items/preview",
                 "insert": "/v3/libraries/insert"}
        if action not in paths:
            raise ValueError("Library action must be list/query/get/preview/insert")
        payload = {"contextToken": context_token}
        if action != "list":
            if not library:
                raise ValueError("An explicit library source or unique installed name is required")
            payload["library"] = library
        if action in ("get", "preview", "insert"):
            if not item:
                raise ValueError("An exact item ID or unique name is required")
            payload["item"] = item
        if action == "query":
            payload.update(offset=offset, limit=limit, text=text)
        if action == "get":
            payload["detail"] = detail
        if action in ("preview", "insert"):
            payload["scale"] = scale
            payload["trustedLocalLibrary"] = trusted_local_library
        if action == "insert":
            if not base_revision:
                raise ValueError("Native insertion requires the current base_revision")
            payload.update(baseRevision=base_revision, position=position, createAnchorProxy=create_anchor_proxy,
                           logicalId=logical_id, diagramId=diagram_id)
        result = self.request("POST", paths[action], payload)
        if action == "preview":
            encoded = result["image"]["base64"]
            if encoded.startswith("data:"):
                encoded = encoded.split(",", 1)[1]
            data_bytes = base64.b64decode(encoded, validate=True)
            if len(data_bytes) < 24 or data_bytes[:8] != b"\x89PNG\r\n\x1a\n":
                raise BridgeError("Library preview did not return a PNG", code="PNG_EXPORT_FAILED")
            path = Path(out_path).resolve() if out_path else (artifact_directory() / "library-previews" / f"{uuid.uuid4().hex}.png").resolve()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data_bytes)
            result = {key: value for key, value in result.items() if key != "image"}
            result.update(out_path=str(path), _base64=encoded, coverage="library-item")
        return result

    def compose(self, context_token: str, base_revision: str, diagram: dict) -> dict:
        try:
            return compose_diagram(self, context_token, base_revision, diagram)
        except CompositionError as error:
            raise BridgeError(str(error), code=getattr(error.cause, "code", "COMPOSITION_FAILED"),
                              status=getattr(error.cause, "status", 422),
                              details={"phase": error.stage, "appliedStages": error.applied,
                                       "cause": getattr(error.cause, "details", None), "atomic": False}) from error

    def present(self, context_token: str, base_revision: str, presentation: dict) -> dict:
        try:
            return create_presentation(self, context_token, base_revision, presentation)
        except CompositionError as error:
            raise BridgeError(str(error), code=getattr(error.cause, "code", "PRESENTATION_FAILED"),
                              status=getattr(error.cause, "status", 422),
                              details={"phase": error.stage, "appliedStages": error.applied,
                                       "cause": getattr(error.cause, "details", None), "atomic": False}) from error


def create_cli_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser with subcommands."""
    parser = argparse.ArgumentParser(
        prog="drawing_client",
        description="CLI client for Obsidian Excalidraw Bridge",
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # 1. context
    p_ctx = subparsers.add_parser("context", help="Discover, create, or bind canvas")
    p_ctx.add_argument("--action", choices=["discover", "create", "bind"], required=True)
    p_ctx.add_argument("--filename", help="Target filename for create")
    p_ctx.add_argument("--foldername", help="Target folder for create")
    p_ctx.add_argument("--file-path", help="Existing file path for bind")

    # 2. read
    p_read = subparsers.add_parser("read", help="Read elements from canvas")
    p_read.add_argument("--context-token", required=True)
    p_read.add_argument("--ids", help="Comma-separated element IDs")
    p_read.add_argument("--detail", choices=["summary", "detail", "full"], default="summary")
    p_read.add_argument("--offset", type=int)
    p_read.add_argument("--limit", type=int)

    # 3. measure
    p_meas = subparsers.add_parser("measure", help="Measure text dimensions")
    p_meas.add_argument("--context-token", required=True)
    p_meas.add_argument("--text")
    p_meas.add_argument("--font-family")
    p_meas.add_argument("--font-size", type=float, default=20.0)
    p_meas.add_argument("--line-height", type=float, default=1.2)
    p_meas.add_argument("--width", type=float)
    p_meas.add_argument("--items", help="JSON string of batch items")
    p_meas.add_argument("--items-file", help="Path to JSON file of batch items")

    # 4. plan
    p_plan = subparsers.add_parser("plan", help="Plan diagram layout without applying")
    p_plan.add_argument("--context-token", required=True)
    p_plan.add_argument("--diagram", help="JSON string of diagram specification")
    p_plan.add_argument("--diagram-file", help="Path to JSON file of diagram specification")

    # 5. apply
    p_apply = subparsers.add_parser("apply", help="Apply operations to canvas")
    p_apply.add_argument("--context-token", required=True)
    p_apply.add_argument("--base-revision", required=True)
    p_apply.add_argument("--operations", help="JSON string of operations array")
    p_apply.add_argument("--operations-file", help="Path to JSON file containing operations")

    # 6. check
    p_check = subparsers.add_parser("check", help="Run geometry and structural checks")
    p_check.add_argument("--context-token", required=True)
    p_check.add_argument("--expected", help="JSON string of expected semantic assertions")
    p_check.add_argument("--expected-file", help="Path to JSON file of expected semantic assertions")
    p_check.add_argument("--scope", default="all")

    # 7. preview
    p_prev = subparsers.add_parser("preview", help="Render canvas to PNG preview")
    p_prev.add_argument("--context-token", required=True)
    p_prev.add_argument("--base-revision")
    p_prev.add_argument("--scope", default="all")
    p_prev.add_argument("--ids", help="Comma-separated element IDs")
    p_prev.add_argument("--scale", default="auto")
    p_prev.add_argument("--padding", type=float, default=20.0)
    p_prev.add_argument("--out-path", help="Output PNG path")

    # 8. review
    p_rev = subparsers.add_parser("review", help="Record review round in persistent ledger")
    p_rev.add_argument("--context-token", required=True)
    p_rev.add_argument("--revision", required=True)
    p_rev.add_argument("--preview-id", required=True)
    p_rev.add_argument("--visual-reviewed", action="store_true", default=False)
    p_rev.add_argument("--visual-issues", help="JSON string of visual issues")
    p_rev.add_argument("--visual-issues-file", help="Path to JSON file of visual issues")
    p_rev.add_argument("--changes-summary")
    p_rev.add_argument("--check-result", help="JSON string of check result")
    p_rev.add_argument("--check-result-file", help="Path to JSON file of check result")
    p_rev.add_argument("--max-rounds", type=int, default=5)

    # 9. revert
    p_revt = subparsers.add_parser("revert", help="Undo last canvas transaction")
    p_revt.add_argument("--context-token", required=True)
    p_revt.add_argument("--transaction-id")

    # 10. json
    p_json = subparsers.add_parser("json", help="Execute single-payload JSON request or read from stdin")
    p_json.add_argument("--request", help="JSON request payload string")

    for command in ("template", "primitives", "library", "compose", "present"):
        extended = subparsers.add_parser(command, help=f"Execute typed {command} arguments from JSON")
        source = extended.add_mutually_exclusive_group(required=True)
        source.add_argument("--request", help="JSON object containing method arguments")
        source.add_argument("--request-file", help="UTF-8 JSON file containing method arguments")

    return parser


def cli_main() -> None:
    parser = create_cli_parser()
    args = parser.parse_args()

    client = DrawingClient()

    try:
        sub = args.subcommand
        if sub == "context":
            result = client.context(
                action=args.action,
                filename=args.filename,
                foldername=args.foldername,
                file_path=args.file_path,
            )

        elif sub == "read":
            ids_list = [x.strip() for x in args.ids.split(",")] if args.ids else None
            result = client.read(
                context_token=args.context_token,
                ids=ids_list,
                detail=args.detail,
                offset=args.offset,
                limit=args.limit,
            )

        elif sub == "measure":
            items = None
            if args.items_file:
                items = json.loads(Path(args.items_file).read_text(encoding="utf-8"))
            elif args.items:
                items = json.loads(args.items)

            result = client.measure(
                context_token=args.context_token,
                text=args.text,
                font_family=args.font_family,
                font_size=args.font_size,
                line_height=args.line_height,
                width=args.width,
                items=items,
            )

        elif sub == "plan":
            diagram_data = None
            if args.diagram_file:
                diagram_data = json.loads(Path(args.diagram_file).read_text(encoding="utf-8"))
            elif args.diagram:
                diagram_data = json.loads(args.diagram)
            else:
                raise BridgeError("Missing --diagram or --diagram-file", code="INVALID_ARGUMENT", status=400)

            result = client.plan(
                context_token=args.context_token,
                diagram=diagram_data,
            )

        elif sub == "apply":
            ops = None
            if args.operations_file:
                ops = json.loads(Path(args.operations_file).read_text(encoding="utf-8"))
            elif args.operations:
                ops = json.loads(args.operations)
            else:
                raise BridgeError("Missing --operations or --operations-file", code="INVALID_ARGUMENT", status=400)

            result = client.apply(
                context_token=args.context_token,
                base_revision=args.base_revision,
                operations=ops,
            )

        elif sub == "check":
            expected = None
            if args.expected_file:
                expected = json.loads(Path(args.expected_file).read_text(encoding="utf-8"))
            elif args.expected:
                expected = json.loads(args.expected)

            result = client.check(
                context_token=args.context_token,
                expected=expected,
                scope=args.scope,
            )

        elif sub == "preview":
            ids_list = [x.strip() for x in args.ids.split(",")] if args.ids else None
            scale_val = args.scale
            try:
                scale_val = float(scale_val)
            except ValueError:
                pass

            res = client.preview(
                context_token=args.context_token,
                base_revision=args.base_revision,
                scope=args.scope,
                ids=ids_list,
                scale=scale_val,
                padding=args.padding,
                out_path=args.out_path,
            )
            # Remove raw base64 from CLI stdout to keep it clean and compact
            res.pop("_base64", None)
            result = res

        elif sub == "review":
            visual_issues = None
            if args.visual_issues_file:
                visual_issues = json.loads(Path(args.visual_issues_file).read_text(encoding="utf-8"))
            elif args.visual_issues:
                visual_issues = json.loads(args.visual_issues)

            check_res = None
            if args.check_result_file:
                check_res = json.loads(Path(args.check_result_file).read_text(encoding="utf-8"))
            elif args.check_result:
                check_res = json.loads(args.check_result)

            result = client.review(
                context_token=args.context_token,
                revision=args.revision,
                preview_id=args.preview_id,
                visual_reviewed=args.visual_reviewed,
                visual_issues=visual_issues,
                changes_summary=args.changes_summary,
                check_result=check_res,
                max_rounds=args.max_rounds,
            )

        elif sub == "revert":
            result = client.revert(
                context_token=args.context_token,
                transaction_id=args.transaction_id,
            )

        elif sub in ("template", "primitives", "library", "compose", "present"):
            parameters = json.loads(Path(args.request_file).read_text(encoding="utf-8") if args.request_file else args.request)
            method = "templates" if sub == "template" else sub
            result = getattr(client, method)(**parameters)
            result.pop("_base64", None)

        elif sub == "json":
            raw_input = args.request
            if not raw_input:
                raw_input = sys.stdin.read()
            req = json.loads(raw_input)
            tool = req.get("tool") or req.get("action")
            args_dict = req.get("arguments") or req.get("args") or req

            if tool in ("drawing_context", "context"):
                result = client.context(**args_dict)
            elif tool in ("drawing_read", "read"):
                result = client.read(**args_dict)
            elif tool in ("drawing_measure", "measure"):
                result = client.measure(**args_dict)
            elif tool in ("drawing_plan", "plan"):
                result = client.plan(**args_dict)
            elif tool in ("drawing_apply", "apply"):
                result = client.apply(**args_dict)
            elif tool in ("drawing_check", "check"):
                result = client.check(**args_dict)
            elif tool in ("drawing_preview", "preview"):
                res = client.preview(**args_dict)
                res.pop("_base64", None)
                result = res
            elif tool in ("drawing_review", "review"):
                result = client.review(**args_dict)
            elif tool in ("drawing_revert", "revert"):
                result = client.revert(**args_dict)
            elif tool in ("drawing_templates", "template", "templates"):
                result = client.templates(**args_dict)
            elif tool in ("drawing_primitives", "primitives"):
                result = client.primitives(**args_dict)
            elif tool in ("drawing_library", "library"):
                result = client.library(**args_dict)
                result.pop("_base64", None)
            elif tool in ("drawing_compose", "compose"):
                result = client.compose(**args_dict)
            elif tool in ("drawing_present", "present"):
                result = client.present(**args_dict)
            else:
                raise BridgeError(f"Unknown tool or action: '{tool}'", code="UNKNOWN_TOOL", status=400)

        # Output JSON to stdout
        print(json.dumps(result, indent=2, ensure_ascii=False), flush=True)
        sys.exit(0)

    except BridgeError as e:
        sys.stderr.write(f"BridgeError: {e}\n")
        print(json.dumps(e.to_dict(), indent=2, ensure_ascii=False), flush=True)
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": {
                        "code": "EXECUTION_ERROR",
                        "message": str(e),
                        "status": 500,
                    },
                },
                indent=2,
                ensure_ascii=False,
            ),
            flush=True,
        )
        sys.exit(1)


if __name__ == "__main__":
    cli_main()
