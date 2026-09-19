# AHICP Protocol Core

## Purpose

This file records the active human-originated design commitments that define the AI-Assisted Human Inquiry and Creation Protocol (AHICP) project itself.

It is the project's semantic source of truth for what AHICP is intended to achieve. AI elaborations may extend these ideas, but should not silently replace them.

---

## P1. GitHub-centered durable project state and AI assistance

The protocol should support sustained human inquiry and creation on top of a durable repository such as GitHub, with assistance from one or more replaceable AI agents.

Important project state should be explicitly stored in repository documents rather than depending on the memory or conversation context of one particular AI platform or agent.

The initial protocol targets GitHub. Other platforms may be considered later.

## P2. Human-originated substantive thought must be preserved separately

During discussion, the human author will express, correct, accept, reject, qualify, and develop substantive ideas.

Durable human decisions about the project's substantive content should be extracted and persisted into a foundational content document.

AI-generated expansion must not silently contradict or replace this human foundation.

## P3. Form/presentation intention must be separated from substantive content

Human instructions about typography, layout, visual design, citation presentation, writing format, artifact type, and other presentation concerns are distinct from substantive content decisions.

They should therefore be stored in a separate form/presentation source of truth.

Reusable author preferences may be inherited by future projects where appropriate.

## P4. Layer 2 should preserve a durable but highly revisable operational framework

Layer 2 belongs to Long-Term Project Memory but is more revisable than Layer 1. It should represent the current structure of a paper, book, creative work, or other artifact in a compact, inspectable form.

This layer should contain core propositions, key concepts, inferential relations, section/chapter functions, conceptual distinctions, and current structural state.

Layer 2 must remain constrained by the Layer 1 Human Authorial Core while it may contain structural material not stated item-by-item in Layer 1 but necessary for developing the project.

For large projects, it should be the primary human–AI interface for structural discussion. Working Frameworks / Argument Maps and Approved Framework snapshots may serve as different approval states or project-type instances within this long-term layer.

## P5. Human feedback must propagate upstream first

When the human author makes a substantive correction or decision, the AI agent should first persist the human decision in the appropriate foundational document, then update the operational representation, and only then propagate the change into the final expanded artifact.

## P6. The operational framework can become a human-confirmed responsibility anchor

The AI-maintained Working Framework is not automatically human-endorsed.

Once a version has been explicitly read and confirmed by the human author, it should be preserved as a versioned Approved Framework.

For long works, the Approved Framework is the primary structural anchor of human intellectual responsibility. Before approval, the human author must clearly understand, review item by item, and confirm every substantive element actually represented in the framework, including central claims, inferential relations, key distinctions, scope conditions, section/chapter roles, and any specific wording included in the framework. AI may assist in organizing and expressing the framework, but the approved version must genuinely represent the intellectual structure the human understands and endorses.

## P7. The approved framework should be visible in the final work's overview

The core human-approved intellectual structure should be faithfully projected into the final artifact's reader-facing overview.

Typical mappings include:

- academic paper: abstract and introduction;
- article: opening/introductory overview;
- book: introduction/overview chapter and chapter roadmap.

## P8. AI may perform extensive expansion, but framework fidelity matters

After framework approval, AI agents may perform substantial elaboration, drafting, explanation, literature integration, and formatting.

Such expansion remains derivative of the approved human-governed structure and should not silently introduce material departures from it.

## P9. Project memory should be recoverable across agents

A new AI agent should be able to take over the project by reading repository state, without requiring the complete original conversation history.

The repository may accumulate long historical memory, while active canonical summaries remain compact enough for practical onboarding.

## P10. Context-window independence is achieved through externalized state, not infinite context

The protocol should reduce dependence on a single conversation window by storing durable project state in GitHub.

It should not assume an AI can load unlimited history at once. Large projects should use compact active state, logs, archives, indexes, and selective retrieval.

## P11. The protocol should be reusable and portable

AHICP should exist as an independent open project, not depend on any one research topic, and provide reusable specifications and templates for inquiry, research, papers, books, articles, reports, creative work, and other sustained projects.

A future AI agent should be able to inspect this repository and instantiate a topic-appropriate project structure that follows the same collaboration logic.

## P12. The protocol should make the boundary between human agency and AI assistance explicit

The system should distinguish at least:

- human intellectual intention;
- human presentation intention;
- AI operational representation;
- AI-assisted derived expression;
- evidence constraints;
- approval state;
- historical decisions.

The purpose is not to hide AI assistance, but to make that assistance auditable while keeping human purpose, judgment, approval, and responsibility explicit.

## P13. Framework-level responsibility and expansion-level defects should be distinguished

In long-form collaboration, the human-approved framework is the primary substantive intellectual responsibility anchor. Framework Approval means that the human has understood, reviewed, and confirmed every substantive element actually represented in that framework.

If a core claim, inferential relation, central distinction, scope condition, section role, or specific formulation included in the framework is already present in the explicitly approved framework, it is framework-level content within the human-confirmed intellectual architecture; a structural defect there is therefore a framework-level defect.

If a problem arises only in later AI expansion—for example weak wording, a poor transition, an unnecessary example, or another local implementation defect—it should be distinguishable from a defect in the framework itself.

This distinction does not remove any Final Artifact Approval, public-accountability, factual-accuracy, or research-integrity requirement that may apply before submission or publication.

## P14. Form preferences should support inheritance across author, artifact type, and project

The form system should be reusable rather than recreated from scratch in every project.

It should be possible to distinguish and combine:

- reusable author-level presentation preferences;
- artifact-type profiles, such as `BOOK`, `ACADEMIC_PAPER`, and `ARTICLE`;
- project-specific presentation decisions;
- external venue constraints;
- temporary AI/tool defaults.

A new project should identify its artifact type at initialization and inherit only preferences that are explicitly applicable. Unknown form decisions must remain unresolved rather than being invented by an AI agent.

## P15. Audits must be repair cycles, not passive reviews

When the project performs a multi-pass integration audit, each pass should be a complete cycle:

`review -> identify defects -> repair/implement -> verify the repair`.

A stated three-pass audit therefore means three successive review-and-repair cycles, not three readings followed by one repair stage.

After those cycles, the project should perform an additional independent post-repair audit to detect residual omissions, regressions, or inconsistencies.

## P16. AHICP should produce both an executable open project and a methodology article

AHICP has two mutually supporting outputs:

1. an executable and reusable open collaboration protocol, including specifications, templates, states, and governance rules;
2. a methodology article explaining the conceptual basis of the protocol and developing its significance for research practice in the AI era.

The article should address, among other themes, humans as the bearers of responsibility in research and inquiry, human authorization of research purpose and direction, the scope of work that AI tools may perform or assist, human intellectual responsibility at the framework layer, responsibility for public dissemination of knowledge, AI-assisted expansion, epistemic dependence, persistent external research memory, and the conditions under which human accountability remains meaningful.

The article is a scholarly derivative of the protocol and should itself be developed under AHICP-style framework control rather than treated as an ungoverned explanatory essay.

## P17. AI is an assistive tool; humans remain the bearers of project purpose, direction, and responsibility

AHICP treats an AI Agent as an assistive tool within human-led inquiry and creation, not as a participant that must be granted human-like cognitive-subject status or ultimate responsibility-bearing status. The protocol should not use “AI performs cognitive labor” or “AI performs cognitive tasks” as normative language. More precisely, AI may perform or assist with extensive search, synthesis, drafting, restructuring, checking, formatting, and related work.

The purpose, central problem, and direction of a research or creative project should originate with humans and remain under human initiation, navigation, or approval. AI capability to perform substantial work does not transfer the project's purpose, core judgments, or the position of ultimate responsibility to AI.

Accordingly, AHICP's shorthand “human responsibility” should be understood more precisely as follows: **in human–AI collaborative research and inquiry, humans remain the bearers of responsibility.** Especially when research results, arguments, or knowledge claims enter public circulation through papers, books, reports, websites, or other forms, the ultimate bearers of responsibility must remain human.

For long-form work, this responsibility-bearing status is operationalized primarily through the Layer 2 Current / Approved Framework: the human author must clearly understand, carefully review, and explicitly confirm the core theses, inferential relations, key distinctions, scope conditions, section/chapter functions, and specific formulations actually represented there. AI may help propose, organize, or express the framework, but it cannot replace human authorization of the project's direction and intellectual architecture or become the ultimate bearer of responsibility for it.

Framework Approval does not remove Final Artifact Approval; the concrete public version must still receive final human review and approval by human bearers of responsibility under applicable scholarly, institutional, publisher, venue, and research-integrity requirements.

## P18. Chinese is the canonical language; English is a synchronized mirror

All substantive AHICP project documents should exist in Chinese and English.

The Chinese version is the **canonical source of meaning and editing authority**. Human review, correction, confirmation, and substantive editing are based on the Chinese version unless the human explicitly decides otherwise for a specific artifact.

The English version is a **synchronized translation mirror**. Any substantive edit to the Chinese canonical version must be propagated to the English counterpart in the same work cycle. An edit is not complete while the two language versions are materially out of sync.

If the Chinese and English versions conflict, the Chinese version governs and the English version must be repaired.

New substantive Markdown documents should be created as bilingual pairs from the beginning. Machine-neutral files such as BibTeX, schemas, source data, or code need not be duplicated merely for language, but their human-readable documentation should be bilingual.

The repository should make language status and canonical precedence discoverable to new AI agents.

For bilingual files that existed before the rule was established on 2026-09-18, if the English version had historically developed newer substantive content not yet absorbed by Chinese, perform a one-time legacy catch-up first: incorporate those English developments into Chinese so that Chinese represents the genuinely latest semantic state at cutover, then resynchronize English as the mirror. Canonical cutover is complete only after this reconciliation.

After canonical cutover, the normal substantive development direction is fixed as: `human decision -> Chinese canonical -> English synchronized mirror`. English must not continue as an independent substantive development branch.

## P19. High-impact uncertainty must enter the Working Memory Clarification queue

AHICP no longer treats Critical Clarification as an independent “Layer 1.5” between Layer 1 and Layer 2.

A Clarification is an item type inside **Working Memory**.

When an AI Agent has non-trivial, high-impact uncertainty about authorial intention, a core claim, a key concept, scope, an inferential relation, section function, important terminology, or source-language / English correspondence, it MUST NOT silently choose one interpretation and propagate it downstream.

The Agent should record the uncertainty in the Working Memory Clarification area, including candidate interpretations, affected scope, severity, and the question requiring human confirmation.

An unresolved item is not a durable human commitment and may be marked `BLOCKING` or `NON-BLOCKING`.

After human confirmation or correction, the result MUST be promoted:

`Working Memory -> Decision Log -> appropriate Long-Term Memory destination`

If the result concerns human core content, it enters the Layer 1 Content Core and then propagates to the Layer 2 Framework and Layer 3 Artifact. Form / Protocol decisions enter the corresponding durable Core; purely structural Framework decisions enter Layer 2.

After Promotion, the Working Memory item leaves active state and retains only a resolved/promoted pointer and audit information.

AHICP SHOULD proactively perform a Working Memory / Clarification Scan before major stage transitions, Framework Approval, propagation of key terminology across an artifact, formal translation, large-scale chapter expansion, and Final Artifact Review.

## P20. Zero-context takeover requires an explicit entry point and onboarding handshake

An AHICP project SHOULD provide an **entry point discoverable from zero context** so that a new AI Agent can reconstruct current project state in a deterministic order without old chat history, platform memory, or prior project knowledge.

The entry point SHOULD include at least:

- a human/Agent-readable root `START_HERE` file;
- a root `AGENTS` contract;
- a machine-readable AHICP manifest or equivalent index;
- an explicit mandatory read order;
- Working Memory Index;
- Current Focus;
- Task Plan;
- entry points for Framework Status, Working/Approved Framework, and Artifact state;
- a bootstrap prompt that can be copied directly to an arbitrary AI Agent.

Before making substantive changes, a new AI Agent SHOULD complete an **Onboarding Handshake**. The report should state at least:

- the highest-priority current objective;
- primary blocker and immediate next action;
- active tasks and TODO / backlog;
- pending human decisions / Clarifications;
- Framework / Artifact status;
- synchronization defects;
- currently permitted and blocked next actions.

Work Log is not default required reading for zero-context takeover. It is read on demand only when the human requests historical review, during a dedicated audit, for direction-change reconstruction, or when current state conflicts with history.

If the Agent cannot produce this report from repository state alone, the project has an onboarding/persistence defect that should be repaired before large-scale inquiry, research, writing, or creation continues.

The protocol cannot guarantee that every external platform will automatically read a particular filename. AHICP therefore aims to **maximize discoverability and verifiable takeover** through visible root entry points, a generic Agent contract, a machine-readable manifest, README navigation, and a copyable prompt so that any repository-capable Agent willing to follow project instructions can reconstruct the same workflow.

## P21. Session context retains only a repository-access kernel, not a second authoritative project state

AHICP's durable state lives in the repository. After onboarding, a new AI Agent MAY retain a minimal **Repository Resolver / Active Session Kernel** in the current conversation context, limited to:

- GitHub is the sole authoritative project-state source;
- where the manifest and context interface are located;
- the precedence of Chinese canonical / English mirror;
- whether the current task routes through CONTENT / FORM / PROTOCOL;
- when repository state must be re-read;
- how stale cache is invalidated after writes.

The session kernel SHOULD NOT maintain long-lived copies of Current Focus, Task Plan, Framework state, Artifact state, Core content, or other dynamic project state.

Dynamic content should be fetched on demand from the latest canonical GitHub revision. Any earlier Onboarding Report, session summary, file excerpt, or model memory is only a non-authoritative cache.

The precedence is:

`Platform system/developer rules > AHICP repository access kernel > ordinary task-level AI defaults`

This mechanism does not promote repository files into the platform's true system prompt and does not claim to modify model parameters or platform memory.

## P22. GitHub should serve as the authoritative external context and working-state interface

AHICP SHOULD support a **Repository-Backed Context Interface**:

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

A model still needs to retrieve relevant information into transient context for a particular task, but it MUST NOT maintain a parallel long-term authoritative copy alongside GitHub.

Each substantive task should follow:

`Resolve -> Fetch latest -> Reason -> Act -> Write-through -> Invalidate stale cache -> Refresh if needed`

Updates that should constrain future Agents are written to GitHub. Session copies become stale immediately after repository writes.

Before high-impact judgments and writes, the Agent MUST reconfirm the latest revision of relevant canonical files. Direct GitHub API, MCP, connector/plugin, or equivalent repository access is preferred over asking the human to paste repository content into chat.

AHICP SHOULD provide a machine-readable context-interface manifest describing task routing, revision policy, cache invalidation, write-through, and trust boundaries.

## P23. Three layers of Long-Term Project Memory and parallel Working Memory must remain distinct

AHICP models core project state using three layers of Long-Term Project Memory:

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

- Layer 1 preserves the human author's evolving, corrected, confirmed, and refined substantive foundation.
- Layer 2 builds on Layer 1 and preserves the current operational framework, core claims/elements, key concepts, and structural relations. It is durable but more revisable.
- Layer 3 expands mainly from Layer 2 into the complete artifact while remaining constrained by Layer 1 and evidence.

In parallel with these three long-term layers, the project MUST maintain **Working Memory**.

Working Memory records current stage, objectives, plan, active tasks, completed work, next actions, TODOs, blockers, pending human decisions, clarifications, synchronization defects, and handoff notes.

Its purpose is to let any new human participant or AI Agent quickly answer:

> “Where is the project now, and where should work resume?”

Working Memory is not a fourth long-term semantic layer and MUST NOT become an alternative truth source for durable claims.

Stable confirmed results in Working Memory MUST be promoted to the appropriate Long-Term Memory destination. After Promotion, Working Memory keeps only status, Decision IDs, and destination pointers.

## P24. Working Memory is a functional area, not a mandatory single file

The normative object is a **set of Working Memory roles**, not one fixed physical document.

Depending on project scale, AI Agent performance, context cost, and workflow convenience, a project MAY implement Working Memory as one file or several files. Regardless of physical layout, it SHOULD provide at least three logical functions:

1. **Current Focus**
   - stores the most immediate, highest-priority objective;
   - states the current stage, current task, primary blocker, and immediate next action;
   - remains very short and is the highest-priority operational state during takeover.

2. **Task Plan**
   - stores dynamic plans, TODOs, active tasks, blocked/waiting-human items, backlog, and next actions;
   - completed tasks leave the active list;
   - new tasks are added as work develops;
   - completed work is compressed into Work Log, while durable normative results are also promoted to Long-Term Memory.

3. **Work Log**
   - stores stage-level historical summaries primarily for later human retrospective review;
   - records broad progress, important work/idea transitions, completed task batches, and milestones;
   - serves human retrospective review rather than default AI onboarding;
   - SHOULD be updated periodically, but SHOULD NOT be read in full merely to continue ordinary current work;
   - MAY be retrieved when the human requests historical review, when provenance or change history must be reconstructed, when current state conflicts with history, or during a dedicated audit.

Work Log MUST NOT store hidden model chain-of-thought, scratchpads, or unverifiable internal reasoning. It records only auditable project-level changes, expressed reasons, decisions, milestones, and high-level summaries.

Working Memory MAY provide a stable Index / Resolver that maps these logical roles to current physical files. A lightweight project may map several roles to one file; a complex project may split them.

Recommended resume order:

`Working Memory Index -> Current Focus -> Task Plan -> task-relevant Long-Term Memory`

Work Log is not part of the default required read chain.

---

## P25. External-system operations should use authority-bounded machine-operable-first escalation

When an AI Agent needs an external system, account, or service and appropriate human authorization already exists, it should first safely discover and verify available built-in tools, connectors/plugins, official MCP servers, provider APIs, official integrations, repository automation, and approved adapters before deciding that human handoff is necessary.

A tool being listed as installed / enabled / connected is not sufficient evidence that it is actually callable; when technically possible and safe, capability should be verified with a real minimal invocation.

The Agent must not ask a human to paste passwords, tokens, private keys, or other secrets into chat. Escalation to a human should be reserved for identity authorization, account-owner consent, permission grants, non-delegable high-impact decisions, or actions that currently available tool capabilities genuinely cannot perform. Handoff must be minimized, written for a nontechnical operator, and followed by the Agent resuming machine-operable work after the necessary authorization is completed.

For external actions that affect future work, the Agent should verify provider actual state and write the verified durable result back to the repository. Provider UI, chat state, and model memory must not become a parallel authoritative project-state source.


## P26. Authorization is scoped, impact-sensitive, and lifecycle-separated

AHICP must distinguish:

`proposal != authorization != execution != verification != durable write-back`.

Durable state is not automatically high-impact. An already-authorized, low-risk, reversible machine operation should not be escalated merely because it persists.

Where authorization boundaries matter, authority should be represented with enough scope to identify the action class, target, allowed side effects, reversibility / rollback assumptions, duration or occurrence bound, escalation conditions, and authorization provenance.

Authorization may derive from an explicit human decision or a durable human-approved pre-authorization policy, except where AHICP or project governance marks the action as human-reserved / non-delegable. Technical capability, provider state, repository state, successful execution, or upstream changes do not create human authorization.

High impact is determined by foreseeable effects on responsibility-bearing external commitments, access/security/identity/permission boundaries, canonical identity or public cutover, adopted governance authority, or irreversible / materially difficult-to-reverse state. Technical action names such as repository write, merge, deployment, email send, or API call are not authorization levels by themselves.

When first configuring an authorization policy that later operations will repeatedly rely on, the Agent should propose appropriate authorization patterns based on action class, target, side effects, reversibility, and high-impact boundaries; where applicable it should distinguish per-action authorization, bounded pre-authorization, and a mixed policy, with their scopes and escalation conditions. The AI may only propose; the human must select, modify, or reject the authorization mode, and the final choice, including its scope, authorization provenance, and escalation conditions, must be recorded in repository durable state before later operations rely on it.

Within a valid scope, the Agent may execute machine-operable work, verify actual state, and write the result back to durable repository state. If the action is non-delegable, falls outside scope, or materially changes the assumed impact or reversibility, the Agent must escalate only the authorization or judgment that is genuinely missing.

---

## Current scope

AHICP v0.3 currently focuses on:

`Human + durable repository + AI Agent(s)`

for sustained **human-led, AI-assisted inquiry, research, reasoning, writing, and creation**.

The current reference implementation uses GitHub as the authoritative external project-state source; future implementations may map the same logical roles to other platforms.

AHICP does not define publishing infrastructure. The source / build / publish / release / archive lifecycle belongs to the separate **Personal Publishing Framework (PPF)** or another compatible publishing framework.

