"""Task-specific, bundled drawing instructions returned by the real start tool."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Literal

SKILL_ROOT = Path(__file__).resolve().parents[1] / "skills" / "obsidian-excalidraw"
DiagramType = Literal[
    "auto",
    "general",
    "microarchitecture",
    "circuit",
    "math",
    "physical_structure",
    "explanatory_page",
    "teaching",
]
DIAGRAM_TYPES = (
    "auto",
    "general",
    "microarchitecture",
    "circuit",
    "math",
    "physical_structure",
    "explanatory_page",
    "teaching",
)


def teaching_requested(request: str) -> bool:
    return bool(re.search(r"教学|学习|教程|图解|示意图|讲解|机制|工作原理|画出|可视化解释|\b(?:teach|tutorial|learning|explain|mechanism)\b", request, re.I))


def diagram_type(request: str, requested: str = "auto") -> str:
    if requested not in DIAGRAM_TYPES:
        raise ValueError("diagram_type must be " + "/".join(DIAGRAM_TYPES))
    # Select representation by the expressed relationship/view, not subject alone.
    physical = re.search(
        r"剖[面切]|截面|爆炸图|斜投影|层叠|分层结构|封装结构|封装.*(?:图|讲解)|封装示意|\b(?:cross.section|cutaway|exploded|oblique|package stack)\b",
        request,
        re.I,
    )
    logical = re.search(
        r"微架构|数据通路|寄存器堆|逻辑门|电路|\b(?:ALU|MUX|RTL|datapath|microarchitecture|circuit)\b",
        request,
        re.I,
    )
    if requested in ("physical_structure", "explanatory_page"):
        if requested == "explanatory_page" and logical and not physical:
            # Page is a carrier, not permission to drop a declared logical network.
            return (
                "circuit"
                if re.search(r"电路|逻辑门|\bcircuit\b", request, re.I)
                else "microarchitecture"
            )
        return requested
    if physical:
        return "physical_structure"
    if logical:
        return (
            "circuit"
            if re.search(r"电路|逻辑门|\bcircuit\b", request, re.I)
            else "microarchitecture"
        )
    if re.search(r"讲解页|演示页|信息图|\b(?:PPT|slide|infographic)\b", request, re.I):
        return "explanatory_page"
    if teaching_requested(request):
        return "teaching"
    if requested != "auto":
        return requested
    if re.search(r"\bCPU\b|硬件|流水线|缓存层级|片上互连", request, re.I):
        return "microarchitecture"
    if re.search(r"矩阵|转置|分式|求和|递推|LaTeX|matrix|transpose", request, re.I):
        return "math"
    return "general"


def guidance(kind: str, request: str = "") -> dict:
    names = [
        "SKILL.md",
        "references/visual-design.md",
        "references/diagram-recipes.md",
        "references/acceptance.md",
        "references/typography.md",
        "references/workflow-details.md",
    ]
    if kind == "teaching" or teaching_requested(request):
        names.append("references/teaching-design.md")
    if kind in ("microarchitecture", "circuit"):
        names.append("references/microarchitecture.md")
    if kind in ("physical_structure", "explanatory_page"):
        names.extend(
            ["references/technical-illustration.md", "references/native-features.md"]
        )
    if kind == "math" or re.search(
        r"矩阵|转置|分式|求和|递推|LaTeX|matrix|transpose", request, re.I
    ):
        names.append("references/visual-content.md")
    documents = []
    for name in names:
        data = (SKILL_ROOT / name).read_bytes()
        documents.append(
            {
                "path": name,
                "sha256": hashlib.sha256(data).hexdigest(),
                "content": data.decode("utf-8"),
            }
        )
    logical = kind in ("microarchitecture", "circuit")
    return {
        "diagram_type": kind,
        "representation_required": logical,
        "design_confirmation_required": kind == "teaching" or teaching_requested(request),
        "design_step": "What visual structure explains the objective? Propose 2–3 actual alternatives with a recommendation; use the client's ask UI before creation. Cite explicit delegation/inheritance only when real. Style/color choice does not select an expression method.",
        "documents": documents,
        "relation_strategy": "ports_and_signals"
        if logical
        else "physical_and_annotation"
        if kind == "physical_structure"
        else "composition",
        "workflow": [
            "analyze purpose, reference evidence, relations and view before picking shapes",
            "resolve cited preferences and requirements",
            "declare a logical network only for logical diagrams; never invent signals for a physical section",
            "create/bind one task canvas",
            "apply validated native operations",
            "use deterministic projection/stack/array/leader geometry when appropriate",
            "inspect the current PNG and repair locally",
            "record all requirement checks with drawing_review",
            "drawing_deliver verifies the same file/revision/PNG/review",
        ],
        "trust": "Bundled instructions are not proof of model understanding or truthful user evidence. Physical projection is a 2D schematic, not CAD/electrical/scientific certification.",
    }
