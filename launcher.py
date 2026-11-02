"""Portable entry point for MCP serving and first-time Obsidian connection."""
from __future__ import annotations

import argparse
import json
import runpy
import sys
from pathlib import Path
from typing import Any, Literal

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "runtime"))

from setup_connection import (connect_vault, discover_vaults, list_connections,
                              select_connection, setup_status, start_bridge)


def serve() -> None:
    import server
    from drawing_client import DrawingClient

    @server.mcp.tool()
    def drawing_setup(action: Literal["status", "connect", "start"] = "status",
                      vault_path: str | None = None, vault_name: str | None = None,
                      port: int | None = None, open_uri: bool = True,
                      obsidian_config_dir: str = ".obsidian") -> dict[str, Any]:
        """Report connection status, or deploy/start the local Obsidian drawing bundle.

        Status includes mode=remote when rendering through a host SSH tunnel.
        Remote clients cannot connect/start a vault; do that on the graphical host.
        Local status discovers a unique self-published Bridge; ambiguous targets
        require explicit CLI vaults/use selection. First deployment is host-local.
        Never returns a bearer token or rewrites plugin trust permissions.
        """
        if action == "status":
            return setup_status()
        if action == "connect":
            result = connect_vault(vault_path, vault_name, port, open_uri, obsidian_config_dir)
        else:
            result = start_bridge(open_uri)
        server.client = DrawingClient()
        return result

    server.mcp.run("stdio")


def smoke(filename: str, font_family: str) -> dict[str, Any]:
    from drawing_client import DrawingClient

    client = DrawingClient()
    fonts = client.context("discover")["capabilities"]["fonts"]["registered"]
    if font_family not in fonts:
        raise ValueError("Use --font with an exact family returned by discovery/fonts")
    brief = {
        "task_id": "installation-smoke:" + filename,
        "preferences": {
            key: {"value": value, "source": "user",
                  "evidence": "Explicit invocation of the documented fixed installation smoke with --font; not a general artwork request"}
            for key, value in {"style": "professional", "review": "medium",
                               "palette": "semantic diagnostic blue/green/orange", "background": "white",
                               "font": font_family}.items()
        },
        "requirements": [
            {"id": "branches", "description": "Keep approved and rejected branches with complete Chinese labels"},
            {"id": "native", "description": "Keep native editable shapes, text and directed bound arrows"},
        ],
    }
    context = client.context("create", filename=filename, foldername="Agent-Diagrams", brief=brief)
    token = context["contextToken"]
    initial = client.read(token)
    diagram = {"diagramId": "installation-smoke", "kind": "flowchart", "style": {"profile": "professional", "fontFamily": font_family},
               "nodes": [{"id": "request", "shape": "rectangle", "label": "提交申请", "variant": "primary"},
                         {"id": "review", "shape": "diamond", "label": "审核"},
                         {"id": "approve", "shape": "rectangle", "label": "发放凭据", "variant": "success"},
                         {"id": "reject", "shape": "rectangle", "label": "说明拒绝原因", "variant": "warning"},
                         {"id": "end", "shape": "ellipse", "label": "结束"}],
               "edges": [{"id": "to-review", "from": "request", "to": "review"},
                         {"id": "yes", "from": "review", "to": "approve", "fromPort": "left", "label": "通过"},
                         {"id": "no", "from": "review", "to": "reject", "fromPort": "right", "label": "未通过"},
                         {"id": "approved-end", "from": "approve", "to": "end", "toPort": "left"},
                         {"id": "rejected-end", "from": "reject", "to": "end", "toPort": "right"}]}
    plan = client.plan(token, diagram)
    applied = client.apply(token, plan["baseRevision"], plan["operations"])
    expected = [{"type": "label_equals", "id": node["id"], "text": node["label"]} for node in diagram["nodes"]]
    expected += [{"type": "edge_label", "from": "review", "to": edge["to"], "text": edge["label"]}
                 for edge in diagram["edges"] if edge.get("label")]
    check = client.check(token, expected=expected)
    preview = client.preview(token, base_revision=check["revision"])
    preview.pop("_base64", None)
    return {"file": context["file"], "contextToken": token,
            "initial": initial, "transactionId": applied.get("transactionId"),
            "check": check, "preview": preview, "visual_reviewed": False,
            "next": "Actually inspect the PNG, then use drawing_review for the current revision. This smoke does not pretend to perform visual review."}


def _identity(value: dict[str, Any]) -> str:
    name, identifier = value.get("name"), value.get("id")
    return f"{name} ({identifier})" if name and identifier else str(name or identifier or "unknown")


def _print_status(result: dict[str, Any]) -> None:
    live = result.get("status") or {}
    host = result.get("host") or live.get("host") or {}
    vault = result.get("vault") or live.get("vault") or {}
    connected = result.get("connected") is True
    code = result.get("code") or ("READY" if connected else "CONNECTION_FAILED")
    print("Connection: {} ({})".format(code, "connected" if connected else "not connected"))
    print("Mode: {} | rendering: {}".format(result.get("mode", "local"), result.get("rendering_location", "unknown")))
    runtime = result.get("runtime") or {}
    print("Runtime: {} | {}".format(runtime.get("version", "unknown"), runtime.get("path", "unknown")))
    print("Host: " + _identity(host))
    print("Vault: " + (_identity(vault) if vault else result.get("vault_name") or "unknown"))
    path = vault.get("path") or result.get("host_vault_path") or result.get("vault_path")
    if path:
        print("Host vault path: " + str(path))
    if result.get("remote_host"):
        print("SSH peer: " + str(result["remote_host"]))
    print("Bridge URL: " + str(result.get("bridge_url") or "not configured"))
    print("Bridge: {} | plugin: {}".format(live.get("version") or live.get("bridgeVersion") or "unknown",
                                           result.get("plugin_version") or live.get("pluginVersion") or "unknown"))
    readiness = result.get("readiness") or ("ready" if result.get("ready", live.get("ready")) else "not ready")
    print("Canvas readiness: " + str(readiness))
    if live.get("file"):
        print("Current canvas: {} | revision: {}".format(live["file"], live.get("revision", "unknown")))
    canvases = result.get("open_canvases", live.get("openCanvases", []))
    if canvases:
        print("Open canvases:")
        for canvas in canvases:
            print("  - " + str(canvas.get("file", "unknown")))
    else:
        print("Open canvases: none reported")
    engines = result.get("engines", live.get("engines"))
    if isinstance(engines, list):
        print("Engines: " + (", ".join(str(engine) for engine in engines) or "none reported"))
    elif engines is not None:
        print("Engines: " + json.dumps(engines, ensure_ascii=False))
    else:
        print("Engines: unknown")
    print("Client state: " + str(result.get("state_directory") or "unknown"))
    print("Connection config: " + str(result.get("config_path") or "not selected"))
    if result.get("selected_connection_id"):
        print("Selected profile: " + str(result["selected_connection_id"]))
        profile = next((item for item in result.get("connections", [])
                        if item.get("id") == result["selected_connection_id"]), {})
        print("Effective profile: " + str(profile.get("config_path") or "unknown"))
    if result.get("reason"):
        print("Reason: " + str(result["reason"]))
    if result.get("remediation"):
        print("Next: " + str(result["remediation"]))
    if code == "NO_CANVAS":
        print("The authenticated Bridge is connected; create or explicitly bind a canvas before drawing.")
    if result.get("needs_vault_selection"):
        print("Choose a target with vaults, then use ID_OR_UNIQUE_NAME; no target was guessed.")


def _vault_catalog() -> dict[str, Any]:
    result = list_connections()
    try:
        result["available_vaults"] = discover_vaults()
    except Exception as error:
        result["available_vaults"] = []
        result["catalog_error"] = {"code": getattr(error, "code", "CATALOG_UNAVAILABLE"),
                                   "message": str(error)}
    return result


def _print_vaults(result: dict[str, Any]) -> None:
    print("Known connection profiles (local discovery / paired remote):")
    connections = result.get("connections", [])
    for connection in connections:
        identifier = connection.get("id")
        name = connection.get("name") or "unnamed"
        selected = connection.get("selected") or identifier == result.get("selected_connection_id")
        marker = "*" if selected else "-"
        print("  {} {}  {}  [{}]".format(marker, identifier or "unknown", name, connection.get("mode", "local")))
        if connection.get("host"):
            print("      host: " + _identity(connection["host"]))
        if connection.get("vault"):
            print("      vault: " + _identity(connection["vault"]))
        if connection.get("code"):
            print("      status: " + str(connection["code"]))
    if not connections:
        print("  none")
    print("Registered vault catalog (registration does not imply running or paired):")
    for vault in result.get("available_vaults", []):
        print("  - " + _identity(vault))
        if vault.get("path"):
            print("      host path: " + str(vault["path"]))
        flags = ["{}={}".format(key, str(vault[key]).lower())
                 for key in ("pluginEnabled", "running", "selected") if key in vault]
        if flags:
            print("      " + ", ".join(flags))
    if not result.get("available_vaults"):
        print("  none available")
    if result.get("catalog_error"):
        error = result["catalog_error"]
        print("Catalog unavailable: {}: {}".format(error["code"], error["message"]))
    print("Select an available connection with: use ID_OR_UNIQUE_NAME")
    print("Catalog-only remote vaults must first be paired on the graphical host; do not use a host path remotely.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    commands.add_parser("serve", help="Serve the bundled drawing MCP tools over stdio")
    for name, help_text in (("status", "Show read-only connection, host and canvas status"),
                            ("doctor", "Require a reachable authenticated Bridge; NO_CANVAS is connected"),
                            ("vaults", "List known profiles and the host registered-vault catalog")):
        command = commands.add_parser(name, help=help_text)
        command.add_argument("--json", action="store_true", help="Emit redacted machine-readable JSON")
    use = commands.add_parser("use", help="Select a discovered local or paired remote connection by ID or unique name")
    use.add_argument("selector", help="Connection ID or unique name, not a remote host filesystem path")
    use.add_argument("--json", action="store_true", help="Emit redacted machine-readable JSON")
    connect = commands.add_parser("connect", help="Deploy bundled scripts and connect a selected vault")
    connect.add_argument("--vault", dest="vault_path")
    connect.add_argument("--vault-name")
    connect.add_argument("--port", type=int)
    connect.add_argument("--obsidian-config-dir", default=".obsidian")
    connect.add_argument("--no-open", action="store_true")
    start = commands.add_parser("start", help="Start the previously connected Bridge")
    start.add_argument("--no-open", action="store_true")
    trial = commands.add_parser("smoke", help="Create a real native diagram and PNG without fabricated visual approval")
    trial.add_argument("--filename", default="Drawing-Installation-Smoke")
    trial.add_argument("--font", required=True, help="Exact host-discovered font for this fixed diagnostic drawing")
    cli = commands.add_parser("cli", help="Run the full drawing CLI; options after -- are forwarded")
    cli.add_argument("arguments", nargs=argparse.REMAINDER)
    dsl = commands.add_parser("dsl", help="Render or incrementally update YAML/JSON scenes; options after -- are forwarded")
    dsl.add_argument("arguments", nargs=argparse.REMAINDER)
    cdp = commands.add_parser("cdp", help="Opt-in fixed read-only CDP diagnostics; no input/eval/write commands")
    cdp.add_argument("arguments", nargs=argparse.REMAINDER)
    metadata = commands.add_parser("library-maintain", help="Inspect local library files or apply reviewed description-only edits")
    metadata.add_argument("arguments", nargs=argparse.REMAINDER)
    for name in ("remote-deploy", "remote-tunnel"):
        remote = commands.add_parser(name, help="Install a headless client or keep its SSH reverse tunnel open")
        remote.add_argument("--host", required=True, help="Existing SSH alias on this graphical host")
        remote.add_argument("--remote-port", type=int)
    args = parser.parse_args()
    if args.action == "serve":
        serve()
        return 0
    if args.action == "dsl":
        from scene_dsl.cli import main as scene_main
        forwarded = args.arguments[1:] if args.arguments[:1] == ["--"] else args.arguments
        sys.argv = ["launcher.py dsl", *forwarded]
        return scene_main()
    if args.action == "cdp":
        from cdp_readonly import main as cdp_main
        forwarded = args.arguments[1:] if args.arguments[:1] == ["--"] else args.arguments
        sys.argv = ["launcher.py cdp", *forwarded]
        return cdp_main()
    if args.action == "library-maintain":
        forwarded = args.arguments[1:] if args.arguments[:1] == ["--"] else args.arguments
        sys.argv = [str(ROOT / "runtime/library_metadata.py"), *forwarded]
        runpy.run_path(str(ROOT / "runtime/library_metadata.py"), run_name="__main__")
        return 0
    if args.action == "cli":
        forwarded = args.arguments[1:] if args.arguments[:1] == ["--"] else args.arguments
        sys.argv = [str(ROOT / "runtime/drawing_client.py"), *forwarded]
        runpy.run_path(str(ROOT / "runtime/drawing_client.py"), run_name="__main__")
        return 0
    try:
        if args.action in ("remote-deploy", "remote-tunnel"):
            from remote_control import deploy_remote, tunnel_command
            if args.action == "remote-tunnel":
                import subprocess
                return subprocess.run(tunnel_command(args.host, args.remote_port)).returncode
            result = deploy_remote(args.host, args.remote_port)
        elif args.action == "connect":
            result = connect_vault(args.vault_path, args.vault_name, args.port, not args.no_open, args.obsidian_config_dir)
        elif args.action == "start":
            result = start_bridge(not args.no_open)
        elif args.action == "smoke":
            result = smoke(args.filename, args.font)
        elif args.action == "vaults":
            result = _vault_catalog()
        elif args.action == "use":
            result = select_connection(args.selector)
        else:
            result = setup_status()
        if args.action in ("status", "doctor", "vaults", "use") and not args.json:
            (_print_vaults if args.action == "vaults" else _print_status)(result)
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.action == "vaults" and result.get("catalog_error"):
            return 1
        if args.action == "doctor":
            return 0 if result["connected"] else 1
        if args.action == "smoke":
            return 0 if result["check"]["status"] == "pass" and result["preview"]["complete"] else 1
        return 0
    except Exception as error:
        failure = {"ok": False, "error": {"code": getattr(error, "code", "SETUP_ERROR"),
                                           "message": str(error)}}
        if args.action in ("status", "doctor", "vaults", "use") and not args.json:
            print("{}: {}".format(failure["error"]["code"], error), file=sys.stderr)
        else:
            print(json.dumps(failure, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
