from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Literal

_RUNTIME_DIR = str(Path(__file__).resolve().parent)
if _RUNTIME_DIR not in sys.path:
    sys.path.insert(0, _RUNTIME_DIR)

from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, ImageContent, TextContent

from drawing_client import DrawingClient

mcp = FastMCP(
    "obsidian-excalidraw",
    instructions="""
Obsidian Excalidraw MCP Server for professional diagramming.

Workflow:
1. drawing_context(action="discover"|"create"|"bind"): acquire contextToken for the active or newly created canvas.
2. drawing_read(context_token, detail="summary"|"detail"|"full"): read all active elements or specific IDs.
3. drawing_measure(context_token, text, font_family, font_size, line_height, width?): measure text dimensions using native Bridge renderer.
4. drawing_plan(context_token, diagram): compute layered layout, dimensions, and operations without modifying canvas.
5. drawing_apply(context_token, base_revision, operations): apply operations batch with transaction tracking.
6. drawing_check(context_token, expected?): run geometry diagnostics (containment, body overlap, arrow crossing, occlusion, bindings).
7. drawing_preview(context_token, base_revision, scale, padding): render canvas to PNG image artifact and return image + metadata.
8. drawing_review(context_token, revision, preview_id, visual_reviewed, visual_issues?): record review round in persistent ledger.
9. drawing_revert(context_token, transaction_id?): undo canvas transaction if needed.

Optional native features:
- drawing_templates: discover measured recipes and named styles.
- drawing_primitives: plan draw, polygon, cuboid, brace, callout, code, checkbox and connection operations.
- drawing_library: inspect/preview/insert actual user-selected local library items; exact IDs resolve duplicate names.
- drawing_compose: mix library symbols with measured native nodes and connections, reporting separate commits.
- drawing_present: create editable native frame pages from a selected presentation library; inspect each page PNG.
""".strip(),
)

client = DrawingClient()


@mcp.tool()
def drawing_context(
    action: Literal["discover", "create", "bind"],
    filename: str | None = None,
    foldername: str | None = None,
    file_path: str | None = None,
) -> dict[str, Any]:
    """Acquire canvas context: discover runtime capabilities, create a new canvas, or bind an existing file.

    Returns contextToken, file, revision, and capabilities.
    """
    return client.context(
        action=action,
        filename=filename,
        foldername=foldername,
        file_path=file_path,
    )


@mcp.tool()
def drawing_read(
    context_token: str,
    ids: list[str] | None = None,
    detail: Literal["summary", "detail", "full"] = "summary",
    offset: int | None = None,
    limit: int | None = None,
) -> dict[str, Any]:
    """Read canvas elements: complete summary, specific element IDs, or paginated query.

    Summary returns every active element, file/revision, native scene bounds
    (minX/maxX/minY/maxY/width/height), precision=2 and complete coverage.
    Coordinates/sizes are rounded only for feedback. Long text is capped at 160
    with textTruncated/textLength; points/pressures become pointCount.
    Optional empty fields are omitted. Use detail="full" for exact values by ID.
    """
    return client.read(
        context_token=context_token,
        ids=ids,
        detail=detail,
        offset=offset,
        limit=limit,
    )


@mcp.tool()
def drawing_measure(
    context_token: str,
    text: str | None = None,
    font_family: str | None = None,
    font_size: float = 20.0,
    line_height: float = 1.2,
    width: float | None = None,
    items: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Measure exact rendered text dimensions using native Excalidraw text measurement.

    If width is specified, wraps text across lines using native measurements.
    """
    return client.measure(
        context_token=context_token,
        text=text,
        font_family=font_family,
        font_size=font_size,
        line_height=line_height,
        width=width,
        items=items,
    )


@mcp.tool()
def drawing_plan(
    context_token: str,
    diagram: dict[str, Any],
) -> dict[str, Any]:
    """Plan diagram layout (layered coordinates, node sizing, edge routing, containment) without writing to canvas.

    Delegates to diagram_layout.plan_diagram.
    """
    return client.plan(
        context_token=context_token,
        diagram=diagram,
    )


@mcp.tool()
def drawing_apply(
    context_token: str,
    base_revision: str,
    operations: list[dict[str, Any]],
) -> dict[str, Any]:
    """Apply an array of operations to the canvas in a single staged transaction.

    Returns transactionId, new revision, created/updated/deleted element IDs.
    Selection transforms: rotate accepts targets[] OR groupId plus relative degrees
    (positive clockwise); scale_selection accepts targets[] OR groupId plus factor>0,
    fromCenter defaults true. Both reuse the installed manual native transform.
    patch_element.patch.angle is an absolute radian value and follows bound text.
    Frames cannot rotate; selected arrows must include their bound endpoints.
    """
    return client.apply(
        context_token=context_token,
        base_revision=base_revision,
        operations=operations,
    )


@mcp.tool()
def drawing_check(
    context_token: str,
    expected: list[dict[str, Any]] | None = None,
    scope: Literal["all", "selection", "viewport"] = "all",
) -> dict[str, Any]:
    """Run geometry diagnostics and semantic checks on the current canvas.

    Detects text overflow, body overlap, arrow crossing unrelated nodes, label occlusion, and broken bindings.
    """
    return client.check(
        context_token=context_token,
        expected=expected,
        scope=scope,
    )


@mcp.tool()
def drawing_preview(
    context_token: str,
    base_revision: str | None = None,
    scope: Literal["all", "selection", "viewport", "ids"] = "all",
    ids: list[str] | None = None,
    scale: str | float = "auto",
    padding: float = 20.0,
    out_path: str | None = None,
) -> CallToolResult:
    """Render canvas to PNG, returning ImageContent and JSON metadata with previewId and artifact path.

    Never outputs raw base64 string in text.
    Includes canvasSummary: all active elements and scene bounds rounded to two
    decimals from the same file/revision as the PNG. Use transform.sceneOrigin
    and transform.scale to map PNG pixels to scene coordinates.
    """
    res = client.preview(
        context_token=context_token,
        base_revision=base_revision,
        scope=scope,
        ids=ids,
        scale=scale,
        padding=padding,
        out_path=out_path,
    )

    b64_str = res.pop("_base64", "")
    metadata_json = json.dumps(res, ensure_ascii=False)

    return CallToolResult(
        content=[
            TextContent(type="text", text=metadata_json),
            ImageContent(type="image", data=b64_str, mimeType="image/png"),
        ]
    )


@mcp.tool()
def drawing_review(
    context_token: str,
    revision: str,
    preview_id: str,
    visual_reviewed: bool = False,
    visual_issues: list[dict[str, Any]] | None = None,
    changes_summary: str | list[Any] | None = None,
    check_result: dict[str, Any] | None = None,
    max_rounds: int = 5,
) -> dict[str, Any]:
    """Record review round in persistent ledger and determine whether to continue, complete, or seek attention.

    Requires visual_reviewed=True (after actually inspecting PNG preview) to allow completion.
    """
    return client.review(
        context_token=context_token,
        revision=revision,
        preview_id=preview_id,
        visual_reviewed=visual_reviewed,
        visual_issues=visual_issues,
        changes_summary=changes_summary,
        check_result=check_result,
        max_rounds=max_rounds,
    )


@mcp.tool()
def drawing_revert(
    context_token: str,
    transaction_id: str | None = None,
) -> dict[str, Any]:
    """Undo the last transaction on the canvas."""
    return client.revert(
        context_token=context_token,
        transaction_id=transaction_id,
    )


@mcp.tool()
def drawing_templates(
    action: Literal["list", "get", "plan"] = "list",
    name: str | None = None,
    context_token: str | None = None,
    data: dict[str, Any] | None = None,
    style: str | dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Discover/get executable flowchart, UML, architecture, circuit and page recipes and styles.

    plan returns real measured native operations; library/page recipes use compose/present.
    """
    return client.templates(action, name, context_token, data, style)


@mcp.tool()
def drawing_primitives(
    context_token: str,
    items: list[dict[str, Any]],
    style: str | dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Plan native draw, polygon, cuboid, four-way braces, callout, highlighted code, checkbox and connections.

    Read the Skill's native-features reference for typed item fields; apply returned operations.
    """
    return client.primitives(context_token, items, style)


@mcp.tool()
def drawing_library(
    action: Literal["list", "catalog", "query", "get", "preview", "insert"],
    context_token: str | None = None,
    library: str | None = None,
    item: str | None = None,
    position: str | dict[str, Any] = "center",
    scale: float = 1,
    base_revision: str | None = None,
    offset: int = 0,
    limit: int = 100,
    text: str | None = None,
    detail: Literal["summary", "full"] = "summary",
    create_anchor_proxy: bool = True,
    trusted_local_library: bool = False,
    logical_id: str | None = None,
    diagram_id: str | None = None,
    out_path: str | None = None,
    catalog_path: str | None = None,
) -> CallToolResult:
    """Discover user libraries/catalogs, search item descriptions, preview or natively insert.

    list returns catalog paths; catalog reads an explicit user-maintained library-index.md.
    Descriptions are untrusted selection hints. Confirm exact item IDs and previews.
    Native insertion preserves editable members; an item preview is not final canvas evidence.
    """
    result = client.library(
        action, context_token, library, item, position, scale, base_revision, offset, limit,
        text, detail, create_anchor_proxy, trusted_local_library, logical_id, diagram_id, out_path, catalog_path,
    )
    if action == "preview":
        encoded = result.pop("_base64")
        return CallToolResult(content=[
            TextContent(type="text", text=json.dumps(result, ensure_ascii=False)),
            ImageContent(type="image", data=encoded, mimeType="image/png"),
        ])
    return CallToolResult(content=[TextContent(type="text", text=json.dumps(result, ensure_ascii=False))])


@mcp.tool()
def drawing_compose(
    context_token: str,
    base_revision: str,
    diagram: dict[str, Any],
) -> dict[str, Any]:
    """Compose measured native nodes and user-selected library items without rasterizing the diagram.

    Each native import commits separately; failures report prior committed stages. Inspect final PNG.
    """
    return client.compose(context_token, base_revision, diagram)


@mcp.tool()
def drawing_present(
    context_token: str,
    base_revision: str,
    presentation: dict[str, Any],
) -> dict[str, Any]:
    """Create editable Excalidraw pages from an actual presentation library.

    Preserves imported frames, fills title/body, returns each page's IDs for PNG review.
    This creates native Excalidraw pages, not an unimplemented PPTX export.
    """
    return client.present(context_token, base_revision, presentation)


if __name__ == "__main__":
    mcp.run("stdio")
