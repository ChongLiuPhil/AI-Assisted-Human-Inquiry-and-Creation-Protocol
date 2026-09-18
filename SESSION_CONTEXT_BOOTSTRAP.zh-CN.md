# HARC Session Context Bootstrap
## 会话上下文启动内核

> **本中文文件是规范性基准；英文 `SESSION_CONTEXT_BOOTSTRAP.md` 是同步镜像。**

## 0. 新定位

本文件不再要求 AI Agent 把动态项目状态复制进当前对话。

它只负责在当前会话中加载一个极小的 **Repository Resolver / Context Kernel**，告诉 Agent：

- GitHub 是唯一权威项目状态源；
- 去哪里读取 manifest 与 context-interface；
- 中文 canonical / 英文 mirror 的关系；
- 如何按任务选择性读取；
- 什么时候必须重新读取最新 revision；
- 写入后如何使旧缓存失效。

动态状态不在本文件或会话契约中长期保存。

## 1. 必须加载的最小内核

新 Agent 完成 bootstrap 后，应在当前回复中确认：

```text
HARC REPOSITORY CONTEXT — ACTIVE

Source of truth:
- GitHub repository

Control files:
- HARC_MANIFEST.yaml
- HARC_CONTEXT_INTERFACE.yaml

Working Memory:
- index: docs/working-memory.zh-CN.md
- current focus: docs/working-memory/current-focus.zh-CN.md
- task plan: docs/working-memory/task-plan.zh-CN.md
- work log: docs/working-memory/work-log.zh-CN.md (human-retrospective; not default read)
- operational state only; not long-term semantic authority

Language:
- Chinese canonical
- English synchronized mirror

Context policy:
- repository-backed
- selective retrieval
- no authoritative session copy
- read latest before high-impact action
- read latest before write
- invalidate touched cache after write
- write-through to repository

Current task:
- route: CONTENT / FORM / PROTOCOL
- authoritative refs: [paths only]
```

这个区块只保存控制信息和文件引用，不复制 Blocking Clarifications、Framework、Artifact、Core 等动态内容。

## 2. 动态状态如何使用

如果任务需要知道：

- 当前 Blocking Clarifications；
- 当前 Framework Status；
- 最新 Approved Framework；
- Artifact 状态；
- Core 内容；
- 最近人类决定；

Agent 必须直接读取 GitHub 中相应 canonical 文件的最新版本。

先前聊天中曾经出现过这些内容，不构成免除重新读取的理由。

## 3. Context Refresh

`HARC CONTEXT REFRESH` 的含义是：

1. 重新读取 `HARC_MANIFEST.yaml`；
2. 重新读取 `HARC_CONTEXT_INTERFACE.yaml`；
3. fresh-fetch Working Memory Index + Current Focus + Task Plan，确认当前续接点；
4. 默认跳过 Work Log；
5. 根据当前任务解析长期记忆依赖文件；
6. fresh-fetch 这些文件；
7. 丢弃旧缓存；
8. 继续工作。

不需要把全部项目状态重新复制到聊天中。

## 4. 更新后的双层模型

现在不是：

`Repository State + Duplicated Session State`

而是：

`Repository State + Minimal Session Resolver`

其中：

- Repository = durable authoritative memory；
- Session Resolver = control plane；
- retrieved excerpts = transient non-authoritative cache。

## 5. 何时强制刷新

以下情况必须重新读取相关 GitHub 状态：

- 高影响决定前；
- Clarification resolution 前；
- Framework Approval 前；
- Final Artifact Review 前；
- 对目标文件写入前；
- 仓库发生相关更新后；
- Agent 怀疑当前缓存已经过期；
- revision token 与预期不一致。

## 6. 写入后的缓存规则

任何 canonical 文件更新后：

- 旧文件摘录立即标记为 `STALE`；
- 旧 Onboarding summary 不能继续当权威；
- 如后续推理仍依赖该文件，必须重新读取；
- 不需要同步维护一份聊天内“更新后的副本”。

## 7. 平台优先级

本内核不是平台真正的 system prompt。

优先级：

`Platform system/developer rules > HARC Repository Resolver > ordinary AI defaults`

## 8. 原则

> **会话里保留的是“如何找到记忆”，而不是“另一份记忆”。**
