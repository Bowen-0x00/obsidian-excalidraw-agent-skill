"""Task-specific, bundled drawing instructions returned by the real start tool."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1] / "skills" / "obsidian-excalidraw"
DIAGRAM_TYPES = ("auto", "general", "microarchitecture", "circuit", "math")


def diagram_type(request: str, requested: str = "auto") -> str:
    if requested not in DIAGRAM_TYPES:
        raise ValueError("diagram_type must be auto/general/microarchitecture/circuit/math")
    # Routing cues select required references; they do not infer scientific truth.
    hardware = re.search(r"\b(?:CPU|ALU|MUX|RTL|datapath|microarchitecture)\b|微架构|数据通路|寄存器堆|硬件", request, re.I)
    circuit = re.search(r"\bcircuit\b|电路|逻辑门", request, re.I)
    if hardware or circuit:
        return "circuit" if circuit and not hardware else "microarchitecture"
    if requested != "auto":
        return requested
    return "math" if re.search(r"矩阵|转置|分式|求和|递推|LaTeX|matrix|transpose", request, re.I) else "general"


def guidance(kind: str, request: str = "") -> dict:
    names = ["SKILL.md", "references/diagram-recipes.md", "references/acceptance.md", "references/typography.md", "references/workflow-details.md"]
    if kind in ("microarchitecture", "circuit"):
        names.append("references/microarchitecture.md")
    if kind == "math" or re.search(r"矩阵|转置|分式|求和|递推|LaTeX|matrix|transpose", request, re.I):
        names.append("references/visual-content.md")
    documents = []
    for name in names:
        path = SKILL_ROOT / name
        data = path.read_bytes()  # missing bundled guidance is an explicit failure
        documents.append({"path": name, "sha256": hashlib.sha256(data).hexdigest(), "content": data.decode("utf-8")})
    return {"diagram_type": kind, "documents": documents,
            "representation_required": kind in ("microarchitecture", "circuit"),
            "workflow": ["resolve cited preferences and requirements", "declare component/port/signal contract when required",
                         "create/bind one task canvas", "apply validated native operations", "map saved native IDs with drawing_contract",
                         "inspect the current PNG and repair locally", "record all requirement checks with drawing_review", "drawing_deliver verifies the same file/revision/PNG/review"],
            "trust": "These are bundled instructions, not proof that the model read them or that user evidence is true. No electrical/scientific correctness certification."}
