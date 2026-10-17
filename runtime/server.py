from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Any, Literal

_RUNTIME_DIR = str(Path(__file__).resolve().parent)
if _RUNTIME_DIR not in sys.path:
    sys.path.insert(0, _RUNTIME_DIR)

from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, ImageContent, TextContent

from drawing_client import BridgeError, DrawingClient
from review_ledger import ReviewLedger

mcp = FastMCP(
    "obsidian-excalidraw",
    instructions="""
Obsidian Excalidraw MCP Server for professional diagramming.

Workflow:
Fast path: create -> drawing_compose(diagram) -> optional drawing_apply(post-style, inspect=True) -> view PNG -> drawing_review.
drawing_compose(inspect=True) returns the checked PNG directly when no post-styling is needed.
Granular plan/apply/check/preview and every advanced operation remain available; no validation or visual gate is skipped.
Optional scene DSL: drawing_dsl(plan|render, document, font_family, state_id, filename|file_path) compiles measured spatial scenes and reconciles stable identities. First render needs a unique filename or explicit existing file; repeat the same state_id to update, never replay the graph with compose. Render returns actual checked PNG; view it then call drawing_review. Native tools remain the path for libraries, interaction and precise unmanaged edits.
Native table themes: discover capabilities.nativeTable.callable, then drawing_table(create|style). The paired host TableManager owns schema-v2 cells, themes/borders/reflow; never simulate palettes/three-line borders. Older hosts fail TABLE_RUNTIME_REQUIRED. Native manager saves are not atomic Bridge undo transactions. The paired host feature may still be a development build; do not claim package install upgrades the host plugin.
Acceptance levels low/medium/high (default medium) control QA depth, not model effort.
Medium/high require actual content/readability/occlusion checks on the current PNG.
High also checks connections and hierarchy/style; unbound arrows are legal unless binding is explicitly required.
Geometric candidates can be adjudicated individually with current PNG evidence, never blanket-ignored.
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


def _inspected_response(
    kind: str, context_token: str, receipt: dict[str, Any], started: float,
    expected: list[dict[str, Any]] | None,
    acceptance_level: str | None = None,
) -> CallToolResult:
    mutation_ms = (time.perf_counter() - started) * 1000
    try:
        result = client.inspect(context_token, receipt["revision"], expected=expected, acceptance_level=acceptance_level)
    except Exception as error:
        failure = BridgeError(
            str(error), code=getattr(error, "code", "INSPECTION_FAILED"),
            status=getattr(error, "status", 500),
            details={"phase": "inspection", kind: receipt, "atomic": False,
                     "cause": getattr(error, "details", None)},
        )
        return CallToolResult(isError=True, content=[
            TextContent(type="text", text=json.dumps(failure.to_dict(), ensure_ascii=False)),
        ])
    image = result["preview"].pop("_base64")
    result[kind] = receipt
    result["timings"].update(mutationMs=mutation_ms, totalMs=(time.perf_counter() - started) * 1000)
    return CallToolResult(content=[
        TextContent(type="text", text=json.dumps(result, ensure_ascii=False)),
        ImageContent(type="image", data=image, mimeType="image/png"),
    ])


@mcp.tool()
def drawing_context(
    action: Literal["discover", "create", "bind"],
    filename: str | None = None,
    foldername: str | None = None,
    file_path: str | None = None,
) -> dict[str, Any]:
    """Acquire canvas context: discover runtime capabilities, create a new canvas, or bind an existing file.

    Returns contextToken, file, revision, and capabilities.
    Before creating a new drawing, use the client's real choice UI for unspecified
    visual preferences per the Skill; do not re-ask specified choices or restyle edits.
    capabilities.fonts.registered lists current host families; source/error expose
    native getFontFamilies versus legacy registry evidence. Availability is not
    glyph coverage or suitability. Follow typography.md to assess fonts and choose
    explicit families by text role; do not assume a fixed installed font list.
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
    Pass the role-selected, currently discovered font_family explicitly. Equal
    widths for a few samples do not prove full monospace or absence of fallback.
    Remeasure after font/weight changes; dimensions alone do not verify rendering.
    This measures plain text, not MathJax: $...$ remains literal in text/labels.
    Render formulas with create_latex (bare tex); mixed prose needs native text
    plus formula images or the explicitly trusted host Extract-Latex Action.
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
    Plain node/edge labels do not parse $...$; use latex content for formulas,
    or compose mixed prose from text plus real LaTeX images per the Skill.
    Choose edge-level startArrowhead/endArrowhead explicitly by semantics (triangle
    for data, block_arrow/block_arrow_outline for emphasis, UML-specific heads).
    Profiles do not auto-select heads/palettes. Use style.roundness {type,value}
    for fixed corners instead of relying on edge="round".
    Hardware microarchitecture is NOT ordinary service-graph layout. Read the
    Skill's microarchitecture reference first: explicit components/ports/stage
    geometry. kind="microarchitecture" alone adds no hardware layout semantics.
    """
    return client.plan(
        context_token=context_token,
        diagram=diagram,
    )


@mcp.tool()
def drawing_table(
    context_token: str,
    base_revision: str,
    action: Literal["create", "style"],
    target: str | None = None,
    options: dict[str, Any] | None = None,
    theme: str | None = None,
    border: str | None = None,
    ref: str | None = None,
) -> dict[str, Any]:
    """Create/style a native schema-v2 table through the paired host TableManager.

    Discover capabilities.nativeTable first. Create options: x/y, rows/cols,
    cellWidth>=40, cellHeight>=32, cells string matrix, optional columnWidths
    and text style. Themes/borders come from that capability catalog.
    Style needs an explicit native root/cell target. Content and sizing survive
    theme/border changes. Host native undo applies; not atomic/drawing_revert.
    Older hosts fail TABLE_RUNTIME_REQUIRED rather than simulating a theme.
    """
    return client.table(context_token, base_revision, action, target, options, theme, border, ref)


@mcp.tool()
def drawing_dsl(
    action: Literal["plan", "render"],
    document: dict[str, Any],
    font_family: str | None = None,
    state_id: str | None = None,
    filename: str | None = None,
    foldername: str | None = None,
    file_path: str | None = None,
    scale: str | float = "auto",
    acceptance_level: Literal["low", "medium", "high"] | None = None,
) -> Any:
    """Compile an optional declarative scene into native editable elements.

    document is the parsed scene DSL object: version/id/nodes/edges/layout, plus
    optional groups/classes/style/acceptance. Shapes include native tables,
    MUX/ALU polygons and source-preserving image/formula/chart content.
    row/column/grid express fixed spatial composition; root flow is for graphs.
    Select an exact host-discovered font_family (or document.style.font).
    First render requires filename or explicit file_path; plan requires existing
    managed state or file_path for real text measurement and does not edit canvas.
    state_id defaults to document.id, is private and host/vault-scoped. Reuse it
    for incremental updates. Native IDs, bindings and unrelated content remain;
    external edits to managed elements are conflicts, never auto-overwritten.
    Render performs full checks and PNG export, not visual approval: inspect the
    returned image and use drawing_review with its contextToken/previewId.
    Do not mix this schema with drawing_compose's ordinary diagram schema.
    """
    from scene_dsl.service import execute

    try:
        result = execute(client, action, document, font_family=font_family, state_id=state_id,
                         filename=filename, foldername=foldername, file_path=file_path,
                         scale=scale, acceptance_level=acceptance_level)
        if action == "plan":
            return result
        image = result["preview"].pop("_base64")
        return CallToolResult(content=[
            TextContent(type="text", text=json.dumps(result, ensure_ascii=False)),
            ImageContent(type="image", data=image, mimeType="image/png"),
        ])
    except Exception as error:
        failure = {"ok": False, "error": {"code": getattr(error, "code", "DSL_ERROR"),
                   "message": str(error), "path": getattr(error, "path", None),
                   "details": getattr(error, "details", None),
                   "committedReceipt": getattr(error, "committed_receipt", None)},
                   "note": "Inspect current canvas/state after a committed or unknown transaction; never blindly replay drawing."}
        return CallToolResult(isError=True, content=[
            TextContent(type="text", text=json.dumps(failure, ensure_ascii=False)),
        ])


@mcp.tool()
def drawing_apply(
    context_token: str,
    base_revision: str,
    operations: list[dict[str, Any]],
    inspect: bool = False,
    expected: list[dict[str, Any]] | None = None,
    acceptance_level: Literal["low", "medium", "high"] | None = None,
) -> Any:
    """Apply an array of operations to the canvas in a single staged transaction.

    Returns transactionId, new revision, created/updated/deleted element IDs.
    Every operations item REQUIRES "op", NOT "type". Example title bold:
    {"op":"set_text_global_style","targets":["actual native text ID"],"bold":true}
    Use compose's refs["diagram:title"] and its current revision for post-styling.
    inspect=True also performs full geometry/structure/semantic checks and returns
    a registered PNG ImageContent, full canvasSummary and measured phase timings.
    It does NOT perform visual review. Use drawing_review only after seeing the PNG.
    A post-mutation inspection error retains the committed receipt; no false rollback.
    resize {target,width,height,anchor:"top-left"} changes one non-linear element,
    not a compound item or its font sizes. For an imported template/circuit symbol,
    scale_selection the complete instance (including anchor/frame children), not
    only its outer frame/transparent anchor. factor is relative to CURRENT size.
    Selection transforms: rotate accepts targets[] OR groupId plus relative degrees
    (positive clockwise); scale_selection accepts targets[] OR groupId plus factor>0,
    fromCenter defaults true. Both reuse the installed manual native transform.
    patch_element.patch.angle is an absolute radian value and follows bound text.
    Frames cannot rotate; selected arrows must include their bound endpoints.
    create_text/set_text/label do NOT parse inline $...$ or $$...$$. Use create_latex
    with bare tex and numeric scaleX/scaleY for actual formulas. Mixed prose must
    use native text+formula composition or the trusted host Extract-Latex Action;
    that Action replaces text IDs, so preserve owner/group/frame/bindings explicitly.
    Select head/body/routing separately: set_arrow_style supports semantic heads;
    patch_element.patch.roundness {type:3,value:6,roundType:"arc"} fixes rectangle
    corners; elbow arrows use type:2,value (0 for square turns). Preserve bindings.
    Low-level connect defaults elbowed=False and directly joins endpoints without
    waypoints; it does not auto-route. Hardware wires must use explicit orthogonal
    routes and verify every saved world-coordinate segment, not just angle/elbow flag.
    PPT block_arrow/block_arrow_outline use customData.blockArrowWidth in scene
    units for shaft thickness: patch_custom_data merge, not set_arrow_style width.
    Path length, arrowHeadSize and outline strokeWidth are separate controls.
    Read runtime head support and inspect the full visible envelope in PNG.
    acceptance_level is QA depth (default medium), independent of model effort.
    It is retained for later checks/reviews even when inspect=False.
    """
    started = time.perf_counter()
    if acceptance_level is not None or expected is not None:
        settings = ReviewLedger(context_token, acceptance_level=acceptance_level)
        if expected is not None:
            settings.expected = expected
        settings.save()
    receipt = client.apply(context_token, base_revision, operations)
    return _inspected_response("applied", context_token, receipt, started, expected, acceptance_level) if inspect else receipt


@mcp.tool()
def drawing_check(
    context_token: str,
    expected: list[dict[str, Any]] | None = None,
    scope: Literal["all", "selection", "viewport"] = "all",
    acceptance_level: Literal["low", "medium", "high"] | None = None,
    preview_id: str | None = None,
) -> dict[str, Any]:
    """Run geometry diagnostics and semantic checks on the current canvas.

    Detects text overflow, body overlap, arrow crossing unrelated nodes, label occlusion, and broken bindings.
    Geometry pass does not certify MathJax or inline formula rendering. Inspect
    the actual PNG and retained source TeX; literal math source in normal text
    is not a rendered formula unless the user requested source/code.
    Default medium; an omitted level inherits this canvas context's stored selection.
    Text/text, shaft-through-text and paint-order risks are distinct from legal
    text over a background. issueId/blocking identify targeted repairs or specific
    PNG-based false-positive adjudication. No blanket mandatory arrow binding.
    preview_id adds output-scale readability triggers from a current registered PNG.
    """
    return client.check(
        context_token=context_token,
        expected=expected,
        scope=scope,
        acceptance_level=acceptance_level,
        preview_id=preview_id,
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
    acceptance_level: Literal["low", "medium", "high"] | None = None,
    visual_checks: dict[str, str] | None = None,
    dispositions: list[dict[str, Any]] | None = None,
    detail_preview_ids: list[str] | None = None,
) -> dict[str, Any]:
    """Record review round in persistent ledger and determine whether to continue, complete, or seek attention.

    Requires visual_reviewed=True (after actually inspecting PNG preview) to allow completion.
    Medium requires visual_checks content/readability/occlusion; high also requires
    connections/hierarchy_style. Values: pass, not_applicable, fail. Low keeps a
    lighter checklist but never bypasses broken references or missing resources.
    dispositions: [{issue_id,decision:"false_positive"|"intentional",reason}] apply
    only to current geometric candidates after real PNG inspection, not semantic
    or native structural errors. Findings remain disclosed; detail IDs must be
    registered at this revision. Level and expected assertions persist per context.
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
        acceptance_level=acceptance_level,
        visual_checks=visual_checks,
        dispositions=dispositions,
        detail_preview_ids=detail_preview_ids,
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
    Ask once for unspecified visual preferences using the client's selection UI.
    Palette names are Skill workflows, not extra profiles; resolve colors/fonts/
    bold/corners/heads to real native properties and respect strict color lists.
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
    Read exact bounds/frame dimensions and choose numeric scale for the intended
    content area BEFORE insertion; default 1 preserves source size, not automatic fit.
    Preserve aspect ratio; adjust imported complete instances with scale_selection.
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
    inspect: bool = False,
    expected: list[dict[str, Any]] | None = None,
    acceptance_level: Literal["low", "medium", "high"] | None = None,
) -> Any:
    """Compose measured native nodes and user-selected library items without rasterizing the diagram.

    Prefer this also for ordinary native graphs: plan->apply stays in code, with
    no need to copy operations through the model. inspect=True adds full checks
    and registered PNG ImageContent/timings; actual visual review stays separate.
    For title bold or other post-styling, compose first, then drawing_apply with
    inspect=True to get the final checked PNG in that same call.
    Each native import commits separately; failures report prior committed stages. Inspect final PNG.
    Set each nodes[].library.scale from real source bounds and target symbol size
    before wiring; node.size reserves layout space but does not rescale library art.
    For CPU/datapath/array diagrams, read microarchitecture.md before composing.
    Preserve independent hardware blocks, named ports and explicit stage geometry;
    never replace ALU/RF/MUX with stage bullet lists to make checks pass.
    A committed composition with failed check must be repaired by IDs, not replayed.
    Hardware signals need axis-aligned straight links or explicit orthogonal routes.
    Native elbow mode may reroute small port anchors: audit saved points, endpoints
    and collisions. An explicit orthogonal polyline need not have elbowed=True.
    acceptance_level selects low/medium/high QA, default medium, not model effort.
    inspect/check detects text-legibility risks; actual PNG review is still required.
    """
    started = time.perf_counter()
    if acceptance_level is not None or expected is not None:
        settings = ReviewLedger(context_token, acceptance_level=acceptance_level)
        if expected is not None:
            settings.expected = expected
        settings.save()
    receipt = client.compose(context_token, base_revision, diagram)
    return _inspected_response("composition", context_token, receipt, started, expected, acceptance_level) if inspect else receipt


@mcp.tool()
def drawing_present(
    context_token: str,
    base_revision: str,
    presentation: dict[str, Any],
) -> dict[str, Any]:
    """Create editable Excalidraw pages from an actual presentation library.

    Preserves imported frames, fills title/body, returns each page's IDs for PNG review.
    Read source frame dimensions and set presentation.scale BEFORE filling text;
    default 1 is source size, not page/content auto-fit. Only top-level scale exists,
    not per-page scale/width/height. Fit differing source sizes in separate calls.
    This creates native Excalidraw pages, not an unimplemented PPTX export.
    """
    return client.present(context_token, base_revision, presentation)


if __name__ == "__main__":
    mcp.run("stdio")
