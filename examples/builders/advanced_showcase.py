"""Reproducible advanced native showcases; real host APIs, no scene JSON renderer.

Run from a connected package checkout:
  uv run --frozen python examples/builders/advanced_showcase.py pipeline --font "EXACT_HOST_FAMILY" --brief-file ./drawing-brief.json --filename Unique-Pipeline --output ./output/pipeline.json

These are explicit authored examples, not a generic hardware compiler or RTL
simulator. A report/PNG is not visual approval; inspect then drawing_review.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "runtime"))
from drawing_client import DrawingClient
from diagram_layout import Metrics, _route, _segment_clear
from visual_diagnostics import _crosses

INK = "#17324d"
BLUE = "#2563eb"
TEAL = "#0f766e"
PURPLE = "#7c3aed"
AMBER = "#b45309"
MUTED = "#64748b"


class Scene:
    """Small example-authoring helper; operations still use the existing API."""
    def __init__(self, client, context, font, name):
        self.client, self.context, self.font, self.name = client, context, font, name
        self.metrics = Metrics(client, context["contextToken"], font)
        self.ops, self.nodes, self.nets, self.routes = [], {}, [], {}
        self.regions = []
        self.text_boxes, self.decorative = [], set()
        self.expected, self.details = [], {}

    def meta(self, key, role="body", unit=None):
        return {"agentDiagram": {"diagramId": self.name, "logicalId": key, "role": role},
                **({"agentPrimitive": {"instanceId": self.name + ":" + unit, "role": role}} if unit else {})}

    def text(self, key, text, x, y, size=24, color=INK, center=None, unit=None):
        ms = self.metrics.size(text, size, 1.2)
        if center is not None:
            x = center - ms["width"] / 2
        self.ops.append({"op": "create_text", "ref": key, "x": x, "y": y, "text": text,
                         "style": {"fontFamily": self.font, "fontSize": size, "lineHeight": 1.2, "strokeColor": color},
                         "customData": self.meta(key, "text", unit)})
        self.text_boxes.append((x, y, x + ms["width"], y + ms["height"]))
        return ms

    def rect(self, key, x, y, w, h, fill="#ffffff", stroke="#cbd5e1", radius=6, container=False, unit=None):
        self.ops.append({"op": "create_shape", "ref": key, "type": "rectangle", "x": x, "y": y,
                         "width": w, "height": h, "style": {"strokeColor": stroke, "backgroundColor": fill,
                         "strokeWidth": 1.5, "fillStyle": "solid", "roughness": 0,
                         "roundness": {"type": 3, "value": radius, "roundType": "arc"} if radius else None},
                         "customData": {**self.meta(key, "container" if container else "body", unit),
                                        **({"isContainer": True} if container else {})}})

    def region(self, key, title, x, y, w, h, color=BLUE, fill="#f8fafc", subtitle=None):
        self.rect(key, x, y, w, h, fill, "#d8e1ed", 10, True)
        self.regions.append((x, y, x+w, y+h))
        self.rect(key + ":stripe", x, y, 6, h, color, color, 0)
        self.decorative.add(key + ":stripe")
        self.text(key + ":title", title, x + 24, y + 20, 27, color)
        if subtitle:
            self.text(key + ":subtitle", subtitle, x + 24, y + 57, 17, MUTED)

    def header(self, title, subtitle, width, number):
        self.rect("masthead", 30, 25, width, 115, "#102b46", "#102b46", 10, True)
        self.text("title", title, 62, 42, 38, "#ffffff")
        self.text("subtitle", subtitle, 65, 96, 19, "#cbdbea")
        self.text("number", number, 0, 55, 38, "#4dd0b1", center=width - 35)

    def node(self, key, label, x, y, w=180, h=100, color=BLUE, fill="#ffffff", ports=None, kind="box", size=24):
        ports = ports or {}
        b = {"x": x, "y": y, "width": w, "height": h}
        self.nodes[key] = {**b, "ports": ports, "kind": kind}
        self.expected.append({"type": "node_exists", "id": key})
        if kind in ("mux", "alu"):
            self.rect(key, x, y, w, h, "transparent", "transparent", 0, True, key)
            norm = ([[0, 0], [1, .16], [1, .84], [0, 1], [0, 0]] if kind == "mux"
                    else [[0, 0], [1, .2], [1, .8], [0, 1], [0, .65], [.22, .5], [0, .35], [0, 0]])
            self.ops.append({"op": "create_linear", "ref": key + ":outline", "kind": "line", "x": x, "y": y,
                             "points": [[u*w, v*h] for u, v in norm], "polygon": True, "closed": True,
                             "style": {"strokeColor": color, "backgroundColor": fill, "fillStyle": "solid", "strokeWidth": 2,
                                       "roughness": 0, "roundness": None}, "customData": self.meta(key + ":outline", "body", key)})
        else:
            self.rect(key, x, y, w, h, fill, color, 2 if kind == "register" else 6, False, key)
        ms = self.metrics.size(label, size, 1.2)
        self.text(key + ":label", label, x, y + (h-ms["height"])/2, size, color, center=x+w/2+(w*.04 if kind=="alu" else 0), unit=key)
        for pname, spec in ports.items():
            side, ratio, caption = spec
            px = x + (0 if side == "left" else w if side == "right" else w*ratio)
            py = y + (0 if side == "top" else h if side == "bottom" else h*ratio)
            if caption:
                pm = self.metrics.size(caption, 14, 1.2)
                tx = px + 7 if side == "left" else px-pm["width"]-7 if side == "right" else px-pm["width"]/2
                inset = h * .12 + 5 if kind in ("mux", "alu") else 5
                ty = py-pm["height"]/2 if side in ("left", "right") else py+inset if side=="top" else py-pm["height"]-inset
                self.text(key+":port:"+pname, caption, tx, ty, 14, color, unit=key)
        return key

    def endpoint(self, endpoint):
        key, port = endpoint.split(".", 1)
        b = self.nodes[key]
        if port in b["ports"]:
            side, ratio, _ = b["ports"][port]
        else:
            side, ratio = port, .5
        fixed = {"left": [0,ratio], "right": [1,ratio], "top": [ratio,0], "bottom": [ratio,1]}[side]
        return key, side, fixed, (b["x"]+b["width"]*fixed[0], b["y"]+b["height"]*fixed[1])

    def edge(self, key, source, dest, kind="data", label="", via=None, color=None):
        self.nets.append({"id":key,"from":source,"to":dest,"kind":kind,"label":label,"via":via,"color":color})

    def wire(self):
        obstacles = [{k:b[k] for k in ("x","y","width","height")} for b in self.nodes.values()]
        # Standalone headings/captions outside bodies are genuine obstacles.
        for a,b,c,d in self.text_boxes:
            if not any(a>=n["x"] and b>=n["y"] and c<=n["x"]+n["width"] and d<=n["y"]+n["height"] for n in self.nodes.values()):
                obstacles.append({"x":a-5,"y":b-4,"width":c-a+10,"height":d-b+8})
        reserved = []
        def overlap(route, driver):
            total = 0
            for a,b in zip(route,route[1:]):
                axis = 0 if a[0] == b[0] else 1
                other = 1-axis
                for c,d,owner in reserved:
                    if driver == owner or c[axis] != d[axis] or abs(a[axis]-c[axis]) > 4:continue
                    total += max(0,min(max(a[other],b[other]),max(c[other],d[other]))-max(min(a[other],b[other]),min(c[other],d[other])))
            return total
        for net in self.nets:
            source,ss,sf,sp=self.endpoint(net["from"]);target,ts,tf,tp=self.endpoint(net["to"])
            try:
                route=[sp,*net["via"],tp] if net["via"] is not None else _route(sp,tp,ss,ts,obstacles,clearance=16)
            except ValueError as error:
                raise ValueError(f'{net["id"]}: {net["from"]} -> {net["to"]}: {error}') from error
            if any(abs(a[0]-b[0])>1e-6 and abs(a[1]-b[1])>1e-6 for a,b in zip(route,route[1:])):
                raise ValueError("Nonorthogonal authored net: "+net["id"])
            # Separate unrelated collinear tracks; perpendicular crossings use
            # the host's native gap renderer, not masks or fake bridge arcs.
            if net["via"] is None:
                route=[list(pt) for pt in route]
                source_box=self.nodes[source];target_box=self.nodes[target]
                clearance_boxes=[(b["x"]-3,b["y"]-3,b["x"]+b["width"]+3,b["y"]+b["height"]+3)
                                 for b in obstacles if b != {k:source_box[k] for k in ("x","y","width","height")}
                                 and b != {k:target_box[k] for k in ("x","y","width","height")}]
                clearance_boxes += [(b["x"],b["y"],b["x"]+b["width"],b["y"]+b["height"]) for b in (source_box,target_box)]
                for _ in range(3):
                    score=overlap(route,net["from"]);best=route
                    for i in range(1,len(route)-2):
                        axis=0 if route[i][0]==route[i+1][0] else 1
                        for offset in (10,-10,20,-20,30,-30,40,-40,60,-60):
                            candidate=[pt[:] for pt in route]
                            candidate[i][axis]+=offset;candidate[i+1][axis]+=offset
                            value=overlap(candidate,net["from"])
                            if value < score and all(_segment_clear(tuple(a),tuple(b),clearance_boxes) for a,b in zip(candidate,candidate[1:])):
                                best,score=candidate,value
                    if best is route:break
                    route=best
            reserved.extend((a,b,net["from"]) for a,b in zip(route,route[1:]))
            self.routes[net["id"]]=route
            color=net["color"] or {"data":BLUE,"control":AMBER,"feedback":PURPLE,"memory":TEAL}[net["kind"]]
            self.ops.append({"op":"connect","ref":net["id"],"from":"@"+source,"to":"@"+target,
                             "start":{"anchor":ss,"fixedPoint":sf,"mode":"inside"},"end":{"anchor":ts,"fixedPoint":tf,"mode":"inside"},
                             "waypoints":route[1:-1],"elbowed":False,"startArrowhead":None,"endArrowhead":"triangle",
                             "style":{"strokeColor":color,"strokeWidth":2 if net["kind"]=="control" else 2.6,"strokeStyle":"dashed" if net["kind"]=="control" else "solid","roughness":0,"roundness":None},
                             "customData":{**self.meta(net["id"],"edge"),"lineCrossings":"gap","lineJumpPriority":0}})
            self.expected.append({"type":"edge_exists","from":source,"to":target})
        # Signal annotations sit off the actual wire; they must clear all nets.
        segments=[(a,b) for route in self.routes.values() for a,b in zip(route,route[1:])]
        occupied=list(self.text_boxes)
        for net in self.nets:
            if not net["label"]:continue
            ms=self.metrics.size(net["label"],18,1.2);w,h=ms["width"],ms["height"]
            candidates=[]
            for a,b in zip(self.routes[net["id"]],self.routes[net["id"]][1:]):
                for fraction in (.5,.3,.7,.15,.85):
                    if a[1]==b[1] and abs(a[0]-b[0])>=w+12:
                        x=a[0]+(b[0]-a[0])*fraction-w/2
                        for offset in (8,28,52,82):
                            candidates.extend([(x,a[1]-h-offset),(x,a[1]+offset)])
                    elif a[0]==b[0] and abs(a[1]-b[1])>=h+20:
                        y=a[1]+(b[1]-a[1])*fraction-h/2
                        for offset in (9,30,55,85):
                            candidates.extend([(a[0]+offset,y),(a[0]-w-offset,y)])
            selected=None
            for x,y in candidates:
                box=(x-3,y-3,x+w+3,y+h+3)
                if any(min(box[2],r)>max(box[0],l) and min(box[3],d)>max(box[1],t) for l,t,r,d in occupied):continue
                if any(min(box[2],n["x"]+n["width"])>max(box[0],n["x"]) and min(box[3],n["y"]+n["height"])>max(box[1],n["y"]) for n in self.nodes.values()):continue
                if any(_crosses(a,b,box) for l,t,r,d in self.regions for a,b in [((l,t),(r,t)),((r,t),(r,d)),((r,d),(l,d)),((l,d),(l,t))]):continue
                if any(_crosses(a,b,box) for a,b in segments):continue
                selected=(x,y);occupied.append(box);break
            if selected is None:raise ValueError("No readable annotation placement: "+net["id"])
            self.text(net["id"]+":label",net["label"],*selected,18,net["color"] or MUTED)


def p(side, ratio=.5, label=""):
    return side,ratio,label


def pipeline(s):
    s.header("RV32I  /  FIVE-STAGE DATAPATH", "Single issue  •  EX branch resolution  •  Forwarding + load-use interlock  •  Editable native schematic", 2920, "01")
    columns=[("if","IF  /  FETCH",50,430),("id","ID  /  DECODE",620,430),("ex","EX  /  EXECUTE",1220,630),("mem","MEM  /  ACCESS",2020,300),("wb","WB  /  COMMIT",2500,420)]
    for key,title,x,w in columns:s.region("stage:"+key,title,x,180,w,980,BLUE if key in ("if","ex") else TEAL)
    # Narrow pipeline latches, not stage bullet cards. Named ports retain field roles.
    latch_ports={"pc":p("left",.15,"pc"),"pcq":p("right",.15,"pc"),"inst":p("left",.38,"inst"),"instq":p("right",.38,"inst"),"d1":p("left",.55,"A"),"q1":p("right",.55,"A"),"d2":p("left",.72,"B"),"q2":p("right",.72,"B"),"rd":p("left",.88,"rd"),"rdq":p("right",.88,"rd"),"imm":p("left",.81,"imm"),"immq":p("right",.81,"imm"),"ctl_d":p("bottom",.2,"D"),"ctl":p("bottom",.8,"Q"),"we":p("top",.2),"flush":p("top",.8)}
    fields={"ifid":{"pc","pcq","inst","instq","we","flush"},
            "idex":{"pc","pcq","inst","instq","d1","q1","d2","q2","rd","rdq","imm","immq","ctl_d","ctl","flush"},
            "exmem":{"d1","q1","d2","q2","rd","rdq","ctl_d","ctl"},
            "memwb":{"d1","q1","d2","q2","rd","rdq","ctl_d","ctl"}}
    for key,label,x in [("ifid","IF/ID",515),("idex","ID/EX",1090),("exmem","EX/MEM",1890),("memwb","MEM/WB",2370)]:
        ports={name:(side,ratio,("alu" if name in ("d1","q1") else "store" if key=="exmem" else "load") if key in ("exmem","memwb") and name in ("d1","q1","d2","q2") else caption)
               for name,(side,ratio,caption) in latch_ports.items() if name in fields[key]}
        s.node(key,label,x,350,90,760,TEAL,"#e9f7f3",ports,kind="register",size=16)
    s.node("pc","PC",95,570,130,180,BLUE,"#eff6ff",{"d":p("left"),"q":p("right"),"we":p("top",.5,"we")},"register",28)
    s.node("npc","NEXT",90,345,100,140,BLUE,"#ffffff",{"seq":p("left",.25,"0"),"br":p("left",.75,"1"),"out":p("bottom"),"sel":p("top",.5,"sel")},"mux",20)
    s.node("pc4","PC + 4",285,340,145,105,BLUE,"#eff6ff",{"in":p("left"),"out":p("right")},"alu",20)
    s.node("imem","I-MEM",280,585,150,180,TEAL,"#f0fdfa",{"addr":p("left",.3,"addr"),"data":p("right",.5,"inst")},"box",24)
    s.node("rf","REGISTER\nFILE",680,540,270,260,TEAL,"#ffffff",{"raddr":p("top",.5,"rs1/rs2"),"r1":p("right",.3,"rd1"),"r2":p("right",.72,"rd2"),"wd":p("bottom",.65,"wdata"),"wa":p("bottom",.3,"rd"),"we":p("left",.85,"we")},"register",28)
    s.node("decode","DECODE",675,315,250,95,AMBER,"#fff7ed",{"inst":p("left"),"ctl":p("right"),"rd":p("bottom",.8,"rd")},size=24)
    s.node("imm","IMM GEN",750,925,180,90,TEAL,"#f0fdfa",{"inst":p("left"),"imm":p("right")},size=24)
    for key,label,y in [("fa","FWD A",520),("fb","FWD B",820)]:
        s.node(key,label,1260,y,110,170,BLUE,"#eff6ff",{"reg":p("left",.2,"00"),"wb":p("left",.5,"01"),"ex":p("left",.8,"10"),"out":p("right"),"sel":p("top",.5,"sel")},"mux",18)
    s.node("src","SRC",1490,790,105,155,BLUE,"#ffffff",{"reg":p("left",.25,"0"),"imm":p("left",.75,"1"),"out":p("right"),"sel":p("bottom",.5,"sel")},"mux",20)
    s.node("alu","ALU",1635,565,165,200,BLUE,"#dbeafe",{"a":p("left",.2,"A"),"b":p("left",.8,"B"),"y":p("right"),"ctl":p("top",.5,"op")},"alu",32)
    s.node("branch","BRANCH\nADD + CMP",1500,310,270,145,AMBER,"#fff7ed",{"pc":p("left",.2,"pc"),"imm":p("left",.8,"imm"),"a":p("bottom",.25,"A"),"b":p("bottom",.75,"B"),"target":p("top",.35,"target"),"taken":p("top",.8,"taken"),"ctl":p("right",.5,"br")},size=22)
    s.node("dmem","D-MEM",2070,615,200,255,TEAL,"#f0fdfa",{"addr":p("left",.2,"addr"),"wd":p("left",.72,"wdata"),"rd":p("right",.45,"rdata"),"ctl":p("top",.5,"rd/wr")},size=28)
    s.node("wbmux","WB",2550,565,110,200,BLUE,"#eff6ff",{"alu":p("left",.25,"0"),"mem":p("left",.75,"1"),"out":p("right"),"sel":p("top",.5,"sel")},"mux",24)
    s.node("retire","WB rd",2730,820,145,110,TEAL,"#f0fdfa",{"in":p("left"),"out":p("bottom")},size=22)
    s.node("hazard","INTERLOCK + FLUSH",560,1280,460,100,AMBER,"#fff7ed",{"ids":p("top",.2,"rs1/rs2"),"ex":p("top",.55,"rd"),"read":p("top",.85,"MemRead"),"taken":p("bottom",.5,"taken"),"stall":p("left",.3),"hold":p("left",.7),"flush_if":p("right",.3),"flush_ex":p("right",.7)},size=26)
    s.node("forward","FORWARDING UNIT",1280,1280,500,100,PURPLE,"#faf5ff",{"ex":p("right",.2,"EX rd"),"ex_ctl":p("right",.4,"we"),"wb":p("right",.65,"WB rd"),"wb_ctl":p("right",.9,"we"),"rs":p("left",.5,"rs1/rs2"),"a":p("top",.25,"FwdA"),"b":p("top",.75,"FwdB")},size=27)
    # Data paths, bundle crossings and distinct branch operands.
    for key,a,b in [("pc_imem","pc.q","imem.addr"),("pc_inc","pc.q","pc4.in"),("pc_seq","pc4.out","npc.seq"),("next_pc","npc.out","pc.d"),("inst_latch","imem.data","ifid.inst"),("pc_latch","pc.q","ifid.pc"),("decode_inst","ifid.instq","decode.inst"),("read_addr","ifid.instq","rf.raddr"),("imm_inst","ifid.instq","imm.inst"),("id_pc","ifid.pcq","idex.pc"),("read_a","rf.r1","idex.d1"),("read_b","rf.r2","idex.d2"),("id_rd","decode.rd","idex.rd"),("fwd_a_reg","idex.q1","fa.reg"),("fwd_b_reg","idex.q2","fb.reg"),("alu_a","fa.out","alu.a"),("src_reg","fb.out","src.reg"),("alu_b","src.out","alu.b"),("result_pipe","alu.y","exmem.d1"),("store_pipe","fb.out","exmem.d2"),("rd_ex_pipe","idex.rdq","exmem.rd"),("mem_addr","exmem.q1","dmem.addr"),("store_wdata","exmem.q2","dmem.wd"),("load_pipe","dmem.rd","memwb.d2"),("alu_pipe","exmem.q1","memwb.d1"),("rd_mem_pipe","exmem.rdq","memwb.rd"),("wb_alu","memwb.q1","wbmux.alu"),("wb_mem","memwb.q2","wbmux.mem"),("retire_rd","memwb.rdq","retire.in"),("branch_pc","idex.pcq","branch.pc"),("branch_a","fa.out","branch.a"),("branch_b","fb.out","branch.b")]:s.edge(key,a,b)
    s.edge("imm_latch","imm.imm","idex.imm")
    s.edge("fields_latch","ifid.instq","idex.inst")
    s.edge("imm_src","idex.immq","src.imm",label="immediate",via=[(1198,965.6),(1198,1190),(1470,1190),(1470,906.25)])
    s.edge("imm_branch","idex.immq","branch.imm",label="sign-extended")
    # WB data is genuine writeback. EX/MEM forwarding is not load rdata.
    for dest in ["rf.wd","fa.wb","fb.wb"]:s.edge("writeback:"+dest,"wbmux.out",dest,"feedback")
    s.text("wbdata_caption","WB data",2705,1080,18,PURPLE)
    for dest in ["fa.ex","fb.ex"]:
        s.edge("ex_bypass:"+dest,"exmem.q1",dest,"feedback",
               via=[(1996,768),(1996,344),(1796,344),(1796,464),(1231,464),(1231,656)] if dest=="fa.ex" else None)
    s.edge("redirect","branch.target","npc.br","feedback",label="branch target")
    s.edge("pcsrc","branch.taken","npc.sel","control",label="PCSrc")
    controls=[
        ("decode_control","decode.ctl","idex.ctl_d"),("mem_control","idex.ctl","exmem.ctl_d"),
        ("wb_control","exmem.ctl","memwb.ctl_d"),("alu_control","idex.ctl","alu.ctl"),
        ("branch_control","idex.ctl","branch.ctl"),("src_select","idex.ctl","src.sel"),
        ("dmem_control","exmem.ctl","dmem.ctl"),("wb_select","memwb.ctl","wbmux.sel"),
        ("wb_we","memwb.ctl","rf.we"),("wb_wa","retire.out","rf.wa"),
        ("hazard_id","ifid.instq","hazard.ids"),("hazard_ex","idex.rdq","hazard.ex"),
        ("hazard_read","idex.ctl","hazard.read"),("hazard_taken","branch.taken","hazard.taken"),
        ("pc_write","hazard.stall","pc.we"),("ifid_hold","hazard.hold","ifid.we"),
        ("ifid_flush","hazard.flush_if","ifid.flush"),("idex_bubble","hazard.flush_ex","idex.flush"),
        ("forward_ex","exmem.rdq","forward.ex"),("forward_wb","memwb.rdq","forward.wb"),
        ("forward_ex_we","exmem.ctl","forward.ex_ctl"),("forward_wb_we","memwb.ctl","forward.wb_ctl"),
        ("forward_rs","idex.instq","forward.rs"),("fwd_sel_a","forward.a","fa.sel"),("fwd_sel_b","forward.b","fb.sel")]
    for key,a,b in controls:s.edge(key,a,b,"control")
    s.region("notes","HAZARD CONTRACT",50,1470,2870,300,AMBER,"#f8fafc")
    s.text("note1","00 = register   |   01 = MEM/WB result   |   10 = EX/MEM ALU result (not a pending load)",85,1540,25,INK)
    s.text("note2","Load-use holds PC + IF/ID and bubbles ID/EX. EX-taken branch redirects PC and flushes IF/ID + ID/EX through the interlock.",85,1590,23,INK)
    s.text("note3","Teaching subset: ALU / load / store / BEQ; static not-taken, separate I/D memories. No JAL, CSR, traps or MUL/DIV implementation.",85,1640,21,MUTED)
    s.text("legend","BLUE  data        PURPLE  bypass / writeback        AMBER DASH  control        TEAL  registered state / memory",85,1690,23,TEAL)
    s.details={"execute":[1220,270,700,900],"decode":[620,250,560,910],"memory":[1890,300,1030,850]}


def inference(s):
    s.header("INFERENCE FABRIC  /  REQUEST TO TOKEN", "Disaggregated prefill / decode  •  Paged KV ownership  •  Cancellation and backpressure are explicit",2500,"02")
    s.region("edge","01  /  EDGE + ADMISSION",50,190,460,1120,BLUE,"#eff6ff","Identity, policy and bounded queues")
    s.region("scheduler","02  /  SCHEDULING CONTROL",560,190,770,330,PURPLE,"#faf5ff","Placement is separate from token execution")
    s.region("prefill","03  /  PREFILL POOL",560,580,770,730,BLUE,"#f6f9ff","Prompt compute produces transferable KV pages")
    s.region("decode","04  /  DECODE POOL",1380,190,730,1120,TEAL,"#f0fdfa","Owner-local paged KV and continuous batches")
    s.region("delivery","05  /  DELIVERY",2160,190,390,1120,AMBER,"#fffbeb","Ordering, cancellation and stream lifetime")
    specs=[("clients","CLIENTS",95,335,350,100,BLUE), ("gateway","API GATEWAY",95,550,350,110,BLUE),("admission","ADMISSION\nquota / deadline",95,790,350,120,BLUE),("queue","BOUNDED QUEUE",95,1090,350,100,BLUE),
           ("router","PLACEMENT",610,320,230,105,PURPLE),("directory","KV DIRECTORY",880,320,220,105,PURPLE),("registry","MODEL\nREGISTRY",1150,300,160,140,PURPLE),
           ("tokenizer","TOKENIZE +\nPREFIX LOOKUP",610,735,255,130,BLUE),("batch","PREFILL\nMICROBATCH",1010,735,260,130,BLUE),("prefillgpu","PREFILL GPU\nTP GROUP",610,1020,255,155,BLUE),("transfer","KV TRANSFER\nRDMA / HOST",1010,1020,260,155,TEAL),
           ("allocator","PAGE ALLOCATOR",1430,335,270,100,TEAL),("kv","PAGED KV\nGPU LOCAL",1770,335,270,170,TEAL),("decodebatch","CONTINUOUS\nBATCHER",1430,650,270,130,TEAL),("decodegpu","DECODE GPU\nTP GROUP",1770,650,270,170,TEAL),("sampler","LOGITS +\nSAMPLING",1770,990,270,130,TEAL),("reclaim","CANCEL / RECLAIM",1430,1130,270,100,PURPLE),
           ("sequencer","SEQUENCE\n+ DETOKENIZE",2205,540,290,150,AMBER),("stream","SSE STREAM",2205,850,290,110,AMBER),("return","CLIENT TOKENS",2205,1130,290,100,AMBER)]
    ports={"prefillgpu":{"launch":p("left",.3),"model":p("top",.6)},
           "registry":{"prefill":p("bottom",.15),"weights":p("bottom",.5),"rollout":p("bottom",.85)},
           "kv":{"install":p("bottom",.25),"read":p("bottom",.75)},
           "allocator":{"lookup":p("top",.3),"publish":p("top",.7)},
           "decodegpu":{"model":p("top",.7),"kv":p("top",.3)}}
    for key,label,x,y,w,h,c in specs:s.node(key,label,x,y,w,h,c,"#ffffff",ports=ports.get(key),size=25)
    edges=[("edge_request","clients.bottom","gateway.top"),("policy","gateway.bottom","admission.top"),
           ("queue_work","admission.bottom","queue.top"),("place","queue.right","router.left"),
           ("prefix","router.bottom","tokenizer.top"),("microbatch","tokenizer.right","batch.left"),
           ("prefill_launch","batch.bottom","prefillgpu.launch"),("kv_produced","prefillgpu.right","transfer.left"),
           ("install_kv","transfer.right","kv.install"),("assign_pages","allocator.right","kv.left"),
           ("continuous","decodebatch.right","decodegpu.left"),("read_kv","kv.read","decodegpu.kv"),
           ("logits","decodegpu.bottom","sampler.top"),("sampled","sampler.right","sequencer.left"),
           ("serialize","sequencer.bottom","stream.top"),("deliver","stream.bottom","return.top")]
    for key,a,b in edges:
        s.edge(key,a,b,"memory" if key in ["kv_produced","install_kv","assign_pages","read_kv"] else "data",
               label={"install_kv":"KV pages","sampled":"token + sequence"}.get(key,""),
               via=[(2090,1055),(2090,900),(2140,900),(2140,615)] if key=="sampled" else None)
    controls=[("kv_location","directory.right","allocator.lookup"),("choose_decode","router.right","directory.left"),
              ("load_model_p","registry.prefill","prefillgpu.model"),("load_model_d","registry.right","decodegpu.model"),
              ("owner_update","allocator.publish","directory.bottom"),("next_step","sampler.left","decodebatch.bottom"),
              ("end_or_cancel","stream.left","reclaim.right"),("free_pages","reclaim.top","allocator.bottom"),
              ("capacity","decodebatch.left","admission.right")]
    for key,a,b in controls:s.edge(key,a,b,"feedback" if key in ["next_step","owner_update"] else "control",
                                 label="next token" if key=="next_step" else "backpressure" if key=="capacity" else "")
    s.edge("resume_decode","transfer.right","decodebatch.top","control",label="KV ready")
    s.region("ops","OPERATIONS PLANE  /  METRICS + ROLLOUT",50,1380,2500,360,TEAL,"#f8fafc")
    for key,label,x,c in [("metrics","METRICS / TRACES",100,TEAL),("slo","SLO + ALERTS",650,AMBER),("rollout","CANARY / ROLLBACK",1200,PURPLE),("weights","WEIGHTS + ARTIFACTS",1850,BLUE)]:s.node(key,label,x,1500,390 if key!="weights" else 610,110,c,"#ffffff",size=24)
    for key,a,b in [("traces","gateway.bottom","metrics.top"),("gpu_metrics","decodegpu.bottom","metrics.top"),("evaluate","metrics.right","slo.left"),("rollback_policy","slo.right","rollout.left"),("versioned_weights","weights.top","registry.weights")]:s.edge(key,a,b,"control")
    s.edge("activate_version","rollout.top","registry.rollout","control")
    s.text("scope","Reference architecture, not deployment measurements. Network/KV failure handling, allocator consistency and model compatibility remain implementation responsibilities.",85,1670,19,MUTED)
    s.details={"decode":[1380,190,730,1120],"prefill":[560,580,770,730]}


def accelerator(s):
    s.header("TILED MATRIX ENGINE  /  DATA REUSE AT EVERY LEVEL", "Output-stationary 4 × 4 PE tile  •  Double-buffered operands  •  Explicit east / south forwarding",2420,"03")
    s.region("external","01  /  MEMORY + COMMAND",50,190,460,1340,BLUE,"#eff6ff","DMA movement and tile ownership")
    s.region("buffers","02  /  ON-CHIP STAGING",570,190,430,1340,TEAL,"#f0fdfa","Ping-pong buffers overlap load + compute")
    s.region("tile","03  /  OUTPUT-STATIONARY ARRAY",1060,330,1000,1000,PURPLE,"#faf5ff","A travels east; B travels south; C stays local")
    s.region("out","04  /  EPILOGUE",2120,190,350,1340,AMBER,"#fffbeb","Quantize / activation / writeback")
    s.node("hbm","EXTERNAL\nMEMORY",105,360,340,180,BLUE,"#ffffff",size=29)
    s.node("dma","DMA\nDESCRIPTORS",105,750,340,150,BLUE,"#ffffff",size=27)
    s.node("command","TILE SCHEDULER\nM / N / K",105,1120,340,150,AMBER,"#fff7ed",size=27)
    for name,label,y in [("abuf","A TILE  /  4 × K",350),("bbuf","B TILE  /  K × 4",730),("cbuf","C TILE  /  4 × 4",1140)]:
        s.node(name,label,620,y,330,125,TEAL,"#ffffff",size=24)
        for i in range(2):
            s.rect(name+":bank:"+str(i),635+i*150,y+145,135,62,"#ccfbf1" if i==0 else "#f0fdfa",TEAL,0)
            s.text(name+":banktext:"+str(i),"BANK "+str(i),647+i*150,y+160,19,TEAL)
    # Four independent B injectors and A row injectors; no implicit all-to-all bus.
    for i in range(4):
        s.node("ain"+str(i),"A"+str(i),1090,599.5+i*180,70,70,TEAL,"#ccfbf1",size=22)
        s.node("bin"+str(i),"B"+str(i),1234.75+i*190,455,70,70,BLUE,"#dbeafe",size=22)
    for r in range(4):
        for c in range(4):
            key=f"pe{r}{c}";x=1190+c*190;y=600+r*180
            s.node(key,f"PE {r},{c}",x,y,145,115,PURPLE,"#ffffff",{"a":p("left",.3,"A"),"ae":p("right",.3,"A"),"b":p("top",.55,"B"),"bs":p("bottom",.55,"B"),"ci":p("top",.85,"C"),"co":p("bottom",.85,"C")},size=21)
            s.text(key+":mac","C += A × B",x+14,y+76,15,MUTED,unit=key)
    s.node("collect","ACCUMULATOR DRAIN",1165,1390,810,100,PURPLE,"#ede9fe",ports={f"c{i}":p("top",(i+.5)/4) for i in range(4)},size=27)
    s.node("epilogue","BIAS +\nACTIVATION",2165,510,260,150,AMBER,"#ffffff",size=26)
    s.node("quant","REQUANTIZE",2165,850,260,110,AMBER,"#ffffff",size=24)
    s.node("write","WRITEBACK",2165,1190,260,110,TEAL,"#f0fdfa",size=24)
    for key,a,b,kind in [("mem_dma","hbm.bottom","dma.top","data"),("load_a","dma.right","abuf.left","memory"),("load_b","dma.right","bbuf.left","memory"),("tile_order","command.right","abuf.top","control"),("compute_go","command.right","collect.left","control"),("drain","collect.right","epilogue.left","memory"),("activate","epilogue.bottom","quant.top","data"),("quantize","quant.bottom","write.top","data"),("c_scratch","write.left","cbuf.right","memory"),("store_c","cbuf.left","hbm.left","feedback")]:s.edge(key,a,b,kind)
    for i in range(4):
        s.edge("a_feed"+str(i),"abuf.right","ain"+str(i)+".left","memory")
        s.edge("a_inject"+str(i),"ain"+str(i)+".right",f"pe{i}0.a","memory",via=[])
        s.edge("b_feed"+str(i),"bbuf.right","bin"+str(i)+".top","data")
        s.edge("b_inject"+str(i),"bin"+str(i)+".bottom",f"pe0{i}.b","data")
    for r in range(4):
        for c in range(4):
            if c<3:s.edge(f"a_east{r}{c}",f"pe{r}{c}.ae",f"pe{r}{c+1}.a","memory")
            if r<3:s.edge(f"b_south{r}{c}",f"pe{r}{c}.bs",f"pe{r+1}{c}.b","data")
            if r<3:s.edge(f"c_shift{r}{c}",f"pe{r}{c}.co",f"pe{r+1}{c}.ci","feedback")
    # A separate drain phase shifts every retained C through per-column C lanes.
    # It does not misuse B forwarding as a result port or claim a reduction.
    for c in range(4):s.edge("drain_col"+str(c),f"pe3{c}.co",f"collect.c{c}","feedback")
    s.region("math","COMPUTE CONTRACT  /  SYNTHETIC TEACHING TILE",50,1600,2420,330,PURPLE,"#f8fafc")
    s.text("equation","C[i,j] = sum_k A[i,k] × B[k,j]     |     16 MAC cells     |     2 × operand staging banks",90,1680,29,INK)
    s.text("reuse","Reuse: one A stream serves four columns; one B stream serves four rows. Array fill/drain and memory service determine utilization.",90,1740,23,TEAL)
    s.text("limit","Architectural illustration, not a chip performance claim. Per-column drain is schematic; timing, precision, arbitration and edge buffering are not simulated.",90,1795,19,MUTED)
    s.text("drain_phase","Purple C lanes are used only in the drain phase; each PE retains its own accumulator during the MAC phase.",90,1840,21,PURPLE)
    s.details={"array":[1060,330,1000,1000],"staging":[50,190,950,1340]}


SCENES = {"pipeline":pipeline,"inference":inference,"accelerator":accelerator}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scene",choices=SCENES)
    parser.add_argument("--font",required=True)
    parser.add_argument("--filename",required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--brief-file",type=Path,required=True,help="Resolved preferences and user requirements")
    args=parser.parse_args()
    if args.output.exists():raise ValueError("Use a new output report; existing receipts must not be overwritten by a blind rebuild")
    client=DrawingClient()
    context=client.context("create",filename=args.filename,foldername="Agent-Diagrams/Advanced-Showcase",brief=json.loads(args.brief_file.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps({**context,"stage":"created_before_planning"},ensure_ascii=False,indent=2),encoding="utf-8")
    capabilities=client.context("discover")["capabilities"]
    if args.font not in capabilities["fonts"]["registered"]:raise ValueError("Choose an exact discovered host font")
    scene=Scene(client,context,args.font,"advanced-"+args.scene)
    SCENES[args.scene](scene)
    scene.wire()
    operations=scene.ops
    receipts=[];refs={};revision=context["revision"]
    # API ref scope is per transaction. Resolve already-created references in
    # each subsequent batch; no raw full-scene JSON is authored.
    for start in range(0,len(operations),350):
        batch=json.loads(json.dumps(operations[start:start+350]))
        def resolve(value):
            if isinstance(value,str) and value.startswith("@") and value[1:] in refs:return refs[value[1:]]
            if isinstance(value,list):return [resolve(v) for v in value]
            if isinstance(value,dict):return {k:resolve(v) for k,v in value.items()}
            return value
        receipt=client.apply(context["contextToken"],revision,[resolve(op) for op in batch],acceptance_level="medium")
        receipts.append(receipt);refs.update(receipt.get("refs",{}));revision=receipt["revision"]
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps({"file":context["file"],"contextToken":context["contextToken"],"revision":revision,"receipts":receipts,"stage":"committed_partial","refs":refs},ensure_ascii=False,indent=2),encoding="utf-8")
    checked=client.check(context["contextToken"],expected=scene.expected)
    preview=client.preview(context["contextToken"],base_revision=checked["revision"],out_path=str(args.output.with_suffix(".png")))
    preview.pop("_base64",None)
    checked=client.check(context["contextToken"],preview_id=preview["previewId"])
    report={"method":"Authored Python + existing native API (not scene DSL)","file":context["file"],"contextToken":context["contextToken"],"revision":preview["revision"],"refs":refs,"receipts":receipts,"check":checked,"preview":preview,"visualReviewed":False,"nodes":len(scene.nodes),"declaredNets":len(scene.nets),"plannedRoutes":scene.routes,"detailRegions":scene.details,"expected":scene.expected,"operations":len(operations)}
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"file":report["file"],"nodes":len(scene.nodes),"nets":len(scene.nets),"operations":len(operations),"check":checked["status"],"complete":preview["complete"],"PNG":preview["out_path"]},ensure_ascii=False))
    return 0 if checked["status"]=="pass" and preview["complete"] else 2


if __name__=="__main__":
    raise SystemExit(main())
