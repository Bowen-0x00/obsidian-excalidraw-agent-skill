# Obsidian Excalidraw Agent Skill

[English](README.md) | [简体中文](README.zh-CN.md)

An Agent Skill for natural-language diagrams in **Obsidian Excalidraw-ymjr**: native editable elements, measured layout, geometry checks, PNG inspection and targeted repairs.

**This repository distributes the Skill and its references only.** It does not install a drawing MCP server, Engine-Agent Bridge, Obsidian plugin, fonts or libraries. Installing the Skill alone does not create a working drawing backend. It targets the `drawing_*` tool contract below, not every Excalidraw MCP server or the unmodified upstream plugin.

## Requirements

- [oh my pi (OMP)](https://github.com/can1357/oh-my-pi), with Skill discovery enabled.
- Obsidian Desktop and [Excalidraw-ymjr installation/releases](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr). Back up the vault before changing plugins; follow the plugin's instructions for avoiding conflicts with upstream Excalidraw.
- A separately installed, compatible drawing MCP/Bridge runtime connected to your own vault. Use runtime discovery to confirm available APIs and Feature Engines; the public plugin release alone does not prove that the drawing tools exist.
- An image-capable agent for actual PNG review. Libraries, images, custom fonts and LaTeX components are optional dependencies of the requested diagram, not bundled assets.

The plugin's public source is [obsidian-excalidraw-plugin/tree/ymjr](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin/tree/ymjr); component source is [excalidraw/tree/ymjr](https://github.com/Bowen-0x00/excalidraw/tree/ymjr). Related scripts are maintained in [obsidian-excalidraw-scripts](https://github.com/Bowen-0x00/obsidian-excalidraw-scripts); availability of a particular Bridge/Engine must be checked, not assumed.

## Install globally in OMP

Recommended: install the versioned marketplace plugin at **user scope**.

```sh
omp plugin marketplace add Bowen-0x00/obsidian-excalidraw-agent-skill
omp plugin install --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

Restart OMP after CLI installation. For installation from an existing TUI session, run `/reload-plugins`. The Skill is available outside the cloned repository; this does not automatically globalize a project-only MCP configuration.

Verify from another working directory:

```sh
omp read skill://obsidian-excalidraw
```

Updates and removal:

```sh
omp plugin marketplace update obsidian-excalidraw-agent
omp plugin upgrade --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
omp plugin uninstall --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

Marketplace update refreshes the catalog; upgrade reinstalls the plugin. Do not install a second manual copy unless you intentionally want to override the marketplace Skill. A differing project Skill can shadow the global one.

### Manual installation alternative

Clone this repository and copy **the complete** `skills/obsidian-excalidraw` directory, including `references`, into your active OMP user agent directory's `skills/` folder. For the default profile this is `~/.omp/agent/skills/obsidian-excalidraw/`. Custom agent roots and named profiles use their own directory.

PowerShell, run from the clone:

```powershell
$destination = Join-Path $HOME '.omp/agent/skills'
New-Item -ItemType Directory -Force $destination | Out-Null
Copy-Item -Recurse './skills/obsidian-excalidraw' $destination
```

POSIX shell, run from the clone:

```sh
mkdir -p ~/.omp/agent/skills
cp -R skills/obsidian-excalidraw ~/.omp/agent/skills/
```

Check for an existing same-named Skill before copying; do not overwrite an unrelated customization. Manual copies are not managed by `omp plugin upgrade`. The `.claude-plugin` catalog is also usable with Claude Code's plugin marketplace; this release's runtime verification is for OMP.

## Connect your execution runtime

Keep your real MCP configuration private. OMP's default user-level file is `~/.omp/agent/mcp.json`; the project-level file is `.omp/mcp.json`. To use drawing from every directory, merge **only your drawing server entry** into the user-level configuration without replacing other servers. Preserve existing top-level settings. Named profiles require their own user configuration.

For a separately installed Python stdio server, configure the actual Python executable and `server.py` paths, the runtime's working directory, and `EXCALIDRAW_BRIDGE_URL`, `EXCALIDRAW_BRIDGE_TOKEN`, `EXCALIDRAW_BRIDGE_TIMEOUT` as required by that runtime. Do not use the Skill cache directory as the runtime directory. This repository intentionally ships no credential-bearing MCP configuration and no nonexistent default server path.

In OMP, `/mcp list` should show the drawing server. Tool names may be prefixed, for example `mcp__excalidraw_drawing_context`. Confirm real tool schemas before calling:

| Tools | Responsibility |
| --- | --- |
| `drawing_context`, `drawing_read` | Discover capabilities, create/bind an explicit vault file, read complete summaries and selected details |
| `drawing_measure`, `drawing_plan`, `drawing_apply` | Native text measurement, deterministic layout and revision-checked operations |
| `drawing_check`, `drawing_preview`, `drawing_review`, `drawing_revert` | Diagnostics, real PNG delivery, persistent review rounds and transaction undo |
| `drawing_templates`, `drawing_primitives` | Optional diagram/style recipes and native complex-element planning |
| `drawing_library`, `drawing_compose`, `drawing_present` | Optional real library import, staged composition and editable frame pages |

If those tools are absent, install/configure the compatible runtime first. A generic tool with a similar name is not proof of this contract. If your runtime documents CLI access instead, `EXCALIDRAW_AGENT_HOME` can identify its actual installation directory; the Skill checks real scripts/environments rather than assuming they are bundled.

## Use natural language

You can ask directly, or explicitly invoke `/skill:obsidian-excalidraw` when Skill commands are enabled.

> Draw a request-review flowchart: submit → security review; approval issues credentials, rejection explains the reason; both paths end. Preserve every branch label, create a separate editable canvas and inspect the PNG.

> Use Visio-style UML to show Order, Customer and Payment, with fields, methods and correctly directed composition arrows.

> Use the digital-circuit library I installed to connect MUX → ALU → CROSSBAR. Discover the exact items first; do not replace them with approximate rectangles.

> Create three editable Excalidraw presentation pages using my installed presentation library. Preserve frames and decorations; inspect each page and the overview. Do not claim a PPTX export.

> In the vault-relative file I specify, rename this node and move it right. Preserve unrelated content, style and bindings, then inspect the updated PNG.

## What the Skill enforces

- Explicit target file/context and current revisions; no clearing/rebuilding an existing user drawing.
- Native shapes, text, arrows, freehand strokes, complex primitives and library members where runtime support exists; no full-diagram raster substitute.
- Font-based measurement, complete scene summaries, reciprocal bindings and semantic checks for full labels and branch directions.
- `check → PNG → actually inspect → review → local repair`. Default maximum: **five reviews, including the initial drawing**; stop early when requirements pass.
- Report missing resources, unsupported geometry, stale previews and two consecutive non-improving transitions. Export success is not visual approval.
- Preserve editable source/options for images, formulas, ECharts and embeddables. Require discovered Feature Engines for shadow, gradient, callout, highlighted code and checkbox.
- User-selected libraries are discovered, previewed and natively imported; duplicate names require exact IDs. Composition can commit in stages and must report partial progress rather than invent atomicity.

## Package contents

- [SKILL.md](skills/obsidian-excalidraw/SKILL.md): core workflow and acceptance rules.
- [Diagram/style recipes](skills/obsidian-excalidraw/references/diagram-recipes.md): flowcharts, architecture, UML, microarchitecture and frame presentations.
- [Native primitives](skills/obsidian-excalidraw/references/native-features.md): draw, polygons, cuboids, braces, callout, code, checkbox and connections.
- `.claude-plugin/`: versioned plugin manifest and installable marketplace catalog.

## Privacy and limitations

The release allowlist excludes tokens, private MCP files, machine-specific paths, vault drawings, libraries, screenshots, previews, review ledgers, logs, caches and virtual environments. Your runtime can read and write the vault: keep its bearer token private and local, and grant only the access you intend. Executable library `customData` needs explicit local-source trust; arbitrary generated code is not a default extension interface.

The Skill is a workflow, not a renderer or a guarantee of subjective beauty. Missing image access must be reported as unreviewed. Curve/rotation diagnostics may be unsupported by the connected runtime. Excalidraw frame pages are not `.pptx` files. This package is not affiliated with Obsidian or upstream Excalidraw.

## Development

Use Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`), update [CHANGELOG.md](CHANGELOG.md), and review every public file before release. The repository uses an explicit distribution allowlist; add new public paths intentionally. Never commit real user artifacts to demonstrate success. Installation approach follows the plugin/marketplace layout also used by [academic-research-skills](https://github.com/Imbad0202/academic-research-skills); its content is not bundled here.

[MIT License](LICENSE). Plugin, components and user-selected libraries keep their own licenses.
