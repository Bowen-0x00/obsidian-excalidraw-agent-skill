# 视觉效果、列表和常见元素

## 已有Bridge适配器

### Shadow

目标类型任意，Bridge `FEATURE_SPECS.shadow`支持`set_feature/clear_feature`，存储`customData.shadow`和`customData.hover.shadow/pointer`，需要Shadow Engine：

```json
{"op":"set_feature","feature":"shadow","targets":["shapeId"],"config":{"shadows":[{"shadowColor":"rgba(0,0,0,0.3)","shadowBlur":"12px","shadowOffsetX":"6px","shadowOffsetY":"8px"}],"hoverPointer":true}}
```

`shadowColor`可CSS色或相对亮度数值；blur/offset的无单位数是相对比例，只有`22px`这类字符串是绝对像素。不要用复制偏移的多边形假造阴影。通过`set_feature`，不要直接写gradient/document/echarts等受限customData；Bridge会拒绝不安全字段。阴影静态效果可随PNG检查，hover shadow必须另做鼠标验证。

### Callout

目标是rectangle，Callout Engine根据`customData.callout`渲染标题栏、图标和bound body text。Bridge适配器：

```json
{"op":"set_feature","feature":"callout","targets":["boxId"],"config":{"type":"warning","colorType":"alpha"}}
```

真实type包括`note/info/tip/success/failure/warning/error/quote/cite/example/danger/bug/question/abstract`；先以runtime feature spec为准。`title`不是随便叠加一个文本，复杂标题/正文须使用Engine的真实绑定规则或`drawing_primitives kind=callout`。Edge/外部连接不要假定Callout header是正文容器。PNG可证明当前渲染，不证明编辑时避让。

### Code highlight

目标是text，source文字保持原始换行与缩进：

```json
{"op":"set_feature","feature":"code_highlight","targets":["codeTextId"],"config":{"language":"python","theme":"atom-one-dark","embedFont":true,"fontSize":16}}
```

Bridge存储`customData.codeHighlight`，Engine渲染高亮；theme/language必须是宿主真实配置，不因字符串看起来合法就当支持。不要为适配窄框删减源码；先用native `drawing_measure`，调整容器/字体/局部PNG。高亮是渲染，不执行代码；PNG对可读性需实际查看。

### Gradient 和富文本

已有Bridge `gradient`适配器仅接受direction `horizontal/vertical/diagonal/radial`和至少两个`{offset,color}` stops，拒绝raw JavaScript gradient；`rich_text`支持全局bold/fontWeight/color/gradient及局部bold/color，不支持partial_gradient。旧样例中的`customData.gradient`代码字符串不能直接回写。

## Smart list 与 Bullet

这两个功能不同：

- **Smart List Engine**：对选中的已有元素写`customData.list={type:"order"|"unorder",index?:number}`，Engine在Canvas旁实时画序号/项目标记，不创建额外文字元素；`continue`会按上方最近列表延续order index。列表是交互渲染，不把Unicode `1.`/`•`写入业务文字。PNG可检查当前静态编号，但Engine必须运行。
- **Bullet Engine**：用户通过面板启用后点击画布，真实生成“椭圆容器+文本”的原生元素组；默认设置来自`plugin.settings.scriptEngineSettings.bullet_settings`：`fontSize`、`circleSize`、`colorList`、`fontColor`。它是可移动可编辑的真实元素，不是Smart List的同义词。自动生成需要真实UI/Engine或授权非交互EA脚本复用`addText({box:"ellipse"...})`，不要声称Bridge已有bullet Feature。

Smart List的安全更新可用受信脚本：读取选中元素→copy到EA→merge `customData.list`→await `addElementsToView`；不要直接拼完整元素JSON。Bullet的点击放置需要实际宿主Canvas，默认脚本是面板交互，URI只能触发不能提供点击坐标。

## 常见生成图元

现有`drawing_primitives`能规划`draw/polygon/cuboid/brace/callout/code/checkbox/connection`，与`native-features.md`配合。`generate/Action-Generate-Digital-SVG.md`和`Action-Generate-Digital-Microarch-Items.md`是用户脚本参考，不是本包自动调用的隐含模板；运行前读取、备份、绑定明确画布，使用真实测量和`svgPathShape/svgViewBox`。

所有视觉效果遵循：原生编辑性优先；Feature元数据和Engine依赖记录；check→PNG→实际看图。不存在真实adapter的功能用[script-execution](script-execution.md)和用户授权的受信EA脚本，不能把面板按钮包装成无交互MCP。

来源：Bridge `FEATURE_SPECS`中的`shadow/callout/code_highlight/rich_text/gradient`；绘图脚本目录下`shadow`、`callout`、`code-highlight`、`list/Feature-Smart-List-Engine.md`、`generate/Feature-Bullet-Engine.md`及`native-features.md`。
