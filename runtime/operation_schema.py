"""Native operation input contract. The host remains authoritative for features/resources."""
from __future__ import annotations

import json
from typing import Annotated, Any, Literal, Union

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, ValidationError, create_model

Number = Annotated[float, Field(allow_inf_nan=False)]
Positive = Annotated[float, Field(gt=0, allow_inf_nan=False)]
Nonnegative = Annotated[float, Field(ge=0, allow_inf_nan=False)]
Reference = Annotated[str, Field(min_length=1)]
Point = Annotated[list[Number], Field(min_length=2, max_length=2)]
Points = Annotated[list[Point], Field(min_length=2)]
Targets = Annotated[list[Reference], Field(min_length=1)]


class NativeModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False, populate_by_name=True)


class Roundness(NativeModel):
    type: Literal[1, 2, 3]
    value: Nonnegative | None = None
    roundType: Literal["arc", "bezier"] | None = None


class Style(NativeModel):
    strokeColor: str | None = None
    backgroundColor: str | None = None
    fillStyle: str | None = None
    strokeWidth: Nonnegative | None = None
    strokeStyle: str | None = None
    roughness: Nonnegative | None = None
    opacity: Annotated[Number, Field(ge=0, le=100)] | None = None
    angle: Number | None = None
    roundness: Roundness | None = None
    fontFamily: str | None = None
    fontSize: Positive | None = None
    textAlign: Literal["left", "center", "right"] | None = None
    verticalAlign: Literal["top", "middle", "bottom"] | None = None
    lineHeight: Positive | None = None
    labelPosition: Any = None
    edge: Any = None


class Patch(Style):
    x: Number | None = None
    y: Number | None = None
    width: Nonnegative | None = None
    height: Nonnegative | None = None
    points: Points | None = None
    polygon: bool | None = None
    elbowed: bool | None = None
    startArrowhead: str | None = None
    endArrowhead: str | None = None
    autoResize: bool | None = None
    locked: bool | None = None
    link: str | None = None
    customData: dict[str, Any] | None = None
    pressures: list[Number] | None = None
    simulatePressure: bool | None = None


class Label(NativeModel):
    text: str
    ref: Reference | None = None
    padding: Nonnegative | None = None
    autoResize: bool | None = None
    style: Style | None = None
    customData: dict[str, Any] | None = None


class Endpoint(NativeModel):
    anchor: Literal["left", "right", "top", "bottom", "center", "top-left", "top-right", "bottom-left", "bottom-right"] | None = None
    fixedPoint: Annotated[list[Annotated[Number, Field(ge=0, le=1)]], Field(min_length=2, max_length=2)] | None = None
    mode: Literal["inside", "orbit", "edge"] | None = None


class ViewBox(NativeModel):
    width: Positive
    height: Positive
    x: Number | None = None
    y: Number | None = None


# One source-backed field table, not a permissive fallback operation. Required
# geometry is explicit; optional fields are never injected into native payloads.
COMMON = {"ref": Reference, "id": Reference, "style": Style, "patch": Patch, "customData": dict[str, Any]}
XY = {"x": Number, "y": Number}
BOX = {**XY, "width": Positive, "height": Positive}
ARROW = {"startArrowhead": str, "endArrowhead": str, "arrowHeadSize": Positive}
LABEL = {"label": str | Label}


def _model(name: str, required: dict, optional: dict) -> type[NativeModel]:
    fields = {key: (annotation, ...) for key, annotation in required.items()}
    fields.update({key: (annotation | None, None) for key, annotation in optional.items() if key not in required})
    fields["op"] = (Literal[name], ...)
    return create_model("".join(part.title() for part in name.split("_")), __base__=NativeModel, **fields)


def _fields(names: str, **extra: Any) -> dict:
    return {**{name: COMMON[name] for name in names.split()}, **extra}


MODELS = [
    _model("create_shape", {"type": Literal["rectangle", "ellipse", "diamond"], **BOX}, _fields("ref id style patch customData", **LABEL)),
    _model("create_text", {**XY, "text": str}, _fields("ref id style customData", textAlign=str, verticalAlign=str, autoResize=bool, wrapAt=Positive, width=Positive, height=Positive)),
    _model("create_linear", {**XY, "points": Points}, _fields("ref id style patch customData", kind=Literal["line", "arrow"], polygon=bool, closed=bool, elbowed=bool, **ARROW)),
    _model("create_svg_path", {**BOX, "path": Reference, "viewBox": ViewBox}, _fields("ref id style customData", closed=bool)),
    _model("create_draw", {**XY, "points": Points}, _fields("ref id style patch customData", pressures=list[Number], simulatePressure=bool, metadata=dict[str, Any])),
    _model("create_frame", BOX, _fields("ref style customData", name=str)),
    _model("create_image", {**XY, "source": Reference}, _fields("ref customData", width=Positive, height=Positive, scale=bool, anchor=bool)),
    _model("create_latex", {**XY, "tex": Reference}, _fields("ref customData", scaleX=Number, scaleY=Number)),
    _model("create_table", {**XY, "rows": Annotated[int, Field(gt=0, le=500)], "cols": Annotated[int, Field(gt=0, le=500)], "cellWidth": Positive, "cellHeight": Positive}, _fields("ref style", groupRef=Reference, cells=list[list[str | Label | None]])),
    _model("create_embeddable", BOX, _fields("ref id patch customData", source=str, url=str, file=str, filePath=str, mdProps=dict[str, Any])),
    _model("connect", {"from": Reference, "to": Reference}, _fields("ref id style customData", start=Endpoint, end=Endpoint, waypoints=list[Point], elbowed=bool, **ARROW, **LABEL, labelRef=Reference)),
    _model("patch_element", {"target": Reference, "patch": Patch}, {"expectedVersion": int}),
    _model("patch_custom_data", {"target": Reference}, {"expectedVersion": int, "merge": dict[str, Any], "remove": list[str]}),
    _model("set_feature", {"feature": Reference, "targets": Targets}, {"config": dict[str, Any]}),
    _model("clear_feature", {"feature": Reference, "targets": Targets}, {}),
    _model("set_text_global_style", {"targets": Targets}, {"style": dict[str, Any], "bold": bool, "fontWeight": str | Number, "font_weight": str | Number, "color": str, "gradient": str | dict[str, Any]}),
    _model("set_text_partial_style", {"targets": Targets}, {"style": dict[str, Any], "ranges": list[Any], "boldRanges": list[Any], "colorRanges": list[Any]}),
    _model("set_arrow_style", {"targets": Targets}, {"strokeWidth": Positive, **ARROW, "edge": Any}),
    _model("translate", {"targets": Targets, "dx": Number, "dy": Number}, {"includeBoundText": bool}),
    _model("resize", {"target": Reference, "width": Positive, "height": Positive}, {"anchor": str, "includeBoundText": bool}),
    _model("rotate", {"degrees": Number}, {"targets": Targets, "groupId": Reference, "fromCenter": bool}),
    _model("scale_selection", {"factor": Positive}, {"targets": Targets, "groupId": Reference, "fromCenter": bool}),
    _model("set_text", {"target": Reference, "text": str}, {"style": Style}),
    _model("bind_text", {"container": Reference, "text": Reference}, {"padding": Nonnegative}),
    _model("unbind_text", {"text": Reference}, {}),
    _model("rebind_arrow", {"arrow": Reference}, {"startTarget": Reference, "endTarget": Reference, "start": Endpoint, "end": Endpoint, "preservePoints": bool}),
    _model("unbind_arrow", {"arrow": Reference}, {"end": Literal["start", "end", "both"]}),
    _model("delete", {"targets": Targets}, {"cascadeBoundText": bool}),
    _model("duplicate", {"target": Reference}, {"ref": Reference, "dx": Number, "dy": Number}),
    _model("group", {"targets": Targets}, {"ref": Reference}),
    _model("ungroup", {}, {"targets": Targets, "groupId": Reference}),
    _model("add_to_frame", {"frame": Reference, "targets": Targets}, {}),
    _model("remove_from_frame", {"targets": Targets}, {}),
    _model("center_in", {"target": Reference, "container": Reference}, {"axis": Literal["horizontal", "vertical", "both"], "includeBoundText": bool}),
    _model("align", {"targets": Targets, "alignment": Literal["left", "right", "top", "bottom", "center-horizontal", "center-vertical"]}, {"includeBoundText": bool}),
    _model("distribute", {"targets": Targets, "direction": Literal["horizontal", "vertical"]}, {"includeBoundText": bool}),
]
Operation = Annotated[Union[tuple(MODELS)], Field(discriminator="op")]
OPERATIONS = TypeAdapter(list[Operation])


def operation_examples() -> dict[str, dict]:
    return {
        "shape": {"op": "create_shape", "ref": "alu", "type": "rectangle", "x": 0, "y": 0, "width": 160, "height": 80},
        "text": {"op": "create_text", "ref": "label", "x": 20, "y": 20, "text": "ALU", "style": {"fontFamily": "EXACT_DISCOVERED_FAMILY", "fontSize": 20, "lineHeight": 1.2}},
        "bound_connection": {"op": "connect", "ref": "bus", "from": "@alu", "to": "@register", "start": {"anchor": "right"}, "end": {"anchor": "left"}, "elbowed": True},
        "orthogonal_wire": {"op": "create_linear", "ref": "wire", "kind": "line", "x": 160, "y": 40, "points": [[0, 0], [40, 0], [40, 80], [80, 80]]},
        "formula": {"op": "create_latex", "ref": "equation", "x": 0, "y": 180, "tex": r"y = W x"},
    }


def validate_operations(operations: list[dict | BaseModel]) -> list[dict]:
    try:
        values = OPERATIONS.validate_python(operations)
        result = [value.model_dump(exclude_unset=True, by_alias=True) for value in values]
        for index, item in enumerate(result):
            if item["op"] in ("rotate", "scale_selection", "ungroup") and not (item.get("targets") or item.get("groupId")):
                raise ValueError(f"operations[{index}] needs targets or groupId")
        # Arbitrary extension dictionaries still must contain finite JSON data.
        json.dumps(result, allow_nan=False)
        return result
    except (ValidationError, ValueError, TypeError) as error:
        raise ValueError(
            "INVALID_NATIVE_OPERATIONS (committed=false): " + str(error) +
            ". Use create_shape with type=rectangle/ellipse/diamond, create_linear or connect; "
            "fontSize/fontFamily/lineHeight belong in style (or label.style); bold belongs in "
            "set_text_global_style, not create_text.style.fontWeight. Read drawing_begin's examples/schema."
        ) from error
