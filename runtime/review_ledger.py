from __future__ import annotations

import datetime
import json
import re
from pathlib import Path
from typing import Any

from runtime_config import artifact_directory
from acceptance import DEFAULT_LEVEL, TEXT_CONFLICT_CODES, issue_id, level, triage, unsupported_issues, visual_check_issues


class ReviewLedger:
    """Persistent ledger for tracking diagram review rounds and stop conditions."""

    def __init__(
        self,
        context_token: str,
        ledger_path: str | None = None,
        max_rounds: int | None = None,
        acceptance_level: str | None = None,
        canvas_key: str | None = None,
    ) -> None:
        if max_rounds is not None and (isinstance(max_rounds, bool) or not isinstance(max_rounds, int) or max_rounds < 1):
            raise ValueError("max_rounds must be a positive integer")
        self.context_token = context_token
        self.canvas_key = canvas_key
        self.max_rounds = max_rounds or 5

        if ledger_path:
            self.path = Path(ledger_path)
        else:
            sanitized = re.sub(r"[^\w\-.]", "_", context_token[:24])
            self.path = artifact_directory() / "ledgers" / f"{sanitized}_ledger.json"

        self.rounds: list[dict[str, Any]] = []
        self.status: str = "continue"
        self.acceptance_level = DEFAULT_LEVEL
        self.expected: list[dict[str, Any]] = []
        self._load()
        if acceptance_level is not None:
            self.acceptance_level = level(acceptance_level)
        if max_rounds is not None:
            self.max_rounds = min(self.max_rounds, max_rounds) if self.rounds else max_rounds

    def _load(self) -> None:
        if self.path.exists():
            data = json.loads(self.path.read_text(encoding="utf-8"))
            if self.canvas_key is not None:
                if data.get("canvasKey") != self.canvas_key:
                    raise ValueError("Review ledger belongs to a different canvas")
            elif data.get("contextToken") != self.context_token:
                raise ValueError("Review ledger belongs to a different canvas context")
            self.max_rounds = data["maxRounds"]
            self.rounds = data["rounds"]
            self.status = data["status"]
            self.acceptance_level = level(data.get("acceptanceLevel"))
            self.expected = data.get("expected", [])

    def save(self) -> str:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "contextToken": self.context_token,
            "canvasKey": self.canvas_key,
            "maxRounds": self.max_rounds,
            "acceptanceLevel": self.acceptance_level,
            "expected": self.expected,
            "currentRound": len(self.rounds),
            "status": self.status,
            "updatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "rounds": self.rounds,
        }
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        temporary.replace(self.path)
        return str(self.path.resolve())


    @classmethod
    def _calculate_severity_score(cls, issues: list[dict[str, Any]]) -> float:
        score = 0.0
        for iss in issues:
            sev = iss.get("severity", "error")
            if sev == "error":
                score += 3.0
            elif sev == "warning":
                score += 1.0
            else:
                score += 0.25
        return score

    def record_round(
        self,
        revision: str,
        preview_id: str,
        visual_reviewed: bool,
        visual_issues: list[dict[str, Any]] | None = None,
        changes_summary: str | list[Any] | None = None,
        check_result: dict[str, Any] | None = None,
        preview_complete: bool = True,
        visual_checks: dict[str, str] | None = None,
        dispositions: list[dict[str, Any]] | None = None,
        detail_preview_ids: list[str] | None = None,
        requirement_checks: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """Count initial review as round one; never bypass the cap on unknown/incomplete output."""
        if len(self.rounds) >= self.max_rounds:
            raise ValueError(f"Review budget exhausted ({self.max_rounds} rounds)")
        if self.status == "needs_attention":
            raise ValueError("Automatic review stopped for unresolved issues; report them instead of bypassing the stop.")
        if any(entry["previewId"] == preview_id for entry in self.rounds):
            raise ValueError("This preview has already been reviewed; do not count the same image twice")
        round_number = len(self.rounds) + 1
        check = check_result or {}
        hard_issues = check.get("issues", [])
        unsupported_checks = check.get("unsupportedChecks", [])
        all_round_issues = [{"source": "hard_check", **issue} for issue in hard_issues]
        all_round_issues.extend({"source": "visual", **issue} for issue in (visual_issues or []))
        all_round_issues.extend(unsupported_issues(unsupported_checks))
        all_round_issues.extend(visual_check_issues(self.acceptance_level, visual_checks, check.get("visualApplicability")))
        if not visual_reviewed:
            all_round_issues.append({"code": "VISUAL_NOT_REVIEWED", "severity": "error", "reason": "PNG has not actually been inspected"})
        if not preview_complete:
            all_round_issues.append({"code": "PREVIEW_INCOMPLETE", "severity": "error", "reason": "Required exported resources are missing"})
        if check.get("status") not in ("pass", "fail", "unknown") or (check.get("status") != "pass" and not hard_issues and not unsupported_checks):
            all_round_issues.append({"code": "CHECK_NOT_PASSED", "severity": "error", "reason": "Hard check evidence is absent or inconsistent"})
        if dispositions and not visual_reviewed:
            raise ValueError("A geometric disposition requires inspection of the current PNG")
        issues_by_id = {issue_id(issue): issue for issue in all_round_issues}
        for decision in dispositions or []:
            preview = decision.get("preview_id")
            if preview not in {preview_id, *(detail_preview_ids or [])}:
                raise ValueError("Disposition evidence must be a current registered PNG listed as actually viewed")
            issue = issues_by_id.get(decision.get("issue_id"))
            if issue and issue.get("code") in TEXT_CONFLICT_CODES and preview not in (detail_preview_ids or []):
                raise ValueError("A text-conflict false positive requires a readable current detail PNG, not only an overview")
        for issue in all_round_issues:
            issue.setdefault("severity", "error")
            if issue["severity"] not in ("error", "warning", "info"):
                raise ValueError("Issue severity must be error, warning, or info")
        unresolved, advisories = triage(all_round_issues, self.acceptance_level, dispositions)
        severity_score = self._calculate_severity_score(unresolved)
        if not unresolved:
            status, message = "completed", "Current PNG and required acceptance checks passed; disclosed advisories may remain."
        elif round_number >= self.max_rounds:
            status, message = "needs_attention", f"Reached {self.max_rounds} rounds with unresolved issues."
        elif round_number >= 3 and all(entry.get("acceptanceLevel", DEFAULT_LEVEL) == self.acceptance_level for entry in self.rounds[-2:]) and severity_score >= self.rounds[-1]["severityScore"] >= self.rounds[-2]["severityScore"]:
            status, message = "needs_attention", "No improvement in unresolved issue severity for two consecutive rounds."
        else:
            status, message = "continue", f"Round {round_number}: repair the {len(unresolved)} remaining issues, then export and inspect again."
        self.status = status
        self.rounds.append({
            "round": round_number,
            "revision": revision,
            "previewId": preview_id,
            "visualReviewed": visual_reviewed,
            "previewComplete": preview_complete,
            "changesSummary": changes_summary,
            "acceptanceLevel": self.acceptance_level,
            "visualChecks": visual_checks or {},
            "requirementChecks": requirement_checks or [],
            "dispositions": dispositions or [],
            "detailPreviewIds": detail_preview_ids or [],
            "advisories": advisories,
            "hardIssues": hard_issues,
            "visualIssues": visual_issues or [],
            "unsupportedChecks": unsupported_checks,
            "allIssues": all_round_issues,
            "severityScore": severity_score,
            "status": status,
            "message": message,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        })
        return {
            "status": status,
            "round": round_number,
            "maxRounds": self.max_rounds,
            "acceptanceLevel": self.acceptance_level,
            "advisories": advisories,
            "rawCheckStatus": check.get("status"),
            "visualChecks": visual_checks or {},
            "unresolvedIssues": unresolved,
            "visualReviewed": visual_reviewed,
            "ledgerPath": self.save(),
            "message": message,
        }
