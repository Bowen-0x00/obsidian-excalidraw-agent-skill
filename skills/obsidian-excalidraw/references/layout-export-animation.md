# 排版、Arrow特殊属性、动画与外部导出

## Distribute

现有Bridge支持`distribute`与`align`，输入明确native IDs。简单独立元素：

```json
{"op":"distribute","targets":["a","b","c"],"direction":"horizontal","includeBoundText":true}
```

Bridge horizontal/vertical算法按外包围盒总跨度与总尺寸计算等边距；绘图脚本`distribute/Action-Distribute-Horizontally/Vertically.md`则先BFS合并group/container/bound text为不可分割实体、按视觉中心等距、首尾不动，还处理单实体在frame中居中。两者不是等价实现，不能把MCP独立元素distribute用于复杂群组后声称保留全部内部布局。

复杂组先显式求group/container/bound-text闭包、计算每组真实bounds，再translate整组并去重绑定text位移，或在受信宿主复用原Action的算法。文字已跟随容器移动时不能二次移动；箭头绑定/锁定图元须读回校验。对角线/文字排版看`Action-Distribute-Diagonally.md`与`Action-Distribute-Text.md`，不造第三个direction；没有对应adapter就受信脚本复用，不假称Bridge支持。paste auto-distribute是粘贴Hook，不能当全画布自动布局。

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
