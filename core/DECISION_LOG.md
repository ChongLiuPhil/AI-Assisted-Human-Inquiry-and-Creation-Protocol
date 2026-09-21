# HARC Decision Log

> **Language:** Chinese canonical: `core/DECISION_LOG.zh-CN.md`; this English file is the synchronized mirror.

This file is the chronological audit trail of substantive human decisions about the protocol project.

## Entry format

- Date
- Identifier
- Source
- Classification
- Decision
- Affected components
- Status

---

## 2026-09-17 — HARC-D001

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** Create an independent open GitHub project devoted solely to the Human–AI Research Collaboration Protocol, separate from any particular research paper or topic.

**Affected components:** repository scope, README, specification, white paper, templates

**Status:** implemented.

---

## 2026-09-17 — HARC-D002

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** The initial implementation should focus on GitHub as the persistent collaboration platform between a human and AI agent(s). Other platforms may be considered later.

**Affected components:** scope and architecture

**Status:** implemented.

---

## 2026-09-17 — HARC-D003

**Source:** Human project founder  
**Classification:** CONTENT, PROTOCOL

**Decision:** Human discussion should produce a persistent foundational record of the human author's substantive claims, corrections, confirmations, and revisions. AI expansion must remain constrained by that foundation.

**Affected components:** Content Core model, upstream-first rule

**Status:** implemented.

---

## 2026-09-17 — HARC-D004

**Source:** Human project founder  
**Classification:** FORM, PROTOCOL

**Decision:** Presentation and formatting instructions must be separated from research-content instructions and persisted in an independent form/presentation foundation. Cross-project author preferences should be reusable where appropriate.

**Affected components:** Form Core, routing model, templates

**Status:** implemented.

---

## 2026-09-17 — HARC-D005

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** AI agents should maintain a compact operational representation of the article/book argument. This representation is the primary discussion interface for structural collaboration and should remain subordinate to the human foundational state.

**Affected components:** Working Argument Map

**Status:** implemented.

---

## 2026-09-17 — HARC-D006

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** Human corrections should propagate upstream first: persist the human change, then update the operational representation, then update the expanded artifact.

**Affected components:** update cycles

**Status:** implemented.

---

## 2026-09-17 — HARC-D007

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** A working AI-maintained argument framework is not automatically human-endorsed. Human-confirmed versions should be explicitly preserved, and those approved frameworks should govern subsequent expansion.

**Affected components:** Framework Approval Gate, versioned framework snapshots

**Status:** implemented.

---

## 2026-09-17 — HARC-D008

**Source:** Human project founder  
**Classification:** CONTENT, FORM, PROTOCOL

**Decision:** The human-approved core framework should be reflected in the final work's overview—for example abstract/introduction in a paper, opening/overview in an article, or introduction/chapter roadmap in a book.

**Affected components:** overview projection rule

**Status:** implemented.

---

## 2026-09-17 — HARC-D009

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** Project continuity should depend explicitly on repository state rather than a particular AI platform's context or memory. Important discussion outcomes must be promoted into GitHub documents.

**Affected components:** persistent memory model, handoff requirements

**Status:** implemented.

---

## 2026-09-17 — HARC-D010

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** The repository may accumulate long-lived project memory, but active summaries should remain compact so new agents can reconstruct the project through selective reading rather than loading all history at once.

**Affected components:** memory scaling

**Status:** implemented.

---

## 2026-09-17 — HARC-D011

**Source:** Human project founder  
**Classification:** CONTENT, PROTOCOL

**Decision:** For long works, the human-approved operational framework should function as the primary substantive intellectual responsibility anchor. The human author should explicitly understand and approve the core theses, inferential relations, major distinctions, and section/chapter roles. Defects in that approved architecture should be distinguishable from local defects introduced only during later AI expansion. This does not replace any separate final-release review required before publication or submission.

**Affected components:** Protocol Core, Framework Approval model, responsibility model

**Status:** implemented after founding-idea repair audit.

---

## 2026-09-17 — HARC-D012

**Source:** Human project founder  
**Classification:** FORM, PROTOCOL

**Decision:** Form and presentation preferences should be reusable across projects and should support artifact-type differentiation. A new project should identify whether it is a book, academic paper, article, report, or another artifact type, and then combine reusable author preferences with artifact-type and project-specific form rules rather than rebuilding presentation decisions from scratch.

**Affected components:** Form Core model, form-profile inheritance, templates

**Status:** implemented after founding-idea repair audit.

---

## 2026-09-17 — HARC-D013

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** A requested three-pass review must be interpreted as three complete review-and-repair cycles. In each cycle the agent should inspect the project, identify omissions or defects, repair and implement the required changes, and then verify the repair before moving to the next cycle. After all three cycles, perform a further independent post-repair audit.

**Affected components:** Protocol Core, audit procedure, audit documentation

**Status:** implemented.

---

## 2026-09-17 — HARC-D014

**Source:** Human project founder  
**Classification:** CONTENT, FORM, PROTOCOL

**Decision:** HARC should simultaneously be a high-quality open project and produce a standalone methodology article. The article should explain HARC's conceptual architecture and examine human cognitive responsibility, the scope and limits of delegating intellectual work to AI, framework-level authorship, persistent research memory, and related questions of human–AI collaboration in the AI era.

**Affected components:** project purpose, README, methodology article, article framework, evidence layer, roadmap

**Status:** first governed methodology-article framework and complete Chinese provisional draft implemented; human Framework Approval and later Final Artifact Approval remain pending.

## 2026-09-18 — HARC-D015

**Source:** Human project founder  
**Classification:** FORM, PROTOCOL

**Decision:** All substantive content in the Human–AI Research Collaboration Protocol project must be maintained in both Chinese and English. Chinese is the canonical editing and review baseline. Every substantive edit must be synchronized to the English version in the same work cycle. If the two versions diverge, Chinese governs and the English mirror must be repaired. New project documents should be created bilingually from the start.

**Affected components:** Protocol Core, Specification, AGENTS contract, README, methodology article, evidence notes, audits, templates, future files

**Status:** initial repository-wide bilingual migration implemented; every future substantive edit remains subject to ongoing synchronization. See `docs/BILINGUAL_PARITY_AUDIT.md`.

---

## 2026-09-18 — HARC-D016

**Source:** Human project founder  
**Classification:** CONTENT, FORM, PROTOCOL

**Decision:** When the Chinese-canonical / English-synchronized-mirror rule is introduced, an older Chinese version must not mechanically overwrite substantive developments that had already been made in English before the rule existed. For any such legacy divergence, first absorb the newer English content into Chinese so that Chinese represents the genuinely latest semantic state at cutover; after bilingual parity is restored, switch permanently to Chinese-first development with English synchronization. After cutover, English must not develop substantive content independently.

**Affected components:** Bilingual Sync Policy, Protocol Core, AGENTS, Whitepaper, Parity Audit, future legacy migrations

**Status:** implemented. The white paper completed an English -> Chinese catch-up and then returned to a Chinese -> English synchronization relationship.

---

## 2026-09-18 — HARC-D017

**Source:** Human project founder  
**Classification:** CONTENT, FORM, PROTOCOL

**Decision:** HARC should add a dedicated document layer for governing high-impact uncertainty. When an AI Agent has important uncertainty about authorial intent, core positions, key claims, concepts, terminology, primary-language/English correspondence, scope, or argument structure, it should proactively register the issue and ask the human author for confirmation rather than silently selecting an interpretation and implementing it. Human confirmations or corrections should be promoted into the relevant foundational Core / Decision Log and then propagated into argument structure and final artifacts. This layer should especially protect issues whose misinterpretation would materially alter the second-layer framework or central expression.

**Architectural decision:** use a `Critical Clarification Register` positioned as a **Layer 1.5 bridge** between Layer 1 and Layer 2. Open entries are not human commitments; resolved entries require Resolution Promotion.

**Affected components:** Protocol Core, Specification, AGENTS, Architecture, project template, methodology article governance, framework review workflow

**Status:** implemented.

---

## 2026-09-18 — HARC-D018

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** HARC should provide an explicit pre-work bootstrap entry and prompt mechanism for any AI Agent taking over from zero context, so the Agent can immediately understand project layers, read order, clarification governance, Framework/Artifact state, and required propagation workflow. Before substantive work, the Agent should complete an onboarding handshake and report the current state reconstructed from the repository. The project should provide a human-readable start file, copyable bootstrap prompt, agent contract, and machine-readable manifest to reduce discovery differences across AI platforms.

**Qualification:** repository files cannot technically guarantee that every external AI platform automatically reads a particular filename. HARC's conformance target is maximal entry-point discoverability plus an Onboarding Report that verifies the Agent actually reconstructed and follows the workflow.

**Affected components:** START_HERE, HARC_MANIFEST, AGENTS, README, Specification, Persistent Memory, project templates, agent handoff

**Subsequent human confirmation:** the human project founder explicitly confirmed that the above understanding was substantially accurate and instructed that it be formally implemented. This ratifies the zero-context bootstrap, standalone startup prompt, manifest, Onboarding Handshake, and Onboarding Report as formal HARC protocol components.

**Status:** human-confirmed and implemented.

---

## 2026-09-18 — HARC-D019

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** After a replacement AI Agent reads the GitHub repository and completes onboarding, it should further compress key HARC rules and current project state into a session-level operating contract and explicitly write that contract into its own current reply, so the rules re-enter the active conversation context. This creates a two-layer safeguard: durable repository state plus an active session contract. The mechanism should refresh after major state changes or suspected context loss.

**Qualification:** this must not be represented as promoting repository content into the platform's true system prompt or as modifying model weights, hidden memory, or platform-level memory. Platform system/developer/safety instructions remain higher priority than the HARC Session Contract.

**Implementation:** add `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` / English mirror and connect it to START_HERE, Bootstrap Prompt, Manifest, Onboarding Report, Agent contract, and project templates.

**Status:** human-confirmed and implemented.

---

## 2026-09-18 — HARC-D020

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:** HARC should further treat GitHub directly as the AI Agent's authoritative external memory and working-state store. The Agent does not need to maintain a long-lived duplicate project-state mirror in chat context; it should retrieve the latest canonical files from GitHub on demand for the current task, and all updates that should constrain future work should be written directly back to GitHub. Model context retains only a minimal access kernel and task-relevant transient cache.

**Interface principle:**

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

After a write, old context copies become stale; before high-impact judgments or writes, latest revisions must be reconfirmed. Direct GitHub API, MCP, connector/plugin, or equivalent tool access is preferred for on-demand reads and write-through updates.

**Revision to HARC-D019 / P21:** the Active Session Contract no longer carries a dynamic project-state copy. It is narrowed to a Repository Resolver / access kernel. Dynamic Blocking Clarifications, Framework, Artifact, and Core state are fetched from the latest repository version when needed.

**Implementation:** add `protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md`, its English mirror, and machine-readable `HARC_CONTEXT_INTERFACE.yaml`, and connect them to startup, manifests, agent contracts, and project templates.

**Status:** human-confirmed and implemented.

---

## 2026-09-18 — HARC-D021

**Source:** Human project founder  
**Classification:** PROTOCOL, CONTENT

**Decision:** Retire the former “Layer 1.5 / Critical Clarification Layer” model. HARC should distinguish three layers of **Long-Term Research Memory** from a parallel **Working Memory**.

The three long-term layers are:

1. Layer 1 — Human Authorial Core: progressively accumulated, corrected, and refined human core commitments;
2. Layer 2 — Current Framework: core propositions, key concepts, argument structure, and inferential relations based on Layer 1; durable but more revisable and able to contain structural material not stated item-by-item in Layer 1;
3. Layer 3 — Derived Artifact: the complete artifact expanded primarily from Layer 2.

Working Memory is parallel to all three and records current stage, work objective, overall plan, active tasks, completed/uncompleted work, next actions, TODOs, blockers, pending human decisions, clarifications, synchronization defects, and handoff information.

Clarification is an item type inside Working Memory, not an independent layer. After human resolution, the normative result is promoted into the appropriate long-term memory destination; the Working Memory item leaves active state and retains only resolved/promoted pointers and audit trace.

**Affected components:** Protocol Core, Persistent Memory, Architecture, clarification workflow, Working Memory, Onboarding/Handoff, Manifest, Context Interface, Specification, AGENTS, project templates, methodology article

**Status:** implemented.

---

## 2026-09-18 — HARC-D022

**Source:** Human project founder  
**Classification:** PROTOCOL, CONTENT

**Decision:** Working Memory should not be fixed as a single document. It should be defined as a functional area that may use one or multiple files according to engineering needs. Its core logical functions include at least:

1. `Current Focus` — the most immediate, highest-priority work objective;
2. `Task Plan` — the dynamic task and planning list;
3. `Work Log` — a stage-level historical record primarily for later human review.

Completed Task Plan items leave the active list and are summarized into Work Log; if they create stable normative results, those results must also be promoted into appropriate Long-Term Memory.

Work Log should be updated periodically to preserve broad progress, changes in intellectual/work direction, and milestones, but it is not default required reading for AI onboarding. It primarily serves the human author's later retrospective review. AI retrieves it on demand for historical review, audit, or conflict reconstruction.

Current Focus should remain the shortest and highest-salience component so a replacement Agent can immediately determine what matters most after interruption.

**Implementation principle:** logical roles are fixed; physical file layout is adaptable; the manifest maps roles explicitly.

**Status:** confirmed and implemented.


---

## 2026-09-18 — HARC-D023

**Source:** human project founder  
**Classification:** CONTENT, PROTOCOL

**Decision:** HARC adopts the following principles for human responsibility in AI-assisted research and creation:

1. The purpose, central problem, and direction of a research or creative project should originate with humans and remain under human initiation, navigation, and approval; humans bear the core responsibility for the resulting work.
2. AI Agents participate in HARC as tools. They may perform or assist with extensive search, synthesis, structuring, drafting, restructuring, checking, formatting, and related work, but the protocol and methodology article should not characterize AI as a cognitive subject or use “AI performs cognitive labor / cognitive tasks” as normative language.
3. For long-form work, the Layer 2 Current / Approved Framework is the primary structural carrier of human intellectual responsibility. Before Framework Approval, the human author must clearly understand, carefully review, and explicitly confirm every substantive element actually represented in the framework, including core theses, inferential relations, key distinctions, scope conditions, section/chapter functions, and any specific wording included in the framework.
4. AI may help organize and express a framework, but an approved version must genuinely represent the human author’s core ideas and endorsed positions. The human is responsible for the originality, understanding, judgment, and intellectual commitments carried by that framework. This does not remove Final Artifact Approval or any venue-, discipline-, institution-, or research-integrity requirements applicable to the final work.
5. `responsibility concentration` is not retained as the current central term. The responsibility model should instead be expressed descriptively in terms such as human purpose/direction and the framework as a responsibility anchor, without forcing a new single coined term.
6. Treating an Approved Framework as a possible submission attachment in future human–AI scholarly norms remains a possible development direction, not a current mandatory HARC protocol requirement.

**Affected components:** Protocol Core, Specification, research-project templates, README, methodology-article Content Core / Working Argument Map / Derived Artifact, Framework Status, Working Memory

**Clarifications resolved:** `CLR-001`, `CLR-002`, `CLR-005`

**Status:** confirmed; Promotion and bilingual propagation implemented in this work cycle.


---

## 2026-09-18 — HARC-D024

**Source:** human project founder  
**Classification:** CONTENT, FORM, PROTOCOL

**Decision:**

1. The Chinese methodology-article title **“从对话到持久研究状态：AI时代的人机研究协作、人类责任与可审计作者性”** is explicitly human-approved. The English title is maintained as a synchronized translation mirror of the Chinese canonical title. Approval of the title does not constitute Framework Approval of the complete Working Framework.
2. HARC-D023's responsibility language is further clarified: `human responsibility / 人类责任` should not be treated as a self-sufficient central concept requiring no explanation. The more precise core claim is: **humans remain the bearers of responsibility**.
3. In research and inquiry, especially when research results, arguments, or knowledge claims enter public knowledge dissemination through papers, books, reports, or other forms, humans must remain the responsibility-bearing subjects. AI Agents may act as tools and perform or assist extensive work, but they cannot become the bearers of ultimate responsibility for project purpose, core judgment, framework authorization, or public dissemination of knowledge claims.
4. “Human responsibility” may remain as shorthand in titles or general exposition, but theoretical definitions, protocol rules, and key arguments should make explicit that it means humans remain the bearers of responsibility.
5. All other confirmed elements of HARC-D023 remain in force.

**Relation:** this decision clarifies HARC-D023 without rescinding its other contents.

**Affected components:** Article Form Core, Article Content Core, Working Argument Map, methodology article, Protocol Core, Framework Approval, Specification, README, Agent contracts/templates, Framework Status, Working Memory

**Status:** confirmed; bilingual Promotion and propagation implemented in this work cycle.


---

## 2026-09-18 — HARC-D025

**Source:** human project founder  
**Classification:** CONTENT, PROTOCOL

**Decision:**

1. Approve a structural repair to the methodology article Working Framework dependency graph so that T9–T13 are properly represented as supporting the governance, continuity, and executability relations around T1/T2/T7/T8, and so that the T3 node name is synchronized to “AI Tool Work / Humans as Bearers of Responsibility.”
2. Framework Approval may include items explicitly marked `AI-PROPOSED`, `UNRESOLVED`, `NON-BLOCKING`, or equivalent, but **overall approval approves only their place, scope, and treatment as unresolved/provisional items within the framework; it does not automatically approve their substantive content**.
3. Therefore, an overall `APPROVE` decision on a framework containing explicit unresolved items MUST NOT promote provisional terminology, empirical plans, theoretical positioning, or other AI proposals into human-originated or human-confirmed commitments. Only a later separate human decision may change their provenance/approval status.
4. This decision is not overall Framework Approval of the current complete Working Framework and MUST NOT by itself trigger creation of `MA-FW-001`.

**Affected components:** Working Argument Map dependency structure; Framework Approval protocol; Framework Status; Working Memory.

**Status:** confirmed; bilingual propagation implemented.


---

## 2026-09-19 — AHICP-D026

**Source:** human project founder  
**Classification:** PROTOCOL, CONTENT, FORM

**Decision:**

1. The former **Human–AI Research Collaboration Protocol (HARC)** formally migrates to **AI-Assisted Human Inquiry and Creation Protocol (AHICP)**.
2. The fixed subtitle is: **A protocol for human-led inquiry, research, reasoning, writing, and creation with AI assistance.**
3. The normative direction is explicitly **human-led, AI-assisted, repository-grounded**.
4. AI is not normatively characterized as a cognitive subject, an intellectual-labor subject, or an ultimate bearer of responsibility symmetric with the human. AI may perform or assist extensive retrieval, comparison, structuring, proposal generation, drafting, verification, transformation, and repository maintenance; human purpose, direction, substantive judgment, approval, and ultimate responsibility remain non-transferable.
5. The protocol generalizes from research as its primary default setting to inquiry / research / reasoning / writing / creation. Text genuinely specific to research evidence, research integrity, scholarly articles, or research policy may remain research-specific and must not be mechanically generalized.
6. The mature governance architecture from HARC v0.2.x is inherited; the migration target is **AHICP v0.3.0-draft**.
7. Historical decision IDs (for example HARC-D001–HARC-D025) remain unchanged as audit identifiers; new decisions use the AHICP prefix beginning with this entry.
8. AHICP remains separate from the **Personal Publishing Framework (PPF)**: AHICP governs AI assistance in human inquiry and creation; PPF governs the source / build / publish / release / archive lifecycle. They may be adopted independently or together.

**Status:** explicitly human-confirmed; propagation is in progress on the v0.3 semantic-migration branch.

---

## 2026-09-19 — AHICP-D027

**Source:** Human project founder  
**Classification:** PROTOCOL

**Decision:**

1. AHICP formally adopts general **External Systems, Tool Discovery, Authorization, and Human Handoff** governance.
2. When work requires an external system, account, or service and appropriate human authorization already exists, an AI Agent should first safely discover and exhaust currently available and authorized machine-operable paths before returning routine operational steps to the human.
3. Discovery should cover platform built-in tools, connected plugins/connectors, official MCP servers, provider APIs, official GitHub Apps/integrations, existing repository automation, and explicitly approved adapters/plugins.
4. “Installed / enabled / connected” does not prove that a capability is actually callable. When capability status affects the execution route or a decision to escalate to a human, it must be verified through a real minimal invocation when technically possible and safe.
5. Where functionally equivalent, official, OAuth, provider-managed, least-secret-handling connections are preferred. Humans must not be asked to paste passwords, tokens, private keys, or other secrets into chat for convenience.
6. Human escalation is reserved for identity authorization, account-owner consent, permission grants, non-delegable high-impact decisions, or actions that currently authorized tools genuinely cannot perform. Human handoff must use the fewest steps, request only the necessary current action, assume no technical background, and identify values that must not be sent to AI.
7. After the necessary human action, the AI Agent should re-read the repository, re-verify capability/provider actual state, and resume later machine-operable work.
8. External operations that affect future project work must be followed by verification of actual provider state and write-back of the verified durable result to the repository. Provider UI, chat state, and model memory must not become a parallel authoritative project-state source.
9. This is provider-neutral AHICP execution/escalation governance. It does not place Cloudflare or any other specific provider in the normative core and does not change the publishing-lifecycle boundary owned by PPF.

**Affected components:** Protocol Core, Specification, AGENTS, research-project template, future adoption/conformance audits.

**Status:** explicitly requested for execution by the human; this decision authorizes the current normative propagation.

---

## 2026-09-20 — AHICP-D028

**Source:** human project founder  
**Classification:** PROTOCOL

**Decision:**

1. When a project first configures an integration, automation, or workflow whose later machine actions will rely on a reusable authorization policy, the AI Agent should first analyze the situation and propose suitable human authorization patterns; configuration that relies on the policy proceeds only after the human chooses.
2. The AI may recommend authorization patterns and explain their differences and scope, but **AI proposal != human authorization**. The Agent must not silently choose a default authorization mode for the human or first establish an authorization policy through configuration and then infer human authorization from the technical result.
3. Where applicable, the proposal should distinguish at least:
   - `per-action authorization`: the human confirms each action or state transition designated as requiring separate authorization;
   - `bounded pre-authorization`: the human approves a clearly bounded action-class / target / side-effect / duration scope in advance, within which the AI may act repeatedly;
   - `mixed policy`: selected low-risk actions may be pre-authorized while specified high-impact or human-reserved actions continue to require per-action human decisions.
4. The human may select, modify, or reject the AI proposal. The final choice, including its scope, authorization provenance, and escalation conditions, must be recorded in repository durable state before the AI relies on that policy for later configuration and machine operations.
5. If later actions exceed the selected action class, target, allowed side effects, or duration, or if impact / reversibility materially changes, renewed human selection or authorization is required.
6. This decision refines the authorization / human-handoff semantics of AHICP-D027 and authorizes propagation of this rule in current PR #3. It **does not constitute overall approval of the remaining AI-proposed normative content in PR #3 and does not authorize automatic merge**.

**Affected components:** Specification §23.5, Protocol Core P26, AGENTS, research-project template, Protocol Contract CI.

**Status:** this principle is explicitly human-confirmed and authorized for propagation in current PR #3.

---

## 2026-09-20 — AHICP-D029

**Source:** human project founder  
**Classification:** PROTOCOL

**Decision:**

1. The human project founder approves the normative direction and current substantive content of PR #3 on **scoped authorization for durable-state actions**, including:
   - `proposal != authorization != execution != verification != durable write-back`;
   - explicit modeling of authorization scope and provenance;
   - durability not being automatically equivalent to high impact;
   - a provider-neutral high-impact test;
   - avoiding unnecessary human escalation for authorized, low-risk, reversible machine operations;
   - the initial-configuration authorization-mode human-choice gate confirmed by AHICP-D028.
2. The human-reserved / non-delegable boundary remains: bounded pre-authorization must not override actions that governing rules explicitly reserve for human authorization.
3. The AHICP / PPF boundary remains unchanged: AHICP governs authorization provenance, scope, selection, escalation, execution/verification separation, and durable write-back; PPF or another publishing framework continues to own publication-lifecycle state semantics.
4. This decision authorizes moving PR #3 out of draft and merging it into `main` once Protocol Contract CI succeeds on the latest head and no new substantive conflict has appeared.
5. Merge completion, CI success, or any other machine-execution result does not itself create authorization. This human decision is the authorization provenance for the current normative promotion / merge.

**Affected components:** Specification §23.5, Protocol Core P26, AGENTS, research-project template, Decision Log, Protocol Contract CI.

**Status:** explicitly human-approved; authorized to complete PR #3 normative consolidation and merge after green CI.

---

## 2026-09-20 — AHICP-D030

**Source:** human project founder  
**Classification:** CONTENT, PROTOCOL, FORM

**Decision:**

1. The existing AHICP methodology article will continue to develop as **one unified paper** rather than being split into separate “protocol” and “memory” papers.
2. The paper is authorized for substantial structural revision so that the following become core theoretical contributions rather than peripheral implementation details:
   - **Project Memory Architecture:** the durable memory of a long-running human–AI project should belong to the project rather than depend on a particular model, Agent, chat, or platform memory;
   - **Working Memory as a continuity layer:** Working Memory is a persistent operational representation of the project's current epistemic/task state and a cross-session continuity layer, not human psychological working memory and not a model's hidden state;
   - **Agent / Model Substitution:** AI Agents and models should be replaceable while project purpose, evidence, decisions, current state, and next actions remain recoverable from the repository; substitution is an important stress test of the architecture;
   - **Human Decision Persistence:** human-confirmed, rejected, deferred, or authorized decisions are first-class project memory and must not collapse into unattributed text or become re-opened merely because a new Agent takes over.
3. The article should present AHICP memory as a **multi-role, layered, governable project-memory architecture**. In addition to the three Long-Term Research Memory layers and parallel Working Memory, it should discuss functional roles such as normative memory, epistemic/evidence memory, decision memory, operational memory, handoff memory, and publication/authorization memory. These are functional roles and need not map one-to-one onto physical files.
4. The article should explicitly distinguish **agent memory / conversational memory** from **project memory**. Existing agent-memory research largely asks how an Agent stores, retrieves, updates, and uses past information; AHICP asks how a long-running project can maintain authoritative state that is Agent-independent, inspectable, versionable, provenance-aware, and portable.
5. The paper must discuss:
   - inspectability / editability / versionability / provenance;
   - separation of evidence, inference, proposal, and human-confirmed decision;
   - stale state, conflicting memory, memory curation, selective retrieval, and memory growth;
   - Working Memory promotion / resolution / write-back;
   - privacy, unpublished material, and publication authorization as project-state boundaries;
   - how human responsibility, Framework Approval, and Final Artifact Approval connect to durable project memory.
6. The human project founder accepts inclusion of the previously discussed evaluation program in the same paper, including handoff/resumption tests, agent/model-substitution tests, decision-persistence tests, semantic-drift/fidelity tests, review-effort studies, and evaluation of memory curation/conflict handling. **These are currently proposed evaluation / research agenda items and must not be represented as completed empirical results.**
7. The article should engage current work on agent memory, long-term interactive memory, provenance, distributed cognition / extended mind, epistemic dependence, automation reliance, and authorship/accountability norms, without claiming that those literatures have already validated AHICP.
8. The existing title remains in place. This decision authorizes major structural rewriting of the Working Framework and DERIVED-PROVISIONAL article to implement the direction above. It **does not constitute overall Framework Approval of the rewritten complete framework and does not constitute Final Artifact Approval**.
9. Chinese remains the canonical scholarly draft and English the synchronized mirror; substantive structural changes in this work cycle must update both languages.
10. This decision changes the methodology article's content and structural direction only. It does not supersede `AHICP-D027`–`AHICP-D029` external-system, authorization, human-handoff, or scoped-authorization governance; those rules remain active for this project and future Agent operations.

**Affected components:** Article Content Core, Working Argument Map, Framework Status, methodology article, evidence layer, bibliography, Working Memory, Decision Log.

**Status:** explicitly human-confirmed; authorizes the current structural revision and article upgrade.

---

## 2026-09-21 — AHICP-D031

**Source:** human project founder  
**Classification:** CONTENT, FORM, GOVERNANCE

**Decision:**

1. The human project founder explicitly responded **“agree, complete it”** to the proposal to finish the methodology article Framework scholarly review and promote the content that survives current evidence and boundary constraints into the first Approved Framework snapshot.
2. Under that authorization and the completed 2026-09-21 scholarly review, the current methodology-article framework receives overall **Framework Approval** with snapshot identifier:
   - `MA-FW-001`
   - Chinese canonical: `paper/frameworks/MA-FW-001.zh-CN.md`
   - English mirror: `paper/frameworks/MA-FW-001.md`
3. T1–T13 enter `MA-FW-001` in their evidence-constrained / bounded wording:
   - T1 / T11: AHICP must not be presented as originating project memory, organizational memory, design rationale, decision provenance, or Agent long-term memory;
   - T2 / T3 / T7 / T8 / T13: approved as design principles or architecture specifications, not validated universal performance laws;
   - T4: Working Memory is explicitly not psychological working memory, model hidden state, scratchpad, or chain-of-thought;
   - T5: Human Decision Persistence is approved as a governance mechanism while acknowledging prior decision/rationale/provenance literature;
   - T6: Agent / Model Substitution is approved as a design goal and proposed stress test, not as an already validated robustness result;
   - T9: approved only as AHICP normative governance, not as a universal theory of authorship or cognitive responsibility across all domains;
   - T10: formally adopts **Framework Approval as a Structured Human-Review Gate and Responsibility Anchor**, replacing the approval-level use of “Compressed Responsibility Interface”;
   - T12: approved only as a proposed empirical research agenda, with no empirical results.
4. Framework Approval means human approval of the current intellectual architecture, argumentative boundaries, and research agenda. It does not mean every sentence of the current long-form article is finally approved or that citation/style requirements of a particular venue have been satisfied.
5. The article status should move from `DERIVED-PROVISIONAL` to:
   `DERIVED-FROM-MA-FW-001 — FINAL ARTIFACT APPROVAL PENDING`
6. `MA-FW-001` is the fixed approval baseline. Later substantive changes to core theses, argument structure, scope, or approval semantics should create a new framework snapshot rather than silently rewriting `MA-FW-001`.
7. This decision **does not constitute Final Artifact Approval, select a target venue, or automatically authorize PR merge / publication / release**. Those remain separate governance actions.
8. AHICP-D027–D030 remain active for external-system, authorization, human-handoff, scoped-authorization, and methodology structural-direction governance. D031 completes only the current methodology article Framework Approval.

**Affected components:** Methodology Article Framework snapshot, Working Argument Map, Framework Status, methodology article status, Working Memory, Methodology Article CI, Decision Log.

**Status:** explicitly human-approved; `MA-FW-001` Framework Approval completed.

---

## 2026-09-21 — AHICP-D032

**Source:** human project founder  
**Classification:** GOVERNANCE, FORM, PUBLICATION

**Decision:**

1. The human project founder explicitly approves interpreting **Framework Approval** as **bounded auto-merge authorization** for a dedicated PR that satisfies strict scope conditions.
2. That authorization applies only when all of the following are true:
   - the PR is dedicated to an approved Framework and its direct synchronization/governance implementation;
   - the PR contains no unauthorized substantive scope expansion beyond the approved scope;
   - any substantive change added after Framework Approval has separate explicit human authorization, or the change is only non-substantive follow-up such as validation, state synchronization, citation/format repair;
   - latest-head required CI / validation is green;
   - no unresolved blocking review / review thread exists;
   - the branch is not behind its base, or has been synchronized without unresolved conflict;
   - the merge does not bypass required provider-side protections, permissions, or explicit human-reserved gates.
3. When these conditions hold, no duplicate merge approval is required merely to write the same approved work into `main`. Framework Approval itself carries scoped merge authorization for that dedicated PR.
4. This rule does **not** allow Framework Approval to authorize unrelated features, deployments, external side effects, secret handling, publication/release, or other later unapproved scope added to the same PR.
5. For current PR #26, this human confirmation also explicitly approves:
   - the `MA-FW-001` Framework scope;
   - direct governance synchronization after Framework Approval;
   - the current target-venue review and recording/state propagation of this decision itself;
   therefore PR #26 may auto-merge under this rule once its latest-head diff contains no new unapproved substantive scope, CI is green, and no blocking review remains.
6. The human project founder also approves **Ethics and Information Technology** as the methodology article's current **primary target venue**.
7. **Science and Engineering Ethics** remains the current secondary candidate. AI & Society and Journal of Documentation are not current primary targets unless policy fit changes or the editorial office provides explicit compatible guidance.
8. Target-venue selection is not Final Artifact Approval and is not publication/submission authorization. Venue-specific manuscript preparation, AI-use disclosure, citation/style verification, and Final Artifact Approval remain required.
9. AHICP-D027–D031 remain active. This decision adds merge-authorization semantics and target-venue selection without superseding proposal / authorization / execution / verification / write-back separation.

**Affected components:** merge governance, Working Memory, Target Venue Review, methodology PR #26, Final Artifact preparation.

**Status:** explicitly human-approved.
