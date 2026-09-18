# HARC Working Memory — Task Plan
## 动态任务计划

> **中文 canonical；英文 `task-plan.md` 为同步 mirror。**

**状态：** `ACTIVE TASK PLAN`  
**原则：** 这里只维护当前计划。完成项退出 active list，并写入 Work Log；稳定规范结果另行 Promotion。

## 1. ACTIVE TASKS

- `WM-T008` — 人类决定 CLR-001：`WAITING-HUMAN`
- `WM-T009` — 人类决定 CLR-002：`WAITING-HUMAN`
- `WM-T010` — 人类决定 CLR-005：`WAITING-HUMAN`
- `WM-T011` — 将上述决定 Promotion 并传播到 Layer 1 / Layer 2 / Layer 3：`TODO`
- `WM-T012` — 重新执行 Framework Approval readiness review：`TODO`
- `WM-T013` — CLR-009 licensing 决定（formal release 前）：`WAITING-HUMAN`

## 2. NEXT ACTIONS

1. 人类确认 `CLR-001 / CLR-002 / CLR-005`；
2. Agent 记录 Decision Log 并 Promotion；
3. 同步 Article Content Core、Working Argument Map、Framework Status 与方法论正文；
4. 重新执行 `MA-FW-001` readiness review；
5. 如人类明确批准具体版本，才创建 Approved Framework Snapshot；
6. 正式 release 前解决 `CLR-009`。

## 3. BLOCKERS / GATES

### Framework Approval

`MA-FW-001` 被以下 item 阻塞：

- `CLR-001`
- `CLR-002`
- `CLR-005`

### Formal release

- `CLR-009` — license 未决定。

## 4. PENDING HUMAN DECISIONS / CLARIFICATIONS

### CLR-001 — 方法论文章的中心责任概念

**状态：** `WAITING-HUMAN`  
**严重度：** `BLOCKING`

问题：如何区分和命名“AI 可以承担的认知工作”与“人类必须保留的责任”？

候选：

- `cognitive labor / 认知劳动`
- `epistemic responsibility / 认识责任`
- `cognitive responsibility / 认知责任`
- 人类提出的其他术语体系

**AI-PROPOSED：** 使用“认知劳动 vs 认识责任”的分层区分。

**Promotion 目标：** Article Content Core -> Framework -> Artifact。

### CLR-002 — Framework Responsibility Thesis 的强度

**状态：** `WAITING-HUMAN`  
**严重度：** `BLOCKING`

候选：

1. 强版本：Framework Approval 一般性地构成 AI 辅助长篇成果中实质性思想作者身份的中心；
2. 中等版本：Framework Approval 是 HARC 内集中高杠杆人类审阅的主要责任锚点，不主张一般 authorship theory；
3. 人类修订的第三种版本。

**AI-PROPOSED：** 暂偏向中等版本。

### CLR-003 — `semantic version control`

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

**AI-PROPOSED：** 作为明确限定的 HARC working term / coinage，而非既有成熟标准。

### CLR-004 — `generation–verification asymmetry`

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

**AI-PROPOSED：** 仅作为 heuristic label，不表述成已证实的经验定律。

### CLR-005 — `responsibility concentration` 是否保留

**状态：** `WAITING-HUMAN`  
**严重度：** `BLOCKING`

候选：

- `epistemic responsibility anchoring / 认识责任锚定`
- `responsibility architecture / 责任架构`
- `high-leverage human review / 高杠杆人类审阅`
- 保留 `responsibility concentration` 但严格限定

**AI-PROPOSED：** 降级或替换。

### CLR-006 — extended / distributed cognition 的理论关系

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

候选：中心理论基础 / 次级比较 / 最少背景。  
**AI-PROPOSED：** 次级概念比较。

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

## 5. BACKLOG

- 自动化 onboarding / conformance check；
- repository-backed context 的上下文成本与 stale-state 研究；
- Working Memory 更新粒度、压缩策略与 handoff 效率研究；
- 跨 Agent / 跨平台接管测试。

## 6. SYNC DEFECTS

`NONE RECORDED`

## 7. COMPLETION RULE

任务完成时：

1. 从本文件 active list 删除/退出；
2. 在 Work Log 增加高层完成摘要；
3. 如形成长期规范结果，执行 Promotion；
4. 必要时更新 Current Focus；
5. 不在本文件积累长期 completed-history。
