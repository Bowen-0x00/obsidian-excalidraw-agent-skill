# Changelog

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
