# Obsidian Excalidraw Agent Skill

[English](README.md) | [简体中文](README.zh-CN.md)

面向 **Obsidian Excalidraw-ymjr** 的 Agent Skill：自然语言组织内容，创建原生可编辑元素，通过真实测量、几何检查、PNG 视觉评审与局部修正完成绘图。

**本仓库只分发 Skill 与参考文档。** 不包含绘图 MCP server、Engine-Agent Bridge、Obsidian 插件、字体或素材库。只安装 Skill 不等于已经有可工作的绘图后端。本 Skill 面向下述 `drawing_*` 工具契约，不保证适用于任意 Excalidraw MCP 或未经修改的上游插件。

## 使用前提

- [oh my pi（OMP）](https://github.com/can1357/oh-my-pi)，已启用 Skill 发现。
- Obsidian Desktop，以及 [Excalidraw-ymjr 安装与发布仓库](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr)。切换插件前备份 vault，按插件说明避免与原版 Excalidraw 冲突。
- 单独安装、配置并连接自己 vault 的兼容绘图 MCP/Bridge 执行器。通过运行时 discovery 核对 API 与 Feature Engines；插件公开版本存在，不代表已经提供所有绘图工具。
- 能实际查看 PNG 的 Agent。素材库、图片、自定义字体与 LaTeX 组件按绘图需求准备，本包不自带这些资源。

插件源码：[obsidian-excalidraw-plugin/tree/ymjr](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin/tree/ymjr)；组件源码：[excalidraw/tree/ymjr](https://github.com/Bowen-0x00/excalidraw/tree/ymjr)。相关脚本仓库：[obsidian-excalidraw-scripts](https://github.com/Bowen-0x00/obsidian-excalidraw-scripts)。具体 Bridge/Engine 是否已发布、已安装，必须核实，不能凭链接推断。

## 在 OMP 中全局安装

推荐通过 marketplace 安装到 **user scope**，由 OMP 管理版本。

```sh
omp plugin marketplace add Bowen-0x00/obsidian-excalidraw-agent-skill
omp plugin install --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

CLI 安装后重新启动 OMP；已有 TUI 会话可执行 `/reload-plugins`。Skill 不依赖启动目录，但不会自动把项目级 MCP 配置变成全局配置。

在其他工作目录验证：

```sh
omp read skill://obsidian-excalidraw
```

更新与卸载：

```sh
omp plugin marketplace update obsidian-excalidraw-agent
omp plugin upgrade --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
omp plugin uninstall --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

`marketplace update` 仅更新目录，`plugin upgrade` 才重新安装插件。不要同时再装手动副本，除非有意覆盖 marketplace Skill。项目里不同内容的同名 Skill 可能覆盖全局版本。

### 备选：手动安装

克隆本仓库，将 **完整** `skills/obsidian-excalidraw` 目录（包括 `references`）复制到当前 OMP 用户 agent 目录下的 `skills/`。默认 profile 的位置是 `~/.omp/agent/skills/obsidian-excalidraw/`；自定义 agent 根目录和命名 profile 使用各自目录。

在克隆目录执行 PowerShell：

```powershell
$destination = Join-Path $HOME '.omp/agent/skills'
New-Item -ItemType Directory -Force $destination | Out-Null
Copy-Item -Recurse './skills/obsidian-excalidraw' $destination
```

在克隆目录执行 POSIX shell：

```sh
mkdir -p ~/.omp/agent/skills
cp -R skills/obsidian-excalidraw ~/.omp/agent/skills/
```

先检查是否存在同名 Skill，不覆盖无关自定义内容。手动副本不由 `omp plugin upgrade` 管理。`.claude-plugin` 目录也可供 Claude Code marketplace 使用；本次运行验证范围是 OMP。

## 连接自己的绘图执行器

实际 MCP 配置保持私有。OMP 默认用户级文件是 `~/.omp/agent/mcp.json`，项目级文件是 `.omp/mcp.json`。需要在任何目录画图时，把 **自己的绘图 server 条目** 合并到用户级配置，不覆盖其他 server 和顶层设置。命名 profile 需要各自的用户配置。

使用单独安装的 Python stdio server 时，配置真实 Python 可执行文件、`server.py` 路径、执行器工作目录，以及该执行器要求的 `EXCALIDRAW_BRIDGE_URL`、`EXCALIDRAW_BRIDGE_TOKEN`、`EXCALIDRAW_BRIDGE_TIMEOUT`。Skill 的缓存目录不是执行器目录。本仓库刻意不提供带凭据的 MCP 配置，也不虚构一个默认 server 路径。

在 OMP 中用 `/mcp list` 确认绘图服务。工具可能带前缀，例如 `mcp__excalidraw_drawing_context`。调用前查看真实 schema：

| 工具 | 职责 |
| --- | --- |
| `drawing_context`、`drawing_read` | 能力发现、创建/绑定明确 vault 文件、完整摘要与按需详情 |
| `drawing_measure`、`drawing_plan`、`drawing_apply` | 原生文字测量、确定性布局、revision 保护的批量操作 |
| `drawing_check`、`drawing_preview`、`drawing_review`、`drawing_revert` | 诊断、真实 PNG 交付、持久化评审轮次、事务撤销 |
| `drawing_templates`、`drawing_primitives` | 可选图型/风格 recipe 与原生复杂图元规划 |
| `drawing_library`、`drawing_compose`、`drawing_present` | 可选真实素材库导入、分阶段组合、可编辑 frame 演示页 |

没有这些工具时，先安装配置兼容执行器。同名或近似名称的通用工具不能证明符合本契约。执行器若明确支持 CLI，可用 `EXCALIDRAW_AGENT_HOME` 指向其真实安装目录；Skill 会核实脚本与运行环境，不假定它们随包分发。

## 自然语言使用

直接描述需求即可；已启用 Skill 命令时，也可显式调用 `/skill:obsidian-excalidraw`。

> 画访问申请流程：提交申请→安全审核，通过发凭据，不通过拒绝并说明原因，两路到结束。保留完整中文与分支标签，创建独立可编辑画布，检查 PNG。

> 用 Visio 风格 UML 展示订单、客户和支付，包含字段、方法与方向正确的组合箭头。

> 使用我已安装的数字电路素材库，连接 MUX→ALU→CROSSBAR。先发现实际 item，不拿近似矩形替代。

> 使用我已安装的演示素材库，生成三页可编辑 Excalidraw 页面。保留 frame 和装饰，逐页看 PNG 并看总览，不声称输出 PPTX。

> 修改我指定的 vault 相对路径画布：更改这个节点的标签并向右移动。其他内容、样式和绑定不变，检查更新后的 PNG。

## Skill 强制执行的规则

- 明确文件、context 和当前 revision；不清空重建已有用户画布。
- 执行器支持时使用原生形状、文字、箭头、自由笔画、复杂图元与库成员，不用整图栅格化替代。
- 按真实字体测量，完整读取画布，维护双向绑定，对全文与分支方向做语义检查。
- `check → PNG → 实际看图 → review → 局部修正`。默认最多 **五次评审，初图也计入**；达标立即结束。
- 缺资源、几何 unknown、旧预览和连续两次无改善必须报告；导出成功不等于视觉通过。
- 图片、公式、ECharts、嵌入保留真实源/配置；shadow、gradient、callout、代码高亮、checkbox 依赖已发现的 Feature Engines。
- 用户指定素材库先发现、预览，再原生导入；同名 item 用准确 ID。组合可能分阶段提交，失败必须报告已执行部分，不冒称原子事务。

## 文件内容

- [SKILL.md](skills/obsidian-excalidraw/SKILL.md)：主工作流和验收规则。
- [图型与风格参考](skills/obsidian-excalidraw/references/diagram-recipes.md)：流程图、架构、UML、微架构、frame 演示页。
- [原生图元参考](skills/obsidian-excalidraw/references/native-features.md)：draw、多边形、立方体、大括号、callout、代码、checkbox、连接。
- `.claude-plugin/`：带版本的插件 manifest 和可安装 marketplace 目录。

## 隐私与能力边界

发布白名单排除令牌、私有 MCP 文件、个人机器路径、vault 画布、素材库、截图、预览、review ledger、日志、缓存与虚拟环境。执行器可以读写 vault：Bearer token 应保持私有与本地使用，仅授予必要权限。素材库内可执行 `customData` 需要显式信任本地来源；任意模型生成代码不是默认扩展入口。

Skill 是工作流程，不是渲染器，也不保证主观审美。无法实际查看图像时必须标记未评审；连接的执行器可能不能完整检查曲线和旋转几何；Excalidraw frame 页面不是 `.pptx`。本包与 Obsidian、上游 Excalidraw 没有官方关联。

## 开发与贡献

使用 Conventional Commits（`feat:`、`fix:`、`docs:`、`chore:`），更新 [CHANGELOG.md](CHANGELOG.md)，发布前审查所有公开文件。本仓库采用显式分发白名单，新增公开文件必须有意放行；不要上传用户真实产物来证明成功。安装方式参考 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 的插件/marketplace 组织方式，不分发该项目内容。

[MIT 许可证](LICENSE)。插件、组件和用户选用素材库各自保留原许可证。
