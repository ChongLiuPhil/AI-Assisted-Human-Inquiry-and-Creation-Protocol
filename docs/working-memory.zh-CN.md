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

HARC v0.2 draft 正在进行协议架构完善与方法论文章 Working Framework 阶段。

当前最新协议发展：

- zero-context onboarding 已建立；
- repository-backed context interface 已建立；
- 原 “Layer 1.5 / Critical Clarification Layer” 正在迁移为与三层长期记忆并行的 Working Memory；
- 方法论文章尚无 Approved Framework；
- 方法论文章正文仍为 `DERIVED-PROVISIONAL`。

## 2. CURRENT_OBJECTIVE

### WM-OBJ-001 — 完成 Working Memory 架构迁移

**状态：** `IN-PROGRESS`

目标：

- 建立 Working Memory protocol 与项目状态文件；
- 把 Clarification 从“1.5 层”改为 Working Memory item type；
- 将现有 CLR-001 至 CLR-009 迁移到本文件；
- 更新 manifest、context interface、onboarding、architecture、templates 与方法论文章；
- 保留旧 clarification-register 路径作为兼容指针；
- 完成中英文 parity 与自举验证。

## 3. ACTIVE_TASKS

- `WM-T001` — 更新 Protocol Core / Decision Log：`IN-PROGRESS`
- `WM-T002` — 建立 Working Memory protocol 与当前 Working Memory：`IN-PROGRESS`
- `WM-T003` — 迁移 Clarification workflow：`TODO`
- `WM-T004` — 更新 onboarding / manifest / context interface：`TODO`
- `WM-T005` — 更新 project templates：`TODO`
- `WM-T006` — 更新方法论文章上游状态与正文：`TODO`
- `WM-T007` — 双语 / repository regression audit：`TODO`

## 4. RECENTLY_COMPLETED

- `HARC-D018` — zero-context onboarding / handshake；
- `HARC-D019` — session-context safeguard 的早期版本；
- `HARC-D020` — 将其收缩为 Repository Resolver，并建立 Repository-Backed Context Interface；
- 当前仓库已采用中文 canonical / 英文 synchronized mirror；
- 当前 GitHub 已作为权威外部记忆和工作状态源。

## 5. NEXT_ACTIONS

1. 完成 D021 向全部协议与模板传播；
2. 将本 Working Memory 设为 onboarding 的 resume index；
3. 完成后重新检查方法论文章 Framework gate；
4. 之后优先处理阻塞 `MA-FW-001` 的 CLR-001 / CLR-002 / CLR-005；
5. 正式 release 前解决 CLR-009 licensing。

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

当前 D021 Working Memory migration 尚未完全传播完成，在完成本轮前视为临时同步缺陷。

完成条件：

- Protocol Core / Decision Log；
- Working Memory protocol；
- Persistent Memory / Architecture / Specification；
- START_HERE / AGENTS / Bootstrap / Onboarding；
- Manifest / Context Interface；
- templates；
- methodology article；
- bilingual parity；
- onboarding self-test。

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
