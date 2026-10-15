# 常见图型与多风格参考

这些是可执行输入和工作流，不是渲染结果。使用`drawing_templates(action="list")`看图型与style列表；`action="get",name=...`取一份简短recipe，修改业务内容后执行。**不得把示例业务当用户事实。**

## 风格

| profile | 确定性规则 | 使用条件 |
|---|---|---|
| professional | roughness0、浅色solid、Helvetica与系统中文fallback、克制语义色 | 默认文档图 |
| handdrawn | roughness1、hachure、手绘线边；布局/绑定仍确定 | 用户要手绘效果，不等于自由笔画 |
| visio | roughness0、sharp边、1.5线宽、Helvetica与中文fallback | 正交工程图、UML；不声称输出.vsdx |
| blueprint | 白底蓝线、清晰数据通路与端口 | 电路/微架构；默认保留库素材本身样式 |
| presentation | 较大字号与标题层级、Helvetica与系统中文fallback | 原生frame演示页，指定库版式优先 |

在普通图描述加`"style":"visio"`或`"style":"handdrawn"`。允许对象`{"profile":"visio","fontFamily":"Helvetica","shape":{"strokeWidth":2}}`做显式覆盖。优先级：硬保护→用户显式局部字段→原图未请求字段→role/variant→profile默认。已有图不自动全图换主题。库源样式默认原样保留；只有用户明确要求才对本次导入的副本重新样式。

`roughjs`/`rough-js`是`handdrawn`的已声明别名；`drawing_templates(list)`同时返回aliases。自然语言中的“手画/handdraw白板笔迹”用原生`draw`/freedraw，**不是第二个Rough.js renderer或名为handdraw的profile**；可混用freedraw轮廓、原生文字及有binding的arrow。不要为证明多风格把所有场景都画成同一种矩形。

Visio/电路/微架构中的必要线—线交叉，采用修改版原生lineCrossings：独立线路arc/gap，明确连通才dot，不用白色遮罩模拟断开。visio profile不自动推断交叉语义；规划后按关系ref补patch_custom_data，详见layout-export-animation的Line Crossings。

演示与GIF适合1280×900左右的可读构图；极宽/极长全图在auto PNG中会缩小文字。先按语义组织少量列/行/分区，不通过删业务关系或截短标签压尺寸。`layout.nodeGap>=32`、`rankGap>=40`；默认值优先，紧凑布局需遵守真实planner边界。

## 流程图

`drawing_templates(get,name="flowchart")`，再`drawing_plan`或`drawing_templates(plan,...)`。节点、关系、分支标签齐全；长中文先测量和语义换行。菱形不要过宽；失败回边用外围通道，不能为了美观删业务关系。

## UML类图

`drawing_templates(get,name="uml-class")`。`nodes`含`id,label,attributes,methods`；`edges`含关联、composition/aggregation端点头与multiplicity标签。`drawing_templates(plan,name="uml-class",context_token,data=diagram,style="visio")`生成原生三分区类框、分隔线、独立文字与group；提交后可继续改字段和方法。

- 实心diamond放整体端是composition；空心diamond对应aggregation。泛化triangle_outline在父类端，realization还应dashed。
- 不根据“UML”三个字自动选择类图；用户强调交互顺序时选sequence。
- class整体移动用成员闭包，不仅移外框；外部连接绑定class body。

## UML时序图

`drawing_templates(plan,name="uml-sequence",data={participants,messages,title},style="visio")`。参与者head、虚线lifeline与逐时消息是原生元素；返回消息用dashed。

```json
{
  "participants": [{"id":"user","label":"用户"},{"id":"api","label":"API"},{"id":"db","label":"数据库"}],
  "messages": [{"from":"user","to":"api","label":"请求"},{"from":"api","to":"db","label":"查询"},{"from":"db","to":"api","label":"结果","return":true}],
  "title":"请求时序"
}
```

透明原生port只服务于消息绑定，不能看不到port就断言消息没有锚点。当前recipe没有自动实现任意alt/loop/activation DSL；用户要求这些时通过明确原生容器/短线补齐并看PNG，不宣传成全UML标准验证器。

## 系统架构图

`drawing_templates(get,name="architecture")`，普通`drawing_plan`执行。group是一起移动，container是可见分区，两者分开。跨容器边不能变成说明文字来“消除穿线”。代码测量+路径避障，PNG检查标签留白和层级。

## 微架构/电路：用户指定库优先

`drawing_templates(get,name="microarchitecture"|"circuit")`提供数字电路库示例；示例中的library来源必须替换为用户机器上已发现的真实库。用户指定的目录原文可传给`drawing_library`，它会返回真实resolvedLibrary；找不到或同名歧义不能悄悄用其它库。

可按文件名查找 `digital-circuit-components(svg).excalidrawlib`，但不能假设任何绝对路径或固定item数量。先通过 `drawing_library(list/query)` 发现安装库与真实vault相对路径；同名item用exact ID。顺序：query→get真实bounds/类型/资源→preview候选→**按角色/端口和目标内容区计算library.scale**→compose或native insert→以缩放后的几何连接与label→全图check/PNG。库素材svgPathShape仍是可编辑line carrier，不是整项PNG。node.size增加布局空位不会放大库符号；已导入尺寸不合适就对完整实例scale_selection，见[尺寸适配](layout-export-animation.md)。

`drawing_compose(context_token,base_revision,diagram)`接受普通nodes和：

```json
{"id":"alu","label":"算术逻辑单元","library":{"source":"指定库路径","item":"ALU","scale":2}}
```

库图元是line时不能假称能直接作为箭头绑定目标。组合器请求透明原生rectangle anchor，和整项编组；外部连接用返回anchorElementId，内部元素原样保留。`fromFixedPoint/toFixedPoint`是0–1比例，但必须按**当前素材的真实端口stub**计算，不能把示例0.28/0.72当固定MUX引脚：端口scene位置=`carrier origin + source stub × targetSize/viewBoxSize`，比例由当前anchor几何反算。库未声明电子引脚时只提供几何锚点，不臆造电气语义或网表验证。

每次native插入分别提交；出错返回已完成的stage/ID，不自动重放整图。重复item插入生成独立ID/group/frame，不共享身份。

## 多页演示：presentation-bundle

`drawing_templates(get,name="presentation")`提供同系列intro/slides页计划；先发现本机的 `presentation-bundle.excalidrawlib`，再将真实返回路径传给 `drawing_present`。本包不分发素材库，不假设本机已经安装这些模板。

`drawing_present(context_token,base_revision,presentation)`逐页原生插入frame模板，保留装饰、组与源→native ID映射，再用原生text填标题/正文。**先get源frame尺寸并计算presentation.scale，再填字；不能默认小底板scale=1然后把正文挤在上面。**各模板源尺寸不同则分次调用或逐项insert后适配；没有page.scale/width/height自动fit字段。不能手写frameId猜关联。title/body越界先检查底板尺寸、留白和布局，再按内容拆页，不裁业务文字。每页返回frameId与elementIds，用这些IDs导出单页PNG；还需全图overview与所有页实际看图后review。

```json
{
  "library":"Libraries/presentation-bundle.excalidrawlib",
  "pages":[
    {"template":"Simplicity (intro)","title":"绘图方案","subtitle":"原生可编辑与视觉反馈"},
    {"template":"Simplicity (slides)","title":"执行闭环","body":["自然语言组织语义","原生绘图和程序检查","PNG反馈与局部修正"]}
  ]
}
```
示例的library路径和template名称必须先经query/get确认；它们不是每台机器的默认值。当前输出是可编辑的Excalidraw演示页面，不自动声称PPTX。用户明确要求.pptx时需加载本机实际提供的对应PPTX Skill，并说明演示页导出与原生Excalidraw源之间的编辑边界；没有调用真实导出工具就不能改文件后缀假装PowerPoint。

## 含复杂图元的模板

需要draw、cuboid、brace、callout、代码高亮、checkbox或特定连接样式时，再读`references/native-features.md`并用`drawing_primitives`。常见图recipe和低层图元是互补关系；Skill始终要执行完整PNG评审循环。
