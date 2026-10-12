# Changelog

## 0.4.1 — Global Skill distribution

- Package the existing drawing workflow and two reference files as a user-scope OMP marketplace plugin; execution tools remain a separately configured dependency.
- Replace project-relative CLI assumptions and machine-specific library paths with explicit runtime installation and real library discovery.
- Add linked English and Simplified Chinese READMEs covering installation, updates, removal, natural-language use, execution prerequisites and public plugin/source links.
- Add an MIT license and an explicit public-file allowlist. Exclude credentials, MCP configuration, user drawings, assets, previews, ledgers, logs and local runtime files.

The referenced workflow targets native editable diagrams with deterministic geometry checks and actual PNG review. This Skill package does not implement or bundle a renderer, MCP server, Bridge or PPTX exporter.
