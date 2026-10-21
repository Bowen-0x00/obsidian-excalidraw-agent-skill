"""Editable 2.5D packaging teaching figure; native primitives, not a traced bitmap.

Use one explicit canvas/brief/state for every update. Dimensions/counts are schematic.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "runtime"))
from drawing_client import DrawingClient
from illustration_geometry import project

COLORS = {
    "pcb": "#297647",
    "substrate": "#64748b",
    "interposer": "#e6a99b",
    "logic": "#70af8b",
    "hbm": "#f2bd87",
    "rf": "#ab8aa7",
    "mems": "#83c7d8",
    "ink": "#243447",
    "muted": "#526477",
    "via": "#d9ac36",
}


def visual_plan(reference):
    return {
        "purpose": "解释2.5D封装中芯粒与中介层、基板的承载关系，并对照斜投影与A—A示意剖面",
        "reference": {
            "source": reference,
            "mode": "structural",
            "observations": [
                "参考图左侧为斜投影封装示意，右侧为Logic/GPU与HBM剖面",
                "参考含Interposer、Package Substrate、PCB与Heat Spreader标注",
            ],
            "uncertainties": [
                "截图不能确认真实尺寸、工艺层数或材料",
                "RF与MEMS不一定落在右侧剖切面内；本图明确置于剖切面外",
            ],
        },
        "views": [
            {
                "id": "oblique",
                "method": "oblique",
                "description": "异质芯粒同面集成斜投影",
            },
            {
                "id": "section",
                "method": "section",
                "description": "A—A示意截面经过Logic与HBM",
            },
        ],
        "objects": [
            {"id": o, "role": r, "views": views, "label": label}
            for o, r, views, label in [
                ("pcb", "board", ["oblique", "section"], "PCB"),
                ("substrate", "support", ["oblique", "section"], "Package Substrate"),
                ("interposer", "routing support", ["oblique", "section"], "Interposer"),
                ("logic", "compute", ["oblique", "section"], "Logic / GPU"),
                ("hbm", "stacked memory", ["oblique", "section"], "HBM"),
                ("rf", "off-section die", ["oblique"], "RF"),
                ("mems", "off-section die", ["oblique"], "MEMS"),
                ("lid", "heat spreader", ["section"], "Heat Spreader"),
            ]
        ],
        "relations": [
            {"kind": "supported_by", "source": a, "target": b}
            for a, b in [
                ("substrate", "pcb"),
                ("interposer", "substrate"),
                ("logic", "interposer"),
                ("hbm", "interposer"),
            ]
        ],
        "illustrative_limits": [
            "非按比例绘制；所有厚度、凸点、TSV数量和HBM层数均为示意",
            "不代表特定厂商制造截面或热/电性能",
            "RF与MEMS位于右图剖切面外；剖面并非所有芯粒的投影",
        ],
    }


def build_items(font, hbm_layers=5, logic_offset=0, interposer_thickness=28):
    if not 3 <= hbm_layers <= 9:
        raise ValueError("demo HBM schematic layer count must be 3..9")
    if not -20 <= logic_offset <= 35:
        raise ValueError("demo logic offset must stay within support and clear of HBM")
    if not 18 <= interposer_thickness <= 50:
        raise ValueError("demo interposer thickness must be 18..50")
    items = []

    def text(
        identity, x, y, value, size=20, width=600, obj=None, view="page", color=None
    ):
        item = {
            "kind": "text",
            "id": identity,
            "x": x,
            "y": y,
            "text": value,
            "width": width,
            "style": {
                "fontFamily": font,
                "fontSize": size,
                "strokeColor": color or COLORS["ink"],
            },
        }
        if obj:
            item.update(objectId=obj, viewId=view)
        items.append(item)

    def leader(identity, points, obj, view):
        items.append(
            {
                "kind": "leader",
                "id": identity,
                "points": points,
                "target": points[-1],
                "targetObject": obj,
                "viewId": view,
                "style": {
                    "strokeColor": COLORS["muted"],
                    "strokeWidth": 1.4,
                    "roundness": None,
                },
            }
        )

    text("page-title", 65, 34, "2.5D 封装：从同面集成到分层剖面", 34, 1510)
    text(
        "page-subtitle",
        65,
        91,
        "多个芯粒承载于共同中介层，再通过封装基板连接PCB。左看空间关系，右看层次与垂直互连。",
        20,
        1500,
    )
    text("left-heading", 65, 168, "01  同面集成 · 斜投影", 25, 710)
    text("right-heading", 905, 168, "02  A—A · 示意剖面", 25, 700)
    x, y = 245, 605
    projection = [0.56, -0.43]

    def p(u, v, z):
        return project([x, y], projection, u, v, z)

    layers = [
        {"id": "pcb", "height": 24, "color": COLORS["pcb"]},
        {"id": "substrate", "height": 40, "color": COLORS["substrate"]},
        {
            "id": "interposer",
            "height": interposer_thickness,
            "color": COLORS["interposer"],
        },
    ]
    top = 64 + interposer_thickness
    items.append(
        {
            "kind": "layer_stack",
            "id": "left-base",
            "viewId": "oblique",
            "view": "oblique",
            "x": x,
            "y": y,
            "width": 570,
            "depth": 215,
            "projection": projection,
            "layers": layers,
        }
    )
    chip_specs = [
        ("rf", 35, 20, 100, 68, 24),
        ("mems", 35, 125, 100, 60, 24),
        ("logic", 180 + logic_offset, 20, 210, 162, 40),
    ]
    for obj, u, v, w, d, h in chip_specs:
        color = COLORS[obj]
        items.append(
            {
                "kind": "projected_box",
                "id": "left-" + obj,
                "objectId": obj,
                "viewId": "oblique",
                "x": x,
                "y": y,
                "projection": projection,
                "u": u,
                "v": v,
                "z": top,
                "width": w,
                "depth": d,
                "height": h,
                "faceColors": {"front": color, "side": color, "top": color},
            }
        )
    items.append(
        {
            "kind": "layer_stack",
            "id": "left-hbm",
            "viewId": "oblique",
            "view": "oblique",
            "x": x,
            "y": y,
            "u": 440,
            "v": 55,
            "z": top,
            "width": 105,
            "depth": 115,
            "projection": projection,
            "gap": 3,
            "layers": [
                {
                    "id": f"die-{i}",
                    "objectId": "hbm",
                    "height": 12,
                    "color": COLORS["hbm"],
                }
                for i in range(hbm_layers)
            ],
        }
    )
    # Native repeated contacts below PCB, not a textured screenshot.
    items.append(
        {
            "kind": "grid_array",
            "id": "left-balls",
            "objectId": "pcb",
            "viewId": "oblique",
            "x": x + 18,
            "y": y + 4,
            "rows": 1,
            "cols": 16,
            "pitch": [34, 20],
            "size": [11, 11],
            "style": {
                "backgroundColor": "#cbd5e1",
                "strokeWidth": 1,
                "strokeColor": "#8293a5",
            },
        }
    )
    # Label columns outside the projected shapes; annotation endpoints are derived from the model.
    for obj, zmid in [
        ("pcb", 12),
        ("substrate", 44),
        ("interposer", 64 + interposer_thickness / 2),
    ]:
        labels = {
            "pcb": "PCB",
            "substrate": "Package Substrate",
            "interposer": "Interposer",
        }
        target = p(0, 0, zmid)
        text(
            "left-label-" + obj,
            65,
            target[1] - 10,
            labels[obj],
            16,
            145,
            obj,
            "oblique",
        )
        leader("left-leader-" + obj, [[230, target[1]], target], obj, "oblique")
    for obj, label, tx, ty, point in [
        ("rf", "RF", 65, 284, p(75, 50, top + 24)),
        ("mems", "MEMS", 65, 245, p(75, 150, top + 24)),
        (
            "logic",
            "Logic / GPU",
            445 + logic_offset,
            246,
            p(285 + logic_offset, 90, top + 40),
        ),
    ]:
        text("left-label-" + obj, tx, ty, label, 20, 180, obj, "oblique")
        start = [tx + min(130, len(label) * 10), ty + 28]
        leader(
            "left-leader-" + obj,
            [start, [start[0], point[1] - 18], point],
            obj,
            "oblique",
        )
    hbm_roof = p(492.5, 170, top + hbm_layers * 12 + (hbm_layers - 1) * 3)
    text(
        "left-label-hbm",
        hbm_roof[0] - 28,
        hbm_roof[1] - 34,
        "HBM",
        20,
        120,
        "hbm",
        "oblique",
    )
    text(
        "left-caption",
        65,
        795,
        "RF / MEMS 位于右图剖切面外；芯粒位置、大小与颜色用于说明结构。",
        17,
        740,
        color=COLORS["muted"],
    )
    # Right: same semantic layer order, different view origin. Depth retained for relation checks.
    sx, sy = 970, 605
    items.append(
        {
            "kind": "layer_stack",
            "id": "right-base",
            "viewId": "section",
            "x": sx,
            "y": sy,
            "width": 560,
            "depth": 215,
            "layers": layers,
        }
    )
    items.append(
        {
            "kind": "layer_stack",
            "id": "right-logic",
            "viewId": "section",
            "x": sx,
            "y": sy,
            "u": 30 + logic_offset,
            "v": 20,
            "z": top,
            "width": 270,
            "depth": 162,
            "layers": [
                {
                    "id": "logic",
                    "objectId": "logic",
                    "height": 112,
                    "color": COLORS["logic"],
                }
            ],
        }
    )
    items.append(
        {
            "kind": "layer_stack",
            "id": "right-hbm",
            "viewId": "section",
            "x": sx,
            "y": sy,
            "u": 350,
            "v": 55,
            "z": top,
            "width": 165,
            "depth": 115,
            "gap": 3,
            "layers": [
                {
                    "id": f"die-{i}",
                    "objectId": "hbm",
                    "height": 12,
                    "color": COLORS["hbm"],
                }
                for i in range(hbm_layers)
            ],
        }
    )
    lid_z = top + max(112, hbm_layers * 12 + (hbm_layers - 1) * 3) + 27
    items.append(
        {
            "kind": "layer_stack",
            "id": "right-lid",
            "viewId": "section",
            "x": sx,
            "y": sy,
            "z": lid_z,
            "width": 560,
            "depth": 215,
            "layers": [
                {"id": "lid", "objectId": "lid", "height": 18, "color": "#9db6c6"}
            ],
        }
    )
    text(
        "right-label-lid",
        1120,
        sy - lid_z - 51,
        "Heat Spreader",
        19,
        350,
        "lid",
        "section",
    )
    text(
        "right-label-logic",
        sx + 72 + logic_offset,
        sy - top - 74,
        "Logic / GPU",
        25,
        240,
        "logic",
        "section",
    )
    text(
        "right-label-hbm",
        sx + 389,
        sy - top - hbm_layers * 12 - (hbm_layers - 1) * 3 - 31,
        "HBM",
        22,
        120,
        "hbm",
        "section",
    )
    for obj, label, zmid in [
        ("pcb", "PCB", 12),
        ("substrate", "Package Substrate", 44),
        ("interposer", "Interposer", 64 + interposer_thickness / 2),
    ]:
        if obj == "pcb":
            tx, ty = sx + 220, sy - zmid - 12
        elif obj == "substrate":
            tx, ty = sx + 165, sy - zmid - 12
        else:
            tx, ty = sx + 195, sy - zmid - 11
        text("right-label-" + obj, tx, ty, label, 18, 350, obj, "section")
    # Through-layer vertical markers kept off layer titles and treated as part of Interposer.
    items.append(
        {
            "kind": "grid_array",
            "id": "right-vias",
            "objectId": "interposer",
            "viewId": "section",
            "x": sx + 18,
            "y": sy - top + 2,
            "rows": 1,
            "cols": 5,
            "pitch": [29, 20],
            "size": [5, interposer_thickness - 4],
            "shape": "rectangle",
            "style": {
                "strokeColor": COLORS["via"],
                "backgroundColor": COLORS["via"],
                "strokeWidth": 0.5,
            },
        }
    )
    text("via-label", 1105, 663, "垂直互连（示意）", 18, 280)
    leader(
        "via-leader",
        [
            [1105, 691],
            [950, 691],
            [950, sy - top + interposer_thickness / 2],
            [sx + 78, sy - top + interposer_thickness / 2],
        ],
        "interposer",
        "section",
    )
    items.append(
        {
            "kind": "grid_array",
            "id": "right-balls",
            "objectId": "pcb",
            "viewId": "section",
            "x": sx + 15,
            "y": sy + 4,
            "rows": 1,
            "cols": 16,
            "pitch": [34, 20],
            "size": [11, 11],
            "style": {
                "backgroundColor": "#cbd5e1",
                "strokeColor": "#8293a5",
                "strokeWidth": 1,
            },
        }
    )
    text(
        "right-caption",
        905,
        731,
        f"HBM 采用 {hbm_layers} 层示意；剖面只表示选定切面。",
        18,
        680,
        color=COLORS["muted"],
    )
    text(
        "right-caption-2",
        905,
        767,
        "中介层可采用不同实现；本图不据颜色断定材料。",
        18,
        680,
        color=COLORS["muted"],
    )
    text(
        "footer",
        65,
        866,
        "读图提示  |  先辨芯粒 → 再看中介层 → 基板 → PCB；引出线用于注释，不是电气网表。",
        19,
        1500,
    )
    text(
        "limits",
        65,
        908,
        "示意图，非按比例。厚度、凸点、垂直互连及HBM层数不代表特定产品；不用于制造、热或电气分析。",
        17,
        1510,
        color=COLORS["muted"],
    )
    return items


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--file", required=True, help="Explicit existing host canvas")
    p.add_argument("--brief-file", type=Path, required=True)
    p.add_argument("--font", required=True)
    p.add_argument("--state-id", default="package-illustration")
    p.add_argument("--hbm-layers", type=int, default=5)
    p.add_argument("--logic-offset", type=float, default=0)
    p.add_argument("--interposer-thickness", type=float, default=28)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    c = DrawingClient()
    brief = json.loads(args.brief_file.read_text(encoding="utf-8"))
    ctx = c.context("bind", file_path=args.file, brief=brief)
    result = c.primitives(
        ctx["contextToken"],
        build_items(
            args.font, args.hbm_layers, args.logic_offset, args.interposer_thickness
        ),
        style={
            "fontFamily": args.font,
            "fontSize": 20,
            "roughness": 0,
            "strokeWidth": 1.2,
            "strokeColor": COLORS["ink"],
            "roundness": None,
        },
        action="render",
        state_id=args.state_id,
        base_revision=ctx["revision"],
    )
    result["preview"].pop("_base64", None)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "file": result["file"],
                "revision": result["revision"],
                "diff": result["diff"],
                "check": result["check"]["status"],
                "png": result["preview"]["out_path"],
            },
            ensure_ascii=False,
        )
    )
    return (
        0
        if result["check"]["status"] == "pass" and result["preview"]["complete"]
        else 2
    )


if __name__ == "__main__":
    raise SystemExit(main())
