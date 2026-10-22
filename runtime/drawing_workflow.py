"""Client-private drawing briefs and stable task/canvas ownership.

This records the Agent's cited user choices, not proof that a choice UI ran.
The authenticated Bridge remains trusted; raw HTTP is not a security sandbox.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from runtime_config import artifact_directory, load_connection
from drawing_entry import DiagramType, diagram_type
from representation_contract import validate_contract
from typing import Annotated, Literal
from pydantic import BaseModel, ConfigDict, Field, model_validator
from representation_contract import RepresentationContract
from illustration_contract import VisualPlan
from teaching_contract import TeachingPlan, validate_teaching


class Choice(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    value: Annotated[str, Field(min_length=1)]
    source: Literal["user", "answer", "inherited", "delegated"]
    evidence: Annotated[str, Field(min_length=1)]


class Preferences(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    style: Choice
    review: Choice
    palette: Choice
    background: Choice
    font: Choice


class Requirement(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    id: Annotated[str, Field(min_length=1)]
    description: Annotated[str, Field(min_length=1)]


class DrawingBrief(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    task_id: Annotated[str, Field(min_length=1)]
    preferences: Preferences
    requirements: Annotated[list[Requirement], Field(min_length=1)]
    diagram_type: DiagramType = "auto"
    representation: RepresentationContract | None = None
    visual_plan: VisualPlan | None = None
    teaching_plan: TeachingPlan | None = None

    @model_validator(mode="after")
    def resolved(self):
        validate_brief(self.model_dump(exclude_unset=True))
        return self

PREFERENCES = ("style", "review", "palette", "background", "font")
SOURCES = {"user", "answer", "inherited", "delegated"}


def validate_brief(brief: Any) -> dict:
    required = {"task_id", "preferences", "requirements"}
    if not isinstance(brief, dict) or not required.issubset(brief) or set(brief) - required - {"diagram_type", "representation", "visual_plan", "teaching_plan"}:
        raise ValueError("DRAWING_BRIEF_REQUIRED: brief needs task_id/preferences/requirements and task-appropriate representation/visual_plan/teaching_plan")
    if not isinstance(brief["task_id"], str) or not brief["task_id"].strip():
        raise ValueError("brief.task_id must identify this user drawing request")
    preferences = brief["preferences"]
    if not isinstance(preferences, dict) or set(preferences) != set(PREFERENCES):
        raise ValueError("PREFERENCES_REQUIRED: resolve style, review, palette, background and font individually")
    for name, choice in preferences.items():
        if not isinstance(choice, dict) or set(choice) != {"value", "source", "evidence"}:
            raise ValueError(f"brief.preferences.{name} needs value, source and cited user evidence")
        if not isinstance(choice["source"], str) or choice["source"] not in SOURCES or any(not isinstance(choice[key], str) or not choice[key].strip() for key in ("value", "evidence")):
            raise ValueError(f"brief.preferences.{name}: source must be user/answer/inherited/delegated with nonempty value and evidence")
    if preferences["review"]["value"] not in ("low", "medium", "high"):
        raise ValueError("brief.preferences.review.value must be low, medium or high")
    requirements = brief["requirements"]
    if not isinstance(requirements, list) or not requirements:
        raise ValueError("REQUIREMENTS_REQUIRED: list the user's required content, comparisons, relations and invariants")
    identities = set()
    for item in requirements:
        if not isinstance(item, dict) or set(item) != {"id", "description"} or any(not isinstance(item[k], str) or not item[k].strip() for k in ("id", "description")):
            raise ValueError("Each brief.requirements item needs a nonempty id and description")
        if item["id"] in identities:
            raise ValueError("Requirement IDs must be unique")
        identities.add(item["id"])
    kind = diagram_type("\n".join(item["description"] for item in requirements), brief.get("diagram_type", "auto"))
    validate_contract(brief.get("representation"), kind)
    if brief.get("visual_plan") is not None:
        VisualPlan.model_validate(brief["visual_plan"])
    elif kind in ("physical_structure", "explanatory_page"):
        raise ValueError("VISUAL_PLAN_REQUIRED: declare purpose, views, objects, physical relations and illustrative limits; do not invent a port/signal network for a section or slide")
    validate_teaching(brief.get("teaching_plan"), requirements, required=kind == "teaching")
    return json.loads(json.dumps(brief, ensure_ascii=False, allow_nan=False))


def _key(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def _host() -> str:
    connection = load_connection()
    # SSH aliases and tunnel ports can change without changing the host vault.
    return str(connection.get("host_vault_path") or connection.get("vault_path") or connection.get("bridge_url") or "default")


def _root() -> Path:
    return artifact_directory() / "drawing-tasks"


def _load(path: Path) -> dict | None:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def _save(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)


def task_path(task_id: str) -> Path:
    return _root() / "tasks" / (_key([_host(), task_id]) + ".json")


def canvas_path(file: str) -> Path:
    return _root() / "canvases" / (_key([_host(), file]) + ".json")


def reserve_create(brief: dict) -> dict:
    brief = validate_brief(brief)
    path = task_path(brief["task_id"])
    if path.exists():
        previous = _load(path)
        raise ValueError(f"TASK_ALREADY_STARTED: bind the same task file {previous.get('file')!r}; do not recreate or change task_id after an unknown/failed transaction")
    record = {"brief": brief, "file": None, "status": "creating"}
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive reservation prevents concurrent duplicate canvases for one task.
    with path.open("x", encoding="utf-8") as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2)
    return record


def attach_context(context: dict, brief: dict | None = None) -> dict | None:
    file, token = context["file"], context["contextToken"]
    owner = _load(canvas_path(file))
    if brief is not None:
        brief = validate_brief(brief)
        path = task_path(brief["task_id"])
        previous = _load(path)
        if previous and previous.get("file") not in (None, file):
            raise ValueError("TASK_CANVAS_CONFLICT: this task already owns another file; repair that file")
        if owner and owner["brief"] != brief:
            prior = _load(review_path(file, owner["brief"]["task_id"]))
            if not prior or prior.get("status") != "completed" or owner["brief"]["task_id"] == brief["task_id"]:
                raise ValueError("CANVAS_TASK_CONFLICT: repair the existing task; only a new request after completed review can replace its brief")
        if previous and previous["brief"] != brief:
            raise ValueError("TASK_BRIEF_CONFLICT: do not silently change requirements or selected review depth")
        owner = {**(owner or {}), "brief": brief, "file": file, "status": "bound"}
        if not previous or previous["brief"]["task_id"] != brief["task_id"]:
            owner.pop("representationBindings", None)
            owner.pop("delivery", None)
        _save(path, owner)
        _save(canvas_path(file), owner)
    if owner:
        _save(_root() / "contexts" / (_key(token) + ".json"), {"file": file, "task_id": owner["brief"]["task_id"]})
    return owner


def for_context(token: str) -> dict | None:
    binding = _load(_root() / "contexts" / (_key(token) + ".json"))
    record = _load(canvas_path(binding["file"])) if binding else None
    return record if record and binding["task_id"] == record["brief"]["task_id"] else None


def require_context(token: str) -> dict:
    record = for_context(token)
    if record is None:
        raise ValueError("DRAWING_BRIEF_REQUIRED: bind this explicit file with a resolved brief before modifying it; read/discovery remain available")
    return record


def review_path(file: str, task_id: str) -> Path:
    return _root() / "reviews" / (_key([_host(), file, task_id]) + ".json")


def requirement_issues(requirements: list[dict], checks: list[dict] | None, element_ids: set[str]) -> list[dict]:
    supplied = {}
    for check in checks or []:
        if not isinstance(check, dict) or set(check) != {"requirement_id", "outcome", "element_ids", "evidence"}:
            raise ValueError("requirement_checks needs requirement_id, outcome, element_ids and evidence for each user requirement")
        identity = check["requirement_id"]
        if identity in supplied or identity not in {r["id"] for r in requirements}:
            raise ValueError("Requirement checks must identify each declared requirement once; no unknown IDs")
        if check["outcome"] not in ("pass", "fail"):
            raise ValueError("A user requirement outcome must be pass or fail, not not_applicable")
        ids = check["element_ids"]
        if not isinstance(ids, list) or not ids or any(not isinstance(i, str) or i not in element_ids for i in ids):
            raise ValueError("Requirement evidence must reference existing current native element IDs")
        if not isinstance(check["evidence"], str) or not check["evidence"].strip():
            raise ValueError("Explain how the named elements satisfy this user requirement; labels existing alone is not semantic proof")
        supplied[identity] = check
    return [{"code": "REQUIREMENT_NOT_VERIFIED", "severity": "error", "requirementId": r["id"], "elementIds": [],
             "message": r["description"]} for r in requirements if supplied.get(r["id"], {}).get("outcome") != "pass"]


def set_representation_bindings(token: str, bindings: dict[str, list[str]]) -> dict:
    record = require_context(token)
    if record["brief"].get("representation") is None:
        raise ValueError("REPRESENTATION_REQUIRED: no component/port/signal contract was declared in this task brief")
    if not isinstance(bindings, dict) or any(not isinstance(k, str) or not isinstance(v, list) or not v or any(not isinstance(i, str) or not i for i in v) for k, v in bindings.items()):
        raise ValueError("bindings must map declared component/signal IDs to nonempty lists of native element IDs")
    record["representationBindings"] = bindings
    record.pop("delivery", None)
    _save(canvas_path(record["file"]), record)
    _save(task_path(record["brief"]["task_id"]), record)
    return record


def save_delivery(token: str, receipt: dict) -> None:
    record = require_context(token)
    record["delivery"] = receipt
    _save(canvas_path(record["file"]), record)
    _save(task_path(record["brief"]["task_id"]), record)


def delivery_evidence(record: dict, scene: dict, receipt: dict, ledger: Any) -> dict:
    """Identity/completion gate shared by native and CLI delivery."""
    if scene["file"] != record["file"] or receipt["file"] != record["file"] or receipt["revision"] != scene["revision"]:
        raise ValueError("STALE_DELIVERY: current task, canvas and PNG must name the same file/revision")
    if receipt["scope"] != "all" or not receipt["complete"]:
        raise ValueError("INCOMPLETE_DELIVERY: a complete all-canvas PNG is required")
    last = ledger.rounds[-1] if ledger.rounds else None
    if ledger.status != "completed" or not last or last["status"] != "completed" or last["revision"] != receipt["revision"] or last["previewId"] != receipt["previewId"]:
        raise ValueError("DELIVERY_REVIEW_REQUIRED: no completed review for this exact current PNG; check=pass is not completion")
    if not last["visualReviewed"] or not last["previewComplete"]:
        raise ValueError("DELIVERY_REVIEW_REQUIRED: current PNG was not actually reviewed or resources were incomplete")
    return last
