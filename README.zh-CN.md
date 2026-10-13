# Obsidian Excalidraw Agent

[English](README.md) · [简体中文](README.zh-CN.md)

让 Agent 根据自然语言在 Obsidian Excalidraw-ymjr 中绘制可编辑图。仓库包含绘图 Skill、MCP 服务，以及连接 Obsidian 的 Bridge 和 Feature Engine 脚本。

## 功能

- 流程图、系统架构图、UML、泳道图和可编辑演示页面。
- 原生形状、文字、箭头，以及运行环境支持的图片、公式、图表和用户素材库。
- 文字尺寸测量、布局规划、几何检查、PNG 预览和局部修改。
- 远端无 GUI 的 OMP 控制本机 Obsidian 绘图，并收到 PNG 进行检查。

## 环境要求

本机绘图需要：

- Obsidian Desktop；目标 vault 中已安装并启用 [Excalidraw-ymjr](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr)。
- 支持 Agent Plugins 的 [OMP](https://github.com/can1357/oh-my-pi)、PATH 中可用的 [uv](https://docs.astral.sh/uv/getting-started/installation/)，以及 Python 3.11+。
- 支持图像输入的模型，以便实际查看 PNG。

[Advanced URI](https://github.com/Vinzent03/obsidian-advanced-uri) 可选。安装后可自动执行 Bridge 启动命令；没有它时，在 Obsidian 中手动运行返回的命令即可。自定义字体和素材库按需准备。LaTeX 需要已启用、版本兼容的 Excalidraw Extras MathJax 组件。

## 快速开始

### 1. 安装 OMP 插件包

```sh
omp plugin marketplace add Bowen-0x00/obsidian-excalidraw-agent-skill
omp plugin install --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

重启 OMP，或在已有会话执行 `/reload-plugins`。包内 MCP 通过 uv 启动，首次使用会下载依赖。用 `/mcp list` 检查绘图服务，名称可能带插件前缀。

### 2. 连接 vault

保持 Obsidian 打开，在 OMP 中输入：

> 使用 skill://obsidian-excalidraw，连接我选择的 Obsidian vault，并检查绘图服务。

Agent 通过 `drawing_setup` 列出 vault，并连接选定目标。脚本安装在插件已配置脚本目录的 `Agent-Drawing` 子目录，不覆盖无关文件，也不修改插件启用权限。

无法自动启动时，打开一个画布，在 Obsidian 命令面板运行 `Agent-Drawing/mcp/Start-Agent-Drawing`。新脚本尚未出现在列表中时，重载一次 Obsidian。

### 3. 描述要画的内容

> 画申请审批流程：提交申请→审核，通过则发放凭据，未通过则说明拒绝原因，两路到结束。保留完整中文，检查 PNG。

> 画订单系统架构，分为前端、业务服务、存储三个区域，保留跨区域连接。

> 修改我指定画布中的一个节点标签，其他内容和样式不变。

原生可编辑图保存在已连接的 vault。PNG 和评审记录保存在执行器的数据目录。Agent 查看图片后修复具体问题，不会为一次局部修改重建整图。默认最多五次评审，达标提前结束；仍有问题时明确报告。

## 远端绘图

本机运行 Obsidian 和 Bridge。远端运行 OMP、Skill 和 Python MCP 客户端，不需要 Obsidian、桌面或 X11。

在本机的仓库克隆目录或已安装包目录执行以下命令。先选择与本机 MCP 相同的连接状态；使用 marketplace 安装时，可将 `EXCALIDRAW_AGENT_STATE_DIR` 设置为 `drawing_setup(status)` 返回的目录。

```sh
uv run --frozen python launcher.py remote-deploy --host Redhat --remote-port 28125
uv run --frozen python launcher.py remote-tunnel --host Redhat --remote-port 28125
```

`Redhat` 是本机已有 SSH 别名。部署要求远端有 Python 3.11+、pip 和 OMP，会在远端用户目录安装 Skill 和 `excalidraw-local` MCP，保留已有 OMP 配置。第二条命令持续保持反向隧道，将远端 loopback 端口 28125 转发到本机 Bridge。使用期间保持它和 Obsidian 运行。

已经登录远端时，直接运行 `omp`；已有会话执行 `/reload-plugins`，然后描述绘图需求即可。无需用特定 SSH 命令登录。

画布和源素材仍在本机 vault。PNG 字节通过隧道返回，保存到远端，并以 MCP 图片消息交给模型；返回的 PNG 路径可以由远端 Agent 直接读取。`drawing_setup(status)` 返回 `mode=remote`。选择 vault、启动 Obsidian 要在本机完成，不能在远端调用本机部署操作。

远端连接凭据保存在权限 0600 的私有文件中，只应授权可信用户。隧道使用独立 SSH 配置、密钥登录和 known-host 验证，不使用别名中其他端口转发，也不启用 X11。断线后重启隧道。本机切换 vault 后重新 `remote-deploy`，并重启远端 MCP。通过 SSH 脚本执行 `omp -p` 时使用 `ssh -n` 关闭 stdin；交互使用正常终端即可。

## 用户自己的素材库

语义信息放在用户维护的文件里：item 的 `description` 与原有 `name` 同级；每个库目录的 `library-index.md` 汇总库用途、代表item ID和用户偏好。Agent先读摘要筛选候选，再核对真实item、查看预览，最后原生导入。

`drawing_library(list)` 返回发现的摘要路径，`catalog` 读取摘要，`query/get` 返回并检索item描述。它们只帮助选素材，不改变渲染，也不授权执行库内代码。当前原生UI搜索仍只读name，description是JSON扩展元数据，不是新增的UI编辑框。

复制 [素材库维护prompt](skills/obsidian-excalidraw/prompts/maintain-libraries.zh-CN.md)，再追加自己的库目录和补充描述，即可让Agent清点、预览、保留人工描述、增补字段并生成可继续编辑的摘要。本机维护工具只按准确ID修改description，检查源hash并保存原字节备份，不改图元或资源。命令及兼容边界见 [库摘要参考](skills/obsidian-excalidraw/references/library-catalog.md)。文件维护应在能访问库的宿主执行；远端OMP可以通过MCP读宿主摘要，但不能把本机路径当远端文件。

## 插件原生 CLI

较新的 ymjr 插件还提供原生 CLI，适合不经过本包 Bridge 的简单创建、读取、编辑和导出。终端入口要求 **Obsidian 1.12.2+、CLI 已启用**，且已安装插件版本注册了这些命令。

```sh
obsidian vault="目标vault" obsidian-excalidraw-plugin-ymjr:status
obsidian vault="目标vault" obsidian-excalidraw-plugin-ymjr:help
obsidian vault="目标vault" obsidian-excalidraw-plugin-ymjr:schema action=create
```

命令前缀以真实插件 ID 为准。Windows 捕获输出使用已安装的 `Obsidian.com` console launcher。可信 EA 脚本中可以通过 `ea.executeCLI(request)` 调用相同 JSON 协议，不依赖终端注册条件；先确认安装版本实际提供该方法。

Skill 已区分原生 CLI 与本包的 `launcher.py cli`，会检查保存回执、请求 ID、分页读取和真实导出。原生 CLI **不提供本包的自动布局、几何诊断、review ledger 或远端图片传输**。完整绘图和已连接的远端工作流继续使用 `drawing_*`。接口差异、保存结果、限制及错误恢复见 [原生 CLI 参考](skills/obsidian-excalidraw/references/native-cli.md)。

## 配置与文件位置

| 内容 | 位置 |
| --- | --- |
| Marketplace 连接配置和产物 | OMP 持久化插件数据目录中的 `${PLUGIN_DATA}/state` |
| 直接 CLI 的连接配置和产物 | 平台用户数据目录，`launcher.py status` 返回实际路径 |
| 远端运行时、连接配置和产物 | `~/.local/share/obsidian-excalidraw-agent-remote/` |
| 远端 Skill / MCP 注册 | 用户 agent 目录，通常为 `~/.omp/agent/skills/` 和 `~/.omp/agent/mcp.json` |
| Obsidian 端脚本 | `<已配置脚本目录>/Agent-Drawing/` |

`EXCALIDRAW_AGENT_STATE_DIR` 选择状态目录；`EXCALIDRAW_AGENT_CONFIG` 选择私有连接文件。setup 工具不返回令牌。vault 内的 `Agent-Bridge-Connection.json` 只保存外部配置路径，公开 vault 仓库应忽略该文件，避免泄露机器相关路径。

直接使用 CLI 时，克隆仓库后运行 `uv run --frozen python launcher.py --help`；完整绘图命令见 `launcher.py cli -- --help`。其他 MCP 客户端可通过 uv 启动 `launcher.py serve`。执行代码在 `runtime/`，Obsidian 脚本在 `bridge/`，Agent 绘图规范在 `skills/`。

## 更新与卸载

```sh
omp plugin marketplace update obsidian-excalidraw-agent
omp plugin upgrade --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent
```

更新后重启 OMP。重新连接同一 vault 更新受管脚本；Engine 变更后重启 Obsidian。远端受管安装通过重新执行 `remote-deploy` 更新。用户修改过的脚本或 Skill 不会静默覆盖。

卸载命令为 `omp plugin uninstall --scope user obsidian-excalidraw-agent-skill@obsidian-excalidraw-agent`。卸载不会删除图、数据目录或已部署 vault 脚本；不再使用时再单独清理。从旧手动执行器迁移时，只移除它的过时 MCP 条目，避免覆盖包内服务，保留其他配置。

## 常见问题与限制

| 现象 | 检查项 |
| --- | --- |
| 找不到 Skill 或绘图工具 | 重启 OMP 或 `/reload-plugins`，检查 `/mcp list` 和 uv 是否在 PATH |
| 服务未连接 | 查看 `drawing_setup(status)`，启动本机 Bridge；远端使用还需保持隧道运行 |
| `ready=false`，但 `connected=true` | 服务可能没有活动画布，显式创建或绑定目标即可 |
| 文件被修改，更新被拒绝 | 先保留或处理该自定义修改，再部署 |
| 找不到原生命令 | 检查 CLI 设置、Obsidian API版本、console launcher、插件版本和目标 vault |

Bridge 是有 vault 读写权限的受信任本地代码，不是沙箱；仅监听 loopback，并对请求鉴权。素材库里的可执行 `customData` 需要显式信任。曲线或旋转几何可能不能完整检查，Excalidraw 演示页面不等于 PPTX。没有图像能力或资源缺失时，不能把导出成功计为评审通过。

首次依赖安装使用 PyPI，远端部署使用官方索引。SSH 部署会把包代码和连接凭据发送到选定主机。绘图使用本机插件和资源，不另接第三方渲染服务；Agent 使用的模型服务会接收它处理的提示和图片。

## 开发与许可证

```sh
uv run --frozen python -m unittest discover -s runtime/tests -v
```

[Skill](skills/obsidian-excalidraw/SKILL.md) · [图型参考](skills/obsidian-excalidraw/references/diagram-recipes.md) · [原生图元](skills/obsidian-excalidraw/references/native-features.md) · [更新记录](CHANGELOG.md)

相关项目：[ymjr插件/发布](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin-ymjr)、[插件源码](https://github.com/Bowen-0x00/obsidian-excalidraw-plugin/tree/ymjr)、[组件源码](https://github.com/Bowen-0x00/excalidraw/tree/ymjr)、[原脚本](https://github.com/Bowen-0x00/obsidian-excalidraw-scripts)。

原创包代码使用 [MIT 许可证](LICENSE)。内嵌库保留 [第三方声明](THIRD_PARTY_NOTICES.md) 中各自许可证。本项目与 Obsidian、上游 Excalidraw 无官方关联。
