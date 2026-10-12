"""Executable native diagram recipes. They are reference inputs, not fabricated output."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from diagram_layout import Metrics, plan_diagram
from drawing_styles import resolve_style, style_catalog

CIRCUIT_LIBRARY = "digital-circuit-components(svg)"
PRESENTATION_LIBRARY = "presentation-bundle"

RECIPES = {
    "flowchart": {
        "description": "中文流程与分支；程序测量和PNG局部修正。",
        "prompt": "画访问申请：提交→审核；通过发凭据，未通过拒绝说明，两路结束。中文全文、箭头标签保留。",
        "diagram": {"diagramId": "example-flowchart", "kind": "flowchart", "title": "访问申请流程",
                    "nodes": [{"id": "submit", "shape": "rectangle", "label": "提交访问申请", "variant": "primary"},
                              {"id": "review", "shape": "diamond", "label": "身份、权限和资源使用条件是否通过审核？"},
                              {"id": "grant", "shape": "rectangle", "label": "发放凭据", "variant": "success"},
                              {"id": "reject", "shape": "rectangle", "label": "拒绝并说明原因", "variant": "warning"},
                              {"id": "end", "shape": "ellipse", "label": "结束"}],
                    "edges": [{"id": "submit-review", "from": "submit", "to": "review"},
                              {"id": "yes", "from": "review", "to": "grant", "label": "通过", "fromPort": "left"},
                              {"id": "no", "from": "review", "to": "reject", "label": "未通过", "fromPort": "right"},
                              {"id": "grant-end", "from": "grant", "to": "end", "toPort": "left"},
                              {"id": "reject-end", "from": "reject", "to": "end", "toPort": "right"}]},
    },
    "architecture": {
        "description": "三层架构、原生容器和跨组连接。",
        "prompt": "画浏览器→网关→订单服务→数据库，分前端/后端/存储；后端服务一起移动，跨区连接不删除。",
        "diagram": {"diagramId": "example-architecture", "kind": "architecture", "title": "订单系统架构",
                    "nodes": [{"id": "browser", "label": "浏览器"}, {"id": "gateway", "label": "API 网关"},
                              {"id": "orders", "label": "订单服务"}, {"id": "database", "label": "数据库"}],
                    "edges": [{"id": "https", "from": "browser", "to": "gateway", "label": "HTTPS"},
                              {"id": "dispatch", "from": "gateway", "to": "orders"},
                              {"id": "read-write", "from": "orders", "to": "database", "label": "读写"}],
                    "containers": [{"id": "front", "label": "前端", "members": ["browser"]},
                                   {"id": "back", "label": "后端", "members": ["gateway", "orders"]},
                                   {"id": "store", "label": "存储", "members": ["database"]}],
                    "groups": [{"id": "services", "members": ["gateway", "orders"]}]},
    },
    "uml-class": {
        "description": "原生三分区类框、属性/方法分隔线、composition及multiplicity。",
        "prompt": "画订单UML类图：Customer关联Order；Order组合多个LineItem。显示类名、属性、方法和基数。",
        "diagram": {"diagramId": "example-uml", "kind": "uml", "title": "订单领域类图",
                    "nodes": [{"id": "customer", "label": "Customer", "attributes": ["+ id: UUID", "+ name: String"], "methods": ["+ placeOrder(): Order"]},
                              {"id": "order", "label": "Order", "attributes": ["+ id: UUID", "+ status: Status"], "methods": ["+ total(): Money"]},
                              {"id": "item", "label": "LineItem", "attributes": ["+ sku: String", "+ quantity: int"], "methods": ["+ subtotal(): Money"]}],
                    "edges": [{"id": "owns", "from": "customer", "to": "order", "label": "1 → 0..*", "endArrowhead": None},
                              {"id": "composition", "from": "order", "to": "item", "label": "1 → 1..*", "startArrowhead": "diamond", "endArrowhead": None}]},
    },
    "uml-sequence": {
        "description": "原生参与者、虚线生命线与分时消息，适用已说明顺序的交互。",
        "prompt": "画时序图：用户向API发请求，API查询数据库，数据库返回结果，API回应用户。",
        "sequence": {"title": "请求处理时序", "participants": [{"id": "user", "label": "用户"}, {"id": "api", "label": "API"}, {"id": "db", "label": "数据库"}],
                     "messages": [{"from": "user", "to": "api", "label": "提交请求"}, {"from": "api", "to": "db", "label": "查询"},
                                  {"from": "db", "to": "api", "label": "返回结果", "return": True}, {"from": "api", "to": "user", "label": "响应", "return": True}]},
    },
    "microarchitecture": {
        "description": "用户数字电路库的MUX/ALU/CROSSBAR，透明原生绑定载体与精确端口，不栅格化素材。",
        "prompt": "从指定digital-circuit-components(svg)库插入MUX、ALU、CROSSBAR画微架构数据通路；A/B输入经选择到ALU，结果送交叉开关。不得用近似矩形替代库符号。",
        "diagram": {"diagramId": "example-datapath", "kind": "microarchitecture", "title": "微架构数据通路", "style": "blueprint",
                    "nodes": [{"id": "operand-a", "label": "操作数 A"}, {"id": "operand-b", "label": "操作数 B"},
                              {"id": "mux", "label": "操作数选择", "library": {"source": CIRCUIT_LIBRARY, "item": "MUX", "scale": 2}},
                              {"id": "alu", "label": "算术逻辑单元", "library": {"source": CIRCUIT_LIBRARY, "item": "ALU", "scale": 2}},
                              {"id": "crossbar", "label": "结果路由", "library": {"source": CIRCUIT_LIBRARY, "item": "CROSSBAR", "scale": 2}}],
                    "edges": [{"id": "a-mux", "from": "operand-a", "to": "mux", "toFixedPoint": [0, 0.28]},
                              {"id": "b-mux", "from": "operand-b", "to": "mux", "toFixedPoint": [0, 0.72]},
                              {"id": "mux-alu", "from": "mux", "to": "alu", "label": "选定操作数"}, {"id": "alu-crossbar", "from": "alu", "to": "crossbar", "label": "结果"}]},
    },
    "circuit": {
        "description": "指定电路素材的组合电路示例；重复名称必须用itemId消歧。",
        "prompt": "使用指定库的NOT、OR和XOR画组合电路，保留原符号与输入输出方向；没有端口定义时明确采用的几何锚点。",
        "diagram": {"diagramId": "example-circuit", "kind": "circuit", "title": "组合电路", "style": "blueprint",
                    "nodes": [{"id": "input", "label": "输入 A / B"},
                              {"id": "not", "label": "反相", "library": {"source": CIRCUIT_LIBRARY, "item": "NOT", "scale": 2}},
                              {"id": "or", "label": "或", "library": {"source": CIRCUIT_LIBRARY, "item": "OR", "scale": 2}},
                              {"id": "xor", "label": "异或", "library": {"source": CIRCUIT_LIBRARY, "item": "XOR", "scale": 2}}],
                    "edges": [{"id": "a-not", "from": "input", "to": "not"}, {"id": "not-or", "from": "not", "to": "or"}, {"id": "or-xor", "from": "or", "to": "xor"}]},
    },
    "presentation": {
        "description": "从presentation-bundle原生frame模板创建多页，按页修改placeholder并单独导出PNG；不是PPTX导出。",
        "prompt": "用指定presentation-bundle创建三页演示：标题/问题、架构、结论。选同系列intro/slides，保留原生frame，按页检查PNG。",
        "presentation": {"library": PRESENTATION_LIBRARY,
                         "pages": [{"template": "Simplicity (intro)", "title": "绘图能力", "subtitle": "原生元素与视觉反馈"},
                                   {"template": "Simplicity (slides)", "title": "执行闭环", "body": ["描述并组织语义", "原生绘图与程序检查", "查看PNG并局部修正"]},
                                   {"template": "Simplicity (slides)", "title": "交付标准", "body": ["内容、关系完整", "图形原生可编辑", "当前PNG视觉复核通过"]}]},
    },
}


def template_catalog() -> dict[str, Any]:
    return {"templates": [{"name": name, "description": value["description"]} for name, value in RECIPES.items()], **style_catalog()}


def get_template(name: str, style: str | dict | None = None) -> dict[str, Any]:
    if name not in RECIPES:
        raise ValueError(f"Unknown template {name}; available: {', '.join(RECIPES)}")
    result = {"name": name, **deepcopy(RECIPES[name])}
    if style is not None and "diagram" in result:
        resolve_style(style)
        result["diagram"]["style"] = style
    return result


def plan_template(client: Any, context_token: str, name: str, data: dict | None = None, style: str | dict | None = None) -> dict:
    recipe = get_template(name, style)
    if name == "uml-sequence":
        return _plan_sequence(client, context_token, data or recipe["sequence"], style)
    if "diagram" not in recipe:
        raise ValueError("Presentation recipe executes native library imports via drawing_present, not a fictitious operation plan")
    diagram = data or recipe["diagram"]
    diagram = deepcopy(diagram)
    if style is not None:
        diagram["style"] = style
    if any(node.get("library") for node in diagram.get("nodes", [])):
        raise ValueError("Library recipes use drawing_compose, which reports each native insertion and its commit state")
    if name == "uml-class":
        return _plan_classes(client, context_token, diagram)
    return plan_diagram(client, context_token, diagram)


def _plan_classes(client: Any, token: str, diagram: dict) -> dict:
    profile = resolve_style(diagram.get("style", "visio"))
    metrics = Metrics(client, token, profile["fontFamily"])
    sections = {}
    measured_diagram = deepcopy(diagram)
    measured_diagram["style"] = diagram.get("style", "visio")
    measured_diagram["layout"] = {"direction": "LR", "rankGap": 160, **diagram.get("layout", {})}
    for edge in measured_diagram.get("edges", []):
        edge.setdefault("labelPosition", 0.5)
    for node in measured_diagram["nodes"]:
        parts = [str(node["label"]), "\n".join(node.get("attributes", [])), "\n".join(node.get("methods", []))]
        measured = [metrics.wrap(part, 300, profile["fontSize"]) for part in parts]
        sections[node["id"]] = measured
        node["size"] = {"minWidth": max(size["width"] for _, size in measured) + 40,
                        "minHeight": sum(size["height"] + 24 for _, size in measured)}
        node["label"] = ""
    plan = plan_diagram(client, token, measured_diagram)
    extra = []
    for node in diagram["nodes"]:
        name = node["id"]
        box = plan["layout"]["nodes"][name]
        y, section_refs = box["y"] + 12, []
        for index, (text, size) in enumerate(sections[name]):
            ref = f"node:{name}:section:{index}"
            section_refs.append("@" + ref)
            extra.append({"op": "create_text", "ref": ref, "x": box["x"] + (box["width"] - size["width"]) / 2 if index == 0 else box["x"] + 20,
                          "y": y, "text": text,
                          "style": {**profile["text"], "fontFamily": profile["fontFamily"], "fontSize": profile["fontSize"]},
                          "customData": {"agentDiagram": {"diagramId": plan["diagramId"], "logicalId": name, "role": "uml-section", "originalLabel": text}}})
            y += size["height"] + 24
            if index != 2:
                ref = f"node:{name}:divider:{index}"
                section_refs.append("@" + ref)
                extra.append({"op": "create_linear", "kind": "line", "ref": ref, "x": box["x"], "y": y - 12,
                              "points": [[0, 0], [box["width"], 0]], "style": profile["edge"]})
        extra.append({"op": "group", "targets": ["@node:" + name, *section_refs]})
    plan["operations"].extend(extra)
    plan["operationCount"] = len(plan["operations"])
    return plan


def _plan_sequence(client: Any, token: str, data: dict, style: str | dict | None) -> dict:
    profile = resolve_style(style or "visio")
    context = client.request("POST", "/v3/context", {"contextToken": token, "includeElements": False})
    participants = data.get("participants", [])
    ids = [part["id"] for part in participants]
    if len(ids) != len(set(ids)) or len(ids) < 2:
        raise ValueError("Sequence needs at least two uniquely identified participants")
    messages = data.get("messages", [])
    if any(message.get("from") not in ids or message.get("to") not in ids for message in messages):
        raise ValueError("Sequence message target is missing")
    metrics = Metrics(client, token, profile["fontFamily"])
    width = max(160, max(metrics.size(str(part["label"]), profile["fontSize"])["width"] + 32 for part in participants))
    centers = {name: index * (width + 140) + width / 2 for index, name in enumerate(ids)}
    total_height = 120 + len(messages) * 80
    ops = []
    for part in participants:
        name = part["id"]
        ops.extend([
            {"op": "create_shape", "type": "rectangle", "ref": "actor:" + name, "x": centers[name] - width / 2, "y": 0,
             "width": width, "height": 64, "style": profile["shape"], "label": {"text": str(part["label"]), "style": {**profile["text"], "fontFamily": profile["fontFamily"], "fontSize": profile["fontSize"]}}},
            {"op": "create_linear", "kind": "line", "ref": "lifeline:" + name, "x": centers[name], "y": 64,
             "points": [[0, 0], [0, total_height - 64]], "style": {**profile["edge"], "strokeStyle": "dashed"}},
        ])
    for index, message in enumerate(messages):
        y = 110 + index * 80
        endpoints = []
        for end in ("from", "to"):
            ref = f"message:{index}:{end}"
            endpoints.append("@" + ref)
            ops.append({"op": "create_shape", "type": "rectangle", "ref": ref, "x": centers[message[end]] - 1, "y": y - 1, "width": 2, "height": 2,
                        "style": {"strokeColor": "transparent", "backgroundColor": "transparent", "opacity": 100, "roughness": 0},
                        "customData": {"agentDiagram": {"role": "message-port", "logicalId": ref}}})
        rightward = centers[message["to"]] > centers[message["from"]]
        ops.append({"op": "connect", "ref": f"message:{index}", "from": endpoints[0], "to": endpoints[1],
                    "start": {"anchor": "right" if rightward else "left"}, "end": {"anchor": "left" if rightward else "right"},
                    "label": {"text": str(message.get("label", "")), "style": {**profile["text"], "fontFamily": profile["fontFamily"], "fontSize": 18, "labelPosition": 0.5}},
                    "style": {**profile["edge"], "strokeStyle": "dashed" if message.get("return") else "solid"}})
    title = str(data.get("title", "交互时序"))
    ops.append({"op": "create_text", "x": 0, "y": -64, "text": title,
                "style": {**profile["text"], "fontFamily": profile["fontFamily"], "fontSize": 28}})
    return {"baseRevision": context["revision"], "contextToken": token, "operations": ops, "operationCount": len(ops),
            "layout": {"participants": centers, "height": total_height, "styleProfile": profile["name"]},
            "notes": ["Native lifelines and message ports remain editable; verify labels and direction in PNG."]}
