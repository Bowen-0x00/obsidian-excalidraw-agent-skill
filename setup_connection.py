"""Deploy the bundled Bridge into an explicitly selected Obsidian vault."""
from __future__ import annotations

import hashlib
import json
import os
import secrets
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path, PurePosixPath
from typing import Any

from runtime_config import (ConnectionSelectionRequired, bridge_get, connection_path,
                            connection_profiles, effective_connection, load_connection,
                            probe_connection, read_connection, state_directory, vault_identity)

ROOT = Path(__file__).resolve().parent
PLUGIN_ID = "obsidian-excalidraw-plugin-ymjr"


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _private_write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    temporary = path.with_name(path.name + ".tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    if os.name != "nt":
        temporary.chmod(0o600)
    temporary.replace(path)


def _inside(root: Path, relative: str) -> Path:
    relative = relative.replace("\\", "/")
    parsed = PurePosixPath(relative)
    if not relative or parsed.is_absolute() or ".." in parsed.parts or ":" in relative:
        raise ValueError("Expected a vault-relative path without traversal")
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError("Path escapes the selected directory")
    return target


def _local_vaults() -> list[dict[str, Any]]:
    override = os.environ.get("OBSIDIAN_CONFIG_DIR")
    if override:
        config_dir = Path(override)
    elif sys.platform == "win32":
        config_dir = Path(os.environ.get("APPDATA", str(Path.home() / "AppData/Roaming"))) / "obsidian"
    elif sys.platform == "darwin":
        config_dir = Path.home() / "Library/Application Support/obsidian"
    else:
        config_dir = Path(os.environ.get("XDG_CONFIG_HOME", str(Path.home() / ".config"))) / "obsidian"
    registry = config_dir / "obsidian.json"
    if not registry.is_file():
        return []
    data = _read_json(registry)
    if not isinstance(data, dict) or not isinstance(data.get("vaults", {}), dict):
        raise ValueError("Malformed Obsidian vault registry")
    result = []
    for registry_id, entry in data.get("vaults", {}).items():
        if not isinstance(entry, dict) or not entry.get("path"):
            continue
        candidate = Path(entry["path"]).expanduser()
        if not candidate.is_dir():
            continue
        candidate = candidate.resolve()
        plugin = candidate / ".obsidian/plugins" / PLUGIN_ID
        enabled_path = candidate / ".obsidian/community-plugins.json"
        try:
            enabled = _read_json(enabled_path) if enabled_path.is_file() else []
            manifest = _read_json(plugin / "manifest.json") if (plugin / "manifest.json").is_file() else {}
            eligible = PLUGIN_ID in enabled and manifest.get("id") == PLUGIN_ID and (plugin / "main.js").is_file()
        except (OSError, ValueError, TypeError, AttributeError):
            eligible = False
        result.append({"id": vault_identity(str(candidate)), "registry_id": registry_id,
                       "name": candidate.name, "path": str(candidate), "pluginEnabled": eligible,
                       "running": False, "selected": False})
    return result


def discover_vaults() -> list[dict[str, Any]]:
    try:
        config = effective_connection()
    except ConnectionSelectionRequired as error:
        # With several remote hosts there is no single authenticated registry to query.
        return [] if any(p["config"].get("mode") == "remote" for p in error.profiles) else _local_vaults()
    if config.get("mode") == "remote":
        if not config.get("bridge_token") or not config.get("bridge_url"):
            return []
        registry = bridge_get(config, "/v3/vaults")
        if not isinstance(registry.get("vaults"), list):
            raise ValueError("Host Bridge lacks the authenticated vault registry; update and restart the host Bridge.")
        return [{key: entry[key] for key in ("id", "name", "path", "pluginEnabled", "running", "selected") if key in entry}
                for entry in registry["vaults"] if isinstance(entry, dict)]
    vaults = _local_vaults()
    running_ids, running_paths = set(), set()
    for profile in connection_profiles():
        if profile["config"].get("mode") == "remote":
            continue
        probe = _bridge_probe(profile["config"])
        observed = probe.get("status", {}).get("vault")
        if probe["connected"] and isinstance(observed, dict):
            running_ids.add(observed.get("id"))
            running_paths.add(observed.get("path"))
    for vault in vaults:
        vault["selected"] = vault["id"] == config.get("vault_id") or vault["path"] == config.get("vault_path")
        vault["running"] = vault["id"] in running_ids or vault["path"] in running_paths
    return vaults


def _bridge_probe(config: dict[str, Any]) -> dict[str, Any]:
    return probe_connection(config)


def _public_status(status: dict[str, Any]) -> dict[str, Any]:
    return {key: status[key] for key in ("ok", "ready", "file", "revision", "scriptPath", "host", "vault",
                                        "pluginVersion", "bridgeVersion", "openCanvases", "engines") if key in status}


def _catalog(config: dict[str, Any], profiles: list[dict[str, Any]], *,
             selected_probe: dict[str, Any] | None = None, probe_all: bool = True) -> dict[str, Any]:
    connections, selected_id = [], None
    for profile in profiles:
        candidate = profile["config"]
        selected = (candidate.get("bridge_url"), candidate.get("bridge_token")) == (config.get("bridge_url"), config.get("bridge_token"))
        if selected:
            selected_id = profile["id"]
        probe = (selected_probe if selected and selected_probe is not None else
                 _bridge_probe(candidate) if probe_all else
                 {"connected": False, "ready": False, "code": "NOT_CHECKED"})
        observed = probe.get("status", {})
        connections.append({"id": profile["id"], "name": candidate.get("vault_name") or profile["id"],
                            "mode": candidate.get("mode", "local"), "config_path": profile["config_path"],
                            "host": observed.get("host") or {"id": candidate.get("host_id"), "name": candidate.get("host_name") or candidate.get("remote_host")},
                            "vault": observed.get("vault") or {"id": candidate.get("vault_id"), "name": candidate.get("vault_name"),
                                                               "path": candidate.get("host_vault_path") or candidate.get("vault_path")},
                            "selected": selected, **{key: probe[key] for key in ("connected", "ready", "code")}})
    live = sum(entry["connected"] for entry in connections)
    return {"connections": connections, "selected_connection_id": selected_id,
            "needs_selection": not bool(config.get("bridge_token")) and live > 1}


def list_connections() -> dict[str, Any]:
    try:
        config = effective_connection()
    except ConnectionSelectionRequired:
        config = {}
    return _catalog(config, connection_profiles(remote=config.get("mode") == "remote"))


def select_connection(selector: str) -> dict[str, Any]:
    # Reading an explicit malformed binding must fail, not silently discover another target.
    try:
        current = load_connection()
    except ConnectionSelectionRequired:
        current = {}
    profiles = connection_profiles(remote=current.get("mode") == "remote")
    matches = [profile for profile in profiles if profile["id"] == selector]
    if not matches:
        matches = [profile for profile in profiles if selector in (profile["config"].get("vault_id"), profile["config"].get("vault_name"))]
    if len(matches) != 1:
        raise ValueError("Unknown connection selector" if not matches else "Ambiguous connection name; select an id")
    selected = dict(matches[0]["config"])
    selected["connection_id"] = matches[0]["id"]
    selected["mode"] = selected.get("mode", "local")
    target = connection_path().resolve()
    if target.is_relative_to(ROOT) or (selected.get("mode") != "remote" and selected.get("vault_path") and target.is_relative_to(Path(selected["vault_path"]).resolve())):
        raise ValueError("Private connection configuration must stay outside the vault and installed package")
    _private_write(target, selected)
    return setup_status()


_REMEDIATION = {
    "READY": "Connected and ready to draw.",
    "NO_CANVAS": "Connected. Open an Excalidraw canvas or create/bind one before drawing.",
    "NOT_CONFIGURED": "Run vaults, then use a connection id or connect an eligible registered vault.",
    "SELECTION_REQUIRED": "Multiple choices are available. Run vaults, then use a connection id or connect with a registered vault id/name.",
    "CONFIG_INVALID": "Repair the explicitly configured connection file; it was not replaced or bypassed.",
    "CONNECTION_FAILED": "Start the selected host Bridge; for remote mode also restore its SSH tunnel.",
    "AUTH_FAILED": "Re-pair the selected connection to refresh its credential; no other connection was selected.",
    "IDENTITY_MISMATCH": "The responding host/vault is not the selected target. Use the intended paired connection or restart the intended Bridge.",
    "BRIDGE_UPDATE_REQUIRED": "Update and restart the selected host Bridge to expose host/vault identity.",
}


def setup_status() -> dict[str, Any]:
    runtime = {"version": _read_json(ROOT / "plugin.json").get("version"), "path": str(ROOT)}
    try:
        config = effective_connection()
        probe = _bridge_probe(config)
    except ConnectionSelectionRequired as error:
        config = {"mode": "remote"} if all(p["config"].get("mode") == "remote" for p in error.profiles) else {}
        probe = {"connected": False, "ready": False, "code": "SELECTION_REQUIRED"}
    except ValueError as error:
        return {"configured": False, "connected": False, "ready": False, "code": "CONFIG_INVALID", "readiness": "broken",
                "runtime": runtime, "mode": "unknown", "state_directory": str(state_directory()),
                "reason": str(error), "remediation": _REMEDIATION["CONFIG_INVALID"], "config_path": str(connection_path()),
                "connections": [], "available_vaults": [], "needs_vault_selection": False}
    remote = config.get("mode") == "remote"
    catalog = _catalog(config, connection_profiles(remote=remote), selected_probe=probe, probe_all=False)
    try:
        registry_error = None
        if remote:
            available = discover_vaults() if probe["connected"] else []
            if not probe["connected"]:
                registry_error = "The selected host is unavailable; known paired profiles remain listed."
        else:
            available = _local_vaults()
            observed_vault = probe.get("status", {}).get("vault") or {}
            if not isinstance(observed_vault, dict):
                observed_vault = {}
            for vault in available:
                vault["selected"] = vault["id"] == config.get("vault_id") or vault["path"] == config.get("vault_path")
                vault["running"] = probe["connected"] and vault["id"] == observed_vault.get("id")
    except (OSError, ValueError) as error:
        available, registry_error = [], str(error)
    unbound = not config and not connection_path().exists() and not os.environ.get("EXCALIDRAW_AGENT_CONFIG")
    if probe["code"] == "NOT_CONFIGURED" and unbound and (len([v for v in available if v.get("pluginEnabled")]) > 1 or catalog["needs_selection"]):
        probe["code"] = "SELECTION_REQUIRED"
    observed = _public_status(probe.pop("status", {}))
    bridge_url = config.get("bridge_url")
    try:
        parsed_url = urllib.parse.urlsplit(bridge_url or "")
        if parsed_url.username or parsed_url.password or parsed_url.query or parsed_url.fragment:
            bridge_url = None
    except ValueError:
        bridge_url = None
    return {"configured": bool(config.get("bridge_token")), "config_path": str(connection_path()),
            "runtime": runtime,
            "mode": "remote" if remote else "local", "rendering_location": "host" if remote else "local",
            "remote_host": config.get("remote_host"), "host_vault_path": config.get("host_vault_path") if remote else None,
            "vault_path": None if remote else config.get("vault_path"), "vault_name": config.get("vault_name"),
            "bridge_url": bridge_url, "state_directory": str(state_directory()),
            "available_vaults": available, **catalog, **probe, "status": observed,
            "host": observed.get("host"), "vault": observed.get("vault"), "plugin_version": observed.get("pluginVersion"),
            "open_canvases": observed.get("openCanvases", []), "engines": observed.get("engines", {}),
            "readiness": "ready" if probe["ready"] else ("connected" if probe["connected"] else "broken"),
            "remediation": _REMEDIATION[probe["code"]], "needs_vault_selection": probe["code"] == "SELECTION_REQUIRED",
            **({"vault_registry_error": registry_error} if registry_error else {})}


def _launch_uri(uri: str) -> None:
    if sys.platform == "win32":
        os.startfile(uri)
    elif sys.platform == "darwin":
        subprocess.run(["open", uri], check=True)
    else:
        subprocess.run(["xdg-open", uri], check=True)


def start_bridge(open_uri: bool = True, wait_seconds: float = 15) -> dict[str, Any]:
    config = load_connection()
    if config.get("mode") == "remote":
        raise ValueError("Remote rendering connection: start Obsidian/Bridge and the SSH tunnel on the host machine, not on this headless client.")
    if not config.get("vault_path") or not config.get("bridge_script"):
        raise ValueError("Select a vault with connect before starting the Bridge")
    vault = Path(config["vault_path"])
    bootstrap = config["bootstrap_script"]
    script_name = PurePosixPath(bootstrap).with_suffix("").as_posix()
    script_folder = config["script_folder"].rstrip("/") + "/"
    if not script_name.startswith(script_folder):
        raise ValueError("Bootstrap is outside the configured script folder")
    command = PLUGIN_ID + ":" + script_name[len(script_folder):]
    uri = "obsidian://adv-uri?" + urllib.parse.urlencode({"vault": config["vault_name"], "commandid": command})
    community_file = vault / config.get("obsidian_config_dir", ".obsidian") / "community-plugins.json"
    enabled = _read_json(community_file) if community_file.is_file() else []
    can_open = "obsidian-advanced-uri" in enabled
    launched = False
    if open_uri and can_open:
        _launch_uri(uri)
        launched = True
    result = {"command_id": command, "start_uri": uri, "launched": launched,
              "manual_instruction": "Open this vault in Obsidian and run the Agent-Drawing/mcp/Start-Agent-Drawing script from the command palette. If new scripts are not indexed yet, reload Obsidian once.",
              "advanced_uri_enabled": can_open}
    if launched:
        deadline = time.monotonic() + wait_seconds
        while True:
            probe = _bridge_probe(config)
            if probe["connected"] or time.monotonic() >= deadline:
                return {**result, **probe}
            time.sleep(0.25)
    return {**result, **_bridge_probe(config)}


def connect_vault(vault_path: str | None = None, vault_name: str | None = None,
                  port: int | None = None, open_uri: bool = True,
                  obsidian_config_dir: str = ".obsidian") -> dict[str, Any]:
    try:
        current = effective_connection()
    except ConnectionSelectionRequired:
        current = {}
        if not vault_path and not vault_name:
            return setup_status()
    remote = current.get("mode") == "remote"
    if remote and vault_path:
        raise ValueError("Remote rendering connection: explicit vault paths cannot deploy scripts on this headless client.")
    if vault_name and not vault_path:
        profiles = connection_profiles(remote=remote)
        matches = [profile for profile in profiles if vault_name in (profile["id"], profile["config"].get("vault_id"), profile["config"].get("vault_name"))]
        if len(matches) == 1:
            selected_config = matches[0]["config"]
            if remote or selected_config.get("mode") == "remote" or not selected_config.get("vault_path"):
                return select_connection(matches[0]["id"])
            select_connection(matches[0]["id"])
            current = effective_connection()
            vault_path = current["vault_path"]
            vault_name = None
        if len(matches) > 1:
            raise ValueError("Ambiguous connection name; select a connection id")
    if not vault_path and not vault_name and (current.get("bridge_token") or connection_path().exists() or
            any(key in os.environ for key in ("EXCALIDRAW_AGENT_CONFIG", "EXCALIDRAW_BRIDGE_URL", "EXCALIDRAW_BRIDGE_TOKEN"))):
        if remote or not current.get("vault_path"):
            return setup_status()
        # Refresh only the already selected local vault; never fall through to another registry candidate.
        vault_path = current["vault_path"]
    candidates = discover_vaults() if vault_name or not vault_path else []
    if vault_name:
        matches = [entry for entry in candidates if vault_name in (entry["id"], entry["name"])]
        if len(matches) != 1:
            raise ValueError("Unknown registered vault selector" if not matches else "Ambiguous vault name; select an id")
        chosen = matches[0]
        if vault_path and Path(vault_path).expanduser().resolve() != Path(chosen["path"]).resolve():
            raise ValueError("vault_name selects a different registered vault than vault_path")
        vault_path = chosen["path"]
    if remote:
        return {**setup_status(), "needs_vault_selection": True, "code": "SELECTION_REQUIRED",
                "instruction": "Select a known paired profile with use; new remote vaults must be paired on the host."}
    if not vault_path:
        eligible = [entry for entry in candidates if entry.get("pluginEnabled")]
        if len(eligible) != 1:
            return {**setup_status(), "needs_vault_selection": True, "available_vaults": candidates,
                    "code": "SELECTION_REQUIRED" if eligible else "NOT_CONFIGURED",
                    "instruction": "Select an eligible registered vault id/name or an explicit vault_path; no vault has been changed."}
        vault_path = eligible[0]["path"]
    vault = Path(vault_path).expanduser().resolve()
    if not vault.is_dir():
        raise ValueError("The selected vault does not exist")
    config_root = _inside(vault, obsidian_config_dir)
    plugin_root = config_root / "plugins" / PLUGIN_ID
    manifest_path = plugin_root / "manifest.json"
    if not manifest_path.is_file():
        raise ValueError("Install Excalidraw-ymjr in this vault first: https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr")
    manifest = _read_json(manifest_path)
    if manifest.get("id") != PLUGIN_ID or not (plugin_root / "main.js").is_file():
        raise ValueError("The vault does not contain a complete Excalidraw-ymjr plugin installation")
    enabled_path = config_root / "community-plugins.json"
    enabled = _read_json(enabled_path) if enabled_path.is_file() else []
    if PLUGIN_ID not in enabled:
        raise ValueError("Enable Excalidraw-ymjr in Obsidian before connecting; the installer does not change plugin permissions")
    data_path = plugin_root / "data.json"
    settings = _read_json(data_path) if data_path.is_file() else {}
    script_folder = settings.get("scriptFolderPath") or "Excalidraw/Scripts"
    # The user's plugin configuration explicitly authorizes this script root,
    # including Obsidian vault junctions/symlinks to a shared script directory.
    relative_folder = str(script_folder).replace("\\", "/").rstrip("/")
    folder_parts = PurePosixPath(relative_folder)
    if not relative_folder or folder_parts.is_absolute() or ".." in folder_parts.parts or ":" in relative_folder:
        raise ValueError("The configured script folder must be vault-relative")
    script_root = (vault / relative_folder).resolve()
    destination = _inside(script_root, "Agent-Drawing")
    bundle = _read_json(ROOT / "bridge/bundle.json")
    scripts = bundle["scripts"]
    source_root = ROOT / "bridge/Scripts"
    install_record = state_directory() / "installation.json"
    previous = _read_json(install_record) if install_record.is_file() else {}
    previous_hashes = previous.get("files", {}) if previous.get("destination") == str(destination) else {}
    staged = []
    for relative in scripts:
        source = _inside(source_root, relative)
        target = _inside(destination, relative)
        content = source.read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        if target.exists():
            existing_digest = hashlib.sha256(target.read_bytes()).hexdigest()
            if existing_digest != digest and previous_hashes.get(relative) != existing_digest:
                raise ValueError(f"Refusing to overwrite a modified or unmanaged script: {relative}")
        staged.append((relative, target, content, digest))
    private_path = connection_path().resolve()
    if private_path.is_relative_to(vault) or private_path.is_relative_to(ROOT):
        raise ValueError("Private connection configuration must stay outside the vault and the installed package")
    previous_connection = load_connection()
    same_vault = previous_connection.get("vault_path") == str(vault)
    chosen_port = port if port is not None else (previous_connection.get("port", 27124) if same_vault else 27124)
    if isinstance(chosen_port, bool) or not isinstance(chosen_port, int) or not 1024 <= chosen_port <= 65535:
        raise ValueError("Bridge port must be an integer between 1024 and 65535")
    token = previous_connection.get("bridge_token") if same_vault else None
    token = token or secrets.token_hex(32)
    bootstrap = str(script_folder).rstrip("/") + "/Agent-Drawing/" + bundle["bootstrap"]
    bridge_script = str(script_folder).rstrip("/") + "/Agent-Drawing/" + bundle["bridge"]
    config = {"bridge_url": f"http://127.0.0.1:{chosen_port}", "bridge_token": token,
              "bridge_timeout": 180, "port": chosen_port, "vault_path": str(vault),
              "vault_name": vault.name, "vault_id": vault_identity(str(vault)), "plugin_id": PLUGIN_ID,
              "script_folder": script_folder, "bootstrap_script": bootstrap,
              "bridge_script": bridge_script, "obsidian_config_dir": obsidian_config_dir}
    _private_write(private_path, config)
    _private_write(state_directory() / "connections" / (config["vault_id"] + ".json"), config)
    deployed = {}
    for relative, target, content, digest in staged:
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_name(target.name + ".agent-install.tmp")
        temporary.write_bytes(content)
        temporary.replace(target)
        deployed[relative] = digest
    descriptor = destination / "mcp/Agent-Bridge-Connection.json"
    _private_write(descriptor, {"configPath": str(private_path)})
    _private_write(install_record, {"destination": str(destination), "files": deployed, "version": _read_json(ROOT / "plugin.json")["version"]})
    result = {"configured": True, "vault_path": str(vault), "deployed_scripts": len(deployed),
              "script_directory": str(destination), "config_path": str(private_path),
              "token_disclosed": False, "plugin_version": manifest.get("version"),
              "note": "The generated token stays outside the vault. Plugin and autostart permissions were not changed."}
    return {**result, **start_bridge(open_uri=open_uri)}
