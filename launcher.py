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

from setup_connection import connect_vault, setup_status, start_bridge


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
        Local first use discovers vaults then connects the intended vault_path.
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


def smoke(filename: str) -> dict[str, Any]:
    from drawing_client import DrawingClient

    client = DrawingClient()
    context = client.context("create", filename=filename, foldername="Agent-Diagrams")
    token = context["contextToken"]
    initial = client.read(token)
    diagram = {"diagramId": "installation-smoke", "kind": "flowchart", "style": "professional",
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    commands.add_parser("serve", help="Serve the bundled drawing MCP tools over stdio")
    commands.add_parser("status", help="Show redacted connection status and available vaults")
    commands.add_parser("doctor", help="Require a reachable authenticated Bridge")
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
    cli = commands.add_parser("cli", help="Run the full drawing CLI; options after -- are forwarded")
    cli.add_argument("arguments", nargs=argparse.REMAINDER)
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
            result = smoke(args.filename)
        else:
            result = setup_status()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.action == "doctor":
            return 0 if result["connected"] else 1
        if args.action == "smoke":
            return 0 if result["check"]["status"] == "pass" and result["preview"]["complete"] else 1
        return 0
    except Exception as error:
        print(json.dumps({"ok": False, "error": {"code": getattr(error, "code", "SETUP_ERROR"),
                                                 "message": str(error)}}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
