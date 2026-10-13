# Obsidian Excalidraw Agent

[English](README.md) · [简体中文](README.zh-CN.md)

Draw editable diagrams in Obsidian Excalidraw-ymjr from natural-language requests. The package includes an Agent Skill, a drawing MCP server, and the scripts that connect it to Obsidian.

## Features

- Flowcharts, architecture diagrams, UML, swimlanes and editable presentation frames.
- Native shapes, text and arrows; image/LaTeX/chart content and user-installed libraries where supported.
- Measured text layout, geometry checks, PNG previews and incremental edits.
- Headless remote OMP support: render in desktop Obsidian and return the PNG to the remote Agent.

## Requirements

For local drawing:

- Obsidian Desktop with [Excalidraw-ymjr](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr) installed and enabled in the target vault.
- [OMP](https://github.com/can1357/oh-my-pi) with Agent Plugins support, plus [uv](https://docs.astral.sh/uv/getting-started/installation/) on PATH and Python 3.11+.
- A model that accepts images, so it can inspect the exported PNG.

[Advanced URI](https://github.com/Vinzent03/obsidian-advanced-uri) is optional. Setup uses it to start the Bridge; without it, run the returned command in Obsidian. Custom fonts and libraries are optional. LaTeX requires a compatible enabled Excalidraw Extras MathJax component.

## Quick start

### 1. Install the OMP package

```sh
omp plugin marketplace add Bowen-0x00/obsidian-excalidraw-agent-skill
omp plugin install --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

Restart OMP or run `/reload-plugins`. The package starts its MCP server through uv; dependencies are downloaded on first use. `/mcp list` should show the drawing server, possibly under a plugin-prefixed name.

### 2. Connect a vault

Keep Obsidian open, then ask OMP:

> Use skill://obsidian-excalidraw. Connect to my chosen Obsidian vault and check the drawing service.

The Agent uses `drawing_setup` to list vaults and connect the selected one. Setup installs scripts under the plugin's configured script folder, in an `Agent-Drawing` subdirectory. It preserves unrelated files and does not change plugin permissions.

If automatic startup is unavailable, open a drawing and run `Agent-Drawing/mcp/Start-Agent-Drawing` in Obsidian's command palette. Reload Obsidian once if newly installed scripts are not listed yet.

### 3. Describe the diagram

> Draw a request-review flowchart: submit → review; approved → issue credentials, rejected → explain the reason; both paths end. Keep all labels and inspect the PNG.

> Draw an order-system architecture with frontend, services and storage containers. Keep cross-container connections.

> Rename a node in the drawing I specify, leaving other content and styles unchanged.

The editable drawing is saved in the connected vault. PNG previews and review records are saved in the execution server's data directory. The Agent checks the image and repairs specific problems rather than rebuilding the whole drawing. By default it stops after a successful review or at five reviews, reporting unresolved issues.

## Remote drawing

The desktop machine runs Obsidian and the Bridge. The remote machine runs OMP, the Skill and a Python MCP client; it does not need Obsidian, a desktop or X11.

On the desktop host, use a checkout of this repository or the installed package directory. Select the same connection state used by your local MCP: set `EXCALIDRAW_AGENT_STATE_DIR` to the path returned by `drawing_setup(status)` if needed. Then run:

```sh
uv run --frozen python launcher.py remote-deploy --host Redhat --remote-port 28125
uv run --frozen python launcher.py remote-tunnel --host Redhat --remote-port 28125
```

`Redhat` is an existing SSH alias. Deployment requires remote Python 3.11+, pip and OMP. It installs the Skill and `excalidraw-local` MCP under the remote user's account, preserving existing OMP settings. The second command keeps an SSH reverse tunnel open from remote loopback port 28125 to the desktop Bridge. Keep that command and Obsidian running.

Already logged into the remote machine? Run `omp` normally, or `/reload-plugins` in an existing session, then describe the diagram. You do not need to log in using a special SSH command.

Native drawings and source assets remain in the desktop vault. PNG bytes return through the tunnel, are saved on the remote machine, and reach the model as MCP image content. The returned PNG path is therefore readable by the remote Agent. Remote `drawing_setup(status)` reports `mode=remote`; selecting a vault or starting Obsidian must be done on the desktop host.

The remote client stores its Bridge credential in a private 0600 file. Give access only to trusted users. The tunnel uses an isolated SSH configuration with key authentication and known-host verification; it does not reuse unrelated port forwards or enable X11. Stop/restart the tunnel after disconnection. After changing the host vault, rerun `remote-deploy` and restart the remote MCP. For scripted `omp -p` calls over SSH, use `ssh -n` to close stdin; interactive sessions use a normal terminal.

## Native Excalidraw CLI

Recent ymjr versions also include a plugin-native CLI. It is useful for simple creation, inspection, edits and exports without this package's Bridge. The terminal entry requires **Obsidian 1.12.2+ with CLI enabled** and a plugin build that registers the commands.

```sh
obsidian vault="My vault" obsidian-excalidraw-plugin-ymjr:status
obsidian vault="My vault" obsidian-excalidraw-plugin-ymjr:help
obsidian vault="My vault" obsidian-excalidraw-plugin-ymjr:schema action=create
```

Use the actual plugin ID as the command prefix. On Windows, use the installed `Obsidian.com` console launcher to capture output. In trusted EA scripts, `ea.executeCLI(request)` exposes the same JSON protocol without the terminal registration requirement; check that the installed plugin provides the method first.

The Skill now distinguishes this native CLI from `launcher.py cli`. It checks save receipts and request IDs, uses paged reads, and inspects real exports. The native CLI does **not** supply our automatic layout, geometry diagnostics, review ledger or remote image transport. Connected MCP/remote workflows continue using `drawing_*`. See [Native CLI reference](skills/obsidian-excalidraw/references/native-cli.md) for schemas, persistence, limits and error recovery.

## Configuration and files

| Item | Location |
| --- | --- |
| Marketplace connection and artifacts | OMP's persistent plugin data directory, `${PLUGIN_DATA}/state` |
| Direct CLI connection and artifacts | Platform user-data directory; `launcher.py status` shows the path |
| Remote runtime, connection and artifacts | `~/.local/share/obsidian-excalidraw-agent-remote/` |
| Remote Skill / MCP registration | User agent directory, normally `~/.omp/agent/skills/` and `~/.omp/agent/mcp.json` |
| Deployed Obsidian scripts | `<configured script folder>/Agent-Drawing/` |

`EXCALIDRAW_AGENT_STATE_DIR` selects a state directory; `EXCALIDRAW_AGENT_CONFIG` selects a private connection file. Credentials are not returned by the setup tool. The vault's `Agent-Bridge-Connection.json` contains only the external config path; exclude it from public vault repositories because that path is machine-specific.

For direct CLI use, clone the repository and run `uv run --frozen python launcher.py --help`. The drawing CLI is `launcher.py cli -- --help`. MCP clients can start `launcher.py serve` through uv. The execution code lives in `runtime/`; the Obsidian scripts in `bridge/`; drawing conventions in `skills/`.

## Updates and removal

```sh
omp plugin marketplace update obsidian-excalidraw-agent
omp plugin upgrade --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

Restart OMP after an update. Reconnect the same vault to update managed scripts; restart Obsidian after Engine changes. Run `remote-deploy` again to update a managed remote installation. Modified scripts/Skills are not silently overwritten.

Uninstall with `omp plugin uninstall --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent`. This does not delete drawings, data directories or deployed vault scripts. Remove those separately only if no longer needed. When migrating from an old manually configured executor, remove only its obsolete MCP entry so it does not override the packaged server.

## Troubleshooting and limits

| Symptom | Check |
| --- | --- |
| Skill or drawing tools missing | Restart OMP or `/reload-plugins`; check `/mcp list` and uv on PATH |
| Service disconnected | Run `drawing_setup(status)`; start the Bridge locally and, for remote use, the tunnel |
| `ready=false` but `connected=true` | The service may have no active drawing; create or bind an explicit canvas |
| Modified file blocks an update | Preserve or resolve that customization before redeploying |
| Native command missing | Check CLI setting, Obsidian API version, console launcher, plugin build and selected vault |

The Bridge is trusted local code with vault read/write access, not a sandbox. It listens on loopback and authenticates requests. Executable library `customData` requires explicit trust. Curves/rotated geometry may have unsupported diagnostics; frame presentations are not PPTX files. Missing image access or resources must be reported, not counted as a successful review.

Initial dependency installation uses PyPI (remote deployment uses the official index); SSH deployment sends connection credentials and package code to the selected host. Drawing itself uses the local plugin and resources, with no separate rendering service. Your Agent/model provider receives the prompts and images it processes.

## Development and license

```sh
uv run --frozen python -m unittest discover -s runtime/tests -v
```

[Skill](skills/obsidian-excalidraw/SKILL.md) · [Diagram recipes](skills/obsidian-excalidraw/references/diagram-recipes.md) · [Native features](skills/obsidian-excalidraw/references/native-features.md) · [Changelog](CHANGELOG.md)

Related projects: [ymjr plugin/releases](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr), [plugin source](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin/tree/ymjr), [component source](https://github.com/Bowen-0x00/excalidraw/tree/ymjr), [original scripts](https://github.com/Bowen-0x00/obsidian-excalidraw-scripts).

Original package code is [MIT licensed](LICENSE). Embedded libraries retain the licenses in [Third-party notices](THIRD_PARTY_NOTICES.md). This project is not affiliated with Obsidian or upstream Excalidraw.
