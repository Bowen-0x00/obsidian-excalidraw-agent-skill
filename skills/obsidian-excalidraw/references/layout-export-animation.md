# 排版、Arrow特殊属性、动画与外部导出

## Distribute

现有Bridge支持`distribute`与`align`，输入明确native IDs。简单独立元素：

```json
{"op":"distribute","targets":["a","b","c"],"direction":"horizontal","includeBoundText":true}
```

Bridge horizontal/vertical算法按外包围盒总跨度与总尺寸计算等边距；绘图脚本`distribute/Action-Distribute-Horizontally/Vertically.md`则先BFS合并group/container/bound text为不可分割实体、按视觉中心等距、首尾不动，还处理单实体在frame中居中。两者不是等价实现，不能把MCP独立元素distribute用于复杂群组后声称保留全部内部布局。

复杂组先显式求group/container/bound-text闭包、计算每组真实bounds，再translate整组并去重绑定text位移，或在受信宿主复用原Action的算法。文字已跟随容器移动时不能二次移动；箭头绑定/锁定图元须读回校验。对角线/文字排版看`Action-Distribute-Diagonally.md`与`Action-Distribute-Text.md`，不造第三个direction；没有对应adapter就受信脚本复用，不假称Bridge支持。paste auto-distribute是粘贴Hook，不能当全画布自动布局。

## 尺寸适配：先定用途，再插素材

库里的坐标单位和原始尺寸不是最终阅读尺寸。Agent须主动决定大小，不要求用户给坐标，也不能把“小但无碰撞”当成已完成。PNG导出`scale`只提高输出像素，**不会改变元素之间的大小关系**。

| 对象/时机 | 已有入口 | 适用边界 |
| --- | --- | --- |
| 素材尚未插入 | `drawing_library(insert,scale=s)`；compose的`nodes[].library.scale` | 整项等比缩放；默认1不是自动fit。compose的node.size只影响布局空间，不会替代library.scale |
| 素材/整页已插入 | `drawing_apply`的`scale_selection {targets:[完整成员ID],factor:s,fromCenter:false}` | 原生整体缩放位置、点列、文字和frame子元素；含透明anchor和全部装饰，不只选可见主图元 |
| 单个普通形状或图片 | `resize {target,width,height,anchor:"top-left"}` | 仅改该元素尺寸和绑定文字布局，不自动缩放组员/字号；line/arrow被拒绝，SVG line carrier用scale_selection |

1. `query/get`取得精确`bounds`，`preview`看真实内容。已有图按ID读取full，并确认groupIds、frameId、锁定、绑定和实例成员；不要把整个共享外层group误当某个小符号。使用插入返回的`insertedElementIds/sourceIdMap/anchorElementId`定位本次素材。
   模板中已通过预览确认的整页底色/内页rectangle是合法包含背景；需要时以`patch_custom_data.merge:{isContainer:true}`声明容器语义再检查，不移动/删除底板来消除“重叠”。不得给真正冲突的业务节点乱标container，也不把所有库矩形自动当背景。
2. 选内容区`W×H`，给图文留内边距。等比装入用`s=min(W/sourceWidth,H/sourceHeight)`；按目标宽或高用相应比值，另一维同步计算。`s>1`允许放大。页模板以frame宽高为页面基准，普通符号以整项真实bounds为基准；含标题等突出部分时另查整体bounds，防止相邻页相碰。库scale现有范围`0<s<=20`，不把这个范围误写成PNG倍率。
3. 插入前优先传scale，减少重排。插入后算的是`factor=目标尺寸/当前尺寸`，不是源尺寸的绝对scale；多次修改每次重新读当前尺寸，不能反复乘同一绝对倍率。精确选区用targets，原生group确认无多余内容时才用groupId。`fromCenter:false`便于保留左上角；要求居中则显式true。
4. 演示新页未指定尺寸时，以1280×720作为版式起点，先适配模板再测量/填标题、正文和图片。模板比例不同则保留比例，选择合适同系列版式、留白或按用户允许重排；不把4:3模板静默拉伸成16:9。`drawing_present`现有输入是**presentation顶层scale**，不是page.scale/width/height；各页源尺寸不同时分次调用或逐页insert后适配，不能传不存在的自动fit字段。
5. 电路/架构先按角色和端口密度确定符号目标大小，同类同尺度；不同角色不强行同宽高。读真实stub后在**缩放后**重算端口scene坐标和fixedPoint，再接线。对已连线符号缩放其完整实例（含anchor），不选只接一端的外部箭头；邻边随绑定更新后读回检查。放大透明anchor而不放大可见SVG不算适配。
6. 按目标阅读字号测量新文字。底板放大后再填字；已有完整页整体放大会连字号一起放大，随后按用户意图调整正文排版，不靠压小字体掩盖底板或空间不足。确实需要更多内容时调整布局/页尺寸或拆页，不删减业务内容。
7. read确认实际尺寸、相对位置、frame归属、ID/源码和绑定；check→全图及单页/局部PNG→实际看图→review。必须把“底板不足、符号主次比例失衡、字太小”作为视觉问题修正；程序无重叠不等于尺寸合适。锁定/原生API缺失则明确报告，不伪称已resize。

例如读取某符号60×45，要240×180，插入用`scale:4`；已插为120×90则用`factor:2`，不是再乘4。这是计算示例，不是每个ALU/MUX的固定尺寸。

## 原生选区旋转与缩放

Bridge 0.13.0新增`rotate`、`scale_selection`，通过现有`drawing_apply`批量提交，没有另造MCP工具或复制缩放算法。宿主`App.selectionTool.ts::maybeHandleResize` → `resizeElements.ts::transformElements` → `rotateSingleElement/rotateMultipleElements/resizeSingleElement/resizeMultipleElements`；实际安装包入口是`excalidrawAPI.App.maybeHandleResize`，不可用时报`NATIVE_TRANSFORM_UNAVAILABLE`，不回退逐项改JSON。

```json
{"op":"rotate","groupId":"真实原生group ID","degrees":90}
{"op":"scale_selection","targets":["节点A ID","节点B ID","内部箭头ID"],"factor":1.5,"fromCenter":true}
{"op":"patch_element","target":"单节点ID","patch":{"angle":1.5707963267948966}}
```

- `groupId`与`targets`二选一。targets是精确选区；groupId读取当前`groupIds`，包括嵌套组中的成员，不用logicalId代替。绑定text由owner处理一次；单独选绑定text会提升到owner。
- `rotate.degrees`是相对角度，正数顺时针；`element.angle`及patch.angle是绝对弧度。共同中心由真实边界求出；不是各自绕自身中心修改angle。
- `factor>0`，默认中心缩放；`fromCenter:false`保留未旋转多选边界左上角，单个已旋转元素则对应其本地西北角。位置、点列、形状与文字同缩放，字号/最小尺寸/anchored资源遵从原生规则；不提供镜像或非等比整组缩放。
- 内部箭头保留双向绑定；节点的外部箭头更新端点，外部节点保留。若明确选中箭头但没有选其绑定端点，报`TRANSFORM_PARTIAL_BINDING`；原生变换若改变连接目标则报`TRANSFORM_BINDING_CHANGED`，不静默丢业务关系。
- 原生Frame不允许旋转；缩放包含frame children及绑定文字。锁定选区或被更新邻边/文字报`ELEMENT_LOCKED`。最小尺寸导致无变更报`NATIVE_TRANSFORM_NO_CHANGE`。
- 执行器同步切换到隔离Scene副本，恢复App scene/state/selection/Hook后才提交变更，保留同一事务revision检查与undo。失败不提交之前暂存的变换。返回`transforms`包含center、selectedIds、updatedIds、degrees/factor和真实实现来源。
- `afterTransformElements`宿主Hook可能异步写live API，因此准备阶段不触发。表格行列边界联动、泳道吞并/剥离等Engine特定手势**不是**这两个原生几何操作的承诺；相关元数据不自动重解释。
- 90°整数倍的世界坐标bbox/直线点列纳入现有碰撞检查；任意非直角旋转与曲线仍unknown，不伪造check=pass。完成后read/check→PNG→实际看图→review。

真实宿主验证：同组双节点+内部标签箭头绕共同中心顺时针90°，再放大1.5倍，节点文字20→30；外部节点及文字不变，外部箭头跟随；另验证绝对π弧度、已旋转单节点缩放、负坐标freedraw点列/压力、SVG path源保留、Frame children缩放、锁定/失败不提交与undo。PNG均实际查看，非对所有扩展Engine作全面手势兼容保证。

## 原生 Line Crossings：弧跳、留白、交点

这是更新后的Excalidraw-ymjr**渲染器**能力，不是额外Engine、素材或MCP Feature。作用于原生`line`/`arrow`的`customData.lineCrossings`；原始points、ID和绑定保持不变，交叉邻居移动后由宿主重算呈现。原生几何优先，**禁止默认叠白色/背景色矩形遮罩、手画桥弧/圆点或切成多条线模拟断开**；gap是实际抬笔留白，彩色背景不穿帮。

| 值 | 表达 | 选择规则 |
|---|---|---|
| `arc` | 跨越方绘制弧跳 | 业务/电气上不连接；默认垂直线跨过水平线 |
| `gap` | 让路方在交叉处留白 | 不连接；默认水平线让路，建议相交两线都标gap |
| `dot` | 实心交点 | 仅当用户语义确认在此连接/汇流；**视觉标记不新增端点绑定或netlist关系** |
| `none` | 普通交叉，无跳线处理 | 显式关闭此样式；不是“保证两线物理不连接”的语义替代 |

### 现有MCP调用，不新增DSL

`drawing_apply`的原生创建可以直接传customData。两条线都声明相同模式，不依赖侧栏“下一笔继承”的会话状态：

```json
[
  {"op":"create_linear","kind":"line","ref":"horizontal","x":0,"y":120,"points":[[0,0],[300,0]],"style":{"strokeWidth":2,"roughness":0},"customData":{"lineCrossings":"arc"}},
  {"op":"create_linear","kind":"arrow","ref":"vertical","x":150,"y":0,"points":[[0,0],[0,240]],"endArrowhead":"arrow","style":{"strokeWidth":2,"roughness":0},"customData":{"lineCrossings":"arc"}}
]
```

连接已知节点时，把同一字段放在connect的**顶层customData**，不是style，不是`set_feature`：

```json
{"op":"connect","ref":"bus","from":"@source","to":"@target","elbowed":true,"style":{"strokeWidth":2,"roughness":0},"customData":{"lineCrossings":"gap"}}
```

已有连线按明确ID做merge，保留其他扩展与绑定；批量是多个操作，并非patch_custom_data支持targets：

```json
[
  {"op":"patch_custom_data","target":"水平线ID","merge":{"lineCrossings":"gap"}},
  {"op":"patch_custom_data","target":"垂直线ID","merge":{"lineCrossings":"gap"}}
]
```

关闭用`merge:{"lineCrossings":"none"}`，或`remove:["lineCrossings"]`；不要替换整份customData。迁移旧遮罩图时先确认哪些ID确为模拟交叉的装饰，仅移除这些冗余遮罩/假弧/假点，保留原业务线、标签和用户主动叠放内容，不全图clear重建。

当前planner的`diagram.edges`和`drawing_primitives`连接输入**不会自动转发任意edge.customData**。不要把字段塞进图描述后当已生效：保留完整plan.operations，再附`patch_custom_data {target:"@edge:关系逻辑ID",merge:{lineCrossings:"arc"}}`，或apply后用真实refs/ID修改；primitive按其返回ref处理。使用`drawing_templates(style="visio")`也不会自动加交叉语义。

### 优先级与适用边界

- `customData.lineJumpPriority`是数字；当前源码只有**两条线都提供数字且不同**时才按较大值跨越，否则回到垂直/水平规则，同向或斜线再按ID确定。要水平线弧跳，就给水平线10、垂直线0，并把两者lineCrossings设为arc；不要只给一根线10就声称强制优先级成功。
- arc桥弧/gap半宽当前默认8个scene单位，近邻交点可能缩小；不是PNG固定像素，也没有已暴露的radius配置。不要靠装饰图元改半径。
- 首选直线/折线/正交elbow箭头。靠近端点/拐角、极短线段、平行或共线重叠有排除规则；曲线、block-arrow和svgPathShape走特殊渲染分支，不保证与普通点列有相同交叉效果，不把所有line载体都设为走线。
- T型分支由几何端点与线段位置识别，不应强行桥接；用户提供规范描述了自动圆点，源码也有junction记录，**本轮真实PNG的T分支未显示圆点**。不可把自动圆点当已验证的导出保证；需要这一语义时实际查看并报告差异，不悄悄补一个假圆点或修改用户插件。
- `dot`不修改startBinding/endBinding/boundElements，不能用它代替connect/rebind的业务关系。`arc/gap`也只解决线—线交叉，不免除穿节点、标签遮挡、箭头端点错误等检查。
- 侧栏Line Crossings可改选中line/arrow，并通过`currentItemLineCrossings`影响后续手绘线；Agent自动创建仍逐条显式传值，避免修改全局绘制偏好。Native CLI与Bridge schema不同，先读其schema确认customData是否允许；未确认时走已验证MCP，不照抄op到原生CLI。

### 验证与能力来源

先按目标ID读full，确认line/arrow、原始points和业务绑定；apply后重新读回customData及关系，再全图PNG实际查看。交叉配对需要场景上下文，ids局部PNG必须包含两根相交线，单根预览不能证明全图无交叉。没有新renderer的旧宿主可能保存字段却不显示效果；字段能写≠能力已生效，不静默退回遮罩技巧。

本轮已在真实更新宿主验证：arc/gap/dot/none、两线数字priority反转；浅蓝背景下gap露出原背景、无交叉遮罩；connect创建的双向绑定elbow箭头弧跳→gap切换；patch前后ID/points/绑定与元素数量保持。PNG实际查看；T分支圆点缺口单独保留。没有以这轮PNG证明SVG/所有特殊箭头或交互帧率。

来源：用户提供的Line Crossings规范；内核`packages/element/src/crossings.ts`（检测/优先级/path）、`shape.ts`（普通/elbow分支）、`renderElement.ts`（Canvas交点）、`packages/excalidraw/actions/actionProperties.tsx::actionChangeLineCrossings`及`App.tsx`（UI继承）。文档中的8px/60FPS不是Agent必须硬编码的布局常数或已测性能承诺。

## Arrow特殊属性

| 属性/功能 | 真实入口/字段 | 限制与检查 |
|---|---|---|
| 箭头端点与头类型 | Bridge `set_arrow_style`/`arrow_style`，startArrowhead/endArrowhead；arrow/bar/circle及outline/triangle/diamond/block_arrow_outline按runtime集合 | 保持原生绑定，不直接patch绑定内部字段；头大小不能遮标签 |
| 头部大小 | `customData.arrowHeadSize`，Bridge校验0.125–8 | 这是真实ymjr倍数，不等于像素宽度 |
| 特殊点拖拽约束 | `customData.fixedDragablePoints={dragablePointIndex,fixedPointsIndex,centerIndex}`，Arrow-Head-Resize Engine | 索引数组，-1表示末点；不是arrowHeadSize；必须与实际points一致 |
| 定长旋转 | `customData.fixedLength=true`，Fixed-Length Engine的handlePointDragging | 以局部[0,0]为基准保持拖拽半径；不是任意复杂折线路径总长度锁定 |
| 实时测量 | `customData.measure={ratio,unit}`，`plugin.measureEngine.updateMeasureText(elements,isLiveDrag)` | 代码测量首尾直线距离`hypot(dx,dy)/ratio`，并非折线路径长度；标签可能被复用/覆盖，不与业务箭头标签混用 |

已有非交互样式示例：

```json
{"op":"set_arrow_style","targets":["arrowId"],"endArrowhead":"block_arrow_outline","arrowHeadSize":2,"strokeWidth":2}
```

fixedLength/measure特殊Engine不在默认bundle内；按[script-execution](script-execution.md)发现并挂载宿主真实脚本。原定长/测量Action是浮动面板，不能在无UI自动等待。`Feature-Measure-Engine`直接维护文字/索引，使用前核对宿主版本与既有绑定，读回关系；未验证就不声称真实测量交互通过。

## Animation与演示

- **Arrow animation**：`animation/Feature-Arrow-Animation-Engine.md`读`customData.animation={type:"flow"|"dash"|"arrow",speed:number,color:CSS}`，Action仅是选线配置面板。Engine维护overlay canvas/RAF；PNG不保存运动。按实际speed范围/颜色配置，演示前后检查原箭头绑定和非动画内容。
- **Progressive drawing**：`Action-Progressive-Drawing-Animator.md`提供选中/全图逐笔、打字、播放暂停/停止/录屏模式。plugin `_ymjr_animator`存active/paused/progressMap；函数在Action作用域，未暴露MCP控制API。需要真实UI控制或用户授权改为非交互的本地脚本，不捏造`drawing_animation`。必须验证播放/暂停/停止与缓存恢复，不只截图第一帧。
- **Step appear**：`step-appear/Action-Step-Appear-Setup.md`沿选定引导线找实体并写`customData.appear={index}`，随后删除引导线；因此有明确删除副作用，只有该线被用户指定用于设置才运行。Engine基于hide逐步显示，需保留组和bound text同一index。PNG只代表当前步骤。
- 静态多页演示使用原生frame + drawing_present；动态演示和PPTX导出不是同一功能。没有真实视频/PPTX出口不能宣称已生成动画文件。

本包默认不部署上述animation/step-appear Engine。普通绘图不自动开启持续RAF/鼠标模式；用户要求演示再挂载，完成后按真实stop/disable恢复，不能通过Native CLI一次性script启动常驻动画。

真实smoke已观察Arrow animation overlay的像素hash与globalOffset跨RAF帧改变，调用`plugin["disable_ymjr.feature.animation-engine"]()`后overlay消失且loopId为null。逐笔/step-appear播放没有在本轮运行，不能把箭头动画证据覆盖这些独立能力。

## Export与其他软件

- PNG/SVG：现有MCP preview、EA createPNG/createSVG或Native CLI export；按明确文件/区域、资源和尺寸预算，实际看PNG。SVG/PNG是交付格式，不自动替换原图。
- **Anki**：`export/Action-Export-Image-To-Anki.md`生成选中元素SVG后浮动面板调用AnkiConnect，默认端口8765；真实payload为`action:"addNotes",version:6`，`notes`中deckName/modelName/fields/tags。原脚本写Default/Basic，不能代替用户所需deck/model。这是外部写入，需要用户明确导出授权、接口/字段正确与真实result确认；不自动创建卡片当smoke。
- **Eagle**：`Action-Export-Image-To-Eagle.md`纯图片用本机文件`/api/item/addFromPath`，混合图元用SVG dataURL的`/api/item/addFromURLs`；`Feature-Export-Eagle.md`也提供右键项。真实token从用户私有配置读取，不能把脚本里硬编码示例token复制到Skill或报告。HTTP ok不等于库item写入已核对，需真实返回/目标库确认；用户明确授权才发送。
- Embeddable DOM导出依赖`Feature-Export-Embeddable`真实capture；网络或DOM资源失败应incomplete，不用空边框冒充。外部应用联动不在drawing_preview的默认副作用内。

来源（相对绘图脚本目录）：`distribute/*`、`arrow/*`、`animation/*`、`step-appear/*`、`export/*`；Bridge `distribute/set_arrow_style`。接口版本和外部应用条件须在任务环境实际发现。
