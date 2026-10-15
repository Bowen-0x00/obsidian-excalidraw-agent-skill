# 硬件微架构：先表达部件和信号，再绘图

## 强制分流与任务边界

用户说CPU/流水线/微架构/数据通路/缓存层级/寄存器堆/阵列/互连/加速器时，**在创建图元前读取本参考**。不是普通服务架构图；不能因为主Skill有低往返路径就直接提交一列nodes+edges。速度优化只减少JSON复制和模型往返，不降低结构粒度。

先区分用途：系统/模块概览、微架构块图、详细数据通路、门级电路。用户未进一步说明“微架构”时，默认**部件级＋关键端口/信号**；不能自行降成五阶段说明或功能列表。无需追问普通视觉细节；只有ISA/流水级/分支解决位置/目标实现差异会改变结构且无依据时，问一个关键问题或明确声明保守教学假设。用户给了真实架构/RTL/论文则以真实资料为准，不补造容量、带宽、流水级或功能。

三类参考表达的要点：TPU式是存储/阵列/控制/带宽与回流，RISC式是流水边界/MUX/命名端口/旁路网络，南湖式是层次区域/队列/重复执行单元/存储层级。矩形并非错误；**把不同部件都做成同尺寸文字卡片、把信号都做成模块间关系箭头才是错误**。不是每个抽象模块都必须画门级图标，也不是强制所有架构套五级CPU。

## 创建前的硬件计划（简短表，不是新DSL）

先在Agent工作计划中确定以下内容，不要求用户手写JSON：

1. **已知事实与假设**：用途、抽象层级、ISA/时序边界、数据宽度/数量/容量的依据；未指定不猜具体型号指标。
2. **部件清单**：每个需要讨论的ALU、MUX、RF、存储、流水寄存器、队列、控制器、阵列/执行lane是独立对象；记录角色、阶段/区域和重复数量。不把关键部件仅写进阶段框的bullet。
3. **端口表**：部件的输入/输出/控制端口、数据宽度及方向；区别数据值、寄存器号/地址、选择/使能和状态。RF读/写端口、MUX数据/选择、ALU A/B/result、memory addr/wdata/rdata/we不要接成同一个中心点。
4. **信号表**：`source.port → destination.port`、数据/控制/反馈/旁路类别、时序跨哪个寄存器、必要的总线名称/位宽；一条值不能靠“数据+控制”标签代替其明确路由。可聚合明确的控制bundle，但必须在消费端拆解/标明。
5. **空间骨架**：流水级固定列/行、边界寄存器狭长条、主通路和旁路/控制通道、存储/阵列形状、主标题/图例。这不是普通有向图的拓扑rank。
6. **验收清单**：每个部件/关键端口/关系必须在画布中真实存在；哪些关系可合并为总线、哪些细节明确省略。后续报错不得偷偷改变这份清单。

计划按实际任务展开，别先生成几十个空字段的大DSL。`customData.agentDiagram`可保存logicalId/role/原文及Agent注释，但注释不是电气网表、实际绑定或新MCP参数。

## 现有接口的能力与限制

- `kind:"microarchitecture"`只是已有planner接受的分类，**没有自动硬件符号/阶段列/多端口/bus布线语义**。单纯改kind不能把服务架构图变成数据通路。
- 普通planner按有向边最长路径分层；控制边会影响rank。`containers`是节点排完后的包围框，不会把所有EX单元固定在EX列。需要硬件骨架时用显式`nodes[].position`/实际尺寸、原生create/apply分批构图或库insert，然后显式connect路由。
- compose仍可在代码内完整plan→apply，inspect仍可合并check/PNG；但只在它能保留本计划的硬件拓扑、尺寸和位置时使用。复杂固定列图可以先创建全部部件再一次批量连接，不要求每条线等一个模型响应。
- planner字段是`layout.nodeGap/rankGap`，不是nodeSpacing/rankSpacing；容器成员是`members`，不是children；节点style用strokeColor/backgroundColor。当前容器的逐项style不是通用承诺，使用profile.container/实际region.color或按native refs patch，**输入字段写了不等于生效**。
- 不同节点输入size/position要按当前真实schema；原生图元x/y是scene左上角，线points是局部点且可负，connect.waypoints是scene点。只让API维护ID/version/index与双向绑定。
- 创建时优先省略`id`让API生成原生ID，用`ref`保存长logical名称；后续用refs/read回实际ID。已实测某宿主保存会把新建长text ID规范化为8字符，导致revision/preview过期；不能手填`text_rf_wdata_label`之类ID后假称身份稳定。**先保存并重新read，再check/PNG/review**；若ID改变，按实际映射重建非持久回执和断言，不对旧ID继续操作，也不改用户原生版本机制。

## 符号、尺寸和素材

- **先发现/查询真实用户库**，确认当前可用ALU/MUX/寄存器/队列等，get/preview后按实际轮廓、朝向、viewBox与stub确定尺寸。用户指定库必须优先使用；名称相同用exact item ID。不预设个人路径、item数量或所有库引脚相同。
- 库中只有line/SVG carrier时，用insert返回的anchorElementId建立关系，保留完整instance/group与sourceIdMap；不直接把不支持的line当绑定目标。需要调整朝向/大小时对完整实例rotate/scale_selection，再按**变换后的**几何重算端口。
- 找不到/不适合现有素材时，ALU用原生闭合多边形凹口、MUX用多边形梯形＋明确数据/选择端、流水寄存器用狭长条并显示时钟/字段分段；这些是静态可编辑形状，不是用PNG替代。已有create_linear(polygon/closed)/create_svg_path及EA原生构造即可，不造第二个renderer。必要的透明anchor只服务绑定且与符号编组，不夸成已存在电子引脚。
  **不能把“查到库”当已使用符号**：若最终MUX仍是写着“MUX”的普通矩形且无可辨输入/选择端，或ALU/RF端口仅在正文中列名字，验收不通过。原生构造可用`{"op":"create_linear","kind":"line","x":100,"y":100,"points":[[0,0],[60,12],[60,88],[0,100]],"polygon":true,"closed":true,"style":{"strokeColor":"#1d4ed8","backgroundColor":"#eff6ff","fillStyle":"solid","roughness":0}}`创建MUX梯形轮廓（坐标仅示意）；端口/anchor/文字需按真实输入数另建并编组，不能直接把line轮廓当可绑定节点。
- RF/memory/queue/cache可以用矩形，但使用不同长宽比、端口、内部区划/entries或bank示意表达角色；阵列用适量重复格/网格＋数量标注，不为显示64k单元生成64k对象。stacked memory用真实层叠原生元素，合法包含/叠放有construction unit，不让诊断忽略所有重叠。
- 流水边界不是220×72文字卡片；以阶段间的窄高条贯穿所需数据/控制高度，字段标签简洁。计算块、memory、RF、controller尺寸由功能/端口密度和阅读尺度共同决定，不用统一最小220宽覆盖所有硬件。
- 配色按硬件角色和信号类别，不默认一阶段一种彩虹色。常用深蓝/黑实线数据、细红/橙虚线控制；灰度方案用线型/粗细/标签冗余。图例必须与实际元素颜色/虚实线一致，不能只写“红色控制”却仍画普通实线。

## 端口、总线和路由

- 对每条关键连接显式选source/destination的side/fixedPoint；多个RF输出或MUX输入必须分离。可在原生部件上加命名小端口/短stub；这些是实际图元，不把“Read Data1/2”写进说明就当已建端口。
- connect的`from/to`用真实部件/anchor ID，`start/end`的anchor、fixedPoint、mode按实际API传，维护start/endBinding及目标boundElements。命名端口标签与正确fixedPoint结合；只有命名metadata没有几何连接不算完成。
- 每个MUX须列出**每一路数据输入源和选择源**，逐项对应实际独立边；3:1旁路MUX不能只有ID/EX数据＋一根ForwardA虚线。Forwarding Unit只产生选择码，不产生旁路数据；EX/MEM.ALUResult与MEM/WB.WBData要分别到FwdA/FwdB数据端。load的EX/MEM值是地址而非读回数据，禁止当load value旁路。
- ALUSrc的立即数、store write data、WB的rd地址与RegWrite、PC的branch target与PCSrc是不同信号。BEQ判决由Branch控制与比较结果形成；branch target加法器结果不是AND门的逻辑输入。图中只连接其中一部分时必须标未完成，不能用RF/ALU框内一句“所有端口”冒充完整连接。
- 选择码必须与每个MUX输入编号一致（如MemtoReg=1是否选load，ForwardA的00/01/10各选何源）；不能只验“有三条入边”。信号表里写明选择映射，图内标号、控制输出说明、实际连接三者对照；如果采用非惯例编码，明确说明而非混用常见含义。
- 主数据从左到右/上到下，反馈/写回走外围通道，控制带在上或下；对跨多个流水级的旁路留独立track。控制器/Hazard/Forwarding常应在局部控制区域而不串进主数据链导致拉长rank。
- 可将同一真实网络以主干＋分支表示；每个fanout落在真实信号，分叉点dot仅用于语义连通，独立交叉用arc/gap。不能随便把各独立arrow的中点绑定在一起宣称电气总线。没有net对象的接口就保留明确端点列表和可验证分支，不假称完整网表验证。
- 短局部线不需要长段论文文字；用端口名、`rs1`/`rd`/`32b`/`MemWrite`等短标签，完整说明放旁边注释。跨级bundle可以有简短总线名，不能每条边都加“[数据通路]”把间距撑大。
- 自动LR的最长标签会扩大所有rank间距，不能靠无限增大rankGap消除拥挤。固定列时手动分配bus/label净空与折点，标签避开头部/节点。需要复杂精确路由就用显式waypoints，不假设通用避障器理解阶段列/控制网。

## 五级 CPU 的可执行规划范式

这是**无指定型号时的教学范式**，不是对任意CPU或用户RTL的事实断言。可采用单发射RV32I教学数据通路（ALU/load/store/BEQ；分支EX决策、静态不取、独立I/D存储），并在图中写清简化边界；用户指定MIPS/RV64/其它branch阶段则按实际改，不能混称“MIPS/RISC-V都完全一样”。未实现JAL/CSR/中断/乘除等不宣称完整RV32I实现。

- 五列IF、ID、EX、MEM、WB；四个边界IF/ID、ID/EX、EX/MEM、MEM/WB。边界显示数据及必要EX/MEM/WB控制bundle的跨拍保存，不能把Stage仅做成一个大框。
- IF：PC、Next-PC MUX、PC+4加法器、I-memory；两条next-PC值输入来自顺序值和branch target，select是独立控制端。PC+4和instruction进入IF/ID，PC或必要PC基值继续流向branch加法器。
- ID：RF至少两个读端口和rd/wdata/we写端；ImmGen、Decoder/Control、Load-use Hazard。指令字段分别到读地址/立即数/控制；读数据、立即数、rd和必要控制进入ID/EX。不要用一条“操作数+全部控制”边隐藏端口。
- EX：两路operand forwarding MUX、ALUSrc MUX、ALU、branch target加法器及比较/branch逻辑；Forwarding控制来自EX/MEM、MEM/WB的rd/RegWrite和ID/EX的rs1/rs2。操作数A/B、select、ALUCtrl及Zero/compare结果按端口分开。
- MEM：D-memory的addr/wdata/rdata/MemRead/MemWrite；ALU result/rd/control继续流入MEM/WB，store value应来自正确的寄存/旁路路径。可把存储和ALU结果并行直通画出，不让所有指令看起来都必须读memory。
- WB：result MUX在ALU result和load data间选择，输出writeback data/rd/RegWrite回RF；写回总线也参与forward。EX/MEM和MEM/WB旁路信号分别到对应operand MUX，而不只是写一段“Forwarding Unit”。
- Hazard输出PCWrite、IF/IDWrite、ID/EX bubble/flush等明确到消费部件；branch redirect/flush到正确PC选择和需清空的边界。简化设计采用哪些停顿/前递规则须写清，不把load尚未返回的数据错误地从EX/MEM当load value前递。

一次完整图可以用overview＋各区域局部PNG评审，不为了挤进1600宽删除这些对象。若具体细节会让图过密，可以按用户允许拆成“主数据通路”“控制/冒险/前递”两张互相对应的详细图，但不能把其中一张省掉，或偷偷降成阶段概要。

## 错误恢复：绝不靠降粒度通过

- 先读错误receipt和当前revision。compose有提交而check=fail时，图已经存在：**不再次compose整份diagram**，不换diagramId让重复创建保护失效。按错误native IDs修节点/端口/route/label；成功对象和全部业务关系保持。
- 若确需整体替换，仅对本轮明确创建的IDs做可追踪切换并保留原图/回执；不clear、不删除用户原内容，不在新文件重复画一个更简单图然后宣布原任务完成。
- 不把ALU/RF/MUX等独立部件收进“IF阶段：…列表”，不删除反馈/控制/旁路线，不缩短业务内容，不随便把冲突节点标isContainer以躲检查。需要改变抽象层级/省略内容必须征得用户同意。
- `expected`要非空并覆盖部件与关键关系，既有node_exists/edge_exists/label_equals/edge_label可用；它们只能证明确切已建对象/边，不自动验证电气时序。额外端口/阶段检查由执行代码或Agent按读回精确元素核对，不能传虚构assertion type。
- 第一次发现问题就记录review visual_issues及相关IDs；每轮计入同一预算，不把多次PNG后最终第一次review伪称只花一轮。达到上限或无进展报告needs_attention，不用新token/新文件刷过关。
- 不允许把程序异常用`except: pass`当作成功，也不对未知状态无条件revert再重新apply整图。先读状态/receipt，只撤销明确属于本轮且确需回退的事务；已通过部分保持，修复用最新revision按ID局部提交。批量客户端参数取当前安装包路径和`EXCALIDRAW_AGENT_STATE_DIR`，不猜Python包名或导入工作区旧原型；耗时源代码搜索不是绘图前提。

## 必须逐项验收

1. **结构粒度**：计划中所有硬件部件仍是独立图元/组件；关键端口有实际信号连接，不仅标签。阶段概要不能替代微架构。
2. **硬件逻辑**：沿“取指→读操作数→执行→访存/直通→写回”追踪一条ALU、一条load、一条store和一条branch；核对Forwarding/load-use/flush的输入与消费端，哪些示例不在任务范围则按实际检查。检查数据与select/enable未混接。
3. **时序/空间**：阶段列和边界清楚，同级功能并列而不是按普通rank排成十几列；数据/控制/反馈track有组织、没有无意穿过部件；具体容量/带宽/位宽有来源或教学假设。
4. **检查证据**：check只验证了已提交的对象；expected为空时不得称“语义100%通过”。绑定引用存在不是端口正确，更不是电气/时序网表通过；frame/group存在不是硬件层次正确。
5. **可读性**：按`preview.actualScale × text.fontSize`计算输出中的有效字高。若overview正文约6px、图细长到只剩一条线，必须调整布局/尺度或提供并实际查看每个必要区域的局部图，不能把complete=true当可读。约12–14px可作为overview正文设计起点而非通用硬上限；复杂图细节以局部图证明，最终用途决定尺度。
   局部预览不能把某个区域内对象的所有boundElements（尤其跨全图的箭头）无条件加入选区；否则被长线撑成另一张缩略全图。ids仅含目标区域及其绑定文字、**局部需要**的完整边；跨区网络用单独网络预览或真实区域裁剪。读取返回bounds/actualScale确认真的放大；若使用已有PNG裁剪，记录其原PNG/revision/区域且不冒充新注册preview。不改场景裁切用户内容，不将跨区线删掉来获得局部图。
6. **真实视觉**：看整个PNG和必要局部（所有流水级、符号端口、旁路交叉、长标签）。符号未显示/端口错位/文字糊或遗漏必须修，不能visual_issues=[]。参考图的逻辑角色、空间层级和线网组织应可辨认，不强求像素临摹。
7. **交付诚实**：保存原生源、全图＋必要局部PNG、结构/语义清单及剩余限制。review只是Agent对真实PNG作出的评审记录，不是自动专业质量证明；未满足本任务硬件验收就不得标completed。
   绘图任务默认要求可追踪的逻辑/端口/时序假设，不要求凭空提供RTL仿真；没有RTL不是单独的视觉错误，也不能声称已仿真。发现具体缺线、选择码不一致、时序矛盾才列硬件问题；“未经独立RTL验证”作为明确范围限制，避免用泛泛免责声明替代逐条检查。达到本轮实际自动修复上限时，即使ledger因漏记前轮仍返回continue，也停止并报告needs_attention；不得把账本轮数当已经执行次数。

## 实测范围与未满足项

本参考基于真实五级CPU运行修订，不把通用三节点图当能力证明。首轮Gemini/high实际建立独立部件和流水边界，但依然用了矩形MUX/ALU、漏掉部分旁路值连接，局部预览被长边撑大；其completed声明被独立评审拒绝。后续按原图ID局部修复，保留原始113个元素及48条原有箭头，增加7个原生polygon轮廓、命名端点、旁路/控制网络和有效1.6x局部PNG；最终351元素、73条记录信号、227条既有断言类型通过几何/绑定检查。

这轮**不宣传为全自动专业微架构验收完成**：整体反馈线仍拥挤，细节依赖局部图，选择码/时序仍需按具体实现审查；实际ledger最后是continue，自动修复已停止。证据证明已有API可以保留硬件对象和端口并显式报告问题，不证明仅更新Skill即可让任意模型稳定达到参考论文图水准。后续任务同样按上面的质量门执行，不复用本次completed/continue或轮数作为新图结论。

## 能力定位

这是Skill工作流与已有原生/库/路由API的组合，不宣称新增硬件自动布局器、通用电气端口DSL或RTL验证器。优先使用现有模块；如真实运行暴露某工具不能保持所需结构，应报告具体缺口并切换到现有更低层API，不拿文字卡片掩盖缺口。high可以辅助硬件规划，但不是正确表达层和验收的替代品。
