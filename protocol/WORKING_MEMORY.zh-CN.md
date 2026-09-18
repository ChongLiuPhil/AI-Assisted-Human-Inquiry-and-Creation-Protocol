# HARC Working Memory Protocol
## 工作记忆协议

> **本中文文件是规范性基准；英文 `WORKING_MEMORY.md` 是同步镜像。**

## 1. 定义

HARC 区分两类项目记忆：

### A. Long-Term Research Memory — 长期研究记忆

用于保存项目“是什么”、已经形成什么持续性思想结构，以及哪些成果构成项目的长期状态。

长期记忆包含三个层次：

1. **Layer 1 — Human Authorial Core / 人类作者核心基础**
   - 人类作者主动表达、纠正、确认、限定和持续净化后的核心观点；
   - Content Core / Form Core / Protocol Core；
   - Decision Log 负责保存这些决定的历史。

2. **Layer 2 — Current Framework / 当前论述框架**
   - 当前论述结构、核心命题、关键概念、推论关系、章节功能；
   - 以 Layer 1 为上游约束；
   - 可以包含 Layer 1 没有逐项表述、但为展开研究所必需的结构化内容；
   - 比 Layer 1 更可修改，但仍属于持久项目状态；
   - Working Argument Map 与 Approved Framework snapshots 属于这一层的不同批准状态。

3. **Layer 3 — Derived Artifact / 派生成果**
   - 论文、书稿、报告、文章等完整成果；
   - 主要由 Layer 2 展开生成；
   - 同时必须与 Layer 1 和证据约束兼容；
   - 可以经历 DERIVED-PROVISIONAL -> FINAL-REVIEW -> FINAL-APPROVED。

### B. Working Memory — 工作记忆

Working Memory 与上述三层**并行**，不是 Layer 1.5，也不是第四个长期语义层。

它回答：

- 当前项目处于什么阶段？
- 当前工作目标是什么？
- 当前正在做什么？
- 哪些已经完成？
- 哪些还没有完成？
- 下一步是什么？
- 哪些事项正在等待人类确认？
- 哪些问题阻塞继续推进？
- 当前有哪些同步缺陷、待办与交接信息？

原则：

> **Long-term memory stores what the project is; Working Memory stores where the project currently is in its work.**

## 2. Working Memory 是功能区，不是固定文件

Working Memory 规范的是**逻辑角色**，物理实现可以是一份文件，也可以拆成多份文件。

一个合规实现至少应覆盖：

### 2.1 Working Memory Index / Resolver

稳定入口，负责告诉 Agent / 人类：

- Current Focus 在哪里；
- Task Plan 在哪里；
- Work Log 在哪里；
- 哪些文件是默认 onboarding 必读；
- 哪些只按需读取。

Index SHOULD 尽量不复制动态状态。

### 2.2 Current Focus

最短、显著度最高的工作状态。

至少应说明：

- `CURRENT_STAGE`；
- `CURRENT_OBJECTIVE`；
- 本轮/最近期最核心任务；
- `PRIMARY_BLOCKER`；
- `IMMEDIATE_NEXT_ACTION`；
- handoff 所需的最小指针。

Current Focus 应适合任何工作流突然中断后由新 Agent 在几十秒内恢复方向。

### 2.3 Task Plan

动态计划与待办状态。

至少可以包含：

- `ACTIVE_TASKS`；
- `NEXT_ACTIONS`；
- `TODO / BACKLOG`；
- `BLOCKERS`；
- `WAITING-HUMAN`；
- `PENDING_HUMAN_DECISIONS`；
- `CLARIFICATIONS`；
- `SYNC_DEFECTS`。

任务完成后应退出 active list，而不是无限积累 completed-history。

### 2.4 Work Log

主要供人类作者以后回顾的历史纪要。

它可以记录：

- 阶段性进展；
- 重要里程碑；
- 已完成任务批次；
- 方向变化；
- 思想/工作路径的变化；
- 已表达的高层理由；
- 重要 handoff / phase transition。

Work Log：

- SHOULD 定期更新；
- SHOULD 以阶段性高层总结为主；
- MUST NOT 保存 AI 隐藏 chain-of-thought、scratchpad 或不可验证的内部推理；
- MUST NOT 被视为当前规范状态；
- SHOULD NOT 默认进入 AI onboarding 的必读上下文；
- MAY 在人类要求历史回顾、审计、变迁重建或历史冲突调查时按需读取。

### 2.5 物理布局可适配

轻量项目可以：

`Index = Current Focus = Task Plan = Work Log = one file`

复杂项目可以拆成：

`Index + Current Focus + Task Plan + Work Log (+ archives)`

Manifest MUST 显式映射实际角色。

## 3. 权威边界

Working Memory 是持久化的**操作状态**，但不是长期实质性主张的最终权威来源。

如果 Working Memory 与长期 canonical 文件冲突：

- Layer 1 canonical Core / Decision Log 对人类长期承诺具有优先权；
- Approved Framework 对相应批准版本具有优先权；
- 当前 Working Framework 对当前结构状态具有优先权；
- Working Memory 必须被修正。

Working Memory 应尽量保存“状态 + 指针”，而不是长期复制已沉淀的完整规范内容。

## 4. Clarification 不再是独立 Layer

Critical Clarification 是 Working Memory 中的一种记录类型，而不是 Layer 1 与 Layer 2 之间的独立 1.5 层。

当 AI 发现高影响不确定性时：

`ambiguity -> Working Memory / Clarification item -> human resolution`

未解决 clarification：

- 不属于人类长期承诺；
- 可以是 `BLOCKING` 或 `NON-BLOCKING`；
- 必须在 Working Memory 中保持可见。

## 5. Promotion — 从工作记忆沉淀到长期记忆

当 Working Memory 中的项目获得人类确认或形成稳定结果时，应执行 **Promotion**。

### 5.1 人类核心观点 / 概念 / 范围

`Working Memory -> Decision Log -> Layer 1 Content Core -> Layer 2 Framework -> Layer 3 Artifact`

### 5.2 Form 决定

`Working Memory -> Decision Log -> Form Core -> affected Framework/Artifact if applicable`

### 5.3 Protocol 决定

`Working Memory -> Decision Log -> Protocol Core / Specification -> Agent behavior / templates`

### 5.4 纯结构性 Framework 决定

如果一项结构安排并不构成人类基础内容命题，但已成为当前研究结构：

`Working Memory -> Decision Log when human-confirmed -> Layer 2 Working Framework / Approved Framework`

不得为了“清空 Working Memory”而把 AI 临时推测写入 Layer 1。

## 6. Promotion 后如何处理原 Working Memory 条目

Promotion 完成后，该条目应：

- 从 `ACTIVE / WAITING_HUMAN / BLOCKED` 退出；
- 标记为 `RESOLVED / PROMOTED`；
- 记录 Decision ID；
- 记录目标长期文件路径；
- 从 Task Plan 的 active 区退出；
- 把完成事项的高层历史摘要写入 Work Log；
- 如需审计，记录 Decision ID 与长期目标路径。

权威答案不再由 Working Memory 条目或 Work Log 承载。

## 7. 工作进度生命周期

推荐状态：

- `TODO`
- `IN-PROGRESS`
- `WAITING-HUMAN`
- `BLOCKED`
- `RESOLVED`
- `PROMOTED`
- `SUPERSEDED`
- `ARCHIVED`

Clarification 可以继续使用：

- `BLOCKING`
- `NON-BLOCKING`

作为 severity，而不是层级名称。

## 8. 更新纪律

### Current Focus

SHOULD 在以下情况更新：

- 当前最重要目标变化；
- blocker 变化；
- 本轮对话/任务目标变化；
- phase transition；
- handoff 前。

### Task Plan

SHOULD 在以下情况更新：

- 新任务产生；
- 任务状态变化；
- 新 clarification / blocker 出现；
- 人类作出重要决定；
- 任务完成；
- Framework / Artifact gate 状态变化。

完成项应及时退出 active list。

### Work Log

SHOULD 定期更新，但不是每个微小动作都记录。

推荐写入节点：

- 一个任务批次完成；
- 一个重要协议/研究阶段完成；
- 重大人类决定导致方向变化；
- framework / artifact phase transition；
- 较长工作周期结束；
- 人类要求形成阶段纪要。

Work Log 的目标是**可回顾历史**，不是实时事件流。

## 9. Onboarding / Handoff

推荐顺序：

1. control plane：Manifest / Context Interface / START_HERE / AGENTS；
2. Working Memory Index；
3. Current Focus；
4. Task Plan；
5. 当前任务所需的三层 Long-Term Memory；
6. 必要 Evidence / Artifact。

**Work Log 默认跳过。**

只有在以下情况才读取 Work Log：

- 人类要求回顾；
- 需要理解为什么方向发生变化；
- 当前状态疑似 stale / inconsistent；
- 专门审计或 provenance reconstruction。

因此：

> **Current Focus 告诉 Agent 现在最重要的事；Task Plan 告诉 Agent 接下来怎么推进；Work Log 告诉人类我们是怎么走到这里的。**

## 10. 可扩展性

Working Memory 的 **Current Focus + Task Plan** 应保持短小、当前、可扫读。

Work Log 可以持续增长，但应：

- 以阶段条目而不是逐操作事件为单位；
- 必要时按年份/阶段分卷归档；
- 保留目录或索引；
- 不进入默认 AI context；
- 与 Decision Log / Git history 分工：Work Log 适合人类叙事性回顾，Decision Log 适合规范决定审计，Git history 适合精确版本追踪。

## 11. 原则

> **三层长期记忆描述研究对象及其成果；工作记忆描述研究过程的当前状态。**

形式化：

`Long-Term Memory = L1 Authorial Core -> L2 Current Framework -> L3 Derived Artifact`

并行：

`Working Memory Area = Index + Current Focus + Task Plan + Work Log`

其中：

`Current Focus + Task Plan = operational resume state`

`Work Log = human retrospective history`

Promotion：

`Working Memory resolution -> appropriate Long-Term Memory destination`
