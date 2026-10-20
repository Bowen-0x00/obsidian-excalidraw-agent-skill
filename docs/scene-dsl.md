# Scene DSL: measured, editable diagrams

The DSL is an **optional authoring layer in this package**, not a second renderer or a required replacement for native tools. YAML files and parsed JSON objects describe the same scene. A real connected Obsidian Excalidraw-ymjr host measures text, constructs native elements, maintains bindings and exports PNGs.

Use it for repeatable flowcharts, nested spatial regions, tables, named-port schematics and chart panels. Use ordinary `drawing_compose` for a quick graph, and native read/apply/library/present tools for precise edits and extensions outside the DSL.

## Run an example

From the installed package/repository directory, with the same private connection used by MCP:

```sh
uv run --frozen python launcher.py status
uv run --frozen python launcher.py dsl -- fonts
uv run --frozen python launcher.py dsl -- render examples/dsl/release-flow.yaml --font "EXACT_HOST_FAMILY" --brief-file ./drawing-brief.json --state-id release-demo --filename "Release-Demo-Unique" --output ./output/release.json
```

`EXACT_HOST_FAMILY` is a placeholder: select an exact string returned by `fonts`, not a machine-specific name copied from a screenshot. Open an Excalidraw canvas if discovery reports `NO_EXCALIDRAW_VIEW`. The output directory is on the CLI/MCP client, not necessarily on the graphical host. Set the existing `EXCALIDRAW_AGENT_STATE_DIR` environment variable when selecting a non-default connection.

Before a first render, save the resolved choices and user requirements in `drawing-brief.json` using the [brief format](../skills/obsidian-excalidraw/references/diagram-recipes.md). Ask unresolved style/review first. CLI and MCP share this gate; source layout and generated labels do not replace the user's requirement list. Existing managed state keeps its task brief on subsequent renders.


Edit the YAML and repeat the same command with **the same `--state-id`**; omit `--filename` after the first render. This updates the original managed elements rather than appending a second diagram. Omitting state-id uses the document's stable `id`; use distinct state IDs for distinct canvases of the same source.

Read-only planning needs a real canvas for text measurement:

```sh
uv run --frozen python launcher.py dsl -- plan examples/dsl/release-flow.yaml --font "EXACT_HOST_FAMILY" --state-id release-demo --output ./output/plan.json
```

For a first plan without managed state, replace `--state-id release-demo` with `--file "Agent-Diagrams/existing.excalidraw.md"`. Plan does not edit the canvas. It is not an offline character-width estimator.

## The one MCP entrypoint

`drawing_dsl` accepts these fields:

| Field | Meaning |
| --- | --- |
| `action` | `plan` or `render` |
| `document` | Parsed JSON scene object; same schema as the YAML file |
| `font_family` | Exact discovered family; otherwise use document `style.font` |
| `state_id` | Private identity key, default document.id, scoped to connection host/vault |
| `filename`, `foldername` | First new canvas name and optional vault folder |
| `file_path` | Explicit existing vault canvas; needed for a first read-only plan or deliberate addition to an existing file |
| `scale` | `auto` by default or a numeric native export scale |
| `acceptance_level` | Optional low/medium/high, must match the task's resolved review choice |
| `brief` | Required for a new drawing: task_id, per-choice provenance and user requirements; same structure as CLI --brief-file |

```javascript
const request = {
  brief: resolvedDrawingBrief, // actual per-choice answers and requirement list from the linked format
  "action": "render",
  "document": {
    "version": 1,
    "id": "approval",
    "nodes": {"start": "Request", "review": "Review", "done": "Done"},
    "layout": {"row": ["start", "review", "done"], "gap": 100},
    "edges": {
      "submit": {"from": "start.right", "to": "review.left"},
      "approve": {"from": "review.right", "to": "done.left"}
    }
  },
  font_family: discoveredFamily,
  "state_id": "approval-demo",
  "filename": "Approval-Demo-Unique"
}
```

Do not pass this object to `drawing_compose`: its `diagram` schema is different. Do not hand-edit raw native IDs, versions, indices or binding reciprocity. The DSL compiles to the existing native operations, not to a full scene JSON replacement.

Render returns file/contextToken/revision/stateId, operationCount/diff, layout, check and preview metadata. MCP additionally returns **actual PNG ImageContent**. `visualReviewed:false` and `status:rendered_needs_visual_review` do not mean completed. Plan returns proposed native operations without applying them.

## Inspect, then review

Actually open the generated PNG. For medium acceptance record content, readability and occlusion; high also requires connections and hierarchy/style. Only write the following outcomes if the image supports them:

```json
{
  "visual_checks": {"content": "pass", "readability": "pass", "occlusion": "pass"},
  "visual_issues": [],
  "changes_summary": "Describe what was actually inspected and any repairs.",
  "requirement_checks": [
    {"requirement_id":"the actual brief requirement ID","outcome":"pass","element_ids":["current native IDs"],"evidence":"Explain the observed content/relationship and limitations, not just that a label was generated."}
  ]
}
```

```sh
uv run --frozen python launcher.py dsl -- review --report ./output/release.json --checks ./output/observations.json --output ./output/review.json
```

MCP callers use existing `drawing_review` with the returned contextToken, previewId and revision. Existing check/preview tools can supply readable detail crops. A render never fabricates a visual checklist or automatically approves itself.

Text-conflict false positives require matching element IDs, a distinct reason, and a current readable registered detail PNG. Intentional text collisions and repeated blanket reasons are rejected. Small overview text requires readable detail coverage at medium/high. `rawCheckStatus` preserves the unwaived diagnostics; a completed review is not proof of hardware/math correctness or that every glyph avoided font fallback.


CLI exit codes: **0** = command succeeded (render still needs visual review), **1** = parse/compile/conflict/execution error, **2** = rendered but checks/resources need attention or review is not completed. A nonzero post-commit result is not a rollback. Read `committedReceipt` and current state before any retry; never replay an unknown transaction blindly.

## Authoring contract

```yaml
version: 1
id: named_ports
title: Select and compute
acceptance: medium
style: {font_size: 20, stroke: '#475569', fill: '#f8fafc'}
classes:
  compute: {stroke: '#1d4ed8', fill: '#eff6ff'}
nodes:
  input: {label: Input, ports: {out: right}}
  mux:
    shape: mux
    label: MUX
    ports: {a: 'left:0.25', b: 'left:0.75', sel: top, out: right}
  alu:
    shape: alu
    label: ALU
    class: compute
    ports: {a: 'left:0.25', result: right}
layout: {row: [input, mux, alu], gap: 130}
edges:
  incoming: {from: input.out, to: mux.a}
  selected: {from: mux.out, to: alu.a}
```

Stable document/node/group/edge IDs use ASCII identifiers. Labels may contain other languages. Node strings abbreviate `{label: ...}`. Duplicate keys, unknown fields/references, duplicate placement, containment cycles, YAML aliases, executable tags and raw operation injection are rejected. `Yes/No` remain table strings; explicit `true/false` are booleans.

### Shapes and resources

| Shape | Content and behavior |
| --- | --- |
| `box`, `ellipse`, `diamond`, `text` | Native shapes/text with real measured wrapping |
| `mux`, `alu` | Editable polygon silhouette, text and transparent binding anchor |
| `polygon` | At least three normalized 0..1 points; closed native line polygon |
| `table` | `columns` and equal-width-in-count `rows`; measured per-column widths, sharp cells, contrasting header, native bound text |
| `image` | `source` and reserved `size`; real source resource, aspect-preserving native measurement |
| `formula` | Bare `tex` and reserved `size`; native MathJax resource retains TeX, needs host prerequisites |
| `chart` | Structured ECharts `options` and `size`; retained native configuration, not a replacement screenshot |
| `embed` | Host-supported `source` and `size`; export depends on actual DOM capture/resource readiness |

`size:[width,height]` sets a minimum for ordinary shapes and a reserved content area for resources. Captions occupy additional space. `wrap` controls actual measured wrapping, not source truncation. `at:[x,y]` pins a node in global scene coordinates, including negative coordinates; it does not automatically expand its region or push neighbors away.

Local CLI images can use `asset:assets/example.png` beneath the source directory. Only PNG/JPEG files up to 2 MB are uploaded by this helper. MCP uses data URLs or actual host resources; a remote client path is not a host path.

Node/region style priority: built-in defaults → document style → named class → local style. CLI `--font`/MCP font_family overrides document.style.font; explicit class/node fonts still apply. Keys: stroke/fill/text/font/font_size/stroke_width/dash/roughness, and edge head/shaft/head_scale. Edge category defaults are independent of node fills; edge class/local style override them. Fonts and geometry-changing styles require remeasurement.

Controlled features are `shadow`, `gradient`, `rich_text`. Structured configs go through existing adapters; arbitrary customData/scripts are not accepted. ECharts advanced chart types use the Bridge's `custom` plus complete JSON options. Charts created this way can roundtrip through the host JSON editor; restoring a specialized visual-form data model is not claimed.

### Spatial layout

- `row` and `column`: measured ordered composition with centered cross-axis alignment.
- `grid`: rows of members, `null` for an empty cell, shared column/row track sizes.
- `groups`: visible regions with label/layout/padding/class/style; default padding 28 plus a measured header band.
- `flow:right/down`: root-only ordinary graph layout, no groups; feedback/control do not force feed-forward ranks.
- `gap`: scalar or `[horizontal,vertical]`, default `[100,90]`, minimum 24 scene units.
- Root `origin:[x,y]`: layout-area top-left, not a restriction that all global coordinates be nonnegative.

Every node and group must be placed exactly once. **DSL groups are layout regions, not native `groupIds`/frames**. Compound polygons/tables are editable multi-object constructions; dragging only one outline in the GUI is not guaranteed to move the entire compound. The existing native grouping API remains available outside this authoring contract.

### Ports and routes

Endpoints are `node`, `node.left/right/top/bottom`, or `node.named_port`. Port values are `side` or `side:fraction` with fraction 0..1. Unknown names fail instead of silently connecting to center. Named ports become native markers plus fixed-point bindings; they are not electrical pins or an RTL netlist.

Edges have stable IDs and from/to/label/kind/class/style/via/label_at. Kinds are data/control/feedback/line/ppt. Automatic routing reuses the native package's orthogonal obstacle router; it is not a globally optimal bus optimizer. Explicit `via` points are global scene coordinates and must make orthogonal segments without crossing unrelated nodes. `label_at` is a 0..1 position along the route. Labels and saved routes still require current PNG inspection.

## Incremental state and safety

Private state lives below the existing state directory, under `scene-dsl/<connection-scope>/<state-id>.json`. It holds the target file, generated native ID mapping, prior descriptors and fingerprints, **not bearer credentials**. Retain it when upgrading. Identical source is a true no-op; semantic changes reconcile the managed subset, and omitted owned edges/nodes are deleted deliberately. Unowned content is not rewritten.

An external change to managed position/text/style/binding/resource/lock/customData causes a conflict. Do not use raw apply on managed objects and expect the next DSL render to adopt that edit silently; there is no automatic GUI→DSL merge/adopt command. Unowned objects are preserved but are not all compiled as layout obstacles, so full-scene checks and PNG inspection remain necessary.

Changing a construction/resource kind or an image/formula/embed source requires an explicitly new logical ID. Adding a previously absent bound label also requires a new logical ID. Rows/cells use positional identities, not stable database row keys. The compiler is not a replacement for Table Engine row/column interaction features.

Concurrent operations on one state ID fail rather than racing its state file. After a process crash, inspect its PID/current scene before deliberately removing the `.lock` file; there is no blind stale-lock retry. Native base revisions protect the final commit. The identity receipt is saved before inspection/export; a later failure can leave a committed drawing. Plan, native transaction, local state, PNG and review are not one distributed atomic operation.

Limits: 512 KB source description, at most 100 logical nodes+edges, table 12 columns/20 data rows, 450 explicit initial operation descriptors, 500 incremental operations. These are supported package boundaries, not Excalidraw maximum canvas or PNG limits. Font/resource availability, export scale and native endpoint rounding are host-dependent.

## Examples and boundaries

[Real gallery](gallery.md) links source YAML, native example canvases and actual host PNGs, including a dense Tomasulo illustration. Diagram size is evidence of that example, not an automatic correctness or aesthetics score. Hardware examples explicitly omit implementation details; the DSL does not prove electrical connectivity, cycle behavior or RTL correctness. Interaction, animation, library-specific contracts, arbitrary customData and additional backends remain on their existing native paths, not silently approximated by this DSL.
