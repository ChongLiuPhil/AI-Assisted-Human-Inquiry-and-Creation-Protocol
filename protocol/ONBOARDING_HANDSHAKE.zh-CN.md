# Zero-Context Onboarding Handshake Protocol
## 零上下文接管握手协议

> **本中文文件是规范性基准；英文 `ONBOARDING_HANDSHAKE.md` 是同步镜像。**

## 1. 目的

持久仓库状态只有在新的 AI Agent 能够正确发现、读取、区分权威层级并据此行动时，才真正支持跨 Agent 连续性。

因此 HARC 不把“Agent 已经获得仓库访问权限”视为“Agent 已经接管成功”。

接管成功必须通过一个显式的 **Onboarding Handshake** 验证。

## 2. 何时触发

以下情况必须执行完整握手：

- 新 AI Agent 第一次接手项目；
- 更换模型、平台或主要 Agent；
- Agent 无法访问之前对话；
- 长时间中断后重新启动，且当前状态可能已经变化；
- 人类明确要求重新 onboarding；
- Agent 发现 manifest、Core、Framework 或 Clarification 状态存在明显不一致。

对于同一 Agent 的短期连续工作，不必每轮重复完整握手，但在重要状态变化后应重新读取相关上游文件。

## 3. 握手前禁止动作

完整握手通过前，不得：

- 创建或批准 Framework；
- 把 AI 提议升级成人类承诺；
- 未经人类确认就解决或关闭 Clarification；
- 大规模重构 Argument Map；
- 大规模改写 Artifact；
- 改变作者级 Form preference；
- 进行 release / submission 判断；
- 用英文 mirror 覆盖中文 canonical。

允许的动作仅限于：

- 读取；
- 状态重建；
- 检查路径/版本/同步；
- 报告缺陷；
- 修复显而易见的 onboarding infrastructure defect，但不得借机改动研究内容。

## 4. 必须读取的状态

根 manifest 决定具体路径。至少包括：

1. START_HERE；
2. HARC_MANIFEST；
3. HARC_CONTEXT_INTERFACE；
4. AGENTS / Session Context Bootstrap；
5. Working Memory Index；
6. Current Focus；
7. Task Plan；
8. Onboarding Handshake / Protocol governance；
9. 与当前任务相关的 Layer 1 Core / Decision Log；
10. 与当前任务相关的 Layer 2 Framework Status / Working or Approved Framework；
11. 与当前任务相关的 Layer 3 Artifact；
12. 与任务相关的 Evidence；
13. 英文 mirror parity。

## 4.5 Working Memory resume check

在大范围读取长期记忆之前，Agent SHOULD 依次读取 Working Memory Index、Current Focus 与 Task Plan，并确认：

- CURRENT_STAGE；
- CURRENT_OBJECTIVE；
- PRIMARY_BLOCKER；
- IMMEDIATE_NEXT_ACTION；
- ACTIVE_TASKS；
- NEXT_ACTIONS；
- TODO / BACKLOG；
- BLOCKERS；
- PENDING_HUMAN_DECISIONS / Clarifications。

Work Log 默认不读取；只有历史回顾、审计、变迁重建或 current/history conflict 时才按需读取。

如果 Working Memory 与长期 canonical 状态明显冲突，Agent MUST 报告 `WORKING-MEMORY-STALE` 并先修复 Working Memory，不能把其旧摘要继续当成当前状态。

## 5. 必须输出的 Onboarding Report

报告至少覆盖：

- 协议版本与 canonical language；
- 人类已确认内容；
- Form 状态；
- Current Focus 的 CURRENT_STAGE / CURRENT_OBJECTIVE / PRIMARY_BLOCKER / IMMEDIATE_NEXT_ACTION；
- Task Plan 的 ACTIVE_TASKS / NEXT_ACTIONS / TODO / BACKLOG；
- BLOCKERS / PENDING_HUMAN_DECISIONS / Clarifications；
- Working / Approved Framework；
- Artifact 状态；
- Evidence conflict；
- 双语同步状态；
- 当前允许与被阻塞的下一步；
- 当前请求的 propagation path。

推荐格式见：

`ONBOARDING_REPORT_TEMPLATE.zh-CN.md`

## 5.5 Repository Context Activation

Onboarding Report 完成后，Agent MUST 读取 `HARC_CONTEXT_INTERFACE.yaml` 与 `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`，并确认：

`HARC REPOSITORY CONTEXT — ACTIVE`

该确认只加载最小 Repository Resolver：

- GitHub source-of-truth；
- manifest / context-interface 路径；
- task route；
- latest-revision / write-through / cache-invalidation 规则。

它不得长期复制 Working Memory、Framework、Artifact、Core 等动态项目状态。

Onboarding 可判定为 `PASS` 的条件是：

- Onboarding Report 完成；
- Repository Context 已激活；
- Agent 能从最新 Working Memory 读取当前 blockers / pending decisions，并从对应长期 canonical 文件核验相关 gates；
- Agent 明确知道报告摘要与会话摘录都是非权威缓存。

## 6. PASS / PARTIAL / FAIL

### PASS

当 Agent 可以仅根据仓库准确回答核心状态问题，且没有会阻止当前工作的 onboarding defect。

### PARTIAL

Agent 能重建大部分状态，但某些任务被：

- 缺失文件；
- unresolved clarification；
- 不清楚的 adopted protocol version；
- evidence gap；
- synchronization defect

限制。

只能执行不受这些问题影响的工作。

### FAIL

如果 Agent 无法可靠判断：

- 哪些内容是人类承诺；
- 哪些是 AI 提议；
- 哪些 clarification 正在 blocking；
- 当前 Framework / Artifact 状态；
- canonical language / mirror 关系；
- 当前允许的下一步，

则 onboarding 失败。

FAIL 状态下不得继续大规模实质工作。

## 7. 人类验证

Onboarding Report 的目的不是要求人类逐字重新审核仓库，而是提供一个**压缩校验界面**。

人类可以：

- 确认 Agent 理解正确；
- 纠正误读；
- 指出缺失状态；
- 对新的高影响不确定性给出澄清；
- 决定是否允许进入下一阶段。

## 8. 机器 manifest 与人类文本的关系

`HARC_MANIFEST.yaml` 是路径、状态入口和不变量的机器可读索引。

它不替代：

- Protocol Core；
- Decision Log；
- Content/Form Core；
- Task Plan / Clarification state；
- Framework。

如果 manifest 与中文 canonical 人类可读规范冲突，以中文 canonical 为准，并修复 manifest。

## 9. 平台独立性的现实边界

HARC 无法保证任意第三方 AI 平台会自动读取 `START_HERE`、`AGENTS` 或 manifest。

因此 HARC 使用多重发现机制：

- 根目录显眼文件；
- README 导航；
- AGENTS 契约；
- 独立 Bootstrap Prompt；
- 机器 manifest；
- 人类可直接复制的启动指令；
- Onboarding Report 验证。

目标不是“平台自动服从”，而是：

> **只要 Agent 具有仓库读取能力并遵循显式项目指令，它就能够从零上下文重建同一治理状态，而且人类能够验证这一点。**

## 10. 原则

> **持久状态解决“记忆没有丢失”；Onboarding Handshake 解决“新 Agent 是否真正读懂并按正确权威关系使用这些记忆”。**
