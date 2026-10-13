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

from runtime_config import connection_path, load_connection, state_directory

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


def discover_vaults() -> list[dict[str, str]]:
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
    result = []
    for vault_id, entry in data.get("vaults", {}).items():
        candidate = Path(entry.get("path", "")).expanduser()
        if entry.get("path") and candidate.is_dir():
            result.append({"id": vault_id, "name": candidate.name, "path": str(candidate.resolve())})
    return result


def _bridge_probe(config: dict[str, Any]) -> dict[str, Any]:
    url = str(config.get("bridge_url", ""))
    token = config.get("bridge_token")
    if not url or not token:
        return {"connected": False, "reason": "Not connected. Run drawing_setup(action='connect') or launcher.py connect."}
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "http" or parsed.hostname not in ("127.0.0.1", "localhost", "::1") or parsed.username or parsed.password:
        raise ValueError("The Bridge URL must be an HTTP loopback address")
    request = urllib.request.Request(url.rstrip("/") + "/v3/status", headers={"Authorization": "Bearer " + token})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(request, timeout=3) as response:
            status = json.load(response)
        expected_script = config.get("bridge_script")
        correct_target = not expected_script or status.get("scriptPath") == expected_script
        return {"connected": status.get("ok") is True and correct_target, "status": status,
                **({} if correct_target else {"reason": "Another Bridge is responding; start the connected vault bundle or choose a different port."})}
    except (OSError, ValueError) as error:
        return {"connected": False, "reason": str(error)}


def setup_status() -> dict[str, Any]:
    config = load_connection()
    remote = config.get("mode") == "remote"
    return {"configured": bool(config.get("bridge_token")), "config_path": str(connection_path()),
            "mode": "remote" if remote else "local",
            "rendering_location": "host" if remote else "local",
            "remote_host": config.get("remote_host"),
            "host_vault_path": config.get("host_vault_path") if remote else None,
            "vault_path": None if remote else config.get("vault_path"), "vault_name": config.get("vault_name"),
            "bridge_url": config.get("bridge_url"), "state_directory": str(state_directory()),
            "available_vaults": [] if remote else discover_vaults(), **_bridge_probe(config)}


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
    if load_connection().get("mode") == "remote":
        raise ValueError("Remote rendering connection: select/connect the vault on the host machine; this client must not deploy vault scripts.")
    candidates = discover_vaults()
    if not vault_path:
        if len(candidates) != 1:
            return {"configured": False, "needs_vault_selection": True, "available_vaults": candidates,
                    "instruction": "Select the intended vault_path; no vault has been changed."}
        vault_path = candidates[0]["path"]
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
              "vault_name": vault_name or vault.name, "plugin_id": PLUGIN_ID,
              "script_folder": script_folder, "bootstrap_script": bootstrap,
              "bridge_script": bridge_script, "obsidian_config_dir": obsidian_config_dir}
    _private_write(private_path, config)
    deployed = {}
    for relative, target, content, digest in staged:
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_name(target.name + ".agent-install.tmp")
        temporary.write_bytes(content)
        temporary.replace(target)
        deployed[relative] = digest
    descriptor = destination / "mcp/Agent-Bridge-Connection.json"
    _private_write(descriptor, {"configPath": str(private_path)})
    _private_write(install_record, {"destination": str(destination), "files": deployed, "version": "0.6.1"})
    result = {"configured": True, "vault_path": str(vault), "deployed_scripts": len(deployed),
              "script_directory": str(destination), "config_path": str(private_path),
              "token_disclosed": False, "plugin_version": manifest.get("version"),
              "note": "The generated token stays outside the vault. Plugin and autostart permissions were not changed."}
    return {**result, **start_bridge(open_uri=open_uri)}
