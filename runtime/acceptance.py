"""Acceptance depth, issue triage and explicit PNG-based geometric adjudication.

Levels change review depth, never model effort or native reference correctness.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

LEVELS = ("low", "medium", "high")
DEFAULT_LEVEL = "medium"
VISUAL_CODES = frozenset({"BODY_OVERLAP", "ARROW_CROSSES_NODE", "ARROW_LABEL_OCCLUSION", "TEXT_OUTSIDE_CONTAINER",
    "TEXT_TEXT_OVERLAP", "TEXT_PAINTED_OVER", "LINE_THROUGH_TEXT", "BORDER_THROUGH_TEXT", "SMALL_OUTPUT_TEXT", "UNSUPPORTED_GEOMETRY"})
REQUIRED_VISUAL_CHECKS = {
    "low": (),
    "medium": ("content", "readability", "occlusion"),
    "high": ("content", "readability", "occlusion", "connections", "hierarchy_style"),
}


def level(value: str | None) -> str:
    result = DEFAULT_LEVEL if value is None else value
    if result not in LEVELS:
        raise ValueError("acceptance_level must be low, medium, or high")
    return result


def issue_id(issue: dict) -> str:
    identity = {"code": issue.get("code"), "elementIds": sorted(str(v) for v in issue.get("elementIds", [])),
                "type": issue.get("type"), "actual": issue.get("actual")}
    return "issue_" + hashlib.sha256(json.dumps(identity, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


def is_resolvable(issue: dict) -> bool:
    return issue.get("code") in VISUAL_CODES and issue.get("source") != "native_validation"


def blocks(issue: dict, acceptance_level: str) -> bool:
    if issue.get("severity", "error") == "info":
        return False
    if issue.get("code") == "SMALL_OUTPUT_TEXT":
        # Output-size trigger is advisory; real readability remains in visual QA.
        return False
    if issue.get("code") == "UNSUPPORTED_GEOMETRY":
        return acceptance_level != "low"
    if issue.get("severity", "error") == "error":
        return True
    if acceptance_level == "low":
        return False
    if acceptance_level == "high":
        return issue.get("category") != "cosmetic"
    code = str(issue.get("code", ""))
    return any(word in code for word in ("TEXT", "LABEL", "OCCLUSION", "COLLISION", "OVERFLOW"))


def decorate(issues: list[dict], acceptance_level: str) -> list[dict]:
    acceptance_level = level(acceptance_level)
    return [{**issue, "issueId": issue_id(issue), "blocking": blocks(issue, acceptance_level),
             "resolvableWithVisualEvidence": is_resolvable(issue)} for issue in issues]


def unsupported_issues(unsupported: list[dict]) -> list[dict]:
    return [{"code": "UNSUPPORTED_GEOMETRY", "severity": "warning", "elementIds": [item["elementId"]] if item.get("elementId") else [],
             "message": item.get("reason", "Geometry needs visual inspection"), "type": item.get("type"),
             "evidence": "unsupported_geometry", "visualReviewRequired": True} for item in unsupported]


def triage(issues: list[dict], acceptance_level: str, dispositions: list[dict] | None = None) -> tuple[list[dict], list[dict]]:
    decorated = decorate(issues, acceptance_level)
    by_id = {issue["issueId"]: issue for issue in decorated}
    decisions = {}
    for decision in dispositions or []:
        identity = decision.get("issue_id")
        if identity in decisions or identity not in by_id:
            raise ValueError("Disposition must identify one current issue exactly once")
        issue = by_id[identity]
        if not is_resolvable(issue) or decision.get("decision") not in ("false_positive", "intentional") or not str(decision.get("reason", "")).strip():
            raise ValueError("Only geometric candidates may be adjudicated with a reason and actual PNG evidence")
        decisions[identity] = decision
    for issue in decorated:
        decision = decisions.get(issue["issueId"])
        if decision:
            issue["disposition"] = decision
            issue["blocking"] = False
    return [i for i in decorated if i["blocking"]], [i for i in decorated if not i["blocking"]]


def visual_check_issues(acceptance_level: str, checks: dict[str, str] | None, applicability: dict[str, bool] | None = None) -> list[dict]:
    checks = checks or {}
    required = REQUIRED_VISUAL_CHECKS[level(acceptance_level)]
    result = []
    for name in required:
        outcome = checks.get(name)
        if outcome not in ("pass", "not_applicable") or (outcome == "not_applicable" and (applicability or {}).get(name)):
            result.append({"code": "VISUAL_CHECK_FAILED" if outcome == "fail" else "VISUAL_CHECK_MISSING", "severity": "error",
                "elementIds": [], "message": f"The {name} visual check must be recorded after inspecting the current PNG.", "check": name})
    for name, outcome in checks.items():
        if outcome not in ("pass", "not_applicable", "fail"):
            raise ValueError("visual_checks values must be pass, not_applicable, or fail")
        if outcome == "fail" and name not in required:
            result.append({"code": "VISUAL_CHECK_FAILED", "severity": "error", "elementIds": [], "message": f"Visual check failed: {name}", "check": name})
    return result
