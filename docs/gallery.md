# Real drawing gallery / 真实绘图画廊

These previews are **actual Obsidian Excalidraw-ymjr exports** from the included YAML scenes. They were decoded and visually inspected; checks, resource completeness and recorded visual review are separate gates. They are not mockups or external-renderer approximations.

以下图片来自附带YAML的真实宿主渲染；每张都有源码与可编辑画布。它们展示实际完成过的表达规模，不代表任意同规模图的自动正确率、审美评分或完整硬件仿真。

## Coverage and complexity / 范围与复杂度

| Example / 示例 | Native elements / 原生元素 | Declared connections / 连接 | What it demonstrates / 表达能力 |
| --- | ---: | ---: | --- |
| Release flow / 变更上线 | 22 | 6 | Long Chinese decision, branch labels and resubmission loop |
| Task architecture / 异步任务架构 | 29 | 6 | Three measured regions, state update and external query tracks |
| Feedback datapath / 寄存反馈 | 62 | 8 | MUX/ALU polygons, named ports, data/control/feedback separation |
| Observability panel / 观测面板 | 62 | 0 | Native sharp-cell table, KPI blocks and two ECharts carriers |
| Tomasulo | 259 | 15 | Dense native tables, independent units/ports, CDB-related connections |
| Resources / 资源与效果 | 36 | 2 | Actual PNG asset, rendered source-preserving LaTeX, gradient/shadow and editable polygons |

Counts include native labels, binding anchors and port markers; they are not logical-node counts or a performance benchmark. Dashboard zero connections is intentional: it is a data panel, not a graph. Example data and hardware register states are synthetic teaching material.

## 1. Release flow / 变更上线

[Source YAML](../examples/dsl/release-flow.yaml) · [Native canvas](../examples/native/release-flow.excalidraw.md)

<img src="images/release-flow.png" width="560" alt="Actual release-flow PNG with complete long Chinese decision and revision loop">

Full Chinese content is retained and wrapped using the actual host font. Approved/rejected paths and the resubmission loop remain independent native arrows with bindings. This is an ordinary flow example, not a complete release-management policy.

## 2. Fixed-region architecture / 分组架构

[Source YAML](../examples/dsl/task-architecture.yaml) · [Native canvas](../examples/native/task-architecture.excalidraw.md)

![Actual three-region task architecture](images/task-architecture.png)

Regions come from explicit row/column composition. Progress and query paths have declared waypoints/label positions after real PNG feedback; automatic routing is not presented as a perfect first-pass result. DSL regions are visible layout regions, not native group/frame semantics.

## 3. Feedback datapath / 硬件反馈数据通路

[Source YAML](../examples/dsl/feedback-datapath.yaml) · [Native canvas](../examples/native/feedback-datapath.excalidraw.md)

![Actual named-port feedback datapath](images/feedback-datapath.png)

The MUX and ALU are editable native polygons with anchors and labels; registers, result and controller are separate objects. Source and picture explicitly omit clock/reset/opcode. Two Q destinations are a schematic representation, not a certified electrical netlist. Route labels were repaired without deleting required relations or rebuilding the canvas; saved endpoints may have subpixel native rounding.

## 4. Table and ECharts / 表格与图表

[Source YAML](../examples/dsl/observability-panel.yaml) · [Native canvas](../examples/native/observability-panel.excalidraw.md)

![Actual native table and ECharts observability panel](images/observability-panel.png)

The table is native sharp-corner cells plus bound text, with measured unequal columns and a contrasting header. ECharts retains complete JSON options in native rectangle carriers; the whole scene is not rasterized. The PNG verifies the static plots/axes/legend, not live hover/dataZoom or a visual-form editing roundtrip. All displayed service metrics are demonstration data.

## 5. Dense teaching diagram / 密集教学结构

[Source YAML](../examples/dsl/tomasulo.yaml) · [Native canvas](../examples/native/tomasulo.excalidraw.md)

![Actual dense Tomasulo example](images/tomasulo.png)

Reservation-station Tag/Busy/Op/Vj/Vk/Qj/Qk fields, Qi register state and queue/buffer entries remain individual editable cells and text. FP units use polygon silhouettes and named ports. The figure declares its teaching boundary: no ROB/precise-exception implementation and no cycle-by-cycle simulation proof. Overview/detail readability and declared bindings were inspected, not inferred from element count alone.

## 6. Source-backed resources / 资源与效果

[Source YAML](../examples/dsl/resources.yaml) · [Original PNG asset](../examples/dsl/assets/sample.png) · [Native canvas](../examples/native/resources.excalidraw.md)

![Actual resource gallery with image formula shadow and gradient](images/resources.png)

The formula is rendered by the actual host MathJax path with TeX retained, not literal source text. The image is an original generated PNG asset, and gradient/shadow use the host's controlled adapters. These examples do not redistribute a user's `.excalidrawlib` or assume every host has identical fonts/resources.

## Reproduce and edit / 复现与修改

Follow the [DSL usage guide](scene-dsl.md). Choose an actual discovered font, a unique filename and private state ID. The examples deliberately avoid a fixed font in the YAML. Inspect the PNG at the target output scale; use real detail previews when necessary. Edit source and reuse state-id to reconcile, rather than importing the included native sample and pretending it already has your private ownership state.

The native `.excalidraw.md` files can be opened in the modified plugin as editable reference outputs. They are **not** preconfigured managed DSL sessions: fresh CLI/MCP execution generates its own IDs/state. Included native resource references are valid only when their self-contained resources or the documented host prerequisites are available.

## Provenance and limits / 证据与限制

- Authored sources and original diagram content are distributed under the repository MIT license. No third-party user symbol library is included.
- Previews were produced with the real Bridge/native renderer and reviewed; current package release verification reruns the integrated CLI/MCP paths rather than treating old experiment screenshots as installation proof.
- Host evidence: Bridge 0.13.5; ECharts Engine 1.3.0 for plots; an actually discovered CJK family for Chinese text; compatible MathJax for formulas. These are verified example conditions, not portable installed-font promises.
- A check pass and a recorded review describe the observed version/output only. Interaction, arbitrary GUI-to-DSL changes, new engines, other hosts, unknown curves/rotation and general electrical semantics need their own evidence.
- Source size/native plan byte reductions from early experiments are not model token, latency or success-rate benchmarks. This gallery makes no such performance claim.
