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

## 2. Working Memory 的典型内容

Working Memory SHOULD 包括：

- `CURRENT_STAGE` — 当前阶段；
- `CURRENT_OBJECTIVE` — 当前主要目标；
- `ACTIVE_TASKS` — 正在执行的任务；
- `NEXT_ACTIONS` — 下一步；
- `RECENTLY_COMPLETED` — 最近完成；
- `BACKLOG / TODO` — 后续任务；
- `BLOCKERS` — 阻塞项；
- `PENDING_HUMAN_DECISIONS` — 等待人类确认；
- `CLARIFICATIONS` — 高影响不确定性；
- `SYNC_DEFECTS` — 已知同步缺陷；
- `HANDOFF_NOTE` — 给下一位人类参与者或 AI Agent 的续接说明。

Working Memory 可以包含临时分析，但必须明确为非权威、可淘汰状态。

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
- 从当前 Active 工作区移至简短的 Recently Resolved / Archive 区。

权威答案不再由 Working Memory 条目承载。

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

## 8. 更新时机

AI Agent SHOULD 在以下节点更新 Working Memory：

- 一个明确工作目标开始时；
- 一个任务完成时；
- 人类给出重要决定后；
- 新 clarification / blocker 出现时；
- clarification 被解决并 promotion 后；
- Framework 状态改变时；
- Artifact 阶段改变时；
- 每个较大的工作循环结束时；
- Agent handoff 前；
- 新 Agent onboarding 时发现 Working Memory 已过期时。

## 9. Onboarding / Handoff

新的 AI Agent 或人类协作者接入时，建议顺序：

1. 读取 control plane：`HARC_MANIFEST.yaml`、`HARC_CONTEXT_INTERFACE.yaml`、START_HERE / AGENTS；
2. 读取 `docs/working-memory.zh-CN.md`；
3. 从 Working Memory 得知当前阶段、目标、任务、阻塞与待确认事项；
4. 根据当前任务，从三层长期记忆中 selective retrieval 最新 canonical state；
5. 不把 Working Memory 当成长期语义真值源。

这样 Working Memory 是**续接索引**，长期记忆是**权威研究状态**。

## 10. 可扩展性

Working Memory 应保持短小、当前、可扫读。

当其历史增长时：

- Active 区只保留当前工作；
- resolved/promoted 项目压缩为索引；
- 详细历史移入 archive；
- Decision Log 和 Git 历史承担长期审计。

## 11. 原则

> **三层长期记忆描述研究对象及其成果；工作记忆描述研究过程的当前状态。**

形式化：

`Long-Term Memory = L1 Authorial Core -> L2 Current Framework -> L3 Derived Artifact`

并行：

`Working Memory <-> current goals / tasks / clarifications / blockers / handoff`

Promotion：

`Working Memory resolution -> appropriate Long-Term Memory destination`
