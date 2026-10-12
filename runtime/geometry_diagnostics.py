from __future__ import annotations

from typing import Any


def _segment_intersects_box(
    p1: tuple[float, float],
    p2: tuple[float, float],
    box: tuple[float, float, float, float],
) -> bool:
    """Check if line segment p1->p2 intersects the interior of axis-aligned box (min_x, min_y, max_x, max_y).

    Uses Liang-Barsky line clipping algorithm.
    """
    x1, y1 = p1
    x2, y2 = p2
    min_x, min_y, max_x, max_y = box

    # Quick rejection
    if max(x1, x2) <= min_x or min(x1, x2) >= max_x:
        return False
    if max(y1, y2) <= min_y or min(y1, y2) >= max_y:
        return False

    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - min_x, max_x - x1, y1 - min_y, max_y - y1]

    u1 = 0.0
    u2 = 1.0

    for i in range(4):
        pi = p[i]
        qi = q[i]
        if pi == 0:
            if qi < 0:
                return False
        else:
            t = qi / pi
            if pi < 0:
                if t > u2:
                    return False
                if t > u1:
                    u1 = t
            else:
                if t < u1:
                    return False
                if t < u2:
                    u2 = t
    return u1 < u2


def _get_logical_id(el: dict[str, Any]) -> str | None:
    custom_data = el.get("customData")
    if isinstance(custom_data, dict):
        agent_diagram = custom_data.get("agentDiagram")
        if isinstance(agent_diagram, dict):
            return agent_diagram.get("logicalId")
    return None


def _is_container_element(el: dict[str, Any]) -> bool:
    custom_data = el.get("customData")
    if isinstance(custom_data, dict):
        if custom_data.get("isContainer") or custom_data.get("swimlane"):
            return True
        agent_diagram = custom_data.get("agentDiagram")
        if isinstance(agent_diagram, dict) and agent_diagram.get("role") in ("container", "lane"):
            return True
    return el.get("type") == "frame"

def _construction_unit(el: dict[str, Any]) -> str | None:
    custom = el.get("customData") or {}
    library = custom.get("agentLibrary")
    if isinstance(library, dict) and library.get("instanceId"):
        return "library:" + str(library["instanceId"])
    primitive = custom.get("agentPrimitive")
    if isinstance(primitive, dict) and primitive.get("instanceId"):
        return "primitive:" + str(primitive["instanceId"])
    return None


def _body_obstacles(active_elements: list[dict[str, Any]]) -> list[dict[str, Any]]:
    bodies = []
    for element in active_elements:
        role = (element.get("customData") or {}).get("agentDiagram", {}).get("role")
        primitive = (element.get("customData") or {}).get("agentPrimitive", {})
        if _is_container_element(element) or role == "message-port":
            continue
        if primitive.get("role") == "body" and primitive.get("compoundBounds"):
            bodies.append({**element, **primitive["compoundBounds"]})
        elif element.get("type") == "line" and element.get("polygon"):
            points = element.get("points") or []
            if points:
                xs = [element["x"] + point[0] for point in points]
                ys = [element["y"] + point[1] for point in points]
                bodies.append({**element, "x": min(xs), "y": min(ys), "width": max(xs) - min(xs), "height": max(ys) - min(ys)})
        elif element.get("type") in ("rectangle", "diamond", "ellipse", "embeddable", "image"):
            bodies.append(element)
    anchored_units = {_construction_unit(element) for element in bodies
                      if _construction_unit(element) is not None and (element.get("customData") or {}).get("agentDiagram", {}).get("role") == "library-anchor"}
    return [element for element in bodies if _construction_unit(element) not in anchored_units
            or (element.get("customData") or {}).get("agentDiagram", {}).get("role") == "library-anchor"]


def check_bindings(
    active_elements: list[dict[str, Any]],
    elements_by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []

    for el in active_elements:
        el_id = el.get("id", "")
        el_type = el.get("type", "")

        # Check arrow bindings
        if el_type == "arrow":
            start_binding = el.get("startBinding")
            if isinstance(start_binding, dict):
                target_id = start_binding.get("elementId")
                if not target_id or target_id not in elements_by_id:
                    issues.append({
                        "code": "DANGLING_START_BINDING",
                        "severity": "error",
                        "elementIds": [el_id],
                        "logicalId": _get_logical_id(el),
                        "message": f"Arrow {el_id} startBinding references missing element '{target_id}'",
                        "repairHint": "Reconnect arrow startBinding to a valid element ID or remove startBinding",
                    })
                else:
                    target = elements_by_id[target_id]
                    target_bounds = [
                        b.get("id") if isinstance(b, dict) else b
                        for b in (target.get("boundElements") or [])
                    ]
                    if el_id not in target_bounds:
                        issues.append({
                            "code": "ASYMMETRIC_START_BINDING",
                            "severity": "warning",
                            "elementIds": [el_id, target_id],
                            "logicalId": _get_logical_id(el),
                            "message": f"Target {target_id} boundElements does not include arrow {el_id}",
                            "repairHint": f"Add {el_id} to {target_id} boundElements",
                        })

            end_binding = el.get("endBinding")
            if isinstance(end_binding, dict):
                target_id = end_binding.get("elementId")
                if not target_id or target_id not in elements_by_id:
                    issues.append({
                        "code": "DANGLING_END_BINDING",
                        "severity": "error",
                        "elementIds": [el_id],
                        "logicalId": _get_logical_id(el),
                        "message": f"Arrow {el_id} endBinding references missing element '{target_id}'",
                        "repairHint": "Reconnect arrow endBinding to a valid element ID or remove endBinding",
                    })
                else:
                    target = elements_by_id[target_id]
                    target_bounds = [
                        b.get("id") if isinstance(b, dict) else b
                        for b in (target.get("boundElements") or [])
                    ]
                    if el_id not in target_bounds:
                        issues.append({
                            "code": "ASYMMETRIC_END_BINDING",
                            "severity": "warning",
                            "elementIds": [el_id, target_id],
                            "logicalId": _get_logical_id(el),
                            "message": f"Target {target_id} boundElements does not include arrow {el_id}",
                            "repairHint": f"Add {el_id} to {target_id} boundElements",
                        })

        # Check bound text container references
        if el_type == "text":
            container_id = el.get("containerId")
            if container_id:
                if container_id not in elements_by_id:
                    issues.append({
                        "code": "DANGLING_CONTAINER_REF",
                        "severity": "error",
                        "elementIds": [el_id],
                        "logicalId": _get_logical_id(el),
                        "message": f"Text {el_id} containerId references missing element '{container_id}'",
                        "repairHint": "Remove containerId or assign a valid container ID",
                    })
                else:
                    container = elements_by_id[container_id]
                    c_bounds = [
                        b.get("id") if isinstance(b, dict) else b
                        for b in (container.get("boundElements") or [])
                    ]
                    if el_id not in c_bounds:
                        issues.append({
                            "code": "ASYMMETRIC_CONTAINER_BINDING",
                            "severity": "warning",
                            "elementIds": [el_id, container_id],
                            "logicalId": _get_logical_id(el),
                            "message": f"Container {container_id} boundElements does not include bound text {el_id}",
                            "repairHint": f"Add text {el_id} to container {container_id} boundElements",
                        })

    return issues


def check_text_containment(
    active_elements: list[dict[str, Any]],
    elements_by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []

    for el in active_elements:
        if el.get("type") != "text":
            continue
        container_id = el.get("containerId")
        if not container_id or container_id not in elements_by_id:
            continue

        container = elements_by_id[container_id]
        if container.get("type") in ("arrow", "line"):
            # Arrow-label placement is checked against nearby bodies, not its zero-height line bbox.
            continue
        cw = float(container.get("width", 0))
        ch = float(container.get("height", 0))
        tw = float(el.get("width", 0))
        th = float(el.get("height", 0))
        shape_type = container.get("type", "rectangle")
        logical_id = _get_logical_id(el) or _get_logical_id(container)

        if shape_type == "diamond":
            # For a diamond with width W and height H, centered text (w, h)
            # must satisfy: (w / W) + (h / H) <= 1.0 (with 2% tolerance)
            fit_ratio = (tw / max(cw, 1.0)) + (th / max(ch, 1.0))
            if fit_ratio > 1.02:
                issues.append({
                    "code": "TEXT_OUTSIDE_CONTAINER",
                    "severity": "error",
                    "elementIds": [container["id"], el["id"]],
                    "logicalId": logical_id,
                    "message": (
                        f"Text ({tw:.1f}x{th:.1f}) exceeds diamond inscribed area "
                        f"({cw:.1f}x{ch:.1f}, fit ratio {fit_ratio:.2f} > 1.0)"
                    ),
                    "actual": {
                        "requiredWidth": tw,
                        "requiredHeight": th,
                        "containerWidth": cw,
                        "containerHeight": ch,
                        "fitRatio": round(fit_ratio, 3),
                    },
                    "repairHint": "Expand diamond dimensions or wrap text / reduce fontSize",
                })
        elif shape_type == "ellipse":
            fit_ratio_sq = (tw / max(cw, 1.0)) ** 2 + (th / max(ch, 1.0)) ** 2
            if fit_ratio_sq > 1.05:
                issues.append({
                    "code": "TEXT_OUTSIDE_CONTAINER",
                    "severity": "error",
                    "elementIds": [container["id"], el["id"]],
                    "logicalId": logical_id,
                    "message": (
                        f"Text ({tw:.1f}x{th:.1f}) exceeds ellipse inscribed area ({cw:.1f}x{ch:.1f})"
                    ),
                    "actual": {
                        "requiredWidth": tw,
                        "requiredHeight": th,
                        "containerWidth": cw,
                        "containerHeight": ch,
                        "fitRatioSq": round(fit_ratio_sq, 3),
                    },
                    "repairHint": "Expand ellipse dimensions or reduce fontSize",
                })
        else:
            # Rectangle or standard box (default 8px padding)
            padding = 8.0
            if tw > (cw - padding) or th > (ch - padding):
                issues.append({
                    "code": "TEXT_OUTSIDE_CONTAINER",
                    "severity": "error",
                    "elementIds": [container["id"], el["id"]],
                    "logicalId": logical_id,
                    "message": (
                        f"Text ({tw:.1f}x{th:.1f}) exceeds container content area ({cw:.1f}x{ch:.1f})"
                    ),
                    "actual": {
                        "requiredWidth": tw,
                        "requiredHeight": th,
                        "containerWidth": cw,
                        "containerHeight": ch,
                    },
                    "repairHint": "Expand container width/height or wrap text to smaller width",
                })

    return issues


def check_body_overlap(active_elements: list[dict[str, Any]]) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []

    # Filter body elements
    body_elements = _body_obstacles(active_elements)

    n = len(body_elements)
    for i in range(n):
        a = body_elements[i]
        ax = float(a.get("x", 0))
        ay = float(a.get("y", 0))
        aw = float(a.get("width", 0))
        ah = float(a.get("height", 0))
        a_id = a.get("id", "")

        for j in range(i + 1, n):
            b = body_elements[j]
            bx = float(b.get("x", 0))
            by = float(b.get("y", 0))
            bw = float(b.get("width", 0))
            bh = float(b.get("height", 0))
            b_id = b.get("id", "")
            if _construction_unit(a) is not None and _construction_unit(a) == _construction_unit(b):
                # Explicit library/cuboid construction, not arbitrary shared group membership.
                continue

            # Check if one legitimate contains the other via parent/group
            a_parent = (a.get("customData") or {}).get("parent") or a.get("parentId")
            b_parent = (b.get("customData") or {}).get("parent") or b.get("parentId")
            if a_parent == b_id or b_parent == a_id:
                continue

            # Overlap AABB
            ow = min(ax + aw, bx + bw) - max(ax, bx)
            oh = min(ay + ah, by + bh) - max(ay, by)

            if ow > 6.0 and oh > 6.0:
                area = ow * oh
                if area > 36.0:
                    issues.append({
                        "code": "BODY_OVERLAP",
                        "severity": "error",
                        "elementIds": [a_id, b_id],
                        "message": (
                            f"Unexpected body overlap between {a_id} ({a.get('type')}) and "
                            f"{b_id} ({b.get('type')}) with overlap area {area:.0f}px"
                        ),
                        "actual": {
                            "overlapWidth": round(ow, 1),
                            "overlapHeight": round(oh, 1),
                            "overlapArea": round(area, 1),
                        },
                        "repairHint": "Separate bodies with at least 30-40px spacing",
                    })

    return issues


def check_arrow_crossing(
    active_elements: list[dict[str, Any]],
    elements_by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []

    # Find arrows
    arrows = [el for el in active_elements if el.get("type") == "arrow"]
    # Candidate body obstacles
    obstacles = _body_obstacles(active_elements)

    for arrow in arrows:
        arrow_id = arrow.get("id", "")
        ax = float(arrow.get("x", 0))
        ay = float(arrow.get("y", 0))
        points = arrow.get("points") or [[0, 0], [arrow.get("width", 0), arrow.get("height", 0)]]

        if len(points) < 2:
            continue

        scene_pts = [(ax + float(p[0]), ay + float(p[1])) for p in points]
        segments = [(scene_pts[k], scene_pts[k + 1]) for k in range(len(scene_pts) - 1)]

        # Endpoints
        start_target = (arrow.get("startBinding") or {}).get("elementId")
        end_target = (arrow.get("endBinding") or {}).get("elementId")
        exempt_ids = {arrow_id}
        if start_target:
            exempt_ids.add(start_target)
        if end_target:
            exempt_ids.add(end_target)

        for obs in obstacles:
            obs_id = obs.get("id", "")
            if obs_id in exempt_ids:
                continue
            if _construction_unit(arrow) is not None and _construction_unit(arrow) == _construction_unit(obs):
                continue

            ox = float(obs.get("x", 0))
            oy = float(obs.get("y", 0))
            ow = float(obs.get("width", 0))
            oh = float(obs.get("height", 0))

            # Inset obstacle by 4px to avoid false triggers on adjacent touching borders
            box = (ox + 4.0, oy + 4.0, ox + ow - 4.0, oy + oh - 4.0)
            if box[2] <= box[0] or box[3] <= box[1]:
                continue

            crossed = False
            for p1, p2 in segments:
                if _segment_intersects_box(p1, p2, box):
                    crossed = True
                    break

            if crossed:
                issues.append({
                    "code": "ARROW_CROSSES_NODE",
                    "severity": "error",
                    "elementIds": [arrow_id, obs_id],
                    "message": f"Arrow {arrow_id} passes through unrelated node {obs_id} ({obs.get('type')})",
                    "repairHint": "Reroute arrow waypoints or adjust node placement to avoid collision",
                })

    return issues


def check_arrow_label_occlusion(
    active_elements: list[dict[str, Any]],
    elements_by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []

    # Find labels attached to arrows
    arrow_labels: list[dict[str, Any]] = []
    for el in active_elements:
        if el.get("type") == "text":
            cid = el.get("containerId")
            if cid and elements_by_id.get(cid, {}).get("type") == "arrow":
                arrow_labels.append(el)

    body_obstacles = [
        el for el in active_elements
        if el.get("type") in ("rectangle", "diamond", "ellipse")
        and not _is_container_element(el)
    ]

    for label in arrow_labels:
        lid = label.get("id", "")
        lx = float(label.get("x", 0))
        ly = float(label.get("y", 0))
        lw = float(label.get("width", 0))
        lh = float(label.get("height", 0))
        arrow_id = label.get("containerId", "")
        arrow = elements_by_id.get(arrow_id, {})

        exempt_ids = {
            arrow_id,
            lid,
            (arrow.get("startBinding") or {}).get("elementId"),
            (arrow.get("endBinding") or {}).get("elementId"),
        }

        for obs in body_obstacles:
            oid = obs.get("id", "")
            if oid in exempt_ids:
                continue

            ox = float(obs.get("x", 0))
            oy = float(obs.get("y", 0))
            ow = float(obs.get("width", 0))
            oh = float(obs.get("height", 0))

            inter_w = min(lx + lw, ox + ow) - max(lx, ox)
            inter_h = min(ly + lh, oy + oh) - max(ly, oy)

            if inter_w > 4.0 and inter_h > 4.0 and (inter_w * inter_h) > 20.0:
                issues.append({
                    "code": "ARROW_LABEL_OCCLUSION",
                    "severity": "warning",
                    "elementIds": [lid, oid],
                    "message": f"Arrow label {lid} occludes node {oid}",
                    "repairHint": "Reposition arrow label or expand gap between arrow and node",
                })

    return issues


def check_unsupported_geometry(active_elements: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unsupported: list[dict[str, Any]] = []

    for el in active_elements:
        el_id = el.get("id", "")
        angle = float(el.get("angle", 0))
        if abs(angle) > 1e-4:
            unsupported.append({
                "elementId": el_id,
                "type": "rotated_element",
                "angle": round(angle, 4),
                "reason": (
                    f"Element {el_id} is rotated ({angle:.2f} rad). "
                    "Rotated collision geometry cannot be certified by 2D AABB checker; "
                    "requires visual PNG verification."
                ),
            })

        if el.get("type") == "arrow":
            roundness = el.get("roundness")
            is_elbowed = bool(el.get("elbowed"))
            is_curve = isinstance(roundness, dict) and roundness.get("type") == 2
            points = el.get("points") or []
            if is_curve and not is_elbowed and len(points) > 2:
                unsupported.append({
                    "elementId": el_id,
                    "type": "curved_arrow",
                    "reason": f"Arrow {el_id} uses spline geometry; exact clearance needs visual verification.",
                })

    return unsupported


def check_semantic_assertions(
    active_elements: list[dict[str, Any]],
    elements_by_id: dict[str, dict[str, Any]],
    expected: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []

    # Map logical IDs to elements
    logical_map: dict[str, list[dict[str, Any]]] = {}
    for el in active_elements:
        lid = _get_logical_id(el)
        if lid:
            logical_map.setdefault(lid, []).append(el)

    for idx, assertion in enumerate(expected):
        atype = assertion.get("type")
        if atype == "node_exists":
            target_id = assertion.get("id")
            if target_id not in elements_by_id and target_id not in logical_map:
                issues.append({
                    "code": "SEMANTIC_ASSERTION_FAILED",
                    "severity": "error",
                    "elementIds": [target_id] if target_id else [],
                    "message": f"Expected node '{target_id}' does not exist in diagram",
                    "repairHint": f"Create node with ID or logicalId '{target_id}'",
                })

        elif atype in ("edge_exists", "edge_label"):
            from_id = assertion.get("from")
            to_id = assertion.get("to")
            found = False
            for el in active_elements:
                if el.get("type") == "arrow":
                    sb = (el.get("startBinding") or {}).get("elementId")
                    eb = (el.get("endBinding") or {}).get("elementId")
                    sb_logical = _get_logical_id(elements_by_id.get(sb, {})) if sb else None
                    eb_logical = _get_logical_id(elements_by_id.get(eb, {})) if eb else None
                    if (sb == from_id or sb_logical == from_id) and (eb == to_id or eb_logical == to_id):
                        if atype == "edge_exists":
                            found = True
                        else:
                            labels = [elements_by_id.get(bound["id"], {}) for bound in (el.get("boundElements") or []) if bound.get("type") == "text"]
                            found = any("".join(label.get("text", "").split()) == "".join(str(assertion.get("text", "")).split()) for label in labels)
                        if found:
                            break
            if not found:
                issues.append({
                    "code": "SEMANTIC_ASSERTION_FAILED",
                    "severity": "error",
                    "elementIds": [],
                    "message": f"Expected {atype} from '{from_id}' to '{to_id}' with label '{assertion.get('text', '')}' not found",
                    "repairHint": "Preserve the relationship and create or correct its native bound label",
                })

        elif atype == "label_equals":
            target_id = str(assertion.get("id") or "")
            label_targets = [elements_by_id[target_id]] if target_id in elements_by_id else logical_map.get(target_id, [])
            labels = []
            for target in label_targets:
                if target.get("type") == "text":
                    labels.append(target)
                else:
                    labels.extend(elements_by_id.get(bound["id"], {}) for bound in (target.get("boundElements") or []) if bound.get("type") == "text")
            intended = "".join(str(assertion.get("text", "")).split())
            if not any("".join(label.get("text", "").split()) == intended for label in labels):
                issues.append({"code": "LABEL_CONTENT_MISSING", "severity": "error",
                               "elementIds": [target.get("id") for target in label_targets],
                               "message": f"Label for {target_id} does not preserve required text",
                               "repairHint": "Restore the complete native label; wrapping is allowed, truncation is not"})

        elif atype == "align":
            alignment_targets = [str(value) for value in assertion.get("targets", [])]
            axis = assertion.get("axis", "y")
            tol = float(assertion.get("tolerance", 5.0))
            coords: list[float] = []
            for tid in alignment_targets:
                target_el = elements_by_id.get(tid)
                if not target_el and tid in logical_map:
                    target_el = logical_map[tid][0]
                if target_el:
                    if axis == "y":
                        coords.append(float(target_el.get("y", 0)) + float(target_el.get("height", 0)) / 2.0)
                    else:
                        coords.append(float(target_el.get("x", 0)) + float(target_el.get("width", 0)) / 2.0)

            if len(coords) >= 2:
                diff = max(coords) - min(coords)
                if diff > tol:
                    issues.append({
                        "code": "SEMANTIC_ASSERTION_FAILED",
                        "severity": "warning",
                        "elementIds": alignment_targets,
                        "message": (
                            f"Alignment on axis '{axis}' failed: delta {diff:.1f}px exceeds tolerance {tol:.1f}px"
                        ),
                        "repairHint": f"Align elements {alignment_targets} along center {axis}",
                    })
        else:
            issues.append({"code": "UNKNOWN_SEMANTIC_ASSERTION", "severity": "error", "elementIds": [],
                           "message": f"Unsupported assertion type at index {idx}: {atype}",
                           "repairHint": "Use node_exists, edge_exists, edge_label, label_equals, or align"})

    return issues


def run_geometry_diagnostics(
    elements: list[dict[str, Any]],
    expected: list[dict[str, Any]] | None = None,
    structural_validation: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Run comprehensive geometry diagnostics on the canvas scene."""
    elements_by_id = {
        el["id"]: el for el in elements
        if isinstance(el, dict) and el.get("id") and not el.get("isDeleted", False)
    }
    active_elements = list(elements_by_id.values())

    all_issues: list[dict[str, Any]] = []
    for severity, name in (("error", "errors"), ("warning", "warnings")):
        for issue in (structural_validation or {}).get(name, []):
            all_issues.append({
                **issue,
                "severity": severity,
                "elementIds": [value for value in (issue.get("elementId"), issue.get("relatedId")) if value],
                "source": "native_validation",
            })

    # 1. Bindings integrity
    all_issues.extend(check_bindings(active_elements, elements_by_id))

    # 2. Text containment
    all_issues.extend(check_text_containment(active_elements, elements_by_id))

    # 3. Body overlap
    all_issues.extend(check_body_overlap(active_elements))

    # 4. Arrow crossing
    all_issues.extend(check_arrow_crossing(active_elements, elements_by_id))

    # 5. Arrow label occlusion
    all_issues.extend(check_arrow_label_occlusion(active_elements, elements_by_id))

    # 6. Semantic assertions
    if expected:
        all_issues.extend(check_semantic_assertions(active_elements, elements_by_id, expected))

    # 7. Unsupported geometry (mark unknown)
    unsupported = check_unsupported_geometry(active_elements)

    error_count = sum(1 for iss in all_issues if iss.get("severity") == "error")
    warning_count = sum(1 for iss in all_issues if iss.get("severity") == "warning")

    # Determine status
    if error_count > 0:
        status = "fail"
    elif len(unsupported) > 0:
        # Mark unknown if there are unsupported checks; do not falsely declare passed
        status = "unknown"
    else:
        status = "pass"

    return {
        "valid": (status == "pass"),
        "status": status,
        "summary": {
            "totalElements": len(active_elements),
            "errors": error_count,
            "warnings": warning_count,
            "unsupportedCount": len(unsupported),
        },
        "issues": all_issues,
        "unsupportedChecks": unsupported,
        "structuralValidation": structural_validation or {},
    }
