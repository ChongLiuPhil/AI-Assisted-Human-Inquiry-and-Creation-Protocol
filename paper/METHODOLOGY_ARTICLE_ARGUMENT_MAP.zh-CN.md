# 方法论文章 — Working Argument Map

**状态：** `WORKING-FRAMEWORK — REVISED UNDER AHICP-D030 / HUMAN REVIEW PENDING`  
**题目：** 《从对话到持久研究状态：AI时代的人机研究协作、人类责任与可审计作者性》  
**规范上游：** `METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`  
**授权来源：** `AHICP-D030`  
**说明：** 本 map 是 AI 在人类已确认方向下组织的工作框架。AHICP-D030 授权结构性重写，但不等于对本完整 map 的整体 Framework Approval。

---

## 1. 论文中心问题

生成式 AI 已经能够大规模参与检索、整理、比较、起草、重组、核验、格式处理与执行工作，但长期项目仍面临一个没有被“更长上下文”自动解决的问题：

> **一个持续数月或数年的项目，怎样保存自己的目标、依据、判断、决定、当前状态与发布边界，使它不依赖某一次对话、某一个模型或某个平台记忆？**

论文把这一问题从“AI 如何记住更多”重新表述为“项目如何拥有自己的持久记忆”。

核心工程命题：

> **长期人机项目的持久记忆应属于项目，而不是属于某个具体模型。**

这里的“属于项目”指关键状态被外部化为人类可检查、可编辑、可版本化、可追溯、可迁移的权威状态，而不是只存在于模型上下文、平台私有记忆或不可检查的内部机制中。

---

## 2. 主要理论贡献

### T1 — Governed Project Memory Thesis
**来源：HUMAN-CONFIRMED D030 + LITERATURE-CONSTRAINED**

长期人机协作需要从 conversational / agent memory 区分出 **governed Project Memory**。但 “project memory” 本身不是 AHICP 首创：organizational memory、Project Memory（Weiser & Morrison, 1998）、大型项目中的 project-memory practice（Mariano & Awazu, 2024）以及 design-rationale / architecture-knowledge-management 文献都构成明确前史。

AHICP 的候选贡献应更窄地表达为：把 project memory 进一步组织为适用于可替换 LLM Agent 的 **authoritative, inspectable, versioned, human-governed project state**，并与 Working Memory continuity、human decision status、authorization/publication boundary 与 approval gates 统一。

### T2 — Model-Independent Memory Thesis
**来源：HUMAN-CONFIRMED — AHICP-D030**

项目的关键长期状态应尽可能独立于具体模型、供应商、聊天和平台私有记忆。模型上下文是当前任务的临时投影，不是项目真值源。

### T3 — Layered Project-Memory Architecture
**来源：HUMAN-CONFIRMED + EXISTING AHICP ARCHITECTURE**

AHICP 以三层长期研究记忆和并行 Working Memory 为骨架：

`Layer 1 Human Authorial Core -> Layer 2 Current/Approved Framework -> Layer 3 Derived Artifact`

并行：

`Working Memory = current stage / focus / tasks / blockers / clarifications / next actions / handoff`

同时从功能上区分 normative、epistemic/evidence、decision、working/operational、handoff、publication/authorization memory。功能角色不要求一对一对应物理文件。

### T4 — Working Memory as Continuity Layer
**来源：HUMAN-CONFIRMED — AHICP-D030**

AHICP Working Memory 不是心理学意义上的 working memory，也不是模型隐藏状态或 chain-of-thought。它是项目当前认识/任务状态的持久操作表示，是跨会话、跨 Agent 的 continuity layer。

Current Focus + Task Plan 构成默认 resume state；Work Log 支持按需历史回顾。

### T5 — Human Decision Persistence
**来源：HUMAN-CONFIRMED — AHICP-D030**

人类决定本身是 first-class project memory。系统必须能区分至少：
- PROPOSED；
- CONFIRMED / APPROVED；
- REJECTED；
- DEFERRED / OPEN；
- AUTHORIZED within scope。

换 Agent 不应使已拒绝方案重新变成“未知”，也不应使已确认决定失去来源。未来当然可以修改决定，但修改需要新的 provenance、理由、版本和授权。

### T6 — Agent / Model Substitution Resilience
**来源：HUMAN-CONFIRMED — AHICP-D030**

Agent 与模型应可替换而不破坏项目连续性。替换当前 Agent、移除原始聊天与平台私有记忆后，新 Agent 仍应能恢复项目目的、证据、决定、framework、当前任务、隐私/发布边界与下一步。

这既是设计原则，也是可经验测试的 stress test。

### T7 — Inspectable and Provenance-Aware State
**来源：HUMAN-CONFIRMED — AHICP-D030 + existing AHICP**

影响长期工作的记忆应尽量可检查、可编辑、可版本化，并保留来源和状态。Git commit history 本身不足以表达语义状态，因此还需要 Decision Log、evidence/provenance、approval state 与 upstream-first propagation。

### T8 — Memory Dynamics and Curation
**来源：HUMAN-CONFIRMED — AHICP-D030**

可靠 project memory 不是“保存一切”。必须治理：
- active vs archived；
- current vs stale；
- conflicting memory；
- selective retrieval；
- summaries / indexes；
- promotion / resolution / write-back；
- history growth；
- privacy / disclosure boundary。

模型上下文只应读取当前任务所需的最小权威状态；写回后旧摘录立即视为 stale。

### T9 — Human Authority and Responsibility as AHICP Normative Governance
**来源：HUMAN-CONFIRMED — HARC-D023/D024 + AHICP-D030**

在 AHICP 的治理范围内，项目目的、核心问题、方向、实质判断、关键批准与最终公开责任位置保持在人类一侧；AI 可以执行或辅助大量检索、整理、起草、核验与技术操作。Decision persistence 使这种人类治理不只存在于当下对话，而成为可追踪项目状态。

**边界：** 这是 AHICP 的规范性治理原则，并受具体研究诚信、出版与领域规则约束；它不被写成关于所有认知系统、所有领域或一般作者身份的普遍哲学定律。

### T10 — Framework Approval as a Structured Human-Review Gate and Responsibility Anchor
**来源：HUMAN-CONFIRMED — HARC-D023/D024；SCHOLARLY REVIEW REWORDED 2026-09-21**

对于长篇成果，Layer 2 Framework 是显式呈现核心主张、推论关系、关键区分、范围条件与结构性承诺的 structured human-review interface。Framework Approval 在 AHICP 内部构成重要 responsibility anchor；Final Artifact Approval 继续作为独立门，确认具体公开版本。

**边界：** 当前没有实证证据证明 Framework Approval 能减少总审阅成本，也不把它当作 Final Artifact Approval 或全文事实核验的替代品。

### T11 — Prior Project Memory, Agent Memory, and the AHICP Integration Boundary
**来源：HUMAN-CONFIRMED D030 + LITERATURE-CONSTRAINED**

既有 organizational/project-memory 文献已经讨论项目历史、知识、上下文、rationale 与新成员续接；design-rationale / architecture-knowledge-management / decision-provenance 文献已经讨论决定理由与来源；Generative Agents、MemGPT、Agent-memory surveys、LongMemEval / MemBench 与 RealMem 则把长期 memory 带入 LLM Agent 与 project-oriented interaction。

因此 AHICP 不应与这些传统竞争“谁首先提出 project memory”或“谁让 Agent 记得更多”。其候选贡献是把三条传统连接成一个 governed Project Memory architecture：即使 Agent 有强内部 memory，项目仍维护独立的 authoritative state，并把 Working Memory、human decision status、authorization/publication boundary 与 cross-Agent substitution 作为一体化治理机制。

### T12 — Empirical Evaluation Framework
**来源：HUMAN-CONFIRMED AS RESEARCH AGENDA — AHICP-D030**

论文提出、但不伪造结果：
- zero-context handoff / resumption；
- agent/model substitution；
- decision persistence；
- semantic drift / framework fidelity；
- review effort；
- stale/conflict handling；
- memory curation / retrieval efficiency。

### T13 — Provider-Neutrality
**来源：EXISTING AHICP + D030**

GitHub 是当前参考实现，不是理论前提。真正的架构要求是存在一个可版本化、可查询、可写回、可迁移、权限可控的 authoritative project-state substrate。

---

## 3. 与现有研究的概念边界

### 3.1 Organizational / Project Memory
Walsh & Ungson 的 organizational memory、Weiser & Morrison 的 Project Memory，以及 Mariano & Awazu 对大型项目记忆实践的研究都说明：组织/项目层的记忆、历史、context、rationale 与续接并非 AHICP 首创。

AHICP 不把“Project Memory”本身作为 novelty claim。它关注的是 AI-assisted inquiry 中 **authoritative project state + human governance + Agent/model substitution** 的组合。

### 3.2 Agent Memory
现有研究常讨论 experience storage、retrieval、reflection、long/short-term memory management、multi-session recall、temporal reasoning、knowledge updates 等。它们主要优化 Agent 的记忆能力。

AHICP 不要求替代内部 Agent memory；相反，它把内部 memory 视为可能的辅助层，但不允许其自动成为项目权威状态。

### 3.3 Design Rationale / Architecture Knowledge Management / Decision Provenance
软件工程与 accountability 文献已经长期讨论 design decisions、rationale、knowledge capture/maintenance 与 decision provenance。AHICP 的 Human Decision Persistence 必须建立在这一前史上，而不是声称首先发现“决定需要被保存”。

AHICP 进一步要求决定携带 project-governance semantics，例如 proposed / approved / rejected / deferred / authorized，并参与 Working Memory -> Decision Log -> Long-Term Memory -> Artifact 的传播。

### 3.4 Provenance Standards
W3C PROV 等工作提供描述实体、活动、Agent 与派生关系的通用背景。AHICP 借鉴“来源应可追踪”的思想，但并不声称自身文件模型是 PROV 的实现，也不以 provenance 标准证明 AHICP 的有效性。

### 3.5 Extended / Distributed Cognition
Clark & Chalmers、Hutchins 提供外部认知脚手架和分布式认知的理论背景。论文采取弱主张：repository 是 persistent cognitive/project-state scaffold；不需要把 AI 或 repository 提升为独立认知主体。

### 3.6 Candidate Synthesis Contribution
当前最可辩护的 novelty 定位是：AHICP 把 prior project memory、Agent memory、decision/rationale provenance 与 human approval/authorization 机制组织为一个 **governed, model-substitutable Project Memory Architecture**。

该 novelty 仍需系统 literature review 与同行评审检验；当前 framework 不得使用未经证据支持的 “first” / “unique” 优先权表述。

---

## 4. 论文结构

### I. 引言：从“AI能不能写”转向“项目怎样保持连续”
提出 generation–verification asymmetry 作为分析标签，并把问题导向 project memory。

### II. 相关工作与问题边界：既有 Project Memory、Agent Memory 与 Decision Provenance
讨论 organizational/project memory、design rationale / architecture knowledge management、decision provenance、Generative Agents、MemGPT、Agent-memory survey、LongMemEval、MemBench、RealMem，以及 provenance / distributed cognition 背景。

### III. 设计要求：一个长期项目的记忆必须具备什么性质
提出 model independence、inspectability、versionability、provenance、decision persistence、resumability、selective retrieval、privacy boundary 与 human authority。

### IV. AHICP Project Memory Architecture
给出三层长期记忆 + Working Memory + Decision/Evidence/Form/Authorization 等功能角色映射，解释 repository-backed context。

### V. Working Memory：作为跨会话连续性层
明确不是心理学 working memory / hidden state；解释 Current Focus、Task Plan、Work Log、Clarification、Promotion。

### VI. 决策持久化与人类权威
讨论 proposed/confirmed/rejected/deferred/authorized，Decision Log，授权 provenance，以及人类决定如何成为长期状态。

### VII. Agent / Model 替换：从原则到压力测试
解释 zero-context onboarding、manifest、bootstrap、Onboarding Report、stale-cache invalidation 与 handoff criterion。

### VIII. 记忆不是越多越好：curation、冲突、过期与隐私
讨论 memory bloat、conflicting state、selective retrieval、archive、summary、privacy/publication boundary。

### IX. Framework Approval、作者责任与公开成果
把 project memory 架构与 Framework Approval / Final Artifact Approval、framework defect vs derived-expansion defect、reader-facing projection 连接起来。

### X. 与既有 Project Memory、Agent Memory 与 Provenance 研究的关系
明确三条传统的交叉与边界，并把 AHICP novelty 限定为 governed, model-substitutable Project Memory Architecture 的 candidate synthesis。

### XI. 评估框架与研究议程
列出测试任务、指标与对照设计，明确没有实证结果。

### XII. 局限与反对意见
维护成本、rubber-stamp approval、错误持久化、过度结构化、隐私、平台依赖、冲突解决、不同领域适用性。

### XIII. 结论
核心句：

> **一个长期人机项目的持久记忆，应当属于项目，而不是属于某一个模型。**

并连接人类目的、证据、决定、可续接状态与责任。

---

## 5. 评估框架（当前为 proposed evaluation）

| 测试 | 操作 | 主要指标 |
|---|---|---|
| Zero-context handoff | 移除聊天历史，让新 Agent 只读项目入口 | state reconstruction accuracy, missing critical state, time-to-resume |
| Agent/model substitution | 更换模型/供应商 | decision retention, task continuity, policy adherence |
| Decision persistence | 注入 confirmed / rejected / deferred decisions | reopening error rate, provenance accuracy |
| Semantic drift / fidelity | 多轮 AI 修改同一项目 | core-claim drift, framework-artifact consistency |
| Stale/conflict handling | 提供新旧冲突状态 | stale-use rate, conflict surfacing rate |
| Memory curation | 扩大历史规模 | retrieval precision/recall, context cost, resume quality |
| Review effort | 与 chat-centric workflow 比较 | human review time, serious defect rate, correction latency |

这些指标只是研究设计。当前论文不报告实验结果。

---

## 6. 当前来源与批准状态

- T1–T10、T12 的方向由 AHICP-D030 与此前 HARC-D023/D024 等人类决定支持。
- T11 的文献定位受外部证据约束，不应把相关研究写成对 AHICP 的验证。
- `semantic version control` 与 `generation–verification asymmetry` 可作为解释性标签使用，但不声称是成熟领域标准术语。
- 当前完整 framework 仍是 `WORKING-FRAMEWORK`；AHICP-D030 是 `REVISE / STRUCTURAL REWRITE AUTHORIZED`，不是整体 `APPROVE`。
- Final Artifact Approval 尚未发生。