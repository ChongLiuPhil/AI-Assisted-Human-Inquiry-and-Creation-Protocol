# HARC Project Session Context Bootstrap

> **本中文文件是规范性基准；英文 `SESSION_CONTEXT_BOOTSTRAP.md` 是同步镜像。**

## 目的

当前会话只加载一个最小 **Repository Resolver**，不复制项目动态状态。

```text
HARC REPOSITORY CONTEXT — ACTIVE

Source of truth:
- GitHub repository

Control:
- HARC_MANIFEST.yaml
- HARC_CONTEXT_INTERFACE.yaml

Working Memory:
- index: docs/working-memory.zh-CN.md
- current focus: docs/working-memory/current-focus.zh-CN.md
- task plan: docs/working-memory/task-plan.zh-CN.md
- work log: docs/working-memory/work-log.zh-CN.md (human-retrospective; not default read)
- operational state only; not long-term semantic authority

Policy:
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

Working Memory 需要时先从 GitHub fresh-fetch，用于确定当前阶段与续接点；Layer 1 / Layer 2 / Layer 3 / Evidence 的权威状态再按任务从最新 canonical revision 选择性读取。

## Context Refresh

`HARC CONTEXT REFRESH` 表示：

1. 重读 manifest / context interface；
2. fresh-fetch Working Memory，确认当前阶段、目标、任务、阻塞与 next actions；
3. 解析当前任务所需的长期记忆依赖；
4. fresh-fetch 这些 canonical 文件；
5. 丢弃 stale cache；
6. 继续工作。

不把全部项目状态重新复制进聊天。

## 写入规则

canonical 文件写入后，旧上下文摘录立即视为 `STALE`。如果后续仍依赖，重新读取。

## 原则

> **会话里保留的是如何找到记忆，而不是另一份记忆。**
