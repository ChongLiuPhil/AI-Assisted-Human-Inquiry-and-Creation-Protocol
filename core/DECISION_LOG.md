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
