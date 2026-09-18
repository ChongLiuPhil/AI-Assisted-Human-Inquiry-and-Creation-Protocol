# HARC Working Memory
## 当前工作记忆区

**状态：** `ACTIVE WORKING MEMORY`  
**角色：** 当前项目阶段、任务、阻塞、待确认事项与续接状态的持久操作界面。  
**权威边界：** 本文件不是长期实质性主张的最终真值源；稳定结果必须 Promotion 到对应长期记忆。  
**语言：** 中文 canonical；英文 `working-memory.md` 是同步 mirror。

> 新的人类协作者或 AI Agent 应先用本文件回答：“项目现在做到哪里，下一步从哪里继续？”  
> 然后再从三层长期记忆中按当前任务 selective retrieval 最新 canonical state。

---

## 1. CURRENT_STAGE

HARC v0.2 draft 的 Working Memory 架构迁移已完成。当前主要处于**方法论文章 Working Framework 的人类澄清 / Framework Approval 准备阶段**。

当前状态：

- zero-context onboarding 已建立；
- repository-backed context interface 已建立；
- 三层 Long-Term Research Memory + 并行 Working Memory 已正式实施；
- Clarification 已成为 Working Memory item，旧 clarification-register 仅为 compatibility pointer；
- 方法论文章尚无 Approved Framework；
- 方法论文章正文仍为 `DERIVED-PROVISIONAL`。

## 2. CURRENT_OBJECTIVE

### WM-OBJ-002 — 推进方法论文章进入 Framework Approval 准备状态

**状态：** `WAITING-HUMAN`

当前需要人类解决三个阻塞 `MA-FW-001` 的核心问题：

- `CLR-001` — 方法论文章中心责任概念；
- `CLR-002` — Framework Responsibility Thesis 的强度；
- `CLR-005` — `responsibility concentration` 是否保留或替换。

这些决定完成并 Promotion 后，才能重新校准 Article Content Core / Argument Map / Draft，并进入 Framework Approval review。

## 3. ACTIVE_TASKS

- `WM-T008` — 人类决定 CLR-001：`WAITING-HUMAN`
- `WM-T009` — 人类决定 CLR-002：`WAITING-HUMAN`
- `WM-T010` — 人类决定 CLR-005：`WAITING-HUMAN`
- `WM-T011` — 将上述决定 Promotion 并传播到 Layer 1 / Layer 2 / Layer 3：`TODO`
- `WM-T012` — 重新执行 Framework Approval readiness review：`TODO`
- `WM-T013` — CLR-009 licensing 决定（formal release 前）：`WAITING-HUMAN`

## 4. RECENTLY_COMPLETED

- `HARC-D018` — zero-context onboarding / handshake；
- `HARC-D019` — session-context safeguard 的早期版本；
- `HARC-D020` — Repository Resolver / Repository-Backed Context Interface；
- `HARC-D021` — 三层 Long-Term Research Memory + 并行 Working Memory；
- `WM-T001–WM-T007` — Working Memory protocol、Clarification migration、onboarding、manifest/context interface、templates、方法论文章、双语与 repository regression audit 全部完成；
- 最新递归双语检查：`108 Markdown = 54 Chinese canonical + 54 English mirror; missing pairs = 0`。

## 5. NEXT_ACTIONS

1. 人类确认 `CLR-001 / CLR-002 / CLR-005`；
2. Agent 将确认结果 Promotion 到 Decision Log 与相应长期记忆；
3. 同步 Article Content Core、Working Argument Map 与方法论正文；
4. 重新执行 `MA-FW-001` Framework Approval readiness review；
5. 如人类明确批准具体 framework 版本，再创建 Approved Framework Snapshot；
6. 正式 release 前解决 `CLR-009` licensing。

## 6. BLOCKERS / GATES

### 方法论文章 Framework Approval

`MA-FW-001` 当前仍被以下项目阻塞：

- `CLR-001`
- `CLR-002`
- `CLR-005`

### 正式开放授权 / release

- `CLR-009` — license 未决定。

## 7. PENDING_HUMAN_DECISIONS / CLARIFICATIONS

Clarification 是 Working Memory item，不是独立 Layer。

### CLR-001 — 方法论文章的中心责任概念

**状态：** `WAITING-HUMAN`  
**严重度：** `BLOCKING`  
**类别：** CONCEPT / TERMINOLOGY / TRANSLATION

**问题：** 如何区分和命名“AI 可以承担的认知工作”与“人类必须保留的责任”？

候选包括：

- `cognitive labor / 认知劳动`
- `epistemic responsibility / 认识责任`
- `cognitive responsibility / 认知责任`
- 人类提出的其他术语体系

**AI-PROPOSED：** 使用认知劳动 vs 认识责任的分层区分。

**Promotion 目标：** Article Content Core -> Framework -> Artifact。

### CLR-002 — Framework Responsibility Thesis 的强度

**状态：** `WAITING-HUMAN`  
**严重度：** `BLOCKING`

候选：

1. 强版本：Framework Approval 一般性地构成 AI 辅助长篇成果中实质性思想作者身份的中心；
2. 中等版本：Framework Approval 是 HARC 内集中高杠杆人类审阅的主要责任锚点，不主张一般 authorship theory；
3. 人类修订的第三种版本。

**AI-PROPOSED：** 暂偏向中等版本。

### CLR-003 — `semantic version control` 是否正式采用

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

**AI-PROPOSED：** 可作为明确限定的 HARC working term / coinage，而非既有成熟标准。

### CLR-004 — `generation–verification asymmetry` 的地位

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

### CLR-006 — 与 extended / distributed cognition 的理论关系

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

候选：中心理论基础 / 次级比较 / 最少背景。

**AI-PROPOSED：** 次级概念比较。

### CLR-007 — 经验验证计划在方法论文章中的地位

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

候选：核心贡献 / Future Research / 省略。

**AI-PROPOSED：** Future Research Agenda。

### CLR-008 — 方法论文章主要学科定位

**状态：** `WAITING-HUMAN`  
**严重度：** `NON-BLOCKING`

候选包括：

- philosophy of technology / epistemology
- research methodology
- scholarly communication / research integrity
- interdisciplinary AI governance

**AI-PROPOSED：** interdisciplinary research methodology，以 philosophy of technology / epistemology 为理论核心。

### CLR-009 — HARC 开放许可

**状态：** `WAITING-HUMAN`  
**严重度：** `BLOCKING`（formal release），`NON-BLOCKING`（methodology framework）

候选：

- documentation CC BY 4.0 + code MIT
- Apache-2.0
- MIT
- 其他

**关联：** `LICENSE-DECISION.zh-CN.md`

## 8. SYNC_DEFECTS

**当前已知协议级同步缺陷：** `NONE RECORDED`

D021 已传播至：

- Protocol Core / Decision Log；
- Working Memory protocol / Clarification workflow；
- Persistent Memory / Architecture / Specification；
- START_HERE / AGENTS / Bootstrap / Onboarding；
- Manifest / Context Interface；
- project templates；
- methodology article Content Core / Argument Map / Framework Status / Draft；
- bilingual parity audit / onboarding self-test。

未决的人类决定属于 `PENDING_HUMAN_DECISIONS`，不等同于同步缺陷。

## 9. RECENTLY_RESOLVED / PROMOTED

### CLR-000 — 中文 canonical / 英文 synchronized mirror

**状态：** `PROMOTED`  
**Decision IDs：** HARC-D015、HARC-D016  
**长期目标：** Protocol Core、Bilingual Sync Policy、Specification、AGENTS、templates。

该项的权威答案已经存在长期记忆，本文件只保留指针。

## 10. HANDOFF_NOTE

新接入者：

1. 先读取 `HARC_MANIFEST.yaml` 与 `HARC_CONTEXT_INTERFACE.yaml`；
2. 读取本 Working Memory，确认 CURRENT_STAGE / CURRENT_OBJECTIVE / BLOCKERS；
3. 不要把本文件中的 substantive summary 当成长效真值；
4. 按当前任务从 Layer 1 / Layer 2 / Layer 3 最新 canonical 文件读取权威状态；
5. 完成任务后更新本 Working Memory 的完成情况与下一步。

---

## Long-Term Memory Pointers

### Layer 1 — Human Authorial Core

- `core/PROTOCOL_CORE.zh-CN.md`
- `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`
- `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`
- `core/DECISION_LOG.zh-CN.md`

### Layer 2 — Current Framework

- `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`
- `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`
- Approved Framework snapshots（如有）

### Layer 3 — Derived Artifact

- `paper/METHODOLOGY_ARTICLE.zh-CN.md`
- `paper/METHODOLOGY_ARTICLE.en.md`
