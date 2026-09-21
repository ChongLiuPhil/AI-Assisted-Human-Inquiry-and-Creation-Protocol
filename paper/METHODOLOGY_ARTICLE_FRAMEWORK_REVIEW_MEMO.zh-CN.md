# 方法论文章 — Framework Scholarly Review Memo

**状态：** `SCHOLARLY REVIEW COMPLETED — MA-FW-001 APPROVED`  
**日期：** 2026-09-21  
**对象：** `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`  
**依据：** HARC-D023 / HARC-D024 / HARC-D025、AHICP-D030，以及 2026-09-21 prior-art / novelty audit。  
**说明：** 本文件记录形成 `MA-FW-001` 的最终 scholarly review。Framework 的正式批准已由 `AHICP-D031` 与 `paper/frameworks/MA-FW-001.zh-CN.md` 固化；本 memo 仍是审阅记录，不替代批准快照。

---

## 1. 总体结论

当前 13 项 framework theses 已足够形成 AHICP 方法论文章的第一个 Approved Framework，但必须保持以下学术边界：

1. 不把 AHICP 写成 “project memory” 概念、organizational memory、design rationale、decision provenance 或 Agent long-term memory 的首创；
2. 不把架构设计原则写成已经由实验验证的效果性定律；
3. 不把 AHICP 的人类责任规范泛化成所有领域的普遍作者身份理论；
4. Framework Approval 只作为 AHICP 内部的 structured human-review gate / responsibility anchor，不声称它已经被证明减少审阅成本；
5. proposed evaluation 继续属于 research agenda；没有真实实验数据就不得升级成效果结论；
6. Final Artifact Approval 与 venue-specific requirements 继续独立存在。

在这些边界下，当前框架已依据 AHICP-D031 批准为 `MA-FW-001`。

---

## 2. T1–T13 逐项审阅

### T1 — Governed Project Memory Thesis
**结论：`APPROVE — LITERATURE-CONSTRAINED`**

可批准的内容是：AHICP 把既有 project-memory / organizational-memory 前史进一步组织为面向可替换 LLM Agent 的 authoritative、inspectable、versioned、human-governed project state。

**不得主张：** AHICP 首创 project memory。

### T2 — Model-Independent Memory Thesis
**结论：`APPROVE AS DESIGN PRINCIPLE`**

模型上下文与平台私有 memory 不应成为项目唯一权威状态。该主张是 AHICP 的工程设计原则，不是关于所有 AI 系统的经验定律。

### T3 — Layered Project-Memory Architecture
**结论：`APPROVE AS ARCHITECTURE SPECIFICATION`**

批准三层 Long-Term Research Memory + 并行 Working Memory，以及 normative / epistemic / decision / operational / handoff / publication-authorization 等功能角色。

**限定：** memory role 是功能分类，不要求一一映射到物理文件。

### T4 — Working Memory as Continuity Layer
**结论：`APPROVE WITH TERMINOLOGY BOUNDARY`**

批准 AHICP Working Memory 作为持久 current-state / resume-state layer。

**必须保持：** 它不是心理学 working memory、模型 hidden state、scratchpad 或 chain-of-thought。

### T5 — Human Decision Persistence
**结论：`APPROVE AS GOVERNANCE MECHANISM`**

批准 proposed / approved / rejected / deferred / authorized 等状态作为 first-class project state。

**限定：** 决策记录、rationale 与 provenance 有明确前史；AHICP 的候选贡献在于把它们与 Agent substitution、Working Memory 和 authorization lifecycle 统一。

### T6 — Agent / Model Substitution Resilience
**结论：`APPROVE AS DESIGN GOAL + PROPOSED STRESS TEST`**

批准“替换 Agent/model 后项目仍可恢复”为设计目标；批准 substitution test 作为 proposed evaluation。

**不得主张：** 当前 AHICP 已被实验验证具有跨模型鲁棒性。

### T7 — Inspectable and Provenance-Aware State
**结论：`APPROVE AS DESIGN REQUIREMENT`**

批准 inspectability / editability / versionability / provenance-aware state。

Git commit history 可作为变化记录，但不应被写成足够表达 semantic state；Decision Log、evidence/provenance、approval state 等承担更具体的语义职责。

### T8 — Memory Dynamics and Curation
**结论：`APPROVE AS DESIGN REQUIREMENT + RESEARCH QUESTION`**

批准 active/archive、current/stale、conflict surfacing、selective retrieval、promotion/write-back、privacy boundary 等治理要求。

**效果问题继续开放：** 最优 retrieval / curation policy 仍需经验研究。

### T9 — Human Authority and Responsibility
**结论：`APPROVE AS AHICP NORMATIVE GOVERNANCE`**

批准 AHICP 内部的人类目的、关键判断、批准与最终公开责任位置。

**重要收缩：** 这是 AHICP 的治理规范与出版/研究诚信约束下的设计立场，不写成关于所有认知系统、所有领域或所有作者身份问题的普遍哲学定律。

### T10 — Framework Approval as Structured Human-Review Gate and Responsibility Anchor
**结论：`APPROVE — REWORDED`**

原 “Compressed Responsibility Interface” 过度暗示审阅效率已经成立，改为：

> **Framework Approval as a Structured Human-Review Gate and Responsibility Anchor**

批准以下内容：
- framework 是长篇项目中集中呈现核心主张、推论关系、区分、范围与结构性承诺的审阅界面；
- approved framework 是 AHICP 内部的重要 responsibility anchor；
- Final Artifact Approval 独立存在。

**不得主张：** Framework Approval 已被证明能减少总审阅时间或替代最终全文审查。

### T11 — Prior Project Memory, Agent Memory, and the AHICP Integration Boundary
**结论：`APPROVE — LITERATURE-CONSTRAINED`**

批准三条研究传统的交叉定位：prior project/organizational memory、decision/rationale/provenance、Agent memory。

AHICP novelty 仅作为 **candidate architectural synthesis** 表述，留给系统 literature review 与同行评审最终判断。

### T12 — Empirical Evaluation Framework
**结论：`APPROVE AS RESEARCH AGENDA`**

批准 seven-part evaluation program：
- zero-context handoff；
- Agent/model substitution；
- decision persistence；
- semantic drift / framework fidelity；
- stale/conflict handling；
- memory curation / retrieval efficiency；
- human review effort。

**状态：** proposed evaluation；无实证结果。

### T13 — Provider Neutrality
**结论：`APPROVE AS IMPLEMENTATION PRINCIPLE`**

批准 GitHub 作为 reference implementation，而非理论前提。底层 substrate 只需满足 versionable / queryable / writable / migratable / access-controlled 等必要能力。

---

## 3. 批准后的核心压缩命题

`MA-FW-001` 应围绕以下压缩命题组织：

> **长期 AI-assisted inquiry / creation 应把对未来工作有约束力的项目状态外部化为可检查、可版本化、可追溯、可迁移且由人类治理的 Project Memory。模型与 Agent 可以替换；项目的目的、证据、决定、当前工作状态、授权与发布边界不应因此丢失。AHICP 通过三层长期研究记忆、并行 Working Memory、Human Decision Persistence、provenance-aware state 与 Framework / Final Artifact approval gates，把项目连续性与人类责任连接起来。该架构的实际效果仍需通过明确的 empirical evaluation 进行检验。**

---

## 4. 仍不进入 Approved Framework 的更强主张

以下内容继续保持 provisional / open，不因 Framework Approval 自动成立：

- AHICP 是首个 project-memory framework；
- governed Project Memory Architecture 在学术上“独一无二”；
- AHICP 已经提高准确性、研究诚信、效率或降低审阅成本；
- Framework Approval 是普遍作者身份理论；
- 人类必须对所有 AI 辅助内容逐字独立重新推导；
- repository-backed state 是所有任务唯一正确的 memory architecture；
- extended-mind thesis 或 distributed cognition 的强形而上学版本；
- specific benchmark 的样本、统计设计和最终效果结论；
- target venue / disciplinary positioning 的最终选择。

---

## 5. Framework Approval 与 Final Artifact Approval

本轮可以完成 **Framework Approval**，创建 `MA-FW-001`。

这只表示人类已批准当前思想架构及上述边界，不表示：
- 当前长篇正文逐句最终批准；
- 引文格式已满足某个目标期刊；
- venue-specific AI / authorship policy 已完成核验；
- Final Artifact Approval 已发生；
- 论文已经适合直接投稿而无需最终编辑。

因此 Framework Approval 后，正文状态应从 `DERIVED-PROVISIONAL` 转为 **derived from MA-FW-001 / Final Artifact Approval pending**。

---

## 6. 当前审阅结论

**Framework scholarly review：`PASS WITH BOUNDED REWORDING`**

批准所需的唯一实质性 wording repair 是 T10 的收紧以及对 T9 的规范性边界明确化；其余 T1–T13 可以按现有 evidence-constrained 版本进入 `MA-FW-001`。

