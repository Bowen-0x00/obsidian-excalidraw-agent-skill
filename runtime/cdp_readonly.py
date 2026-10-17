"""Opt-in CDP observations, never a general CDP/JavaScript execution tool.

Only the two fixed, V8 side-effect-checked queries below and Runtime.enable
are sent. No input, navigation, debugger pause, save, export or mutation API.
The unrestricted Electron debugging endpoint itself is NOT read-only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from runtime_config import state_directory

CONFIG_NAME = "cdp-readonly.json"
MAX_BYTES = 8 * 1024 * 1024


class DiagnosticError(ValueError):
    def __init__(self, code: str, message: str, **details: Any):
        super().__init__(message)
        self.code, self.details = code, details


def endpoint_url(value: str) -> str:
    parsed = urlsplit(value)
    try:
        port = parsed.port
    except ValueError as error:
        raise DiagnosticError(
            "CDP_ENDPOINT_INVALID", "Specify a numeric loopback port"
        ) from error
    if (
        parsed.scheme != "http"
        or parsed.hostname not in ("127.0.0.1", "::1")
        or port is None
        or not 1024 <= port <= 65535
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in ("", "/")
    ):
        raise DiagnosticError(
            "CDP_ENDPOINT_INVALID",
            "Use http://127.0.0.1:PORT (or [::1]); no credentials, path or public host",
        )
    host = "[::1]" if parsed.hostname == "::1" else "127.0.0.1"
    return f"http://{host}:{port}"


def vault_identity(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise DiagnosticError(
            "CDP_VAULT_REQUIRED", "Pin the exact absolute HOST vault path"
        )
    path = value.replace("\\", "/").rstrip("/") or "/"
    if not (
        path.startswith("/") or re.match(r"^[A-Za-z]:/", path)
    ) or ".." in path.split("/"):
        raise DiagnosticError(
            "CDP_VAULT_REQUIRED", "Pin an absolute host path without parent traversal"
        )
    return path.casefold() if re.match(r"^[A-Za-z]:/", path) else path


def drawing_path(value: str) -> str:
    if not isinstance(value, str) or not value:
        raise DiagnosticError(
            "CDP_FILE_REQUIRED",
            "Inspect requires an explicit already-open drawing path",
        )
    parts = value.split("/")
    if (
        value.startswith("/")
        or "\\" in value
        or ":" in value
        or any(p in ("", ".", "..") for p in parts)
        or not value.endswith((".excalidraw.md", ".excalidraw"))
    ):
        raise DiagnosticError(
            "CDP_FILE_INVALID", "Use a vault-relative Excalidraw path without traversal"
        )
    return value


def config_path() -> Path:
    return state_directory() / CONFIG_NAME


def _load() -> dict[str, Any]:
    path = config_path()
    if not path.exists():
        return {"enabled": False}
    config = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(config, dict) or type(config.get("enabled")) is not bool:
        raise DiagnosticError(
            "CDP_CONFIG_INVALID",
            "Diagnostic config must contain a boolean enabled flag",
        )
    if config["enabled"]:
        endpoint_url(config.get("endpoint", ""))
        vault_identity(config.get("vault_path", ""))
    return config


def status() -> dict[str, Any]:
    """Local opt-in state only: status never probes a debugging endpoint."""
    config = _load()
    return {
        "enabled": config["enabled"],
        "mode": "read-only",
        "networkProbed": False,
        "endpoint": config.get("endpoint") if config["enabled"] else None,
        "vault_path": config.get("vault_path") if config["enabled"] else None,
        "target_id": config.get("target_id") if config["enabled"] else None,
        "config_path": str(config_path()),
        "enable": "User opts in with launcher.py cdp -- enable --endpoint ... --vault-path ...; no MCP enable action",
    }


def configure(
    enabled: bool,
    endpoint: str | None = None,
    vault_path: str | None = None,
    target_id: str | None = None,
) -> dict[str, Any]:
    """Explicit CLI opt-in; writes only client-private config, never vault/profile."""
    config = {"enabled": False}
    if enabled:
        if not endpoint or not vault_path:
            raise DiagnosticError(
                "CDP_CONFIG_REQUIRED", "Enable needs endpoint and exact host vault path"
            )
        endpoint = endpoint_url(endpoint)
        vault_identity(vault_path)
        if target_id is not None and (not target_id or len(target_id) > 200):
            raise DiagnosticError(
                "CDP_TARGET_INVALID", "Use a target ID from the selected debugger"
            )
        config = {
            "enabled": True,
            "endpoint": endpoint,
            "vault_path": vault_path,
            "target_id": target_id,
        }
    path = config_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
        json.dump(config, stream, ensure_ascii=False, indent=2)
    os.chmod(temporary, 0o600)
    temporary.replace(path)
    return status()


_IDENTITY = "({vaultPath:app.vault.adapter.basePath,vaultName:app.vault.getName()})"
# Data-only arguments are JSON-encoded, never interpolated as JavaScript source.
_COLLECTOR = r"""(args => {
    const fail = code => ({error: code});
    const canonical = value => {
        let p = String(value).replace(/\\/g, '/').replace(/\/+$/, '') || '/';
        return /^[A-Za-z]:\//.test(p) ? p.toLowerCase() : p;
    };
    if (canonical(app.vault.adapter.basePath) !== args.vault) return fail('CDP_VAULT_MISMATCH');
    const leaves = app.workspace.getLeavesOfType('excalidraw').filter(l => l.view.file?.path === args.file);
    if (!leaves.length) return fail('CDP_FILE_NOT_OPEN');
    if (leaves.length !== 1) return fail('CDP_VIEW_AMBIGUOUS');
    const v = leaves[0].view, api = v.excalidrawAPI;
    if (!api || !v._loaded) return fail('CDP_VIEW_NOT_READY');
    const elements = api.getSceneElements();
    const identity = list => list.map(e => [e.id, e.version, e.versionNonce, e.updated]);
    const first = identity(elements);
    const text = value => typeof value === 'string' ? value.slice(0, 240) : null;
    const number = value => typeof value === 'number' && Number.isFinite(value) ? value : null;
    const binding = b => b ? {elementId:b.elementId,mode:b.mode,fixedPoint:b.fixedPoint ?? null} : null;
    const ids = args.ids ? new Set(args.ids) : null;
    const matches = elements.filter(e => !ids || ids.has(e.id));
    const page = matches.slice(args.offset, args.offset + args.limit).map(e => {
        const cd = e.customData || {}, t = cd.table || {};
        return {
            id:e.id,type:e.type,order:elements.indexOf(e),x:e.x,y:e.y,width:e.width,height:e.height,angle:e.angle,
            version:e.version,versionNonce:e.versionNonce,locked:!!e.locked,opacity:e.opacity,
            strokeColor:e.strokeColor,backgroundColor:e.backgroundColor,fillStyle:e.fillStyle,
            strokeWidth:e.strokeWidth,strokeStyle:e.strokeStyle,roughness:e.roughness,roundness:e.roundness ?? null,
            text:text(e.text),originalText:text(e.originalText),textLength:typeof e.text==='string'?e.text.length:null,
            originalTextLength:typeof e.originalText==='string'?e.originalText.length:null,
            textTruncated:typeof e.text==='string'&&e.text.length>240,sourceTruncated:typeof e.originalText==='string'&&e.originalText.length>240,
            fontFamily:e.fontFamily ?? null,fontSize:e.fontSize ?? null,lineHeight:e.lineHeight ?? null,
            bold:cd.bold === true,fontWeight:typeof cd.fontWeight==='number'||typeof cd.fontWeight==='string'?cd.fontWeight:null,
            textAlign:e.textAlign ?? null,verticalAlign:e.verticalAlign ?? null,
            containerId:e.containerId ?? null,groupIds:e.groupIds || [],frameId:e.frameId ?? null,
            boundElements:e.boundElements || [],startBinding:binding(e.startBinding),endBinding:binding(e.endBinding),
            pointCount:e.points?.length ?? 0,points:e.points?.length<=100?e.points:null,
            fileId:e.fileId ?? null,imageStatus:e.status ?? null,crop:e.crop ?? null,
            customDataKeys:Object.keys(cd).slice(0,40),
            table:cd.table?{schemaVersion:t.schemaVersion,role:t.role,root:t.root,rowId:t.rowId,colId:t.colId,row:t.row,col:t.col,
                rowNum:t.rowNum,colNum:t.colNum,padding:t.padding,overflow:t.overflow,heightMode:t.heightMode,
                columnWidths:t.columnWidths,theme:t.appearance?.theme,border:t.appearance?.border}:null
        };
    });
    const state = api.getAppState();
    const files = api.getFiles();
    const rect = v.containerEl.getBoundingClientRect();
    const viewport = {x:rect.x,y:rect.y,width:rect.width,height:rect.height,devicePixelRatio:window.devicePixelRatio,
        zoom:number(state.zoom?.value),scrollX:number(state.scrollX),scrollY:number(state.scrollY),
        theme:state.theme,viewBackgroundColor:state.viewBackgroundColor};
    const canvases = [...v.containerEl.querySelectorAll('canvas')].slice(0,8).map(c =>
        ({width:c.width,height:c.height,clientWidth:c.clientWidth,clientHeight:c.clientHeight}));
    const resources = page.filter(e=>e.type==='image').map(e=>
        ({elementId:e.id,fileId:e.fileId,status:e.status,fileRegistered:!!files[e.fileId]}));
    const last = identity(api.getSceneElements());
    if (JSON.stringify(first)!==JSON.stringify(last) || v.file?.path!==args.file) return fail('CDP_SCENE_CHANGED');
    return {
        vault:{path:app.vault.adapter.basePath,name:app.vault.getName()},file:args.file,
        sceneIdentity:first,sceneCount:elements.length,matched:matches.length,offset:args.offset,
        returned:page.length,truncated:args.offset+page.length<matches.length,
        coverage:ids?'ids':(args.offset===0&&page.length===matches.length?'complete':'page'),elements:page,
        viewport,canvases,resources,
        renderer:{fontSetStatus:document.fonts.status,registeredImageFiles:Object.keys(files).length,
            textEditorOpen:!!v.containerEl.querySelector('textarea.excalidraw-wysiwyg'),
            embeddedFrames:v.containerEl.querySelectorAll('iframe').length,
            nativeTableAvailable:typeof v.tableManager?.stage==='function',
            focused:document.hasFocus()},
        consistency:'Synchronous scene identity checked before/after; not a Bridge revision or a pixel/glyph proof'
    };
})"""


def _read_json(url: str) -> Any:
    # No redirect may turn a loopback opt-in into an external request.
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    with opener.open(url, timeout=5) as response:
        raw = response.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise DiagnosticError(
            "CDP_RESPONSE_TOO_LARGE", "Debugger discovery response exceeds limit"
        )
    return json.loads(raw)


def _target(config: dict[str, Any]) -> tuple[dict, str]:
    endpoint = endpoint_url(config["endpoint"])
    pages = _read_json(endpoint + "/json/list")
    if not isinstance(pages, list):
        raise DiagnosticError(
            "CDP_DISCOVERY_INVALID", "Debugger did not return a target list"
        )
    candidates = [
        p
        for p in pages
        if isinstance(p, dict)
        and p.get("type") == "page"
        and p.get("url", "").startswith("app://obsidian.md/")
        and (not config.get("target_id") or p.get("id") == config["target_id"])
    ]
    if len(candidates) != 1:
        raise DiagnosticError(
            "CDP_TARGET_REQUIRED",
            "Select one Obsidian renderer target ID; no focus-based selection",
            target_ids=[p.get("id") for p in candidates],
        )
    target = candidates[0]
    ws = urlsplit(target.get("webSocketDebuggerUrl", ""))
    base = urlsplit(endpoint)
    try:
        valid = (
            ws.scheme == "ws"
            and ws.hostname == base.hostname
            and ws.port == base.port
            and ws.username is None
            and ws.password is None
            and not ws.query
            and not ws.fragment
            and ws.path.startswith("/devtools/page/")
        )
    except ValueError:
        valid = False
    if not valid:
        raise DiagnosticError(
            "CDP_TARGET_INVALID",
            "Target WebSocket must stay on the explicitly enabled loopback endpoint",
        )
    return target, target["webSocketDebuggerUrl"]


class _Session:
    """The narrow transport accepts only known, guarded observations."""

    def __init__(self, socket, snapshot_args: dict | None = None):
        self.socket, self.sequence = socket, 0
        self.events = {"consoleErrors": 0, "exceptions": 0}
        self.snapshot_expression = (
            (_COLLECTOR + "(" + json.dumps(snapshot_args, ensure_ascii=True) + ")")
            if snapshot_args is not None
            else None
        )

    def request(self, method: str, params: dict | None = None) -> dict:
        params = params or {}
        expression = params.get("expression", "")
        fixed = expression == _IDENTITY or (
            self.snapshot_expression is not None
            and expression == self.snapshot_expression
        )
        if not (method == "Runtime.enable" and not params) and not (
            method == "Runtime.evaluate"
            and fixed
            and params.get("throwOnSideEffect") is True
            and params.get("returnByValue") is True
            and params.get("disableBreaks") is True
            and params.get("silent") is True
            and params.get("timeout") == 3000
            and set(params)
            == {
                "expression",
                "throwOnSideEffect",
                "returnByValue",
                "timeout",
                "disableBreaks",
                "silent",
            }
        ):
            raise DiagnosticError(
                "CDP_OPERATION_FORBIDDEN",
                "Only fixed side-effect-checked observations are permitted",
            )
        self.sequence += 1
        self.socket.send(
            json.dumps({"id": self.sequence, "method": method, "params": params})
        )
        deadline = time.monotonic() + 8
        while time.monotonic() < deadline:
            packet = json.loads(
                self.socket.recv(timeout=max(0.01, deadline - time.monotonic()))
            )
            if packet.get("method") == "Runtime.exceptionThrown":
                self.events["exceptions"] += 1
            elif (
                packet.get("method") == "Runtime.consoleAPICalled"
                and packet.get("params", {}).get("type") == "error"
            ):
                self.events["consoleErrors"] += 1
            if packet.get("id") != self.sequence:
                continue
            if "error" in packet:
                raise DiagnosticError(
                    "CDP_PROTOCOL_ERROR",
                    "Debugger rejected the guarded read; no unguarded fallback",
                )
            result = packet.get("result", {})
            if "exceptionDetails" in result:
                raise DiagnosticError(
                    "CDP_READ_REJECTED",
                    "Read threw or V8 could not rule out side effects; do not retry without the guard",
                )
            return result
        raise DiagnosticError(
            "CDP_TIMEOUT",
            "Diagnostic query timed out; no write or automatic restart attempted",
        )

    def evaluate(self, expression: str) -> Any:
        return (
            self.request(
                "Runtime.evaluate",
                {
                    "expression": expression,
                    "throwOnSideEffect": True,
                    "returnByValue": True,
                    "timeout": 3000,
                    "disableBreaks": True,
                    "silent": True,
                },
            )
            .get("result", {})
            .get("value")
        )


def inspect(
    file_path: str, ids: list[str] | None = None, offset: int = 0, limit: int = 100
) -> dict[str, Any]:
    config = _load()
    if not config["enabled"]:
        raise DiagnosticError(
            "CDP_DISABLED",
            "Read-only CDP is off. Ask the user before enabling it; normal Bridge/PNG remain available",
        )
    file_path = drawing_path(file_path)
    if (
        type(offset) is not int
        or offset < 0
        or type(limit) is not int
        or not 1 <= limit <= 200
    ):
        raise DiagnosticError(
            "CDP_PAGE_INVALID", "offset >= 0 and 1 <= limit <= 200 are required"
        )
    if ids is not None and (
        not isinstance(ids, list)
        or not 1 <= len(ids) <= 100
        or any(not isinstance(i, str) or not i or len(i) > 200 for i in ids)
    ):
        raise DiagnosticError(
            "CDP_IDS_INVALID", "ids must contain 1–100 actual element IDs"
        )
    target, url = _target(config)
    from websockets.sync.client import connect

    with connect(
        url,
        proxy=None,
        compression=None,
        open_timeout=5,
        close_timeout=2,
        max_size=MAX_BYTES,
    ) as socket:
        args = {
            "vault": vault_identity(config["vault_path"]),
            "file": file_path,
            "ids": ids,
            "offset": offset,
            "limit": limit,
        }
        session = _Session(socket, args)
        identity = session.evaluate(_IDENTITY)
        if not isinstance(identity, dict) or vault_identity(
            identity.get("vaultPath", "")
        ) != vault_identity(config["vault_path"]):
            raise DiagnosticError(
                "CDP_VAULT_MISMATCH",
                "Connected renderer is not the user-pinned vault; no scene was read",
            )
        session.request("Runtime.enable")
        result = session.evaluate(session.snapshot_expression)
        if not isinstance(result, dict):
            raise DiagnosticError("CDP_READ_INVALID", "Inspector returned no snapshot")
        if result.get("error"):
            raise DiagnosticError(
                result["error"],
                "The requested drawing must already be uniquely open and unchanged; diagnostics never open/select it",
            )
        identity_bytes = json.dumps(
            result.pop("sceneIdentity"), separators=(",", ":")
        ).encode()
        return {
            "mode": "read-only",
            "targetId": target["id"],
            "sceneFingerprint": hashlib.sha256(identity_bytes).hexdigest(),
            **result,
            "runtimeEventCounts": {
                **session.events,
                "scope": "Renderer-wide cached/new events during attachment; messages/arguments withheld, not file-attributed",
            },
            "limits": [
                "No screenshot/export, input, navigation, plugin reload, save, write or arbitrary JavaScript",
                "Registration/resource presence does not prove correct glyphs, decode or actual pixels",
                "Return to current Bridge read/revision and user-authorized apply for fine-tuning; still inspect actual PNG",
            ],
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    commands.add_parser("status")
    enable = commands.add_parser(
        "enable", help="User opts in to read-only diagnostics for one host vault"
    )
    enable.add_argument("--endpoint", required=True)
    enable.add_argument("--vault-path", required=True)
    enable.add_argument("--target-id")
    commands.add_parser(
        "disable", help="Disable before any future diagnostic connection"
    )
    observe = commands.add_parser("inspect")
    observe.add_argument("--file", required=True)
    observe.add_argument("--ids", nargs="+")
    observe.add_argument("--offset", type=int, default=0)
    observe.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()
    try:
        if args.action == "enable":
            result = configure(True, args.endpoint, args.vault_path, args.target_id)
        elif args.action == "disable":
            result = configure(False)
        elif args.action == "status":
            result = status()
        else:
            result = inspect(args.file, args.ids, args.offset, args.limit)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as error:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": {
                        "code": getattr(error, "code", "CDP_UNAVAILABLE"),
                        "message": str(error),
                        "details": getattr(error, "details", {}),
                    },
                },
                ensure_ascii=False,
            ),
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
