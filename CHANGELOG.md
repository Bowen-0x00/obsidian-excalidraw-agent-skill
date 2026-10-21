# Changelog

## 0.10.2 — Executable start, native input, topology and delivery gates (2026-10-21)

- Add drawing_begin with actual bundled Skill/task-reference content and hashes, current host discovery and optional existing canvas/review evidence; preparation does not create or modify a canvas.
- Expose native op-discriminated Pydantic input models and validate the full batch before HTTP for MCP, Python and CLI. Keep feature/customData execution checks at the host; do not alias invalid historical operations.
- Require declared component/port/signal representation for hardware tasks; map saved native IDs with drawing_contract and recompute body types, world ports, endpoints, bindings and orthogonality at check/review/delivery. Text cannot replace a declared body. Unsupported exact geometry is explicit, not waived as an overlap.
- Add drawing_deliver: require same owned file/current revision/full registered PNG/hash, completed review and current requirements/topology. Preserve raw check status/advisories and trust limits; successful writes or exports are not completion.
- Existing Bridge/bootstrap remain 0.13.7; this runtime/Skill change does not require restarting or replacing host scripts. Upgrade the package and reload MCP/Skill to discover the three new tools. Preserve private connection, task/DSL state, user canvases and historical package snapshots.
- Verification: 115 runtime tests and 7 shared-sync tests passed; 15 shared Engines checked. Real stdio MCP rejected invalid batches before mutation and blocked text-only hardware delivery; native topology passed, a deliberately shifted signal invalidated delivery, and same-ID repair/rebind retained review history. The actual final PNG was viewed and high review completed; CLI delivery succeeded. Redhat discovered 21 tools and the same 36 native operation models through the real host connection.

## 0.10.1 — Semantic LaTeX routing and math-specific visual review (2026-10-20)

- Route mathematical matrices, vectors/transposes, fractions, sums, recurrences and structured scripts before font choice or generic text helpers, even when input contains no dollar delimiters. Reject ASCII-space matrices and Unicode/offset-text imitations in the Skill workflow.
- Keep RTL identifiers/slices, literal code, bitstrings, pin names and waveforms as editable native text/geometry. Separate Chinese prose from source-preserving native LaTeX resources; measure real formula bounds, scale uniformly, group mixed content and preserve owners/bindings during local replacement.
- Add math-specific requirement/PNG review: exact saved TeX, real image/fileId resources, matrix shape/brackets, script ownership, sum bounds, fraction/root structure, mixed baselines and readability. Numeric verification and label-copy assertions do not certify typography. This is Agent guidance, not a new automatic semantic parser or runtime enforcement claim.
- Real-host verification created eight formula resources for GEMV matrices/vectors, transpose, sum, recurrence, mixed prose and a fraction/root. Source TeX round-tripped exactly, resource geometry matched native measurement, literal RTL/bit labels stayed text, and actual PNG high review completed. Existing runtime/Bridge APIs remain unchanged; bootstrap and Bridge stay 0.13.7.

## 0.10.0 — Choice-first drawing, strict review and matched startup (2026-10-20)

### Bootstrap and upgrade

- Update every active managed bootstrap together with its paired Bridge to 0.13.7. Start reports the actual version/path and rejects mismatched runtime identity; retain 15 declared feature Engines and do not restart retired table hooks.
- New drawings/native writes require a cited drawing brief; reviews require per-user-requirement evidence. Installation smoke now takes an explicit discovered `--font` and adopts its documented fixed diagnostic design, rather than silently bypassing the new contract.
- Upgrade package/marketplace/Python lock metadata to 0.10.0. Preserve private connections, DSL state, user canvases, customized scripts and archived version snapshots.

### Choice-first drawing and enforceable review evidence

- Make unresolved style and review depth first-class questions before creation; retain per-choice user/answer/inherited/delegated provenance in a required drawing brief, alongside the user's content requirements. Read/discovery stay available without a brief.
- Bind tasks to one canvas and persist review history across context-token changes. Reject recreating an already-started task, silently replacing unresolved requirements, and lowering a task's selected review depth. This is workflow bookkeeping, not verification of user dialogue or a sandbox against arbitrary trusted code.
- Bridge 0.13.7 rejects unknown/misplaced operation, style and label fields before staging any batch element. Native text creation and measurement share the host's `refreshTextDimensions`, including the actual requested line height.
- Require current native IDs and per-requirement coverage at review. Text-conflict exemptions cannot be intentional; false positives need registered readable detail PNGs and specific matching IDs. Reject duplicate blanket reasons and retain raw diagnostics even when a justified candidate is adjudicated.
- Smoke-exercise an isolated real Obsidian host: wrong fields leave the scene unchanged, 13-point Chinese text measures identically to committed geometry, blanket waivers fail, rebind retains history, local repair preserves every native ID, and the inspected final PNG passes high review. Runtime regressions cover the corresponding boundaries.

### Refresh long-lived Bridge connections

- Re-resolve unpinned URL/token/timeout settings before every request, so a live MCP follows an intentionally updated private connection instead of retaining stale credentials while setup reports connected. Explicit constructor/environment overrides retain precedence; malformed config fails closed and failed writes are never retried.
- Reproduce the stale-connection bug with real loopback HTTP services, then verify connection rotation and explicit-override/error boundaries. Document cwd-versus-vault selection, unavailable automatic startup, ownership-conflict handling and the prohibition on forging installation hashes or mining historical tokens.

### Opt-in read-only CDP diagnostics

- Add `drawing_debug(status|inspect)` and `launcher.py cdp -- status|enable|inspect|disable`. Default is off; explicit user CLI opt-in pins a numeric-loopback debugger endpoint and exact host vault. MCP cannot enable it, accept arbitrary JS/protocol commands or mutate a drawing.
- Read fixed scene/paint/text/binding/table/image-reference/canvas/viewport snapshots plus renderer event counts through short CDP sessions. Require an already uniquely open file, validate vault/target identity, deny redirects/retargeted sockets, and use V8 `throwOnSideEffect` with no unguarded fallback. No input, navigation, pause, save/export, plugin changes or raw console arguments.
- Route unexplained PNG/rendering problems to the optional diagnostic workflow. Skill and both READMEs distinguish observed state from hypotheses; any authorized fine-tuning uses fresh normal Bridge/API/DSL state followed by actual PNG/review, never CDP writes.
- Keep diagnostic opt-in client-private and disabled for existing/remote installations. The unrestricted Electron debugger is not a sandbox or made read-only by this adapter; no host/plugin/Bridge script change or automatic debugging-port/SSH setup.
### Four arrow path styles documented

- Document the actual `sharp`, `round`, `elbow` and modified-fork `curveArrow` path renderers separately from arrowhead types. Specify fields, selection semantics, S-curve limits, bindings, readback and PNG/unknown geometry acceptance.
- Clarify that `routing:"curve"` is not a public alias for the fork's `customData.curveArrow`; no arbitrary Bezier/control-point or obstacle-avoidance guarantee is added. Keep microarchitecture signals on sharp/elbow by default.

### Event-driven synchronization

- Remove the six-hour shared-Engine synchronization schedule. Retain upstream push notifications and manual workflow dispatch; missed notifications require a manual catch-up rather than periodic polling. Import validation and PR policy are unchanged.

### Retire the upstream table hook Engine

- Remove the retired `Feature-Table-Engine.md` from the shared import manifest/lock, bundle inventory and bootstrap, and delete its bundled copy. Scripts `3a1f79f` moved table interaction to the host plugin; the obsolete required input caused scheduled shared-Engine synchronization to fail.
- Keep missing-input and shared-copy drift protection intact for the 15 remaining Engines. Native tables continue through host capability discovery; legacy `create_table`/DSL grids are unchanged. This change does not deploy to vaults or unload already mounted hooks.

### Diverse README and native table themes

- Retain the RISC-V showcase and add five different forms/domains: handwritten water-cycle landscape, dark calculus geometry with real TeX, transit wayfinding, mint Gantt planning and an academic ecology results page. Keep earlier examples in the gallery; include authored sources, editable canvases and actual PNGs.
- Add `drawing_table(create|style)` and Python `DrawingClient.table`, backed by Bridge 0.13.6 `/v3/tables` and the paired host `TableManager`. Discover `nativeTable.callable`, use the host's eight theme/five border IDs, preserve native semantic cells and bound text, and report non-atomic saves/partial failures. Older hosts fail explicitly; legacy create_table/DSL contracts are unchanged.
- Exercise native theme/border application without changing IDs/content/geometry, reject stale revisions and invalid requests before mutation, and verify omitted-font creation returns a real PNG through stdio MCP. Preserve native table order above page backgrounds; do not copy palettes or simulate table borders.
- Five final medium PNG reviews completed. Landscape/point superpositions and the river curve retain specific visual dispositions, not a fake raw-geometry pass. All five CLI sources ran on real hosts; 78 runtime regressions and the 16 locked Engine checks passed.
- Native table appearance was rendered in the existing isolated paired development host. This Agent change is not a host plugin/Extras release and does not replace the personal-vault plugin or rewrite shared Table Engine scripts.

### Advanced native showcase gallery

- Lead the English/Chinese READMEs with real five-stage RISC-V, disaggregated inference and 4×4 matrix-engine diagrams. Keep the six DSL examples and explicitly distinguish DSL compilation from Agent-authored Python/native API drawing.
- Include the executable source, editable native canvases, actual overview/detail PNGs and scoped provenance. Exercise all three builder CLI entrypoints against the real host; verify declared endpoints/reciprocal bindings and inspect readable details rather than treating an overview or check pass as complete visual proof.
- Preserve 68/32/66 declared connections while correcting port roles, control D/Q boundaries, independent signal tracks, labels and drain-phase semantics. These are authored teaching/reference illustrations, not an automatic hardware layout engine, complete ISA implementation, production benchmark or simulator. No Bridge/shared Engine/DSL runtime change.

## 0.9.0 — Optional scene DSL and real editable example gallery

- Integrate the measured YAML/JSON compiler as `runtime/scene_dsl`, served by one new `drawing_dsl(plan|render)` MCP tool and `launcher.py dsl` CLI. Preserve all existing compose/native/library/presentation and CLI paths; retire the independent experiment runtime instead of maintaining a second implementation.
- Compile spatial row/column/grid/flow regions, native sharp-cell tables, named ports, polygons and source-backed resources through existing APIs. Private connection-scoped state keeps native IDs, no-op submissions, explicit diff/deletion and external-edit conflict protection; plan remains read-only and render returns actual PNG rather than visual approval.
- Share execution/state/error semantics across MCP and CLI, lock concurrent state access, reject YAML aliases/cycles/nonfinite data, refresh bound labels during geometry changes and remove obsolete owned visual overrides. Preserve post-commit receipts when inspection fails; no automatic adopt/GUI-to-DSL merge or general electrical correctness claim.
- Rewrite English/Chinese READMEs around natural language, ordinary compose, repeatable DSL, precise native edits, automation and remote rendering. Publish six genuine PNG/YAML/native-canvas examples with scope/provenance, complete DSL and maintenance guides, and focused Skill routing rather than loading every reference.
- Verify 78 runtime and 7 importer behavior tests, real stdio MCP image return, six freshly rendered examples and same-source zero-op submissions, same-ID label updates, unowned-content preservation, external-edit refusal and read-only planning. Native tables/resources/bindings and actual PNGs were checked; installation and remote-update evidence is recorded separately.
- Include the reviewed upstream ECharts 1.3.0 shared snapshot and preserve its source lock; no independent Table Engine or plugin renderer rewrite.

### Table styling, ECharts 1.3.0 guidance and hardware DSL lessons

- Separate table cells from rounded node cards: explicit sharp corners, continuous thin grids, contrasting headers/bodies, measured column widths and native bound-text styling. Keep the current create_table/metadata contract; no Table Engine change.
- Document the 16 published ECharts examples, 12 visual types plus custom, multi-series/stacked/dual-axis/XY data, schemaVersion 2 edit roundtrips and own-options SVG export. Advanced Agent charts use current Bridge custom/options rather than unsupported UI enum values; shared source, bundled copy and mounted Engine versions remain distinct.
- Distill the real hwdiagram/1 datapath's body/port alignment, native symbol contracts, semantic fanout, separate control/feedback channels and style-dependent remeasurement. Reject recipe-specific hardcoding, schema-only implementation claims and obsolete crossing masks; leave the user's existing reference canvas unchanged.
- Real Obsidian smoke preserved all IDs/table metadata while styling 33 native cells and unequal columns; dual-axis mixed and custom heatmap PNGs were complete and visually reviewed. The reference hardware canvas was read/rendered only; 16 existing chart examples and editor screenshots were inspected, not all interactions rerun. No Bridge, Table Engine or renderer code changed.

### Shared Engine source locking and automatic update PRs

- Declare the 16 shared Engine source/target mappings and LF-normalized content/version locks. Preserve the legacy snapshot without inventing a source commit; imported updates pin a real published source tree.
- Add manifest-aware Scripts push notifications and a target receiver with manual/scheduled fallback. Validate all inputs before import, reject shared-copy drift/deletions/renames, skip unrelated/no-op updates, and reuse a scoped bot PR without overwriting human edits.
- Add nonexecuting JavaScript syntax checks, isolated importer behavior regressions and secret-free integrity CI. Source code is never executed merely because it was published upstream.
- Keep Agent Bridge/bootstrap ownership, package release, vault deployment and loaded-Engine compatibility as separate responsibilities. Document scoped encrypted credentials, rotation and the real-host acceptance gate.

## 0.8.17 — Tiered, visual-first diagram acceptance

- Add low/medium/high acceptance, default medium and independent of model effort. User prompt/choice flows resolve the same acceptance_level parameter across MCP, client/CLI, inspection, checks and persistent review. High deepens content/connection/style inspection without universal mandatory bindings.
- Detect native text-line overlap, later paint covering text, shafts/borders through text and thick-shaft proximity; account for paint order, opaque panels, hidden/deleted elements and native own-arrow label masking. Geometric boxes remain candidates, not fabricated glyph/pixel proofs.
- Require content/readability/occlusion visual check outcomes at medium/high and connection/hierarchy-style outcomes at high. Specific current-PNG adjudications can accept legitimate composition or false positives while retaining findings and reasons. Structural and explicit semantic failures cannot be waived.
- Retain prior semantic assertions when review omits check_result, validate detail preview state/completeness, and use actual output scale for advisory small-text triggers rather than hardcoded font-size rejection. Preserve revision guards and finite/no-progress stopping rules.
- Real native-canvas counterexamples exercised legal background containment, opaque masking, an unbound pointer, line-through-text, font/spacing collisions and overpaint. Two targeted repair passes preserved all 26 IDs; high review completed only after actual PNG checks. A separate whitespace intersection was accepted with explicit visual evidence, not by muting all overlap checks. A real long-Chinese branching flow also passed the new MCP inspection path.
- Existing and new behavior regressions cover level persistence, checklist gates, non-waivable errors, geometry boundaries and stopping limits. No plugin/kernel/shared Engine snapshots were modified.

## 0.8.16 — Editable PPT block arrow sizing

- Add general-purpose filled/outline block arrow selection and sizing guidance for flow, architecture, teaching and comparison diagrams. Separate path length, scene-unit shaft width, head scale and outline stroke; include short/wide versus long/slim examples and same-ID width-only edits.
- Update the current renderer contract: blockArrowWidth controls shaft thickness; arrowHeadSize scales the block head, with native length capping. Both variants accept explicit backgroundColor/fillStyle. Document visual-envelope, spline/orthogonal, clipping and high-level customData forwarding limits rather than treating centerline checks as thick-arrow proof.
- Bridge 0.13.5 adds block_arrow to the existing arrowhead whitelist/schema and updates the PPT recipe. Width uses existing patch_custom_data, not a new set_arrow_style field or a second renderer.
- Explicitly distinguish strokeColor from backgroundColor/fillStyle on both PPT variants and ordinary thin-arrow line color. Real native PNGs verified separate dark outlines and light fills; width-only updates retained the original IDs, centerline points, labels, styles and bindings. Visual acceptance remains separate from metadata/binding checks.
- Real bound-arrow PNGs also exposed a host export alignment discrepancy: at shaft width 36, the visible shaft center was about 36 scene units below the unchanged native centerline. Record this as a visual compatibility issue rather than marking the sample completed or moving binding ports to hide it; no plugin/kernel renderer was modified.

## 0.8.15 — Host-discovered fonts and Agent-selected text roles

- Add a generic typography workflow: complete current-host discovery, task-scoped evidence/unknown inventory, bounded candidate sampling, language/role selection, explicit family measurement and application, and saved-text/PNG verification. No local font catalogue, mandatory font-file access, new classifier or typography DSL.
- Preserve explicit user fonts and existing drawing styles; distinguish proportional/monospace/tabular digits, handwrite/code/display roles, registration/loading/coverage/fallback, and missing-font limitations. Explain single-font planner limits and measured native operations for mixed roles.
- Remove assumed font names from Skill defaults and selection examples; code primitives must receive the Agent's resolved family instead of relying on their historical default. Add typography guidance to existing context/measure tool descriptions.
- Bridge 0.13.4 obtains exact family names from the active package's getFontFamilies() when available. Existing fonts.registered remains the result field; source identifies native versus legacy registry evidence, and error reports failed/unavailable discovery rather than an apparently successful empty list.
- Real-host verification exposed a first-measurement font-loading race: the same selected code family initially measured narrow/wide samples differently; after render, both measured 93.75 at size 20 and stabilized. Add bounded readiness/sample-render/remeasure guidance instead of classifying from a cold measurement.
- Exercised native prose/code/identifier/annotation/Chinese samples and a same-ID bound-text font change; text and relationships were retained, checks passed and PNGs were inspected. Synthetic host-list/failure boundaries are separate smoke evidence, not claims of a second real host's font rendering or per-glyph fallback detection.

## 0.8.14 — Hardware production loop and orthogonal signal routing

- Distill the actual component/port-first workflow into gated stages: intent contract, fixed geometry, components, signal batches, post-save audit, bounded previews and minimal repairs. Reject duplicate graph replay, layout simplification and check-only completion.
- Require axis-aligned hardware signal segments and a separate full-precision saved-point audit. Distinguish symbol outline diagonals from wires, element angle from segment direction, and explicit orthogonal polylines from native automatic elbow mode. No new hardware router or built-in checker assertion is claimed.
- Actual CPU repair found seven two-point diagonal arrows among 73 signals. Blind native-elbow conversion caused three node-crossing errors; explicit four-point H–V–H polylines preserved the port bindings and endpoint coordinates and passed the existing 227 assertions. All 351 element IDs and unrelated geometry/styles were retained. Overview and 1.6x detail PNGs were inspected; overall density remains a documented limitation, not a completed professional-quality claim.

## 0.8.13 — Hardware-specific planning and honest acceptance

- Route CPU/pipeline/datapath/array/cache requests to microarchitecture.md before creation. Separate hardware components, named ports, signal classes, timing boundaries and fixed stage geometry from ordinary service-graph layout.
- Require real ALU/MUX symbols or editable native polygons, explicit data-versus-select inputs, forwarding value sources, RF/memory ports and readable bounded previews. Explain existing planner/schema limits rather than inventing a hardware layout engine or electrical DSL.
- Prohibit stage-bullet substitution, dropped feedback networks, duplicate compose replay, unconditional rebuild/revert and check-only completion claims. Record partial execution, explicit semantic assertions, visual readability and actual repair limits; retain review/preview revision guards.
- Actual full CPU verification exposed rectangular symbol fallback, missing data inputs, ineffective closeups and save-time text-ID normalization. Tighten guidance with concrete op/ref, signal-selection mapping, post-save readback and local preview rules.
- Targeted real-canvas repair retained the original 113 element IDs and 48 arrows, adding seven native polygon symbols and explicit ports/networks. Final geometric/binding checks covered 351 elements and 227 assertions; 1.6x bounded PNGs were inspected. The diagram remains visually dense and the ledger remains continue, not completed; this is evidence for the workflow and its limits, not a claim of automatic professional-quality hardware validation.
- Existing 27 regression checks passed. No host plugin renderer, hardware automatic layout, script execution permissions or user's original business CPU drawing was changed.

## 0.8.12 — Preserve label readability on the fast path

- Measure edge-label widths before automatic LR rank placement and reserve actual label space. Center labels on ordinary two-point links; preserve explicit labelPosition and decision/multi-segment placement rules.
- A visually inspected Gemini run exposed labels overlapping endpoints despite check=pass. Preserve that run as a quality miss, not a successful quality-equivalent timing sample.
- Verified the same generated labeled graph using actual host measurements: both labels remain between their endpoint nodes with at least 16 scene units of clearance; all content and bindings retained.

## 0.8.11 — Make the fast-path operation contract explicit

- Distinguish operations[].op from expected[].type with a complete title-bold example in the Skill and MCP description. Avoid an invalid operation followed by broad reference searches.
- Keep already-specified ordinary graph styles on the concise path; advanced references remain available only when their capabilities are actually needed.
- Preserve the first Gemini 0.8.10 measurement, including its slower invalid-parameter recovery, rather than presenting it as a speedup.

## 0.8.10 — Fewer round trips without weaker drawing checks

- Prefer existing drawing_compose for ordinary measured native graphs as well as library composition, keeping plan→apply inside code instead of copying operation JSON through the model.
- Add optional inspect=true and expected assertions to drawing_compose/drawing_apply. Return real PNG ImageContent, complete same-revision canvasSummary, full structure/geometry/semantic checks, original commit receipt and measured phase timings. Default false retains the old result. Visual review remains separate and rechecks current state.
- Preserve committed receipts as structured MCP errors when inspection/export fails after mutation; reject changed revisions and keep diagnostic failures visible rather than marking completion.
- Reduce the default Skill entry by moving detailed concurrency/summary/operation rules into workflow-details.md; retain all advanced routes and quality gates. Batch related schema reads and progress with real work, avoid repeating the visual questionnaire for specified styles.
- Verified actual Obsidian stdio composition/inspection, semantic failure visibility, stale-write rejection, committed empty-export failure receipts, undo and legacy result shape. Existing 27 behavioral regressions passed.

## 0.8.9 — Visual choices, semantic arrows and fixed corner radii

- Ask once at new-drawing startup for unspecified visual preferences using the client's real selection UI: native style, palette/strict allowed colors, background/lightness, categorical versus grayscale encoding, and installed font/title-weight strategy. Reuse explicit/session choices, preserve local edits, and honor “decide for me”; no fictitious Obsidian/MCP style dialog.
- Define palette-to-native-property mapping, contrast checks, font discovery, bold text IDs, neutral/background allowances and image/library exceptions. Morandi/dark/grayscale are workflows, not invented profile names; planner defaults do not automatically enforce a strict palette.
- Select triangle data-flow heads, sparse PPT-wide block outlines, lightweight controls and UML-specific endpoints by semantics. Document head/body/routing distinctions, actual whitelist, blockArrowWidth, outline background behavior, labels/bindings and envelope limitations.
- Document fixed rectangle roundness {type:3,value:6,roundType:"arc"} and elbow values {type:2,value:0|6|24}; preserve small radii across ordinary resize instead of relying on adaptive large corners.
- Bridge 0.13.3 removes duplicate arrow validators whose missing return erased set_arrow_style endpoint values. Keep the existing host create_linear.elbowed handling; actual head changes now retain native IDs, geometry, bound labels and endpoints, and unsupported head types still fail.
- Verified real PNGs for semantic arrows, fixed/zero/adaptive corner radii, and five native palette/font/weight variants. Corrected low-contrast Morandi/grayscale borders using the allowed neutral palette; existing regression suite passed.

## 0.8.8 — Explicit mixed-text LaTeX rendering workflow

- Reject literal math source in ordinary text/labels as a completed formula. Route mixed prose through the existing host latex/Action-Extract-Latex.md or existing native text+create_latex composition; no new parser, DSL, script allowlist or pretend MCP tool.
- Document real Action behavior and boundaries: selected text only, single/double dollar parsing, measured fragments, source TeX resources, replacement IDs, no automatic wrapping/frame/group/binding migration, unawaited writes and behind-background stacking. Verify prerequisites, preserve originals during conversion, repair relationships/stacking, and inspect actual formula PNGs rather than trusting geometry pass.
- Expose these boundaries in measure/plan/apply/check MCP descriptions. Preserve the user's original Action source and existing business canvases.
- Verified the actual host Action on single-line/multiple-formula, multiline Chinese and double-dollar inputs: five real formula images with retained TeX. Verified safe replacement of a bound node label, group/frame restoration and actual stacking repair while preserving owner/downstream/arrow IDs, geometry and binding targets.

## 0.8.7 — Size-aware library workflow and remote PNG inputs

- Require source bounds/frame inspection and an explicit target size before placing presentation templates or circuit symbols. Distinguish numeric library scale, relative native selection factor, single-element resize, layout allocation and PNG export scale; preserve aspect ratios and complete instance membership.
- Surface sizing guidance directly in apply/library/compose/present MCP descriptions. Keep existing execution APIs: no new resize DSL, no silent auto-fit, no frame-only or transparent-anchor-only enlargement. Presentation scale is top-level; differing source sizes require separate sizing.
- Verified through actual Redhat stdio MCP: a native library frame grew from 648.12×431.88 to 1280×852.93 with its decorations; editable SVG ALU 60×45 → library scale 2 → 120×90 → relative factor 2 → 240×180 retained its source, native IDs, anchor and updated external binding. Single resize produced 160×64 with font size 20 unchanged. A populated page scaled and restored with all text/IDs/internal bindings retained; final hard checks and inspected PNG passed.
- Document remote PNG byte transport through existing data:image create_image inputs, total 4MiB request budgeting and independent page image/text editability. Two real remote PNGs persisted as host attachments with matching SHA-256; image/text/frame PNG inspection and review completed.

## 0.8.6 — Native Visio-style line crossing guidance

- Route arc/gap/dot/none through the updated host's native customData.lineCrossings with existing create_linear/connect/patch_custom_data operations; stop using white/background masks, manually drawn bridge arcs/dots or split wire geometry to simulate crossings.
- Document paired numeric lineJumpPriority, planner/primitive metadata forwarding boundaries, semantic versus binding distinction, full-scene PNG verification and safe migration of identified legacy decorations.
- Verified actual native rendering on colored background and bound elbow arrows, metadata-only changes retaining IDs/points/bindings/counts. Keep the observed T-junction PNG-dot limitation explicit rather than claiming every case works.

## 0.8.5 — Lean summaries and explicit deployment verification

- Omit per-element version from default read/PNG summaries: mandatory canvas baseRevision already protects normal writes. Native versions and optional expectedVersion remain available in full element reads.
- Clarify native new-tab versus new-pane: dedicated tabs avoid the installed plugin's adjacent-pane reuse policy; deliberate manual split views remain useful without changing user preferences.

## 0.8.4 — Compact coordinate feedback and concurrent canvases

- Return complete scene summaries with native world minX/maxX/minY/maxY bounds, file/revision/count/coverage and feedback-only two-decimal coordinates. Preserve exact values in full reads; flag capped text, summarize dense geometry by pointCount and omit empty optional fields.
- Include the all-canvas compact summary alongside each PNG at the same revision, with sceneOrigin/scale for pixel-to-scene adjustments. Summary/get/query/render/undo require an explicit canvas token.
- Scope undo lookup to the target file's latest transaction rather than the Bridge-global latest transaction, retaining revision protection and the existing shared 20-transaction history limit.
- Open created or rebound canvases in explicit native new tabs: the host's new-pane path can reuse an adjacent view and invalidate an earlier Agent context when a third canvas opens.
- Document separate-file Agent ownership, shared serial execution, same-file revision conflicts and one-time coordinator setup. Verified real concurrent clients, stale-write rejection, cross-file undo, unchanged native precision, negative/rotated bounds, empty/deleted scenes and bounded dense-stroke/long-text feedback.

## 0.8.3 — Native selection rotation and scaling

- Added Bridge 0.13.0 rotate (relative signed degrees, clockwise positive) and scale_selection (uniform factor, center or corner anchor), using the installed editor's actual manual transform handler against an isolated native Scene before transactional commit.
- Absolute patch_element.angle remains radians and now updates bound text and attached arrows through the native rotation path. Preserve native IDs, groups, frames, SVG paths and freedraw pressures; reject locked affected elements, Frame rotation and partial-arrow binding changes rather than silently detaching relationships.
- Added world-coordinate quarter-turn geometry checks; arbitrary angles and curved paths remain explicitly unsupported by the existing exact-check scope. Documented the staging boundary: host afterTransformElements Engine hooks are not replayed.
- Verified real Obsidian group rotation by 90°, 1.5× scaling with text 20→30 and unchanged external node, single-node absolute rotation/scaling, SVG/freedraw/frame children, staging failure, locks and undo; inspected actual PNGs.

## 0.8.2 — Real style showcase and waveform export readiness

- Ran OMP with the installed Skill to create eight editable diagrams across Visio architecture/UML, Rough.js flows, professional swimlanes, blueprint library composition, native freehand strokes and a presentation containing WaveDrom/code/callout. Actual PNGs were inspected; architecture layout and MUX input ports were repaired in place.
- Fixed WaveDrom cold-cache export: use the real Engine image with bounded readiness wait and contain scaling, or return complete=false with a resource issue. Export leaves the native carrier and source unchanged.
- Discover roughjs/rough-js as aliases of handdrawn; keep handdraw/freehand requests on native draw primitives rather than inventing a second renderer.
- Tightened Skill guidance for planner spacing bounds, package/config selection, real library stub coordinates and review accounting across reconnection.
- Added reproducible showcase/GIF prompts and a source-backed next-ai-draw-io comparison; user assets and private run artifacts stay outside the public package.

## 0.8.1 — Clear multi-Agent setup and portable terminology

- Reorganized both READMEs around prerequisites, Agent installation, Obsidian connection, natural-language use and user libraries; OMP is an example, not a dependency.
- Added source-backed Claude Code/Codex Skill and stdio MCP instructions, with client-specific commands, state-sharing rules and the current OMP-specific remote deployment boundary.
- Replaced the personal script folder name in public guidance with drawing script directory and relative source paths; actual host directories and runtime compatibility defaults are unchanged.
- Made Skill references portable local paths, with skill:// access optional for clients that provide it.
- Documented library-update behavior: requery current items and refresh user-maintained metadata/catalogs; do not copy user .excalidrawlib files into the Skill.

## 0.8.0 — Drawing-script capability coverage

- Added Skill references for trusted URI/EA execution, web-image acquisition and native asset insertion, interaction/navigation engines, visual effects/lists, mindmaps/WaveDrom/GIF/Git boundaries, layout/arrow/animation and Anki/Eagle export.
- Documented which features are Bridge adapters versus host-only Engines/UI actions, including hover, line highlight, zoom hide, detail, checkbox, layer, outline, thumbnail, Smart List, Bullet, shadow, callout, code highlight and animation.
- Corrected the Bridge mindmap state contract from `closed` to the installed Engine's actual `close` state; stale `closed` requests are rejected instead of silently diverging.
- Verified in an isolated real Obsidian host: official Python image download to a vault attachment/native image, checkbox Shift-click, selection-mode hover, zoom hide transitions, mindmap layout/collapse, WaveDrom/callout/code/shadow PNG and arrow-animation pixels across frames plus stop cleanup. Final full PNG was inspected with zero diagnostics and completed review; all 24 regressions pass. Optional thumbnail UI opened; detail/outline/thumbnail navigation and other unexercised host actions remain explicitly limited.
- Added SVG-path component authoring from both real Digital/Microarch generators: native DOM bounds, normalized path/viewBox versus target size, line carriers, grouping/labels/anchors and per-component library boundaries. Verified two native grouped components, negative coordinates, curved/arc paths and full inspected PNG; do not treat the source scripts' regex shifter as a universal SVG parser or copy their destructive whole-canvas rebuild into general editing.

## 0.7.0 — User-maintained library descriptions and catalogs

- Preserve optional item/library description metadata in Bridge library summaries; include descriptions in item search and distinguish missing metadata from empty text.
- Discover user-maintained library-index.md alongside vault libraries and expose bounded catalog reads through drawing_library without requiring a canvas for discovery.
- Add local metadata-only inventory/apply commands with exact-ID proposals, source-hash checks and original-byte backups; preserve elements, resources and unrelated fields.
- Provide a copy-paste Agent prompt and Skill reference for inspecting multiple libraries, incorporating user notes, writing descriptions and maintaining an editable summary.
- Keep catalog/description contents as untrusted selection data, not execution instructions or visual proof. Native UI search remains name-based.
- Verified a real 11-item circuit library copy in isolated Obsidian with the installed ymjr 2.27.3-1 build and Bridge 0.11.0: metadata-only edit and original-byte backup, catalog discovery/read, description-only search with cache refresh, native item restore/export retention, native ALU insertion and inspected complete PNG. Final review completed in one round with zero diagnostics; all 44 original library files remained hash-identical. Twenty-four regressions pass.

## 0.6.1 — Native CLI guidance and documentation

- Teach the Skill to choose between the drawing MCP, the plugin's native terminal CLI and in-process `ea.executeCLI()` without mixing operation schemas, revisions or preview receipts.
- Document the ymjr command prefix, runtime prerequisites, numeric native font IDs, paged reads, request replay/recovery, save outcomes, trusted-script lifetime and PNG export limits.
- Keep the Bridge-based layout/diagnostics/remote PNG workflow as the default for full diagram authoring; native CLI is an optional plugin feature, not a replacement remote service.
- Rewrite English and Chinese READMEs around installation, local use, remote use, native CLI, updates and troubleshooting.
- Verify in-process native create/open/read/apply/export against the actual 2.29.0-1 build: saved edits, identical-request replay and stale-write rejection. Terminal handler invocation remains unverified on the installed host because its console CLI launcher is unavailable.

## 0.6.0 — Headless remote drawing over SSH

- Add host-side `remote-deploy` and `remote-tunnel` commands to provision a remote Python MCP/Skill and an isolated loopback-only SSH reverse tunnel without reusing unrelated user forwarding/X11 settings.
- Transfer credentials only through encrypted SSH stdin into remote private 0600 configuration; preserve existing OMP model/auth/settings, other servers and customized managed files.
- Add remote setup mode: show the host rendering target and tunnel status, reject vault deployment/GUI startup on the headless client, and store returned PNGs/review evidence on the remote machine.
- Preserve native host-vault editing and existing MCP ImageContent delivery for remote model inspection without a GUI.
- Verified real headless Redhat OMP creation of a host-vault native Chinese approval flow, PNG ImageContent/file delivery back to Redhat, visual inspection and same-token local repair; final review completed at round 2/5 with 18 active elements and zero diagnostics. Twenty behavior regressions pass; remote credentials are 0600 and existing model/settings fingerprints remain unchanged.

## 0.5.0 — Complete drawing runtime and first-time connection

- Bundle the real MCP server and all native planning, geometry, resource, library, composition and review modules instead of requiring a separate private executor.
- Add standard Agent Plugins metadata and a credential-free MCP launch using uv and locked dependencies; register 15 tools including `drawing_setup`.
- Package Bridge 0.10.0, a dependency-ordered bootstrap and 16 Feature Engines, retaining third-party license notices for offline embedded libraries.
- Deploy into an isolated Agent-Drawing script subtree, preserve unrelated/customized files and plugin permissions, generate credentials outside the vault, and return authenticated startup status.
- Persist preview receipts and ledgers outside the versioned package/cache and working directory; use portable native fonts and discovered library sources.
- Replace Skill-only installation instructions with complete bilingual installation, first connection, upgrade, CLI, privacy and troubleshooting guidance.
- Verified 18 consumer-visible regressions, all 18 host-script syntax paths, real stdio MCP initialization/tool discovery, an independent clean Obsidian vault without existing user Engines, and actual editable Chinese diagrams/PNGs. Cold-host review completed in one round; marketplace Agent drawing required a parent visual branch-routing repair and completed at round two.

## 0.4.1 — Global Skill distribution

- Package the existing drawing workflow and two reference files as a user-scope OMP marketplace plugin; execution tools remain a separately configured dependency.
- Replace project-relative CLI assumptions and machine-specific library paths with explicit runtime installation and real library discovery.
- Add linked English and Simplified Chinese READMEs covering installation, updates, removal, natural-language use, execution prerequisites and public plugin/source links.
- Add an MIT license and an explicit public-file allowlist. Exclude credentials, MCP configuration, user drawings, assets, previews, ledgers, logs and local runtime files.

The 0.4.1 release was Skill-only; 0.5.0 supersedes that scope with the complete execution package. Native Excalidraw frames remain editable presentations, not an unimplemented PPTX exporter.
