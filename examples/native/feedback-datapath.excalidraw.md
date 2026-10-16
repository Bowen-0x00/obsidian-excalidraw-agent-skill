---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'

# Excalidraw Data

## Text Elements
A 寄存器 ^jlYwqWqj

B 寄存器 ^e4aXNq26

MUX ^7rypRphE

ALU ^WZKU28cY

ACC ^TlyRES26

输出结果 ^R955pvQO

控制器 ^ghRAXMb7

教学示意：sel=0 选 A，sel=1 选 ACC.Q；en=1 时写 ACC。两条 Q 出线表示同一寄存值的两个去向。省略时钟、复位与运算码，不表示完整 RTL。 ^SncI0ym3

32 位累加数据通路：选择、运算与寄存反馈 ^v0hlNRso

32 bit ^jQEauxiv

32 bit ^VBQIbRiJ

32 bit ^Tuv2Wdd8

32 bit ^8JiRNgci

Q / 32 bit ^8fVyYbjG

Q 反馈 / 32 bit ^3Wj0xB6c

sel / 1 bit ^NfutqGxh

en / 1 bit ^0KS9F7fw

Q ^I8XfqqeT

Q ^wAPGuFqY

i0 ^spICeNNt

i1 ^JuR2tZeD

sel ^8pJTHBwR

y ^I45mCqyB

a ^2Tnx5f3b

b ^87y1td2z

y ^vNzf36bq

D ^EDKAQNDy

Q ^dkfWlgEf

en ^inY5zRxh

sel ^Q9ldyZdK

en ^Sv19v5z2


## Tags
%%
## Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.29.0-3",
	"elements": [
		{
			"id": "0JbSZOGD",
			"type": "rectangle",
			"x": 50,
			"y": 400,
			"width": 140,
			"height": 180,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": {
				"type": 3,
				"value": 5,
				"roundType": "arc"
			},
			"seed": 971,
			"version": 2,
			"versionNonce": 367269030,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "jlYwqWqj",
					"type": "text"
				},
				{
					"id": "85xEJy8w",
					"type": "arrow"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095746,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.a"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.a",
					"role": "body"
				}
			},
			"index": "a0"
		},
		{
			"text": "A 寄存器",
			"fontSize": 23,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "jlYwqWqj",
			"type": "text",
			"x": 73.54000854492188,
			"y": 475.625,
			"width": 92.91998291015625,
			"height": 28.75,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 1799,
			"version": 2,
			"versionNonce": 965832890,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095746,
			"containerId": "0JbSZOGD",
			"originalText": "A 寄存器",
			"rawText": "A 寄存器",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.a:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.a:label",
					"role": "label"
				}
			},
			"index": "a1"
		},
		{
			"id": "V4TaDvZz",
			"type": "ellipse",
			"x": 188,
			"y": 443,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#263746",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 84473,
			"version": 2,
			"versionNonce": 1996918758,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095746,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.a:port:Q"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.a:port:Q",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:a",
					"role": "decoration"
				}
			},
			"index": "a2"
		},
		{
			"id": "VMM3jM1k",
			"type": "rectangle",
			"x": 50,
			"y": 740,
			"width": 140,
			"height": 140,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": {
				"type": 3,
				"value": 5,
				"roundType": "arc"
			},
			"seed": 18109,
			"version": 2,
			"versionNonce": 1314343290,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "e4aXNq26",
					"type": "text"
				},
				{
					"id": "JruMkmS0",
					"type": "arrow"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095746,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.b"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.b",
					"role": "body"
				}
			},
			"index": "a3"
		},
		{
			"text": "B 寄存器",
			"fontSize": 23,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "e4aXNq26",
			"type": "text",
			"x": 74.00000762939453,
			"y": 795.625,
			"width": 91.99998474121094,
			"height": 28.75,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 58457,
			"version": 2,
			"versionNonce": 1555538726,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095747,
			"containerId": "VMM3jM1k",
			"originalText": "B 寄存器",
			"rawText": "B 寄存器",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.b:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.b:label",
					"role": "label"
				}
			},
			"index": "a4"
		},
		{
			"id": "cyEqCsxM",
			"type": "ellipse",
			"x": 188,
			"y": 808,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#263746",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 78652,
			"version": 2,
			"versionNonce": 644090426,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095747,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.b:port:Q"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.b:port:Q",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:b",
					"role": "decoration"
				}
			},
			"index": "a5"
		},
		{
			"id": "ivsV5ljg",
			"type": "rectangle",
			"x": 350,
			"y": 400,
			"width": 150,
			"height": 180,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": {
				"type": 3,
				"value": 5,
				"roundType": "arc"
			},
			"seed": 29012,
			"version": 2,
			"versionNonce": 1768181350,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "85xEJy8w",
					"type": "arrow"
				},
				{
					"id": "BvHm1K4T",
					"type": "arrow"
				},
				{
					"id": "wiL77g7r",
					"type": "arrow"
				},
				{
					"id": "bywBknqO",
					"type": "arrow"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095747,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux",
					"role": "container"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				},
				"isContainer": true
			},
			"index": "a6"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					150,
					28.80000000000001
				],
				[
					150,
					151.20000000000005
				],
				[
					0,
					180
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
			"id": "Ws6jta0M",
			"type": "line",
			"x": 350,
			"y": 400,
			"width": 150,
			"height": 180,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 61212,
			"version": 2,
			"versionNonce": 144356090,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095747,
			"polygon": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux:outline"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux:outline",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				}
			},
			"index": "a7"
		},
		{
			"text": "MUX",
			"fontSize": 23,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "7rypRphE",
			"type": "text",
			"x": 400.1025161743164,
			"y": 476.2,
			"width": 49.79496765136719,
			"height": 28.75,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 80301,
			"version": 2,
			"versionNonce": 1775866278,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095748,
			"containerId": null,
			"originalText": "MUX",
			"rawText": "MUX",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux:title"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux:title",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				}
			},
			"index": "a8"
		},
		{
			"id": "F0l1C9MF",
			"type": "ellipse",
			"x": 348,
			"y": 443,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#263746",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 36186,
			"version": 2,
			"versionNonce": 1736328122,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095748,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux:port:i0"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux:port:i0",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				}
			},
			"index": "a9"
		},
		{
			"id": "bbuhAy8h",
			"type": "ellipse",
			"x": 348,
			"y": 533,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#263746",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 31597,
			"version": 2,
			"versionNonce": 155479270,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095748,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux:port:i1"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux:port:i1",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				}
			},
			"index": "aA"
		},
		{
			"id": "HcZhZGLG",
			"type": "ellipse",
			"x": 423,
			"y": 398,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#263746",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 1423,
			"version": 2,
			"versionNonce": 1831976058,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095748,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux:port:sel"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux:port:sel",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				}
			},
			"index": "aB"
		},
		{
			"id": "1x1imIsK",
			"type": "ellipse",
			"x": 498,
			"y": 488,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#263746",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 81442,
			"version": 2,
			"versionNonce": 87154726,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095748,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux:port:y"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux:port:y",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				}
			},
			"index": "aC"
		},
		{
			"id": "jzCUXb1q",
			"type": "rectangle",
			"x": 700,
			"y": 400,
			"width": 180,
			"height": 180,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": {
				"type": 3,
				"value": 5,
				"roundType": "arc"
			},
			"seed": 67392,
			"version": 2,
			"versionNonce": 125312314,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "BvHm1K4T",
					"type": "arrow"
				},
				{
					"id": "JruMkmS0",
					"type": "arrow"
				},
				{
					"id": "pUI7K2OE",
					"type": "arrow"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095748,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.alu"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.alu",
					"role": "container"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:alu",
					"role": "decoration"
				},
				"isContainer": true
			},
			"index": "aD"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					180,
					39.60000000000002
				],
				[
					180,
					140.39999999999998
				],
				[
					0,
					180
				],
				[
					0,
					113.39999999999998
				],
				[
					41.39999999999998,
					90
				],
				[
					0,
					66.60000000000002
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
			"id": "OGulW1mj",
			"type": "line",
			"x": 700,
			"y": 400,
			"width": 180,
			"height": 180,
			"angle": 0,
			"strokeColor": "#1d4ed8",
			"backgroundColor": "#eff6ff",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 83854,
			"version": 2,
			"versionNonce": 1636756326,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095748,
			"polygon": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.alu:outline"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.alu:outline",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:alu",
					"role": "decoration"
				}
			},
			"index": "aE"
		},
		{
			"text": "ALU",
			"fontSize": 23,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "WZKU28cY",
			"type": "text",
			"x": 782.0095123291015,
			"y": 476.2,
			"width": 44.780975341796875,
			"height": 28.75,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 19443,
			"version": 2,
			"versionNonce": 1941202426,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095749,
			"containerId": null,
			"originalText": "ALU",
			"rawText": "ALU",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.alu:title"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.alu:title",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:alu",
					"role": "decoration"
				}
			},
			"index": "aF"
		},
		{
			"id": "06Jgh8kg",
			"type": "ellipse",
			"x": 698,
			"y": 443,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#1d4ed8",
			"backgroundColor": "#1d4ed8",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 90120,
			"version": 2,
			"versionNonce": 480808614,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095749,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.alu:port:a"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.alu:port:a",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:alu",
					"role": "decoration"
				}
			},
			"index": "aG"
		},
		{
			"id": "y7uqdTXI",
			"type": "ellipse",
			"x": 698,
			"y": 533,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#1d4ed8",
			"backgroundColor": "#1d4ed8",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 83022,
			"version": 2,
			"versionNonce": 1256822458,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095749,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.alu:port:b"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.alu:port:b",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:alu",
					"role": "decoration"
				}
			},
			"index": "aH"
		},
		{
			"id": "GIoplzli",
			"type": "ellipse",
			"x": 878,
			"y": 488,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#1d4ed8",
			"backgroundColor": "#1d4ed8",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 50959,
			"version": 2,
			"versionNonce": 1663814118,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095749,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.alu:port:y"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.alu:port:y",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:alu",
					"role": "decoration"
				}
			},
			"index": "aI"
		},
		{
			"id": "Y2vS7jlL",
			"type": "rectangle",
			"x": 1080,
			"y": 400,
			"width": 140,
			"height": 180,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": {
				"type": 3,
				"value": 5,
				"roundType": "arc"
			},
			"seed": 5471,
			"version": 2,
			"versionNonce": 230338426,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "TlyRES26",
					"type": "text"
				},
				{
					"id": "pUI7K2OE",
					"type": "arrow"
				},
				{
					"id": "TaaNGtRb",
					"type": "arrow"
				},
				{
					"id": "wiL77g7r",
					"type": "arrow"
				},
				{
					"id": "56wFxZOl",
					"type": "arrow"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095749,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.acc"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.acc",
					"role": "body"
				}
			},
			"index": "aJ"
		},
		{
			"text": "ACC",
			"fontSize": 23,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "TlyRES26",
			"type": "text",
			"x": 1125.896011352539,
			"y": 475.625,
			"width": 48.207977294921875,
			"height": 28.75,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 6566,
			"version": 2,
			"versionNonce": 1143315750,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095750,
			"containerId": "Y2vS7jlL",
			"originalText": "ACC",
			"rawText": "ACC",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.acc:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.acc:label",
					"role": "label"
				}
			},
			"index": "aK"
		},
		{
			"id": "Trd7dF5T",
			"type": "ellipse",
			"x": 1078,
			"y": 488,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#263746",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 35037,
			"version": 2,
			"versionNonce": 812298298,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095750,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.acc:port:D"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.acc:port:D",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:acc",
					"role": "decoration"
				}
			},
			"index": "aL"
		},
		{
			"id": "ZWZKR4Fi",
			"type": "ellipse",
			"x": 1218,
			"y": 488,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#263746",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 5232,
			"version": 2,
			"versionNonce": 1694697574,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095750,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.acc:port:Q"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.acc:port:Q",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:acc",
					"role": "decoration"
				}
			},
			"index": "aM"
		},
		{
			"id": "nNEJD7jV",
			"type": "ellipse",
			"x": 1148,
			"y": 398,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#263746",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 78477,
			"version": 2,
			"versionNonce": 651991290,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095750,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.acc:port:en"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.acc:port:en",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:acc",
					"role": "decoration"
				}
			},
			"index": "aN"
		},
		{
			"id": "seHPWv08",
			"type": "rectangle",
			"x": 1440,
			"y": 450,
			"width": 160,
			"height": 80,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": {
				"type": 3,
				"value": 5,
				"roundType": "arc"
			},
			"seed": 82606,
			"version": 2,
			"versionNonce": 898698150,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "R955pvQO",
					"type": "text"
				},
				{
					"id": "TaaNGtRb",
					"type": "arrow"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095750,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.result"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.result",
					"role": "body"
				}
			},
			"index": "aO"
		},
		{
			"text": "输出结果",
			"fontSize": 23,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "R955pvQO",
			"type": "text",
			"x": 1474,
			"y": 475.625,
			"width": 92,
			"height": 28.75,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 89779,
			"version": 2,
			"versionNonce": 1888709050,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095750,
			"containerId": "seHPWv08",
			"originalText": "输出结果",
			"rawText": "输出结果",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.result:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.result:label",
					"role": "label"
				}
			},
			"index": "aP"
		},
		{
			"id": "gUTFvTIQ",
			"type": "rectangle",
			"x": 700,
			"y": 140,
			"width": 240,
			"height": 90,
			"angle": 0,
			"strokeColor": "#9a3412",
			"backgroundColor": "#fff7ed",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": {
				"type": 3,
				"value": 5,
				"roundType": "arc"
			},
			"seed": 83088,
			"version": 2,
			"versionNonce": 603760358,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "ghRAXMb7",
					"type": "text"
				},
				{
					"id": "bywBknqO",
					"type": "arrow"
				},
				{
					"id": "56wFxZOl",
					"type": "arrow"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095750,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.control"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.control",
					"role": "body"
				}
			},
			"index": "aQ"
		},
		{
			"text": "控制器",
			"fontSize": 23,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "ghRAXMb7",
			"type": "text",
			"x": 785.5,
			"y": 170.625,
			"width": 69,
			"height": 28.75,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 84897,
			"version": 2,
			"versionNonce": 615654010,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095750,
			"containerId": "gUTFvTIQ",
			"originalText": "控制器",
			"rawText": "控制器",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.control:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.control:label",
					"role": "label"
				}
			},
			"index": "aR"
		},
		{
			"id": "2JTKBDHN",
			"type": "ellipse",
			"x": 758,
			"y": 228,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#9a3412",
			"backgroundColor": "#9a3412",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 82722,
			"version": 2,
			"versionNonce": 1355995686,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095750,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.control:port:sel"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.control:port:sel",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:control",
					"role": "decoration"
				}
			},
			"index": "aS"
		},
		{
			"id": "lailZXnI",
			"type": "ellipse",
			"x": 938,
			"y": 183,
			"width": 4,
			"height": 4,
			"angle": 0,
			"strokeColor": "#9a3412",
			"backgroundColor": "#9a3412",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 23132,
			"version": 2,
			"versionNonce": 2113651514,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095751,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.control:port:en"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.control:port:en",
					"role": "message-port"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:control",
					"role": "decoration"
				}
			},
			"index": "aT"
		},
		{
			"text": "教学示意：sel=0 选 A，sel=1 选 ACC.Q；en=1 时写 ACC。两条 Q 出线表示同一寄存值的两个去向。省略时钟、复位与运算码，不表示完整 RTL。",
			"fontSize": 20,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "SncI0ym3",
			"type": "text",
			"x": 50,
			"y": 1040,
			"width": 1319.8797607421875,
			"height": 25,
			"angle": 0,
			"strokeColor": "#475569",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 67221,
			"version": 2,
			"versionNonce": 1124115814,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095751,
			"containerId": null,
			"originalText": "教学示意：sel=0 选 A，sel=1 选 ACC.Q；en=1 时写 ACC。两条 Q 出线表示同一寄存值的两个去向。省略时钟、复位与运算码，不表示完整 RTL。",
			"rawText": "教学示意：sel=0 选 A，sel=1 选 ACC.Q；en=1 时写 ACC。两条 Q 出线表示同一寄存值的两个去向。省略时钟、复位与运算码，不表示完整 RTL。",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.note"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.note",
					"role": "text"
				}
			},
			"index": "aU"
		},
		{
			"text": "32 位累加数据通路：选择、运算与寄存反馈",
			"fontSize": 28,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "v0hlNRso",
			"type": "text",
			"x": 50,
			"y": 36.400000000000006,
			"width": 547.3999633789062,
			"height": 35,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 46240,
			"version": 2,
			"versionNonce": 1725123578,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095751,
			"containerId": null,
			"originalText": "32 位累加数据通路：选择、运算与寄存反馈",
			"rawText": "32 位累加数据通路：选择、运算与寄存反馈",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "title"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "title",
					"role": "text"
				}
			},
			"index": "aV"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					160,
					0
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "0JbSZOGD",
				"focus": 0,
				"gap": 1,
				"mode": "inside",
				"fixedPoint": [
					1,
					0.25
				]
			},
			"endBinding": {
				"elementId": "ivsV5ljg",
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
			"id": "85xEJy8w",
			"type": "arrow",
			"x": 190,
			"y": 445,
			"width": 160,
			"height": 0,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 72329,
			"version": 3,
			"versionNonce": 633280506,
			"updated": 1792158095764,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "jQEauxiv",
					"type": "text"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095751,
			"customData": {
				"arrowHeadSize": 1,
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.a_input"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.a_input",
					"role": "edge"
				},
				"lineCrossings": "gap"
			},
			"index": "aW",
			"moveMidPointsWithElement": false
		},
		{
			"text": "32 bit",
			"fontSize": 16,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "jQEauxiv",
			"type": "text",
			"x": 248.03202056884766,
			"y": 444.6,
			"width": 43.93595886230469,
			"height": 20,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 40989,
			"version": 2,
			"versionNonce": 87801018,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095752,
			"containerId": "85xEJy8w",
			"originalText": "32 bit",
			"rawText": "32 bit",
			"lineHeight": 1.25,
			"autoResize": true,
			"labelPosition": 0.5,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.a_input:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.a_input:label",
					"role": "label"
				}
			},
			"index": "aX"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					18,
					-0.018000000000029104
				],
				[
					18,
					-45.01800000000003
				],
				[
					200,
					-45.01800000000003
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "ivsV5ljg",
				"focus": 0,
				"gap": 1,
				"mode": "inside",
				"fixedPoint": [
					1,
					0.5
				]
			},
			"endBinding": {
				"elementId": "jzCUXb1q",
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
			"id": "BvHm1K4T",
			"type": "arrow",
			"x": 500,
			"y": 490.01800000000003,
			"width": 200,
			"height": 45.01800000000003,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 20296,
			"version": 3,
			"versionNonce": 1516418362,
			"updated": 1792158095766,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "VBQIbRiJ",
					"type": "text"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095752,
			"customData": {
				"arrowHeadSize": 1,
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.selected"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.selected",
					"role": "edge"
				},
				"lineCrossings": "gap"
			},
			"index": "aY",
			"moveMidPointsWithElement": false
		},
		{
			"text": "32 bit",
			"fontSize": 16,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "VBQIbRiJ",
			"type": "text",
			"x": 578.0320205688477,
			"y": 502.5,
			"width": 43.93595886230469,
			"height": 20,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 68149,
			"version": 2,
			"versionNonce": 1188566394,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095752,
			"containerId": "BvHm1K4T",
			"originalText": "32 bit",
			"rawText": "32 bit",
			"lineHeight": 1.25,
			"autoResize": true,
			"labelPosition": 0.6285714285714286,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.selected:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.selected:label",
					"role": "label"
				}
			},
			"index": "aZ"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					410,
					-0.014000000000010004
				],
				[
					410,
					-275.014
				],
				[
					510,
					-275.014
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "VMM3jM1k",
				"focus": 0,
				"gap": 1,
				"mode": "inside",
				"fixedPoint": [
					1,
					0.5
				]
			},
			"endBinding": {
				"elementId": "jzCUXb1q",
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
			"id": "JruMkmS0",
			"type": "arrow",
			"x": 190,
			"y": 810.014,
			"width": 510,
			"height": 275.014,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 70618,
			"version": 3,
			"versionNonce": 214829242,
			"updated": 1792158095764,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "Tuv2Wdd8",
					"type": "text"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095752,
			"customData": {
				"arrowHeadSize": 1,
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.b_input"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.b_input",
					"role": "edge"
				},
				"lineCrossings": "gap"
			},
			"index": "aa",
			"moveMidPointsWithElement": false
		},
		{
			"text": "32 bit",
			"fontSize": 16,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "Tuv2Wdd8",
			"type": "text",
			"x": 423.03202056884766,
			"y": 937.5,
			"width": 43.93595886230469,
			"height": 20,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 50018,
			"version": 2,
			"versionNonce": 1827362362,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095753,
			"containerId": "JruMkmS0",
			"originalText": "32 bit",
			"rawText": "32 bit",
			"lineHeight": 1.25,
			"autoResize": true,
			"labelPosition": 0.2611464968152866,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.b_input:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.b_input:label",
					"role": "label"
				}
			},
			"index": "ab"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					200,
					0
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "jzCUXb1q",
				"focus": 0,
				"gap": 1,
				"mode": "inside",
				"fixedPoint": [
					1,
					0.5
				]
			},
			"endBinding": {
				"elementId": "Y2vS7jlL",
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
			"id": "pUI7K2OE",
			"type": "arrow",
			"x": 880,
			"y": 490.01800000000003,
			"width": 200,
			"height": 0,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 80591,
			"version": 3,
			"versionNonce": 1044439418,
			"updated": 1792158095764,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "8JiRNgci",
					"type": "text"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095753,
			"customData": {
				"arrowHeadSize": 1,
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.write_acc"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.write_acc",
					"role": "edge"
				},
				"lineCrossings": "gap"
			},
			"index": "ac",
			"moveMidPointsWithElement": false
		},
		{
			"text": "32 bit",
			"fontSize": 16,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "8JiRNgci",
			"type": "text",
			"x": 958.0320205688477,
			"y": 489.6,
			"width": 43.93595886230469,
			"height": 20,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 52253,
			"version": 2,
			"versionNonce": 408452858,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095753,
			"containerId": "pUI7K2OE",
			"originalText": "32 bit",
			"rawText": "32 bit",
			"lineHeight": 1.25,
			"autoResize": true,
			"labelPosition": 0.5,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.write_acc:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.write_acc:label",
					"role": "label"
				}
			},
			"index": "ad"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					220,
					-0.010000000000047748
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Y2vS7jlL",
				"focus": 0,
				"gap": 1,
				"mode": "inside",
				"fixedPoint": [
					1,
					0.5
				]
			},
			"endBinding": {
				"elementId": "seHPWv08",
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
			"id": "TaaNGtRb",
			"type": "arrow",
			"x": 1220,
			"y": 490.01800000000003,
			"width": 220,
			"height": 0.010000000000047748,
			"angle": 0,
			"strokeColor": "#263746",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 44171,
			"version": 3,
			"versionNonce": 358261306,
			"updated": 1792158095764,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "8fVyYbjG",
					"type": "text"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095754,
			"customData": {
				"arrowHeadSize": 1,
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.output"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.output",
					"role": "edge"
				},
				"lineCrossings": "gap"
			},
			"index": "ae",
			"moveMidPointsWithElement": false
		},
		{
			"text": "Q / 32 bit",
			"fontSize": 16,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "8fVyYbjG",
			"type": "text",
			"x": 1293.6720352172852,
			"y": 489.6,
			"width": 72.65592956542969,
			"height": 20,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 44213,
			"version": 2,
			"versionNonce": 1436716986,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095754,
			"containerId": "TaaNGtRb",
			"originalText": "Q / 32 bit",
			"rawText": "Q / 32 bit",
			"lineHeight": 1.25,
			"autoResize": true,
			"labelPosition": 0.5,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.output:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.output:label",
					"role": "label"
				}
			},
			"index": "af"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					30,
					-0.018000000000029104
				],
				[
					30,
					189.98199999999997
				],
				[
					-920,
					189.98199999999997
				],
				[
					-920,
					44.98199999999997
				],
				[
					-870,
					44.98199999999997
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Y2vS7jlL",
				"focus": 0,
				"gap": 1,
				"mode": "inside",
				"fixedPoint": [
					1,
					0.5
				]
			},
			"endBinding": {
				"elementId": "ivsV5ljg",
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
			"id": "wiL77g7r",
			"type": "arrow",
			"x": 1220,
			"y": 490.01800000000003,
			"width": 950,
			"height": 190,
			"angle": 0,
			"strokeColor": "#7c3aed",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 82061,
			"version": 3,
			"versionNonce": 217991930,
			"updated": 1792158095765,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "3Wj0xB6c",
					"type": "text"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095754,
			"customData": {
				"arrowHeadSize": 1,
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.feedback"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.feedback",
					"role": "edge"
				},
				"lineCrossings": "gap"
			},
			"index": "ag",
			"moveMidPointsWithElement": false
		},
		{
			"text": "Q 反馈 / 32 bit",
			"fontSize": 16,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "3Wj0xB6c",
			"type": "text",
			"x": 1639.8720397949219,
			"y": 575,
			"width": 110.25592041015625,
			"height": 20,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 39433,
			"version": 2,
			"versionNonce": 686590074,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095755,
			"containerId": "wiL77g7r",
			"originalText": "Q 反馈 / 32 bit",
			"rawText": "Q 反馈 / 32 bit",
			"lineHeight": 1.25,
			"autoResize": true,
			"labelPosition": 0.5091575091575091,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.feedback:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.feedback:label",
					"role": "label"
				}
			},
			"index": "ah"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					152
				],
				[
					-335,
					152
				],
				[
					-334.985,
					170
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "gUTFvTIQ",
				"focus": 0,
				"gap": 1,
				"mode": "inside",
				"fixedPoint": [
					0.25,
					1
				]
			},
			"endBinding": {
				"elementId": "ivsV5ljg",
				"focus": 0,
				"gap": 1,
				"mode": "inside",
				"fixedPoint": [
					0.5,
					0
				]
			},
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"id": "bywBknqO",
			"type": "arrow",
			"x": 760,
			"y": 230,
			"width": 335,
			"height": 170,
			"angle": 0,
			"strokeColor": "#9a3412",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 56444,
			"version": 3,
			"versionNonce": 797922426,
			"updated": 1792158095766,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "NfutqGxh",
					"type": "text"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095755,
			"customData": {
				"arrowHeadSize": 1,
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.select"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.select",
					"role": "edge"
				},
				"lineCrossings": "gap"
			},
			"index": "ai",
			"moveMidPointsWithElement": false
		},
		{
			"text": "sel / 1 bit",
			"fontSize": 16,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "NfutqGxh",
			"type": "text",
			"x": 891.4040451049805,
			"y": 305,
			"width": 72.19190979003906,
			"height": 20,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 88231,
			"version": 2,
			"versionNonce": 435775802,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095755,
			"containerId": "bywBknqO",
			"originalText": "sel / 1 bit",
			"rawText": "sel / 1 bit",
			"lineHeight": 1.25,
			"autoResize": true,
			"labelPosition": 0.6326732673267327,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.select:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.select:label",
					"role": "label"
				}
			},
			"index": "aj"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					110,
					-0.009000000000014552
				],
				[
					110,
					114.99099999999999
				],
				[
					210,
					114.99099999999999
				],
				[
					210.0139999999999,
					214.99099999999999
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "gUTFvTIQ",
				"focus": 0,
				"gap": 1,
				"mode": "inside",
				"fixedPoint": [
					1,
					0.5
				]
			},
			"endBinding": {
				"elementId": "Y2vS7jlL",
				"focus": 0,
				"gap": 1,
				"mode": "inside",
				"fixedPoint": [
					0.5,
					0
				]
			},
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"id": "56wFxZOl",
			"type": "arrow",
			"x": 940,
			"y": 185.00900000000001,
			"width": 210.0139999999999,
			"height": 215,
			"angle": 0,
			"strokeColor": "#9a3412",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 14986,
			"version": 3,
			"versionNonce": 1269750714,
			"updated": 1792158095765,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "0KS9F7fw",
					"type": "text"
				}
			],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095755,
			"customData": {
				"arrowHeadSize": 1,
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.enable"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.enable",
					"role": "edge"
				},
				"lineCrossings": "gap"
			},
			"index": "ak",
			"moveMidPointsWithElement": false
		},
		{
			"text": "en / 1 bit",
			"fontSize": 16,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "center",
			"verticalAlign": "middle",
			"id": "0KS9F7fw",
			"type": "text",
			"x": 1010.3840408325195,
			"y": 282.5,
			"width": 69.23191833496094,
			"height": 20,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 69366,
			"version": 2,
			"versionNonce": 1076638202,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095756,
			"containerId": "56wFxZOl",
			"originalText": "en / 1 bit",
			"rawText": "en / 1 bit",
			"lineHeight": 1.25,
			"autoResize": true,
			"labelPosition": 0.3941176470588235,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "edge.enable:label"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "edge.enable:label",
					"role": "label"
				}
			},
			"index": "al"
		},
		{
			"text": "Q",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "I8XfqqeT",
			"type": "text",
			"x": 198,
			"y": 424.6,
			"width": 8.939987182617188,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 63961,
			"version": 2,
			"versionNonce": 1298367142,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095756,
			"containerId": null,
			"originalText": "Q",
			"rawText": "Q",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.a:port-label:Q"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.a:port-label:Q",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:a",
					"role": "decoration"
				}
			},
			"index": "am"
		},
		{
			"text": "Q",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "wAPGuFqY",
			"type": "text",
			"x": 198,
			"y": 789.6,
			"width": 8.939987182617188,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 44875,
			"version": 2,
			"versionNonce": 1317528250,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095756,
			"containerId": null,
			"originalText": "Q",
			"rawText": "Q",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.b:port-label:Q"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.b:port-label:Q",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:b",
					"role": "decoration"
				}
			},
			"index": "an"
		},
		{
			"text": "i0",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "spICeNNt",
			"type": "text",
			"x": 331.6440124511719,
			"y": 424.6,
			"width": 10.355987548828125,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 75568,
			"version": 2,
			"versionNonce": 677920230,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095757,
			"containerId": null,
			"originalText": "i0",
			"rawText": "i0",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux:port-label:i0"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux:port-label:i0",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				}
			},
			"index": "ao"
		},
		{
			"text": "i1",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "JuR2tZeD",
			"type": "text",
			"x": 331.6440124511719,
			"y": 514.6,
			"width": 10.355987548828125,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 81524,
			"version": 2,
			"versionNonce": 531594106,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095757,
			"containerId": null,
			"originalText": "i1",
			"rawText": "i1",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux:port-label:i1"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux:port-label:i1",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				}
			},
			"index": "ap"
		},
		{
			"text": "sel",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "8pJTHBwR",
			"type": "text",
			"x": 401.20802307128906,
			"y": 377.6,
			"width": 15.791976928710938,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 32948,
			"version": 2,
			"versionNonce": 296980774,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095757,
			"containerId": null,
			"originalText": "sel",
			"rawText": "sel",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux:port-label:sel"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux:port-label:sel",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				}
			},
			"index": "aq"
		},
		{
			"text": "y",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "I45mCqyB",
			"type": "text",
			"x": 508,
			"y": 469.6,
			"width": 6,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 65349,
			"version": 2,
			"versionNonce": 1105591354,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095758,
			"containerId": null,
			"originalText": "y",
			"rawText": "y",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.mux:port-label:y"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.mux:port-label:y",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:mux",
					"role": "decoration"
				}
			},
			"index": "ar"
		},
		{
			"text": "a",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "2Tnx5f3b",
			"type": "text",
			"x": 685.1000061035156,
			"y": 424.6,
			"width": 6.899993896484375,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 6657,
			"version": 2,
			"versionNonce": 884112486,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095758,
			"containerId": null,
			"originalText": "a",
			"rawText": "a",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.alu:port-label:a"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.alu:port-label:a",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:alu",
					"role": "decoration"
				}
			},
			"index": "as"
		},
		{
			"text": "b",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "87y1td2z",
			"type": "text",
			"x": 685.1240081787109,
			"y": 514.6,
			"width": 6.8759918212890625,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 22401,
			"version": 2,
			"versionNonce": 51275002,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095758,
			"containerId": null,
			"originalText": "b",
			"rawText": "b",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.alu:port-label:b"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.alu:port-label:b",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:alu",
					"role": "decoration"
				}
			},
			"index": "at"
		},
		{
			"text": "y",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "vNzf36bq",
			"type": "text",
			"x": 888,
			"y": 469.6,
			"width": 6,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 25456,
			"version": 2,
			"versionNonce": 1194459046,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095758,
			"containerId": null,
			"originalText": "y",
			"rawText": "y",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.alu:port-label:y"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.alu:port-label:y",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:alu",
					"role": "decoration"
				}
			},
			"index": "au"
		},
		{
			"text": "D",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "EDKAQNDy",
			"type": "text",
			"x": 1063.2640075683594,
			"y": 469.6,
			"width": 8.735992431640625,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 70682,
			"version": 2,
			"versionNonce": 2091627962,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095759,
			"containerId": null,
			"originalText": "D",
			"rawText": "D",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.acc:port-label:D"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.acc:port-label:D",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:acc",
					"role": "decoration"
				}
			},
			"index": "av"
		},
		{
			"text": "Q",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "dkfWlgEf",
			"type": "text",
			"x": 1228,
			"y": 469.6,
			"width": 8.939987182617188,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 15030,
			"version": 2,
			"versionNonce": 1029642982,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095759,
			"containerId": null,
			"originalText": "Q",
			"rawText": "Q",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.acc:port-label:Q"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.acc:port-label:Q",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:acc",
					"role": "decoration"
				}
			},
			"index": "aw"
		},
		{
			"text": "en",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "inY5zRxh",
			"type": "text",
			"x": 1158,
			"y": 377.6,
			"width": 13.571990966796875,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 84114,
			"version": 2,
			"versionNonce": 534834810,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095759,
			"containerId": null,
			"originalText": "en",
			"rawText": "en",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.acc:port-label:en"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.acc:port-label:en",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:acc",
					"role": "decoration"
				}
			},
			"index": "ax"
		},
		{
			"text": "sel",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "Q9ldyZdK",
			"type": "text",
			"x": 768,
			"y": 238,
			"width": 15.791976928710938,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 29992,
			"version": 2,
			"versionNonce": 2110180902,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095759,
			"containerId": null,
			"originalText": "sel",
			"rawText": "sel",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.control:port-label:sel"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.control:port-label:sel",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:control",
					"role": "decoration"
				}
			},
			"index": "ay"
		},
		{
			"text": "en",
			"fontSize": 12,
			"fontFamily": "LXGWWenKai-Regular",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "Sv19v5z2",
			"type": "text",
			"x": 948,
			"y": 164.6,
			"width": 13.571990966796875,
			"height": 15,
			"angle": 0,
			"strokeColor": "#172554",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 44318,
			"version": 2,
			"versionNonce": 1097928506,
			"updated": 1792158095763,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792158095760,
			"containerId": null,
			"originalText": "en",
			"rawText": "en",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"dsl": {
					"document": "gallery_feedback_datapath",
					"key": "node.control:port-label:en"
				},
				"agentDiagram": {
					"diagramId": "dsl:gallery_feedback_datapath",
					"logicalId": "node.control:port-label:en",
					"role": "text"
				},
				"agentPrimitive": {
					"instanceId": "gallery_feedback_datapath:node:control",
					"role": "decoration"
				}
			},
			"index": "az"
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