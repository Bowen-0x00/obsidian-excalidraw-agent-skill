"""Source-driven teaching examples: spatial mechanisms, not paragraph flowcharts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "runtime"))
from drawing_client import DrawingClient

CASES = ("window", "quantization", "paging")


def design(case, confirmed=True):
    options = {
        "window": [
            (
                "mechanism",
                "序列＋掩码对照",
                "token序列与注意力格子对应，直接解释看得到谁",
            ),
            ("steps", "时间步对照", "重点展示下一步窗口移动及替换，不着重完整矩阵"),
        ],
        "quantization": [
            (
                "mechanism",
                "矩阵分组＋位宽对比",
                "同一小矩阵按行列分组，配等数量值的存储位格对比",
            ),
            (
                "bits",
                "位格前后对比",
                "重点解释相同数量数值压缩前后的位宽，不详述离群值分组",
            ),
        ],
        "paging": [
            (
                "mechanism",
                "逻辑—物理映射",
                "逻辑块、Block Table、物理池三列，展示具体非连续映射",
            ),
            (
                "states",
                "两次分配状态对照",
                "重点解释请求增长后怎样再分配，同时保留映射表",
            ),
        ],
    }[case]
    goals = {
        "window": [
            (
                "visibility",
                "sequence_window",
                ["plain", "sink"],
                "怎样看见窗口和固定前缀的保留范围？",
            ),
            ("reuse", "time_steps", ["decode"], "下一步哪些token是新算、哪些可复用？"),
        ],
        "quantization": [
            ("columns", "matrix_groups", ["columns"], "列分组的scale与离群值在哪里？"),
            ("rows", "matrix_groups", ["rows"], "同一矩阵改为行分组，边界有什么不同？"),
            (
                "storage",
                "bitwidth_compare",
                ["bits"],
                "同数量值从16位变4位后存储长度如何变化？",
            ),
        ],
        "paging": [
            (
                "mapping",
                "memory_map",
                ["pages"],
                "逻辑连续的三个块怎样映射到分散物理块？",
            )
        ],
    }[case]
    plan = {
        "objective": {
            "window": "理解窗口保留范围与缓存复用",
            "quantization": "区分分组粒度与存储位宽",
            "paging": "看懂逻辑连续、物理分散的分页映射",
        }[case],
        "candidates": [
            {
                "id": i,
                "label": label,
                "approach": "mechanism",
                "description": description,
            }
            for i, label, description in options
        ],
        "recommended": "mechanism",
        "reason": "所选图形让读者看见对象/位置/变化，而不是在段落里寻找结论",
        "goals": [
            {
                "id": i,
                "requirement_id": "R1",
                "question": question,
                "method": method,
                "components": components,
            }
            for i, method, components, question in goals
        ],
    }
    if confirmed:
        plan.update(
            selected="mechanism",
            choice={
                "source": "answer",
                "evidence": "用户在本轮真实图法选项中选择：" + options[0][1],
            },
        )
    return plan


def brief(case, font, task):
    return {
        "task_id": task,
        "diagram_type": "teaching",
        "preferences": {
            k: {
                "value": value,
                "source": "inherited",
                "evidence": "独立QA复用本次remote配图已确认的专业平整、高验收、莫兰迪语义色和清晰正文；不是新的用户画布偏好声明",
            }
            for k, value in {
                "style": "professional",
                "review": "high",
                "palette": "muted blue/green/warm semantic colors",
                "background": "white",
                "font": font,
            }.items()
        },
        "requirements": [
            {
                "id": "R1",
                "description": "画出实际机制与具体小例子，不能用文字框提到概念来代替："
                + design(case)["objective"],
            },
            {
                "id": "R2",
                "description": "所有标签可读，标示颜色含义及示意边界，不宣称精度/性能实测",
            },
        ],
        "teaching_plan": design(case),
    }


def items(case, font, window=3, mapping=None):
    result = []

    def text(identity, x, y, value, size=20, width=1000):
        result.append(
            {
                "kind": "text",
                "id": identity,
                "x": x,
                "y": y,
                "text": value,
                "width": width,
                "style": {
                    "fontFamily": font,
                    "fontSize": size,
                    "strokeColor": "#334155",
                },
            }
        )

    if case == "window":
        text("title", 60, 25, "滑动窗口：看见谁，保留谁", 32)
        text(
            "subtitle",
            60,
            82,
            "相同的8个示意token；左只留最近窗口，右额外保留开头1个sink。",
            20,
        )
        text("plain-title", 100, 140, "仅滑窗", 24, 400)
        text("sink-title", 650, 140, "滑窗＋固定前缀", 24, 450)
        for identity, x, sinks in (("plain", 100, 0), ("sink", 650, 1)):
            result.append(
                {
                    "kind": "sequence_window",
                    "id": identity,
                    "x": x,
                    "y": 200,
                    "tokens": [str(i) for i in range(8)],
                    "window": window,
                    "sinks": sinks,
                    "step": 7,
                    "show_mask": True,
                    "cell": 40,
                }
            )
        text(
            "legend",
            100,
            730,
            "蓝色＝固定前缀；绿色＝可见／保留；灰色＝不可见／丢弃或未来。",
            19,
        )
        text(
            "states-title", 100, 800, "同一批token：新算与复用不是重新解释一遍历史", 24
        )
        result.append(
            {
                "kind": "time_steps",
                "id": "decode",
                "x": 200,
                "y": 905,
                "tokens": ["A", "B", "C", "D", "E", "F"],
                "cell": 40,
                "steps": [
                    {"id": "prefill", "active": [0, 1, 2, 3], "reused": []},
                    {"id": "decode1", "active": [4], "reused": [0, 1, 2, 3]},
                    {"id": "decode2", "active": [5], "reused": [0, 1, 2, 3, 4]},
                ],
            }
        )
        text(
            "states-legend",
            100,
            1115,
            "橙色＝本步新算；绿色＝已有可复用；灰色＝尚未涉及。",
            19,
        )
        text(
            "limit",
            100,
            1165,
            "小例子只展示可见范围与复用；sink数量和窗口大小不代表某个真实模型配置。",
            17,
        )
    elif case == "quantization":
        text("title", 60, 25, "量化：先看分组，再看位宽", 32)
        text(
            "subtitle",
            60,
            82,
            "两边是相同数值矩阵；红色为 |x| ≥ 8 的示意离群值，蓝色条标记独立分组。",
            19,
        )
        text("columns-title", 140, 155, "按列分组：每列一个scale", 24, 430)
        text("rows-title", 660, 155, "按行分组：每行一个scale", 24, 430)
        values = [[1, 12, 2, 1], [2, 15, 1, 3], [1, 11, 3, 2], [2, 13, 1, 1]]
        result.extend(
            [
                {
                    "kind": "matrix_groups",
                    "id": "columns",
                    "x": 170,
                    "y": 270,
                    "values": values,
                    "group_by": "column",
                    "outlier_threshold": 8,
                    "cell": 48,
                },
                {
                    "kind": "matrix_groups",
                    "id": "rows",
                    "x": 710,
                    "y": 270,
                    "values": values,
                    "group_by": "row",
                    "outlier_threshold": 8,
                    "cell": 48,
                },
            ]
        )
        text("bits-title", 140, 570, "同样3个数：16-bit 与 4-bit 的存储位格", 24)
        result.append(
            {
                "kind": "bitwidth_compare",
                "id": "bits",
                "x": 170,
                "y": 660,
                "count": 3,
                "bits": [16, 4],
                "cell": 32,
            }
        )
        text(
            "limit",
            140,
            880,
            "只比较编码分组与等尺度位数；不据这张示意图推断精度、压缩实现开销或加速比。",
            17,
        )
    else:
        text("title", 50, 25, "分页：逻辑连续，物理不必连续", 32, 900)
        text(
            "subtitle",
            50,
            82,
            "同一请求的逻辑块 L0、L1、L2，分别映射到 P4、P1、P6；其他物理块仍空闲。",
            19,
            950,
        )
        result.append(
            {
                "kind": "memory_map",
                "id": "pages",
                "x": 100,
                "y": 220,
                "mapping": mapping or [4, 1, 6],
                "physical_count": 8,
                "block_tokens": 4,
                "cell": 42,
            }
        )
        text(
            "legend",
            100,
            810,
            "蓝色＝请求的逻辑块与映射项；绿色＝已分配物理块；灰色＝空闲块。",
            19,
            850,
        )
        text(
            "limit",
            100,
            865,
            "每块4个token是教学示意；箭头表示地址映射，不是按时间串联的阅读顺序。",
            17,
            850,
        )
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=CASES)
    parser.add_argument("--font", required=True)
    parser.add_argument("--file", required=True)
    parser.add_argument("--brief-file", required=True, type=Path)
    parser.add_argument("--state-id", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    c = DrawingClient()
    context = c.context(
        "bind",
        file_path=args.file,
        brief=json.loads(args.brief_file.read_text(encoding="utf-8")),
    )
    result = c.primitives(
        context["contextToken"],
        items(args.case, args.font),
        style={
            "fontFamily": args.font,
            "fontSize": 18,
            "roughness": 0,
            "roundness": None,
        },
        action="render",
        state_id=args.state_id,
        base_revision=context["revision"],
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
                "status": result["check"]["status"],
                "png": result["preview"]["out_path"],
            },
            ensure_ascii=False,
        )
    )
    return 0 if result["check"]["status"] == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
