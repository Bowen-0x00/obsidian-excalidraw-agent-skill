"""Small named styles; layout stays deterministic and native library appearance stays intact."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

PROFILES = {
    "professional": {
        "description": "平整、克制的文档图；浅色背景与语义色。",
        "fontFamily": "Helvetica", "fontSize": 20,
        "shape": {"roughness": 0, "fillStyle": "solid", "strokeWidth": 2, "edge": "round"},
        "text": {"strokeColor": "#1e293b", "lineHeight": 1.2},
        "edge": {"strokeColor": "#64748b", "strokeWidth": 2, "roughness": 0, "edge": "sharp"},
        "container": {"strokeColor": "#94a3b8", "backgroundColor": "#f8fafc", "fillStyle": "solid", "roughness": 0, "strokeWidth": 1.5},
    },
    "handdrawn": {
        "description": "真实Rough.js手绘风格；自由笔画另用draw，不用图片模拟。",
        "fontFamily": "Helvetica", "fontSize": 20,
        "shape": {"roughness": 1, "fillStyle": "hachure", "strokeWidth": 2, "edge": "round"},
        "text": {"strokeColor": "#1e293b", "lineHeight": 1.2},
        "edge": {"strokeColor": "#475569", "strokeWidth": 2, "roughness": 1, "edge": "round"},
        "container": {"strokeColor": "#64748b", "backgroundColor": "transparent", "fillStyle": "hachure", "roughness": 1, "strokeWidth": 1.5},
    },
    "visio": {
        "description": "精确对齐、直角、低粗糙度的工程/Visio风格。不是Visio文件格式。",
        "fontFamily": "Helvetica", "fontSize": 20,
        "shape": {"roughness": 0, "fillStyle": "solid", "strokeWidth": 1.5, "edge": "sharp"},
        "text": {"strokeColor": "#172554", "lineHeight": 1.2},
        "edge": {"strokeColor": "#334155", "strokeWidth": 1.5, "roughness": 0, "edge": "sharp"},
        "container": {"strokeColor": "#64748b", "backgroundColor": "#f8fafc", "fillStyle": "solid", "roughness": 0, "strokeWidth": 1.5, "edge": "sharp"},
    },
    "blueprint": {
        "description": "白底蓝线的电路/微架构工程表达；素材本身默认不重新染色。",
        "fontFamily": "Helvetica", "fontSize": 20,
        "shape": {"roughness": 0, "fillStyle": "solid", "strokeWidth": 1.5, "edge": "sharp", "strokeColor": "#1d4ed8", "backgroundColor": "#eff6ff"},
        "text": {"strokeColor": "#1e3a8a", "lineHeight": 1.2},
        "edge": {"strokeColor": "#2563eb", "strokeWidth": 1.5, "roughness": 0, "edge": "sharp"},
        "container": {"strokeColor": "#93c5fd", "backgroundColor": "transparent", "fillStyle": "solid", "roughness": 0, "strokeWidth": 1.5},
    },
    "presentation": {
        "description": "演示页清晰层级；素材库版式优先保留，标题/正文由原生字体测量。",
        "fontFamily": "Helvetica", "fontSize": 24,
        "shape": {"roughness": 0, "fillStyle": "solid", "strokeWidth": 2, "edge": "round"},
        "text": {"strokeColor": "#0f172a", "lineHeight": 1.25},
        "edge": {"strokeColor": "#475569", "strokeWidth": 2, "roughness": 0, "edge": "sharp"},
        "container": {"strokeColor": "#cbd5e1", "backgroundColor": "#ffffff", "fillStyle": "solid", "roughness": 0, "strokeWidth": 1.5},
    },
}
ALIASES = {"手绘": "handdrawn", "hand-drawn": "handdrawn", "roughjs": "handdrawn", "rough-js": "handdrawn", "visio-style": "visio", "专业": "professional", "ppt": "presentation"}


def resolve_style(style: str | dict[str, Any] | None = None) -> dict[str, Any]:
    if style is None:
        name, overrides = "professional", {}
    elif isinstance(style, str):
        name, overrides = ALIASES.get(style, style), {}
    elif isinstance(style, dict):
        name = ALIASES.get(str(style.get("profile", "professional")), str(style.get("profile", "professional")))
        overrides = style
    else:
        raise ValueError("style must be a named profile or a profile object")
    if name not in PROFILES:
        raise ValueError(f"Unknown style {name}; available: {', '.join(PROFILES)}")
    result = {"name": name, **deepcopy(PROFILES[name])}
    allowed = {"fontFamily", "fontSize", "shape", "text", "edge", "container", "profile"}
    if set(overrides) - allowed:
        raise ValueError(f"Unsupported style fields: {sorted(set(overrides) - allowed)}")
    for key, value in overrides.items():
        if key == "profile":
            continue
        if key in ("shape", "text", "edge", "container"):
            if not isinstance(value, dict):
                raise ValueError(f"style.{key} must be an object")
            result[key].update(value)
        else:
            result[key] = value
    return result


def style_catalog() -> dict[str, Any]:
    return {"styles": [{"name": name, "description": data["description"], "defaults": deepcopy(data)} for name, data in PROFILES.items()],
            "aliases": dict(ALIASES),
            "precedence": "native library style preserved; profile < role/variant < explicit local style; hard protections cannot be overridden"}
