"""YAML/JSON scene CLI using the package's current native drawing connection."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from drawing_client import DrawingClient

from .model import load
from .service import execute


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest="action", required=True)
    commands.add_parser("fonts", help="Discover exact current-host font families and resource capabilities")
    for action in ("plan", "render"):
        command = commands.add_parser(action, help="Plan without scene mutation" if action == "plan" else "Incrementally reconcile a managed native scene, check and export PNG")
        command.add_argument("source", type=Path)
        command.add_argument("--font", dest="font_family", help="Exact family from fonts; overrides document style.font")
        command.add_argument("--state-id", help="Private managed identity key; defaults to document.id, scoped to host/vault")
        command.add_argument("--filename", help="Unique canvas name for the first render")
        command.add_argument("--folder", dest="foldername", default="Agent-Diagrams")
        command.add_argument("--file", dest="file_path", help="Explicit existing canvas in the host vault")
        command.add_argument("--output", type=Path, required=True, help="Client-side report JSON; render also writes a same-name PNG")
        command.add_argument("--scale", type=float, default=None)
        command.add_argument("--acceptance-level", choices=("low", "medium", "high"))
        command.add_argument("--brief-file", type=Path, help="Resolved user choices and requirements; required for a new drawing")
    review = commands.add_parser("review", help="Record actual observations of a registered current PNG")
    review.add_argument("--report", type=Path, required=True)
    review.add_argument("--checks", type=Path, required=True, help="JSON containing observed visual_checks and visual_issues")
    review.add_argument("--output", type=Path, required=True)
    return result


def main() -> int:
    args = parser().parse_args()
    result = None
    try:
        client = DrawingClient()
        if args.action == "fonts":
            discovery = client.context("discover")
            capabilities = discovery["capabilities"]
            result = {"fonts": capabilities["fonts"], "latex": capabilities.get("latex"),
                      "features": capabilities.get("features"), "bridge": discovery["status"]["bridgeVersion"]}
        elif args.action == "review":
            report = json.loads(args.report.read_text(encoding="utf-8"))
            observations = json.loads(args.checks.read_text(encoding="utf-8"))
            preview = report["preview"]
            result = client.review(report["contextToken"], revision=preview["revision"], preview_id=preview["previewId"],
                                   visual_reviewed=True, visual_checks=observations["visual_checks"],
                                   visual_issues=observations.get("visual_issues", []),
                                   dispositions=observations.get("dispositions"),
                                   detail_preview_ids=observations.get("detail_preview_ids"),
                                   requirement_checks=observations.get("requirement_checks"),
                                   check_result=report["check"],
                                   changes_summary=observations.get("changes_summary", "Actual scene DSL PNG review"))
        else:
            if args.output.resolve() == args.source.resolve():
                raise ValueError("Report output must not overwrite the source document")
            document = load(args.source)
            result = execute(client, args.action, document, font_family=args.font_family,
                             state_id=args.state_id, filename=args.filename, foldername=args.foldername,
                             file_path=args.file_path, scale=args.scale if args.scale is not None else "auto",
                             acceptance_level=args.acceptance_level, source_directory=args.source.resolve().parent,
                             output_path=args.output,
                             brief=json.loads(args.brief_file.read_text(encoding="utf-8")) if args.brief_file else None)
            if "preview" in result:
                result["preview"].pop("_base64", None)
        encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if getattr(args, "output", None):
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(encoded, encoding="utf-8")
        print(encoded, end="")
        if args.action == "render" and result["status"] == "needs_attention":
            return 2
        if args.action == "review" and result["status"] != "completed":
            return 2
        return 0
    except Exception as error:
        failure = {"ok": False, "error": str(error), "code": getattr(error, "code", "DSL_ERROR"),
                   "path": getattr(error, "path", None), "details": getattr(error, "details", None),
                   "committedReceipt": getattr(error, "committed_receipt", result),
                   "note": "Read current canvas/state after a committed or unknown transaction; never blindly replay drawing."}
        if getattr(args, "output", None) and (not hasattr(args, "source") or args.output.resolve() != args.source.resolve()):
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(failure, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(failure, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
