from __future__ import annotations

import hashlib
import json
import ntpath
import os
import posixpath
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

CONNECTION_KEYS = ("bridge_url", "bridge_token", "bridge_timeout", "vault_path", "vault_name",
                   "plugin_id", "script_folder", "bridge_script", "host_id", "host_name", "vault_id")


class ConnectionSelectionRequired(ValueError):
    def __init__(self, profiles: list[dict[str, Any]]) -> None:
        super().__init__("Multiple live connections are available; select a connection by id or unique name.")
        self.profiles = profiles


def default_state_directory() -> Path:
    """Host-published profiles use the platform default, not the client override."""
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData/Local")))
        return (base / "ObsidianExcalidrawAgent").resolve()
    if sys.platform == "darwin":
        return (Path.home() / "Library/Application Support/ObsidianExcalidrawAgent").resolve()
    return (Path(os.environ.get("XDG_DATA_HOME", str(Path.home() / ".local/share"))) / "obsidian-excalidraw-agent").resolve()


def state_directory() -> Path:
    override = os.environ.get("EXCALIDRAW_AGENT_STATE_DIR")
    return Path(override).expanduser().resolve() if override else default_state_directory()


def connection_path() -> Path:
    override = os.environ.get("EXCALIDRAW_AGENT_CONFIG")
    return Path(override).expanduser().resolve() if override else state_directory() / "connection.json"


def read_connection(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ValueError(f"Cannot read connection config at {path}: {error}") from error
    if not isinstance(data, dict):
        raise ValueError(f"Connection config at {path} must be a JSON object")
    for key in (*CONNECTION_KEYS, "mode", "host_vault_path", "connection_id"):
        if key in data and key != "bridge_timeout" and not isinstance(data[key], str):
            raise ValueError(f"Connection config field {key} at {path} must be a string")
    if "mode" in data and data["mode"] not in ("local", "remote"):
        raise ValueError(f"Unknown connection mode at {path}")
    if "bridge_timeout" in data:
        try:
            if float(data["bridge_timeout"]) <= 0:
                raise ValueError()
        except (TypeError, ValueError) as error:
            raise ValueError(f"Invalid bridge_timeout at {path}") from error
    return data


def path_identity(path: str, platform: str | None = None) -> str:
    windows = platform == "win32" or bool(ntpath.splitdrive(path)[0])
    return ntpath.normpath(path).replace("\\", "/").lower() if windows else posixpath.normpath(path)


def vault_identity(path: str) -> str:
    normalized = path_identity(str(Path(path).expanduser().resolve()), sys.platform)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:24]


def connection_identity_mismatches(config: dict[str, Any], status: dict[str, Any]) -> list[str]:
    host = status.get("host") if isinstance(status.get("host"), dict) else {}
    vault = status.get("vault") if isinstance(status.get("vault"), dict) else {}
    issues = []
    for key, actual in (("host_id", host.get("id")), ("vault_id", vault.get("id"))):
        if config.get(key) and config[key] != actual:
            issues.append(key)
    expected_path = config.get("host_vault_path") if config.get("mode") == "remote" else config.get("vault_path")
    if expected_path and (not vault.get("path") or path_identity(expected_path, host.get("platform")) != path_identity(vault["path"], host.get("platform"))):
        issues.append("vault_path")
    if config.get("bridge_script") and config["bridge_script"] != status.get("scriptPath"):
        issues.append("bridge_script")
    return issues


def missing_connection_identity(config: dict[str, Any], status: dict[str, Any]) -> bool:
    host = status.get("host") if isinstance(status.get("host"), dict) else {}
    vault = status.get("vault") if isinstance(status.get("vault"), dict) else {}
    expected_path = config.get("host_vault_path") if config.get("mode") == "remote" else config.get("vault_path")
    return bool((config.get("host_id") and not host.get("id")) or
                (config.get("vault_id") and not vault.get("id")) or (expected_path and not vault.get("path")))


def bridge_get(config: dict[str, Any], route: str) -> dict[str, Any]:
    url, token = config.get("bridge_url"), config.get("bridge_token")
    if not url or not token:
        raise ValueError("Bridge URL and credential are required")
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "http" or parsed.hostname not in ("127.0.0.1", "localhost", "::1") or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError("The Bridge URL must be an HTTP loopback address")
    request = urllib.request.Request(url.rstrip("/") + route, headers={"Authorization": "Bearer " + token})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(request, timeout=3) as response:
        result = json.load(response)
    if not isinstance(result, dict):
        raise ValueError("Bridge response must be a JSON object")
    return result


def probe_connection(config: dict[str, Any]) -> dict[str, Any]:
    if not config.get("bridge_token") or not config.get("bridge_url"):
        return {"connected": False, "ready": False, "code": "NOT_CONFIGURED", "reason": "No complete Bridge connection is configured."}
    try:
        status = bridge_get(config, "/v3/status")
        if status.get("ok") is not True:
            return {"connected": False, "ready": False, "code": "CONNECTION_FAILED", "reason": "Bridge did not report success."}
        mismatches = connection_identity_mismatches(config, status)
        if mismatches:
            missing_identity = missing_connection_identity(config, status)
            return {"connected": False, "ready": False, "code": "BRIDGE_UPDATE_REQUIRED" if missing_identity else "IDENTITY_MISMATCH",
                    "reason": "Observed Bridge does not match the configured host/vault identity.", "identity_mismatches": mismatches, "status": status}
        ready = status.get("ready") is True
        return {"connected": True, "ready": ready, "code": "READY" if ready else "NO_CANVAS", "status": status}
    except urllib.error.HTTPError as error:
        return {"connected": False, "ready": False, "code": "AUTH_FAILED" if error.code in (401, 403) else "CONNECTION_FAILED", "reason": f"Bridge HTTP {error.code}"}
    except (OSError, ValueError) as error:
        return {"connected": False, "ready": False, "code": "CONNECTION_FAILED", "reason": str(error)}


def connection_profiles(*, remote: bool = False) -> list[dict[str, Any]]:
    """Read paired profiles only; never scan vault paths or other hosts state."""
    roots = [state_directory()]
    if not remote and default_state_directory() not in roots:
        roots.append(default_state_directory())
    profiles = []
    identities = set()
    for root in roots:
        for path in sorted((root / "connections").glob("*.json")):
            try:
                config = read_connection(path)
                if not config.get("bridge_url") or not config.get("bridge_token"):
                    continue
            except ValueError:
                continue
            if remote and config.get("mode") != "remote":
                continue
            if not remote and config.get("mode") == "remote" and root != state_directory():
                continue
            identity = (config.get("host_id"), config.get("vault_id"), config.get("bridge_url"))
            if identity in identities:
                continue
            identities.add(identity)
            profiles.append({"id": config.get("connection_id") or path.stem, "config_path": str(path), "config": config})
    return profiles


def load_connection() -> dict[str, Any]:
    """Honor explicit bindings; only auto-select a unique authenticated live profile."""
    path = connection_path()
    if path.exists():
        config = read_connection(path)
        if config.get("connection_id"):
            matches = [p for p in connection_profiles(remote=config.get("mode") == "remote") if p["id"] == config["connection_id"]]
            if len(matches) != 1:
                raise ValueError("Configured connection_id is unknown or ambiguous")
            return matches[0]["config"]
        return config
    if os.environ.get("EXCALIDRAW_AGENT_CONFIG"):
        raise ValueError(f"Explicit connection config does not exist: {path}")
    if any(key in os.environ for key in ("EXCALIDRAW_BRIDGE_URL", "EXCALIDRAW_BRIDGE_TOKEN")):
        return {}
    live = [profile for profile in connection_profiles() if probe_connection(profile["config"])["connected"]]
    if len(live) > 1:
        raise ConnectionSelectionRequired(live)
    return live[0]["config"] if live else {}


def effective_connection() -> dict[str, Any]:
    config = dict(load_connection())
    for suffix, key in (("URL", "bridge_url"), ("TOKEN", "bridge_token"), ("TIMEOUT", "bridge_timeout")):
        value = os.environ.get("EXCALIDRAW_BRIDGE_" + suffix)
        if value is not None:
            config[key] = value
    return config


def artifact_directory() -> Path:
    return state_directory() / "artifacts"
