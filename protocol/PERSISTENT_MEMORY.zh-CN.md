# 持久研究记忆

> **本中文文件是规范性基准；英文 `PERSISTENT_MEMORY.md` 是同步镜像。**

## 原则

> **聊天是临时交互上下文；仓库才是持久共享研究记忆。**

HARC 把与项目有关的状态外部化，使项目连续性不依赖某一个模型、账号、厂商或对话窗口。

## 提升测试

不是对话中的每一句话都需要提交到仓库。

当下面问题的答案是**是**时，一条人类指令应被提升为仓库状态：

> 如果明天换成一个新的 AI Agent，而且它无法读取当前对话，那么丢失这条指令会不会改变它应该怎样继续项目？

如果会，就应持久化。

## 三层长期记忆与并行 Working Memory

HARC 的研究记忆不是单一平面。

### Long-Term Research Memory

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

- **Layer 1**：人类作者核心基础，最稳定、最具规范权威；
- **Layer 2**：当前论述框架，持久但更可修改，以 Layer 1 为上游约束；
- **Layer 3**：完整派生成果，主要从 Layer 2 展开。

### Working Memory Area

与三层长期记忆并行，但内部至少区分三种逻辑功能：

- **Current Focus** — 当前阶段、最高优先级目标、primary blocker、immediate next action；
- **Task Plan** — active tasks、next actions、TODO/backlog、blockers、pending human decisions、clarifications、sync defects；
- **Work Log** — 主要供人类以后回顾的阶段性历史纪要、里程碑和方向变化。

Working Memory 是“从哪里继续”的操作接口，不是长期实质性真值源。

其中 Current Focus + Task Plan 构成 AI 日常接管需要的 operational resume state；Work Log 主要是 human-retrospective history，默认不进入 AI onboarding 上下文。

Clarification 是 Working Memory item，不再是 Layer 1.5。

稳定结果通过 Promotion 进入长期记忆：

`Working Memory resolution -> Decision Log -> appropriate Long-Term Memory destination`

Promotion 后，Working Memory 只保留状态与指针。

## 什么内容放在哪里

| 持久状态 | 规范位置 |
|---|---|
| 研究意义、命题、区分 | `core/CONTENT_CORE.zh-CN.md` |
| 形式、版式、风格、成果类型 | `core/FORM_CORE.zh-CN.md` |
| 人类历史决定 | `core/DECISION_LOG.zh-CN.md` |
| Working Memory 索引 | `docs/working-memory.zh-CN.md` |
| 当前最重要目标 | `docs/working-memory/current-focus.zh-CN.md` |
| 动态任务/计划/待确认事项 | `docs/working-memory/task-plan.zh-CN.md` |
| 人类历史回顾日志 | `docs/working-memory/work-log.zh-CN.md`（默认不进入 AI context） |
| 旧 Clarification 路径 | `docs/clarification-register.zh-CN.md`（兼容指针，不再承载 active state） |
| 当前论证结构 | `docs/argument-map.zh-CN.md` |
| 经人类批准的论证基线 | `docs/frameworks/FW-xxx.zh-CN.md` |
| 批准/同步状态 | `docs/framework-status.zh-CN.md` |
| 证据与核验 | `evidence/` |
| 零上下文启动与仓库上下文接口 | `START_HERE.zh-CN.md`、`BOOTSTRAP_PROMPT.zh-CN.md`、`SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`、`HARC_MANIFEST.yaml`、`HARC_CONTEXT_INTERFACE.yaml`、`ONBOARDING_REPORT_TEMPLATE.zh-CN.md` |
| 协作规则 | `AGENTS.zh-CN.md`、`protocol/` |
| 扩写成果 | `paper/`、`book/`、`article/` 等 |

采用双语配置时，上述中文规范文件应有同步英文镜像。

## 不允许隐藏依赖

一个稳定项目决定不得只存在于：

- 一次临时聊天；
- 账号级 AI 记忆；
- 模型不可访问的私有推理；
- 未记录的本地格式选择；
- 某一个 Agent 的私有笔记。

如果它影响未来连续性，就应给予显式仓库表示。

## 对上下文窗口独立，不等于无限上下文

HARC 并不声称模型能在一个 prompt 中读取无限增长的仓库。

它采用**分层压缩**。

### 当前活动状态

日常接管时首先读取 Working Memory Index -> Current Focus -> Task Plan，了解“现在最重要的事是什么、接下来怎么推进”。Work Log 默认跳过。

随后只根据当前任务选择性读取：

- Layer 1：Content / Form / Protocol Core 与相关 Decision Log；
- Layer 2：Working Argument Map、Framework Status、最新 Approved Framework；
- Layer 3：相关 Artifact；
- task-relevant Evidence。

Working Memory 本身保存当前工作状态和指针，而不是复制长期层的全部内容。

### 历史状态

可以持续增长：

- 完整日志；
- 证据笔记；
- 来源清单；
- 已归档草稿；
- 较早 framework 版本；
- 分析成果。

### 扩展程序

当历史文件变大时：

1. 保留原始记录；
2. 创建按日期归档或分区；
3. 创建紧凑索引与摘要；
4. 让 active cores 聚焦当前状态；
5. 仅在相关时检索历史细节。

目标是**可恢复性**，而不是让所有历史同时进入模型上下文。

## Repository-backed memory model

HARC 现在采用：

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

这意味着：

- GitHub 保存唯一权威项目状态；
- 会话中不长期维护 Current Focus、Task Plan、Framework、Artifact、Core 等动态状态副本；
- Agent 根据当前任务选择性读取最新 canonical 文件；
- 当前上下文中的文件摘录只是临时、非权威缓存；
- 高影响判断与写入前重新读取相关最新 revision；
- canonical 文件写入后，旧缓存立即视为 `STALE`；
- 后续仍需要时重新读取，而不是同步维护一份聊天副本。

Session Context Bootstrap 只保存 Repository Resolver，也就是“如何找到记忆”，而不是“另一份记忆”。

完整接口见 `protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md` 与 `HARC_CONTEXT_INTERFACE.yaml`。

## 新 Agent 重建目标

在回答这些问题之前，新 Agent 应先完成 Onboarding Handshake，激活 `HARC REPOSITORY CONTEXT — ACTIVE`，依次读取 Working Memory Index、Current Focus 与 Task Plan 了解当前阶段、最高优先级目标和续接点，再按照 manifest/context interface 从三层长期记忆中按需读取最新权威状态。Work Log 默认跳过。

一个新的、能力合格的 Agent 应能回答：

- 人类当前想论证什么？
- 人类当前希望成果呈现成什么样？
- 哪个论证 framework 实际获得了人类批准？
- 哪些 AI 建议仍未接受？
- 哪些高影响不确定性仍在等待人类澄清？
- 哪些其他问题仍未解决？
- 哪些证据冲突重要？
- 下一步应修改什么？

如果没有旧聊天就不能回答这些问题，那么持久化架构仍不完整。
