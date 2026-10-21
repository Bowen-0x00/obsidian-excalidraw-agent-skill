"""Reference-driven visual plans and relation-specific physical checks (not CAD)."""

from __future__ import annotations

import math
from typing import Annotated, Literal
from pydantic import BaseModel, ConfigDict, Field, model_validator

from geometry_diagnostics import _scene_points
from visual_diagnostics import is_visible


class PlanModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class View(PlanModel):
    id: Annotated[str, Field(min_length=1)]
    method: Literal["oblique", "section", "exploded", "page", "comparison"]
    description: Annotated[str, Field(min_length=1)]


class VisualObject(PlanModel):
    id: Annotated[str, Field(min_length=1)]
    role: Annotated[str, Field(min_length=1)]
    views: Annotated[list[str], Field(min_length=1)]
    label: str | None = None


class PhysicalRelation(PlanModel):
    kind: Literal["supported_by", "contains"]
    source: str
    target: str


class Reference(PlanModel):
    source: Annotated[str, Field(min_length=1)]
    mode: Literal["faithful", "structural", "style_only"]
    observations: Annotated[list[str], Field(min_length=1)]
    uncertainties: list[str]


class VisualPlan(PlanModel):
    purpose: Annotated[str, Field(min_length=1)]
    reference: Reference | None = None
    views: Annotated[list[View], Field(min_length=1)]
    objects: Annotated[list[VisualObject], Field(min_length=1)]
    relations: list[PhysicalRelation] = []
    illustrative_limits: Annotated[list[str], Field(min_length=1)]

    @model_validator(mode="after")
    def identities(self):
        views = {v.id for v in self.views}
        objects = {o.id for o in self.objects}
        if len(views) != len(self.views) or len(objects) != len(self.objects):
            raise ValueError("visual plan view/object IDs must be unique")
        for obj in self.objects:
            if set(obj.views) - views or len(set(obj.views)) != len(obj.views):
                raise ValueError(f"object {obj.id} needs unique declared views")
        for relation in self.relations:
            if (
                relation.source not in objects
                or relation.target not in objects
                or relation.source == relation.target
            ):
                raise ValueError("physical relation must identify two declared objects")
        return self


def _meta(element):
    return (element.get("customData") or {}).get("technicalIllustration") or {}


def geometry_matches(element):
    meta = _meta(element)
    expected = meta.get("expected")
    if not expected or abs(float(element.get("angle", 0))) > 1e-7:
        return False
    if "points" in expected:
        actual = _scene_points(element)
        wanted = [
            (expected["x"] + p[0], expected["y"] + p[1]) for p in expected["points"]
        ]
        if len(actual) != len(wanted):
            return False
        return all(math.dist(a, b) <= 0.05 for a, b in zip(actual, wanted))
    return all(
        abs(float(element.get(k, 0)) - v) <= 0.05
        for k, v in expected.items()
        if k in ("x", "y", "width", "height")
    )


def _volume(meta):
    model = meta.get("model")
    if not model:
        return None
    return [
        (model[k], model[k] + model[size])
        for k, size in (("u", "width"), ("v", "depth"), ("z", "height"))
    ]


def projected_overlap_pairs(elements, plan):
    """Only known, unchanged projected solids with disjoint model volumes qualify.

    Text, wires, interpenetrating solids and user-edited polygons are never waived.
    """
    if not plan:
        return set()
    declared = {(view, obj["id"]) for obj in plan["objects"] for view in obj["views"]}
    rows = [
        e
        for e in elements
        if not e.get("isDeleted")
        and _meta(e).get("role") == "body"
        and geometry_matches(e)
        and (_meta(e).get("viewId"), _meta(e).get("objectId")) in declared
        and _volume(_meta(e))
    ]
    result = set()
    for i, a in enumerate(rows):
        ma = _meta(a)
        for b in rows[i + 1 :]:
            mb = _meta(b)
            if ma["viewId"] != mb["viewId"] or ma["objectId"] == mb["objectId"]:
                continue
            if ma.get("projection") != mb.get("projection") or ma.get(
                "origin"
            ) != mb.get("origin"):
                continue
            va, vb = _volume(ma), _volume(mb)
            if any(
                min(aa[1], bb[1]) - max(aa[0], bb[0]) <= 0.001 for aa, bb in zip(va, vb)
            ):
                result.add(frozenset((a["id"], b["id"])))
    return result


def check_illustration(elements, plan):
    if not plan:
        return []
    spec = VisualPlan.model_validate(plan)
    rows = [e for e in elements if not e.get("isDeleted")]
    objects = {}
    issues = []

    def fail(code, ids, message, actual=None):
        issues.append(
            {
                "code": "ILLUSTRATION_" + code,
                "severity": "error",
                "elementIds": ids,
                "message": message,
                "actual": actual,
                "repairHint": "Repair the current named object/geometry/relation; preserve unrelated native IDs",
            }
        )

    for element in rows:
        meta = _meta(element)
        if not meta:
            continue
        key = (meta.get("viewId"), meta.get("objectId"))
        objects.setdefault(key, []).append(element)
        if meta.get("expected") and not geometry_matches(element):
            fail(
                "GEOMETRY_CHANGED",
                [element["id"]],
                "Saved native geometry differs from its projection/array/leader construction",
                key,
            )
        if meta.get("constructionRefs"):
            present = {
                ((e.get("customData") or {}).get("dsl") or {}).get("key", e.get("id"))
                for e in rows
                if _meta(e).get("viewId") == meta.get("viewId")
                and _meta(e).get("itemId") == meta.get("itemId")
            }
            missing = set(meta["constructionRefs"]) - present
            if missing and not any(
                i["code"] == "ILLUSTRATION_CONSTRUCTION_MISSING"
                and i.get("actual") == sorted(missing)
                for i in issues
            ):
                fail(
                    "CONSTRUCTION_MISSING",
                    [element["id"]],
                    "A required layer/array member is missing",
                    sorted(missing),
                )
        if meta.get("role") == "annotation" and meta.get("targetObject"):
            targets = [
                e
                for e in rows
                if _meta(e).get("viewId") == meta.get("viewId")
                and _meta(e).get("objectId") == meta["targetObject"]
                and _meta(e).get("role") == "body"
            ]
            if not targets:
                fail(
                    "ANNOTATION_TARGET",
                    [element["id"]],
                    "Leader target object is missing",
                    meta["targetObject"],
                )
            else:
                # Exact hit requires target to lie in a native body AABB; PNG confirms visible face.
                point = _scene_points(element)[-1]

                def contains(e):
                    pts = (
                        _scene_points(e)
                        if e.get("points")
                        else [
                            (e["x"], e["y"]),
                            (e["x"] + e["width"], e["y"] + e["height"]),
                        ]
                    )
                    return (
                        min(p[0] for p in pts) - 1
                        <= point[0]
                        <= max(p[0] for p in pts) + 1
                        and min(p[1] for p in pts) - 1
                        <= point[1]
                        <= max(p[1] for p in pts) + 1
                    )

                if not any(contains(e) for e in targets):
                    fail(
                        "ANNOTATION_MISS",
                        [element["id"], *[e["id"] for e in targets]],
                        "Leader misses the declared object",
                        point,
                    )
    for obj in spec.objects:
        for view in obj.views:
            members = objects.get((view, obj.id), [])
            bodies = [
                e
                for e in members
                if _meta(e).get("role") in ("body", "detail")
                and is_visible(e)
                and (
                    e.get("type") in ("image", "embeddable")
                    or (
                        e.get("strokeWidth", 1) > 0
                        and str(e.get("strokeColor", "#1e1e1e")).lower()
                        not in ("transparent", "none", "")
                    )
                    or str(e.get("backgroundColor", "transparent")).lower()
                    not in ("transparent", "none", "")
                )
            ]
            if not bodies:
                fail(
                    "OBJECT_MISSING",
                    [],
                    f"Required object {obj.id} has no native body in view {view}",
                )
            if obj.label is not None and not any(
                e.get("type") == "text" and e.get("text") == obj.label for e in members
            ):
                fail(
                    "LABEL_MISMATCH",
                    [e["id"] for e in members],
                    f"Required label for {obj.id} is absent/inconsistent in {view}",
                    obj.label,
                )
    object_specs = {o.id: o for o in spec.objects}
    solids = {}
    for (view, obj), members in objects.items():
        for element in members:
            meta = _meta(element)
            if meta.get("role") == "body" and _volume(meta):
                solids[(view, obj)] = element
                break
    for i, ((view, obj), a) in enumerate(solids.items()):
        for (other_view, other_obj), b in list(solids.items())[i + 1 :]:
            if view != other_view:
                continue
            ma, mb = _meta(a), _meta(b)
            if ma.get("origin") != mb.get("origin") or ma.get("projection") != mb.get(
                "projection"
            ):
                continue
            va, vb = _volume(ma), _volume(mb)
            if all(
                min(aa[1], bb[1]) - max(aa[0], bb[0]) > 0.001 for aa, bb in zip(va, vb)
            ):
                contained = any(
                    r.kind == "contains" and {r.source, r.target} == {obj, other_obj}
                    for r in spec.relations
                )
                if not contained:
                    fail(
                        "INTERPENETRATION",
                        [a["id"], b["id"]],
                        "Independent solids intersect in the model; projection overlap is not a waiver",
                        [obj, other_obj],
                    )
    for rel in spec.relations:
        views = set(object_specs[rel.source].views) & set(
            object_specs[rel.target].views
        )
        if not views:
            fail(
                "RELATION_VIEW",
                [],
                "Related objects have no common view",
                rel.model_dump(),
            )
        for view in views:
            a = [e for e in objects.get((view, rel.source), []) if _volume(_meta(e))]
            b = [e for e in objects.get((view, rel.target), []) if _volume(_meta(e))]
            if not a or not b:
                continue  # object-missing issue explains absent geometry
            va, vb = _volume(_meta(a[0])), _volume(_meta(b[0]))
            footprint = all(
                bb[0] - 0.001 <= aa[0] and aa[1] <= bb[1] + 0.001
                for aa, bb in zip(va[:2], vb[:2])
            )
            valid = footprint and (
                abs(va[2][0] - vb[2][1]) <= 0.001
                if rel.kind == "supported_by"
                else vb[2][0] <= va[2][0] and va[2][1] <= vb[2][1]
            )
            if not valid:
                fail(
                    "PHYSICAL_RELATION",
                    [a[0]["id"], b[0]["id"]],
                    f"{rel.source} does not satisfy {rel.kind} {rel.target} in {view}",
                    rel.model_dump(),
                )
    return issues


def annotation_object_ids(elements, view_id, target_object):
    """Include only the annotation target and its geometrically proven supports."""
    solids = {}
    for element in elements:
        meta = _meta(element)
        if (
            meta.get("viewId") == view_id
            and meta.get("role") == "body"
            and _volume(meta)
            and geometry_matches(element)
        ):
            solids.setdefault(meta["objectId"], meta)
    allowed = {target_object}
    changed = True
    while changed:
        changed = False
        for child in list(allowed):
            a = solids.get(child)
            if a is None:
                continue
            va = _volume(a)
            for identity, b in solids.items():
                if (
                    identity in allowed
                    or a.get("origin") != b.get("origin")
                    or a.get("projection") != b.get("projection")
                ):
                    continue
                vb = _volume(b)
                if abs(va[2][0] - vb[2][1]) <= 0.001 and all(
                    bb[0] <= aa[0] + 0.001 and aa[1] <= bb[1] + 0.001
                    for aa, bb in zip(va[:2], vb[:2])
                ):
                    allowed.add(identity)
                    changed = True
    return {
        e["id"]
        for e in elements
        if _meta(e).get("viewId") == view_id
        and _meta(e).get("objectId") in allowed
        and e.get("type") != "text"
    }
