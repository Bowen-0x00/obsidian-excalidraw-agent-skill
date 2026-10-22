---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'

# Excalidraw Data

## Text Elements
IO-AWARE COMPUTING / ALGORITHM ATLAS 01 ^ao3s2JNW

FlashAttention ^z1cIbbE8

Exact attention. Local tiles. No quadratic HBM workspace. ^Fv9Z4kj2

01 / HBM ^bRwVXVia

Full tensors live here. Only selected blocks cross the boundary. ^Uq9RwEAi

Q ^IFqSOpJW

K ^zc6Z1uQO

V ^lI4bu7ru

O ^LbAKoi38

Rows are partitioned into blocks; grids are schematic. ^ULl0enVb

OUTPUT ^b5GfCB7C

02 / ON-CHIP WORKING SET ^vbMYVjui

SRAM + registers / one query block ^oEE8uuZb

Held through the
K/V sweep ^h9zFklAd

K/V BLOCK ^rGSE7Xjl

1 ^3Z9qZABy

2 ^IqrAqGQO

3 ^3HoGDT8u

4 ^Lg5c6mDS

Block 3 of 4 ^lFPH9z1F

-1.3 ^w2Ye4AoZ

-1.3 ^MyomBxyv

-0.8 ^PaQp78eg

-0.3 ^fAydIV7k

-0.6 ^lHRo6PTk

-1.0 ^EY9gR9A5

-1.1 ^88RL1Q0T

-1.1 ^rROdPLhB

0.5 ^1rGei7G8

-0.1 ^ZltzJqRD

-0.9 ^fQiqdx3Z

-1.5 ^AaGXzalx

0.4 ^XhLNwHjH

0.1 ^hGwBLwwU

-0.4 ^8VEDLdLt

-0.8 ^PkcCFbcs

0.13 ^m7kgRnJe

0.14 ^F1dkoE9i

0.22 ^1t2AC3CG

0.35 ^QFYzEc2h

0.26 ^QGTUTeml

0.18 ^LIekUAak

0.17 ^iymdtwU1

0.17 ^zVkRtyrL

0.82 ^m7UtInMO

0.44 ^rRE7lxV2

0.20 ^9DyBkD0Z

0.11 ^1L2AtIFM

0.96 ^3yVNc4fF

0.70 ^HVLnROGR

0.44 ^2B2zciM5

0.31 ^JAyk4zzD

shift + exp ^R04M0j1c

Unnormalized
weights ^UDTQMvLf

CARRY TO THE NEXT TILE ^0Dr4NlTu

0.7 ^bw3zt0pJ

0.7 ^QS4oEzMW

0.7 ^VwJq1mAe

0.4 ^0TSX2rvB

5.6 ^bgvWNCkb

5.6 ^0L9Rmskg

6.3 ^DF0BUlHY

8.0 ^YoZZu25L

2.3 ^3BfSNxiz

-0.3 ^RaLpuGC9

-1.4 ^WxyP0KmU

-0.7 ^g8eTQevi

1.9 ^aLJMJhSE

-1.3 ^mjdChs7s

-0.9 ^y2M8LBED

0.4 ^zNma0jCv

1.0 ^30ZZ4DJ9

-1.5 ^uPa1TzXp

1.1 ^1TqVb0dN

0.7 ^yfvxqgKy

1.0 ^u6KpKWVp

-1.1 ^jQW0W16P

1.5 ^RR6c1CXW

-0.1 ^zxH3RQsW

rescale + add ^fGSul7lG

old numerator ^h0zGxd91

After the K/V sweep:
normalize once, then write. ^REzkCoQn

03 / THE BUFFER YOU AVOID ^6KgVxHU2

NO FULL S / P BUFFER IN HBM ^xJFQBWgA

Scores are computed, not skipped.
No full score/weight matrix is stored. ^lzDpZAxg

THE ONLINE UPDATE ^lAVQAv8S

One query row q; repeat for each K/V tile. ^4za7nAjQ

m / running maximum
ell / rescaled exponential sum
u / unnormalized numerator ^rhMmJFql

Forward pass / FA2-style query-block schedule / one head / unmasked / no dropout. Memory placement is schematic. ^FoU5IC9Z

Source: Dao, FlashAttention-2, Section 3.1 (2023). Synthetic 16-token, d=4 snapshot; 4x4 tiles are not GPU launch sizes. ^VxZUKUhQ

## Embedded Files
c46e301b86d06bf4705a0cdb9a76815e50b34a8a: $$O=\operatorname{softmax}\!\left(\frac{QK^{\mathsf T}}{\sqrt d}\right)V$$

400f1a19da0b4c4a2f000dd23a56db4d5cb22da2: $$N\times d$$

7e6ff40c18a06e2b71469d828b02177b71e4d431: $$N\times d$$

ab22d2d326f7a33c02d94b7dec1d76a051dabe2b: $$N\times d$$

39e7d172f711551eb04b5c5ea06a68497612f067: $$N\times d$$

eef131b98df998bea42248bd3dd339cbc48ba395: $$Q_i$$

68d5c4cec905d7e0ffbabd57534f0ed8c68720a0: $$B_r\times d$$

f7144b3aadc70a777e98f23882b5cdcfbc976c99: $$K_j^{\mathsf T}$$

d29fd6d9ce5b9f68cd10c197bcd2078df9955f69: $$d\times B_c$$

993bee1faf6bf07cdea6a3c1dc8a76c212770b70: $$V_j$$

9f279b4f520866d01df260c3ece33dd39e7db7e2: $$B_c\times d$$

ea4991917a97ab1abfadc3f69e0582bdd6cb9a40: $$S_{ij}$$

85bb4e5c8f5096c5ae2de0fa288d6aeb1f58a3ec: $$B_r\times B_c$$

f89980f4919e63b898dc028310dd858f83f2522f: $$\widetilde P_{ij}$$

75b0afa6a06f448023413fa43d20ea90b59872ce: $$\widetilde P V_j$$

5170a6cfb74365845514b49ae30ec7a7af5c9e40: $$m_i$$

ded6e9a15e263e844608ac670746872fc8eea114: $$\ell_i$$

aa9376c0bb9c72e523af4ed50fbed13c34425ea0: $$U_i$$

309d196bffb8b26eb07c6057ef638ceabd71b876: $$O_i=\operatorname{diag}(\ell_i)^{-1}U_i$$

ab3bce10ed80430cd6124e27ba01a058a1bd9b5b: $$N\times N$$

247cf78cd9f51a6778764fe2a39ab93794e1cea0: $$\begin{aligned}\ell^{\prime}&=\alpha\ell+\sum p\\[4pt]u^{\prime}&=\alpha u+pV_j\\[4pt]o&=u/\ell\quad\text{after the sweep}\end{aligned}$$

997b13806a0c46597b8af046c4050916abfbc04c: $$m=-\infty,\quad\ell=0,\quad u=\mathbf 0$$

6a5eafffbbc98c306ee959d505183a9d85d33ea2: $$\begin{aligned}s&=qK_j^{\mathsf T}/\sqrt d\\[4pt]m^{\prime}&=\max\!\left(m,\max(s)\right)\\[4pt]\alpha&=e^{m-m^{\prime}}\\[4pt]p&=e^{s-m^{\prime}}\end{aligned}$$


## Tags
%%
## Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.29.0-7",
	"elements": [
		{
			"id": "tFR0KBuo",
			"type": "rectangle",
			"x": 0,
			"y": 0,
			"width": 1960,
			"height": 1520,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 1.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 86806,
			"version": 2,
			"versionNonce": 271896623,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064815,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "page",
					"role": "container"
				},
				"isContainer": true,
				"dsl": {
					"document": "flashattention-flagship",
					"key": "page"
				}
			},
			"index": "a0"
		},
		{
			"text": "IO-AWARE COMPUTING / ALGORITHM ATLAS 01",
			"fontSize": 18,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "ao3s2JNW",
			"type": "text",
			"x": 65,
			"y": 32,
			"width": 412.3828125,
			"height": 22.5,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 16919,
			"version": 2,
			"versionNonce": 1449315905,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064816,
			"containerId": null,
			"originalText": "IO-AWARE COMPUTING / ALGORITHM ATLAS 01",
			"rawText": "IO-AWARE COMPUTING / ALGORITHM ATLAS 01",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "kicker",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "kicker"
				}
			},
			"index": "a1"
		},
		{
			"text": "FlashAttention",
			"fontSize": 64,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "z1cIbbE8",
			"type": "text",
			"x": 65,
			"y": 72,
			"width": 409.125,
			"height": 80,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 74117,
			"version": 2,
			"versionNonce": 1353249359,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064817,
			"containerId": null,
			"originalText": "FlashAttention",
			"rawText": "FlashAttention",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "title",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "title"
				},
				"bold": true
			},
			"index": "a2"
		},
		{
			"text": "Exact attention. Local tiles. No quadratic HBM workspace.",
			"fontSize": 27,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "Fv9Z4kj2",
			"type": "text",
			"x": 68,
			"y": 156,
			"width": 693.3251953125,
			"height": 33.75,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 83250,
			"version": 2,
			"versionNonce": 542203425,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064817,
			"containerId": null,
			"originalText": "Exact attention. Local tiles. No quadratic HBM workspace.",
			"rawText": "Exact attention. Local tiles. No quadratic HBM workspace.",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "subtitle",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "subtitle"
				}
			},
			"index": "a3"
		},
		{
			"id": "4sBM5hto",
			"type": "image",
			"x": 1295,
			"y": 87,
			"width": 306,
			"height": 73.8,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 10818,
			"version": 2,
			"versionNonce": 1318309999,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064827,
			"fileId": "c46e301b86d06bf4705a0cdb9a76815e50b34a8a",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "attention-operator",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "attention-operator"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "a4"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					1830,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "JjKwe4lT",
			"type": "line",
			"x": 65,
			"y": 207,
			"width": 1830,
			"height": 0,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 81282,
			"version": 2,
			"versionNonce": 1906504193,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064827,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "title-rule",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "title-rule"
				}
			},
			"index": "a5"
		},
		{
			"text": "01 / HBM",
			"fontSize": 23,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "bRwVXVia",
			"type": "text",
			"x": 75,
			"y": 228,
			"width": 95.86328125,
			"height": 28.75,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 86365,
			"version": 2,
			"versionNonce": 599648911,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064828,
			"containerId": null,
			"originalText": "01 / HBM",
			"rawText": "01 / HBM",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-heading",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-heading"
				},
				"bold": true
			},
			"index": "a6"
		},
		{
			"text": "Full tensors live here. Only selected blocks cross the boundary.",
			"fontSize": 21,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "Uq9RwEAi",
			"type": "text",
			"x": 380,
			"y": 233,
			"width": 586.71826171875,
			"height": 26.25,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 94663,
			"version": 2,
			"versionNonce": 1867975137,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064828,
			"containerId": null,
			"originalText": "Full tensors live here. Only selected blocks cross the boundary.",
			"rawText": "Full tensors live here. Only selected blocks cross the boundary.",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-caption",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-caption"
				}
			},
			"index": "a7"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				],
				[
					235,
					-95
				],
				[
					0,
					-95
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
			"id": "2vKCGDED",
			"type": "line",
			"x": 120,
			"y": 420,
			"width": 235,
			"height": 95,
			"angle": 0,
			"strokeColor": "#5e8faa",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 67613,
			"version": 2,
			"versionNonce": 484425903,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064828,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-Q",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-Q",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-Q",
					"objectId": "hbm-Q",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 120,
						"y": 420,
						"points": [
							[
								0,
								0
							],
							[
								235,
								0
							],
							[
								235,
								-95
							],
							[
								0,
								-95
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 235,
						"depth": 30,
						"height": 95
					},
					"origin": [
						120,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:front"
				},
				"isContainer": true
			},
			"index": "a8"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					19.5,
					-13.5
				],
				[
					19.5,
					-108.5
				],
				[
					0,
					-95
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
			"id": "NnPF3izD",
			"type": "line",
			"x": 355,
			"y": 420,
			"width": 19.5,
			"height": 108.5,
			"angle": 0,
			"strokeColor": "#5e8faa",
			"backgroundColor": "#5e8faa",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 39040,
			"version": 2,
			"versionNonce": 1920804289,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064828,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-Q",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-Q",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-Q",
					"objectId": "hbm-Q",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 355,
						"y": 420,
						"points": [
							[
								0,
								0
							],
							[
								19.5,
								-13.5
							],
							[
								19.5,
								-108.5
							],
							[
								0,
								-95
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 235,
						"depth": 30,
						"height": 95
					},
					"origin": [
						120,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:side"
				},
				"isContainer": true
			},
			"index": "a9"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				],
				[
					254.5,
					-13.5
				],
				[
					19.5,
					-13.5
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
			"id": "zQJFv3OD",
			"type": "line",
			"x": 120,
			"y": 325,
			"width": 254.5,
			"height": 13.5,
			"angle": 0,
			"strokeColor": "#5e8faa",
			"backgroundColor": "#f5f8fa",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 63261,
			"version": 2,
			"versionNonce": 1537331919,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064828,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-Q",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-Q",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-Q",
					"objectId": "hbm-Q",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 120,
						"y": 325,
						"points": [
							[
								0,
								0
							],
							[
								235,
								0
							],
							[
								254.5,
								-13.5
							],
							[
								19.5,
								-13.5
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 235,
						"depth": 30,
						"height": 95
					},
					"origin": [
						120,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:top"
				},
				"isContainer": true
			},
			"index": "aA"
		},
		{
			"id": "nN6cEGmd",
			"type": "rectangle",
			"x": 120,
			"y": 348.75,
			"width": 235,
			"height": 23.75,
			"angle": 0,
			"strokeColor": "#5e8faa",
			"backgroundColor": "#5e8faa",
			"fillStyle": "solid",
			"strokeWidth": 1.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 77444,
			"version": 2,
			"versionNonce": 104121761,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064829,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-Q:active",
					"role": "container"
				},
				"isContainer": true,
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:active"
				}
			},
			"index": "aB"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "HJkAnlV5",
			"type": "line",
			"x": 120,
			"y": 348.75,
			"width": 235,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 25566,
			"version": 2,
			"versionNonce": 949788911,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064829,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-Q:row:1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:row:1"
				}
			},
			"index": "aC"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "Idlq57S6",
			"type": "line",
			"x": 120,
			"y": 372.5,
			"width": 235,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 48152,
			"version": 2,
			"versionNonce": 632121729,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064829,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-Q:row:2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:row:2"
				}
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
					235,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "pc6QyLQe",
			"type": "line",
			"x": 120,
			"y": 396.25,
			"width": 235,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 82364,
			"version": 2,
			"versionNonce": 1700309775,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064829,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-Q:row:3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:row:3"
				}
			},
			"index": "aE"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "472ytypQ",
			"type": "line",
			"x": 178.75,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 29821,
			"version": 2,
			"versionNonce": 975606113,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064829,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-Q:col:1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:col:1"
				}
			},
			"index": "aF"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "0SMbEbAP",
			"type": "line",
			"x": 237.5,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 91412,
			"version": 2,
			"versionNonce": 1313763631,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064829,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-Q:col:2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:col:2"
				}
			},
			"index": "aG"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "jfXB0Jr1",
			"type": "line",
			"x": 296.25,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 51852,
			"version": 2,
			"versionNonce": 1492106561,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064829,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-Q:col:3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:col:3"
				}
			},
			"index": "aH"
		},
		{
			"text": "Q",
			"fontSize": 36,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "IFqSOpJW",
			"type": "text",
			"x": 120,
			"y": 260,
			"width": 28.001953125,
			"height": 45,
			"angle": 0,
			"strokeColor": "#5e8faa",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 34104,
			"version": 2,
			"versionNonce": 1021735759,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064829,
			"containerId": null,
			"originalText": "Q",
			"rawText": "Q",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-Q:label",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:label"
				},
				"bold": true
			},
			"index": "aI"
		},
		{
			"id": "CBJaWl9K",
			"type": "image",
			"x": 128,
			"y": 437,
			"width": 60.199999999999996,
			"height": 15.399999999999999,
			"angle": 0,
			"strokeColor": "#5e8faa",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 95804,
			"version": 2,
			"versionNonce": 1097362721,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064837,
			"fileId": "400f1a19da0b4c4a2f000dd23a56db4d5cb22da2",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-Q:shape",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-Q:shape"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "aJ"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				],
				[
					235,
					-95
				],
				[
					0,
					-95
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
			"id": "t9SrvGfv",
			"type": "line",
			"x": 550,
			"y": 420,
			"width": 235,
			"height": 95,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 19694,
			"version": 2,
			"versionNonce": 964243823,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064837,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-K",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-K",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-K",
					"objectId": "hbm-K",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 550,
						"y": 420,
						"points": [
							[
								0,
								0
							],
							[
								235,
								0
							],
							[
								235,
								-95
							],
							[
								0,
								-95
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 235,
						"depth": 30,
						"height": 95
					},
					"origin": [
						550,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:front"
				},
				"isContainer": true
			},
			"index": "aK"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					19.5,
					-13.5
				],
				[
					19.5,
					-108.5
				],
				[
					0,
					-95
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
			"id": "wICKfT1v",
			"type": "line",
			"x": 785,
			"y": 420,
			"width": 19.5,
			"height": 108.5,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "#4b8b7a",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 66468,
			"version": 2,
			"versionNonce": 452993281,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064837,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-K",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-K",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-K",
					"objectId": "hbm-K",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 785,
						"y": 420,
						"points": [
							[
								0,
								0
							],
							[
								19.5,
								-13.5
							],
							[
								19.5,
								-108.5
							],
							[
								0,
								-95
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 235,
						"depth": 30,
						"height": 95
					},
					"origin": [
						550,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:side"
				},
				"isContainer": true
			},
			"index": "aL"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				],
				[
					254.5,
					-13.5
				],
				[
					19.5,
					-13.5
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
			"id": "uzEYS9bE",
			"type": "line",
			"x": 550,
			"y": 325,
			"width": 254.5,
			"height": 13.5,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "#f5f8fa",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 55631,
			"version": 2,
			"versionNonce": 760163215,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064837,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-K",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-K",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-K",
					"objectId": "hbm-K",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 550,
						"y": 325,
						"points": [
							[
								0,
								0
							],
							[
								235,
								0
							],
							[
								254.5,
								-13.5
							],
							[
								19.5,
								-13.5
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 235,
						"depth": 30,
						"height": 95
					},
					"origin": [
						550,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:top"
				},
				"isContainer": true
			},
			"index": "aM"
		},
		{
			"id": "mc8aKJxG",
			"type": "rectangle",
			"x": 550,
			"y": 372.5,
			"width": 235,
			"height": 23.75,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "#4b8b7a",
			"fillStyle": "solid",
			"strokeWidth": 1.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 92671,
			"version": 2,
			"versionNonce": 1932941537,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064837,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-K:active",
					"role": "container"
				},
				"isContainer": true,
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:active"
				}
			},
			"index": "aN"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "uzzUUYkS",
			"type": "line",
			"x": 550,
			"y": 348.75,
			"width": 235,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 76097,
			"version": 2,
			"versionNonce": 1151394223,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064837,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-K:row:1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:row:1"
				}
			},
			"index": "aO"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "H4XSQH3k",
			"type": "line",
			"x": 550,
			"y": 372.5,
			"width": 235,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 7864,
			"version": 2,
			"versionNonce": 2073728193,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064837,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-K:row:2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:row:2"
				}
			},
			"index": "aP"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "U3s9cE1q",
			"type": "line",
			"x": 550,
			"y": 396.25,
			"width": 235,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 27363,
			"version": 2,
			"versionNonce": 278320079,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064838,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-K:row:3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:row:3"
				}
			},
			"index": "aQ"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "XDOBhJNN",
			"type": "line",
			"x": 608.75,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 9415,
			"version": 2,
			"versionNonce": 130831521,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064838,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-K:col:1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:col:1"
				}
			},
			"index": "aR"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "zoyJfNJh",
			"type": "line",
			"x": 667.5,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 96843,
			"version": 2,
			"versionNonce": 1766425071,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064838,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-K:col:2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:col:2"
				}
			},
			"index": "aS"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "z3kqIZj3",
			"type": "line",
			"x": 726.25,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 80402,
			"version": 2,
			"versionNonce": 1266358401,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064838,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-K:col:3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:col:3"
				}
			},
			"index": "aT"
		},
		{
			"text": "K",
			"fontSize": 36,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "zc6Z1uQO",
			"type": "text",
			"x": 550,
			"y": 260,
			"width": 24.01171875,
			"height": 45,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 37045,
			"version": 2,
			"versionNonce": 264334351,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064838,
			"containerId": null,
			"originalText": "K",
			"rawText": "K",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-K:label",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:label"
				},
				"bold": true
			},
			"index": "aU"
		},
		{
			"id": "z4WkDcA3",
			"type": "image",
			"x": 558,
			"y": 437,
			"width": 60.199999999999996,
			"height": 15.399999999999999,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 16232,
			"version": 2,
			"versionNonce": 1483104353,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064842,
			"fileId": "7e6ff40c18a06e2b71469d828b02177b71e4d431",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-K:shape",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-K:shape"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "aV"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				],
				[
					235,
					-95
				],
				[
					0,
					-95
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
			"id": "lAwT3avE",
			"type": "line",
			"x": 980,
			"y": 420,
			"width": 235,
			"height": 95,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 2198,
			"version": 2,
			"versionNonce": 267850287,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064843,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-V",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-V",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-V",
					"objectId": "hbm-V",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 980,
						"y": 420,
						"points": [
							[
								0,
								0
							],
							[
								235,
								0
							],
							[
								235,
								-95
							],
							[
								0,
								-95
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 235,
						"depth": 30,
						"height": 95
					},
					"origin": [
						980,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:front"
				},
				"isContainer": true
			},
			"index": "aW"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					19.5,
					-13.5
				],
				[
					19.5,
					-108.5
				],
				[
					0,
					-95
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
			"id": "6QPedSKP",
			"type": "line",
			"x": 1215,
			"y": 420,
			"width": 19.5,
			"height": 108.5,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "#bc8845",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 1966,
			"version": 2,
			"versionNonce": 1549642817,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064843,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-V",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-V",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-V",
					"objectId": "hbm-V",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 1215,
						"y": 420,
						"points": [
							[
								0,
								0
							],
							[
								19.5,
								-13.5
							],
							[
								19.5,
								-108.5
							],
							[
								0,
								-95
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 235,
						"depth": 30,
						"height": 95
					},
					"origin": [
						980,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:side"
				},
				"isContainer": true
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
					235,
					0
				],
				[
					254.5,
					-13.5
				],
				[
					19.5,
					-13.5
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
			"id": "oBBcx4UC",
			"type": "line",
			"x": 980,
			"y": 325,
			"width": 254.5,
			"height": 13.5,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "#f5f8fa",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 83534,
			"version": 2,
			"versionNonce": 1657992271,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064843,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-V",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-V",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-V",
					"objectId": "hbm-V",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 980,
						"y": 325,
						"points": [
							[
								0,
								0
							],
							[
								235,
								0
							],
							[
								254.5,
								-13.5
							],
							[
								19.5,
								-13.5
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 235,
						"depth": 30,
						"height": 95
					},
					"origin": [
						980,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:top"
				},
				"isContainer": true
			},
			"index": "aY"
		},
		{
			"id": "aNARECa7",
			"type": "rectangle",
			"x": 980,
			"y": 372.5,
			"width": 235,
			"height": 23.75,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "#bc8845",
			"fillStyle": "solid",
			"strokeWidth": 1.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 75245,
			"version": 2,
			"versionNonce": 524319777,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064843,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-V:active",
					"role": "container"
				},
				"isContainer": true,
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:active"
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
					235,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "EKZhkbEH",
			"type": "line",
			"x": 980,
			"y": 348.75,
			"width": 235,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 10983,
			"version": 2,
			"versionNonce": 1345163887,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064843,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-V:row:1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:row:1"
				}
			},
			"index": "aa"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					235,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "Tq2m9c9F",
			"type": "line",
			"x": 980,
			"y": 372.5,
			"width": 235,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 57558,
			"version": 2,
			"versionNonce": 1090408449,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064843,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-V:row:2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:row:2"
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
					235,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "tsuiad3L",
			"type": "line",
			"x": 980,
			"y": 396.25,
			"width": 235,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 83098,
			"version": 2,
			"versionNonce": 282029199,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064843,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-V:row:3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:row:3"
				}
			},
			"index": "ac"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "v0Ag9QSa",
			"type": "line",
			"x": 1038.75,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 41444,
			"version": 2,
			"versionNonce": 932620257,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064843,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-V:col:1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:col:1"
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
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "hsDRNRtU",
			"type": "line",
			"x": 1097.5,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 76000,
			"version": 2,
			"versionNonce": 812712623,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064843,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-V:col:2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:col:2"
				}
			},
			"index": "ae"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "68EDYcNC",
			"type": "line",
			"x": 1156.25,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 14479,
			"version": 2,
			"versionNonce": 219743169,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064843,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-V:col:3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:col:3"
				}
			},
			"index": "af"
		},
		{
			"text": "V",
			"fontSize": 36,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "lI4bu7ru",
			"type": "text",
			"x": 980,
			"y": 260,
			"width": 24.01171875,
			"height": 45,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 2333,
			"version": 2,
			"versionNonce": 800773327,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064844,
			"containerId": null,
			"originalText": "V",
			"rawText": "V",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-V:label",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:label"
				},
				"bold": true
			},
			"index": "ag"
		},
		{
			"id": "Ej8NZNxr",
			"type": "image",
			"x": 988,
			"y": 437,
			"width": 60.199999999999996,
			"height": 15.399999999999999,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 400,
			"version": 2,
			"versionNonce": 1571087265,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064849,
			"fileId": "ab22d2d326f7a33c02d94b7dec1d76a051dabe2b",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-V:shape",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-V:shape"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "ah"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					185,
					0
				],
				[
					185,
					-95
				],
				[
					0,
					-95
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
			"id": "Q0nXH8sG",
			"type": "line",
			"x": 1650,
			"y": 420,
			"width": 185,
			"height": 95,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "#e6dff0",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 41114,
			"version": 2,
			"versionNonce": 1715823343,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064849,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-O",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-O",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-O",
					"objectId": "hbm-O",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 1650,
						"y": 420,
						"points": [
							[
								0,
								0
							],
							[
								185,
								0
							],
							[
								185,
								-95
							],
							[
								0,
								-95
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 185,
						"depth": 30,
						"height": 95
					},
					"origin": [
						1650,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:front"
				},
				"isContainer": true
			},
			"index": "ai"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					19.5,
					-13.5
				],
				[
					19.5,
					-108.5
				],
				[
					0,
					-95
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
			"id": "fApjGLo5",
			"type": "line",
			"x": 1835,
			"y": 420,
			"width": 19.5,
			"height": 108.5,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "#8570a5",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 51461,
			"version": 2,
			"versionNonce": 359253889,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064850,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-O",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-O",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-O",
					"objectId": "hbm-O",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 1835,
						"y": 420,
						"points": [
							[
								0,
								0
							],
							[
								19.5,
								-13.5
							],
							[
								19.5,
								-108.5
							],
							[
								0,
								-95
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 185,
						"depth": 30,
						"height": 95
					},
					"origin": [
						1650,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:side"
				},
				"isContainer": true
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
					185,
					0
				],
				[
					204.5,
					-13.5
				],
				[
					19.5,
					-13.5
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
			"id": "89FAB9fI",
			"type": "line",
			"x": 1650,
			"y": 325,
			"width": 204.5,
			"height": 13.5,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "#f5f8fa",
			"fillStyle": "solid",
			"strokeWidth": 1.5,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 80046,
			"version": 2,
			"versionNonce": 614018319,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064850,
			"polygon": true,
			"customData": {
				"agentPrimitive": {
					"instanceId": "illustration:tensors:hbm-O",
					"kind": "projected_box",
					"role": "face"
				},
				"agentDiagram": {
					"logicalId": "hbm-O",
					"role": "physical-body"
				},
				"technicalIllustration": {
					"itemId": "hbm-O",
					"objectId": "hbm-O",
					"viewId": "tensors",
					"role": "body",
					"expected": {
						"x": 1650,
						"y": 325,
						"points": [
							[
								0,
								0
							],
							[
								185,
								0
							],
							[
								204.5,
								-13.5
							],
							[
								19.5,
								-13.5
							],
							[
								0,
								0
							]
						]
					},
					"model": {
						"u": 0,
						"v": 0,
						"z": 0,
						"width": 185,
						"depth": 30,
						"height": 95
					},
					"origin": [
						1650,
						420
					],
					"projection": [
						0.65,
						-0.45
					]
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:top"
				},
				"isContainer": true
			},
			"index": "ak"
		},
		{
			"id": "LNuP8s2E",
			"type": "rectangle",
			"x": 1650,
			"y": 348.75,
			"width": 185,
			"height": 23.75,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "#8570a5",
			"fillStyle": "solid",
			"strokeWidth": 1.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 1507,
			"version": 2,
			"versionNonce": 1856450401,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064850,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-O:active",
					"role": "container"
				},
				"isContainer": true,
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:active"
				}
			},
			"index": "al"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					185,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "pX44kM7R",
			"type": "line",
			"x": 1650,
			"y": 348.75,
			"width": 185,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 29761,
			"version": 2,
			"versionNonce": 372159279,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064850,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-O:row:1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:row:1"
				}
			},
			"index": "am"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					185,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "alRoBmeP",
			"type": "line",
			"x": 1650,
			"y": 372.5,
			"width": 185,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 40760,
			"version": 2,
			"versionNonce": 799841089,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064850,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-O:row:2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:row:2"
				}
			},
			"index": "an"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					185,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "fRYZ6cI9",
			"type": "line",
			"x": 1650,
			"y": 396.25,
			"width": 185,
			"height": 0,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 41372,
			"version": 2,
			"versionNonce": 1668183375,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064850,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-O:row:3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:row:3"
				}
			},
			"index": "ao"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "s8vP0eto",
			"type": "line",
			"x": 1696.25,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 15411,
			"version": 2,
			"versionNonce": 685345569,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064850,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-O:col:1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:col:1"
				}
			},
			"index": "ap"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "CyQt510q",
			"type": "line",
			"x": 1742.5,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 48971,
			"version": 2,
			"versionNonce": 330363759,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064850,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-O:col:2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:col:2"
				}
			},
			"index": "aq"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					95
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "zULhTSsP",
			"type": "line",
			"x": 1788.75,
			"y": 325,
			"width": 0,
			"height": 95,
			"angle": 0,
			"strokeColor": "#91a7b1",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.9,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 38048,
			"version": 2,
			"versionNonce": 1922924289,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064850,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-O:col:3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:col:3"
				}
			},
			"index": "ar"
		},
		{
			"text": "O",
			"fontSize": 36,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "LbAKoi38",
			"type": "text",
			"x": 1650,
			"y": 260,
			"width": 28.001953125,
			"height": 45,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 93449,
			"version": 2,
			"versionNonce": 792636815,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064851,
			"containerId": null,
			"originalText": "O",
			"rawText": "O",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-O:label",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:label"
				},
				"bold": true
			},
			"index": "as"
		},
		{
			"text": "Rows are partitioned into blocks; grids are schematic.",
			"fontSize": 18,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "ULl0enVb",
			"type": "text",
			"x": 1300,
			"y": 485,
			"width": 426.1904296875,
			"height": 22.5,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 81767,
			"version": 2,
			"versionNonce": 1803024097,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064852,
			"containerId": null,
			"originalText": "Rows are partitioned into blocks; grids are schematic.",
			"rawText": "Rows are partitioned into blocks; grids are schematic.",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "input-shape-note",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "input-shape-note"
				}
			},
			"index": "at"
		},
		{
			"text": "OUTPUT",
			"fontSize": 19,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "b5GfCB7C",
			"type": "text",
			"x": 1650,
			"y": 235,
			"width": 78.10595703125,
			"height": 23.75,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 39417,
			"version": 2,
			"versionNonce": 558900143,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064852,
			"containerId": null,
			"originalText": "OUTPUT",
			"rawText": "OUTPUT",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "output-heading",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "output-heading"
				},
				"bold": true
			},
			"index": "au"
		},
		{
			"id": "anQOHA3U",
			"type": "image",
			"x": 1730,
			"y": 272,
			"width": 60.199999999999996,
			"height": 15.399999999999999,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 32303,
			"version": 2,
			"versionNonce": 1979216577,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064857,
			"fileId": "39e7d172f711551eb04b5c5ea06a68497612f067",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "hbm-O:shape",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "hbm-O:shape"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "av"
		},
		{
			"id": "w2BVhuJV",
			"type": "rectangle",
			"x": 75,
			"y": 535,
			"width": 1345,
			"height": 580,
			"angle": 0,
			"strokeColor": "#b3c3cb",
			"backgroundColor": "#f6f9fa",
			"fillStyle": "solid",
			"strokeWidth": 1.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": {
				"type": 3,
				"value": 12,
				"roundType": "arc"
			},
			"seed": 18354,
			"version": 2,
			"versionNonce": 1510856143,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064857,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "workspace",
					"role": "container"
				},
				"isContainer": true,
				"dsl": {
					"document": "flashattention-flagship",
					"key": "workspace"
				}
			},
			"index": "aw"
		},
		{
			"text": "02 / ON-CHIP WORKING SET",
			"fontSize": 24,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "vbMYVjui",
			"type": "text",
			"x": 100,
			"y": 548,
			"width": 325.37109375,
			"height": 30,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 4727,
			"version": 2,
			"versionNonce": 1992192673,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064857,
			"containerId": null,
			"originalText": "02 / ON-CHIP WORKING SET",
			"rawText": "02 / ON-CHIP WORKING SET",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "chip-heading",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "chip-heading"
				},
				"bold": true
			},
			"index": "ax"
		},
		{
			"text": "SRAM + registers / one query block",
			"fontSize": 20,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "oEE8uuZb",
			"type": "text",
			"x": 100,
			"y": 586,
			"width": 315.13671875,
			"height": 25,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 3083,
			"version": 2,
			"versionNonce": 814760943,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064858,
			"containerId": null,
			"originalText": "SRAM + registers / one query block",
			"rawText": "SRAM + registers / one query block",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "chip-note",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "chip-note"
				}
			},
			"index": "ay"
		},
		{
			"id": "f3xjM3ct",
			"type": "rectangle",
			"x": 170,
			"y": 710,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 38266,
			"version": 2,
			"versionNonce": 309950081,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064858,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:0:0"
				}
			},
			"index": "az"
		},
		{
			"id": "JSDchfeh",
			"type": "rectangle",
			"x": 202,
			"y": 710,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 74717,
			"version": 2,
			"versionNonce": 81784335,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064858,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:0:1"
				}
			},
			"index": "b00"
		},
		{
			"id": "LJ6Zpf2B",
			"type": "rectangle",
			"x": 234,
			"y": 710,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 98542,
			"version": 2,
			"versionNonce": 736689761,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064858,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:0:2"
				}
			},
			"index": "b01"
		},
		{
			"id": "ix5xqFFb",
			"type": "rectangle",
			"x": 266,
			"y": 710,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 54967,
			"version": 2,
			"versionNonce": 569725999,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064858,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:0:3"
				}
			},
			"index": "b02"
		},
		{
			"id": "DBM6yq0v",
			"type": "rectangle",
			"x": 170,
			"y": 742,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 30941,
			"version": 2,
			"versionNonce": 568101441,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064858,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:1:0"
				}
			},
			"index": "b03"
		},
		{
			"id": "m37Z2vIW",
			"type": "rectangle",
			"x": 202,
			"y": 742,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 64053,
			"version": 2,
			"versionNonce": 1605957199,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064858,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:1:1"
				}
			},
			"index": "b04"
		},
		{
			"id": "Y7rTH7mS",
			"type": "rectangle",
			"x": 234,
			"y": 742,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 55738,
			"version": 2,
			"versionNonce": 1295227425,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064858,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:1:2"
				}
			},
			"index": "b05"
		},
		{
			"id": "zdXv4sQl",
			"type": "rectangle",
			"x": 266,
			"y": 742,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 50200,
			"version": 2,
			"versionNonce": 84104303,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064858,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:1:3"
				}
			},
			"index": "b06"
		},
		{
			"id": "1OuZ3Fnm",
			"type": "rectangle",
			"x": 170,
			"y": 774,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 73346,
			"version": 2,
			"versionNonce": 1054715393,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064858,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:2:0"
				}
			},
			"index": "b07"
		},
		{
			"id": "4OswJOSm",
			"type": "rectangle",
			"x": 202,
			"y": 774,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 45993,
			"version": 2,
			"versionNonce": 1771892367,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064859,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:2:1"
				}
			},
			"index": "b08"
		},
		{
			"id": "lOJYE19Z",
			"type": "rectangle",
			"x": 234,
			"y": 774,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 26190,
			"version": 2,
			"versionNonce": 1037714913,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064859,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:2:2"
				}
			},
			"index": "b09"
		},
		{
			"id": "AdsvAx2V",
			"type": "rectangle",
			"x": 266,
			"y": 774,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 38221,
			"version": 2,
			"versionNonce": 1480475823,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064859,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:2:3"
				}
			},
			"index": "b0A"
		},
		{
			"id": "8rTbu0f6",
			"type": "rectangle",
			"x": 170,
			"y": 806,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 11735,
			"version": 2,
			"versionNonce": 87613889,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064859,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:3:0"
				}
			},
			"index": "b0B"
		},
		{
			"id": "Af8psZBe",
			"type": "rectangle",
			"x": 202,
			"y": 806,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 76066,
			"version": 2,
			"versionNonce": 814733007,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064859,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:3:1"
				}
			},
			"index": "b0C"
		},
		{
			"id": "9EvVR2X3",
			"type": "rectangle",
			"x": 234,
			"y": 806,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 30453,
			"version": 2,
			"versionNonce": 1108935073,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064859,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:3:2"
				}
			},
			"index": "b0D"
		},
		{
			"id": "cRcNl4yN",
			"type": "rectangle",
			"x": 266,
			"y": 806,
			"width": 29,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 36815,
			"version": 2,
			"versionNonce": 1227498735,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"W2at4Unv"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064859,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:query-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-tile:3:3"
				}
			},
			"index": "b0E"
		},
		{
			"id": "0NL913n7",
			"type": "image",
			"x": 176,
			"y": 661,
			"width": 28.8,
			"height": 24,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 86884,
			"version": 2,
			"versionNonce": 1370105217,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064863,
			"fileId": "eef131b98df998bea42248bd3dd339cbc48ba395",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-name",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-name"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b0F"
		},
		{
			"id": "njxzq4Hl",
			"type": "image",
			"x": 170,
			"y": 853,
			"width": 61.1,
			"height": 18.2,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d4e5ed",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 63283,
			"version": 2,
			"versionNonce": 295022351,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064870,
			"fileId": "68d5c4cec905d7e0ffbabd57534f0ed8c68720a0",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-shape",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-shape"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b0G"
		},
		{
			"text": "Held through the\nK/V sweep",
			"fontSize": 22,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "h9zFklAd",
			"type": "text",
			"x": 170,
			"y": 904,
			"width": 162.6689453125,
			"height": 55,
			"angle": 0,
			"strokeColor": "#5e8faa",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 88213,
			"version": 2,
			"versionNonce": 1059835233,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064870,
			"containerId": null,
			"originalText": "Held through the\nK/V sweep",
			"rawText": "Held through the\nK/V sweep",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-held",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-held"
				}
			},
			"index": "b0H"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					-192,
					0
				],
				[
					-192,
					343
				],
				[
					-95,
					343
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "6YL0aED5",
			"type": "arrow",
			"x": 257,
			"y": 427,
			"width": 192,
			"height": 343,
			"angle": 0,
			"strokeColor": "#5e8faa",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 48028,
			"version": 2,
			"versionNonce": 1951069487,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064870,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "load-query",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "load-query"
				}
			},
			"index": "b0I"
		},
		{
			"id": "6Mq3Q8Mk",
			"type": "rectangle",
			"x": 475,
			"y": 645,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 77236,
			"version": 2,
			"versionNonce": 32340289,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064870,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:0:0"
				}
			},
			"index": "b0J"
		},
		{
			"id": "rd892o6V",
			"type": "rectangle",
			"x": 515,
			"y": 645,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 35832,
			"version": 2,
			"versionNonce": 2024961871,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064870,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:0:1"
				}
			},
			"index": "b0K"
		},
		{
			"id": "w9irnnpz",
			"type": "rectangle",
			"x": 555,
			"y": 645,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 42629,
			"version": 2,
			"versionNonce": 2068752673,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064870,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:0:2"
				}
			},
			"index": "b0L"
		},
		{
			"id": "qlsWEhQR",
			"type": "rectangle",
			"x": 595,
			"y": 645,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 69784,
			"version": 2,
			"versionNonce": 623162735,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064870,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:0:3"
				}
			},
			"index": "b0M"
		},
		{
			"id": "YjbBKQ6U",
			"type": "rectangle",
			"x": 475,
			"y": 667,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 11261,
			"version": 2,
			"versionNonce": 884923649,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:1:0"
				}
			},
			"index": "b0N"
		},
		{
			"id": "5e7L71Bc",
			"type": "rectangle",
			"x": 515,
			"y": 667,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 94538,
			"version": 2,
			"versionNonce": 552218511,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:1:1"
				}
			},
			"index": "b0O"
		},
		{
			"id": "QpQCYdjP",
			"type": "rectangle",
			"x": 555,
			"y": 667,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 68088,
			"version": 2,
			"versionNonce": 1572705505,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:1:2"
				}
			},
			"index": "b0P"
		},
		{
			"id": "3XB1O4IE",
			"type": "rectangle",
			"x": 595,
			"y": 667,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 52514,
			"version": 2,
			"versionNonce": 372991407,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:1:3"
				}
			},
			"index": "b0Q"
		},
		{
			"id": "Qy2dsDn8",
			"type": "rectangle",
			"x": 475,
			"y": 689,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 49184,
			"version": 2,
			"versionNonce": 165302465,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:2:0"
				}
			},
			"index": "b0R"
		},
		{
			"id": "8dYMZQnt",
			"type": "rectangle",
			"x": 515,
			"y": 689,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 10868,
			"version": 2,
			"versionNonce": 1413535695,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:2:1"
				}
			},
			"index": "b0S"
		},
		{
			"id": "3EgvrYMg",
			"type": "rectangle",
			"x": 555,
			"y": 689,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 94146,
			"version": 2,
			"versionNonce": 783585441,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:2:2"
				}
			},
			"index": "b0T"
		},
		{
			"id": "VHdA7qE1",
			"type": "rectangle",
			"x": 595,
			"y": 689,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 23208,
			"version": 2,
			"versionNonce": 823330287,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:2:3"
				}
			},
			"index": "b0U"
		},
		{
			"id": "zq7Nb7hB",
			"type": "rectangle",
			"x": 475,
			"y": 711,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 75008,
			"version": 2,
			"versionNonce": 1643893889,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:3:0"
				}
			},
			"index": "b0V"
		},
		{
			"id": "jCkR9KJA",
			"type": "rectangle",
			"x": 515,
			"y": 711,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 95083,
			"version": 2,
			"versionNonce": 733638671,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:3:1"
				}
			},
			"index": "b0W"
		},
		{
			"id": "i1Q38wQS",
			"type": "rectangle",
			"x": 555,
			"y": 711,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 98019,
			"version": 2,
			"versionNonce": 1466932321,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:3:2"
				}
			},
			"index": "b0X"
		},
		{
			"id": "SMHDEnU8",
			"type": "rectangle",
			"x": 595,
			"y": 711,
			"width": 37,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 96287,
			"version": 2,
			"versionNonce": 1311741487,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"bHmqlwd7"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064871,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:key-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-tile:3:3"
				}
			},
			"index": "b0Y"
		},
		{
			"id": "RHMJwHyv",
			"type": "image",
			"x": 475,
			"y": 607,
			"width": 33.599999999999994,
			"height": 29.4,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 88226,
			"version": 2,
			"versionNonce": 517957697,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064875,
			"fileId": "f7144b3aadc70a777e98f23882b5cdcfbc976c99",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-name",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-name"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b0Z"
		},
		{
			"id": "VrI08f9l",
			"type": "image",
			"x": 646,
			"y": 668,
			"width": 56.4,
			"height": 16.8,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 3756,
			"version": 2,
			"versionNonce": 1331361871,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064879,
			"fileId": "d29fd6d9ce5b9f68cd10c197bcd2078df9955f69",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-shape",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-shape"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b0a"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					85
				],
				[
					-86,
					85
				],
				[
					-86,
					210
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "So3zHh7K",
			"type": "arrow",
			"x": 687,
			"y": 427,
			"width": 86,
			"height": 210,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 88982,
			"version": 2,
			"versionNonce": 573224993,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "load-key",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "load-key"
				}
			},
			"index": "b0b"
		},
		{
			"id": "pDNhRfen",
			"type": "rectangle",
			"x": 1120,
			"y": 645,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 429,
			"version": 2,
			"versionNonce": 1964316271,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:0:0"
				}
			},
			"index": "b0c"
		},
		{
			"id": "aK6I65N2",
			"type": "rectangle",
			"x": 1150,
			"y": 645,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 87730,
			"version": 2,
			"versionNonce": 1665207297,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:0:1"
				}
			},
			"index": "b0d"
		},
		{
			"id": "x0sJCiSP",
			"type": "rectangle",
			"x": 1180,
			"y": 645,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 98465,
			"version": 2,
			"versionNonce": 908488847,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:0:2"
				}
			},
			"index": "b0e"
		},
		{
			"id": "ckLyUXUV",
			"type": "rectangle",
			"x": 1210,
			"y": 645,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 79179,
			"version": 2,
			"versionNonce": 2049041377,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:0:3"
				}
			},
			"index": "b0f"
		},
		{
			"id": "WyPAPaqI",
			"type": "rectangle",
			"x": 1120,
			"y": 667,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 92293,
			"version": 2,
			"versionNonce": 474449583,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:1:0"
				}
			},
			"index": "b0g"
		},
		{
			"id": "GsBeRwlI",
			"type": "rectangle",
			"x": 1150,
			"y": 667,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 67579,
			"version": 2,
			"versionNonce": 1390198721,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:1:1"
				}
			},
			"index": "b0h"
		},
		{
			"id": "MiOvVcCc",
			"type": "rectangle",
			"x": 1180,
			"y": 667,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 64900,
			"version": 2,
			"versionNonce": 1713428687,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:1:2"
				}
			},
			"index": "b0i"
		},
		{
			"id": "fNpHgSPD",
			"type": "rectangle",
			"x": 1210,
			"y": 667,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 29130,
			"version": 2,
			"versionNonce": 730931105,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:1:3"
				}
			},
			"index": "b0j"
		},
		{
			"id": "quUepcn8",
			"type": "rectangle",
			"x": 1120,
			"y": 689,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 70186,
			"version": 2,
			"versionNonce": 1766516463,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:2:0"
				}
			},
			"index": "b0k"
		},
		{
			"id": "8UKnVANj",
			"type": "rectangle",
			"x": 1150,
			"y": 689,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 88838,
			"version": 2,
			"versionNonce": 1382974337,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064880,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:2:1"
				}
			},
			"index": "b0l"
		},
		{
			"id": "6jjBw43G",
			"type": "rectangle",
			"x": 1180,
			"y": 689,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 55832,
			"version": 2,
			"versionNonce": 877539599,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064881,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:2:2"
				}
			},
			"index": "b0m"
		},
		{
			"id": "nZJfulJC",
			"type": "rectangle",
			"x": 1210,
			"y": 689,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 62637,
			"version": 2,
			"versionNonce": 599026529,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064881,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:2:3"
				}
			},
			"index": "b0n"
		},
		{
			"id": "Jie5y5oj",
			"type": "rectangle",
			"x": 1120,
			"y": 711,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 76255,
			"version": 2,
			"versionNonce": 1889744687,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064881,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:3:0"
				}
			},
			"index": "b0o"
		},
		{
			"id": "PVwDpLf4",
			"type": "rectangle",
			"x": 1150,
			"y": 711,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 67257,
			"version": 2,
			"versionNonce": 1202870081,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064881,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:3:1"
				}
			},
			"index": "b0p"
		},
		{
			"id": "arDHH21g",
			"type": "rectangle",
			"x": 1180,
			"y": 711,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 59660,
			"version": 2,
			"versionNonce": 78805327,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064881,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:3:2"
				}
			},
			"index": "b0q"
		},
		{
			"id": "fSo1mSOq",
			"type": "rectangle",
			"x": 1210,
			"y": 711,
			"width": 27,
			"height": 19,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 72447,
			"version": 2,
			"versionNonce": 818399009,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"g9lhqEUp"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064881,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:value-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-tile:3:3"
				}
			},
			"index": "b0r"
		},
		{
			"id": "i0JVRxu5",
			"type": "image",
			"x": 1120,
			"y": 607,
			"width": 22.4,
			"height": 22.4,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 92303,
			"version": 2,
			"versionNonce": 1976858479,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064885,
			"fileId": "993bee1faf6bf07cdea6a3c1dc8a76c212770b70",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-name",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-name"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b0s"
		},
		{
			"id": "wlLwbwzn",
			"type": "image",
			"x": 1251,
			"y": 667,
			"width": 56.4,
			"height": 16.8,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 58573,
			"version": 2,
			"versionNonce": 1499740929,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064890,
			"fileId": "9f279b4f520866d01df260c3ece33dd39e7db7e2",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-shape",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-shape"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b0t"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					85
				],
				[
					91,
					85
				],
				[
					91,
					210
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "nHGJAyDY",
			"type": "arrow",
			"x": 1117,
			"y": 427,
			"width": 91,
			"height": 210,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 57228,
			"version": 2,
			"versionNonce": 173126031,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064890,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "load-value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "load-value"
				}
			},
			"index": "b0u"
		},
		{
			"text": "K/V BLOCK",
			"fontSize": 18,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "rGSE7Xjl",
			"type": "text",
			"x": 800,
			"y": 610,
			"width": 95.0361328125,
			"height": 22.5,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 75825,
			"version": 2,
			"versionNonce": 1107768033,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064891,
			"containerId": null,
			"originalText": "K/V BLOCK",
			"rawText": "K/V BLOCK",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "sweep-caption",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "sweep-caption"
				}
			},
			"index": "b0v"
		},
		{
			"id": "OB2CXUA1",
			"type": "ellipse",
			"x": 790,
			"y": 645,
			"width": 34,
			"height": 34,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 1.6,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 42756,
			"version": 2,
			"versionNonce": 727885743,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064891,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "sweep-0",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "sweep-0"
				}
			},
			"index": "b0w"
		},
		{
			"text": "1",
			"fontSize": 20,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "3Z9qZABy",
			"type": "text",
			"x": 801.4384765625,
			"y": 650,
			"width": 11.123046875,
			"height": 25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 37555,
			"version": 2,
			"versionNonce": 792735425,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064891,
			"containerId": null,
			"originalText": "1",
			"rawText": "1",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "sweep-number-0",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "sweep-number-0"
				}
			},
			"index": "b0x"
		},
		{
			"id": "xSzrn3sL",
			"type": "ellipse",
			"x": 843,
			"y": 645,
			"width": 34,
			"height": 34,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 1.6,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 97806,
			"version": 2,
			"versionNonce": 120576463,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064891,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "sweep-1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "sweep-1"
				}
			},
			"index": "b0y"
		},
		{
			"text": "2",
			"fontSize": 20,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "IqrAqGQO",
			"type": "text",
			"x": 854.4384765625,
			"y": 650,
			"width": 11.123046875,
			"height": 25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 61477,
			"version": 2,
			"versionNonce": 665759393,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064892,
			"containerId": null,
			"originalText": "2",
			"rawText": "2",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "sweep-number-1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "sweep-number-1"
				}
			},
			"index": "b0z"
		},
		{
			"id": "YOAJt8Lf",
			"type": "ellipse",
			"x": 896,
			"y": 645,
			"width": 34,
			"height": 34,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 1.6,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 83726,
			"version": 2,
			"versionNonce": 1926350831,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064892,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "sweep-2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "sweep-2"
				}
			},
			"index": "b10"
		},
		{
			"text": "3",
			"fontSize": 20,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "3HoGDT8u",
			"type": "text",
			"x": 907.4384765625,
			"y": 650,
			"width": 11.123046875,
			"height": 25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 40877,
			"version": 2,
			"versionNonce": 839004801,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064892,
			"containerId": null,
			"originalText": "3",
			"rawText": "3",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "sweep-number-2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "sweep-number-2"
				},
				"bold": true
			},
			"index": "b11"
		},
		{
			"id": "5XsAlOee",
			"type": "ellipse",
			"x": 949,
			"y": 645,
			"width": 34,
			"height": 34,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#edf1f3",
			"fillStyle": "solid",
			"strokeWidth": 1.6,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 37787,
			"version": 2,
			"versionNonce": 206631439,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064892,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "sweep-3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "sweep-3"
				}
			},
			"index": "b12"
		},
		{
			"text": "4",
			"fontSize": 20,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "Lg5c6mDS",
			"type": "text",
			"x": 960.4384765625,
			"y": 650,
			"width": 11.123046875,
			"height": 25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 41854,
			"version": 2,
			"versionNonce": 1392130657,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064892,
			"containerId": null,
			"originalText": "4",
			"rawText": "4",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "sweep-number-3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "sweep-number-3"
				}
			},
			"index": "b13"
		},
		{
			"text": "Block 3 of 4",
			"fontSize": 18,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "lFPH9z1F",
			"type": "text",
			"x": 800,
			"y": 693,
			"width": 94.0517578125,
			"height": 22.5,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 10303,
			"version": 2,
			"versionNonce": 480630831,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064893,
			"containerId": null,
			"originalText": "Block 3 of 4",
			"rawText": "Block 3 of 4",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "sweep-detail",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "sweep-detail"
				}
			},
			"index": "b14"
		},
		{
			"id": "wIJUNnEW",
			"type": "image",
			"x": 475,
			"y": 745,
			"width": 29,
			"height": 23.2,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 41113,
			"version": 2,
			"versionNonce": 1264993857,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064899,
			"fileId": "ea4991917a97ab1abfadc3f69e0582bdd6cb9a40",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-name",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-name"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b15"
		},
		{
			"id": "zP5qJ91H",
			"type": "rectangle",
			"x": 475,
			"y": 795,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 29424,
			"version": 3,
			"versionNonce": 653287568,
			"updated": 1792682434624,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064899,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:0:0"
				}
			},
			"index": "b16"
		},
		{
			"text": "-1.3",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "w2Ye4AoZ",
			"type": "text",
			"x": 479.353271484375,
			"y": 803.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 75983,
			"version": 3,
			"versionNonce": 137156106,
			"updated": 1792682434633,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064900,
			"containerId": null,
			"originalText": "-1.3",
			"rawText": "-1.3",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:0:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:0:0:value"
				}
			},
			"index": "b17"
		},
		{
			"id": "jkMr0Jrh",
			"type": "rectangle",
			"x": 516,
			"y": 795,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 48439,
			"version": 3,
			"versionNonce": 640307802,
			"updated": 1792682434633,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064901,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:0:1"
				}
			},
			"index": "b18"
		},
		{
			"text": "-1.3",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "MyomBxyv",
			"type": "text",
			"x": 520.353271484375,
			"y": 803.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 63325,
			"version": 3,
			"versionNonce": 761554987,
			"updated": 1792682434639,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064901,
			"containerId": null,
			"originalText": "-1.3",
			"rawText": "-1.3",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:0:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:0:1:value"
				}
			},
			"index": "b19"
		},
		{
			"id": "5yG1iJVt",
			"type": "rectangle",
			"x": 557,
			"y": 795,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 22602,
			"version": 3,
			"versionNonce": 655981752,
			"updated": 1792682434639,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064902,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:0:2"
				}
			},
			"index": "b1A"
		},
		{
			"text": "-0.8",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "PaQp78eg",
			"type": "text",
			"x": 561.353271484375,
			"y": 803.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 3454,
			"version": 3,
			"versionNonce": 848778335,
			"updated": 1792682434645,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064902,
			"containerId": null,
			"originalText": "-0.8",
			"rawText": "-0.8",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:0:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:0:2:value"
				}
			},
			"index": "b1B"
		},
		{
			"id": "YWXM5Bi1",
			"type": "rectangle",
			"x": 598,
			"y": 795,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#cebdde",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 64743,
			"version": 3,
			"versionNonce": 656363825,
			"updated": 1792682434645,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064902,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:0:3"
				}
			},
			"index": "b1C"
		},
		{
			"text": "-0.3",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "fAydIV7k",
			"type": "text",
			"x": 602.353271484375,
			"y": 803.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 25749,
			"version": 3,
			"versionNonce": 388408669,
			"updated": 1792682434651,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064903,
			"containerId": null,
			"originalText": "-0.3",
			"rawText": "-0.3",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:0:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:0:3:value"
				}
			},
			"index": "b1D"
		},
		{
			"id": "pbWi1mj3",
			"type": "rectangle",
			"x": 475,
			"y": 836,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 56995,
			"version": 3,
			"versionNonce": 364569495,
			"updated": 1792682434651,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064903,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:1:0"
				}
			},
			"index": "b1E"
		},
		{
			"text": "-0.6",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "lHRo6PTk",
			"type": "text",
			"x": 479.353271484375,
			"y": 844.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 49120,
			"version": 3,
			"versionNonce": 69527052,
			"updated": 1792682434658,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064903,
			"containerId": null,
			"originalText": "-0.6",
			"rawText": "-0.6",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:1:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:1:0:value"
				}
			},
			"index": "b1F"
		},
		{
			"id": "SZgMnOxW",
			"type": "rectangle",
			"x": 516,
			"y": 836,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 44348,
			"version": 3,
			"versionNonce": 432553903,
			"updated": 1792682434658,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064904,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:1:1"
				}
			},
			"index": "b1G"
		},
		{
			"text": "-1.0",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "EY9gR9A5",
			"type": "text",
			"x": 520.353271484375,
			"y": 844.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 52578,
			"version": 3,
			"versionNonce": 880063369,
			"updated": 1792682434664,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064904,
			"containerId": null,
			"originalText": "-1.0",
			"rawText": "-1.0",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:1:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:1:1:value"
				}
			},
			"index": "b1H"
		},
		{
			"id": "iqAJjzQH",
			"type": "rectangle",
			"x": 557,
			"y": 836,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 9299,
			"version": 3,
			"versionNonce": 457675812,
			"updated": 1792682434664,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064904,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:1:2"
				}
			},
			"index": "b1I"
		},
		{
			"text": "-1.1",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "88RL1Q0T",
			"type": "text",
			"x": 561.353271484375,
			"y": 844.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 28249,
			"version": 3,
			"versionNonce": 338960619,
			"updated": 1792682434669,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064905,
			"containerId": null,
			"originalText": "-1.1",
			"rawText": "-1.1",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:1:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:1:2:value"
				}
			},
			"index": "b1J"
		},
		{
			"id": "9gBIozFF",
			"type": "rectangle",
			"x": 598,
			"y": 836,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 30585,
			"version": 3,
			"versionNonce": 430066860,
			"updated": 1792682434669,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064905,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:1:3"
				}
			},
			"index": "b1K"
		},
		{
			"text": "-1.1",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "rROdPLhB",
			"type": "text",
			"x": 602.353271484375,
			"y": 844.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 20380,
			"version": 3,
			"versionNonce": 224404097,
			"updated": 1792682434674,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064905,
			"containerId": null,
			"originalText": "-1.1",
			"rawText": "-1.1",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:1:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:1:3:value"
				}
			},
			"index": "b1L"
		},
		{
			"id": "sJRbhNMR",
			"type": "rectangle",
			"x": 475,
			"y": 877,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#b59ccf",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 71210,
			"version": 3,
			"versionNonce": 298467529,
			"updated": 1792682434675,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064905,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:2:0"
				}
			},
			"index": "b1M"
		},
		{
			"text": "0.5",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "1rGei7G8",
			"type": "text",
			"x": 482.183837890625,
			"y": 885.375,
			"width": 23.63232421875,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 13495,
			"version": 3,
			"versionNonce": 608764640,
			"updated": 1792682434680,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064906,
			"containerId": null,
			"originalText": "0.5",
			"rawText": "0.5",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:2:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:2:0:value"
				}
			},
			"index": "b1N"
		},
		{
			"id": "xc4yrq4f",
			"type": "rectangle",
			"x": 516,
			"y": 877,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#cebdde",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 7227,
			"version": 3,
			"versionNonce": 262893865,
			"updated": 1792682434680,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064906,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:2:1"
				}
			},
			"index": "b1O"
		},
		{
			"text": "-0.1",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "ZltzJqRD",
			"type": "text",
			"x": 520.353271484375,
			"y": 885.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 25973,
			"version": 3,
			"versionNonce": 642612753,
			"updated": 1792682434684,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064906,
			"containerId": null,
			"originalText": "-0.1",
			"rawText": "-0.1",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:2:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:2:1:value"
				}
			},
			"index": "b1P"
		},
		{
			"id": "BXEwBt5c",
			"type": "rectangle",
			"x": 557,
			"y": 877,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 25669,
			"version": 3,
			"versionNonce": 997816454,
			"updated": 1792682434685,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064906,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:2:2"
				}
			},
			"index": "b1Q"
		},
		{
			"text": "-0.9",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "fQiqdx3Z",
			"type": "text",
			"x": 561.353271484375,
			"y": 885.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 20861,
			"version": 3,
			"versionNonce": 477963820,
			"updated": 1792682434689,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064907,
			"containerId": null,
			"originalText": "-0.9",
			"rawText": "-0.9",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:2:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:2:2:value"
				}
			},
			"index": "b1R"
		},
		{
			"id": "iy70YInK",
			"type": "rectangle",
			"x": 598,
			"y": 877,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 96316,
			"version": 3,
			"versionNonce": 48950021,
			"updated": 1792682434689,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064907,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:2:3"
				}
			},
			"index": "b1S"
		},
		{
			"text": "-1.5",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "AaGXzalx",
			"type": "text",
			"x": 602.353271484375,
			"y": 885.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 87331,
			"version": 3,
			"versionNonce": 306144144,
			"updated": 1792682434694,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064907,
			"containerId": null,
			"originalText": "-1.5",
			"rawText": "-1.5",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:2:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:2:3:value"
				}
			},
			"index": "b1T"
		},
		{
			"id": "lfTIsBQJ",
			"type": "rectangle",
			"x": 475,
			"y": 918,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#b59ccf",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 65590,
			"version": 3,
			"versionNonce": 295317296,
			"updated": 1792682434695,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064907,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:3:0"
				}
			},
			"index": "b1U"
		},
		{
			"text": "0.4",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "XhLNwHjH",
			"type": "text",
			"x": 482.183837890625,
			"y": 926.375,
			"width": 23.63232421875,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 46822,
			"version": 3,
			"versionNonce": 538244312,
			"updated": 1792682434704,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064907,
			"containerId": null,
			"originalText": "0.4",
			"rawText": "0.4",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:3:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:3:0:value"
				}
			},
			"index": "b1V"
		},
		{
			"id": "9W0LEzjm",
			"type": "rectangle",
			"x": 516,
			"y": 918,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#cebdde",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 97552,
			"version": 3,
			"versionNonce": 196614854,
			"updated": 1792682434704,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064908,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:3:1"
				}
			},
			"index": "b1W"
		},
		{
			"text": "0.1",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "hGwBLwwU",
			"type": "text",
			"x": 523.183837890625,
			"y": 926.375,
			"width": 23.63232421875,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 11298,
			"version": 3,
			"versionNonce": 921856679,
			"updated": 1792682434709,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064908,
			"containerId": null,
			"originalText": "0.1",
			"rawText": "0.1",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:3:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:3:1:value"
				}
			},
			"index": "b1X"
		},
		{
			"id": "CA2vpeZU",
			"type": "rectangle",
			"x": 557,
			"y": 918,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#cebdde",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 78444,
			"version": 3,
			"versionNonce": 2373796,
			"updated": 1792682434710,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064908,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:3:2"
				}
			},
			"index": "b1Y"
		},
		{
			"text": "-0.4",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "8VEDLdLt",
			"type": "text",
			"x": 561.353271484375,
			"y": 926.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 98769,
			"version": 3,
			"versionNonce": 379939262,
			"updated": 1792682434715,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064909,
			"containerId": null,
			"originalText": "-0.4",
			"rawText": "-0.4",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:3:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:3:2:value"
				}
			},
			"index": "b1Z"
		},
		{
			"id": "obxLvOHd",
			"type": "rectangle",
			"x": 598,
			"y": 918,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 93364,
			"version": 3,
			"versionNonce": 890049160,
			"updated": 1792682434715,
			"isDeleted": false,
			"groupIds": [
				"u1c6yjTx"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064909,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:score-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:3:3"
				}
			},
			"index": "b1a"
		},
		{
			"text": "-0.8",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "PkcCFbcs",
			"type": "text",
			"x": 602.353271484375,
			"y": 926.375,
			"width": 29.29345703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 45741,
			"version": 3,
			"versionNonce": 988444030,
			"updated": 1792682434721,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064909,
			"containerId": null,
			"originalText": "-0.8",
			"rawText": "-0.8",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-tile:3:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-tile:3:3:value"
				}
			},
			"index": "b1b"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					116,
					0
				],
				[
					116,
					43
				],
				[
					165,
					43
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "B8gt9jbu",
			"type": "arrow",
			"x": 302,
			"y": 770,
			"width": 165,
			"height": 43,
			"angle": 0,
			"strokeColor": "#5e8faa",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 19060,
			"version": 2,
			"versionNonce": 651361359,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064910,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "query-to-score",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "query-to-score"
				}
			},
			"index": "b1c"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					47
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "EQFAtm4i",
			"type": "arrow",
			"x": 601,
			"y": 740,
			"width": 0,
			"height": 47,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 93587,
			"version": 2,
			"versionNonce": 556069921,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064910,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "key-to-score",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "key-to-score"
				}
			},
			"index": "b1d"
		},
		{
			"id": "Mhkli5iH",
			"type": "image",
			"x": 655,
			"y": 963,
			"width": 71.25,
			"height": 17.5,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 7770,
			"version": 3,
			"versionNonce": 15114916,
			"updated": 1792682434722,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064915,
			"fileId": "85bb4e5c8f5096c5ae2de0fa288d6aeb1f58a3ec",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-shape",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-shape"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b1e"
		},
		{
			"id": "EtmMwX6E",
			"type": "image",
			"x": 805,
			"y": 745,
			"width": 29,
			"height": 30.45,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 32496,
			"version": 2,
			"versionNonce": 2140391425,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064920,
			"fileId": "f89980f4919e63b898dc028310dd858f83f2522f",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-name",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-name"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b1f"
		},
		{
			"id": "JX3Bo53J",
			"type": "rectangle",
			"x": 805,
			"y": 795,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 80335,
			"version": 3,
			"versionNonce": 445073194,
			"updated": 1792682434722,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064920,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:0:0"
				}
			},
			"index": "b1g"
		},
		{
			"text": "0.13",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "m7kgRnJe",
			"type": "text",
			"x": 807.45654296875,
			"y": 803.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 42643,
			"version": 3,
			"versionNonce": 550977348,
			"updated": 1792682434727,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064921,
			"containerId": null,
			"originalText": "0.13",
			"rawText": "0.13",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:0:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:0:0:value"
				}
			},
			"index": "b1h"
		},
		{
			"id": "wfJqT5bf",
			"type": "rectangle",
			"x": 846,
			"y": 795,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 49731,
			"version": 3,
			"versionNonce": 169333915,
			"updated": 1792682434727,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064922,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:0:1"
				}
			},
			"index": "b1i"
		},
		{
			"text": "0.14",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "F1dkoE9i",
			"type": "text",
			"x": 848.45654296875,
			"y": 803.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 28797,
			"version": 3,
			"versionNonce": 130644622,
			"updated": 1792682434733,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064922,
			"containerId": null,
			"originalText": "0.14",
			"rawText": "0.14",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:0:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:0:1:value"
				}
			},
			"index": "b1j"
		},
		{
			"id": "olSKsVbJ",
			"type": "rectangle",
			"x": 887,
			"y": 795,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 28616,
			"version": 3,
			"versionNonce": 65870059,
			"updated": 1792682434734,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064922,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:0:2"
				}
			},
			"index": "b1k"
		},
		{
			"text": "0.22",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "1t2AC3CG",
			"type": "text",
			"x": 889.45654296875,
			"y": 803.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 9395,
			"version": 3,
			"versionNonce": 866536846,
			"updated": 1792682434740,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064922,
			"containerId": null,
			"originalText": "0.22",
			"rawText": "0.22",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:0:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:0:2:value"
				}
			},
			"index": "b1l"
		},
		{
			"id": "G1ugHP9W",
			"type": "rectangle",
			"x": 928,
			"y": 795,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 23019,
			"version": 3,
			"versionNonce": 816385998,
			"updated": 1792682434741,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064922,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:0:3"
				}
			},
			"index": "b1m"
		},
		{
			"text": "0.35",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "QFYzEc2h",
			"type": "text",
			"x": 930.45654296875,
			"y": 803.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 72142,
			"version": 3,
			"versionNonce": 619496056,
			"updated": 1792682434748,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064923,
			"containerId": null,
			"originalText": "0.35",
			"rawText": "0.35",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:0:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:0:3:value"
				}
			},
			"index": "b1n"
		},
		{
			"id": "rwTJnjQR",
			"type": "rectangle",
			"x": 805,
			"y": 836,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 18211,
			"version": 3,
			"versionNonce": 507226802,
			"updated": 1792682434749,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064923,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:1:0"
				}
			},
			"index": "b1o"
		},
		{
			"text": "0.26",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "QGTUTeml",
			"type": "text",
			"x": 807.45654296875,
			"y": 844.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 3983,
			"version": 3,
			"versionNonce": 264995737,
			"updated": 1792682434755,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064923,
			"containerId": null,
			"originalText": "0.26",
			"rawText": "0.26",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:1:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:1:0:value"
				}
			},
			"index": "b1p"
		},
		{
			"id": "o1X3LqaI",
			"type": "rectangle",
			"x": 846,
			"y": 836,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 51551,
			"version": 3,
			"versionNonce": 863363995,
			"updated": 1792682434756,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064923,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:1:1"
				}
			},
			"index": "b1q"
		},
		{
			"text": "0.18",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "LIekUAak",
			"type": "text",
			"x": 848.45654296875,
			"y": 844.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 29166,
			"version": 3,
			"versionNonce": 280554991,
			"updated": 1792682434761,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064923,
			"containerId": null,
			"originalText": "0.18",
			"rawText": "0.18",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:1:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:1:1:value"
				}
			},
			"index": "b1r"
		},
		{
			"id": "OHvHiJxe",
			"type": "rectangle",
			"x": 887,
			"y": 836,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 82586,
			"version": 3,
			"versionNonce": 131879893,
			"updated": 1792682434761,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064924,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:1:2"
				}
			},
			"index": "b1s"
		},
		{
			"text": "0.17",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "iymdtwU1",
			"type": "text",
			"x": 889.45654296875,
			"y": 844.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 10470,
			"version": 3,
			"versionNonce": 904520810,
			"updated": 1792682434767,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064924,
			"containerId": null,
			"originalText": "0.17",
			"rawText": "0.17",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:1:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:1:2:value"
				}
			},
			"index": "b1t"
		},
		{
			"id": "emaNWFSX",
			"type": "rectangle",
			"x": 928,
			"y": 836,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 97017,
			"version": 3,
			"versionNonce": 362440061,
			"updated": 1792682434767,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064924,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:1:3"
				}
			},
			"index": "b1u"
		},
		{
			"text": "0.17",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "zVkRtyrL",
			"type": "text",
			"x": 930.45654296875,
			"y": 844.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 63724,
			"version": 3,
			"versionNonce": 529055146,
			"updated": 1792682434773,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064924,
			"containerId": null,
			"originalText": "0.17",
			"rawText": "0.17",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:1:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:1:3:value"
				}
			},
			"index": "b1v"
		},
		{
			"id": "g76atmF5",
			"type": "rectangle",
			"x": 805,
			"y": 877,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#b59ccf",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 53128,
			"version": 3,
			"versionNonce": 781627902,
			"updated": 1792682434774,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064924,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:2:0"
				}
			},
			"index": "b1w"
		},
		{
			"text": "0.82",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "m7UtInMO",
			"type": "text",
			"x": 807.45654296875,
			"y": 885.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 34075,
			"version": 3,
			"versionNonce": 494914793,
			"updated": 1792682434780,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064925,
			"containerId": null,
			"originalText": "0.82",
			"rawText": "0.82",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:2:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:2:0:value"
				}
			},
			"index": "b1x"
		},
		{
			"id": "0Rbj9yfE",
			"type": "rectangle",
			"x": 846,
			"y": 877,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 74212,
			"version": 3,
			"versionNonce": 657186403,
			"updated": 1792682434780,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064925,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:2:1"
				}
			},
			"index": "b1y"
		},
		{
			"text": "0.44",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "rRE7lxV2",
			"type": "text",
			"x": 848.45654296875,
			"y": 885.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 2787,
			"version": 3,
			"versionNonce": 614350601,
			"updated": 1792682434786,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064925,
			"containerId": null,
			"originalText": "0.44",
			"rawText": "0.44",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:2:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:2:1:value"
				}
			},
			"index": "b1z"
		},
		{
			"id": "Mx8tcXWb",
			"type": "rectangle",
			"x": 887,
			"y": 877,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 81797,
			"version": 3,
			"versionNonce": 739575984,
			"updated": 1792682434786,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064925,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:2:2"
				}
			},
			"index": "b20"
		},
		{
			"text": "0.20",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "9DyBkD0Z",
			"type": "text",
			"x": 889.45654296875,
			"y": 885.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 19216,
			"version": 3,
			"versionNonce": 873776793,
			"updated": 1792682434793,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064925,
			"containerId": null,
			"originalText": "0.20",
			"rawText": "0.20",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:2:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:2:2:value"
				}
			},
			"index": "b21"
		},
		{
			"id": "tknpZrx4",
			"type": "rectangle",
			"x": 928,
			"y": 877,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f1ecf6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 71,
			"version": 3,
			"versionNonce": 621831177,
			"updated": 1792682434793,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064926,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:2:3"
				}
			},
			"index": "b22"
		},
		{
			"text": "0.11",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "1L2AtIFM",
			"type": "text",
			"x": 931.08740234375,
			"y": 885.375,
			"width": 31.8251953125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 92633,
			"version": 3,
			"versionNonce": 759293617,
			"updated": 1792682434802,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064926,
			"containerId": null,
			"originalText": "0.11",
			"rawText": "0.11",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:2:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:2:3:value"
				}
			},
			"index": "b23"
		},
		{
			"id": "5cNZTodI",
			"type": "rectangle",
			"x": 805,
			"y": 918,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#b59ccf",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 11916,
			"version": 3,
			"versionNonce": 627591012,
			"updated": 1792682434802,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064926,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:3:0"
				}
			},
			"index": "b24"
		},
		{
			"text": "0.96",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "3yVNc4fF",
			"type": "text",
			"x": 807.45654296875,
			"y": 926.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 78726,
			"version": 3,
			"versionNonce": 328406240,
			"updated": 1792682434808,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064926,
			"containerId": null,
			"originalText": "0.96",
			"rawText": "0.96",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:3:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:3:0:value"
				}
			},
			"index": "b25"
		},
		{
			"id": "DJHhiuY2",
			"type": "rectangle",
			"x": 846,
			"y": 918,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#cebdde",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 21653,
			"version": 3,
			"versionNonce": 37475703,
			"updated": 1792682434808,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064926,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:3:1"
				}
			},
			"index": "b26"
		},
		{
			"text": "0.70",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "HVLnROGR",
			"type": "text",
			"x": 848.45654296875,
			"y": 926.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 98546,
			"version": 3,
			"versionNonce": 5627556,
			"updated": 1792682434814,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064926,
			"containerId": null,
			"originalText": "0.70",
			"rawText": "0.70",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:3:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:3:1:value"
				}
			},
			"index": "b27"
		},
		{
			"id": "v1ucTfzh",
			"type": "rectangle",
			"x": 887,
			"y": 918,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 20924,
			"version": 3,
			"versionNonce": 433708716,
			"updated": 1792682434814,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064927,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:3:2"
				}
			},
			"index": "b28"
		},
		{
			"text": "0.44",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "2B2zciM5",
			"type": "text",
			"x": 889.45654296875,
			"y": 926.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 47665,
			"version": 3,
			"versionNonce": 544732677,
			"updated": 1792682434820,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064927,
			"containerId": null,
			"originalText": "0.44",
			"rawText": "0.44",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:3:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:3:2:value"
				}
			},
			"index": "b29"
		},
		{
			"id": "wGyDz9O5",
			"type": "rectangle",
			"x": 928,
			"y": 918,
			"width": 38,
			"height": 38,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e5dcec",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 56681,
			"version": 3,
			"versionNonce": 886863473,
			"updated": 1792682434821,
			"isDeleted": false,
			"groupIds": [
				"br2fpfV5"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064927,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:prob-tile",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:3:3"
				}
			},
			"index": "b2A"
		},
		{
			"text": "0.31",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "JAyk4zzD",
			"type": "text",
			"x": 930.45654296875,
			"y": 926.375,
			"width": 33.0869140625,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 76656,
			"version": 3,
			"versionNonce": 644019699,
			"updated": 1792682434827,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064927,
			"containerId": null,
			"originalText": "0.31",
			"rawText": "0.31",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-tile:3:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-tile:3:3:value"
				}
			},
			"index": "b2B"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					153,
					0
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "9yRZjYWF",
			"type": "arrow",
			"x": 644,
			"y": 867,
			"width": 153,
			"height": 0,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 11804,
			"version": 3,
			"versionNonce": 952561104,
			"updated": 1792682434828,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064928,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-to-prob",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-to-prob"
				}
			},
			"index": "b2C"
		},
		{
			"text": "shift + exp",
			"fontSize": 18,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "R04M0j1c",
			"type": "text",
			"x": 657,
			"y": 823,
			"width": 82.546875,
			"height": 22.5,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 63210,
			"version": 2,
			"versionNonce": 588299745,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064928,
			"containerId": null,
			"originalText": "shift + exp",
			"rawText": "shift + exp",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "exp-label",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "exp-label"
				}
			},
			"index": "b2D"
		},
		{
			"text": "Unnormalized\nweights",
			"fontSize": 18,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "UDTQMvLf",
			"type": "text",
			"x": 985,
			"y": 938,
			"width": 111.0498046875,
			"height": 45,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 42199,
			"version": 3,
			"versionNonce": 85501582,
			"updated": 1792682434828,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064928,
			"containerId": null,
			"originalText": "Unnormalized\nweights",
			"rawText": "Unnormalized\nweights",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-caption",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-caption"
				}
			},
			"index": "b2E"
		},
		{
			"id": "s8QVkkQk",
			"type": "ellipse",
			"x": 1130,
			"y": 822,
			"width": 90,
			"height": 90,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 42448,
			"version": 2,
			"versionNonce": 1826642369,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064928,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "weighted-product",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "weighted-product"
				}
			},
			"index": "b2F"
		},
		{
			"id": "Jx6l7Vvm",
			"type": "image",
			"x": 1159.6,
			"y": 855.45,
			"width": 30.800000000000004,
			"height": 23.1,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "#ecd6b5",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 30189,
			"version": 3,
			"versionNonce": 605985461,
			"updated": 1792682434828,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064936,
			"fileId": "75b0afa6a06f448023413fa43d20ea90b59872ce",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "weighted-product-label",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "weighted-product-label"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b2G"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					148,
					0
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "xaMwYFqI",
			"type": "arrow",
			"x": 974,
			"y": 867,
			"width": 148,
			"height": 0,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 56153,
			"version": 3,
			"versionNonce": 214065399,
			"updated": 1792682434828,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064936,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-to-product",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-to-product"
				}
			},
			"index": "b2H"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					74
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "0dBoFcUJ",
			"type": "arrow",
			"x": 1180,
			"y": 740,
			"width": 0,
			"height": 74,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 13354,
			"version": 2,
			"versionNonce": 152382703,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064936,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "value-to-product",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "value-to-product"
				}
			},
			"index": "b2I"
		},
		{
			"text": "CARRY TO THE NEXT TILE",
			"fontSize": 18,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "0Dr4NlTu",
			"type": "text",
			"x": 170,
			"y": 1038,
			"width": 229.376953125,
			"height": 22.5,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 44920,
			"version": 2,
			"versionNonce": 533962113,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064936,
			"containerId": null,
			"originalText": "CARRY TO THE NEXT TILE",
			"rawText": "CARRY TO THE NEXT TILE",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "carry-heading",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "carry-heading"
				},
				"bold": true
			},
			"index": "b2J"
		},
		{
			"id": "1Sm4PKEl",
			"type": "rectangle",
			"x": 520,
			"y": 1020,
			"width": 43,
			"height": 21,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 9860,
			"version": 2,
			"versionNonce": 786413327,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"QMJuKJPS"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064937,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-m",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-m",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-m:0:0"
				}
			},
			"index": "b2K"
		},
		{
			"text": "0.7",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "bw3zt0pJ",
			"type": "text",
			"x": 530.37890625,
			"y": 1020.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 75092,
			"version": 2,
			"versionNonce": 2036745569,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064937,
			"containerId": null,
			"originalText": "0.7",
			"rawText": "0.7",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-m:0:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-m:0:0:value"
				}
			},
			"index": "b2L"
		},
		{
			"id": "BPdjnoR4",
			"type": "rectangle",
			"x": 520,
			"y": 1044,
			"width": 43,
			"height": 21,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 42563,
			"version": 2,
			"versionNonce": 1796472111,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"QMJuKJPS"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064937,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-m",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-m",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-m:1:0"
				}
			},
			"index": "b2M"
		},
		{
			"text": "0.7",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "QS4oEzMW",
			"type": "text",
			"x": 530.37890625,
			"y": 1044.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 32887,
			"version": 2,
			"versionNonce": 2115563841,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064937,
			"containerId": null,
			"originalText": "0.7",
			"rawText": "0.7",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-m:1:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-m:1:0:value"
				}
			},
			"index": "b2N"
		},
		{
			"id": "hf2E3oqO",
			"type": "rectangle",
			"x": 520,
			"y": 1068,
			"width": 43,
			"height": 21,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 64327,
			"version": 2,
			"versionNonce": 1092255567,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"QMJuKJPS"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064937,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-m",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-m",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-m:2:0"
				}
			},
			"index": "b2O"
		},
		{
			"text": "0.7",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "VwJq1mAe",
			"type": "text",
			"x": 530.37890625,
			"y": 1068.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 753,
			"version": 2,
			"versionNonce": 1397432609,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064938,
			"containerId": null,
			"originalText": "0.7",
			"rawText": "0.7",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-m:2:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-m:2:0:value"
				}
			},
			"index": "b2P"
		},
		{
			"id": "iMmc4KU2",
			"type": "rectangle",
			"x": 520,
			"y": 1092,
			"width": 43,
			"height": 21,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 7582,
			"version": 2,
			"versionNonce": 860601711,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"QMJuKJPS"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064938,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-m",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-m",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-m:3:0"
				}
			},
			"index": "b2Q"
		},
		{
			"text": "0.4",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "0TSX2rvB",
			"type": "text",
			"x": 530.37890625,
			"y": 1092.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 6645,
			"version": 2,
			"versionNonce": 1181504769,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064938,
			"containerId": null,
			"originalText": "0.4",
			"rawText": "0.4",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-m:3:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-m:3:0:value"
				}
			},
			"index": "b2R"
		},
		{
			"id": "1FAaVasc",
			"type": "rectangle",
			"x": 680,
			"y": 1020,
			"width": 43,
			"height": 21,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 51738,
			"version": 2,
			"versionNonce": 1693464463,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GCEWusAq"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064938,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-ell",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-ell",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-ell:0:0"
				}
			},
			"index": "b2S"
		},
		{
			"text": "5.6",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "bgvWNCkb",
			"type": "text",
			"x": 690.37890625,
			"y": 1020.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 18459,
			"version": 2,
			"versionNonce": 1258032353,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064939,
			"containerId": null,
			"originalText": "5.6",
			"rawText": "5.6",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-ell:0:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-ell:0:0:value"
				}
			},
			"index": "b2T"
		},
		{
			"id": "rO6uCmHl",
			"type": "rectangle",
			"x": 680,
			"y": 1044,
			"width": 43,
			"height": 21,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 76041,
			"version": 2,
			"versionNonce": 2084597167,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GCEWusAq"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064939,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-ell",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-ell",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-ell:1:0"
				}
			},
			"index": "b2U"
		},
		{
			"text": "5.6",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "0L9Rmskg",
			"type": "text",
			"x": 690.37890625,
			"y": 1044.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 5534,
			"version": 2,
			"versionNonce": 948553921,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064939,
			"containerId": null,
			"originalText": "5.6",
			"rawText": "5.6",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-ell:1:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-ell:1:0:value"
				}
			},
			"index": "b2V"
		},
		{
			"id": "oWifeeB5",
			"type": "rectangle",
			"x": 680,
			"y": 1068,
			"width": 43,
			"height": 21,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 86778,
			"version": 2,
			"versionNonce": 1147461583,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GCEWusAq"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064939,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-ell",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-ell",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-ell:2:0"
				}
			},
			"index": "b2W"
		},
		{
			"text": "6.3",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "DF0BUlHY",
			"type": "text",
			"x": 690.37890625,
			"y": 1068.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 12356,
			"version": 2,
			"versionNonce": 1219823777,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064940,
			"containerId": null,
			"originalText": "6.3",
			"rawText": "6.3",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-ell:2:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-ell:2:0:value"
				}
			},
			"index": "b2X"
		},
		{
			"id": "bd8DgTsa",
			"type": "rectangle",
			"x": 680,
			"y": 1092,
			"width": 43,
			"height": 21,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#d8e9df",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 82929,
			"version": 2,
			"versionNonce": 259395055,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GCEWusAq"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064940,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-ell",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-ell",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-ell:3:0"
				}
			},
			"index": "b2Y"
		},
		{
			"text": "8.0",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "YoZZu25L",
			"type": "text",
			"x": 690.37890625,
			"y": 1092.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 50893,
			"version": 2,
			"versionNonce": 1429032065,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064940,
			"containerId": null,
			"originalText": "8.0",
			"rawText": "8.0",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-ell:3:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-ell:3:0:value"
				}
			},
			"index": "b2Z"
		},
		{
			"id": "mPGosdOE",
			"type": "image",
			"x": 470,
			"y": 1041,
			"width": 26,
			"height": 13,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 23828,
			"version": 2,
			"versionNonce": 1484552207,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064944,
			"fileId": "5170a6cfb74365845514b49ae30ec7a7af5c9e40",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-m-name",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-m-name"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b2a"
		},
		{
			"id": "4sNk79NA",
			"type": "image",
			"x": 634,
			"y": 1041,
			"width": 24.7,
			"height": 18.2,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 17066,
			"version": 2,
			"versionNonce": 1437733985,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064948,
			"fileId": "ded6e9a15e263e844608ac670746872fc8eea114",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-ell-name",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-ell-name"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b2b"
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
					-5,
					36
				],
				[
					-5,
					48
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "YeCCSMZ7",
			"type": "arrow",
			"x": 548,
			"y": 964,
			"width": 5,
			"height": 48,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2.3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 89142,
			"version": 3,
			"versionNonce": 773406434,
			"updated": 1792682434828,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064948,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "score-to-max",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "score-to-max"
				}
			},
			"index": "b2c"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					33
				],
				[
					-176,
					33
				],
				[
					-176,
					48
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "tWIaIZpu",
			"type": "arrow",
			"x": 879,
			"y": 964,
			"width": 176,
			"height": 48,
			"angle": 0,
			"strokeColor": "#4b8b7a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2.3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 85250,
			"version": 3,
			"versionNonce": 316528753,
			"updated": 1792682434829,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064948,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "prob-to-sum",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "prob-to-sum"
				}
			},
			"index": "b2d"
		},
		{
			"id": "kDf1tp7P",
			"type": "rectangle",
			"x": 1110,
			"y": 977,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#adc7d8",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 58895,
			"version": 2,
			"versionNonce": 691732559,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064948,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:0:0"
				}
			},
			"index": "b2e"
		},
		{
			"text": "2.3",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "3BfSNxiz",
			"type": "text",
			"x": 1115.37890625,
			"y": 981.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 38983,
			"version": 2,
			"versionNonce": 1546596385,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064949,
			"containerId": null,
			"originalText": "2.3",
			"rawText": "2.3",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:0:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:0:0:value"
				}
			},
			"index": "b2f"
		},
		{
			"id": "VkuKbSov",
			"type": "rectangle",
			"x": 1146,
			"y": 977,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e0eaf1",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 74761,
			"version": 2,
			"versionNonce": 632561263,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064949,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:0:1"
				}
			},
			"index": "b2g"
		},
		{
			"text": "-0.3",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "RaLpuGC9",
			"type": "text",
			"x": 1148.71484375,
			"y": 981.5,
			"width": 27.5703125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 66848,
			"version": 2,
			"versionNonce": 1442219009,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064949,
			"containerId": null,
			"originalText": "-0.3",
			"rawText": "-0.3",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:0:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:0:1:value"
				}
			},
			"index": "b2h"
		},
		{
			"id": "xY82l203",
			"type": "rectangle",
			"x": 1182,
			"y": 977,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f0f5f8",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 478,
			"version": 2,
			"versionNonce": 228882575,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064950,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:0:2"
				}
			},
			"index": "b2i"
		},
		{
			"text": "-1.4",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "WxyP0KmU",
			"type": "text",
			"x": 1184.71484375,
			"y": 981.5,
			"width": 27.5703125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 57875,
			"version": 2,
			"versionNonce": 1734892513,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064950,
			"containerId": null,
			"originalText": "-1.4",
			"rawText": "-1.4",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:0:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:0:2:value"
				}
			},
			"index": "b2j"
		},
		{
			"id": "aCMKTQly",
			"type": "rectangle",
			"x": 1218,
			"y": 977,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e0eaf1",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 30589,
			"version": 2,
			"versionNonce": 1724157615,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064950,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:0:3"
				}
			},
			"index": "b2k"
		},
		{
			"text": "-0.7",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "g8eTQevi",
			"type": "text",
			"x": 1220.71484375,
			"y": 981.5,
			"width": 27.5703125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 55969,
			"version": 2,
			"versionNonce": 1083455425,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064950,
			"containerId": null,
			"originalText": "-0.7",
			"rawText": "-0.7",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:0:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:0:3:value"
				}
			},
			"index": "b2l"
		},
		{
			"id": "PZEsCn4g",
			"type": "rectangle",
			"x": 1110,
			"y": 1009,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#adc7d8",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 65628,
			"version": 2,
			"versionNonce": 1807540431,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064950,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:1:0"
				}
			},
			"index": "b2m"
		},
		{
			"text": "1.9",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "aLJMJhSE",
			"type": "text",
			"x": 1115.37890625,
			"y": 1013.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 82543,
			"version": 2,
			"versionNonce": 1671010209,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064951,
			"containerId": null,
			"originalText": "1.9",
			"rawText": "1.9",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:1:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:1:0:value"
				}
			},
			"index": "b2n"
		},
		{
			"id": "cmxOy3fC",
			"type": "rectangle",
			"x": 1146,
			"y": 1009,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f0f5f8",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 32632,
			"version": 2,
			"versionNonce": 1847979759,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064951,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:1:1"
				}
			},
			"index": "b2o"
		},
		{
			"text": "-1.3",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "mjdChs7s",
			"type": "text",
			"x": 1148.71484375,
			"y": 1013.5,
			"width": 27.5703125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 14295,
			"version": 2,
			"versionNonce": 1655176065,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064951,
			"containerId": null,
			"originalText": "-1.3",
			"rawText": "-1.3",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:1:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:1:1:value"
				}
			},
			"index": "b2p"
		},
		{
			"id": "mFeDQxCN",
			"type": "rectangle",
			"x": 1182,
			"y": 1009,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f0f5f8",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 47039,
			"version": 2,
			"versionNonce": 2022193423,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064951,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:1:2"
				}
			},
			"index": "b2q"
		},
		{
			"text": "-0.9",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "y2M8LBED",
			"type": "text",
			"x": 1184.71484375,
			"y": 1013.5,
			"width": 27.5703125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 56292,
			"version": 2,
			"versionNonce": 1576985441,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064951,
			"containerId": null,
			"originalText": "-0.9",
			"rawText": "-0.9",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:1:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:1:2:value"
				}
			},
			"index": "b2r"
		},
		{
			"id": "eEGiwhsz",
			"type": "rectangle",
			"x": 1218,
			"y": 1009,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#c7dbe6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 6382,
			"version": 2,
			"versionNonce": 811351855,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064952,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:1:3"
				}
			},
			"index": "b2s"
		},
		{
			"text": "0.4",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "zNma0jCv",
			"type": "text",
			"x": 1223.37890625,
			"y": 1013.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 79440,
			"version": 2,
			"versionNonce": 1106104129,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064952,
			"containerId": null,
			"originalText": "0.4",
			"rawText": "0.4",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:1:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:1:3:value"
				}
			},
			"index": "b2t"
		},
		{
			"id": "xmCdBTEO",
			"type": "rectangle",
			"x": 1110,
			"y": 1041,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#c7dbe6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 63790,
			"version": 2,
			"versionNonce": 2013954383,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064952,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:2:0"
				}
			},
			"index": "b2u"
		},
		{
			"text": "1.0",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "30ZZ4DJ9",
			"type": "text",
			"x": 1115.37890625,
			"y": 1045.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 14359,
			"version": 2,
			"versionNonce": 1154760481,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064952,
			"containerId": null,
			"originalText": "1.0",
			"rawText": "1.0",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:2:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:2:0:value"
				}
			},
			"index": "b2v"
		},
		{
			"id": "qHEgGw9X",
			"type": "rectangle",
			"x": 1146,
			"y": 1041,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f0f5f8",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 3728,
			"version": 2,
			"versionNonce": 1357610863,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064952,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:2:1"
				}
			},
			"index": "b2w"
		},
		{
			"text": "-1.5",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "uPa1TzXp",
			"type": "text",
			"x": 1148.71484375,
			"y": 1045.5,
			"width": 27.5703125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 35398,
			"version": 2,
			"versionNonce": 622965505,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064953,
			"containerId": null,
			"originalText": "-1.5",
			"rawText": "-1.5",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:2:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:2:1:value"
				}
			},
			"index": "b2x"
		},
		{
			"id": "GFPlIwrH",
			"type": "rectangle",
			"x": 1182,
			"y": 1041,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#c7dbe6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 23556,
			"version": 2,
			"versionNonce": 2101852559,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064953,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:2:2"
				}
			},
			"index": "b2y"
		},
		{
			"text": "1.1",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "1TqVb0dN",
			"type": "text",
			"x": 1187.37890625,
			"y": 1045.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 46668,
			"version": 2,
			"versionNonce": 659925729,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064953,
			"containerId": null,
			"originalText": "1.1",
			"rawText": "1.1",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:2:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:2:2:value"
				}
			},
			"index": "b2z"
		},
		{
			"id": "silIGQG2",
			"type": "rectangle",
			"x": 1218,
			"y": 1041,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#c7dbe6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 81051,
			"version": 2,
			"versionNonce": 1649913775,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064953,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:2:3"
				}
			},
			"index": "b30"
		},
		{
			"text": "0.7",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "yfvxqgKy",
			"type": "text",
			"x": 1223.37890625,
			"y": 1045.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 91900,
			"version": 2,
			"versionNonce": 1409263297,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064953,
			"containerId": null,
			"originalText": "0.7",
			"rawText": "0.7",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:2:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:2:3:value"
				}
			},
			"index": "b31"
		},
		{
			"id": "enhEYmJZ",
			"type": "rectangle",
			"x": 1110,
			"y": 1073,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#c7dbe6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 21962,
			"version": 2,
			"versionNonce": 709091791,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064954,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:3:0"
				}
			},
			"index": "b32"
		},
		{
			"text": "1.0",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "u6KpKWVp",
			"type": "text",
			"x": 1115.37890625,
			"y": 1077.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 80694,
			"version": 2,
			"versionNonce": 1975461537,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064954,
			"containerId": null,
			"originalText": "1.0",
			"rawText": "1.0",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:3:0:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:3:0:value"
				}
			},
			"index": "b33"
		},
		{
			"id": "NZOIPTwd",
			"type": "rectangle",
			"x": 1146,
			"y": 1073,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f0f5f8",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 46382,
			"version": 2,
			"versionNonce": 639946735,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064954,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:3:1"
				}
			},
			"index": "b34"
		},
		{
			"text": "-1.1",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "jQW0W16P",
			"type": "text",
			"x": 1148.71484375,
			"y": 1077.5,
			"width": 27.5703125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 17259,
			"version": 2,
			"versionNonce": 1464052353,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064954,
			"containerId": null,
			"originalText": "-1.1",
			"rawText": "-1.1",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:3:1:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:3:1:value"
				}
			},
			"index": "b35"
		},
		{
			"id": "rM18EYDT",
			"type": "rectangle",
			"x": 1182,
			"y": 1073,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#c7dbe6",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 49928,
			"version": 2,
			"versionNonce": 1879243279,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064955,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:3:2"
				}
			},
			"index": "b36"
		},
		{
			"text": "1.5",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "RR6c1CXW",
			"type": "text",
			"x": 1187.37890625,
			"y": 1077.5,
			"width": 22.2421875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 42384,
			"version": 2,
			"versionNonce": 1095545441,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064955,
			"containerId": null,
			"originalText": "1.5",
			"rawText": "1.5",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:3:2:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:3:2:value"
				}
			},
			"index": "b37"
		},
		{
			"id": "7TQwffl1",
			"type": "rectangle",
			"x": 1218,
			"y": 1073,
			"width": 33,
			"height": 29,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#e0eaf1",
			"fillStyle": "solid",
			"strokeWidth": 0.8,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 77632,
			"version": 2,
			"versionNonce": 1289150511,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [
				"GA1CtiG3"
			],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064955,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U",
					"role": "body"
				},
				"agentPrimitive": {
					"instanceId": "flashattention-flagship:state-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:3:3"
				}
			},
			"index": "b38"
		},
		{
			"text": "-0.1",
			"fontSize": 16,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "zxH3RQsW",
			"type": "text",
			"x": 1220.71484375,
			"y": 1077.5,
			"width": 27.5703125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 14922,
			"version": 2,
			"versionNonce": 950648385,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064956,
			"containerId": null,
			"originalText": "-0.1",
			"rawText": "-0.1",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U:3:3:value",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U:3:3:value"
				}
			},
			"index": "b39"
		},
		{
			"id": "aMMf9Hez",
			"type": "image",
			"x": 1030,
			"y": 1032,
			"width": 23.2,
			"height": 20.3,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 58669,
			"version": 2,
			"versionNonce": 1317601871,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064960,
			"fileId": "aa9376c0bb9c72e523af4ed50fbed13c34425ea0",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-U-name",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-U-name"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b3A"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					51
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "r9d1dryM",
			"type": "arrow",
			"x": 1175,
			"y": 918,
			"width": 0,
			"height": 51,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 13815,
			"version": 2,
			"versionNonce": 2084195873,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064960,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "product-to-U",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "product-to-U"
				}
			},
			"index": "b3B"
		},
		{
			"text": "rescale + add",
			"fontSize": 18,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "fGSul7lG",
			"type": "text",
			"x": 1230,
			"y": 895,
			"width": 108.5712890625,
			"height": 22.5,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 46204,
			"version": 2,
			"versionNonce": 905044079,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064961,
			"containerId": null,
			"originalText": "rescale + add",
			"rawText": "rescale + add",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "accumulate-label",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "accumulate-label"
				}
			},
			"index": "b3C"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					128,
					0
				],
				[
					128,
					-58
				],
				[
					-77,
					-58
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "ukgu5uIl",
			"type": "arrow",
			"x": 1259,
			"y": 1002,
			"width": 205,
			"height": 58,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2.3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 39914,
			"version": 2,
			"versionNonce": 1122886145,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064961,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "U-recurrence",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "U-recurrence"
				}
			},
			"index": "b3D"
		},
		{
			"text": "old numerator",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "h0zGxd91",
			"type": "text",
			"x": 1255,
			"y": 1015,
			"width": 104.888671875,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#bc8845",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 63810,
			"version": 2,
			"versionNonce": 349829775,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064961,
			"containerId": null,
			"originalText": "old numerator",
			"rawText": "old numerator",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "recurrence-note",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "recurrence-note"
				}
			},
			"index": "b3E"
		},
		{
			"id": "Qwmq7wb0",
			"type": "rectangle",
			"x": 1500,
			"y": 1020,
			"width": 240,
			"height": 65,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "#e6dff0",
			"fillStyle": "solid",
			"strokeWidth": 1.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": {
				"type": 3,
				"value": 8,
				"roundType": "arc"
			},
			"seed": 84079,
			"version": 2,
			"versionNonce": 969144801,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064962,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "normalize",
					"role": "container"
				},
				"isContainer": true,
				"dsl": {
					"document": "flashattention-flagship",
					"key": "normalize"
				}
			},
			"index": "b3F"
		},
		{
			"id": "ll5uEk8U",
			"type": "image",
			"x": 1512,
			"y": 1039,
			"width": 157.5,
			"height": 22.5,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "#e6dff0",
			"fillStyle": "solid",
			"strokeWidth": 1.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": {
				"type": 3,
				"value": 8,
				"roundType": "arc"
			},
			"seed": 10490,
			"version": 2,
			"versionNonce": 804901039,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064973,
			"fileId": "309d196bffb8b26eb07c6057ef638ceabd71b876",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "normalize-formula",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "normalize-formula"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b3G"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					193,
					0
				],
				[
					193,
					-28
				],
				[
					233,
					-28
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "9ULobv7D",
			"type": "arrow",
			"x": 1259,
			"y": 1080,
			"width": 233,
			"height": 28,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 1108,
			"version": 2,
			"versionNonce": 1103893953,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064973,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "U-to-finalize",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "U-to-finalize"
				}
			},
			"index": "b3H"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					155,
					0
				],
				[
					155,
					-692
				],
				[
					113,
					-692
				]
			],
			"elbowed": false,
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"id": "xLGp0iGB",
			"type": "arrow",
			"x": 1748,
			"y": 1052,
			"width": 155,
			"height": 692,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 3.2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 89075,
			"version": 2,
			"versionNonce": 553247439,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064973,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "output-write",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "output-write"
				}
			},
			"index": "b3I"
		},
		{
			"text": "After the K/V sweep:\nnormalize once, then write.",
			"fontSize": 21,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "REzkCoQn",
			"type": "text",
			"x": 1500,
			"y": 1100,
			"width": 250.9541015625,
			"height": 52.5,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 30023,
			"version": 3,
			"versionNonce": 462118412,
			"updated": 1792682243829,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064974,
			"containerId": null,
			"originalText": "After the K/V sweep:\nnormalize once, then write.",
			"rawText": "After the K/V sweep:\nnormalize once, then write.",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "normalize-caption",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "normalize-caption"
				}
			},
			"index": "b3J"
		},
		{
			"text": "03 / THE BUFFER YOU AVOID",
			"fontSize": 23,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "6KgVxHU2",
			"type": "text",
			"x": 1515,
			"y": 548,
			"width": 321.62939453125,
			"height": 28.75,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 15058,
			"version": 2,
			"versionNonce": 947040495,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064974,
			"containerId": null,
			"originalText": "03 / THE BUFFER YOU AVOID",
			"rawText": "03 / THE BUFFER YOU AVOID",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-heading",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-heading"
				},
				"bold": true
			},
			"index": "b3K"
		},
		{
			"id": "TOlc87I0",
			"type": "rectangle",
			"x": 1530,
			"y": 650,
			"width": 256,
			"height": 256,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "#f6f7f8",
			"fillStyle": "solid",
			"strokeWidth": 1.4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 46813,
			"version": 2,
			"versionNonce": 1107319169,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064974,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "global-index",
					"role": "container"
				},
				"isContainer": true,
				"dsl": {
					"document": "flashattention-flagship",
					"key": "global-index"
				}
			},
			"index": "b3L"
		},
		{
			"id": "5ingO94m",
			"type": "rectangle",
			"x": 1658,
			"y": 714,
			"width": 64,
			"height": 64,
			"angle": 0,
			"strokeColor": "#8570a5",
			"backgroundColor": "#c6b6da",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 18154,
			"version": 2,
			"versionNonce": 535608079,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064974,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "global-active-tile",
					"role": "container"
				},
				"isContainer": true,
				"dsl": {
					"document": "flashattention-flagship",
					"key": "global-active-tile"
				}
			},
			"index": "b3M"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "PV1sdVOj",
			"type": "line",
			"x": 1530,
			"y": 666,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 71202,
			"version": 2,
			"versionNonce": 781943137,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-1"
				}
			},
			"index": "b3N"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "PaTGyr0j",
			"type": "line",
			"x": 1546,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 10005,
			"version": 2,
			"versionNonce": 1004568879,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-1",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-1"
				}
			},
			"index": "b3O"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "AYFLaMTY",
			"type": "line",
			"x": 1530,
			"y": 682,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 43809,
			"version": 2,
			"versionNonce": 1363586369,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-2"
				}
			},
			"index": "b3P"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "7wmUz2Vm",
			"type": "line",
			"x": 1562,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 49187,
			"version": 2,
			"versionNonce": 1303806799,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-2"
				}
			},
			"index": "b3Q"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "qfEes6Wj",
			"type": "line",
			"x": 1530,
			"y": 698,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 14423,
			"version": 2,
			"versionNonce": 1902206241,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-3"
				}
			},
			"index": "b3R"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "Qy7Fal2O",
			"type": "line",
			"x": 1578,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 71586,
			"version": 2,
			"versionNonce": 1439121775,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-3",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-3"
				}
			},
			"index": "b3S"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "W5CGu5sR",
			"type": "line",
			"x": 1530,
			"y": 714,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 71107,
			"version": 2,
			"versionNonce": 1046155521,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-4",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-4"
				}
			},
			"index": "b3T"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "DrLn5fW0",
			"type": "line",
			"x": 1594,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 46498,
			"version": 2,
			"versionNonce": 895171471,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-4",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-4"
				}
			},
			"index": "b3U"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "9BbCRZZ6",
			"type": "line",
			"x": 1530,
			"y": 730,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 31096,
			"version": 2,
			"versionNonce": 1303595233,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-5",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-5"
				}
			},
			"index": "b3V"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "RjyV0JaB",
			"type": "line",
			"x": 1610,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 62572,
			"version": 2,
			"versionNonce": 279638447,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-5",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-5"
				}
			},
			"index": "b3W"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "EYbsRAzP",
			"type": "line",
			"x": 1530,
			"y": 746,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 94691,
			"version": 2,
			"versionNonce": 1492747457,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-6",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-6"
				}
			},
			"index": "b3X"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "DvSh6wvF",
			"type": "line",
			"x": 1626,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 31956,
			"version": 2,
			"versionNonce": 1893655503,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-6",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-6"
				}
			},
			"index": "b3Y"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "rt0PgVVf",
			"type": "line",
			"x": 1530,
			"y": 762,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 65999,
			"version": 2,
			"versionNonce": 1003308193,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064975,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-7",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-7"
				}
			},
			"index": "b3Z"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "t1Qex6fN",
			"type": "line",
			"x": 1642,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 1415,
			"version": 2,
			"versionNonce": 638554607,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-7",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-7"
				}
			},
			"index": "b3a"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "S1LCdzsw",
			"type": "line",
			"x": 1530,
			"y": 778,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 2957,
			"version": 2,
			"versionNonce": 836634753,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-8",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-8"
				}
			},
			"index": "b3b"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "HmBKTX3y",
			"type": "line",
			"x": 1658,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 42137,
			"version": 2,
			"versionNonce": 1766161423,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-8",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-8"
				}
			},
			"index": "b3c"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "dSpYyGCD",
			"type": "line",
			"x": 1530,
			"y": 794,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 97091,
			"version": 2,
			"versionNonce": 1424707681,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-9",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-9"
				}
			},
			"index": "b3d"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "1wjwe22t",
			"type": "line",
			"x": 1674,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 95222,
			"version": 2,
			"versionNonce": 1048125999,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-9",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-9"
				}
			},
			"index": "b3e"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "OeuKnQwM",
			"type": "line",
			"x": 1530,
			"y": 810,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 85357,
			"version": 2,
			"versionNonce": 1522834497,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-10",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-10"
				}
			},
			"index": "b3f"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "7EOtXBne",
			"type": "line",
			"x": 1690,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 64386,
			"version": 2,
			"versionNonce": 378733647,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-10",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-10"
				}
			},
			"index": "b3g"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "8HuGv2ez",
			"type": "line",
			"x": 1530,
			"y": 826,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 46329,
			"version": 2,
			"versionNonce": 323578913,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-11",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-11"
				}
			},
			"index": "b3h"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "QqrQuBHO",
			"type": "line",
			"x": 1706,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 66443,
			"version": 2,
			"versionNonce": 829137519,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-11",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-11"
				}
			},
			"index": "b3i"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "BUlhZ3QF",
			"type": "line",
			"x": 1530,
			"y": 842,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 74573,
			"version": 2,
			"versionNonce": 644431873,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-12",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-12"
				}
			},
			"index": "b3j"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "y5Fjpogu",
			"type": "line",
			"x": 1722,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 89074,
			"version": 2,
			"versionNonce": 1070300303,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-12",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-12"
				}
			},
			"index": "b3k"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "meltucBp",
			"type": "line",
			"x": 1530,
			"y": 858,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 23924,
			"version": 2,
			"versionNonce": 304322529,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-13",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-13"
				}
			},
			"index": "b3l"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "YQtmwbJS",
			"type": "line",
			"x": 1738,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 55066,
			"version": 2,
			"versionNonce": 1164645039,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-13",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-13"
				}
			},
			"index": "b3m"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "YkdZudKt",
			"type": "line",
			"x": 1530,
			"y": 874,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 73053,
			"version": 2,
			"versionNonce": 1753740225,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064976,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-14",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-14"
				}
			},
			"index": "b3n"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "O5156DuV",
			"type": "line",
			"x": 1754,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 11216,
			"version": 2,
			"versionNonce": 988996815,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064977,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-14",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-14"
				}
			},
			"index": "b3o"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					256,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "t7Deqzey",
			"type": "line",
			"x": 1530,
			"y": 890,
			"width": 256,
			"height": 0,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 41777,
			"version": 2,
			"versionNonce": 1303761825,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064977,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-row-15",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-row-15"
				}
			},
			"index": "b3p"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					0,
					256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "Swn1Y4s3",
			"type": "line",
			"x": 1770,
			"y": 650,
			"width": 0,
			"height": 256,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 49848,
			"version": 2,
			"versionNonce": 1878749935,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064977,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "index-col-15",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "index-col-15"
				}
			},
			"index": "b3q"
		},
		{
			"id": "sQ6JquxQ",
			"type": "image",
			"x": 1595,
			"y": 600,
			"width": 68.6,
			"height": 15.399999999999999,
			"angle": 0,
			"strokeColor": "#cbd3d8",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.7,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 24620,
			"version": 2,
			"versionNonce": 903657345,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064980,
			"fileId": "ab3bce10ed80430cd6124e27ba01a058a1bd9b5b",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "global-index-shape",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "global-index-shape"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b3r"
		},
		{
			"text": "NO FULL S / P BUFFER IN HBM",
			"fontSize": 20,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "xJFQBWgA",
			"type": "text",
			"x": 1515,
			"y": 926,
			"width": 294.482421875,
			"height": 25,
			"angle": 0,
			"strokeColor": "#a65d66",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 48696,
			"version": 2,
			"versionNonce": 755842319,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064981,
			"containerId": null,
			"originalText": "NO FULL S / P BUFFER IN HBM",
			"rawText": "NO FULL S / P BUFFER IN HBM",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "no-global-buffer",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "no-global-buffer"
				},
				"bold": true
			},
			"index": "b3s"
		},
		{
			"text": "Scores are computed, not skipped.\nNo full score/weight matrix is stored.",
			"fontSize": 20,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "lzDpZAxg",
			"type": "text",
			"x": 1515,
			"y": 965,
			"width": 321.220703125,
			"height": 50,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 45878,
			"version": 2,
			"versionNonce": 1664884577,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064982,
			"containerId": null,
			"originalText": "Scores are computed, not skipped.\nNo full score/weight matrix is stored.",
			"rawText": "Scores are computed, not skipped.\nNo full score/weight matrix is stored.",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "global-explanation",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "global-explanation"
				}
			},
			"index": "b3t"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					1830,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "D7xP9Q9S",
			"type": "line",
			"x": 65,
			"y": 1160,
			"width": 1830,
			"height": 0,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 36661,
			"version": 2,
			"versionNonce": 362857263,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064982,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "math-rule",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "math-rule"
				}
			},
			"index": "b3u"
		},
		{
			"text": "THE ONLINE UPDATE",
			"fontSize": 23,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "lAVQAv8S",
			"type": "text",
			"x": 75,
			"y": 1185,
			"width": 235.9970703125,
			"height": 28.75,
			"angle": 0,
			"strokeColor": "#213d4a",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 25245,
			"version": 2,
			"versionNonce": 606309185,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064982,
			"containerId": null,
			"originalText": "THE ONLINE UPDATE",
			"rawText": "THE ONLINE UPDATE",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "math-heading",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "math-heading"
				},
				"bold": true
			},
			"index": "b3v"
		},
		{
			"text": "One query row q; repeat for each K/V tile.",
			"fontSize": 21,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "4za7nAjQ",
			"type": "text",
			"x": 420,
			"y": 1189,
			"width": 386.3671875,
			"height": 26.25,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 275,
			"version": 3,
			"versionNonce": 2968127,
			"updated": 1792682243830,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682064983,
			"containerId": null,
			"originalText": "One query row q; repeat for each K/V tile.",
			"rawText": "One query row q; repeat for each K/V tile.",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "math-subheading",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "math-subheading"
				}
			},
			"index": "b3w"
		},
		{
			"id": "aRGSa1fi",
			"type": "image",
			"x": 775,
			"y": 1245,
			"width": 298.65,
			"height": 130.35,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 86933,
			"version": 2,
			"versionNonce": 1239352175,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682065011,
			"fileId": "247cf78cd9f51a6778764fe2a39ab93794e1cea0",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "online-accumulate",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "online-accumulate"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b3y"
		},
		{
			"text": "m / running maximum\nell / rescaled exponential sum\nu / unnormalized numerator",
			"fontSize": 21,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "rhMmJFql",
			"type": "text",
			"x": 1490,
			"y": 1230,
			"width": 276.650390625,
			"height": 78.75,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 56782,
			"version": 2,
			"versionNonce": 169373441,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682065012,
			"containerId": null,
			"originalText": "m / running maximum\nell / rescaled exponential sum\nu / unnormalized numerator",
			"rawText": "m / running maximum\nell / rescaled exponential sum\nu / unnormalized numerator",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "state-legend",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "state-legend"
				}
			},
			"index": "b3z"
		},
		{
			"id": "zl73tdwZ",
			"type": "image",
			"x": 1490,
			"y": 1350,
			"width": 235,
			"height": 18.75,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 80040,
			"version": 2,
			"versionNonce": 355122575,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682065019,
			"fileId": "997b13806a0c46597b8af046c4050916abfbc04c",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "init-state",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "init-state"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b40"
		},
		{
			"points": [
				[
					0,
					0
				],
				[
					1830,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"id": "APwA4mxh",
			"type": "line",
			"x": 65,
			"y": 1440,
			"width": 1830,
			"height": 0,
			"angle": 0,
			"strokeColor": "#a1b2b9",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 74671,
			"version": 2,
			"versionNonce": 907339489,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682065019,
			"polygon": false,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "footer-rule",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "footer-rule"
				}
			},
			"index": "b41"
		},
		{
			"text": "Forward pass / FA2-style query-block schedule / one head / unmasked / no dropout. Memory placement is schematic.",
			"fontSize": 18,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "FoU5IC9Z",
			"type": "text",
			"x": 75,
			"y": 1457,
			"width": 935.4462890625,
			"height": 22.5,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 25965,
			"version": 2,
			"versionNonce": 255472559,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682065020,
			"containerId": null,
			"originalText": "Forward pass / FA2-style query-block schedule / one head / unmasked / no dropout. Memory placement is schematic.",
			"rawText": "Forward pass / FA2-style query-block schedule / one head / unmasked / no dropout. Memory placement is schematic.",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "scope",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "scope"
				}
			},
			"index": "b42"
		},
		{
			"text": "Source: Dao, FlashAttention-2, Section 3.1 (2023). Synthetic 16-token, d=4 snapshot; 4x4 tiles are not GPU launch sizes.",
			"fontSize": 17,
			"fontFamily": "Liberation Sans",
			"textAlign": "left",
			"verticalAlign": "top",
			"id": "VxZUKUhQ",
			"type": "text",
			"x": 75,
			"y": 1485,
			"width": 912.3720703125,
			"height": 21.25,
			"angle": 0,
			"strokeColor": "#637782",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"roundness": null,
			"seed": 68092,
			"version": 2,
			"versionNonce": 1064788673,
			"updated": 1792682065029,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682065021,
			"containerId": null,
			"originalText": "Source: Dao, FlashAttention-2, Section 3.1 (2023). Synthetic 16-token, d=4 snapshot; 4x4 tiles are not GPU launch sizes.",
			"rawText": "Source: Dao, FlashAttention-2, Section 3.1 (2023). Synthetic 16-token, d=4 snapshot; 4x4 tiles are not GPU launch sizes.",
			"lineHeight": 1.25,
			"autoResize": true,
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "source",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "source"
				}
			},
			"index": "b43"
		},
		{
			"id": "yMsyupCl",
			"type": "image",
			"x": 90,
			"y": 1230,
			"width": 255.75,
			"height": 186.45,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"roundness": null,
			"seed": 71905,
			"version": 2,
			"versionNonce": 173851009,
			"updated": 1792682243861,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [],
			"link": null,
			"locked": false,
			"frameId": null,
			"hasTextLink": false,
			"created": 1792682243849,
			"fileId": "6a5eafffbbc98c306ee959d505183a9d85d33ea2",
			"customData": {
				"agentDiagram": {
					"diagramId": "flashattention-flagship",
					"logicalId": "online-rescale-v2",
					"role": "body"
				},
				"dsl": {
					"document": "flashattention-flagship",
					"key": "online-rescale-v2"
				}
			},
			"scale": [
				1,
				1
			],
			"index": "b44"
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
		"scrollX": 694.25,
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