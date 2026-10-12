# Obsidian Excalidraw Agent

[English](README.md) | [简体中文](README.zh-CN.md)

**Complete drawing package for Obsidian Excalidraw-ymjr:** MCP server, deterministic layout and diagnostics, Engine-Agent Bridge, 16 Feature Engines, first-time vault connection, and the Agent Skill with real PNG review.

Version 0.5.0 replaces the former Skill-only package. You no longer need to obtain a separate drawing backend, compose MCP paths, or copy bearer tokens into prompts. Install once, connect your intended vault, then describe what to draw.

## Host prerequisites

- [oh my pi / OMP](https://github.com/can1357/oh-my-pi) with Agent Plugins support (verified on OMP 18.10.1).
- [uv](https://docs.astral.sh/uv/getting-started/installation/) on PATH. `uv run` prepares the pinned Python dependencies automatically; Python 3.11+ is required. The initial dependency download needs network access.
- Obsidian Desktop with [Excalidraw-ymjr installed and enabled](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr). Back up your vault before changing plugins. The installer does not silently enable plugins, change trust permissions, or replace your upstream Excalidraw installation.
- An image-capable Agent for actual PNG inspection.

[Advanced URI](https://github.com/Vinzent03/obsidian-advanced-uri) is optional: when enabled, setup starts the Bridge automatically; otherwise setup returns the exact Obsidian command to run once. LaTeX needs the compatible Excalidraw Extras MathJax component enabled in Obsidian. Custom fonts and user-selected libraries are optional resources, not prerequisites for ordinary diagrams.

## Install globally

```sh
omp plugin marketplace add Bowen-0x00/obsidian-excalidraw-agent-skill
omp plugin install --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

Restart OMP, or use `/reload-plugins` in an existing TUI session. The package includes a credential-free `mcp.json`: OMP resolves its installed package/data directories and starts `launcher.py serve` through uv. It exposes **15 tools**, including first-time `drawing_setup`.

Check `/mcp list` for `excalidraw`, then ask:

> Use the Obsidian Excalidraw Skill. Connect to the vault I choose, then draw a request-review flowchart: submission → review; approved → issue credentials, rejected → explain the reason; both branches end. Keep the diagram editable and inspect the PNG.

The Agent calls `drawing_setup(action="status")`, discovers local vaults, and connects with `drawing_setup(action="connect", vault_path=the_selected_vault)`. It asks only when the target is ambiguous. Setup:

1. Checks the selected vault's installed/enabled ymjr plugin and configured script folder.
2. Deploys the bundled Bridge and Engines under `<script folder>/Agent-Drawing/`, preserving unrelated scripts and refusing to overwrite locally modified managed files.
3. Generates a local random bearer token and stores it outside the vault/package.
4. Starts `Agent-Drawing/mcp/Start-Agent-Drawing` through Advanced URI, or returns its manual command.
5. Confirms authenticated Bridge status. If Obsidian has not indexed new scripts yet, reload Obsidian once and run `drawing_setup(action="start")`.

After an Obsidian restart, `drawing_setup(action="start")` starts the saved connection again. If another Bridge owns the same port, choose an unused `port` during connection; setup reports failure rather than claiming success. Bridge replacement invalidates old canvas tokens, so rebind before continuing.

**Upgrading from 0.4.1:** remove only the old manually configured `excalidraw` server entry from your private user/project MCP file if it still points at a separate local executor. Native configuration takes precedence over the bundled server; leaving the old entry would keep running the old backend. Preserve other servers and settings. The old Skill-only instructions are obsolete.

## Updates and removal

```sh
omp plugin marketplace update obsidian-excalidraw-agent
omp plugin upgrade --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

Restart OMP, then reconnect the same vault to deploy changed managed scripts. Restart Obsidian after Engine upgrades so already-loaded hooks do not retain an old version. Persistent connection/artifact data is outside the versioned package cache.

```sh
omp plugin uninstall --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

Uninstall removes the OMP package registration, not your drawings or installed vault scripts. If you want to remove the deployed bundle, remove only the `Agent-Drawing` subdirectory you installed, after stopping Obsidian. Keep unrelated scripts and vault files.

## Clone / direct CLI alternative

```sh
git clone https://github.com/Bowen-0x00/obsidian-excalidraw-agent-skill.git
cd obsidian-excalidraw-agent-skill
uv run --frozen python launcher.py status
uv run --frozen python launcher.py connect --vault "/path/to/your/vault"
uv run --frozen python launcher.py doctor
uv run --frozen python launcher.py smoke
```

Replace the example path with the actual vault path. `connect --no-open` deploys without opening a URI; `--vault-name` handles Obsidian aliases; `--obsidian-config-dir` supports a non-default vault configuration folder; `--port` selects a local port. `smoke` creates a real editable flowchart and PNG, but deliberately reports `visual_reviewed=false`: a script cannot pretend to be a model looking at the image.

The complete drawing CLI is `launcher.py cli -- --help`. For another MCP client, run `uv run --frozen --project <clone> python <clone>/launcher.py serve`; no credential belongs in its MCP configuration. The bundled standard `mcp.json` targets OMP/Agent Plugins placeholder semantics; do not assume every client implements them.

Direct CLI mode uses the platform user-data directory. Marketplace mode uses OMP's persistent `${PLUGIN_DATA}/state`. Use `EXCALIDRAW_AGENT_STATE_DIR` to intentionally share a state directory, or `EXCALIDRAW_AGENT_CONFIG` to choose an existing private connection file. `drawing_setup(status)` returns the actual paths without returning tokens.

## Drawing tools

| Tools | Responsibility |
| --- | --- |
| `drawing_setup` | Discover vaults, deploy bundled scripts, create a private connection and start/check the Bridge |
| `drawing_context`, `drawing_read` | Capability discovery, explicit target binding, complete summaries and selected details |
| `drawing_measure`, `drawing_plan`, `drawing_apply` | Native text measurement, deterministic layout and revision-checked operations |
| `drawing_check`, `drawing_preview`, `drawing_review`, `drawing_revert` | Geometry/semantic diagnostics, PNG images, persistent review rounds and transaction undo |
| `drawing_templates`, `drawing_primitives` | Diagram/style recipes; freehand, polygons, cuboids, braces, callout, code, checkbox and connections |
| `drawing_library`, `drawing_compose`, `drawing_present` | Real library discovery/import, staged composition and editable native frame pages |

Tool names may have the `mcp__excalidraw_` prefix. Read the real schema before calling. Library import preserves source-to-native IDs, groups, frames, bindings and resources; composition reports separately committed stages instead of inventing cross-stage atomicity.

## Natural-language examples

> Use Visio-style UML to show Order, Customer and Payment, with fields, methods and correctly directed composition arrows.

> Use the digital-circuit library I installed to connect MUX → ALU → CROSSBAR. Discover and preview exact items first; do not replace them with approximate rectangles.

> Create three editable Excalidraw presentation pages from my installed presentation library. Preserve frames and decorations; inspect every page and the overview. Do not claim a PPTX export.

> In the vault-relative file I specify, rename this node and move it right. Preserve unrelated content, style and bindings, then inspect the updated PNG.

Ordinary diagrams default to native Helvetica with system CJK fallback, avoiding a dependency on a private font asset. Explicit user fonts are preserved and checked against runtime discovery.

## PNG feedback and completion

The Skill requires `check → PNG → actually inspect → review → local repair`. Default maximum: **five reviews including the initial drawing**, with early completion when requirements pass. Two consecutive non-improving transitions stop with unresolved issues. Complete summaries, full node/branch labels, reciprocal bindings, intact current-revision PNGs and resource completeness are checked; subjective visual judgment still requires the Agent to see the image.

Missing image access is unreviewed, not a pass. Unsupported curve/rotation diagnostics are reported. Excalidraw frame pages are not `.pptx` files. User drawings are never cleared and rebuilt just to apply a local edit.

## Package layout

- [Skill](skills/obsidian-excalidraw/SKILL.md), [diagram/style recipes](skills/obsidian-excalidraw/references/diagram-recipes.md), [native primitives](skills/obsidian-excalidraw/references/native-features.md).
- `runtime/`: all drawing, planning, diagnostics, resources and review modules.
- `launcher.py`, `setup_connection.py`: MCP entry and first-time connection.
- [Bridge bundle](bridge/bundle.json): Bridge, bootstrap and 16 required Feature Engines with embedded offline chart/highlight/export libraries.
- `plugin.json`, `mcp.json`, `.claude-plugin/`: versioned installation metadata; `pyproject.toml`/`uv.lock`: pinned execution dependencies.
- [Third-party notices](THIRD_PARTY_NOTICES.md): original script and embedded library licenses.

## Privacy and trust

`connection.json`, bearer tokens, absolute user paths, vault drawings, installed library files, PNGs, ledgers, caches and virtual environments are not release content. The vault descriptor stores only a local path to the external connection file. **That descriptor contains no token, but its path is machine-specific: exclude `Agent-Bridge-Connection.json` from public vault repositories.** POSIX private files are created with mode 0600; Windows uses the current user's data-directory permissions.

The Bridge listens on loopback, authenticates every request, rejects browser origins, and retains revision protection. This is trusted local code with vault read/write access, not a sandbox. Executable user-library `customData` requires explicit source trust. Environment credential overrides are for deliberate advanced setups, not the normal connection flow.

## Development

```sh
uv run --frozen python -m unittest discover -s runtime/tests -v
```

Use Conventional Commits and update [CHANGELOG.md](CHANGELOG.md). Keep real user artifacts private. The allowlist admits only intended runtime/Bridge/source files. Installation organization follows [academic-research-skills](https://github.com/Imbad0202/academic-research-skills); its content is not bundled.

Plugin links: [distribution/releases](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr), [plugin source](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin/tree/ymjr), [component source](https://github.com/Bowen-0x00/excalidraw/tree/ymjr), [original scripts](https://github.com/Bowen-0x00/obsidian-excalidraw-scripts).

[MIT License](LICENSE) for the package's original code; embedded components retain their licenses in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Not affiliated with Obsidian or upstream Excalidraw.
