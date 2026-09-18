# HARC Working Memory — Task Plan
## 动态任务计划

> **中文 canonical；英文 `task-plan.md` 为同步 mirror。**

**状态：** `ACTIVE TASK PLAN`  
**原则：** 这里只维护当前计划。完成项退出 active list，并写入 Work Log；稳定规范结果另行 Promotion。

## 1. ACTIVE TASKS

- `WM-T015` — 人类整体审阅当前方法论文章 Working Framework，并对 `MA-FW-001` 作 APPROVE / REVISE / REJECT 决定：`WAITING-HUMAN`
- `WM-T013` — CLR-009 licensing 决定（formal release 前）：`WAITING-HUMAN`
- `WM-T014` — CLR-010 目标发布渠道与渠道特定形式约束：`WAITING-HUMAN`

## 2. NEXT ACTIONS

1. 人类整体审阅 `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`，重点确认当前命题集合、依赖关系、章节功能与 HARC-D023 后更新的 T3 / T4；
2. 人类明确作出 `APPROVE / REVISE / REJECT` 决定；
3. 只有在明确 `APPROVE` 后，Agent 才创建 `MA-FW-001` Approved Framework Snapshot，并更新 Framework Status；
4. Framework Approval 后再执行当前正文的大规模结构性同步/重写，并继续保留 Final Artifact Approval；
5. 正式 release 前解决 `CLR-009`；
6. 正式投稿/发布形式冻结前解决 `CLR-010`。

## 3. BLOCKERS / GATES

### Framework Approval

`CLR-001 / CLR-002 / CLR-005` 已经通过 HARC-D023 解决并 Promotion。

当前 **没有 blocking clarification** 阻止整体 Framework Approval 审阅。

但 `MA-FW-001` 仍未创建，因为还缺少人类对整个 Working Framework 的明确整体批准。当前 gate：

`WAITING-HUMAN: overall Framework Approval decision`

### Formal release

- `CLR-009` — license 未决定。

### Final submission / publication form

- `CLR-010` — 目标发布渠道及渠道特定引用、字数、版式、AI disclosure 等约束未决定。

## 4. PENDING HUMAN DECISIONS / CLARIFICATIONS

### Framework Approval overall decision

**状态：** `WAITING-HUMAN`  
**类型：** human approval decision，不是新的 Clarification。

需要对当前 Working Framework 整体作：

- `APPROVE`
- `REVISE`
- `REJECT`

局部措辞的接受不自动等于整体批准。

### CLR-003 — `semantic version control`

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

**AI-PROPOSED：** 作为明确限定的 HARC working term / coinage，而非既有成熟标准。

### CLR-004 — `generation–verification asymmetry`

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

**AI-PROPOSED：** 仅作为 heuristic label，不表述成已证实的经验定律。

### CLR-006 — extended / distributed cognition 的理论关系

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

候选：中心理论基础 / 次级比较 / 最少背景。  
**AI-PROPOSED：** 次级概念比较。

**HARC-D023 约束：** 无论采用何种比较强度，都不得把该比较写成 AI 本身具有认知性的前提。

### CLR-007 — 经验验证计划的地位

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

候选：核心贡献 / Future Research / 省略。  
**AI-PROPOSED：** Future Research Agenda。

### CLR-008 — 方法论文章主要学科定位

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

候选：philosophy of technology / epistemology；research methodology；scholarly communication / research integrity；interdisciplinary AI governance。

**AI-PROPOSED：** interdisciplinary research methodology，以 philosophy of technology / epistemology 为理论核心。

### CLR-009 — HARC 开放许可

**状态：** `WAITING-HUMAN`  
**严重度：** formal release = `BLOCKING`；methodology framework = `NON-BLOCKING`

候选：documentation CC BY 4.0 + code MIT / Apache-2.0 / MIT / 其他。

关联：`LICENSE-DECISION.zh-CN.md`

### CLR-010 — 目标发布渠道与渠道特定形式约束

**状态：** `WAITING-HUMAN`  
**严重度：** Framework Approval = `NON-BLOCKING`；Final submission/publication form = `BLOCKING`

问题：方法论文章最终面向什么发布渠道，以及由该渠道带来的具体形式约束是什么？

待确认内容包括：

- 目标期刊 / 会议 / 预印本 / 其他发布渠道；
- 引用与参考文献样式；
- 字数 / 篇幅限制；
- 字体、版式、页面约束（如适用）；
- 渠道特定 AI disclosure / authorship / research-integrity 要求；
- 渠道是否只接受一种语言，以及对项目内部双语版本的输出要求。

与 `CLR-008` 的区别：

- `CLR-008` 处理文章的**学科定位 / intellectual positioning**；
- `CLR-010` 处理具体的**发布渠道 / external form constraints**。

**AI-PROPOSED：** 在 Working Framework 稳定后再选择具体渠道；在渠道确定前，不把当前 citation / layout defaults 升级为人类 Form commitment。

**Promotion 目标：** Article Form Core -> external constraints / final rendering / submission checklist。

## 5. RESOLVED / PROMOTED POINTERS

- `CLR-001` — `RESOLVED / PROMOTED` via `HARC-D023`：不用“AI 认知劳动 / 认知任务”作为中心表述；采用人类目的/方向、AI 工具工作分担与人类责任模型。
- `CLR-002` — `RESOLVED / PROMOTED` via `HARC-D023`：采用人类第三种 Framework Responsibility Thesis；Layer 2 Framework 是核心思想责任的主要结构性承载点，人类必须理解、审核并确认其中全部实质内容。
- `CLR-005` — `RESOLVED / PROMOTED` via `HARC-D023`：`responsibility concentration` 不作为当前中心术语。

## 6. BACKLOG

- 自动化 onboarding / conformance check；
- repository-backed context 的上下文成本与 stale-state 研究；
- Working Memory 更新粒度、压缩策略与 handoff 效率研究；
- 跨 Agent / 跨平台接管测试。

## 7. SYNC DEFECTS

`NONE RECORDED`

## 8. COMPLETION RULE

任务完成时：

1. 从本文件 active list 删除/退出；
2. 在 Work Log 增加高层完成摘要；
3. 如形成长期规范结果，执行 Promotion；
4. 必要时更新 Current Focus；
5. 不在本文件积累长期 completed-history。
