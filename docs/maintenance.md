# Maintenance and release / 维护与发布

User entrypoints are documented in [README](../README.md), [中文README](../README.zh-CN.md), [Scene DSL](scene-dsl.md) and [Agent setup](../skills/obsidian-excalidraw/references/agent-setup.md). This page is for package maintainers, not a prerequisite for asking an Agent to draw a simple graph.

## One optional compiler, one native backend

`runtime/scene_dsl/` contains model/compiler/session/service/CLI. `drawing_dsl` and `launcher.py dsl` share the same service. Ordinary compose, exact native operations, libraries, presentations and host-specific capabilities remain in their existing modules. Do not maintain another backend-path-dependent DSL copy or add compatibility shims for the retired experiment CLI.

Reviewed sources live under `examples/dsl/` (compiler input) and `examples/builders/` (Agent-authored Python calling native APIs); native examples under `examples/native/`; actual PNGs under `docs/images/`. Preserve that distinction in README/gallery/provenance. Other user canvases, connection settings, private identity files, logs and artifacts remain ignored. Changes to geometry/fonts require re-rendering the affected real examples; text-source checks do not prove image quality.

`drawing_table` uses the existing paired host `TableManager` through Bridge `/v3/tables`; the Agent package does not contain a second theme palette, table border renderer or host plugin upgrade. Check `nativeTable.callable` and keep the development-host requirement visible in docs/examples. Native manager creation/style are saved but not one atomic Bridge-undo transaction; retain partial-failure receipts and never blindly recreate after an unknown result.

## Optional read-only diagnostics

`runtime/cdp_readonly.py` is a client-side fixed-observation adapter, not the development lab's unrestricted CDP harness. `drawing_debug` cannot enable itself; CLI opt-in lives only in the client's private `cdp-readonly.json`. Package synchronization must never copy/enable that file or launch/reload a host on the user's behalf. A separately authorized loopback debugger/tunnel and exact host-vault pin are prerequisites.

Preserve the exact query/protocol allowlist and V8 side-effect checks; do not add arbitrary expressions, `Runtime.callFunctionOn`, Input, Page writes, breakpoints, save/export or an unguarded fallback. State collection failures are explicit limitations. Verify real scene/file bytes, selection and viewport are unchanged; tests alone cannot certify read-only host behavior. Keep the unrestricted debugger/security boundary visible in the [diagnostic guide](../skills/obsidian-excalidraw/references/cdp-readonly.md).

## Drawing workflow gates

New drawing creation requires a `brief` with a stable task ID, individually resolved style/review/palette/background/font provenance and user requirements. Native edits require an explicitly bound brief too; read-only observations do not. Rebind maps to file/task-scoped review history, not a fresh token budget. Existing pre-brief diagnostic logs remain preserved; they are not retroactively claimed as verified user choices.

Bridge 0.13.7 preflights all native operation keys before staging, and uses the active host package's `refreshTextDimensions` for text measurement/creation. The native library is required; do not restore an estimated-width or font-default-line-height fallback. The small-text trigger requires readable detail evidence at medium/high, not a larger arbitrary full-canvas scale.

Review must retain raw diagnostics. Text-conflict adjudication permits only specific false-positive evidence with matching IDs and readable registered detail PNGs; repeated boilerplate or intentional unreadability must fail. Requirement coverage and claimed user-choice provenance are Agent attestations, not independent semantic/pixel proofs or a security boundary against arbitrary trusted Bridge/OS code.


## Shared Engine source and automatic update PRs

- [`bridge/shared-scripts.json`](../bridge/shared-scripts.json) is the explicit import allowlist. Shared Engines are maintained only in [Scripts](https://github.com/Bowen-0x00/obsidian-excalidraw-scripts); `mcp/Start-Agent-Drawing.md` and `mcp/Engine-Agent-Bridge.md` belong to this Agent repository and are never imported.
- [`bridge/shared-scripts.lock.json`](../bridge/shared-scripts.lock.json) records the exact source commit, path, script version and SHA-256 of UTF-8/LF content. Historical legacy `sourceCommit:null` represented unknown provenance, not an invented commit; actual imported snapshots pin their published source tree.
- Scripts main pushes notify this repository only for declared inputs or notification-workflow changes. The receiver supports repository dispatch and manual **Run workflow** only; there is no periodic fallback. If a notification fails or is missed, fix the sender and run it manually to catch up. It imports the latest source main, coalesces delayed notices, validates all inputs, compiles JavaScript without executing it, runs behavior regressions and creates/updates one scoped `automation/shared-script-engines` PR.
- Unrelated source changes and identical content are no-ops, including lock commit churn and an already-current PR. Deleted/renamed inputs, missing declarations, symlinks and independently edited shared copies fail before copying. A bot branch with human commits or out-of-scope edits is not overwritten; a rejected/orphaned branch must be resolved before reuse. An unchanged merged branch can be reused.
- Configure `SKILL_SYNC_TOKEN` as an Actions repository secret in both repositories. Prefer an expiring fine-grained credential limited to this Agent repository with Contents read/write, Pull requests read/write and Metadata read. Never paste it in workflow YAML, commit it, enable secret-bearing jobs for untrusted PRs, or broaden repository-wide default permissions unnecessarily. Rotate by replacing both secrets.
- PR creation is automatic; merge/release is a maintainer gate. A PR does not bump package versions, overwrite customized vault scripts, reload mounted Engines or deploy local/remote clients. Source existence, copied bundle and running Engine are distinct states.

### Retired upstream Engines / 上游 Engine 退休

The table Engine was intentionally removed in [Scripts `3a1f79f`](https://github.com/Bowen-0x00/obsidian-excalidraw-scripts/commit/3a1f79f4f63a81989a0c4a338e836c698ee591f4): Excalidraw-ymjr 2.29.0-4 and later own table interaction in the host. The Agent bundle now imports 15 shared Engines and no longer installs or starts `Feature-Table-Engine.md`. `drawing_table` still requires the discovered host `nativeTable.callable` capability; the legacy `create_table`/DSL grid contract is unchanged.

A deliberate retirement must remove the source/target mapping, matching lock entry, bundle script/Engine entries, bootstrap dependency and bundled file together. Do not restore the old hook Engine or make the importer silently skip missing declared inputs just to obtain a green run. Restart an existing host after removing a previously mounted old Engine; this repository change does not modify local vault files or unload running hooks.

表格脚本迁入宿主原生实现后，必须同步移除白名单、锁定项、bundle、启动依赖和旧副本。其他仍声明的文件删除／改名仍应报错；不要通过跳过错误来掩盖清单失配。


## Local validation commands

The source checkout must contain the exact published commit when importing shared scripts:

```sh
python scripts/sync_shared_scripts.py check
python scripts/sync_shared_scripts.py plan --source-dir /path/to/scripts --source-commit FULL_40_CHARACTER_COMMIT
python scripts/sync_shared_scripts.py apply --source-dir /path/to/scripts --source-commit FULL_40_CHARACTER_COMMIT
node scripts/check_shared_scripts.mjs
python -m unittest discover -s scripts/tests -v
uv run --frozen python -m unittest discover -s runtime/tests -v
```

No upstream Engine executes just because it was published. Return fixes to the shared source rather than independently editing the copied Engine. Adding a new Engine requires reviewing the manifest, lock and bundle declaration together—not filename-based automatic import.

## Release gate

1. Preserve unrelated repository/user changes. Update package manifests and the lock consistently; remote and host installation receipts derive the package version rather than a separate stale literal.
2. Run importer/runtime regressions and inspect language diagnostics. Tests must protect behavior, identities, conflicts and boundaries; do not use copied source text or mocked render success as proof.
3. Launch the real packaged CLI and stdio MCP against an isolated explicit canvas. Exercise first render, repeat/no-op, update, external-edit conflict, native bindings, resource completeness and actual PNG/review. Check-only completion is not accepted.
4. Re-render curated examples; verify their public native files contain no private paths, bearer data or missing external image references. Inspect overview/detail PNGs at readable scale. Preserve original sources and report limitations.
5. Check a clean exported installation archive, actual launch entrypoints, image/source/document links and the curated file allowlist. GitHub runners cannot prove Obsidian GUI compatibility; real-host evidence remains a separate gate.
6. Publish the reviewed main commit, version tag and release asset. Installing from the marketplace should receive that same version. Do not claim npm/PyPI or another channel was published if it was not.
7. Update managed local/remote clients without dropping unrelated MCP entries, private connection/DSL state or user settings. If Windows locks an old cache, stop only this package's occupying MCP before supported upgrade; never solve it by deleting user state. Restart/reload the client to discover new tools.

The remote installer includes the optional compiler, dependencies, usage docs and example sources; remote rendering still occurs on the graphical host through loopback SSH. A package update is not permission to replace customized scripts or automatically trust executable library content.

## Safety

The Bridge is trusted code with vault read/write access, not a sandbox. Keep loopback authentication and credentials private. Additional Engines, code-bearing customData/library scripts, external application writes, interaction and animation require their own capability/trust checks. A static PNG cannot certify those runtime effects.
