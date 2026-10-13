"""Inspect user libraries and change description metadata without touching drawings."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any


def read_library(path: Path) -> tuple[bytes, dict[str, Any], list[dict[str, Any]]]:
    raw = path.read_bytes()
    document = json.loads(raw.decode("utf-8-sig"))
    if not isinstance(document, dict) or document.get("type") != "excalidrawlib":
        raise ValueError(f"Not an Excalidraw library: {path}")
    items = document.get("libraryItems")
    if document.get("version") != 2 or not isinstance(items, list) or any(not isinstance(item, dict) for item in items):
        raise ValueError(f"Metadata editing requires an existing v2 libraryItems object array; do not silently migrate legacy libraries: {path}")
    ids = [item.get("id") for item in items]
    if any(not isinstance(item_id, str) or not item_id for item_id in ids) or len(ids) != len(set(ids)):
        raise ValueError(f"Library item IDs must exist and be unique: {path}")
    return raw, document, items


def inventory(directory: Path) -> dict[str, Any]:
    if not directory.is_dir():
        raise ValueError("Library directory does not exist")
    entries = []
    for path in sorted(directory.rglob("*.excalidrawlib")):
        try:
            raw, document, items = read_library(path)
            summaries = []
            for item in items:
                elements = item.get("elements", [])
                if not isinstance(elements, list):
                    raise ValueError(f"Item {item['id']} has invalid elements")
                active = [element for element in elements if isinstance(element, dict) and not element.get("isDeleted")]
                texts = [str(element.get("text") or element.get("originalText"))[:160] for element in active
                         if element.get("type") == "text" and (element.get("text") or element.get("originalText"))]
                features = sorted({str(key) for element in active for key in (element.get("customData") or {})})
                summaries.append({"id": item["id"], "name": item.get("name"),
                                  "description": item.get("description"), "elementCount": len(active),
                                  "types": sorted({str(element.get("type")) for element in active}),
                                  "textSummary": texts[:8], "textSummaryTruncated": len(texts) > 8,
                                  "featureKeys": features})
            entries.append({"path": path.relative_to(directory).as_posix(), "sha256": hashlib.sha256(raw).hexdigest(),
                            "description": document.get("description"), "itemCount": len(items),
                            "describedItemCount": sum(isinstance(item.get("description"), str) and bool(item["description"].strip()) for item in items),
                            "items": summaries, "editable": True})
        except (ValueError, UnicodeError, OSError) as error:
            entries.append({"path": path.relative_to(directory).as_posix(), "editable": False, "error": str(error)})
    return {"directory": str(directory.resolve()), "totalLibraries": len(entries), "coverage": "complete",
            "libraries": entries, "catalog": "library-index.md",
            "note": "Descriptions are user-maintained selection hints; inventory does not infer semantics or render previews."}


def apply_descriptions(path: Path, proposal: dict[str, Any], expected_sha256: str) -> dict[str, Any]:
    path = path.resolve()
    if path.suffix.lower() != ".excalidrawlib":
        raise ValueError("Metadata edits require an explicit .excalidrawlib file")
    if not isinstance(proposal, dict) or set(proposal) - {"description", "items"}:
        raise ValueError("Proposal may contain only description and items")
    raw, document, items = read_library(path)
    digest = hashlib.sha256(raw).hexdigest()
    if digest != expected_sha256:
        raise ValueError("Library changed since inspection; re-read before modifying metadata")
    changes = proposal.get("items", [])
    if not isinstance(changes, list):
        raise ValueError("items must be an array of exact item IDs and descriptions")
    by_id = {item["id"]: item for item in items}
    seen = set()
    changed = []
    def description(value: Any) -> str:
        if not isinstance(value, str) or len(value) > 4000:
            raise ValueError("description must be a string of at most 4000 characters")
        return value
    for change in changes:
        if not isinstance(change, dict) or set(change) != {"id", "description"}:
            raise ValueError("Each item update must contain only id and description")
        item_id = change["id"]
        if not isinstance(item_id, str) or item_id not in by_id or item_id in seen:
            raise ValueError("Item ID is missing, ambiguous or repeated; names are not update identities")
        seen.add(item_id)
        value = description(change["description"])
        if by_id[item_id].get("description") != value:
            by_id[item_id]["description"] = value
            changed.append(item_id)
    library_changed = False
    if "description" in proposal:
        value = description(proposal["description"])
        library_changed = document.get("description") != value
        document["description"] = value
    if not changed and not library_changed:
        return {"path": str(path.resolve()), "changed": False, "sha256": digest, "changedItemIds": []}
    encoded = (json.dumps(document, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
    backup = path.with_name(path.name + "." + digest[:12] + ".metadata-backup")
    if backup.exists():
        if backup.read_bytes() != raw:
            raise ValueError("An existing backup does not match the inspected source")
    else:
        with backup.open("xb") as stream:
            stream.write(raw)
    fd, temporary_name = tempfile.mkstemp(prefix="." + path.name + ".", suffix=".tmp", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(encoded)
        os.chmod(temporary, path.stat().st_mode)
        if path.read_bytes() != raw:
            raise ValueError("Library changed before publication; no metadata was applied")
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)
    return {"path": str(path.resolve()), "changed": True, "changedItemIds": changed,
            "libraryDescriptionChanged": library_changed, "backup": str(backup.resolve()),
            "previousSha256": digest, "sha256": hashlib.sha256(encoded).hexdigest(),
            "note": "Only description metadata changed; IDs, names, elements, resources and unrelated fields were preserved. JSON formatting may change."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inspect = commands.add_parser("inventory", help="List all v2 library metadata without raw elements or resource bodies")
    inspect.add_argument("--directory", required=True, type=Path)
    update = commands.add_parser("apply", help="Apply a reviewed description-only proposal to one library")
    update.add_argument("--library", required=True, type=Path)
    update.add_argument("--updates", required=True, type=Path)
    update.add_argument("--expected-sha256", required=True)
    args = parser.parse_args()
    try:
        result = inventory(args.directory) if args.command == "inventory" else apply_descriptions(
            args.library, json.loads(args.updates.read_text(encoding="utf-8")), args.expected_sha256)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
