---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'

# Excalidraw Data

## Text Elements
RV32I  /  FIVE-STAGE DATAPATH ^EkScu6lN

Single issue  •  EX branch resolution  •  Forwarding + load-use interlock  •  Editable native schematic ^tUdjTJwJ

01 ^doWF47qL

IF  /  FETCH ^SpU3rKN6

ID  /  DECODE ^OFLJfiIZ

EX  /  EXECUTE ^aVjomdrg

MEM  /  ACCESS ^HDvxtZCf

WB  /  COMMIT ^TuAvrJzZ

IF/ID ^ih21a9VN

pc ^r6tFBhpl

pc ^yvdyCrXi

inst ^ME7bqnSH

inst ^oRb2xgHo

ID/EX ^emFI4n1k

pc ^gGtarJ0g

pc ^kozXUTak

inst ^6ZVPSAj4

inst ^OAMk7SHw

A ^jLvGJ2oU

A ^r700J3p3

B ^CFKGBKZX

B ^pDuXNJ9p

rd ^TXTWa33N

rd ^ZiT3zNvz

imm ^tjksiiF4

imm ^AjtalJXP

Q ^A3nGo337

EX/MEM ^LigCEL6m

alu ^ZErDPdGn

alu ^iOsvxZfy

store ^WnaTSqOP

store ^FCz1YrdC

rd ^t9MM4sRf

rd ^vW7piXHX

Q ^7E8D0ICQ

MEM/WB ^nJrxZr8g

alu ^Yl6pjRTD

alu ^bStehDuv

load ^FRz2afV0

load ^rp9FVerd

rd ^PNWVUyGO

rd ^LNoT1RSu

Q ^6toCLcoL

PC ^mNBhaXPR

we ^hIuvqFY9

NEXT ^pK16q5iE

0 ^jObgqycu

1 ^n8wDjrln

sel ^s1fhkb0J

PC + 4 ^DArG5KH4

I-MEM ^9xAZYHce

addr ^mcEEbYBy

inst ^Jc8cgLCs

REGISTER
FILE ^SxzT4s74

rs1/rs2 ^IZtJnu6y

rd1 ^ub9FtUy9

rd2 ^CKMeeBit

wdata ^fIBYA888

rd ^XD53rY4q

we ^fRPbCdPw

DECODE ^dfXosQS5

rd ^Zz09IRcr

IMM GEN ^5pbIoHuH

FWD A ^M1yzc1j0

00 ^h9ff4Pq7

01 ^N2lAAwfw

10 ^S9T6G4C5

sel ^oB5V4s2t

FWD B ^xUXbaD6s

00 ^BjUnnpsM

01 ^GB0pSNBj

10 ^fGSqJcS4

sel ^7944P4nU

SRC ^iaQyp88p

0 ^gTkF3LZN

1 ^apgMtmUK

sel ^rbgNd5ty

ALU ^wYz28KIY

A ^VoQclu4x

B ^VCsvN31K

op ^oZLiv219

BRANCH
ADD + CMP ^u5cOYbiG

pc ^hYGDoWy2

imm ^pB5PwK3Y

A ^lfjeLQTe

B ^LMntLKet

target ^8ECvrykb

taken ^l8MdEGS4

br ^uBXWuVVo

D-MEM ^6f1RDuAc

addr ^5xqL8S3o

wdata ^onb5OmXm

rdata ^RxpPVpf3

rd/wr ^pkYEDe6V

WB ^f62B7KqF

0 ^hOHS1JUD

1 ^Ov0hTOiF

sel ^5wGbkE9g

WB rd ^JUPGT0ta

INTERLOCK + FLUSH ^moPlHbfT

rs1/rs2 ^8q8NIq3d

rd ^nj64QH7S

MemRead ^TbbI7rYt

taken ^iif3aHzO

FORWARDING UNIT ^HDkhPSmx

EX rd ^RQMG3bIn

we ^X8RAjPFR

WB rd ^aEvQ5ZAM

we ^aTCSxrjG

rs1/rs2 ^lbksDAVa

FwdA ^vlpxOMUV

FwdB ^kDi5IT0z

HAZARD CONTRACT ^GuBOfCuu

00 = register   |   01 = MEM/WB result   |   10 = EX/MEM ALU result (not a pending load) ^4aar1aug

Load-use holds PC + IF/ID and bubbles ID/EX. EX-taken branch redirects PC and flushes IF/ID + ID/EX through the interlock. ^p6MB01yj

Teaching subset: ALU / load / store / BEQ; static not-taken, separate I/D memories. No JAL, CSR, traps or MUL/DIV implementation. ^zDQrWUK0

BLUE  data        PURPLE  bypass / writeback        AMBER DASH  control        TEAL  registered state / memory ^XROn0H7m

immediate ^eE1SoAWh

sign-extended ^QqSZyu2c

branch target ^dQetZM4e

PCSrc ^VoVU9VcG

D ^xOKK76oE

D ^e6xFQgjX

D ^BQdz9PN5

WB data ^vZaoyjJW

%%
## Drawing
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.29.0-3",
  "elements": [
    {
      "id": "Sel2EFLk",
      "type": "rectangle",
      "x": 30,
      "y": 25,
      "width": 2920,
      "height": 115,
      "angle": 0,
      "strokeColor": "#102b46",
      "backgroundColor": "#102b46",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 10,
        "roundType": "arc"
      },
      "seed": 72808,
      "version": 2,
      "versionNonce": 942423654,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959703,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "masthead",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "a0"
    },
    {
      "text": "RV32I  /  FIVE-STAGE DATAPATH",
      "fontSize": 38,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "EkScu6lN",
      "type": "text",
      "x": 62,
      "y": 42,
      "width": 582.7841796875,
      "height": 45.6,
      "angle": 0,
      "strokeColor": "#ffffff",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 89714,
      "version": 2,
      "versionNonce": 1586086650,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959704,
      "containerId": null,
      "originalText": "RV32I  /  FIVE-STAGE DATAPATH",
      "rawText": "RV32I  /  FIVE-STAGE DATAPATH",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "title",
          "role": "text"
        }
      },
      "index": "a1"
    },
    {
      "text": "Single issue  •  EX branch resolution  •  Forwarding + load-use interlock  •  Editable native schematic",
      "fontSize": 19,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "tUdjTJwJ",
      "type": "text",
      "x": 65,
      "y": 96,
      "width": 843.1806640625,
      "height": 22.8,
      "angle": 0,
      "strokeColor": "#cbdbea",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 38928,
      "version": 2,
      "versionNonce": 2049147302,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959704,
      "containerId": null,
      "originalText": "Single issue  •  EX branch resolution  •  Forwarding + load-use interlock  •  Editable native schematic",
      "rawText": "Single issue  •  EX branch resolution  •  Forwarding + load-use interlock  •  Editable native schematic",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "subtitle",
          "role": "text"
        }
      },
      "index": "a2"
    },
    {
      "text": "01",
      "fontSize": 38,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "doWF47qL",
      "type": "text",
      "x": 2863.8662109375,
      "y": 55,
      "width": 42.267578125,
      "height": 45.6,
      "angle": 0,
      "strokeColor": "#4dd0b1",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 20168,
      "version": 2,
      "versionNonce": 1292587962,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959704,
      "containerId": null,
      "originalText": "01",
      "rawText": "01",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "number",
          "role": "text"
        }
      },
      "index": "a3"
    },
    {
      "id": "4yF34sgX",
      "type": "rectangle",
      "x": 50,
      "y": 180,
      "width": 430,
      "height": 980,
      "angle": 0,
      "strokeColor": "#d8e1ed",
      "backgroundColor": "#f8fafc",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 10,
        "roundType": "arc"
      },
      "seed": 31134,
      "version": 3,
      "versionNonce": 836811708,
      "updated": 1792161397465,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959704,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:if",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "a4"
    },
    {
      "id": "46SjcXnu",
      "type": "rectangle",
      "x": 50,
      "y": 180,
      "width": 6,
      "height": 980,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "#2563eb",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 9598,
      "version": 2,
      "versionNonce": 1050463354,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959704,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:if:stripe",
          "role": "body"
        }
      },
      "index": "a5"
    },
    {
      "text": "IF  /  FETCH",
      "fontSize": 27,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "SpU3rKN6",
      "type": "text",
      "x": 74,
      "y": 200,
      "width": 151.49267578125,
      "height": 32.4,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 49666,
      "version": 2,
      "versionNonce": 532664358,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959705,
      "containerId": null,
      "originalText": "IF  /  FETCH",
      "rawText": "IF  /  FETCH",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:if:title",
          "role": "text"
        }
      },
      "index": "a6"
    },
    {
      "id": "T7W94PRP",
      "type": "rectangle",
      "x": 620,
      "y": 180,
      "width": 430,
      "height": 980,
      "angle": 0,
      "strokeColor": "#d8e1ed",
      "backgroundColor": "#f8fafc",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 10,
        "roundType": "arc"
      },
      "seed": 70907,
      "version": 3,
      "versionNonce": 694410730,
      "updated": 1792161397465,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959705,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:id",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "a7"
    },
    {
      "id": "sb9p2mAl",
      "type": "rectangle",
      "x": 620,
      "y": 180,
      "width": 6,
      "height": 980,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#0f766e",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 90950,
      "version": 2,
      "versionNonce": 1423891302,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959705,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:id:stripe",
          "role": "body"
        }
      },
      "index": "a8"
    },
    {
      "text": "ID  /  DECODE",
      "fontSize": 27,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "OFLJfiIZ",
      "type": "text",
      "x": 644,
      "y": 200,
      "width": 180.02197265625,
      "height": 32.4,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 49321,
      "version": 2,
      "versionNonce": 295400954,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959705,
      "containerId": null,
      "originalText": "ID  /  DECODE",
      "rawText": "ID  /  DECODE",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:id:title",
          "role": "text"
        }
      },
      "index": "a9"
    },
    {
      "id": "EuEwVZ2j",
      "type": "rectangle",
      "x": 1220,
      "y": 180,
      "width": 630,
      "height": 980,
      "angle": 0,
      "strokeColor": "#d8e1ed",
      "backgroundColor": "#f8fafc",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 10,
        "roundType": "arc"
      },
      "seed": 17548,
      "version": 3,
      "versionNonce": 398388386,
      "updated": 1792161397465,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959705,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:ex",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "aA"
    },
    {
      "id": "r9IYyG2E",
      "type": "rectangle",
      "x": 1220,
      "y": 180,
      "width": 6,
      "height": 980,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "#2563eb",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 40697,
      "version": 2,
      "versionNonce": 963552954,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959705,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:ex:stripe",
          "role": "body"
        }
      },
      "index": "aB"
    },
    {
      "text": "EX  /  EXECUTE",
      "fontSize": 27,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "aVjomdrg",
      "type": "text",
      "x": 1244,
      "y": 200,
      "width": 201.0498046875,
      "height": 32.4,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 43502,
      "version": 2,
      "versionNonce": 1463794150,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959705,
      "containerId": null,
      "originalText": "EX  /  EXECUTE",
      "rawText": "EX  /  EXECUTE",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:ex:title",
          "role": "text"
        }
      },
      "index": "aC"
    },
    {
      "id": "z82ULHba",
      "type": "rectangle",
      "x": 2020,
      "y": 180,
      "width": 300,
      "height": 980,
      "angle": 0,
      "strokeColor": "#d8e1ed",
      "backgroundColor": "#f8fafc",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 10,
        "roundType": "arc"
      },
      "seed": 50500,
      "version": 3,
      "versionNonce": 428587523,
      "updated": 1792161397465,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959705,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:mem",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "aD"
    },
    {
      "id": "X8IFGqb0",
      "type": "rectangle",
      "x": 2020,
      "y": 180,
      "width": 6,
      "height": 980,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#0f766e",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 76764,
      "version": 2,
      "versionNonce": 1882950950,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959705,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:mem:stripe",
          "role": "body"
        }
      },
      "index": "aE"
    },
    {
      "text": "MEM  /  ACCESS",
      "fontSize": 27,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "HDvxtZCf",
      "type": "text",
      "x": 2044,
      "y": 200,
      "width": 211.53076171875,
      "height": 32.4,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 49038,
      "version": 2,
      "versionNonce": 1827389498,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959706,
      "containerId": null,
      "originalText": "MEM  /  ACCESS",
      "rawText": "MEM  /  ACCESS",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:mem:title",
          "role": "text"
        }
      },
      "index": "aF"
    },
    {
      "id": "4VO312R0",
      "type": "rectangle",
      "x": 2500,
      "y": 180,
      "width": 420,
      "height": 980,
      "angle": 0,
      "strokeColor": "#d8e1ed",
      "backgroundColor": "#f8fafc",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 10,
        "roundType": "arc"
      },
      "seed": 52206,
      "version": 3,
      "versionNonce": 194521930,
      "updated": 1792161397465,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959706,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:wb",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "aG"
    },
    {
      "id": "i6DMfv9b",
      "type": "rectangle",
      "x": 2500,
      "y": 180,
      "width": 6,
      "height": 980,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#0f766e",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 75552,
      "version": 2,
      "versionNonce": 1354475770,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959706,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:wb:stripe",
          "role": "body"
        }
      },
      "index": "aH"
    },
    {
      "text": "WB  /  COMMIT",
      "fontSize": 27,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "TuAvrJzZ",
      "type": "text",
      "x": 2524,
      "y": 200,
      "width": 190.4765625,
      "height": 32.4,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 15673,
      "version": 2,
      "versionNonce": 1760230310,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959706,
      "containerId": null,
      "originalText": "WB  /  COMMIT",
      "rawText": "WB  /  COMMIT",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "stage:wb:title",
          "role": "text"
        }
      },
      "index": "aI"
    },
    {
      "id": "uD9EwiAM",
      "type": "rectangle",
      "x": 515,
      "y": 350,
      "width": 90,
      "height": 760,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#e9f7f3",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 2,
        "roundType": "arc"
      },
      "seed": 90318,
      "version": 2,
      "versionNonce": 739277242,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "qNjLnpUH",
          "type": "arrow"
        },
        {
          "id": "Pydlp8xP",
          "type": "arrow"
        },
        {
          "id": "mqwzqZ19",
          "type": "arrow"
        },
        {
          "id": "G7JK65WS",
          "type": "arrow"
        },
        {
          "id": "iphC33F5",
          "type": "arrow"
        },
        {
          "id": "0xSLvgbH",
          "type": "arrow"
        },
        {
          "id": "9NitmObv",
          "type": "arrow"
        },
        {
          "id": "eNuL3zCW",
          "type": "arrow"
        },
        {
          "id": "UcachPP4",
          "type": "arrow"
        },
        {
          "id": "zmRE0G9O",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959706,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "ifid",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:ifid",
          "role": "body"
        }
      },
      "index": "aJ"
    },
    {
      "text": "IF/ID",
      "fontSize": 16,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "ih21a9VN",
      "type": "text",
      "x": 542.66796875,
      "y": 720,
      "width": 34.6640625,
      "height": 19.2,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 55540,
      "version": 2,
      "versionNonce": 915969766,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959706,
      "containerId": null,
      "originalText": "IF/ID",
      "rawText": "IF/ID",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "ifid:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:ifid",
          "role": "text"
        }
      },
      "index": "aK"
    },
    {
      "text": "pc",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "r6tFBhpl",
      "type": "text",
      "x": 522,
      "y": 455.25,
      "width": 14.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 27142,
      "version": 2,
      "versionNonce": 235745914,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959707,
      "containerId": null,
      "originalText": "pc",
      "rawText": "pc",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "ifid:port:pc",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:ifid",
          "role": "text"
        }
      },
      "index": "aL"
    },
    {
      "text": "pc",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "yvdyCrXi",
      "type": "text",
      "x": 583.2138671875,
      "y": 455.25,
      "width": 14.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 31545,
      "version": 2,
      "versionNonce": 175163942,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959708,
      "containerId": null,
      "originalText": "pc",
      "rawText": "pc",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "ifid:port:pcq",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:ifid",
          "role": "text"
        }
      },
      "index": "aM"
    },
    {
      "text": "inst",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "ME7bqnSH",
      "type": "text",
      "x": 522,
      "y": 630.05,
      "width": 21.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 36175,
      "version": 2,
      "versionNonce": 695522106,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959708,
      "containerId": null,
      "originalText": "inst",
      "rawText": "inst",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "ifid:port:inst",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:ifid",
          "role": "text"
        }
      },
      "index": "aN"
    },
    {
      "text": "inst",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "oRb2xgHo",
      "type": "text",
      "x": 576.2138671875,
      "y": 630.05,
      "width": 21.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 52957,
      "version": 2,
      "versionNonce": 1935709542,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959708,
      "containerId": null,
      "originalText": "inst",
      "rawText": "inst",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "ifid:port:instq",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:ifid",
          "role": "text"
        }
      },
      "index": "aO"
    },
    {
      "id": "azKpcPdN",
      "type": "rectangle",
      "x": 1090,
      "y": 350,
      "width": 90,
      "height": 760,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#e9f7f3",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 2,
        "roundType": "arc"
      },
      "seed": 56657,
      "version": 3,
      "versionNonce": 510940297,
      "updated": 1792161830562,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "0xSLvgbH",
          "type": "arrow"
        },
        {
          "id": "vmAC29Nz",
          "type": "arrow"
        },
        {
          "id": "gjdqm2qt",
          "type": "arrow"
        },
        {
          "id": "iths4XL8",
          "type": "arrow"
        },
        {
          "id": "ECQY9lyq",
          "type": "arrow"
        },
        {
          "id": "KdLmJLKR",
          "type": "arrow"
        },
        {
          "id": "ugL8Kp2y",
          "type": "arrow"
        },
        {
          "id": "v7CpLDq4",
          "type": "arrow"
        },
        {
          "id": "yqzKtVT8",
          "type": "arrow"
        },
        {
          "id": "9NitmObv",
          "type": "arrow"
        },
        {
          "id": "rap2QDOI",
          "type": "arrow"
        },
        {
          "id": "cPcmZtQE",
          "type": "arrow"
        },
        {
          "id": "5aWAjEla",
          "type": "arrow"
        },
        {
          "id": "twdDZZ4r",
          "type": "arrow"
        },
        {
          "id": "gIeyRcZt",
          "type": "arrow"
        },
        {
          "id": "1LV6TPTr",
          "type": "arrow"
        },
        {
          "id": "7PxQ9BeL",
          "type": "arrow"
        },
        {
          "id": "viHDu4dC",
          "type": "arrow"
        },
        {
          "id": "r4mihXKS",
          "type": "arrow"
        },
        {
          "id": "DXGvQwea",
          "type": "arrow"
        },
        {
          "id": "1XUNqqH9",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959712,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "body"
        }
      },
      "index": "aY"
    },
    {
      "text": "ID/EX",
      "fontSize": 16,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "emFI4n1k",
      "type": "text",
      "x": 1114.10546875,
      "y": 720,
      "width": 41.7890625,
      "height": 19.2,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 2768,
      "version": 2,
      "versionNonce": 1997512634,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959712,
      "containerId": null,
      "originalText": "ID/EX",
      "rawText": "ID/EX",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "aZ"
    },
    {
      "text": "pc",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "gGtarJ0g",
      "type": "text",
      "x": 1097,
      "y": 455.25,
      "width": 14.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 60304,
      "version": 2,
      "versionNonce": 2064044262,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959712,
      "containerId": null,
      "originalText": "pc",
      "rawText": "pc",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:pc",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "aa"
    },
    {
      "text": "pc",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "kozXUTak",
      "type": "text",
      "x": 1158.2138671875,
      "y": 455.25,
      "width": 14.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 87034,
      "version": 2,
      "versionNonce": 976722042,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959712,
      "containerId": null,
      "originalText": "pc",
      "rawText": "pc",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:pcq",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "ab"
    },
    {
      "text": "inst",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "6ZVPSAj4",
      "type": "text",
      "x": 1097,
      "y": 630.05,
      "width": 21.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 50797,
      "version": 2,
      "versionNonce": 1493681190,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959713,
      "containerId": null,
      "originalText": "inst",
      "rawText": "inst",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:inst",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "ac"
    },
    {
      "text": "inst",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "OAMk7SHw",
      "type": "text",
      "x": 1151.2138671875,
      "y": 630.05,
      "width": 21.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 6503,
      "version": 2,
      "versionNonce": 1868724538,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959713,
      "containerId": null,
      "originalText": "inst",
      "rawText": "inst",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:instq",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "ad"
    },
    {
      "text": "A",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "jLvGJ2oU",
      "type": "text",
      "x": 1097,
      "y": 759.25,
      "width": 9.337890625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 14551,
      "version": 2,
      "versionNonce": 151539558,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959714,
      "containerId": null,
      "originalText": "A",
      "rawText": "A",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:d1",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "ae"
    },
    {
      "text": "A",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "r700J3p3",
      "type": "text",
      "x": 1163.662109375,
      "y": 759.25,
      "width": 9.337890625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 52987,
      "version": 2,
      "versionNonce": 636699130,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959714,
      "containerId": null,
      "originalText": "A",
      "rawText": "A",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:q1",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "af"
    },
    {
      "text": "B",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "CFKGBKZX",
      "type": "text",
      "x": 1097,
      "y": 888.4499999999999,
      "width": 9.337890625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 99353,
      "version": 2,
      "versionNonce": 1465217702,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959714,
      "containerId": null,
      "originalText": "B",
      "rawText": "B",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:d2",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "ag"
    },
    {
      "text": "B",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "pDuXNJ9p",
      "type": "text",
      "x": 1163.662109375,
      "y": 888.4499999999999,
      "width": 9.337890625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 73726,
      "version": 2,
      "versionNonce": 149746362,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959715,
      "containerId": null,
      "originalText": "B",
      "rawText": "B",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:q2",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "ah"
    },
    {
      "text": "rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "TXTWa33N",
      "type": "text",
      "x": 1097,
      "y": 1010.05,
      "width": 12.4482421875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 63247,
      "version": 2,
      "versionNonce": 2124164582,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959717,
      "containerId": null,
      "originalText": "rd",
      "rawText": "rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:rd",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "ai"
    },
    {
      "text": "rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "ZiT3zNvz",
      "type": "text",
      "x": 1160.5517578125,
      "y": 1010.05,
      "width": 12.4482421875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 10044,
      "version": 2,
      "versionNonce": 1794280314,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959718,
      "containerId": null,
      "originalText": "rd",
      "rawText": "rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:rdq",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "aj"
    },
    {
      "text": "imm",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "tjksiiF4",
      "type": "text",
      "x": 1097,
      "y": 956.85,
      "width": 26.4345703125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 27576,
      "version": 2,
      "versionNonce": 1542029606,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959718,
      "containerId": null,
      "originalText": "imm",
      "rawText": "imm",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:imm",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "ak"
    },
    {
      "text": "imm",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "AjtalJXP",
      "type": "text",
      "x": 1146.5654296875,
      "y": 956.85,
      "width": 26.4345703125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 16172,
      "version": 2,
      "versionNonce": 1380387898,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959719,
      "containerId": null,
      "originalText": "imm",
      "rawText": "imm",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:immq",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "al"
    },
    {
      "text": "Q",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "A3nGo337",
      "type": "text",
      "x": 1156.55517578125,
      "y": 1087.5,
      "width": 10.8896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 18879,
      "version": 3,
      "versionNonce": 943274075,
      "updated": 1792161830775,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959719,
      "containerId": null,
      "originalText": "Q",
      "rawText": "Q",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:ctl",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "am"
    },
    {
      "id": "d5OB4XeQ",
      "type": "rectangle",
      "x": 1890,
      "y": 350,
      "width": 90,
      "height": 760,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#e9f7f3",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 2,
        "roundType": "arc"
      },
      "seed": 75650,
      "version": 3,
      "versionNonce": 402745736,
      "updated": 1792161830562,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "rbwAP4Nz",
          "type": "arrow"
        },
        {
          "id": "ptyiq8SN",
          "type": "arrow"
        },
        {
          "id": "ugL8Kp2y",
          "type": "arrow"
        },
        {
          "id": "InAbTB8e",
          "type": "arrow"
        },
        {
          "id": "xszZ1pkl",
          "type": "arrow"
        },
        {
          "id": "3apB4HfZ",
          "type": "arrow"
        },
        {
          "id": "scT7OtYG",
          "type": "arrow"
        },
        {
          "id": "KxWZVUdh",
          "type": "arrow"
        },
        {
          "id": "1altFC77",
          "type": "arrow"
        },
        {
          "id": "AsAbmlKl",
          "type": "arrow"
        },
        {
          "id": "7PxQ9BeL",
          "type": "arrow"
        },
        {
          "id": "zzhwyEHU",
          "type": "arrow"
        },
        {
          "id": "FN4tCitD",
          "type": "arrow"
        },
        {
          "id": "C8cFkKIy",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959719,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "exmem",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:exmem",
          "role": "body"
        }
      },
      "index": "an"
    },
    {
      "text": "EX/MEM",
      "fontSize": 16,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "LigCEL6m",
      "type": "text",
      "x": 1903.44140625,
      "y": 720,
      "width": 63.1171875,
      "height": 19.2,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 21929,
      "version": 2,
      "versionNonce": 279703462,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959719,
      "containerId": null,
      "originalText": "EX/MEM",
      "rawText": "EX/MEM",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "exmem:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:exmem",
          "role": "text"
        }
      },
      "index": "ao"
    },
    {
      "text": "alu",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "ZErDPdGn",
      "type": "text",
      "x": 1897,
      "y": 759.25,
      "width": 18.6826171875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 69244,
      "version": 3,
      "versionNonce": 739975318,
      "updated": 1792161397465,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959721,
      "containerId": null,
      "originalText": "alu",
      "rawText": "alu",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "exmem:port:d1",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:exmem",
          "role": "text"
        }
      },
      "index": "at"
    },
    {
      "text": "alu",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "iOsvxZfy",
      "type": "text",
      "x": 1954.3173828125,
      "y": 759.25,
      "width": 18.6826171875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 50629,
      "version": 3,
      "versionNonce": 169681984,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959721,
      "containerId": null,
      "originalText": "alu",
      "rawText": "alu",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "exmem:port:q1",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:exmem",
          "role": "text"
        }
      },
      "index": "au"
    },
    {
      "text": "store",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "WnaTSqOP",
      "type": "text",
      "x": 1897,
      "y": 888.4499999999999,
      "width": 31.1240234375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 96347,
      "version": 3,
      "versionNonce": 21669694,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959721,
      "containerId": null,
      "originalText": "store",
      "rawText": "store",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "exmem:port:d2",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:exmem",
          "role": "text"
        }
      },
      "index": "av"
    },
    {
      "text": "store",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "FCz1YrdC",
      "type": "text",
      "x": 1941.8759765625,
      "y": 888.4499999999999,
      "width": 31.1240234375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 40779,
      "version": 3,
      "versionNonce": 107878471,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959722,
      "containerId": null,
      "originalText": "store",
      "rawText": "store",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "exmem:port:q2",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:exmem",
          "role": "text"
        }
      },
      "index": "aw"
    },
    {
      "text": "rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "t9MM4sRf",
      "type": "text",
      "x": 1897,
      "y": 1010.05,
      "width": 12.4482421875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 59810,
      "version": 2,
      "versionNonce": 1159927994,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959722,
      "containerId": null,
      "originalText": "rd",
      "rawText": "rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "exmem:port:rd",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:exmem",
          "role": "text"
        }
      },
      "index": "ax"
    },
    {
      "text": "rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "vW7piXHX",
      "type": "text",
      "x": 1960.5517578125,
      "y": 1010.05,
      "width": 12.4482421875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 32906,
      "version": 2,
      "versionNonce": 1690527718,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959722,
      "containerId": null,
      "originalText": "rd",
      "rawText": "rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "exmem:port:rdq",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:exmem",
          "role": "text"
        }
      },
      "index": "ay"
    },
    {
      "text": "Q",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "7E8D0ICQ",
      "type": "text",
      "x": 1956.55517578125,
      "y": 1087.5,
      "width": 10.8896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 92953,
      "version": 3,
      "versionNonce": 801685662,
      "updated": 1792161830776,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959723,
      "containerId": null,
      "originalText": "Q",
      "rawText": "Q",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "exmem:port:ctl",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:exmem",
          "role": "text"
        }
      },
      "index": "b01"
    },
    {
      "id": "X44pjpPY",
      "type": "rectangle",
      "x": 2370,
      "y": 350,
      "width": 90,
      "height": 760,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#e9f7f3",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 2,
        "roundType": "arc"
      },
      "seed": 20361,
      "version": 3,
      "versionNonce": 128140765,
      "updated": 1792161830562,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "H83lmECf",
          "type": "arrow"
        },
        {
          "id": "3apB4HfZ",
          "type": "arrow"
        },
        {
          "id": "scT7OtYG",
          "type": "arrow"
        },
        {
          "id": "m2MGhtYQ",
          "type": "arrow"
        },
        {
          "id": "A7RvIysa",
          "type": "arrow"
        },
        {
          "id": "PkCUjm53",
          "type": "arrow"
        },
        {
          "id": "gXGCrn8b",
          "type": "arrow"
        },
        {
          "id": "zzhwyEHU",
          "type": "arrow"
        },
        {
          "id": "dUkkvKNq",
          "type": "arrow"
        },
        {
          "id": "1lZXV8uW",
          "type": "arrow"
        },
        {
          "id": "KQ5glvkW",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959723,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "memwb",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:memwb",
          "role": "body"
        }
      },
      "index": "b02"
    },
    {
      "text": "MEM/WB",
      "fontSize": 16,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "nJrxZr8g",
      "type": "text",
      "x": 2381.2265625,
      "y": 720,
      "width": 67.546875,
      "height": 19.2,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 90305,
      "version": 2,
      "versionNonce": 313350906,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959723,
      "containerId": null,
      "originalText": "MEM/WB",
      "rawText": "MEM/WB",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "memwb:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:memwb",
          "role": "text"
        }
      },
      "index": "b03"
    },
    {
      "text": "alu",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "Yl6pjRTD",
      "type": "text",
      "x": 2377,
      "y": 759.25,
      "width": 18.6826171875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 57338,
      "version": 3,
      "versionNonce": 422342234,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959726,
      "containerId": null,
      "originalText": "alu",
      "rawText": "alu",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "memwb:port:d1",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:memwb",
          "role": "text"
        }
      },
      "index": "b08"
    },
    {
      "text": "alu",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "bStehDuv",
      "type": "text",
      "x": 2434.3173828125,
      "y": 759.25,
      "width": 18.6826171875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 79565,
      "version": 3,
      "versionNonce": 317849058,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959726,
      "containerId": null,
      "originalText": "alu",
      "rawText": "alu",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "memwb:port:q1",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:memwb",
          "role": "text"
        }
      },
      "index": "b09"
    },
    {
      "text": "load",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "FRz2afV0",
      "type": "text",
      "x": 2377,
      "y": 888.4499999999999,
      "width": 26.46875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 48477,
      "version": 3,
      "versionNonce": 714085047,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959726,
      "containerId": null,
      "originalText": "load",
      "rawText": "load",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "memwb:port:d2",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:memwb",
          "role": "text"
        }
      },
      "index": "b0A"
    },
    {
      "text": "load",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "rp9FVerd",
      "type": "text",
      "x": 2426.53125,
      "y": 888.4499999999999,
      "width": 26.46875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 99999,
      "version": 3,
      "versionNonce": 163724160,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959726,
      "containerId": null,
      "originalText": "load",
      "rawText": "load",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "memwb:port:q2",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:memwb",
          "role": "text"
        }
      },
      "index": "b0B"
    },
    {
      "text": "rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "PNWVUyGO",
      "type": "text",
      "x": 2377,
      "y": 1010.05,
      "width": 12.4482421875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 61323,
      "version": 2,
      "versionNonce": 533227174,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959727,
      "containerId": null,
      "originalText": "rd",
      "rawText": "rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "memwb:port:rd",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:memwb",
          "role": "text"
        }
      },
      "index": "b0C"
    },
    {
      "text": "rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "LNoT1RSu",
      "type": "text",
      "x": 2440.5517578125,
      "y": 1010.05,
      "width": 12.4482421875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 86980,
      "version": 2,
      "versionNonce": 1817394874,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959727,
      "containerId": null,
      "originalText": "rd",
      "rawText": "rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "memwb:port:rdq",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:memwb",
          "role": "text"
        }
      },
      "index": "b0D"
    },
    {
      "text": "Q",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "6toCLcoL",
      "type": "text",
      "x": 2436.55517578125,
      "y": 1087.5,
      "width": 10.8896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 56817,
      "version": 3,
      "versionNonce": 501150915,
      "updated": 1792161830776,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959728,
      "containerId": null,
      "originalText": "Q",
      "rawText": "Q",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "memwb:port:ctl",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:memwb",
          "role": "text"
        }
      },
      "index": "b0G"
    },
    {
      "id": "gDo3FgMn",
      "type": "rectangle",
      "x": 95,
      "y": 570,
      "width": 130,
      "height": 180,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "#eff6ff",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 2,
        "roundType": "arc"
      },
      "seed": 8223,
      "version": 2,
      "versionNonce": 1904891962,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "f9x2CgGD",
          "type": "arrow"
        },
        {
          "id": "sSMAH8eo",
          "type": "arrow"
        },
        {
          "id": "VW4fJOUf",
          "type": "arrow"
        },
        {
          "id": "Pydlp8xP",
          "type": "arrow"
        },
        {
          "id": "QiMUXs0X",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959728,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:pc",
          "role": "body"
        }
      },
      "index": "b0H"
    },
    {
      "text": "PC",
      "fontSize": 28,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "mNBhaXPR",
      "type": "text",
      "x": 140.5517578125,
      "y": 642.5,
      "width": 38.896484375,
      "height": 33.6,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 44601,
      "version": 2,
      "versionNonce": 85057638,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959728,
      "containerId": null,
      "originalText": "PC",
      "rawText": "PC",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:pc",
          "role": "text"
        }
      },
      "index": "b0I"
    },
    {
      "text": "we",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "hIuvqFY9",
      "type": "text",
      "x": 151.0517578125,
      "y": 575,
      "width": 17.896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 70771,
      "version": 2,
      "versionNonce": 1975992570,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959728,
      "containerId": null,
      "originalText": "we",
      "rawText": "we",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc:port:we",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:pc",
          "role": "text"
        }
      },
      "index": "b0J"
    },
    {
      "id": "OiRSfOJq",
      "type": "rectangle",
      "x": 90,
      "y": 345,
      "width": 100,
      "height": 140,
      "angle": 0,
      "strokeColor": "transparent",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 87520,
      "version": 2,
      "versionNonce": 503636902,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "5HFI2OwA",
          "type": "arrow"
        },
        {
          "id": "VW4fJOUf",
          "type": "arrow"
        },
        {
          "id": "TvjJCsTx",
          "type": "arrow"
        },
        {
          "id": "GPTUK7Ri",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959729,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "npc",
          "role": "container"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:npc",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "b0K"
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          100,
          22.399999999999977
        ],
        [
          100,
          117.60000000000002
        ],
        [
          0,
          140
        ],
        [
          0,
          0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": null,
      "endBinding": null,
      "startArrowhead": null,
      "endArrowhead": null,
      "id": "d4ZEQrIY",
      "type": "line",
      "x": 90,
      "y": 345,
      "width": 100,
      "height": 140,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "#ffffff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 8569,
      "version": 2,
      "versionNonce": 1542001082,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959729,
      "polygon": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "npc:outline",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:npc",
          "role": "body"
        }
      },
      "index": "b0L"
    },
    {
      "text": "NEXT",
      "fontSize": 20,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "pK16q5iE",
      "type": "text",
      "x": 113.330078125,
      "y": 402.5,
      "width": 53.33984375,
      "height": 24,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 92646,
      "version": 2,
      "versionNonce": 3505894,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959729,
      "containerId": null,
      "originalText": "NEXT",
      "rawText": "NEXT",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "npc:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:npc",
          "role": "text"
        }
      },
      "index": "b0M"
    },
    {
      "text": "0",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "jObgqycu",
      "type": "text",
      "x": 97,
      "y": 371.25,
      "width": 7.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 73588,
      "version": 2,
      "versionNonce": 1729284730,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959730,
      "containerId": null,
      "originalText": "0",
      "rawText": "0",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "npc:port:seq",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:npc",
          "role": "text"
        }
      },
      "index": "b0N"
    },
    {
      "text": "1",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "n8wDjrln",
      "type": "text",
      "x": 97,
      "y": 441.25,
      "width": 7.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 38232,
      "version": 2,
      "versionNonce": 1613804070,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959730,
      "containerId": null,
      "originalText": "1",
      "rawText": "1",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "npc:port:br",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:npc",
          "role": "text"
        }
      },
      "index": "b0O"
    },
    {
      "text": "sel",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "s1fhkb0J",
      "type": "text",
      "x": 131.0517578125,
      "y": 366.8,
      "width": 17.896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 96643,
      "version": 3,
      "versionNonce": 454262127,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959730,
      "containerId": null,
      "originalText": "sel",
      "rawText": "sel",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "npc:port:sel",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:npc",
          "role": "text"
        }
      },
      "index": "b0P"
    },
    {
      "id": "72xk5Zon",
      "type": "rectangle",
      "x": 285,
      "y": 340,
      "width": 145,
      "height": 105,
      "angle": 0,
      "strokeColor": "transparent",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 18421,
      "version": 2,
      "versionNonce": 1491303782,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "sSMAH8eo",
          "type": "arrow"
        },
        {
          "id": "5HFI2OwA",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959730,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc4",
          "role": "container"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:pc4",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "b0Q"
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          145,
          21
        ],
        [
          145,
          84
        ],
        [
          0,
          105
        ],
        [
          0,
          68.25
        ],
        [
          31.899999999999977,
          52.5
        ],
        [
          0,
          36.75
        ],
        [
          0,
          0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": null,
      "endBinding": null,
      "startArrowhead": null,
      "endArrowhead": null,
      "id": "HvTqadSb",
      "type": "line",
      "x": 285,
      "y": 340,
      "width": 145,
      "height": 105,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "#eff6ff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 36156,
      "version": 2,
      "versionNonce": 925496314,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959730,
      "polygon": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc4:outline",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:pc4",
          "role": "body"
        }
      },
      "index": "b0R"
    },
    {
      "text": "PC + 4",
      "fontSize": 20,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "DArG5KH4",
      "type": "text",
      "x": 332.450390625,
      "y": 380,
      "width": 61.69921875,
      "height": 24,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 7959,
      "version": 2,
      "versionNonce": 530243750,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959730,
      "containerId": null,
      "originalText": "PC + 4",
      "rawText": "PC + 4",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc4:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:pc4",
          "role": "text"
        }
      },
      "index": "b0S"
    },
    {
      "id": "9NPx3ltI",
      "type": "rectangle",
      "x": 280,
      "y": 585,
      "width": 150,
      "height": 180,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#f0fdfa",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 6,
        "roundType": "arc"
      },
      "seed": 32809,
      "version": 2,
      "versionNonce": 1685939386,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "f9x2CgGD",
          "type": "arrow"
        },
        {
          "id": "qNjLnpUH",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959731,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imem",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:imem",
          "role": "body"
        }
      },
      "index": "b0T"
    },
    {
      "text": "I-MEM",
      "fontSize": 24,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "9xAZYHce",
      "type": "text",
      "x": 319.673828125,
      "y": 660,
      "width": 70.65234375,
      "height": 28.799999999999997,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 23491,
      "version": 2,
      "versionNonce": 939776998,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959731,
      "containerId": null,
      "originalText": "I-MEM",
      "rawText": "I-MEM",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imem:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:imem",
          "role": "text"
        }
      },
      "index": "b0U"
    },
    {
      "text": "addr",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "mcEEbYBy",
      "type": "text",
      "x": 287,
      "y": 630.25,
      "width": 28.0205078125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 78407,
      "version": 2,
      "versionNonce": 530890106,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959731,
      "containerId": null,
      "originalText": "addr",
      "rawText": "addr",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imem:port:addr",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:imem",
          "role": "text"
        }
      },
      "index": "b0V"
    },
    {
      "text": "inst",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "Jc8cgLCs",
      "type": "text",
      "x": 401.2138671875,
      "y": 666.25,
      "width": 21.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 87616,
      "version": 2,
      "versionNonce": 673935142,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959731,
      "containerId": null,
      "originalText": "inst",
      "rawText": "inst",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imem:port:data",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:imem",
          "role": "text"
        }
      },
      "index": "b0W"
    },
    {
      "id": "Ci9XxGBw",
      "type": "rectangle",
      "x": 680,
      "y": 540,
      "width": 270,
      "height": 260,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#ffffff",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 2,
        "roundType": "arc"
      },
      "seed": 14195,
      "version": 3,
      "versionNonce": 184683580,
      "updated": 1792161830563,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "G7JK65WS",
          "type": "arrow"
        },
        {
          "id": "vmAC29Nz",
          "type": "arrow"
        },
        {
          "id": "gjdqm2qt",
          "type": "arrow"
        },
        {
          "id": "fQvlBr6A",
          "type": "arrow"
        },
        {
          "id": "oCXi6yZy",
          "type": "arrow"
        },
        {
          "id": "1lZXV8uW",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959731,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "rf",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:rf",
          "role": "body"
        }
      },
      "index": "b0X"
    },
    {
      "text": "REGISTER\nFILE",
      "fontSize": 28,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "SxzT4s74",
      "type": "text",
      "x": 743.4345703125,
      "y": 635,
      "width": 143.130859375,
      "height": 67.2,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 92482,
      "version": 2,
      "versionNonce": 746494566,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959732,
      "containerId": null,
      "originalText": "REGISTER\nFILE",
      "rawText": "REGISTER\nFILE",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "rf:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:rf",
          "role": "text"
        }
      },
      "index": "b0Y"
    },
    {
      "text": "rs1/rs2",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "IZtJnu6y",
      "type": "text",
      "x": 793.60693359375,
      "y": 545,
      "width": 42.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 70996,
      "version": 2,
      "versionNonce": 1411065594,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959732,
      "containerId": null,
      "originalText": "rs1/rs2",
      "rawText": "rs1/rs2",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "rf:port:raddr",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:rf",
          "role": "text"
        }
      },
      "index": "b0Z"
    },
    {
      "text": "rd1",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "ub9FtUy9",
      "type": "text",
      "x": 922.765625,
      "y": 609.25,
      "width": 20.234375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 44615,
      "version": 2,
      "versionNonce": 1808424358,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959732,
      "containerId": null,
      "originalText": "rd1",
      "rawText": "rd1",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "rf:port:r1",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:rf",
          "role": "text"
        }
      },
      "index": "b0a"
    },
    {
      "text": "rd2",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "CKMeeBit",
      "type": "text",
      "x": 922.765625,
      "y": 718.45,
      "width": 20.234375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 37075,
      "version": 2,
      "versionNonce": 1389377466,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959733,
      "containerId": null,
      "originalText": "rd2",
      "rawText": "rd2",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "rf:port:r2",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:rf",
          "role": "text"
        }
      },
      "index": "b0b"
    },
    {
      "text": "wdata",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "fIBYA888",
      "type": "text",
      "x": 836.82080078125,
      "y": 777.5,
      "width": 37.3583984375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 28091,
      "version": 2,
      "versionNonce": 725334246,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959733,
      "containerId": null,
      "originalText": "wdata",
      "rawText": "wdata",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "rf:port:wd",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:rf",
          "role": "text"
        }
      },
      "index": "b0c"
    },
    {
      "text": "rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "XD53rY4q",
      "type": "text",
      "x": 754.77587890625,
      "y": 777.5,
      "width": 12.4482421875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 24713,
      "version": 2,
      "versionNonce": 35991674,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959734,
      "containerId": null,
      "originalText": "rd",
      "rawText": "rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "rf:port:wa",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:rf",
          "role": "text"
        }
      },
      "index": "b0d"
    },
    {
      "text": "we",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "fRPbCdPw",
      "type": "text",
      "x": 687,
      "y": 752.25,
      "width": 17.896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 20582,
      "version": 2,
      "versionNonce": 39824422,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959734,
      "containerId": null,
      "originalText": "we",
      "rawText": "we",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "rf:port:we",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:rf",
          "role": "text"
        }
      },
      "index": "b0e"
    },
    {
      "id": "JtAsLRlW",
      "type": "rectangle",
      "x": 675,
      "y": 315,
      "width": 250,
      "height": 95,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "#fff7ed",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 6,
        "roundType": "arc"
      },
      "seed": 31380,
      "version": 3,
      "versionNonce": 918640312,
      "updated": 1792161830562,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "mqwzqZ19",
          "type": "arrow"
        },
        {
          "id": "iths4XL8",
          "type": "arrow"
        },
        {
          "id": "1LV6TPTr",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959734,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "decode",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:decode",
          "role": "body"
        }
      },
      "index": "b0f"
    },
    {
      "text": "DECODE",
      "fontSize": 24,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "dfXosQS5",
      "type": "text",
      "x": 748.66015625,
      "y": 347.5,
      "width": 102.6796875,
      "height": 28.799999999999997,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 12886,
      "version": 2,
      "versionNonce": 253966182,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959734,
      "containerId": null,
      "originalText": "DECODE",
      "rawText": "DECODE",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "decode:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:decode",
          "role": "text"
        }
      },
      "index": "b0g"
    },
    {
      "text": "rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "Zz09IRcr",
      "type": "text",
      "x": 868.77587890625,
      "y": 387.5,
      "width": 12.4482421875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 93582,
      "version": 2,
      "versionNonce": 1364908538,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959734,
      "containerId": null,
      "originalText": "rd",
      "rawText": "rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "decode:port:rd",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:decode",
          "role": "text"
        }
      },
      "index": "b0h"
    },
    {
      "id": "otHClNTR",
      "type": "rectangle",
      "x": 750,
      "y": 925,
      "width": 180,
      "height": 90,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#f0fdfa",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 6,
        "roundType": "arc"
      },
      "seed": 59955,
      "version": 2,
      "versionNonce": 701717158,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "iphC33F5",
          "type": "arrow"
        },
        {
          "id": "yqzKtVT8",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959735,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imm",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:imm",
          "role": "body"
        }
      },
      "index": "b0i"
    },
    {
      "text": "IMM GEN",
      "fontSize": 24,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "5pbIoHuH",
      "type": "text",
      "x": 787.3359375,
      "y": 955,
      "width": 105.328125,
      "height": 28.799999999999997,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 13341,
      "version": 2,
      "versionNonce": 329353914,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959735,
      "containerId": null,
      "originalText": "IMM GEN",
      "rawText": "IMM GEN",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imm:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:imm",
          "role": "text"
        }
      },
      "index": "b0j"
    },
    {
      "id": "EUNvJS1m",
      "type": "rectangle",
      "x": 1260,
      "y": 520,
      "width": 110,
      "height": 170,
      "angle": 0,
      "strokeColor": "transparent",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 30160,
      "version": 2,
      "versionNonce": 421336550,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "ECQY9lyq",
          "type": "arrow"
        },
        {
          "id": "dx8SRQwx",
          "type": "arrow"
        },
        {
          "id": "sXyktktI",
          "type": "arrow"
        },
        {
          "id": "NJiZtwmY",
          "type": "arrow"
        },
        {
          "id": "KxWZVUdh",
          "type": "arrow"
        },
        {
          "id": "B6Naxv8B",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959735,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fa",
          "role": "container"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fa",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "b0k"
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          110,
          27.200000000000045
        ],
        [
          110,
          142.79999999999995
        ],
        [
          0,
          170
        ],
        [
          0,
          0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": null,
      "endBinding": null,
      "startArrowhead": null,
      "endArrowhead": null,
      "id": "5HnKEUaJ",
      "type": "line",
      "x": 1260,
      "y": 520,
      "width": 110,
      "height": 170,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "#eff6ff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 69948,
      "version": 2,
      "versionNonce": 1666458490,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959735,
      "polygon": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fa:outline",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fa",
          "role": "body"
        }
      },
      "index": "b0l"
    },
    {
      "text": "FWD A",
      "fontSize": 18,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "M1yzc1j0",
      "type": "text",
      "x": 1286.0048828125,
      "y": 593.75,
      "width": 57.990234375,
      "height": 21.599999999999998,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 43352,
      "version": 2,
      "versionNonce": 1175284006,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959735,
      "containerId": null,
      "originalText": "FWD A",
      "rawText": "FWD A",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fa:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fa",
          "role": "text"
        }
      },
      "index": "b0m"
    },
    {
      "text": "00",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "h9ff4Pq7",
      "type": "text",
      "x": 1267,
      "y": 545.25,
      "width": 15.572265625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 31230,
      "version": 2,
      "versionNonce": 2058724410,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959735,
      "containerId": null,
      "originalText": "00",
      "rawText": "00",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fa:port:reg",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fa",
          "role": "text"
        }
      },
      "index": "b0n"
    },
    {
      "text": "01",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "N2lAAwfw",
      "type": "text",
      "x": 1267,
      "y": 596.25,
      "width": 15.572265625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 86820,
      "version": 2,
      "versionNonce": 1880183910,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959736,
      "containerId": null,
      "originalText": "01",
      "rawText": "01",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fa:port:wb",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fa",
          "role": "text"
        }
      },
      "index": "b0o"
    },
    {
      "text": "10",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "S9T6G4C5",
      "type": "text",
      "x": 1267,
      "y": 647.25,
      "width": 15.572265625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 58910,
      "version": 2,
      "versionNonce": 1403587834,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959736,
      "containerId": null,
      "originalText": "10",
      "rawText": "10",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fa:port:ex",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fa",
          "role": "text"
        }
      },
      "index": "b0p"
    },
    {
      "text": "sel",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "oB5V4s2t",
      "type": "text",
      "x": 1306.0517578125,
      "y": 545.4,
      "width": 17.896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 11324,
      "version": 3,
      "versionNonce": 378177552,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959736,
      "containerId": null,
      "originalText": "sel",
      "rawText": "sel",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fa:port:sel",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fa",
          "role": "text"
        }
      },
      "index": "b0q"
    },
    {
      "id": "l9evpEHs",
      "type": "rectangle",
      "x": 1260,
      "y": 820,
      "width": 110,
      "height": 170,
      "angle": 0,
      "strokeColor": "transparent",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 84648,
      "version": 2,
      "versionNonce": 867261882,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "KdLmJLKR",
          "type": "arrow"
        },
        {
          "id": "UdHgQW7G",
          "type": "arrow"
        },
        {
          "id": "ptyiq8SN",
          "type": "arrow"
        },
        {
          "id": "rYOaHdIb",
          "type": "arrow"
        },
        {
          "id": "gyYdZlED",
          "type": "arrow"
        },
        {
          "id": "1altFC77",
          "type": "arrow"
        },
        {
          "id": "9wB7drvG",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959736,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fb",
          "role": "container"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fb",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "b0r"
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          110,
          27.200000000000045
        ],
        [
          110,
          142.79999999999995
        ],
        [
          0,
          170
        ],
        [
          0,
          0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": null,
      "endBinding": null,
      "startArrowhead": null,
      "endArrowhead": null,
      "id": "zMKfd9nG",
      "type": "line",
      "x": 1260,
      "y": 820,
      "width": 110,
      "height": 170,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "#eff6ff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 65321,
      "version": 2,
      "versionNonce": 552071910,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959737,
      "polygon": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fb:outline",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fb",
          "role": "body"
        }
      },
      "index": "b0s"
    },
    {
      "text": "FWD B",
      "fontSize": 18,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "xUXbaD6s",
      "type": "text",
      "x": 1286.0048828125,
      "y": 893.75,
      "width": 57.990234375,
      "height": 21.599999999999998,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 1932,
      "version": 2,
      "versionNonce": 938579578,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959737,
      "containerId": null,
      "originalText": "FWD B",
      "rawText": "FWD B",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fb:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fb",
          "role": "text"
        }
      },
      "index": "b0t"
    },
    {
      "text": "00",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "BjUnnpsM",
      "type": "text",
      "x": 1267,
      "y": 845.25,
      "width": 15.572265625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 61505,
      "version": 2,
      "versionNonce": 712287782,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959737,
      "containerId": null,
      "originalText": "00",
      "rawText": "00",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fb:port:reg",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fb",
          "role": "text"
        }
      },
      "index": "b0u"
    },
    {
      "text": "01",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "GB0pSNBj",
      "type": "text",
      "x": 1267,
      "y": 896.25,
      "width": 15.572265625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 56758,
      "version": 2,
      "versionNonce": 1630320442,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959737,
      "containerId": null,
      "originalText": "01",
      "rawText": "01",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fb:port:wb",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fb",
          "role": "text"
        }
      },
      "index": "b0v"
    },
    {
      "text": "10",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "fGSqJcS4",
      "type": "text",
      "x": 1267,
      "y": 947.25,
      "width": 15.572265625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 32288,
      "version": 2,
      "versionNonce": 512291174,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959738,
      "containerId": null,
      "originalText": "10",
      "rawText": "10",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fb:port:ex",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fb",
          "role": "text"
        }
      },
      "index": "b0w"
    },
    {
      "text": "sel",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "7944P4nU",
      "type": "text",
      "x": 1306.0517578125,
      "y": 845.4,
      "width": 17.896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 43428,
      "version": 3,
      "versionNonce": 226155302,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959738,
      "containerId": null,
      "originalText": "sel",
      "rawText": "sel",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fb:port:sel",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:fb",
          "role": "text"
        }
      },
      "index": "b0x"
    },
    {
      "id": "hEm4s7Bs",
      "type": "rectangle",
      "x": 1490,
      "y": 790,
      "width": 105,
      "height": 155,
      "angle": 0,
      "strokeColor": "transparent",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 50294,
      "version": 3,
      "versionNonce": 349507786,
      "updated": 1792161830562,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "UdHgQW7G",
          "type": "arrow"
        },
        {
          "id": "twVlscTM",
          "type": "arrow"
        },
        {
          "id": "rap2QDOI",
          "type": "arrow"
        },
        {
          "id": "DXGvQwea",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959738,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "src",
          "role": "container"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:src",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "b0y"
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          105,
          24.799999999999955
        ],
        [
          105,
          130.20000000000005
        ],
        [
          0,
          155
        ],
        [
          0,
          0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": null,
      "endBinding": null,
      "startArrowhead": null,
      "endArrowhead": null,
      "id": "gllrAlB8",
      "type": "line",
      "x": 1490,
      "y": 790,
      "width": 105,
      "height": 155,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "#ffffff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 14279,
      "version": 2,
      "versionNonce": 1606398138,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959738,
      "polygon": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "src:outline",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:src",
          "role": "body"
        }
      },
      "index": "b0z"
    },
    {
      "text": "SRC",
      "fontSize": 20,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "iaQyp88p",
      "type": "text",
      "x": 1521.38671875,
      "y": 855,
      "width": 42.2265625,
      "height": 24,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 83587,
      "version": 2,
      "versionNonce": 1104957414,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959738,
      "containerId": null,
      "originalText": "SRC",
      "rawText": "SRC",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "src:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:src",
          "role": "text"
        }
      },
      "index": "b10"
    },
    {
      "text": "0",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "gTkF3LZN",
      "type": "text",
      "x": 1497,
      "y": 820,
      "width": 7.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 31115,
      "version": 2,
      "versionNonce": 347965818,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959739,
      "containerId": null,
      "originalText": "0",
      "rawText": "0",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "src:port:reg",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:src",
          "role": "text"
        }
      },
      "index": "b11"
    },
    {
      "text": "1",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "apgMtmUK",
      "type": "text",
      "x": 1497,
      "y": 897.5,
      "width": 7.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 79566,
      "version": 2,
      "versionNonce": 1188389670,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959739,
      "containerId": null,
      "originalText": "1",
      "rawText": "1",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "src:port:imm",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:src",
          "role": "text"
        }
      },
      "index": "b12"
    },
    {
      "text": "sel",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "rbgNd5ty",
      "type": "text",
      "x": 1533.5517578125,
      "y": 903.9,
      "width": 17.896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 5399,
      "version": 3,
      "versionNonce": 192224670,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959740,
      "containerId": null,
      "originalText": "sel",
      "rawText": "sel",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "src:port:sel",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:src",
          "role": "text"
        }
      },
      "index": "b13"
    },
    {
      "id": "h3i0v3id",
      "type": "rectangle",
      "x": 1635,
      "y": 565,
      "width": 165,
      "height": 200,
      "angle": 0,
      "strokeColor": "transparent",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 19980,
      "version": 3,
      "versionNonce": 914004265,
      "updated": 1792161830562,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "dx8SRQwx",
          "type": "arrow"
        },
        {
          "id": "twVlscTM",
          "type": "arrow"
        },
        {
          "id": "rbwAP4Nz",
          "type": "arrow"
        },
        {
          "id": "viHDu4dC",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959740,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "alu",
          "role": "container"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:alu",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "b14"
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          165,
          40
        ],
        [
          165,
          160
        ],
        [
          0,
          200
        ],
        [
          0,
          130
        ],
        [
          36.299999999999955,
          100
        ],
        [
          0,
          70
        ],
        [
          0,
          0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": null,
      "endBinding": null,
      "startArrowhead": null,
      "endArrowhead": null,
      "id": "CmIqqT4b",
      "type": "line",
      "x": 1635,
      "y": 565,
      "width": 165,
      "height": 200,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "#dbeafe",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 35214,
      "version": 2,
      "versionNonce": 443609850,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959740,
      "polygon": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "alu:outline",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:alu",
          "role": "body"
        }
      },
      "index": "b15"
    },
    {
      "text": "ALU",
      "fontSize": 32,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "wYz28KIY",
      "type": "text",
      "x": 1692.975,
      "y": 645,
      "width": 62.25,
      "height": 38.4,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 90028,
      "version": 2,
      "versionNonce": 931615142,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959741,
      "containerId": null,
      "originalText": "ALU",
      "rawText": "ALU",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "alu:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:alu",
          "role": "text"
        }
      },
      "index": "b16"
    },
    {
      "text": "A",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "VoQclu4x",
      "type": "text",
      "x": 1642,
      "y": 596.25,
      "width": 9.337890625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 3991,
      "version": 2,
      "versionNonce": 1686930362,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959741,
      "containerId": null,
      "originalText": "A",
      "rawText": "A",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "alu:port:a",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:alu",
          "role": "text"
        }
      },
      "index": "b17"
    },
    {
      "text": "B",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "VCsvN31K",
      "type": "text",
      "x": 1642,
      "y": 716.25,
      "width": 9.337890625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 24479,
      "version": 2,
      "versionNonce": 1530539238,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959741,
      "containerId": null,
      "originalText": "B",
      "rawText": "B",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "alu:port:b",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:alu",
          "role": "text"
        }
      },
      "index": "b18"
    },
    {
      "text": "op",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "oZLiv219",
      "type": "text",
      "x": 1709.7138671875,
      "y": 594,
      "width": 15.572265625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 47844,
      "version": 3,
      "versionNonce": 406261012,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959742,
      "containerId": null,
      "originalText": "op",
      "rawText": "op",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "alu:port:ctl",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:alu",
          "role": "text"
        }
      },
      "index": "b19"
    },
    {
      "id": "8oC6OSwF",
      "type": "rectangle",
      "x": 1500,
      "y": 310,
      "width": 270,
      "height": 145,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "#fff7ed",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 6,
        "roundType": "arc"
      },
      "seed": 8873,
      "version": 3,
      "versionNonce": 232335496,
      "updated": 1792161830562,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "v7CpLDq4",
          "type": "arrow"
        },
        {
          "id": "sXyktktI",
          "type": "arrow"
        },
        {
          "id": "rYOaHdIb",
          "type": "arrow"
        },
        {
          "id": "cPcmZtQE",
          "type": "arrow"
        },
        {
          "id": "TvjJCsTx",
          "type": "arrow"
        },
        {
          "id": "GPTUK7Ri",
          "type": "arrow"
        },
        {
          "id": "5KYFChTs",
          "type": "arrow"
        },
        {
          "id": "r4mihXKS",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959742,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:branch",
          "role": "body"
        }
      },
      "index": "b1A"
    },
    {
      "text": "BRANCH\nADD + CMP",
      "fontSize": 22,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "u5cOYbiG",
      "type": "text",
      "x": 1574.79541015625,
      "y": 355,
      "width": 120.4091796875,
      "height": 52.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 27392,
      "version": 2,
      "versionNonce": 1173773626,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959742,
      "containerId": null,
      "originalText": "BRANCH\nADD + CMP",
      "rawText": "BRANCH\nADD + CMP",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:branch",
          "role": "text"
        }
      },
      "index": "b1B"
    },
    {
      "text": "pc",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "hYGDoWy2",
      "type": "text",
      "x": 1507,
      "y": 330.25,
      "width": 14.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 76382,
      "version": 2,
      "versionNonce": 18131814,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959742,
      "containerId": null,
      "originalText": "pc",
      "rawText": "pc",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch:port:pc",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:branch",
          "role": "text"
        }
      },
      "index": "b1C"
    },
    {
      "text": "imm",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "pB5PwK3Y",
      "type": "text",
      "x": 1507,
      "y": 417.25,
      "width": 26.4345703125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 26866,
      "version": 2,
      "versionNonce": 1214948858,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959743,
      "containerId": null,
      "originalText": "imm",
      "rawText": "imm",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch:port:imm",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:branch",
          "role": "text"
        }
      },
      "index": "b1D"
    },
    {
      "text": "A",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "lfjeLQTe",
      "type": "text",
      "x": 1562.8310546875,
      "y": 432.5,
      "width": 9.337890625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 57022,
      "version": 2,
      "versionNonce": 1165381286,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959743,
      "containerId": null,
      "originalText": "A",
      "rawText": "A",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch:port:a",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:branch",
          "role": "text"
        }
      },
      "index": "b1E"
    },
    {
      "text": "B",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "LMntLKet",
      "type": "text",
      "x": 1697.8310546875,
      "y": 432.5,
      "width": 9.337890625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 5606,
      "version": 2,
      "versionNonce": 785897146,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959743,
      "containerId": null,
      "originalText": "B",
      "rawText": "B",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch:port:b",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:branch",
          "role": "text"
        }
      },
      "index": "b1F"
    },
    {
      "text": "target",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "8ECvrykb",
      "type": "text",
      "x": 1576.60009765625,
      "y": 315,
      "width": 35.7998046875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 42576,
      "version": 2,
      "versionNonce": 742492646,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959744,
      "containerId": null,
      "originalText": "target",
      "rawText": "target",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch:port:target",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:branch",
          "role": "text"
        }
      },
      "index": "b1G"
    },
    {
      "text": "taken",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "l8MdEGS4",
      "type": "text",
      "x": 1698.8759765625,
      "y": 315,
      "width": 34.248046875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 92288,
      "version": 2,
      "versionNonce": 1507913594,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959744,
      "containerId": null,
      "originalText": "taken",
      "rawText": "taken",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch:port:taken",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:branch",
          "role": "text"
        }
      },
      "index": "b1H"
    },
    {
      "text": "br",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "uBXWuVVo",
      "type": "text",
      "x": 1750.5517578125,
      "y": 373.75,
      "width": 12.4482421875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 32508,
      "version": 2,
      "versionNonce": 1686330662,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959744,
      "containerId": null,
      "originalText": "br",
      "rawText": "br",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch:port:ctl",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:branch",
          "role": "text"
        }
      },
      "index": "b1I"
    },
    {
      "id": "PX9apXAV",
      "type": "rectangle",
      "x": 2070,
      "y": 615,
      "width": 200,
      "height": 255,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#f0fdfa",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 6,
        "roundType": "arc"
      },
      "seed": 71253,
      "version": 3,
      "versionNonce": 900633905,
      "updated": 1792161830562,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "InAbTB8e",
          "type": "arrow"
        },
        {
          "id": "xszZ1pkl",
          "type": "arrow"
        },
        {
          "id": "H83lmECf",
          "type": "arrow"
        },
        {
          "id": "FN4tCitD",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959745,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "dmem",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:dmem",
          "role": "body"
        }
      },
      "index": "b1J"
    },
    {
      "text": "D-MEM",
      "fontSize": 28,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "6f1RDuAc",
      "type": "text",
      "x": 2122.5654296875,
      "y": 725,
      "width": 94.869140625,
      "height": 33.6,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 10267,
      "version": 2,
      "versionNonce": 866699366,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959745,
      "containerId": null,
      "originalText": "D-MEM",
      "rawText": "D-MEM",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "dmem:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:dmem",
          "role": "text"
        }
      },
      "index": "b1K"
    },
    {
      "text": "addr",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "5xqL8S3o",
      "type": "text",
      "x": 2077,
      "y": 657.25,
      "width": 28.0205078125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 52500,
      "version": 2,
      "versionNonce": 1316149498,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959745,
      "containerId": null,
      "originalText": "addr",
      "rawText": "addr",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "dmem:port:addr",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:dmem",
          "role": "text"
        }
      },
      "index": "b1L"
    },
    {
      "text": "wdata",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "onb5OmXm",
      "type": "text",
      "x": 2077,
      "y": 789.85,
      "width": 37.3583984375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 23559,
      "version": 2,
      "versionNonce": 696175526,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959745,
      "containerId": null,
      "originalText": "wdata",
      "rawText": "wdata",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "dmem:port:wd",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:dmem",
          "role": "text"
        }
      },
      "index": "b1M"
    },
    {
      "text": "rdata",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "RxpPVpf3",
      "type": "text",
      "x": 2231.08984375,
      "y": 721,
      "width": 31.91015625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 29112,
      "version": 2,
      "versionNonce": 1264691642,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959746,
      "containerId": null,
      "originalText": "rdata",
      "rawText": "rdata",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "dmem:port:rd",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:dmem",
          "role": "text"
        }
      },
      "index": "b1N"
    },
    {
      "text": "rd/wr",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "pkYEDe6V",
      "type": "text",
      "x": 2154.44482421875,
      "y": 620,
      "width": 31.1103515625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 11905,
      "version": 2,
      "versionNonce": 1412589286,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959746,
      "containerId": null,
      "originalText": "rd/wr",
      "rawText": "rd/wr",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "dmem:port:ctl",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:dmem",
          "role": "text"
        }
      },
      "index": "b1O"
    },
    {
      "id": "OS0QNaxX",
      "type": "rectangle",
      "x": 2550,
      "y": 565,
      "width": 110,
      "height": 200,
      "angle": 0,
      "strokeColor": "transparent",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 96578,
      "version": 3,
      "versionNonce": 945582277,
      "updated": 1792161830562,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "m2MGhtYQ",
          "type": "arrow"
        },
        {
          "id": "A7RvIysa",
          "type": "arrow"
        },
        {
          "id": "fQvlBr6A",
          "type": "arrow"
        },
        {
          "id": "NJiZtwmY",
          "type": "arrow"
        },
        {
          "id": "gyYdZlED",
          "type": "arrow"
        },
        {
          "id": "dUkkvKNq",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959746,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wbmux",
          "role": "container"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:wbmux",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "b1P"
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          110,
          32
        ],
        [
          110,
          168
        ],
        [
          0,
          200
        ],
        [
          0,
          0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": null,
      "endBinding": null,
      "startArrowhead": null,
      "endArrowhead": null,
      "id": "6VeUOEU1",
      "type": "line",
      "x": 2550,
      "y": 565,
      "width": 110,
      "height": 200,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "#eff6ff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 23133,
      "version": 2,
      "versionNonce": 1951439398,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959746,
      "polygon": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wbmux:outline",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:wbmux",
          "role": "body"
        }
      },
      "index": "b1Q"
    },
    {
      "text": "WB",
      "fontSize": 24,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "f62B7KqF",
      "type": "text",
      "x": 2585.669921875,
      "y": 650,
      "width": 38.66015625,
      "height": 28.799999999999997,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 69369,
      "version": 2,
      "versionNonce": 708444986,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959747,
      "containerId": null,
      "originalText": "WB",
      "rawText": "WB",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wbmux:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:wbmux",
          "role": "text"
        }
      },
      "index": "b1R"
    },
    {
      "text": "0",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "hOHS1JUD",
      "type": "text",
      "x": 2557,
      "y": 606.25,
      "width": 7.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 56707,
      "version": 2,
      "versionNonce": 818308454,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959747,
      "containerId": null,
      "originalText": "0",
      "rawText": "0",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wbmux:port:alu",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:wbmux",
          "role": "text"
        }
      },
      "index": "b1S"
    },
    {
      "text": "1",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "Ov0hTOiF",
      "type": "text",
      "x": 2557,
      "y": 706.25,
      "width": 7.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 113,
      "version": 2,
      "versionNonce": 1900645370,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959747,
      "containerId": null,
      "originalText": "1",
      "rawText": "1",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wbmux:port:mem",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:wbmux",
          "role": "text"
        }
      },
      "index": "b1T"
    },
    {
      "text": "sel",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "5wGbkE9g",
      "type": "text",
      "x": 2596.0517578125,
      "y": 594,
      "width": 17.896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 165,
      "version": 3,
      "versionNonce": 621603700,
      "updated": 1792161397466,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959748,
      "containerId": null,
      "originalText": "sel",
      "rawText": "sel",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wbmux:port:sel",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:wbmux",
          "role": "text"
        }
      },
      "index": "b1U"
    },
    {
      "id": "I31cGUxh",
      "type": "rectangle",
      "x": 2730,
      "y": 820,
      "width": 145,
      "height": 110,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "#f0fdfa",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 6,
        "roundType": "arc"
      },
      "seed": 65484,
      "version": 2,
      "versionNonce": 1726610618,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "PkCUjm53",
          "type": "arrow"
        },
        {
          "id": "oCXi6yZy",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959748,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "retire",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:retire",
          "role": "body"
        }
      },
      "index": "b1V"
    },
    {
      "text": "WB rd",
      "fontSize": 22,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "JUPGT0ta",
      "type": "text",
      "x": 2771.94384765625,
      "y": 861.25,
      "width": 61.1123046875,
      "height": 26.4,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 39767,
      "version": 3,
      "versionNonce": 631806615,
      "updated": 1792162080524,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959749,
      "containerId": null,
      "originalText": "WB rd",
      "rawText": "WB rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "retire:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:retire",
          "role": "text"
        }
      },
      "index": "b1W"
    },
    {
      "id": "gZ7deTRP",
      "type": "rectangle",
      "x": 560,
      "y": 1280,
      "width": 460,
      "height": 100,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "#fff7ed",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 6,
        "roundType": "arc"
      },
      "seed": 71656,
      "version": 3,
      "versionNonce": 78946014,
      "updated": 1792161830563,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "eNuL3zCW",
          "type": "arrow"
        },
        {
          "id": "5aWAjEla",
          "type": "arrow"
        },
        {
          "id": "5KYFChTs",
          "type": "arrow"
        },
        {
          "id": "QiMUXs0X",
          "type": "arrow"
        },
        {
          "id": "UcachPP4",
          "type": "arrow"
        },
        {
          "id": "zmRE0G9O",
          "type": "arrow"
        },
        {
          "id": "twdDZZ4r",
          "type": "arrow"
        },
        {
          "id": "1XUNqqH9",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959749,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "hazard",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:hazard",
          "role": "body"
        }
      },
      "index": "b1X"
    },
    {
      "text": "INTERLOCK + FLUSH",
      "fontSize": 26,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "moPlHbfT",
      "type": "text",
      "x": 658.16552734375,
      "y": 1313.75,
      "width": 263.6689453125,
      "height": 31.2,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 83143,
      "version": 2,
      "versionNonce": 1494701862,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959749,
      "containerId": null,
      "originalText": "INTERLOCK + FLUSH",
      "rawText": "INTERLOCK + FLUSH",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "hazard:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:hazard",
          "role": "text"
        }
      },
      "index": "b1Y"
    },
    {
      "text": "rs1/rs2",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "8q8NIq3d",
      "type": "text",
      "x": 630.60693359375,
      "y": 1285,
      "width": 42.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 50705,
      "version": 2,
      "versionNonce": 1745458746,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959749,
      "containerId": null,
      "originalText": "rs1/rs2",
      "rawText": "rs1/rs2",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "hazard:port:ids",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:hazard",
          "role": "text"
        }
      },
      "index": "b1Z"
    },
    {
      "text": "rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "nj64QH7S",
      "type": "text",
      "x": 806.77587890625,
      "y": 1285,
      "width": 12.4482421875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 67012,
      "version": 2,
      "versionNonce": 665682534,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959750,
      "containerId": null,
      "originalText": "rd",
      "rawText": "rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "hazard:port:ex",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:hazard",
          "role": "text"
        }
      },
      "index": "b1a"
    },
    {
      "text": "MemRead",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "TbbI7rYt",
      "type": "text",
      "x": 918.71044921875,
      "y": 1285,
      "width": 64.5791015625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 33699,
      "version": 2,
      "versionNonce": 363773690,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959750,
      "containerId": null,
      "originalText": "MemRead",
      "rawText": "MemRead",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "hazard:port:read",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:hazard",
          "role": "text"
        }
      },
      "index": "b1b"
    },
    {
      "text": "taken",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "iif3aHzO",
      "type": "text",
      "x": 772.8759765625,
      "y": 1357.5,
      "width": 34.248046875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 25135,
      "version": 2,
      "versionNonce": 1893483942,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959750,
      "containerId": null,
      "originalText": "taken",
      "rawText": "taken",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "hazard:port:taken",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:hazard",
          "role": "text"
        }
      },
      "index": "b1c"
    },
    {
      "id": "z7YyMBDe",
      "type": "rectangle",
      "x": 1280,
      "y": 1280,
      "width": 500,
      "height": 100,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "#faf5ff",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 6,
        "roundType": "arc"
      },
      "seed": 7274,
      "version": 3,
      "versionNonce": 183426404,
      "updated": 1792161830563,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [
        {
          "id": "AsAbmlKl",
          "type": "arrow"
        },
        {
          "id": "gXGCrn8b",
          "type": "arrow"
        },
        {
          "id": "gIeyRcZt",
          "type": "arrow"
        },
        {
          "id": "B6Naxv8B",
          "type": "arrow"
        },
        {
          "id": "9wB7drvG",
          "type": "arrow"
        },
        {
          "id": "C8cFkKIy",
          "type": "arrow"
        },
        {
          "id": "KQ5glvkW",
          "type": "arrow"
        }
      ],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959751,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward",
          "role": "body"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:forward",
          "role": "body"
        }
      },
      "index": "b1d"
    },
    {
      "text": "FORWARDING UNIT",
      "fontSize": 27,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "HDkhPSmx",
      "type": "text",
      "x": 1401.756591796875,
      "y": 1313.125,
      "width": 256.48681640625,
      "height": 32.4,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 11544,
      "version": 2,
      "versionNonce": 97558758,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959751,
      "containerId": null,
      "originalText": "FORWARDING UNIT",
      "rawText": "FORWARDING UNIT",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward:label",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:forward",
          "role": "text"
        }
      },
      "index": "b1e"
    },
    {
      "text": "EX rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "RQMG3bIn",
      "type": "text",
      "x": 1737.986328125,
      "y": 1291.25,
      "width": 35.013671875,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 75770,
      "version": 2,
      "versionNonce": 1974651002,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959751,
      "containerId": null,
      "originalText": "EX rd",
      "rawText": "EX rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward:port:ex",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:forward",
          "role": "text"
        }
      },
      "index": "b1f"
    },
    {
      "text": "we",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "X8RAjPFR",
      "type": "text",
      "x": 1755.103515625,
      "y": 1311.25,
      "width": 17.896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 78920,
      "version": 2,
      "versionNonce": 169317414,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959752,
      "containerId": null,
      "originalText": "we",
      "rawText": "we",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward:port:ex_ctl",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:forward",
          "role": "text"
        }
      },
      "index": "b1g"
    },
    {
      "text": "WB rd",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "aEvQ5ZAM",
      "type": "text",
      "x": 1734.1103515625,
      "y": 1336.25,
      "width": 38.8896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 1688,
      "version": 2,
      "versionNonce": 1945610554,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959752,
      "containerId": null,
      "originalText": "WB rd",
      "rawText": "WB rd",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward:port:wb",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:forward",
          "role": "text"
        }
      },
      "index": "b1h"
    },
    {
      "text": "we",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "aTCSxrjG",
      "type": "text",
      "x": 1755.103515625,
      "y": 1361.25,
      "width": 17.896484375,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 22437,
      "version": 2,
      "versionNonce": 664674150,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959752,
      "containerId": null,
      "originalText": "we",
      "rawText": "we",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward:port:wb_ctl",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:forward",
          "role": "text"
        }
      },
      "index": "b1i"
    },
    {
      "text": "rs1/rs2",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "lbksDAVa",
      "type": "text",
      "x": 1287,
      "y": 1321.25,
      "width": 42.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 20567,
      "version": 2,
      "versionNonce": 1080193530,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959753,
      "containerId": null,
      "originalText": "rs1/rs2",
      "rawText": "rs1/rs2",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward:port:rs",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:forward",
          "role": "text"
        }
      },
      "index": "b1j"
    },
    {
      "text": "FwdA",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "vlpxOMUV",
      "type": "text",
      "x": 1387.10693359375,
      "y": 1285,
      "width": 35.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 33439,
      "version": 2,
      "versionNonce": 1118913190,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959753,
      "containerId": null,
      "originalText": "FwdA",
      "rawText": "FwdA",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward:port:a",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:forward",
          "role": "text"
        }
      },
      "index": "b1k"
    },
    {
      "text": "FwdB",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "kDi5IT0z",
      "type": "text",
      "x": 1637.10693359375,
      "y": 1285,
      "width": 35.7861328125,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 71564,
      "version": 2,
      "versionNonce": 1844847290,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959753,
      "containerId": null,
      "originalText": "FwdB",
      "rawText": "FwdB",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward:port:b",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:forward",
          "role": "text"
        }
      },
      "index": "b1l"
    },
    {
      "id": "NIBASmFf",
      "type": "rectangle",
      "x": 50,
      "y": 1470,
      "width": 2870,
      "height": 300,
      "angle": 0,
      "strokeColor": "#d8e1ed",
      "backgroundColor": "#f8fafc",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": {
        "type": 3,
        "value": 10,
        "roundType": "arc"
      },
      "seed": 90863,
      "version": 2,
      "versionNonce": 771620326,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959753,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "notes",
          "role": "container"
        },
        "isContainer": true
      },
      "index": "b1m"
    },
    {
      "id": "Y0gyaj5H",
      "type": "rectangle",
      "x": 50,
      "y": 1470,
      "width": 6,
      "height": 300,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "#b45309",
      "fillStyle": "solid",
      "strokeWidth": 1.5,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 85370,
      "version": 2,
      "versionNonce": 928365434,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959754,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "notes:stripe",
          "role": "body"
        }
      },
      "index": "b1n"
    },
    {
      "text": "HAZARD CONTRACT",
      "fontSize": 27,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "GuBOfCuu",
      "type": "text",
      "x": 74,
      "y": 1490,
      "width": 268.4970703125,
      "height": 32.4,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 87847,
      "version": 2,
      "versionNonce": 1586581798,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959754,
      "containerId": null,
      "originalText": "HAZARD CONTRACT",
      "rawText": "HAZARD CONTRACT",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "notes:title",
          "role": "text"
        }
      },
      "index": "b1o"
    },
    {
      "text": "00 = register   |   01 = MEM/WB result   |   10 = EX/MEM ALU result (not a pending load)",
      "fontSize": 25,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "4aar1aug",
      "type": "text",
      "x": 85,
      "y": 1540,
      "width": 973.828125,
      "height": 30,
      "angle": 0,
      "strokeColor": "#17324d",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 56929,
      "version": 2,
      "versionNonce": 180632634,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959754,
      "containerId": null,
      "originalText": "00 = register   |   01 = MEM/WB result   |   10 = EX/MEM ALU result (not a pending load)",
      "rawText": "00 = register   |   01 = MEM/WB result   |   10 = EX/MEM ALU result (not a pending load)",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "note1",
          "role": "text"
        }
      },
      "index": "b1p"
    },
    {
      "text": "Load-use holds PC + IF/ID and bubbles ID/EX. EX-taken branch redirects PC and flushes IF/ID + ID/EX through the interlock.",
      "fontSize": 23,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "p6MB01yj",
      "type": "text",
      "x": 85,
      "y": 1590,
      "width": 1274.5908203125,
      "height": 27.599999999999998,
      "angle": 0,
      "strokeColor": "#17324d",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 91984,
      "version": 2,
      "versionNonce": 534264934,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959755,
      "containerId": null,
      "originalText": "Load-use holds PC + IF/ID and bubbles ID/EX. EX-taken branch redirects PC and flushes IF/ID + ID/EX through the interlock.",
      "rawText": "Load-use holds PC + IF/ID and bubbles ID/EX. EX-taken branch redirects PC and flushes IF/ID + ID/EX through the interlock.",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "note2",
          "role": "text"
        }
      },
      "index": "b1q"
    },
    {
      "text": "Teaching subset: ALU / load / store / BEQ; static not-taken, separate I/D memories. No JAL, CSR, traps or MUL/DIV implementation.",
      "fontSize": 21,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "zDQrWUK0",
      "type": "text",
      "x": 85,
      "y": 1640,
      "width": 1230.181640625,
      "height": 25.2,
      "angle": 0,
      "strokeColor": "#64748b",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 36993,
      "version": 2,
      "versionNonce": 371500282,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959755,
      "containerId": null,
      "originalText": "Teaching subset: ALU / load / store / BEQ; static not-taken, separate I/D memories. No JAL, CSR, traps or MUL/DIV implementation.",
      "rawText": "Teaching subset: ALU / load / store / BEQ; static not-taken, separate I/D memories. No JAL, CSR, traps or MUL/DIV implementation.",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "note3",
          "role": "text"
        }
      },
      "index": "b1r"
    },
    {
      "text": "BLUE  data        PURPLE  bypass / writeback        AMBER DASH  control        TEAL  registered state / memory",
      "fontSize": 23,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "XROn0H7m",
      "type": "text",
      "x": 85,
      "y": 1690,
      "width": 1129.95361328125,
      "height": 27.599999999999998,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 44431,
      "version": 2,
      "versionNonce": 1201651622,
      "updated": 1792160959782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959756,
      "containerId": null,
      "originalText": "BLUE  data        PURPLE  bypass / writeback        AMBER DASH  control        TEAL  registered state / memory",
      "rawText": "BLUE  data        PURPLE  bypass / writeback        AMBER DASH  control        TEAL  registered state / memory",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "legend",
          "role": "text"
        }
      },
      "index": "b1s"
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.018000000000029104
        ],
        [
          16,
          -21.01800000000003
        ],
        [
          55,
          -21.01800000000003
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "gDo3FgMn",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "9NPx3ltI",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.3
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "f9x2CgGD",
      "type": "arrow",
      "x": 225,
      "y": 660.018,
      "width": 55,
      "height": 21.01800000000003,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 1658,
      "version": 3,
      "versionNonce": 1580251514,
      "updated": 1792160959789,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959756,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc_imem",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b1t",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.018000000000029104
        ],
        [
          16,
          -267.51800000000003
        ],
        [
          60,
          -267.50750000000005
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "gDo3FgMn",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "72xk5Zon",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.5
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "sSMAH8eo",
      "type": "arrow",
      "x": 225,
      "y": 660.018,
      "width": 60,
      "height": 267.51800000000003,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 17930,
      "version": 3,
      "versionNonce": 1502575162,
      "updated": 1792160959789,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959756,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc_inc",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b1u",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.010499999999979082
        ],
        [
          16,
          -68.51049999999998
        ],
        [
          -356,
          -68.51049999999998
        ],
        [
          -356,
          -12.510499999999979
        ],
        [
          -340,
          -12.510499999999979
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "72xk5Zon",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "OiRSfOJq",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.25
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "5HFI2OwA",
      "type": "arrow",
      "x": 430,
      "y": 392.5105,
      "width": 372,
      "height": 68.51049999999998,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 98638,
      "version": 3,
      "versionNonce": 618144506,
      "updated": 1792160959789,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959757,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc_seq",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b1v",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          -0.009999999999990905,
          16
        ],
        [
          -61.00999999999999,
          16
        ],
        [
          -61.00999999999999,
          175
        ],
        [
          -45.00999999999999,
          175.01800000000003
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "OiRSfOJq",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          1
        ]
      },
      "endBinding": {
        "elementId": "gDo3FgMn",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.5
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "VW4fJOUf",
      "type": "arrow",
      "x": 140.01,
      "y": 485,
      "width": 61.00999999999999,
      "height": 175.01800000000003,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 31720,
      "version": 3,
      "versionNonce": 2056106938,
      "updated": 1792160959789,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959757,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "next_pc",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b1w",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.018000000000029104
        ],
        [
          16,
          -36.218000000000075
        ],
        [
          85,
          -36.218000000000075
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "9NPx3ltI",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "uD9EwiAM",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.38
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "qNjLnpUH",
      "type": "arrow",
      "x": 430,
      "y": 675.018,
      "width": 85,
      "height": 36.218000000000075,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 41610,
      "version": 3,
      "versionNonce": 1288907898,
      "updated": 1792160959790,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959757,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "inst_latch",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b1x",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.018000000000029104
        ],
        [
          16,
          -196.01800000000003
        ],
        [
          290,
          -196.01800000000003
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "gDo3FgMn",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "uD9EwiAM",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.15
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "Pydlp8xP",
      "type": "arrow",
      "x": 225,
      "y": 660.018,
      "width": 290,
      "height": 196.01800000000003,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 59005,
      "version": 3,
      "versionNonce": 1366003002,
      "updated": 1792160959790,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959757,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc_latch",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b1y",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          -276.29999999999995
        ],
        [
          70,
          -276.29049999999995
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "uD9EwiAM",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.38
        ]
      },
      "endBinding": {
        "elementId": "JtAsLRlW",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.5
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "mqwzqZ19",
      "type": "arrow",
      "x": 605,
      "y": 638.8,
      "width": 70,
      "height": 276.29999999999995,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 42119,
      "version": 3,
      "versionNonce": 230282746,
      "updated": 1792160959790,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959758,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "decode_inst",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b1z",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          -114.79999999999995
        ],
        [
          210,
          -114.79999999999995
        ],
        [
          210.02700000000004,
          -98.79999999999995
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "uD9EwiAM",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.38
        ]
      },
      "endBinding": {
        "elementId": "Ci9XxGBw",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "G7JK65WS",
      "type": "arrow",
      "x": 605,
      "y": 638.8,
      "width": 210.02700000000004,
      "height": 114.79999999999995,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 10801,
      "version": 3,
      "versionNonce": 1656817338,
      "updated": 1792160959790,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959758,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "read_addr",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b20",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          331.20000000000005
        ],
        [
          145,
          331.20900000000006
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "uD9EwiAM",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.38
        ]
      },
      "endBinding": {
        "elementId": "otHClNTR",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.5
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "iphC33F5",
      "type": "arrow",
      "x": 605,
      "y": 638.8,
      "width": 145,
      "height": 331.20900000000006,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 50651,
      "version": 3,
      "versionNonce": 421797754,
      "updated": 1792160959790,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959758,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imm_inst",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b21",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          485,
          0
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "uD9EwiAM",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.15
        ]
      },
      "endBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.15
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "0xSLvgbH",
      "type": "arrow",
      "x": 605,
      "y": 464,
      "width": 485,
      "height": 0,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 98143,
      "version": 3,
      "versionNonce": 1831215162,
      "updated": 1792160959790,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959758,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "id_pc",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b22",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          150
        ],
        [
          140,
          150
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "Ci9XxGBw",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.3
        ]
      },
      "endBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.55
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "vmAC29Nz",
      "type": "arrow",
      "x": 950,
      "y": 618,
      "width": 140,
      "height": 150,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 54440,
      "version": 3,
      "versionNonce": 447351034,
      "updated": 1792160959792,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959758,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "read_a",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b23",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          26,
          0
        ],
        [
          26,
          170
        ],
        [
          140,
          169.9999999999999
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "Ci9XxGBw",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.72
        ]
      },
      "endBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.72
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "gjdqm2qt",
      "type": "arrow",
      "x": 950,
      "y": 727.2,
      "width": 140,
      "height": 170,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 98748,
      "version": 5,
      "versionNonce": 52676986,
      "updated": 1792161830805,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959758,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "read_b",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b24",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          16
        ],
        [
          199,
          16
        ],
        [
          199,
          608.8
        ],
        [
          215,
          608.8
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "JtAsLRlW",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.88
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "iths4XL8",
      "type": "arrow",
      "x": 875,
      "y": 410,
      "width": 215,
      "height": 608.8,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 52364,
      "version": 3,
      "versionNonce": 937661050,
      "updated": 1792160959793,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959758,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "id_rd",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b25",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          -214
        ],
        [
          80,
          -214
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.55
        ]
      },
      "endBinding": {
        "elementId": "EUNvJS1m",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.2
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "ECQY9lyq",
      "type": "arrow",
      "x": 1180,
      "y": 768,
      "width": 80,
      "height": 214,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 56320,
      "version": 3,
      "versionNonce": 159331130,
      "updated": 1792160959793,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959758,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fwd_a_reg",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b26",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          1.1368683772161603e-13
        ],
        [
          16,
          -43.19999999999993
        ],
        [
          80,
          -43.19999999999993
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.72
        ]
      },
      "endBinding": {
        "elementId": "l9evpEHs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.2
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "KdLmJLKR",
      "type": "arrow",
      "x": 1180,
      "y": 897.1999999999999,
      "width": 80,
      "height": 43.200000000000045,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 79727,
      "version": 3,
      "versionNonce": 275299322,
      "updated": 1792160959793,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959759,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fwd_b_reg",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b27",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          265,
          -0.01700000000005275
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "EUNvJS1m",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "h3i0v3id",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.2
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "dx8SRQwx",
      "type": "arrow",
      "x": 1370,
      "y": 605.017,
      "width": 265,
      "height": 0.01700000000005275,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 75267,
      "version": 3,
      "versionNonce": 983772346,
      "updated": 1792160959793,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959759,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "alu_a",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b28",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.01700000000005275
        ],
        [
          16,
          -76.26700000000005
        ],
        [
          120,
          -76.26700000000005
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "l9evpEHs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "hEm4s7Bs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.25
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "UdHgQW7G",
      "type": "arrow",
      "x": 1370,
      "y": 905.017,
      "width": 120,
      "height": 76.26700000000005,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 15952,
      "version": 3,
      "versionNonce": 1037141370,
      "updated": 1792160959794,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959759,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "src_reg",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b29",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.015499999999974534
        ],
        [
          16,
          -142.51549999999997
        ],
        [
          40,
          -142.51549999999997
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "hEm4s7Bs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "h3i0v3id",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.8
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "twVlscTM",
      "type": "arrow",
      "x": 1595,
      "y": 867.5155,
      "width": 40,
      "height": 142.51549999999997,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 33942,
      "version": 3,
      "versionNonce": 590792250,
      "updated": 1792160959794,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959759,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "alu_b",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2A",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.01999999999998181
        ],
        [
          16,
          102.98000000000002
        ],
        [
          90,
          102.98000000000002
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "h3i0v3id",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.55
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "rbwAP4Nz",
      "type": "arrow",
      "x": 1800,
      "y": 665.02,
      "width": 90,
      "height": 103,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 89352,
      "version": 3,
      "versionNonce": 1404432122,
      "updated": 1792160959794,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959759,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "result_pipe",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2B",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.01700000000005275
        ],
        [
          16,
          55.98299999999995
        ],
        [
          504,
          55.98299999999995
        ],
        [
          504,
          -7.817000000000007
        ],
        [
          520,
          -7.817000000000121
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "l9evpEHs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.72
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "ptyiq8SN",
      "type": "arrow",
      "x": 1370,
      "y": 905.017,
      "width": 520,
      "height": 63.80000000000007,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 43814,
      "version": 3,
      "versionNonce": 600965050,
      "updated": 1792160959794,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959759,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "store_pipe",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2C",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          710,
          0
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.88
        ]
      },
      "endBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.88
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "ugL8Kp2y",
      "type": "arrow",
      "x": 1180,
      "y": 1018.8,
      "width": 710,
      "height": 0,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 20571,
      "version": 3,
      "versionNonce": 1605236858,
      "updated": 1792160959794,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959759,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "rd_ex_pipe",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2D",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          -102
        ],
        [
          90,
          -102
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.55
        ]
      },
      "endBinding": {
        "elementId": "PX9apXAV",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.2
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "InAbTB8e",
      "type": "arrow",
      "x": 1980,
      "y": 768,
      "width": 90,
      "height": 102,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 59761,
      "version": 3,
      "versionNonce": 1460459834,
      "updated": 1792160959794,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959760,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "mem_addr",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2E",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          1.1368683772161603e-13
        ],
        [
          16,
          -98.59999999999991
        ],
        [
          90,
          -98.59999999999991
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.72
        ]
      },
      "endBinding": {
        "elementId": "PX9apXAV",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.72
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "xszZ1pkl",
      "type": "arrow",
      "x": 1980,
      "y": 897.1999999999999,
      "width": 90,
      "height": 98.60000000000002,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 98515,
      "version": 3,
      "versionNonce": 1766957562,
      "updated": 1792160959794,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959760,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "store_wdata",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2F",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          167.45000000000005
        ],
        [
          100,
          167.44999999999993
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "PX9apXAV",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.45
        ]
      },
      "endBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.72
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "H83lmECf",
      "type": "arrow",
      "x": 2270,
      "y": 729.75,
      "width": 100,
      "height": 167.45000000000005,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 23566,
      "version": 3,
      "versionNonce": 293556922,
      "updated": 1792160959795,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959760,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "load_pipe",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2G",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          26,
          0
        ],
        [
          26,
          118
        ],
        [
          374,
          118
        ],
        [
          374,
          0
        ],
        [
          390,
          0
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.55
        ]
      },
      "endBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.55
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "3apB4HfZ",
      "type": "arrow",
      "x": 1980,
      "y": 768,
      "width": 390,
      "height": 118,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 13818,
      "version": 4,
      "versionNonce": 33585353,
      "updated": 1792161830776,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959760,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "alu_pipe",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2H",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          390,
          0
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.88
        ]
      },
      "endBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.88
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "scT7OtYG",
      "type": "arrow",
      "x": 1980,
      "y": 1018.8,
      "width": 390,
      "height": 0,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 77063,
      "version": 3,
      "versionNonce": 1640066106,
      "updated": 1792160959795,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959760,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "rd_mem_pipe",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2I",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          -153
        ],
        [
          90,
          -153
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.55
        ]
      },
      "endBinding": {
        "elementId": "OS0QNaxX",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.25
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "m2MGhtYQ",
      "type": "arrow",
      "x": 2460,
      "y": 768,
      "width": 90,
      "height": 153,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 50618,
      "version": 3,
      "versionNonce": 1979438330,
      "updated": 1792160959795,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959760,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wb_alu",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2J",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          26,
          1.1368683772161603e-13
        ],
        [
          26,
          -182.19999999999993
        ],
        [
          90,
          -182.19999999999993
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.72
        ]
      },
      "endBinding": {
        "elementId": "OS0QNaxX",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.75
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "A7RvIysa",
      "type": "arrow",
      "x": 2460,
      "y": 897.1999999999999,
      "width": 90,
      "height": 182.20000000000005,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 67220,
      "version": 5,
      "versionNonce": 228624954,
      "updated": 1792161830808,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959760,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wb_mem",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2K",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          -143.79999999999995
        ],
        [
          270,
          -143.789
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.88
        ]
      },
      "endBinding": {
        "elementId": "I31cGUxh",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.5
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "PkCUjm53",
      "type": "arrow",
      "x": 2460,
      "y": 1018.8,
      "width": 270,
      "height": 143.79999999999995,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 11124,
      "version": 3,
      "versionNonce": 1781685882,
      "updated": 1792160959795,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959761,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "retire_rd",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2L",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          -125
        ],
        [
          320,
          -125
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.15
        ]
      },
      "endBinding": {
        "elementId": "8oC6OSwF",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.2
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "v7CpLDq4",
      "type": "arrow",
      "x": 1180,
      "y": 464,
      "width": 320,
      "height": 125,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 67365,
      "version": 3,
      "versionNonce": 538214202,
      "updated": 1792160959796,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959761,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch_pc",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2M",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.01700000000005275
        ],
        [
          16,
          -134.01700000000005
        ],
        [
          197.5,
          -134.01700000000005
        ],
        [
          197.5,
          -150.01700000000005
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "EUNvJS1m",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "8oC6OSwF",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.25,
          1
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "sXyktktI",
      "type": "arrow",
      "x": 1370,
      "y": 605.017,
      "width": 197.5,
      "height": 150.01700000000005,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 28399,
      "version": 3,
      "versionNonce": 1047824378,
      "updated": 1792160959796,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959761,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch_a",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2N",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          26,
          -0.01700000000005275
        ],
        [
          26,
          -374.01700000000005
        ],
        [
          332.5,
          -374.01700000000005
        ],
        [
          332.5,
          -450.01700000000005
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "l9evpEHs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "8oC6OSwF",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.75,
          1
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "rYOaHdIb",
      "type": "arrow",
      "x": 1370,
      "y": 905.017,
      "width": 332.5,
      "height": 450.01700000000005,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 30382,
      "version": 5,
      "versionNonce": 1413952250,
      "updated": 1792161830809,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959761,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch_b",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2O",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.009000000000014552
        ],
        [
          16,
          -4.408999999999992
        ],
        [
          160,
          -4.408999999999992
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "otHClNTR",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.81
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "yqzKtVT8",
      "type": "arrow",
      "x": 930,
      "y": 970.009,
      "width": 160,
      "height": 4.408999999999992,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 50319,
      "version": 3,
      "versionNonce": 1549422970,
      "updated": 1792160959796,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959761,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imm_latch",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2P",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          -114.79999999999995
        ],
        [
          479,
          -114.79999999999995
        ],
        [
          479,
          0
        ],
        [
          485,
          0
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "uD9EwiAM",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.38
        ]
      },
      "endBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.38
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "9NitmObv",
      "type": "arrow",
      "x": 605,
      "y": 638.8,
      "width": 485,
      "height": 114.79999999999995,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 73150,
      "version": 4,
      "versionNonce": 377146410,
      "updated": 1792161830777,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959761,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fields_latch",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2Q",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          18,
          0
        ],
        [
          18,
          224.39999999999998
        ],
        [
          290,
          224.39999999999998
        ],
        [
          290,
          -59.35000000000002
        ],
        [
          310,
          -59.35000000000002
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.81
        ]
      },
      "endBinding": {
        "elementId": "hEm4s7Bs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.75
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "rap2QDOI",
      "type": "arrow",
      "x": 1180,
      "y": 965.6,
      "width": 310,
      "height": 283.75,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 19406,
      "version": 4,
      "versionNonce": 628540493,
      "updated": 1792161830777,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959761,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imm_src",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2R",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          26,
          0
        ],
        [
          26,
          -539.6
        ],
        [
          320,
          -539.6
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.81
        ]
      },
      "endBinding": {
        "elementId": "8oC6OSwF",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.8
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "cPcmZtQE",
      "type": "arrow",
      "x": 1180,
      "y": 965.6,
      "width": 320,
      "height": 539.6,
      "angle": 0,
      "strokeColor": "#2563eb",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 9127,
      "version": 4,
      "versionNonce": 350718688,
      "updated": 1792161830777,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959761,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imm_branch",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2S",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.01999999999998181
        ],
        [
          16,
          460.98
        ],
        [
          -1704,
          460.98
        ],
        [
          -1704,
          150.98000000000002
        ],
        [
          -1804.5,
          150.98000000000002
        ],
        [
          -1804.5,
          134.98000000000002
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "OS0QNaxX",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "Ci9XxGBw",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.65,
          1
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "fQvlBr6A",
      "type": "arrow",
      "x": 2660,
      "y": 665.02,
      "width": 1820.5,
      "height": 461,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 73281,
      "version": 5,
      "versionNonce": 161137594,
      "updated": 1792161830810,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959762,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "writeback:rf.wd",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2T",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.01999999999998181
        ],
        [
          16,
          -331.02
        ],
        [
          -874,
          -331.02
        ],
        [
          -874,
          -161.01999999999998
        ],
        [
          -1416,
          -161.01999999999998
        ],
        [
          -1416,
          -60.01999999999998
        ],
        [
          -1400,
          -60.00299999999993
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "OS0QNaxX",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "EUNvJS1m",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.5
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "NJiZtwmY",
      "type": "arrow",
      "x": 2660,
      "y": 665.02,
      "width": 1432,
      "height": 331.02,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 72937,
      "version": 3,
      "versionNonce": 1251353914,
      "updated": 1792160959797,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959762,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "writeback:fa.wb",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2U",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          -0.01999999999998181
        ],
        [
          16,
          460.98
        ],
        [
          -1416,
          460.98
        ],
        [
          -1416,
          239.98000000000002
        ],
        [
          -1400,
          239.99700000000007
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "OS0QNaxX",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "l9evpEHs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.5
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "gyYdZlED",
      "type": "arrow",
      "x": 2660,
      "y": 665.02,
      "width": 1432,
      "height": 461,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 81542,
      "version": 3,
      "versionNonce": 902917626,
      "updated": 1792160959797,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959762,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "writeback:fb.wb",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2V",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          -424
        ],
        [
          -184,
          -424
        ],
        [
          -184,
          -304
        ],
        [
          -749,
          -304
        ],
        [
          -749,
          -112
        ],
        [
          -720,
          -112
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.55
        ]
      },
      "endBinding": {
        "elementId": "EUNvJS1m",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.8
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "KxWZVUdh",
      "type": "arrow",
      "x": 1980,
      "y": 768,
      "width": 765,
      "height": 424,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 16106,
      "version": 6,
      "versionNonce": 676333463,
      "updated": 1792162080525,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959762,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "ex_bypass:fa.ex",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2W",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          26,
          0
        ],
        [
          26,
          348
        ],
        [
          -726,
          348
        ],
        [
          -726,
          188
        ],
        [
          -720,
          188
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.55
        ]
      },
      "endBinding": {
        "elementId": "l9evpEHs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.8
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "1altFC77",
      "type": "arrow",
      "x": 1980,
      "y": 768,
      "width": 752,
      "height": 348,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 84259,
      "version": 5,
      "versionNonce": 607858783,
      "updated": 1792161897395,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959762,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "ex_bypass:fb.ex",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2X",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          -16
        ],
        [
          -1510.5,
          -16
        ],
        [
          -1510.5,
          140
        ],
        [
          -1504.5,
          140
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "8oC6OSwF",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.35,
          0
        ]
      },
      "endBinding": {
        "elementId": "OiRSfOJq",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.75
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "TvjJCsTx",
      "type": "arrow",
      "x": 1594.5,
      "y": 310,
      "width": 1510.5,
      "height": 156,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2.6,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 98377,
      "version": 4,
      "versionNonce": 572096196,
      "updated": 1792161830777,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959762,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "redirect",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2Y",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          -6
        ],
        [
          -1576,
          -6
        ],
        [
          -1575.99,
          35
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "8oC6OSwF",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          0
        ]
      },
      "endBinding": {
        "elementId": "OiRSfOJq",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "GPTUK7Ri",
      "type": "arrow",
      "x": 1716,
      "y": 310,
      "width": 1576,
      "height": 41,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 7200,
      "version": 5,
      "versionNonce": 398343290,
      "updated": 1792161830813,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959763,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pcsrc",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2Z",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          139,
          -0.009500000000002728
        ],
        [
          139,
          773.4905
        ],
        [
          183,
          773.4905
        ],
        [
          183,
          747.4905
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "JtAsLRlW",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "endBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.2,
          1
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "1LV6TPTr",
      "type": "arrow",
      "x": 925,
      "y": 362.5095,
      "width": 183,
      "height": 773.5,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 62110,
      "version": 9,
      "versionNonce": 742809830,
      "updated": 1792161897415,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959763,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "decode_control",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2a",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          26
        ],
        [
          746,
          26
        ],
        [
          746,
          0
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.2,
          1
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "7PxQ9BeL",
      "type": "arrow",
      "x": 1162,
      "y": 1110,
      "width": 746,
      "height": 26,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 30816,
      "version": 6,
      "versionNonce": 282846957,
      "updated": 1792161830777,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959763,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "mem_control",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2b",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          26
        ],
        [
          426,
          26
        ],
        [
          426,
          0
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.2,
          1
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "zzhwyEHU",
      "type": "arrow",
      "x": 1962,
      "y": 1110,
      "width": 426,
      "height": 26,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 16732,
      "version": 6,
      "versionNonce": 72496472,
      "updated": 1792161830778,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959763,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wb_control",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2c",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          26
        ],
        [
          457,
          26
        ],
        [
          457,
          -561
        ],
        [
          555.5,
          -561
        ],
        [
          555.5165,
          -545
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "h3i0v3id",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "viHDu4dC",
      "type": "arrow",
      "x": 1162,
      "y": 1110,
      "width": 555.5165,
      "height": 587,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 5812,
      "version": 7,
      "versionNonce": 1159783930,
      "updated": 1792161830814,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959763,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "alu_control",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2d",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          26
        ],
        [
          457,
          26
        ],
        [
          457,
          -639
        ],
        [
          614,
          -639
        ],
        [
          614,
          -727.5
        ],
        [
          608,
          -727.4855
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "8oC6OSwF",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.5
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "r4mihXKS",
      "type": "arrow",
      "x": 1162,
      "y": 1110,
      "width": 614,
      "height": 753.5,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 8132,
      "version": 7,
      "versionNonce": 986060474,
      "updated": 1792161830815,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959763,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "branch_control",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2e",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          26
        ],
        [
          380.5,
          26
        ],
        [
          380.5105000000001,
          -165
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "hEm4s7Bs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          1
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "DXGvQwea",
      "type": "arrow",
      "x": 1162,
      "y": 1110,
      "width": 380.5105000000001,
      "height": 191,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 43780,
      "version": 7,
      "versionNonce": 1309093754,
      "updated": 1792161830815,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959763,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "src_select",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2f",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          26
        ],
        [
          92,
          26
        ],
        [
          92,
          -511
        ],
        [
          208,
          -511
        ],
        [
          208.01999999999998,
          -495
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "PX9apXAV",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "FN4tCitD",
      "type": "arrow",
      "x": 1962,
      "y": 1110,
      "width": 208.01999999999998,
      "height": 537,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 78927,
      "version": 7,
      "versionNonce": 858206266,
      "updated": 1792161830815,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959763,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "dmem_control",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2g",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          26
        ],
        [
          92,
          26
        ],
        [
          92,
          -561
        ],
        [
          163,
          -561
        ],
        [
          163.01099999999997,
          -545
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "OS0QNaxX",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "dUkkvKNq",
      "type": "arrow",
      "x": 2442,
      "y": 1110,
      "width": 163.01099999999997,
      "height": 587,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 39936,
      "version": 7,
      "versionNonce": 503912698,
      "updated": 1792161830815,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959764,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wb_select",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2h",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          36
        ],
        [
          -1778,
          36
        ],
        [
          -1778,
          -349
        ],
        [
          -1762,
          -349
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "Ci9XxGBw",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.85
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "1lZXV8uW",
      "type": "arrow",
      "x": 2442,
      "y": 1110,
      "width": 1778,
      "height": 385,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 17041,
      "version": 7,
      "versionNonce": 225895617,
      "updated": 1792161897395,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959764,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wb_we",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2i",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          -0.014500000000225555,
          226
        ],
        [
          -1866.5145000000002,
          226
        ],
        [
          -1866.5145000000002,
          -104
        ],
        [
          -2041.5145000000002,
          -104
        ],
        [
          -2041.5145000000002,
          -130
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "I31cGUxh",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          1
        ]
      },
      "endBinding": {
        "elementId": "Ci9XxGBw",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.3,
          1
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "oCXi6yZy",
      "type": "arrow",
      "x": 2802.5145,
      "y": 930,
      "width": 2041.5145000000002,
      "height": 356,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 58660,
      "version": 7,
      "versionNonce": 1540707366,
      "updated": 1792161897416,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959764,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wb_wa",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2j",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          625.2
        ],
        [
          47,
          625.2
        ],
        [
          47,
          641.2
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "uD9EwiAM",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.38
        ]
      },
      "endBinding": {
        "elementId": "gZ7deTRP",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.2,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "eNuL3zCW",
      "type": "arrow",
      "x": 605,
      "y": 638.8,
      "width": 47,
      "height": 641.2,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 23975,
      "version": 3,
      "versionNonce": 1543991610,
      "updated": 1792160959802,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959764,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "hazard_id",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2k",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          26,
          0
        ],
        [
          26,
          245.20000000000005
        ],
        [
          -367,
          245.20000000000005
        ],
        [
          -367,
          261.20000000000005
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.88
        ]
      },
      "endBinding": {
        "elementId": "gZ7deTRP",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.55,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "5aWAjEla",
      "type": "arrow",
      "x": 1180,
      "y": 1018.8,
      "width": 393,
      "height": 261.20000000000005,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 8320,
      "version": 4,
      "versionNonce": 777586318,
      "updated": 1792161830778,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959764,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "hazard_ex",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2l",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          164
        ],
        [
          -211,
          164
        ],
        [
          -211,
          170
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "gZ7deTRP",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.85,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "1XUNqqH9",
      "type": "arrow",
      "x": 1162,
      "y": 1110,
      "width": 211,
      "height": 170,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 16613,
      "version": 6,
      "versionNonce": 209133842,
      "updated": 1792161830778,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959764,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "hazard_read",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2m",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          -6
        ],
        [
          -680,
          -6
        ],
        [
          -680,
          1086
        ],
        [
          -926,
          1086
        ],
        [
          -925.954,
          1070
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "8oC6OSwF",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          0
        ]
      },
      "endBinding": {
        "elementId": "gZ7deTRP",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          1
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "5KYFChTs",
      "type": "arrow",
      "x": 1716,
      "y": 310,
      "width": 926,
      "height": 1092,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 35959,
      "version": 5,
      "versionNonce": 448701050,
      "updated": 1792161830816,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959764,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "hazard_taken",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2n",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          -309,
          0
        ],
        [
          -309,
          -756
        ],
        [
          -400,
          -756
        ],
        [
          -399.98699999999997,
          -740
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "gZ7deTRP",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.3
        ]
      },
      "endBinding": {
        "elementId": "gDo3FgMn",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "QiMUXs0X",
      "type": "arrow",
      "x": 560,
      "y": 1310,
      "width": 400,
      "height": 756,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 98181,
      "version": 5,
      "versionNonce": 2121810746,
      "updated": 1792161830816,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959765,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pc_write",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2o",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          -61,
          0
        ],
        [
          -61,
          -1016
        ],
        [
          -27,
          -1016
        ],
        [
          -27,
          -1000
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "gZ7deTRP",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.7
        ]
      },
      "endBinding": {
        "elementId": "uD9EwiAM",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.2,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "UcachPP4",
      "type": "arrow",
      "x": 560,
      "y": 1350,
      "width": 61,
      "height": 1016,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 15986,
      "version": 3,
      "versionNonce": 324496634,
      "updated": 1792160959803,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959765,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "ifid_hold",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2p",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          6,
          0
        ],
        [
          6,
          -894
        ],
        [
          -389,
          -894
        ],
        [
          -389,
          -976
        ],
        [
          -433,
          -976
        ],
        [
          -433,
          -960
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "gZ7deTRP",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.3
        ]
      },
      "endBinding": {
        "elementId": "uD9EwiAM",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "zmRE0G9O",
      "type": "arrow",
      "x": 1020,
      "y": 1310,
      "width": 439,
      "height": 976,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 30284,
      "version": 5,
      "versionNonce": 313385440,
      "updated": 1792161897395,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959765,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "ifid_flush",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2q",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          26,
          0
        ],
        [
          26,
          -1016
        ],
        [
          142,
          -1016
        ],
        [
          142,
          -1000
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "gZ7deTRP",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.7
        ]
      },
      "endBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "twdDZZ4r",
      "type": "arrow",
      "x": 1020,
      "y": 1350,
      "width": 142,
      "height": 1016,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 84465,
      "version": 4,
      "versionNonce": 826488239,
      "updated": 1792161830779,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959765,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex_bubble",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2r",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          281.20000000000005
        ],
        [
          -200,
          281.20000000000005
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.88
        ]
      },
      "endBinding": {
        "elementId": "z7YyMBDe",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.2
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "AsAbmlKl",
      "type": "arrow",
      "x": 1980,
      "y": 1018.8,
      "width": 216,
      "height": 281.20000000000005,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 54399,
      "version": 3,
      "versionNonce": 251074362,
      "updated": 1792160959804,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959765,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward_ex",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2s",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          16,
          0
        ],
        [
          16,
          326.20000000000005
        ],
        [
          -680,
          326.20000000000005
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.88
        ]
      },
      "endBinding": {
        "elementId": "z7YyMBDe",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.65
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "gXGCrn8b",
      "type": "arrow",
      "x": 2460,
      "y": 1018.8,
      "width": 696,
      "height": 326.20000000000005,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 10698,
      "version": 3,
      "versionNonce": 1698963450,
      "updated": 1792160959804,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959765,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward_wb",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2t",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          210
        ],
        [
          -182,
          210
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "d5OB4XeQ",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "z7YyMBDe",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.4
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "C8cFkKIy",
      "type": "arrow",
      "x": 1962,
      "y": 1110,
      "width": 182,
      "height": 210,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 63220,
      "version": 6,
      "versionNonce": 444341704,
      "updated": 1792161830779,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959765,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward_ex_we",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2u",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          260
        ],
        [
          -662,
          260
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "X44pjpPY",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.8,
          1
        ]
      },
      "endBinding": {
        "elementId": "z7YyMBDe",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.9
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "KQ5glvkW",
      "type": "arrow",
      "x": 2442,
      "y": 1110,
      "width": 662,
      "height": 260,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 76610,
      "version": 6,
      "versionNonce": 86809003,
      "updated": 1792161830779,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959766,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward_wb_we",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2v",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          6,
          0
        ],
        [
          6,
          691.2
        ],
        [
          100,
          691.21
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "azKpcPdN",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          1,
          0.38
        ]
      },
      "endBinding": {
        "elementId": "z7YyMBDe",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0,
          0.5
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "gIeyRcZt",
      "type": "arrow",
      "x": 1180,
      "y": 638.8,
      "width": 100,
      "height": 691.21,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 36734,
      "version": 5,
      "versionNonce": 599772154,
      "updated": 1792161830817,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959766,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "forward_rs",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2w",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          -766
        ],
        [
          -90,
          -766
        ],
        [
          -89.98900000000003,
          -760
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "z7YyMBDe",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.25,
          0
        ]
      },
      "endBinding": {
        "elementId": "EUNvJS1m",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "B6Naxv8B",
      "type": "arrow",
      "x": 1405,
      "y": 1280,
      "width": 90,
      "height": 766,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 22399,
      "version": 5,
      "versionNonce": 1889025210,
      "updated": 1792161830817,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959766,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fwd_sel_a",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2x",
      "moveMidPointsWithElement": false
    },
    {
      "points": [
        [
          0,
          0
        ],
        [
          0,
          -16
        ],
        [
          -279,
          -16
        ],
        [
          -279,
          -476
        ],
        [
          -340,
          -476
        ],
        [
          -339.98900000000003,
          -460
        ]
      ],
      "elbowed": false,
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "z7YyMBDe",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.75,
          0
        ]
      },
      "endBinding": {
        "elementId": "l9evpEHs",
        "focus": 0,
        "gap": 1,
        "mode": "inside",
        "fixedPoint": [
          0.5,
          0
        ]
      },
      "startArrowhead": null,
      "endArrowhead": "triangle",
      "id": "9wB7drvG",
      "type": "arrow",
      "x": 1655,
      "y": 1280,
      "width": 340,
      "height": 476,
      "angle": 0,
      "strokeColor": "#b45309",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 72741,
      "version": 5,
      "versionNonce": 312776058,
      "updated": 1792161830817,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959766,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "fwd_sel_b",
          "role": "edge"
        },
        "lineCrossings": "gap",
        "lineJumpPriority": 0
      },
      "index": "b2y",
      "moveMidPointsWithElement": false
    },
    {
      "text": "immediate",
      "fontSize": 18,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "eE1SoAWh",
      "type": "text",
      "x": 1283,
      "y": 1066.55,
      "width": 83.0302734375,
      "height": 21.599999999999998,
      "angle": 0,
      "strokeColor": "#64748b",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 84268,
      "version": 4,
      "versionNonce": 938490309,
      "updated": 1792161897395,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959767,
      "containerId": null,
      "originalText": "immediate",
      "rawText": "immediate",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imm_src:label",
          "role": "text"
        }
      },
      "index": "b2z"
    },
    {
      "text": "sign-extended",
      "fontSize": 18,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "QqSZyu2c",
      "type": "text",
      "x": 1296.4599609375,
      "y": 395.5,
      "width": 113.080078125,
      "height": 21.599999999999998,
      "angle": 0,
      "strokeColor": "#64748b",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 49490,
      "version": 3,
      "versionNonce": 208503872,
      "updated": 1792161830781,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959767,
      "containerId": null,
      "originalText": "sign-extended",
      "rawText": "sign-extended",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "imm_branch:label",
          "role": "text"
        }
      },
      "index": "b30"
    },
    {
      "text": "branch target",
      "fontSize": 18,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "dQetZM4e",
      "type": "text",
      "x": 786.216796875,
      "y": 263.5,
      "width": 106.06640625,
      "height": 21.599999999999998,
      "angle": 0,
      "strokeColor": "#64748b",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 45500,
      "version": 3,
      "versionNonce": 739609878,
      "updated": 1792161830781,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959768,
      "containerId": null,
      "originalText": "branch target",
      "rawText": "branch target",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "redirect:label",
          "role": "text"
        }
      },
      "index": "b32"
    },
    {
      "text": "PCSrc",
      "fontSize": 18,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "VoVU9VcG",
      "type": "text",
      "x": 901.99755859375,
      "y": 253.5,
      "width": 52.0048828125,
      "height": 21.599999999999998,
      "angle": 0,
      "strokeColor": "#64748b",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 96788,
      "version": 3,
      "versionNonce": 587546601,
      "updated": 1792161830782,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792160959769,
      "containerId": null,
      "originalText": "PCSrc",
      "rawText": "PCSrc",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "pcsrc:label",
          "role": "text"
        }
      },
      "index": "b33"
    },
    {
      "text": "D",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "xOKK76oE",
      "type": "text",
      "x": 1102.94482421875,
      "y": 1087.5,
      "width": 10.1103515625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 55694,
      "version": 2,
      "versionNonce": 649854970,
      "updated": 1792161830799,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792161830774,
      "containerId": null,
      "originalText": "D",
      "rawText": "D",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "idex:port:ctl_d",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:idex",
          "role": "text"
        }
      },
      "index": "b34"
    },
    {
      "text": "D",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "e6xFQgjX",
      "type": "text",
      "x": 1902.94482421875,
      "y": 1087.5,
      "width": 10.1103515625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 32491,
      "version": 2,
      "versionNonce": 855610534,
      "updated": 1792161830799,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792161830775,
      "containerId": null,
      "originalText": "D",
      "rawText": "D",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "exmem:port:ctl_d",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:exmem",
          "role": "text"
        }
      },
      "index": "b35"
    },
    {
      "text": "D",
      "fontSize": 14,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "BQdz9PN5",
      "type": "text",
      "x": 2382.94482421875,
      "y": 1087.5,
      "width": 10.1103515625,
      "height": 16.8,
      "angle": 0,
      "strokeColor": "#0f766e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 98130,
      "version": 2,
      "versionNonce": 770568378,
      "updated": 1792161830799,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792161830776,
      "containerId": null,
      "originalText": "D",
      "rawText": "D",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "memwb:port:ctl_d",
          "role": "text"
        },
        "agentPrimitive": {
          "instanceId": "advanced-pipeline:memwb",
          "role": "text"
        }
      },
      "index": "b36"
    },
    {
      "text": "WB data",
      "fontSize": 18,
      "fontFamily": "Liberation Sans",
      "textAlign": "left",
      "verticalAlign": "top",
      "id": "vZaoyjJW",
      "type": "text",
      "x": 2705,
      "y": 1080,
      "width": 69.029296875,
      "height": 21.599999999999998,
      "angle": 0,
      "strokeColor": "#7c3aed",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "roundness": null,
      "seed": 52444,
      "version": 2,
      "versionNonce": 1022918138,
      "updated": 1792162080533,
      "isDeleted": false,
      "groupIds": [],
      "boundElements": [],
      "link": null,
      "locked": false,
      "frameId": null,
      "hasTextLink": false,
      "created": 1792162080525,
      "containerId": null,
      "originalText": "WB data",
      "rawText": "WB data",
      "lineHeight": 1.2,
      "autoResize": true,
      "customData": {
        "agentDiagram": {
          "diagramId": "advanced-pipeline",
          "logicalId": "wbdata_caption",
          "role": "text"
        }
      },
      "index": "b37"
    }
  ],
  "appState": {
    "theme": "light",
    "viewBackgroundColor": "#FFFFFF",
    "currentItemStrokeColor": "#000000",
    "currentItemBackgroundColor": "transparent",
    "currentItemFillStyle": "hachure",
    "currentItemStickynoteStrokeColor": "#1e1e1e",
    "currentItemStrokeWidthKey": "medium",
    "currentItemStrokeVariability": "constant",
    "currentItemStrokeStyle": "solid",
    "currentItemRoughness": 1,
    "currentItemOpacity": 100,
    "currentItemFontFamily": 1,
    "currentItemFontSize": 20,
    "currentItemTextAlign": "left",
    "currentItemStartArrowhead": null,
    "currentItemEndArrowhead": "arrow",
    "currentItemArrowType": "round",
    "currentItemFrameRole": null,
    "scrollX": 438.25,
    "scrollY": 420.08856201171875,
    "zoom": {
      "value": 1
    },
    "currentItemRoundness": "sharp",
    "gridSize": 1,
    "gridStep": 5,
    "gridModeEnabled": false,
    "gridColor": {
      "Bold": "rgba(179, 179, 179, 0.5)",
      "Regular": "rgba(204, 204, 204, 0.5)"
    },
    "colorTopPicks": {
      "elementStroke": null,
      "elementBackground": null,
      "bucketFill": null,
      "stickyNoteStroke": null,
      "stickyNoteBackground": null
    },
    "fontTopPicks": null,
    "currentStrokeOptions": null,
    "frameRendering": {
      "enabled": true,
      "clip": true,
      "name": true,
      "outline": true,
      "markerName": true,
      "markerEnabled": true
    },
    "objectsSnapModeEnabled": false,
    "activeTool": {
      "type": "selection",
      "customType": null,
      "locked": false,
      "fromSelection": false,
      "lastActiveTool": null
    },
    "disableContextMenu": false,
    "bindingPreference": "enabled",
    "isMidpointSnappingEnabled": true,
    "boxSelectionMode": "contain",
    "inputDevice": "auto"
  },
  "files": {}
}
```
%%
