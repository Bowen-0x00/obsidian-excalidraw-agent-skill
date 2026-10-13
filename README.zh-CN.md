# Obsidian Excalidraw Agent

[English](README.md) | [简体中文](README.zh-CN.md)

**完整的 Obsidian Excalidraw-ymjr Agent 绘图包**：MCP server、确定性布局和诊断、Engine-Agent Bridge、16 个 Feature Engines、首次 vault 连接，以及强制真实 PNG 评审的 Skill。

0.5.0 替代此前的 Skill-only 发布包。现在无需另找绘图后端、手工拼 MCP 路径或把 Bearer token 贴进提示：安装一次，连接目标 vault，之后直接描述要画什么。

## 宿主前提

- [oh my pi / OMP](https://github.com/can1357/oh-my-pi)，支持 Agent Plugins（实际验证版本：18.10.1）。
- PATH 中有 [uv](https://docs.astral.sh/uv/getting-started/installation/)。`uv run` 自动准备锁定的 Python 依赖；要求 Python 3.11+，首次下载依赖需要网络。
- Obsidian Desktop，目标 vault 中 [Excalidraw-ymjr 已安装并启用](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr)。切换插件前备份 vault；安装器不会擅自启用插件、修改信任权限或替换原版 Excalidraw。
- 能实际查看 PNG 的 Agent。

[Advanced URI](https://github.com/Vinzent03/obsidian-advanced-uri) 可选：启用时自动启动 Bridge；否则安装器返回在 Obsidian 中运行一次的准确命令。LaTeX 需要在 Obsidian 启用兼容的 Excalidraw Extras MathJax 组件。自定义字体和用户素材库按需准备，普通图不依赖它们。

## 全局安装

```sh
omp plugin marketplace add Bowen-0x00/obsidian-excalidraw-agent-skill
omp plugin install --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

重启 OMP，或在已有 TUI 执行 `/reload-plugins`。包内提供无凭据的 `mcp.json`：OMP 解析安装目录和持久化数据目录，通过 uv 启动 `launcher.py serve`。共暴露 **15 个工具**，包含首次连接工具 `drawing_setup`。

用 `/mcp list` 确认 `excalidraw`，然后直接说：

> 使用 Obsidian Excalidraw Skill，连接我选择的 vault。画申请流程：提交申请→审核；通过→发放凭据，未通过→说明拒绝原因；两路到结束。保持原生可编辑，实际检查 PNG。

Agent 先调用 `drawing_setup(action="status")` 发现本机 vault，再通过 `drawing_setup(action="connect", vault_path=选定路径)` 连接。目标有歧义时才询问。连接过程：

1. 核对目标 vault 中已安装、已启用的 ymjr 插件和实际脚本目录。
2. 部署至 `<脚本目录>/Agent-Drawing/`，保留其他脚本，拒绝覆盖已被用户修改的受管文件。
3. 生成本机随机令牌，保存到 vault/安装包之外的私有目录。
4. 通过 Advanced URI 启动 `Agent-Drawing/mcp/Start-Agent-Drawing`；没有该插件则返回手动命令。
5. 确认鉴权后的 Bridge 状态。Obsidian 尚未索引新脚本时，重载一次，再调用 `drawing_setup(action="start")`。

Obsidian 重启后，用 `drawing_setup(action="start")` 启动已保存的连接。已有其他 Bridge 占用端口时，在连接参数 `port` 中选择空闲端口；不能将连接失败冒称成功。替换 Bridge 会让旧画布 token 失效，需要重新 bind。

**从 0.4.1 升级：** 如果用户级/项目级私有 MCP 文件中的旧 `excalidraw` 条目仍指向单独的本地执行器，仅移除这个旧条目，保留其他 server 和设置。原生配置优先级高于包内配置，不移除就会继续运行旧后端。此前“只发布 Skill、另配执行器”的说明已废弃。

## 更新与卸载

```sh
omp plugin marketplace update obsidian-excalidraw-agent
omp plugin upgrade --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

重启 OMP，再连接同一 vault，部署变更的受管脚本。Engine 升级后重启 Obsidian，让已加载 Hook 使用新版本。连接和产物保存在版本缓存之外，不随包更新消失。

```sh
omp plugin uninstall --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

卸载仅移除 OMP 包注册，不删除图或 vault 脚本。需要删除已部署内容时，关闭 Obsidian 后只删除自己安装的 `Agent-Drawing` 子目录；保留其他脚本和 vault 文件。

## 备选：克隆后直接使用 CLI

```sh
git clone https://github.com/Bowen-0x00/obsidian-excalidraw-agent-skill.git
cd obsidian-excalidraw-agent-skill
uv run --frozen python launcher.py status
uv run --frozen python launcher.py connect --vault "/path/to/your/vault"
uv run --frozen python launcher.py doctor
uv run --frozen python launcher.py smoke
```

把示例路径替换成实际 vault 路径。`connect --no-open` 仅部署、不打开 URI；`--vault-name` 适配 Obsidian 别名；`--obsidian-config-dir` 支持非默认配置目录；`--port` 指定本地端口。`smoke` 创建真实可编辑流程图和 PNG，但明确返回 `visual_reviewed=false`：脚本不能冒充模型看图。

完整绘图 CLI：`launcher.py cli -- --help`。其他 MCP 客户端可运行 `uv run --frozen --project <克隆目录> python <克隆目录>/launcher.py serve`，MCP 配置无需凭据。包内标准 `mcp.json` 使用 OMP/Agent Plugins 的占位符语义，不假设所有客户端都支持。

直接 CLI 默认使用平台用户数据目录；marketplace 安装使用 OMP 持久化的 `${PLUGIN_DATA}/state`。需要有意共享时设置 `EXCALIDRAW_AGENT_STATE_DIR`；或通过 `EXCALIDRAW_AGENT_CONFIG` 选择已有私有连接文件。`drawing_setup(status)` 返回实际路径，不返回令牌。

## 无图形界面的远端 Agent 控制本机绘图

0.6.0 增加 SSH 反向隧道部署。先在有桌面的本机连接并启动 Obsidian Bridge，再在本机执行以下命令。使用 marketplace 连接时，先将 `EXCALIDRAW_AGENT_STATE_DIR` 设置为 `drawing_setup(status)` 返回的实际状态目录。

```sh
uv run --frozen python launcher.py remote-deploy --host Redhat --remote-port 28125
uv run --frozen python launcher.py remote-tunnel --host Redhat --remote-port 28125
```

`Redhat` 是本机已有 SSH 别名。第二条命令持续运行：把远端 `127.0.0.1:28125` 转发到本机已配置的 Bridge loopback 端口。独立私有 SSH 配置保留真实目标、密钥、代理，排除原别名的其他端口转发和 X11，不将 Bridge 开放到公网。要求密钥免密登录且 known-host 身份已验证；后台隧道不能回答密码/主机确认提示。

部署会在远端用户目录安装 Python 3.11+ venv、绘图客户端和完整 Skill。远端只需 Python/pip、SSH、OMP，不需要 uv、Obsidian 或显示器。依赖从官方 PyPI 安装，不修改全局 pip 设置。保留既有 OMP 模型、鉴权、设置与其他 MCP server；已修改的受管运行时/Skill 文件不会静默覆盖。

远端重启 OMP，或执行 `/reload-plugins` 同时发现新Skill与MCP；单独 `/mcp reload` 仅重连MCP，不会发现刚复制的新Skill。然后要求使用 `skill://obsidian-excalidraw` 和 `excalidraw-local`。`drawing_setup(status)` 返回 `mode=remote`、`rendering_location=host` 以及首连配置的宿主 vault 身份。远端 `connect`/`start` 被明确禁止：开启 GUI/Bridge、切换 vault 都在本机完成。

从本机进入远端交互 OMP：`ssh -t -o ClearAllForwardings=yes -o ForwardX11=no Redhat omp`。脚本方式通过 SSH 执行 `omp -p` 时用 `ssh -n`，使OMP得到stdin EOF，不会一直等待管道输入。这些单次命令的转发选项不会停止单独运行的绘图隧道。

原生 `.excalidraw.md`、图片/素材源路径属于本机 vault。PNG 字节通过隧道返回，保存到远端状态目录，并作为 MCP `ImageContent` 交给远端模型。所以远端 Agent 无需 X11 就能实际看 PNG，也能在远端读取返回的 `out_path`。预览凭据/ledger 保存在远端持久化目录，普通 PNG 交付无需再 SCP。

远端位置：

- 运行时/venv：`~/.local/share/obsidian-excalidraw-agent-remote/`。
- 私有连接与产物：该目录的 `state/`，连接文件权限 0600。
- Skill：`~/.omp/agent/skills/obsidian-excalidraw/`。
- MCP：合并到 `~/.omp/agent/mcp.json` 的 `excalidraw-local` 条目，支持 `PI_CODING_AGENT_DIR`。

此方案与 SSH-stdio 不同：为让远端 Python 客户端调用宿主 Bridge，令牌经加密 SSH stdin 安全配置到远端受信任用户的私有文件，不出现在命令参数或公开文件。该远端用户有宿主 vault 绘图权限，只给可信账户使用。关闭隧道或宿主 Bridge 会中断远端绘图。本机切换 vault 后重新 `remote-deploy`，远端重启 MCP 加载变更的连接。


## 绘图工具

| 工具 | 职责 |
| --- | --- |
| `drawing_setup` | 发现 vault、部署脚本、建立私有连接、启动/检查 Bridge |
| `drawing_context`、`drawing_read` | 能力发现、明确文件绑定、完整摘要和按需详情 |
| `drawing_measure`、`drawing_plan`、`drawing_apply` | 原生文字测量、确定性布局、revision 保护的批量操作 |
| `drawing_check`、`drawing_preview`、`drawing_review`、`drawing_revert` | 几何/语义检查、真实 PNG、持久化评审、事务撤销 |
| `drawing_templates`、`drawing_primitives` | 图型与风格 recipe；draw、多边形、立方体、大括号、callout、代码、checkbox、连接 |
| `drawing_library`、`drawing_compose`、`drawing_present` | 真实素材库发现/导入、分阶段组合、原生可编辑 frame 页面 |

工具可能带 `mcp__excalidraw_` 前缀，调用前读取真实 schema。素材库导入保留源→新 ID、组、frame、绑定和资源；组合报告分阶段提交，不虚构整笔原子事务。

## 自然语言示例

> 用 Visio 风格 UML 展示订单、客户和支付，包含字段、方法以及方向正确的组合箭头。

> 使用我已安装的数字电路素材库连接 MUX→ALU→CROSSBAR，先发现并预览准确 item，不拿近似矩形替代。

> 从我已安装的演示库创建三页可编辑 Excalidraw 页面。保留 frame 和装饰，逐页及总览实际看 PNG，不声称输出 PPTX。

> 修改我指定的 vault 相对路径画布：更改节点标签并向右移动，其他内容、样式、绑定不变，检查更新后的 PNG。

普通图默认采用原生 Helvetica 与系统中文 fallback，避免依赖个人文楷字体文件。用户明确指定字体时保留其选择，并通过 runtime discovery 核实。

## PNG 反馈与完成条件

强制 `check → PNG → 实际看图 → review → 局部修正`。默认最多 **五次评审，初图计入**，达标提前结束；连续两次无改善则停止并列剩余问题。完整摘要、全文/分支标签、双向绑定、当前 revision 的完整 PNG 和资源就绪由程序检查；视觉判断仍要求 Agent 实际看图。

缺图像能力只能标未评审；不能完整检查的曲线/旋转几何明确报告；Excalidraw frame 页面不是 `.pptx`。局部修改不清空重建用户画布。

## 包内容

- [Skill](skills/obsidian-excalidraw/SKILL.md)、[图型/风格参考](skills/obsidian-excalidraw/references/diagram-recipes.md)、[原生图元参考](skills/obsidian-excalidraw/references/native-features.md)。
- `runtime/`：完整绘图、布局、诊断、资源和评审执行模块。
- `launcher.py`、`setup_connection.py`、`remote_control.py`：MCP 入口、首次连接、无GUI远端部署与SSH隧道。
- [Bridge bundle](bridge/bundle.json)：Bridge、bootstrap、16 个 Feature Engines，包括内嵌的离线图表/高亮/导出库。
- `plugin.json`、`mcp.json`、`.claude-plugin/`：带版本的安装信息；`pyproject.toml`/`uv.lock`：锁定执行依赖。
- [第三方声明](THIRD_PARTY_NOTICES.md)：原脚本和内嵌库许可证。

## 隐私与信任边界

`connection.json`、令牌、用户绝对路径、画布、安装素材库、PNG、ledger、缓存、虚拟环境不进入发布内容。vault 内描述文件只保存外部私有连接文件的路径，**不保存令牌，但路径是机器相关信息：公开 vault 仓库应忽略 `Agent-Bridge-Connection.json`。** POSIX 私有文件以 0600 创建；Windows 使用当前用户数据目录权限。

Bridge 仅监听 loopback，每次请求鉴权，拒绝浏览器 Origin，保留 revision 保护。它是有 vault 读写权限的受信任本地代码，不是沙箱。用户素材中的可执行 `customData` 需要显式信任来源。环境变量凭据覆盖只供有意配置的高级场景，正常连接不需要。

## 开发

```sh
uv run --frozen python -m unittest discover -s runtime/tests -v
```

使用 Conventional Commits，更新 [CHANGELOG.md](CHANGELOG.md)，不上传用户真实产物。分发白名单只放行预期运行时代码/Bridge 源文件。安装组织参考 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)，不分发其内容。

插件链接：[安装/发布仓库](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr)、[插件源码](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin/tree/ymjr)、[组件源码](https://github.com/Bowen-0x00/excalidraw/tree/ymjr)、[原脚本](https://github.com/Bowen-0x00/obsidian-excalidraw-scripts)。

原创包代码使用 [MIT 许可证](LICENSE)，内嵌组件保留 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 中各自许可证。本项目与 Obsidian、上游 Excalidraw 无官方关联。
