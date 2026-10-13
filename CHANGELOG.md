# Changelog

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
