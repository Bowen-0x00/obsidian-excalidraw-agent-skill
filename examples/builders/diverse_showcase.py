"""Five different domains/forms, authored through native Excalidraw APIs.

Run from the package root with a connected graphical host:
 uv run --frozen python examples/builders/diverse_showcase.py water_cycle --font "ACTUAL_HOST_FAMILY" --brief-file ./drawing-brief.json --filename Unique-Water --output ./output/water.json

Gantt and academic require capabilities.nativeTable.callable: the paired native
TableManager owns theme colors, border templates, semantic cells and reflow.
No diagram is a raster mockup or an automatic visual approval.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "runtime"))
sys.path.insert(0, str(Path(__file__).parent))
from drawing_client import DrawingClient
from showcase_support import Scene

INK = "#263238"
MUTED = "#64747b"
BLUE = "#1976d2"
TEAL = "#00897b"
GOLD = "#d18b25"
RED = "#d64a61"


def water_cycle(s):
    s.description = (
        "Handwritten earth-science landscape and six physical water-cycle processes"
    )
    s.scope = "Conceptual landscape, not to scale or a measured hydrologic budget"
    cream, blue, green, brown = "#fffaf0", "#397fa2", "#54755a", "#9c7852"
    s.rect("background", 0, 0, 1450, 970, fill=cream, stroke=cream, container=True)
    s.text("kicker", "EARTH SCIENCE / FIELD NOTES 01", 65, 38, 18, green)
    s.text(
        "title", "Where does the water go?", 65, 78, 46, "#334b45", font="Excalifont"
    )
    s.text(
        "subtitle",
        "A journey through air, land and the ocean",
        68,
        140,
        24,
        MUTED,
        font="Excalifont",
    )
    # One intentionally layered landscape construction, separate from process labels.
    s.polygon(
        "land",
        [
            (530, 650),
            (640, 615),
            (770, 520),
            (900, 580),
            (1030, 420),
            (1170, 600),
            (1390, 650),
            (1390, 900),
            (530, 900),
        ],
        fill="#dce8d2",
        color="#719175",
        roughness=2,
        fill_style="hachure",
        unit="terrain",
    )
    s.polygon(
        "mountain",
        [(665, 615), (790, 410), (920, 615)],
        fill="#c7d5c4",
        color="#66806d",
        roughness=2,
        unit="terrain",
    )
    s.polygon(
        "mountain2",
        [(900, 600), (1030, 385), (1170, 600)],
        fill="#d2dfcf",
        color="#66806d",
        roughness=2,
        unit="terrain",
    )
    s.polygon(
        "snow",
        [(998, 438), (1030, 385), (1064, 440), (1045, 430), (1030, 443), (1016, 428)],
        fill="#ffffff",
        color="#a3b8af",
        roughness=1,
        unit="terrain",
    )
    s.rect(
        "soil",
        530,
        740,
        860,
        160,
        fill="#ead7b7",
        stroke=brown,
        roughness=1,
        fill_style="hachure",
        unit="terrain",
    )
    s.rect(
        "aquifer",
        560,
        827,
        770,
        46,
        fill="#acd8e6",
        stroke="#75afc8",
        roughness=1,
        unit="terrain",
    )
    s.polygon(
        "ocean",
        [(60, 665), (200, 650), (340, 675), (530, 650), (530, 900), (60, 900)],
        fill="#b9dff0",
        color="#4e9ac0",
        roughness=2,
        fill_style="hachure",
        unit="terrain",
    )
    s.path(
        "river",
        [(1050, 600), (990, 635), (885, 650), (760, 684), (650, 700), (530, 714)],
        color="#78bcd7",
        width=17,
        curve=True,
        unit="terrain",
    )
    s.ellipse(
        "sun",
        100,
        245,
        90,
        90,
        fill="#f7d271",
        stroke="#c5902e",
        width=3,
        roughness=2,
        unit="sun",
    )
    for i in range(8):
        a = i * math.pi / 4
        s.line(
            "sunray" + str(i),
            [
                (145 + 58 * math.cos(a), 290 + 58 * math.sin(a)),
                (145 + 77 * math.cos(a), 290 + 77 * math.sin(a)),
            ],
            color="#d0a642",
            roughness=2,
            unit="sun",
        )
    for name, dx, dy in [("left", 0, 0), ("right", 555, -10)]:
        for i, (x, y, w, h) in enumerate(
            [(425, 280, 115, 64), (480, 248, 115, 90), (550, 282, 115, 62)]
        ):
            s.ellipse(
                "cloud:" + name + str(i),
                x + dx,
                y + dy,
                w,
                h,
                fill="#ffffff",
                stroke="#91adb1",
                roughness=2,
                unit="cloud:" + name,
            )
    # Sparse trees are native polygons/trunks, not external icons.
    for i, x in enumerate((680, 735, 1225, 1280, 1335)):
        s.line(
            "trunk" + str(i),
            [(x, 636), (x, 685)],
            color=brown,
            width=5,
            roughness=1,
            unit="tree" + str(i),
        )
        s.polygon(
            "tree" + str(i),
            [(x - 27, 645), (x, 587), (x + 27, 645)],
            fill="#a9c3a0",
            color=green,
            roughness=2,
            unit="tree" + str(i),
        )
    s.arrow(
        "evaporation",
        [(330, 625), (330, 485), (390, 380)],
        color=blue,
        width=4,
        roughness=2,
    )
    s.text("evaporation_label", "1  Evaporation", 80, 445, 26, blue, font="Excalifont")
    s.arrow(
        "condensation", [(675, 300), (935, 300)], color="#64769b", width=4, roughness=2
    )
    s.text(
        "condensation_label",
        "2  Condensation",
        700,
        248,
        25,
        "#64769b",
        font="Excalifont",
    )
    s.arrow(
        "precipitation", [(1195, 350), (1195, 545)], color=blue, width=4, roughness=2
    )
    for i in range(5):
        x = 1080 + i * 18
        s.line(
            "rain" + str(i),
            [(x, 360), (x - 10, 385)],
            color="#78aeca",
            width=2,
            roughness=1,
        )
    s.text(
        "precipitation_label",
        "3  Precipitation",
        1220,
        445,
        23,
        blue,
        font="Excalifont",
    )
    s.arrow(
        "runoff",
        [(1015, 675), (900, 710), (755, 727)],
        color=TEAL,
        width=4,
        roughness=2,
    )
    s.text("runoff_label", "4  Surface runoff", 780, 755, 24, TEAL, font="Excalifont")
    s.arrow(
        "infiltration", [(1315, 715), (1315, 810)], color=brown, width=4, roughness=2
    )
    s.text(
        "infiltration_label", "5  Infiltration", 1090, 760, 24, brown, font="Excalifont"
    )
    s.arrow(
        "groundwater",
        [(1000, 850), (720, 850), (500, 850)],
        color=blue,
        width=4,
        roughness=2,
    )
    s.text(
        "groundwater_label",
        "6  Groundwater return",
        590,
        910,
        24,
        blue,
        font="Excalifont",
    )
    s.text("ocean_label", "OCEAN", 190, 780, 31, blue, font="Excalifont")
    s.text("note", "Conceptual landscape • not to scale", 65, 936, 18, MUTED)
    s.details = {"land": [510, 350, 900, 580]}


def calculus(s):
    s.description = "Dark mathematics plate with a true tangent, right-endpoint rectangles and rendered TeX"
    s.scope = (
        "f(x)=x²/16+1 on [0,8]; eight right-endpoint strips are an upper approximation"
    )
    bg, fg, sub = "#111827", "#f3f4f6", "#cbd5e1"
    s.rect("background", 0, 0, 1450, 930, fill=bg, stroke=bg, container=True)
    s.text("kicker", "MATHEMATICS / VISUAL NOTE 02", 65, 38, 18, "#a78bfa")
    s.text("title", "From local change to total area", 65, 78, 42, fg, bold=True)
    s.text(
        "subtitle",
        "A tangent describes change at one point. An integral accumulates it over an interval.",
        68,
        140,
        22,
        sub,
    )
    s.rect(
        "plot_panel",
        65,
        215,
        845,
        620,
        fill="#172033",
        stroke="#475569",
        width=1.5,
        radius=12,
        container=True,
    )
    ox, oy, sx, sy = 145, 735, 84, 72
    f = lambda x: x * x / 16 + 1
    curve = [(ox + i / 10 * sx, oy - f(i / 10) * sy) for i in range(81)]
    s.polygon(
        "integral_area",
        [(ox, oy), *curve, (ox + 8 * sx, oy)],
        fill="#6853a9",
        color="#6853a9",
        opacity=35,
        unit="integral_construction",
    )
    for i in range(8):
        h = f(i + 1) * sy
        s.rect(
            "strip" + str(i),
            ox + i * sx,
            oy - h,
            sx,
            h,
            fill="#38bdf8",
            stroke="#7dd3fc",
            width=1,
            opacity=25,
            unit="integral_construction",
        )
    s.arrow("x_axis", [(ox, oy), (855, oy)], color=sub, width=2)
    s.arrow("y_axis", [(ox, oy), (ox, 255)], color=sub, width=2)
    for i in range(9):
        x = ox + i * sx
        s.line("x_tick" + str(i), [(x, oy - 5), (x, oy + 5)], color="#94a3b8", width=1)
        s.text("x_num" + str(i), str(i), x - 5, oy + 16, 19, sub)
    for j in (2, 4, 6):
        y = oy - j * sy
        s.line("y_tick" + str(j), [(ox - 5, y), (ox + 5, y)], color="#94a3b8", width=1)
        s.text("y_num" + str(j), str(j), ox - 33, y - 12, 18, sub)
    s.line("function_curve", curve, color="#c4b5fd", width=4)
    px, py = ox + 4 * sx, oy - 2 * sy
    slope = 0.5 * sy / sx
    s.line(
        "tangent",
        [(px - 155, py + 155 * slope), (px + 155, py - 155 * slope)],
        color="#fbbf24",
        width=3,
    )
    s.ellipse(
        "point", px - 7, py - 7, 14, 14, fill="#fbbf24", stroke="#fbbf24", unit="point"
    )
    s.text("point_label", "(4, 2)", px - 66, py + 30, 22, "#fbbf24")
    s.text("plot_caption", "f(x) = x² / 16 + 1", 200, 255, 27, fg)
    s.text("tangent_caption", "slope f′(4) = 1/2", 235, 480, 22, "#fbbf24")
    s.text(
        "strips_caption",
        "8 right-endpoint strips: an upper estimate",
        215,
        795,
        20,
        "#7dd3fc",
    )
    s.text("derive_head", "THE EXACT RELATIONSHIP", 975, 240, 23, "#c4b5fd", bold=True)
    s.latex("formula1", r"\color{#f3f4f6}{f'(x)=\frac{x}{8}}", 975, 305, 1.7)
    s.latex("formula2", r"\color{#f3f4f6}{F(x)=\frac{x^3}{48}+x}", 975, 405, 1.7)
    s.latex(
        "formula3", r"\color{#f3f4f6}{\int_0^8 f(x)\,dx=\frac{56}{3}}", 975, 510, 1.7
    )
    s.text("step1", "Tangent → instantaneous rate", 975, 640, 23, sub)
    s.text("step2", "Strips → finite approximation", 975, 685, 23, sub)
    s.text("step3", "Integral → exact accumulation", 975, 730, 23, sub)
    s.text(
        "foot",
        "Original teaching illustration • editable geometry + source-preserving TeX",
        65,
        880,
        18,
        "#94a3b8",
    )
    s.details = {"equations": [950, 220, 470, 590]}


def transit(s):
    s.description = "Schematic transit wayfinding: three services and two real shared interchange coordinates"
    s.scope = "Original imaginary city; not geographic or navigational data"
    bg = "#faf9f6"
    s.rect("background", 0, 0, 1450, 990, fill=bg, stroke=bg, container=True)
    s.text("kicker", "NORTHLINE / A TRANSIT ATLAS", 65, 38, 18, MUTED)
    s.text("title", "A city connected", 65, 78, 48, INK, bold=True)
    s.text(
        "subtitle",
        "Three services. Two interchanges. Every stop is an editable native symbol.",
        68,
        145,
        22,
        MUTED,
    )
    routes = {
        "N": (
            RED,
            [
                (130, 310),
                (310, 310),
                (430, 430),
                (520, 430),
                (760, 430),
                (880, 310),
                (1090, 310),
                (1280, 500),
            ],
            [
                "Harbor",
                "Cedar",
                "Museum",
                "Central",
                "Gallery",
                "Hilltop",
                "Orchard",
                "Eastgate",
            ],
        ),
        "T": (
            TEAL,
            [
                (160, 790),
                (340, 610),
                (520, 430),
                (520, 230),
                (720, 230),
                (1000, 510),
                (1000, 650),
                (1280, 650),
            ],
            [
                "Southbank",
                "Market",
                "Central",
                "University",
                "North Park",
                "Old Town",
                "Civic",
                "Airport",
            ],
        ),
        "G": (
            GOLD,
            [(180, 850), (400, 850), (600, 650), (1000, 650), (1170, 820), (1330, 820)],
            ["West End", "Garden", "Westfield", "Civic", "Stadium", "Lakeside"],
        ),
    }
    for code, (color, points, names) in routes.items():
        s.line("route:" + code, points, color=color, width=11)
        s.ops[-1]["customData"].update(
            lineCrossings="gap", lineJumpPriority={"N": 0, "T": 1, "G": 2}[code]
        )
    labels = {
        "Harbor": (95, 270),
        "Cedar": (265, 270),
        "Museum": (335, 448),
        "Central": (545, 465),
        "Gallery": (730, 465),
        "Hilltop": (845, 270),
        "Orchard": (1060, 270),
        "Eastgate": (1210, 535),
        "Southbank": (55, 705),
        "Market": (235, 580),
        "University": (390, 198),
        "North Park": (680, 190),
        "Old Town": (1040, 510),
        "Civic": (1035, 620),
        "Airport": (1230, 685),
        "West End": (95, 885),
        "Garden": (355, 885),
        "Westfield": (550, 610),
        "Stadium": (1090, 855),
        "Lakeside": (1270, 855),
    }
    seen = set()
    for code, (color, points, names) in routes.items():
        for (x, y), name in zip(points, names):
            if name in seen:
                continue
            seen.add(name)
            if name in ("Central", "Civic"):
                s.ellipse(
                    "station:" + name,
                    x - 14,
                    y - 14,
                    28,
                    28,
                    fill=bg,
                    stroke=INK,
                    width=5,
                )
            else:
                s.ellipse(
                    "station:" + name,
                    x - 7,
                    y - 7,
                    14,
                    14,
                    fill=bg,
                    stroke=color,
                    width=4,
                )
            s.text(
                "label:" + name,
                name,
                *labels[name],
                21,
                INK,
                bold=name in ("Central", "Civic"),
            )
    s.rect(
        "legend",
        1060,
        45,
        330,
        195,
        fill="#ffffff",
        stroke="#d9d9d5",
        radius=6,
        container=True,
    )
    for i, (name, color) in enumerate(
        [("N  Northline", RED), ("T  Tidelink", TEAL), ("G  Crosstown", GOLD)]
    ):
        y = 80 + i * 43
        s.line("legend_line" + str(i), [(1085, y), (1130, y)], color=color, width=9)
        s.text("legend_label" + str(i), name, 1150, y - 14, 22, INK)
    s.ellipse("legend_interchange", 1090, 201, 18, 18, fill=bg, stroke=INK, width=3)
    s.text("legend_note", "Interchange", 1150, 195, 20, INK)
    s.text(
        "foot",
        "Illustrative network • not navigation • crossings without a ring are not transfers",
        65,
        945,
        19,
        MUTED,
    )
    s.details = {"interchanges": [380, 220, 760, 510]}


def gantt(s):
    s.description = "Project scheduling board with native mint/grid table and aligned seven-week Gantt bars"
    s.scope = (
        "Synthetic field-study schedule; states are planning labels, not telemetry"
    )
    s.rect(
        "background", 0, 0, 1450, 840, fill="#f4f7f2", stroke="#f4f7f2", container=True
    )
    s.text("kicker", "PROJECT OPERATIONS / SEVEN-WEEK PLAN", 60, 38, 18, "#54715f")
    s.text("title", "From question to field release", 60, 83, 43, "#284234", bold=True)
    s.text(
        "subtitle",
        "Ownership stays in the table. Time and overlap stay on the timeline.",
        62,
        148,
        23,
        MUTED,
    )
    cells = [
        ["WORKSTREAM", "OWNER", "STATE"],
        ["Research", "Lin", "done"],
        ["Prototype", "Mira", "active"],
        ["Pilot", "Kai", "planned"],
        ["Release", "Team", "planned"],
    ]
    s.table(
        "schedule_table",
        60,
        240,
        5,
        3,
        175,
        78,
        cells,
        theme="light-mint",
        border="grid",
        column_widths=[250, 120, 160],
    )
    x0, col = 720, 90
    s.text("timeline_head", "WEEK", x0, 215, 18, "#54715f")
    for i in range(8):
        x = x0 + i * col
        s.line("week_line" + str(i), [(x, 260), (x, 645)], color="#d5dfd5", width=1)
        if i < 7:
            s.text(
                "week" + str(i + 1),
                "W" + str(i + 1),
                x,
                275,
                20,
                INK,
                center=x + col / 2,
            )
    for i, (start, duration, color) in enumerate(
        [(0, 2, "#729a84"), (1, 3, "#c18a65"), (3, 3, "#a49b61"), (5, 2, "#8a7796")]
    ):
        y = 335 + i * 78
        s.rect(
            "task_bar" + str(i),
            x0 + start * col + 5,
            y,
            duration * col - 10,
            44,
            fill=color,
            stroke=color,
            radius=7,
            unit="bar" + str(i),
        )
        s.text(
            "duration" + str(i),
            f"{duration} weeks",
            0,
            y + 8,
            21,
            "#ffffff",
            center=x0 + (start + duration / 2) * col,
            unit="bar" + str(i),
        )
    s.text(
        "summary",
        "Research feeds the prototype; the pilot overlaps the release preparation.",
        60,
        700,
        23,
        "#54715f",
    )
    s.text(
        "foot",
        "Illustrative schedule • native light-mint theme + grid border • all rows, text and bars remain editable",
        60,
        780,
        18,
        MUTED,
    )
    s.details = {"table": [45, 225, 570, 450]}


def academic(s):
    s.description = "Ecology results page: native academic table, botanical symbols and an editable stacked fraction"
    s.scope = "Synthetic soil/plant measurements; layout demonstration, not a research finding"
    s.rect(
        "background", 0, 0, 1450, 900, fill="#ffffff", stroke="#ffffff", container=True
    )
    s.text("kicker", "ECOLOGY / METHODS & RESULTS", 70, 38, 18, "#62655f")
    s.text(
        "title",
        "Water retention in three microplots",
        70,
        82,
        40,
        "#252b24",
        font="方正仿宋简体",
    )
    s.text(
        "subtitle",
        "A paper-style page with a source-preserving equation and native academic table",
        72,
        145,
        21,
        MUTED,
    )
    s.text(
        "caption",
        "Table 1. Illustrative treatment means; n = 3 demonstration microplots.",
        70,
        245,
        20,
        "#424a40",
    )
    cells = [
        ["TREATMENT", "MOISTURE (%)", "BIOMASS (g)"],
        ["Control", "18.2", "42.0"],
        ["Mulch", "23.6", "47.8"],
        ["Mulch + shade", "27.4", "51.1"],
    ]
    s.table(
        "academic_table",
        70,
        295,
        4,
        3,
        215,
        72,
        cells,
        theme="academic",
        border="three-line",
        column_widths=[260, 205, 205],
    )
    # Editable botanical study vignette, not a second chart of the same table data.
    for i, (label, color, leaves) in enumerate(
        [
            ("CONTROL", "#9ea890", 2),
            ("MULCH", "#78946b", 3),
            ("MULCH + SHADE", "#547e54", 4),
        ]
    ):
        x = 885 + i * 175
        s.polygon(
            "pot" + str(i),
            [(x, 470), (x + 100, 470), (x + 85, 570), (x + 15, 570)],
            fill="#e4d4c3",
            color="#9d8771",
            unit="plant" + str(i),
        )
        s.line(
            "stem" + str(i),
            [(x + 50, 470), (x + 50, 355 - i * 12)],
            color=color,
            width=4,
            unit="plant" + str(i),
        )
        for j in range(leaves):
            y = 390 + j * 22
            side = -1 if j % 2 == 0 else 1
            s.ellipse(
                f"leaf{i}_{j}",
                x + 50 + (side * 22) - 18,
                y,
                36,
                18,
                fill=color,
                stroke=color,
                unit="plant" + str(i),
            )
        s.text("plant_label" + str(i), label, 0, 605, 16, "#4e5c48", center=x + 50)
    s.text("method_head", "GRAVIMETRIC MOISTURE", 70, 650, 20, "#4e5c48", bold=True)
    s.text("equation_w", "w =", 70, 725, 31, INK)
    s.text("equation_numerator", "wet mass − dry mass", 160, 695, 25, INK)
    s.line("equation_fraction", [(150, 735), (440, 735)], color=INK, width=1.5)
    s.text("equation_denominator", "dry mass", 230, 747, 25, INK)
    s.text("equation_percent", "× 100%", 475, 725, 29, INK)
    s.text(
        "method_note",
        "Dry-mass basis; not volumetric water content.",
        750,
        745,
        20,
        MUTED,
    )
    s.text(
        "foot",
        "Synthetic values and original illustration • no experimental or agronomic claim",
        70,
        850,
        19,
        MUTED,
    )
    s.details = {"table": [55, 230, 700, 380]}


SCENES = {
    "water_cycle": water_cycle,
    "calculus": calculus,
    "transit": transit,
    "gantt": gantt,
    "academic": academic,
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scene", choices=SCENES)
    parser.add_argument("--font", required=True)
    parser.add_argument("--filename", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--brief-file", type=Path, required=True, help="Resolved preferences and user requirements")
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError(
            "Use a new output receipt; refine an existing drawing with its IDs"
        )
    client = DrawingClient()
    caps = client.context("discover")["capabilities"]
    if args.font not in caps["fonts"]["registered"]:
        raise ValueError("Choose an exact discovered host font")
    if args.scene in ("gantt", "academic") and not caps.get("nativeTable", {}).get(
        "callable"
    ):
        raise ValueError(
            "Paired native TableManager host/Bridge required; no simulated table fallback"
        )
    context = client.context(
        "create", filename=args.filename, foldername="Agent-Diagrams/Diverse-Showcase",
        brief=json.loads(args.brief_file.read_text(encoding="utf-8"))
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps({**context, "stage": "created_before_planning"}), encoding="utf-8"
    )
    scene = Scene(client, context, args.font, "diverse-" + args.scene)
    SCENES[args.scene](scene)
    ops = scene.finish()
    refs = {}
    receipts = []
    revision = context["revision"]

    def resolve(value):
        if isinstance(value, str) and value.startswith("@") and value[1:] in refs:
            return refs[value[1:]]
        if isinstance(value, list):
            return [resolve(v) for v in value]
        if isinstance(value, dict):
            return {k: resolve(v) for k, v in value.items()}
        return value

    for start in range(0, len(ops), 350):
        receipt = client.apply(
            context["contextToken"],
            revision,
            [resolve(op) for op in ops[start : start + 350]],
            acceptance_level="medium",
        )
        receipts.append(receipt)
        refs.update(receipt.get("refs", {}))
        revision = receipt["revision"]
        args.output.write_text(
            json.dumps(
                {
                    **context,
                    "revision": revision,
                    "refs": refs,
                    "receipts": receipts,
                    "stage": "committed_partial",
                }
            ),
            encoding="utf-8",
        )
    for table in scene.tables:
        revision = client.read(context["contextToken"])["revision"]
        receipt = client.table(context["contextToken"], revision, **table)
        receipts.append(receipt)
        refs.update(receipt["refs"])
    checked = client.check(context["contextToken"], expected=scene.expected)
    preview = client.preview(
        context["contextToken"],
        base_revision=checked["revision"],
        out_path=str(args.output.with_suffix(".png")),
    )
    preview.pop("_base64", None)
    checked = client.check(context["contextToken"], preview_id=preview["previewId"])
    report = {
        **context,
        "method": "Authored Python + native APIs",
        "scene": args.scene,
        "description": scene.description,
        "scope": scene.scope,
        "refs": refs,
        "receipts": receipts,
        "revision": preview["revision"],
        "check": checked,
        "preview": preview,
        "details": scene.details,
        "visualReviewed": False,
    }
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "file": report["file"],
                "scene": args.scene,
                "check": checked["status"],
                "complete": preview["complete"],
                "png": preview["out_path"],
            }
        )
    )
    return 0 if checked["status"] == "pass" and preview["complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
