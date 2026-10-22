"""Chosen teaching design and observable encoding evidence, not aesthetic scores."""

from __future__ import annotations

import math
from typing import Annotated, Literal
from pydantic import BaseModel, ConfigDict, Field, model_validator
from teaching_geometry import KINDS, plan_teaching
from visual_diagnostics import is_visible

Text = Annotated[str, Field(min_length=1)]
Method = Literal[
    "sequence_window",
    "matrix_groups",
    "bitwidth_compare",
    "memory_map",
    "time_steps",
    "flow",
    "comparison_table",
]


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, str_strip_whitespace=True)


class DesignCandidate(Model):
    id: Text
    label: Text
    approach: Literal["mechanism", "process", "comparison", "reference", "overview"]
    description: Text


class DesignChoice(Model):
    source: Literal["answer", "user", "inherited", "delegated"]
    evidence: Text


class TeachingGoal(Model):
    id: Text
    requirement_id: Text
    question: Text
    method: Method
    components: Annotated[list[Text], Field(min_length=1)]


class TeachingPlan(Model):
    objective: Text
    candidates: Annotated[list[DesignCandidate], Field(min_length=2, max_length=3)]
    recommended: Text
    selected: Text | None = None
    reason: Text
    choice: DesignChoice | None = None
    goals: Annotated[list[TeachingGoal], Field(min_length=1)]

    @model_validator(mode="after")
    def design(self):
        ids = {c.id for c in self.candidates}
        if (
            len(ids) != len(self.candidates)
            or self.recommended not in ids
            or self.selected is not None
            and self.selected not in ids
        ):
            raise ValueError(
                "Design candidate IDs must be unique; selected/recommended must identify a candidate"
            )
        if len({g.id for g in self.goals}) != len(self.goals):
            raise ValueError("Teaching goal IDs must be unique")
        if any(len(set(g.components)) != len(g.components) for g in self.goals):
            raise ValueError("Each goal needs distinct component references")
        if self.selected:
            chosen = next(c for c in self.candidates if c.id == self.selected)
            if chosen.approach in ("mechanism", "comparison") and any(
                g.method in ("flow", "comparison_table") for g in self.goals
            ):
                raise ValueError(
                    "A mechanism/comparison design requires an observable spatial encoding; prose flow/table alone is not mechanism evidence"
                )
        return self


def validate_teaching(plan, requirements, required=False, confirmed=True):
    if plan is None:
        if required:
            raise ValueError(
                "TEACHING_PLAN_REQUIRED: first ask what visual structure explains this objective; submit 2–3 candidates, recommendation, confirmed choice and per-goal encodings"
            )
        return None
    model = TeachingPlan.model_validate(plan)
    if confirmed and (model.selected is None or model.choice is None):
        raise ValueError(
            "DESIGN_CHOICE_REQUIRED: use the client ask UI to confirm an expression candidate, or cite explicit delegation/inheritance; style selection is not a design choice"
        )
    ids = {r["id"] for r in requirements}
    if any(g.requirement_id not in ids for g in model.goals):
        raise ValueError("Teaching goals must reference actual user requirement IDs")
    return model


def design_options(plan):
    model = TeachingPlan.model_validate(plan)
    return {
        "question": model.objective + "：选择怎样的可视结构？",
        "recommended": next(
            i for i, c in enumerate(model.candidates) if c.id == model.recommended
        ),
        "options": [
            {"label": c.label, "description": c.description} for c in model.candidates
        ],
        "candidate_ids": [c.id for c in model.candidates],
        "reason": model.reason,
        "note": "Present with the client's actual ask tool before create. This payload does not prove the UI ran or user answered.",
    }


def check_teaching(elements, plan, required=False):
    if plan is None:
        return (
            [
                {
                    "code": "TEACHING_PLAN_REQUIRED",
                    "severity": "error",
                    "elementIds": [],
                    "message": "This teaching task has no confirmed expression plan; historical all-pass claims are not a current encoding audit",
                    "repairHint": "Keep the drawing; explicitly establish the user-approved task/design before modifying it",
                }
            ]
            if required
            else []
        )
    model = TeachingPlan.model_validate(plan)
    rows = [e for e in elements if not e.get("isDeleted")]
    issues = []

    def fail(code, goal, ids, message, actual=None):
        issues.append(
            {
                "code": "TEACHING_" + code,
                "severity": "error",
                "goalId": goal.id,
                "requirementId": goal.requirement_id,
                "elementIds": ids,
                "message": message,
                "actual": actual,
                "repairHint": "Draw/repair the selected encoding itself; mentioning it inside a paragraph does not satisfy the goal",
            }
        )

    for goal in model.goals:
        if goal.method in ("flow", "comparison_table"):
            # These are explicitly chosen overview/process/reference representations,
            # not a generic escape hatch for mechanism-mode goals.
            members = [
                e
                for e in rows
                if ((e.get("customData") or {}).get("agentDiagram") or {}).get(
                    "logicalId"
                )
                in goal.components
            ]
            bodies = [
                e
                for e in members
                if e.get("type") in ("rectangle", "diamond", "ellipse", "line")
                and is_visible(e)
            ]
            if not bodies:
                fail(
                    "OVERVIEW_MISSING",
                    goal,
                    [],
                    "No native process/reference objects match the declared goal",
                )
            continue
        for component in goal.components:
            members = [
                e
                for e in rows
                if ((e.get("customData") or {}).get("teaching") or {}).get("component")
                == component
            ]
            geometry = [e for e in members if e.get("type") != "text"]
            if not geometry:
                fail(
                    "ENCODING_MISSING",
                    goal,
                    [e["id"] for e in members],
                    f"{component}: no {goal.method} native encoding; labels/paragraph boxes cannot substitute",
                )
                continue
            meta = geometry[0]["customData"]["teaching"]
            if meta.get("kind") != goal.method:
                fail(
                    "METHOD_MISMATCH",
                    goal,
                    [e["id"] for e in geometry],
                    "Saved component does not use the chosen goal method",
                    meta.get("kind"),
                )
                continue
            try:
                expected = plan_teaching(meta["spec"])
            except (KeyError, ValueError, TypeError) as error:
                fail("SPEC_INVALID", goal, [geometry[0]["id"]], str(error))
                continue
            by_part = {}
            for element in members:
                m = element["customData"]["teaching"]
                if m.get("spec") != meta["spec"]:
                    fail(
                        "SPEC_CONFLICT",
                        goal,
                        [element["id"]],
                        "One component has conflicting source encodings",
                    )
                if m.get("part") in by_part:
                    fail(
                        "DUPLICATE_PART",
                        goal,
                        [element["id"], by_part[m["part"]]["id"]],
                        "Duplicate component part identity",
                    )
                by_part[m.get("part")] = element
            for op in expected["operations"]:
                part = op["customData"]["teaching"]["part"]
                actual = by_part.get(part)
                if actual is None:
                    fail(
                        "PART_MISSING",
                        goal,
                        [],
                        f"{component}:{part}: required encoded cell/block/link missing",
                    )
                    continue
                wanted_type = op.get("type", op.get("kind"))
                valid = (
                    actual.get("type") == wanted_type
                    and is_visible(actual)
                    and abs(float(actual.get("angle", 0))) < 1e-7
                )
                if "points" in op:
                    wanted = [(op["x"] + p[0], op["y"] + p[1]) for p in op["points"]]
                    points = [
                        (actual.get("x", 0) + p[0], actual.get("y", 0) + p[1])
                        for p in actual.get("points", [])
                    ]
                    valid = (
                        valid
                        and len(points) == len(wanted)
                        and all(math.dist(a, b) < 0.1 for a, b in zip(points, wanted))
                    )
                else:
                    valid = valid and all(
                        abs(float(actual.get(k, 0)) - op[k]) < 0.1
                        for k in ("x", "y", "width", "height")
                    )
                    valid = (
                        valid
                        and actual.get("backgroundColor")
                        == op["style"]["backgroundColor"]
                    )
                if not valid:
                    fail(
                        "ENCODING_CHANGED",
                        goal,
                        [actual["id"]],
                        f"{component}:{part}: saved geometry/state does not match the encoding (position, grouping, retained state or mapping)",
                        part,
                    )
            for label in expected["labels"]:
                part = label["ref"][len(component) + 1 :]
                actual = by_part.get(part)
                if (
                    not actual
                    or actual.get("type") != "text"
                    or not is_visible(actual)
                    or "".join(str(actual.get("text", "")).split())
                    != "".join(label["text"].split())
                ):
                    fail(
                        "LABEL_MISSING",
                        goal,
                        [actual["id"]] if actual else [],
                        f"{component}:{part}: encoded label/value missing or inconsistent",
                    )
    return issues


def expression_issues(plan, checks, elements):
    if plan is None:
        return []
    model = TeachingPlan.model_validate(plan)
    by_id = {e["id"]: e for e in elements if not e.get("isDeleted")}
    supplied = {}
    for item in checks or []:
        if not isinstance(item, dict) or set(item) != {
            "goal_id",
            "outcome",
            "element_ids",
            "observation",
            "without_prose",
        }:
            raise ValueError(
                "expression_checks need goal_id, outcome, element_ids, observation and without_prose (what geometry alone demonstrates)"
            )
        if item["goal_id"] in supplied or item["goal_id"] not in {
            g.id for g in model.goals
        }:
            raise ValueError(
                "Expression checks must identify each current goal at most once"
            )
        if item["outcome"] not in ("pass", "fail") or not all(
            isinstance(item[k], str) and item[k].strip()
            for k in ("observation", "without_prose")
        ):
            raise ValueError(
                "Expression observations need pass/fail and concrete visual evidence, not only a boolean checklist"
            )
        ids = item["element_ids"]
        if (
            not isinstance(ids, list)
            or not ids
            or any(identity not in by_id for identity in ids)
        ):
            raise ValueError("Expression evidence needs current native IDs")
        goal = next(g for g in model.goals if g.id == item["goal_id"])
        if goal.method in KINDS and not any(
            ((by_id[i].get("customData") or {}).get("teaching") or {}).get("component")
            in goal.components
            and by_id[i].get("type") != "text"
            for i in ids
        ):
            raise ValueError(
                "Mechanism expression evidence must reference its actual native encoded objects, not text IDs"
            )
        supplied[item["goal_id"]] = item
    return [
        {
            "code": "TEACHING_EXPRESSION_NOT_VERIFIED",
            "severity": "error",
            "elementIds": [],
            "goalId": g.id,
            "message": "Actual PNG expression review missing/failed: " + g.question,
        }
        for g in model.goals
        if supplied.get(g.id, {}).get("outcome") != "pass"
    ]
