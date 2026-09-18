# HARC Project Session Context Bootstrap

> **本中文文件是规范性基准；英文 `SESSION_CONTEXT_BOOTSTRAP.md` 是同步镜像。**

## 目的

在仓库持久状态之外，为当前 AI 会话建立一份压缩的 **HARC Active Session Contract**。

该契约不是平台真正的 system prompt，而是项目级 session operating contract。

优先级：

`Platform system/developer rules > HARC Session Contract > ordinary task-level AI defaults`

## 新 Agent 必须执行

完成仓库 onboarding 后，在 Onboarding Report 末尾输出：

`HARC ACTIVE SESSION CONTRACT — LOADED`

至少包含：

- Repository state > prior chat memory；
- Chinese canonical > English mirror；
- Human-confirmed Core > AI proposals；
- Approved Framework > Working Argument Map；
- 当前 Blocking Clarifications；
- Working / Approved Framework 状态；
- Artifact 状态；
- 当前任务 CONTENT / FORM / PROTOCOL 分类；
- upstream-first propagation path；
- 当前 blocked actions。

只有回显完成后，Onboarding 才能标记 `PASS`。

## Context Refresh

在以下情况输出简短的 `HARC CONTEXT REFRESH`：

- Blocking Clarification 被解决；
- Core 发生实质变化；
- 新 Approved Framework 创建；
- 开始大规模 Artifact expansion；
- Final Artifact Review；
- Agent 怀疑早期 HARC 状态已经从活动上下文中丢失。

如果上下文丢失，重新读取 manifest 和 canonical state，不要凭记忆猜测。

## 禁止错误声明

不要声称：

- 已把本文件安装为平台真正的 system prompt；
- 已修改模型参数；
- 已永久修改平台 memory；
- 新会话会自动记住。

HARC 只要求把压缩契约显式写回当前可见会话上下文。
