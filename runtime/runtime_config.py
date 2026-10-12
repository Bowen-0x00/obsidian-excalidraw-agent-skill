from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

CONNECTION_KEYS = (
    "bridge_url",
    "bridge_token",
    "bridge_timeout",
    "vault_path",
    "vault_name",
    "plugin_id",
    "script_folder",
    "bridge_script",
)


def state_directory() -> Path:
    """Return the base state directory for the Excalidraw Agent.

    Honors EXCALIDRAW_AGENT_STATE_DIR environment variable if provided.
    Otherwise defaults to platform-specific user data directory:
      - Windows: %LOCALAPPDATA%/ObsidianExcalidrawAgent
      - macOS: ~/Library/Application Support/ObsidianExcalidrawAgent
      - Linux/POSIX: $XDG_DATA_HOME/obsidian-excalidraw-agent or ~/.local/share/obsidian-excalidraw-agent
    """
    override = os.environ.get("EXCALIDRAW_AGENT_STATE_DIR")
    if override:
        return Path(override).expanduser().resolve()

    if sys.platform == "win32":
        local_app_data = os.environ.get("LOCALAPPDATA")
        base = Path(local_app_data) if local_app_data else Path.home() / "AppData" / "Local"
        return (base / "ObsidianExcalidrawAgent").resolve()
    elif sys.platform == "darwin":
        return (Path.home() / "Library" / "Application Support" / "ObsidianExcalidrawAgent").resolve()
    else:
        xdg_data = os.environ.get("XDG_DATA_HOME")
        base = Path(xdg_data) if xdg_data else Path.home() / ".local" / "share"
        return (base / "obsidian-excalidraw-agent").resolve()


def connection_path() -> Path:
    """Return path to the private connection configuration JSON.

    Honors EXCALIDRAW_AGENT_CONFIG environment variable if provided,
    otherwise defaults to state_directory() / "connection.json".
    """
    override = os.environ.get("EXCALIDRAW_AGENT_CONFIG")
    if override:
        return Path(override).expanduser().resolve()
    return state_directory() / "connection.json"


def load_connection() -> dict[str, Any]:
    """Load private connection settings from disk.

    Returns an empty dict if connection.json is absent.
    Raises ValueError if the file exists but contains invalid JSON or non-object content.
    Never ignores malformed configuration silently.
    """
    path = connection_path()
    if not path.exists():
        return {}
    try:
        raw = path.read_text(encoding="utf-8")
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError(f"Connection config at {path} must be a JSON object, got {type(data).__name__}")
        return data
    except json.JSONDecodeError as err:
        raise ValueError(f"Malformed connection config at {path}: {err}") from err


def artifact_directory() -> Path:
    """Return path to the artifacts directory inside state directory."""
    return state_directory() / "artifacts"
