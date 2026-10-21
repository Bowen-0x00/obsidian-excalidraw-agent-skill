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
from drawing_workflow import (attach_context, for_context, require_context, reserve_create,
                              requirement_issues, review_path, validate_brief, set_representation_bindings, save_delivery, delivery_evidence)
from drawing_entry import diagram_type, guidance
from operation_schema import validate_operations, operation_examples
from representation_contract import check_representation
from acceptance import decorate, issue_id, triage
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
        self._connection_overrides = (bridge_url, bridge_token, timeout)
        self.bridge_url = ""
        self._refresh_connection()

    def _refresh_connection(self) -> None:
        """Resolve unpinned settings before each request; never retry a write."""
        url_override, token_override, timeout_override = self._connection_overrides
        if any(value is None for value in self._connection_overrides):
            resolved_url, resolved_token, resolved_timeout = resolve_bridge_credentials()
        else:
            resolved_url, resolved_token, resolved_timeout = "", "", 180.0
        url = (url_override if url_override is not None else resolved_url).rstrip("/")
        if url != self.bridge_url:
            # Loopback credentials must never pass through an environment proxy.
            host = urllib.parse.urlsplit(url).hostname
            self.opener = urllib.request.build_opener(
                urllib.request.ProxyHandler({}) if host in ("127.0.0.1", "localhost", "::1") else urllib.request.ProxyHandler()
            )
            self.bridge_url = url
        self.bridge_token = token_override if token_override is not None else resolved_token
        self.timeout = timeout_override if timeout_override is not None else resolved_timeout

    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
    ) -> Any:
        """Send an HTTP request to the local Bridge and return the unpacked response data.

        Raises BridgeError on failures.
        """
        self._refresh_connection()
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

    def _require_native_contract(self) -> None:
        capabilities = self.request("GET", "/v3/capabilities")
        if not capabilities.get("operationFields"):
            raise BridgeError("The running host Bridge lacks strict operation fields. Update the managed Bridge and run Start-Agent-Drawing on the host; reloading only MCP is insufficient.",
                              code="BRIDGE_UPDATE_REQUIRED", status=409)

    def begin(self, request: str, diagram_type: str = "auto", action: str = "prepare",
              brief: dict[str, Any] | None = None, filename: str | None = None,
              foldername: str | None = None, file_path: str | None = None) -> dict[str, Any]:
        """Return actual bundled guidance, host evidence and one explicit task target."""
        if not isinstance(request, str) or not request.strip():
            raise ValueError("request must retain the user's actual drawing request")
        from drawing_entry import diagram_type as classify
        kind = classify(request, diagram_type)
        instructions = guidance(kind, request)
        if action not in ("prepare", "create", "bind"):
            raise ValueError("drawing_begin.action must be prepare/create/bind")
        if brief is not None:
            validate_brief({**brief, "diagram_type": kind})
        if action != "prepare":
            if brief is None:
                raise ValueError("DRAWING_BRIEF_REQUIRED: resolve cited preferences/requirements first; prepare is read-only")
            brief = {**brief, "diagram_type": kind}
            validate_brief(brief)
            if action == "bind" and not file_path:
                raise ValueError("TARGET_REQUIRED: bind requires an explicit vault-relative file_path")
            context = self.context(action, filename, foldername, file_path, brief)
            return {**context, "status": "ready_to_draw", "delivery_ready": False, "guidance": instructions,
                    "operation_examples": operation_examples()}
        discovery = self.context("discover")
        evidence = None
        if file_path:
            context = self.context("bind", file_path=file_path)
            scene = self.read(context["contextToken"], detail="summary")
            record = for_context(context["contextToken"])
            ledger = self.review_settings(context["contextToken"])
            evidence = {"file": scene["file"], "revision": scene["revision"], "canvas": scene,
                        "brief": record["brief"] if record else None, "review_status": ledger.status,
                        "review_rounds": len(ledger.rounds), "last_review": ledger.rounds[-1] if ledger.rounds else None}
        return {"status": "prepared_not_created", "delivery_ready": False, "guidance": instructions,
                "discovery": discovery, "existing_evidence": evidence,
                "unresolved_preferences": ["style", "review", "palette", "background", "font"] if brief is None else [],
                "operation_examples": operation_examples()}

    def contract(self, context_token: str, bindings: dict[str, list[str]]) -> dict[str, Any]:
        """Map logical bodies/signals to saved native IDs, without mutating the canvas."""
        scene = self.read(context_token, detail="full")
        record = require_context(context_token)
        issues = check_representation(scene["elements"], record["brief"].get("representation"), bindings)
        if issues:
            return {"status": "needs_repair", "delivery_ready": False, "file": scene["file"],
                    "revision": scene["revision"], "issues": issues, "bindings_saved": False}
        set_representation_bindings(context_token, bindings)
        return {"status": "mapped_needs_review", "delivery_ready": False, "file": scene["file"],
                "revision": scene["revision"], "issues": [], "bindings_saved": True}

    def context(
        self,
        action: str,
        filename: str | None = None,
        foldername: str | None = None,
        file_path: str | None = None,
        brief: dict[str, Any] | None = None,
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
            validate_brief(brief)
            self._require_native_contract()
            reserve_create(brief)
            payload: dict[str, Any] = {}
            if filename:
                payload["filename"] = filename
            if foldername:
                payload["foldername"] = foldername
            context = self.request("POST", "/v3/canvases/create", payload)
            attach_context(context, brief)
            return {**context, "brief": brief, "delivery_ready": False,
                    "guidance": guidance(diagram_type("\n".join(r["description"] for r in brief["requirements"]), brief.get("diagram_type", "auto")))}

        elif action_lower == "bind":
            if brief is not None:
                validate_brief(brief)
            payload = {}
            if file_path:
                payload["filePath"] = file_path
            context = self.request("POST", "/v3/canvases/bind", payload)
            record = attach_context(context, brief)
            return {**context, "brief": record["brief"] if record else None}

        else:
            raise BridgeError(
                f"Unknown action '{action}'. Must be 'discover', 'create', or 'bind'.",
                code="INVALID_ARGUMENT",
                status=400,
            )

    def review_settings(self, context_token: str, acceptance_level: str | None = None,
                        max_rounds: int | None = None) -> ReviewLedger:
        record = for_context(context_token)
        if record:
            selected = record["brief"]["preferences"]["review"]["value"]
            if acceptance_level is not None and acceptance_level != selected:
                raise ValueError("REVIEW_CHOICE_CONFLICT: keep the review depth selected in this drawing brief")
            return ReviewLedger(context_token, str(review_path(record["file"], record["brief"]["task_id"])),
                                max_rounds=max_rounds, acceptance_level=selected, canvas_key=record["file"])
        return ReviewLedger(context_token, max_rounds=max_rounds, acceptance_level=acceptance_level)

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
                return {"file": context["file"], "revision": context["revision"], "total": 0, "elements": [], "coverage": "ids"}
            revision = pages[0]["revision"]
            if any(page["revision"] != revision for page in pages):
                raise BridgeError("Canvas changed during ID traversal", code="REVISION_CONFLICT", status=409)
            elements = [element for page in pages for element in page["elements"]]
            return {"file": pages[0]["file"], "revision": revision, "total": len(elements), "elements": elements, "coverage": "ids"}
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
                return {"file": page["file"], "revision": revision, "total": page["total"], "elements": elements, "coverage": "complete"}
            if not page["elements"]:
                raise BridgeError("Incomplete element page", code="INVALID_RESPONSE", status=502)
            cursor += len(page["elements"])

    def table(self, context_token: str, base_revision: str, action: str,
              target: str | None = None, options: dict[str, Any] | None = None,
              theme: str | None = None, border: str | None = None, ref: str | None = None) -> dict[str, Any]:
        """Create/style a paired native table; host owns themes, borders and layout.

        This is separate from the legacy create_table grid. Native transactions
        are saved but not atomic across create/theme/width changes.
        """
        require_context(context_token)
        return self.request("POST", "/v3/tables", {
            "contextToken": context_token, "baseRevision": base_revision, "action": action,
            **{key: value for key, value in {"target": target, "options": options,
                "theme": theme, "border": border, "ref": ref}.items() if value is not None},
        })

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
        acceptance_level: str | None = None,
    ) -> dict[str, Any]:
        """Apply a batch of operations to the canvas."""
        operations = validate_operations(operations)
        require_context(context_token)
        self._require_native_contract()
        if acceptance_level is not None:
            self.review_settings(context_token, acceptance_level).save()
        receipt = self.request(
            "POST",
            "/v3/operations/apply",
            {
                "contextToken": context_token,
                "baseRevision": base_revision,
                "operations": operations,
            },
        )
        return {**receipt, "status": "applied_needs_review", "delivery_ready": False}

    def _preview_receipt(self, context_token: str, preview_id: str, revision: str | None = None) -> dict[str, Any]:
        if not re.fullmatch(r"prev_[0-9]+_[0-9a-f]{8}", preview_id):
            raise BridgeError("Invalid preview ID", code="PREVIEW_NOT_FOUND", status=404)
        receipt_path = artifact_directory() / "previews" / f"{preview_id}.json"
        if not receipt_path.exists():
            raise BridgeError("Preview was not produced by this execution layer", code="PREVIEW_NOT_FOUND", status=404)
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        if receipt["contextToken"] != context_token or (revision is not None and receipt["revision"] != revision):
            raise BridgeError("Preview belongs to a different canvas or state", code="STALE_PREVIEW", status=409)
        image = Path(receipt["out_path"])
        if not image.is_file() or hashlib.sha256(image.read_bytes()).hexdigest() != receipt["sha256"]:
            raise BridgeError("Preview artifact changed or is missing", code="PREVIEW_CHANGED", status=409)
        return receipt

    def check(
        self,
        context_token: str,
        expected: list[dict[str, Any]] | None = None,
        scope: str = "all",
        acceptance_level: str | None = None,
        preview_id: str | None = None,
    ) -> dict[str, Any]:
        """Check the complete exact scene; a failed validator is not a successful check."""
        scene = self.read(context_token, detail="full")
        ledger = self.review_settings(context_token, acceptance_level)
        if expected is not None:
            ledger.expected = expected
        ledger.save()
        expected = ledger.expected
        preview = self._preview_receipt(context_token, preview_id, scene["revision"]) if preview_id else None
        validation = self.request("POST", "/v3/scene/validate", {"contextToken": context_token, "scope": "all"})
        if validation["revision"] != scene["revision"]:
            raise BridgeError("Canvas changed between geometry and structural checks", code="REVISION_CONFLICT", status=409)
        diagnostics = run_geometry_diagnostics(scene["elements"], expected=expected, structural_validation=validation,
            acceptance_level=ledger.acceptance_level, output_scale=preview.get("actualScale") if preview else None)
        record = for_context(context_token)
        representation = check_representation(scene["elements"], record["brief"].get("representation"), record.get("representationBindings")) if record else []
        if representation:
            diagnostics["issues"] = decorate([*diagnostics["issues"], *representation], ledger.acceptance_level)
            diagnostics["status"], diagnostics["valid"] = "fail", False
            diagnostics["summary"]["errors"] += len(representation)
            diagnostics["summary"]["blocking"] += len(representation)
        diagnostics["representation"] = {"required": bool(record and record["brief"].get("representation")), "issues": representation}
        diagnostics.update(revision=scene["revision"], contextToken=context_token, coverage="complete", expected=expected or [])
        return diagnostics

    def inspect(
        self, context_token: str, base_revision: str,
        expected: list[dict[str, Any]] | None = None,
        acceptance_level: str | None = None,
    ) -> dict[str, Any]:
        """Check and render one exact revision; visual review remains a separate step."""
        started = time.perf_counter()
        checked = self.check(context_token, expected=expected, acceptance_level=acceptance_level)
        checked_at = time.perf_counter()
        if checked["revision"] != base_revision:
            raise BridgeError("Canvas changed after mutation and before inspection",
                              code="REVISION_CONFLICT", status=409,
                              details={"expected": base_revision, "actual": checked["revision"]})
        preview = self.preview(context_token, base_revision=checked["revision"])
        rendered_at = time.perf_counter()
        checked = self.check(context_token, acceptance_level=acceptance_level, preview_id=preview["previewId"])
        return {"check": checked, "preview": preview,
                "timings": {"checkMs": ((checked_at - started) + (time.perf_counter() - rendered_at)) * 1000,
                            "previewMs": (rendered_at - checked_at) * 1000}}

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
            "ids": ids or [],
        }
        receipts = artifact_directory() / "previews"
        receipts.mkdir(parents=True, exist_ok=True)
        (receipts / f"{preview_id}.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
        return {**metadata, "canvasSummary": res["canvasSummary"], "_base64": b64_str}

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
        acceptance_level: str | None = None,
        visual_checks: dict[str, str] | None = None,
        dispositions: list[dict[str, Any]] | None = None,
        detail_preview_ids: list[str] | None = None,
        requirement_checks: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """Review a registered, current PNG; re-run hard checks rather than trusting model-supplied results."""
        receipt = self._preview_receipt(context_token, preview_id, revision)
        if receipt["scope"] != "all":
            raise BridgeError("Completion requires an all-canvas overview", code="INCOMPLETE_COVERAGE", status=422)
        record = require_context(context_token)
        scene = self.read(context_token, detail="full")
        if scene["revision"] != revision:
            raise BridgeError("Canvas changed after PNG export", code="STALE_PREVIEW", status=409)
        by_id = {element["id"]: element for element in scene["elements"] if not element.get("isDeleted")}
        detail_receipts = {}
        for detail_id in detail_preview_ids or []:
            detail = self._preview_receipt(context_token, detail_id, revision)
            if not detail.get("complete"):
                raise BridgeError("Detail preview has missing resources", code="PREVIEW_INCOMPLETE", status=422)
            detail_receipts[detail_id] = detail
        for decision in dispositions or []:
            evidence = detail_receipts.get(decision.get("preview_id"))
            if evidence:
                ids = decision.get("element_ids", [])
                if evidence["scope"] != "ids" or not set(ids).issubset(evidence.get("ids") or []):
                    raise ValueError("A disposition detail must explicitly include every affected native element ID")
                if any(identity in by_id and by_id[identity].get("type") == "text"
                       and by_id[identity].get("fontSize", 20) * evidence.get("actualScale", 0) < 10 for identity in ids):
                    raise ValueError("Disposition detail text remains too small; export a readable local PNG")
        ledger = self.review_settings(context_token, acceptance_level, max_rounds)
        # Carry prior assertions forward; a review without check_result must not drop them.
        expected = list(ledger.expected)
        for assertion in (check_result or {}).get("expected") or []:
            if assertion not in expected:
                expected.append(assertion)
        fresh_check = self.check(context_token, expected=expected, acceptance_level=ledger.acceptance_level, preview_id=preview_id)
        small_ids = {identity for issue in fresh_check["issues"] if issue["code"] == "SMALL_OUTPUT_TEXT"
                     for identity in issue.get("elementIds", [])}
        covered = {identity for detail in detail_receipts.values() if detail.get("scope") == "ids"
                   for identity in detail.get("ids", []) if identity in by_id
                   and by_id[identity].get("fontSize", 20) * detail.get("actualScale", 0) >= 10}
        if ledger.acceptance_level != "low" and small_ids - covered:
            fresh_check["issues"].append({"code": "READABLE_DETAIL_REQUIRED", "severity": "error",
                "elementIds": sorted(small_ids - covered),
                "message": "Overview has small text; inspect registered readable detail PNGs for every affected label or repair the layout"})
        coverage_issues = requirement_issues(record["brief"]["requirements"], requirement_checks, set(by_id))
        fresh_check["issues"].extend(coverage_issues)
        if coverage_issues:
            fresh_check["status"] = "fail"
        if fresh_check["revision"] != revision:
            raise BridgeError("Canvas changed after PNG export", code="STALE_PREVIEW", status=409)
        ledger = self.review_settings(context_token, ledger.acceptance_level, max_rounds)
        return ledger.record_round(
            revision=revision, preview_id=preview_id, visual_reviewed=visual_reviewed,
            visual_issues=visual_issues, changes_summary=changes_summary,
            check_result=fresh_check, preview_complete=receipt["complete"],
            visual_checks=visual_checks, dispositions=dispositions, detail_preview_ids=detail_preview_ids,
            requirement_checks=requirement_checks,
        )

    def deliver(self, context_token: str, revision: str, preview_id: str) -> dict[str, Any]:
        """Issue delivery evidence only for the current task, full PNG and completed review."""
        record = require_context(context_token)
        receipt = self._preview_receipt(context_token, preview_id, revision)
        scene = self.read(context_token, detail="full")
        ledger = self.review_settings(context_token)
        try:
            last = delivery_evidence(record, scene, receipt, ledger)
        except ValueError as error:
            raise BridgeError(str(error), code=str(error).split(":")[0], status=422) from error
        for detail_id in last.get("detailPreviewIds", []):
            self._preview_receipt(context_token, detail_id, revision)
        ids = {e["id"] for e in scene["elements"] if not e.get("isDeleted")}
        coverage = requirement_issues(record["brief"]["requirements"], last.get("requirementChecks"), ids)
        checked = self.check(context_token, preview_id=preview_id)
        reviewed_issues = {issue_id(i) for i in last["hardIssues"]}
        new_issues = [i for i in checked["issues"] if issue_id(i) not in reviewed_issues and i.get("blocking")]
        representation = check_representation(scene["elements"], record["brief"].get("representation"), record.get("representationBindings"))
        unresolved, _ = triage(last["allIssues"], ledger.acceptance_level, last.get("dispositions"))
        if coverage or new_issues or representation or unresolved or not last["visualReviewed"] or not last["previewComplete"]:
            raise BridgeError("Current task checks no longer support completed delivery", code="DELIVERY_CHECK_FAILED", status=422,
                              details={"issues": [*coverage, *new_issues, *representation, *unresolved]})
        result = {"status": "deliverable", "delivery_ready": True, "task_id": record["brief"]["task_id"],
                  "file": scene["file"], "revision": revision, "previewId": preview_id, "png": receipt["out_path"],
                  "sha256": receipt["sha256"], "reviewRound": last["round"], "acceptanceLevel": ledger.acceptance_level,
                  "rawCheckStatus": checked["status"], "advisories": last.get("advisories", []),
                  "limits": "Current native state and PNG/review evidence verified; user-evidence and visual judgments are Agent attestations, not electrical/scientific proof."}
        save_delivery(context_token, result)
        return result

    def revert(
        self,
        context_token: str,
        transaction_id: str | None = None,
    ) -> dict[str, Any]:
        """Undo the target file's latest transaction, optionally verifying its ID."""
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

    def library(self, action: str, context_token: str | None = None, library: str | None = None, item: str | None = None,
                position: str | dict = "center", scale: float = 1, base_revision: str | None = None,
                offset: int = 0, limit: int = 100, text: str | None = None, detail: str = "summary",
                create_anchor_proxy: bool = True, trusted_local_library: bool = False,
                logical_id: str | None = None, diagram_id: str | None = None, out_path: str | None = None,
                catalog_path: str | None = None) -> dict:
        paths = {"list": "/v3/libraries/list", "catalog": "/v3/libraries/catalog",
                 "query": "/v3/libraries/items/query", "get": "/v3/libraries/items/get",
                 "preview": "/v3/libraries/items/preview", "insert": "/v3/libraries/insert"}
        if action not in paths:
            raise ValueError("Library action must be list/catalog/query/get/preview/insert")
        payload = {"contextToken": context_token}
        if action == "catalog":
            if not catalog_path:
                raise ValueError("An explicit catalog_path returned by library list is required")
            payload["catalogPath"] = catalog_path
        elif action != "list":
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
            if not context_token:
                raise ValueError("Library preview/insertion requires an explicit canvas context_token")
            payload["scale"] = scale
            payload["trustedLocalLibrary"] = trusted_local_library
        if action == "insert":
            require_context(context_token)
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

    def compose(self, context_token: str, base_revision: str, diagram: dict, acceptance_level: str | None = None) -> dict:
        require_context(context_token)
        if acceptance_level is not None:
            self.review_settings(context_token, acceptance_level).save()
        try:
            return compose_diagram(self, context_token, base_revision, diagram)
        except CompositionError as error:
            raise BridgeError(str(error), code=getattr(error.cause, "code", "COMPOSITION_FAILED"),
                              status=getattr(error.cause, "status", 422),
                              details={"phase": error.stage, "appliedStages": error.applied,
                                       "cause": getattr(error.cause, "details", None), "atomic": False}) from error

    def present(self, context_token: str, base_revision: str, presentation: dict) -> dict:
        require_context(context_token)
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
    p_ctx.add_argument("--brief", help="JSON drawing brief with cited resolved preferences and user requirements")
    p_ctx.add_argument("--brief-file", help="Path to a JSON drawing brief")

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
    p_apply.add_argument("--acceptance-level", choices=["low", "medium", "high"])

    # 6. check
    p_check = subparsers.add_parser("check", help="Run geometry and structural checks")
    p_check.add_argument("--context-token", required=True)
    p_check.add_argument("--expected", help="JSON string of expected semantic assertions")
    p_check.add_argument("--expected-file", help="Path to JSON file of expected semantic assertions")
    p_check.add_argument("--scope", default="all")
    p_check.add_argument("--acceptance-level", choices=["low", "medium", "high"])
    p_check.add_argument("--preview-id", help="Current registered preview for output readability checks")

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
    p_rev.add_argument("--acceptance-level", choices=["low", "medium", "high"])
    p_rev.add_argument("--visual-checks", help="JSON object of recorded visual checklist outcomes")
    p_rev.add_argument("--dispositions", help="JSON array of per-issue PNG-based geometric adjudications")
    p_rev.add_argument("--detail-preview-ids", help="Comma-separated current registered detail previews actually viewed")
    p_rev.add_argument("--requirement-checks", help="JSON per-requirement outcomes, current element_ids and specific evidence")

    # 9. revert
    p_revt = subparsers.add_parser("revert", help="Undo last canvas transaction")
    p_revt.add_argument("--context-token", required=True)
    p_revt.add_argument("--transaction-id")

    # 10. json
    p_json = subparsers.add_parser("json", help="Execute single-payload JSON request or read from stdin")
    p_json.add_argument("--request", help="JSON request payload string")

    for command in ("begin", "contract", "deliver", "template", "primitives", "library", "compose", "present"):
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
                brief=json.loads(Path(args.brief_file).read_text(encoding="utf-8")) if args.brief_file else json.loads(args.brief) if args.brief else None,
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
                acceptance_level=args.acceptance_level,
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
                acceptance_level=args.acceptance_level,
                preview_id=args.preview_id,
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
                acceptance_level=args.acceptance_level,
                visual_checks=json.loads(args.visual_checks) if args.visual_checks else None,
                dispositions=json.loads(args.dispositions) if args.dispositions else None,
                detail_preview_ids=args.detail_preview_ids.split(",") if args.detail_preview_ids else None,
                requirement_checks=json.loads(args.requirement_checks) if args.requirement_checks else None,
            )

        elif sub == "revert":
            result = client.revert(
                context_token=args.context_token,
                transaction_id=args.transaction_id,
            )

        elif sub in ("begin", "contract", "deliver", "template", "primitives", "library", "compose", "present"):
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

            if tool in ("drawing_begin", "begin"):
                result = client.begin(**args_dict)
            elif tool in ("drawing_contract", "contract"):
                result = client.contract(**args_dict)
            elif tool in ("drawing_deliver", "deliver"):
                result = client.deliver(**args_dict)
            elif tool in ("drawing_context", "context"):
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
