# HARC Protocol Core

## Purpose

This file records the active human-originated design commitments that define the Human–AI Research Collaboration Protocol project itself.

It is the project's semantic source of truth for what HARC is intended to achieve. AI elaborations may extend these ideas, but should not silently replace them.

---

## P1. GitHub-centered persistent collaboration

The protocol should support sustained collaboration among a human author, GitHub, and one or more AI agents.

Important project state should be explicitly stored in repository documents rather than depending on the memory or conversation context of one particular AI platform or agent.

The initial protocol targets GitHub. Other platforms may be considered later.

## P2. Human-originated substantive thought must be preserved separately

During discussion, the human author will express, correct, accept, reject, qualify, and develop substantive ideas.

Durable human decisions about the research topic should be extracted and persisted into a foundational content document.

AI-generated expansion must not silently contradict or replace this human foundation.

## P3. Form/presentation intention must be separated from research content

Human instructions about typography, layout, visual design, citation presentation, writing format, artifact type, and other presentation concerns are distinct from substantive research claims.

They should therefore be stored in a separate form/presentation source of truth.

Reusable author preferences may be inherited by future projects where appropriate.

## P4. AI should maintain a compact operational representation of the argument

A second-level document should represent the actual structure of a paper, book, or other research work in a compressed, inspectable form.

This operational representation should contain the major claims, relationships, section/chapter functions, distinctions, and unresolved issues.

It should become the principal discussion interface between the human and AI for large projects, rather than requiring repeated rereading of the entire expanded artifact.

## P5. Human feedback must propagate upstream first

When the human author makes a substantive correction or decision, the AI agent should first persist the human decision in the appropriate foundational document, then update the operational representation, and only then propagate the change into the final expanded artifact.

## P6. The operational framework can become a human-confirmed responsibility anchor

The AI-maintained working framework is not automatically human-endorsed.

Once a version has been explicitly read and confirmed by the human author, it should be preserved as a versioned approved framework.

For long works, human substantive attention can concentrate on this compressed intellectual architecture: central claims, inferential relations, key distinctions, and section/chapter roles.

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

HARC should exist as an independent open project, not depend on any one research topic, and provide reusable specifications and templates for new papers, books, articles, reports, and sustained intellectual projects.

A future AI agent should be able to inspect this repository and instantiate a topic-appropriate project structure that follows the same collaboration logic.

## P12. The protocol should make human–AI contribution boundaries explicit

The system should distinguish at least:

- human intellectual intention;
- human presentation intention;
- AI operational representation;
- AI-assisted derived expression;
- evidence constraints;
- approval state;
- historical decisions.

The purpose is not to hide AI assistance, but to make the collaboration auditable and intellectually governable.

## P13. Framework-level responsibility and expansion-level defects should be distinguished

The human-approved framework is intended to be the primary substantive intellectual responsibility anchor in long-form collaboration.

A defect in a thesis, inferential relation, central distinction, scope condition, or section/chapter role that is present in an explicitly approved framework is a framework-level defect in the human-confirmed intellectual architecture.

A defect introduced only during later AI expansion—such as weak wording, a poor transition, an unnecessary example, or another local implementation problem—should be distinguishable from a defect in the approved framework itself.

This distinction does not eliminate the separate final-artifact approval and public accountability requirements that may apply before publication or submission.

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

## P16. HARC should produce both an executable open project and a methodology article

HARC is intended to have two mutually supporting outputs:

1. an executable, reusable open collaboration protocol with specifications, templates, states, and governance rules;
2. a methodology article that explains the conceptual rationale of the protocol and develops its implications for research practice in the AI era.

The article should address, among other themes, human cognitive responsibility, the scope of delegable and non-delegable intellectual work, framework-level authorship, AI-assisted expansion, epistemic dependence, persistent external research memory, and the conditions under which human accountability remains meaningful.

The article is a scholarly derivative of the protocol and should itself be developed under HARC-style framework control rather than treated as an ungoverned explanatory essay.

## P17. Human cognitive responsibility should be concentrated, not erased

HARC should not treat AI capability as a reason to eliminate human judgment. Instead it should make the allocation of cognitive labor explicit.

AI agents may perform extensive search, synthesis, drafting, restructuring, checking, formatting, and other assistive work. Human responsibility should remain concentrated on the high-leverage judgments that define and authorize the project: research aims, core commitments, major inferential architecture, treatment of decisive evidence conflicts, framework approval, and release approval as required by the relevant context.

The protocol should therefore distinguish delegation of cognitive labor from delegation of epistemic responsibility.


## P19. High-impact uncertainty must enter the Clarification queue inside Working Memory

HARC no longer treats Critical Clarification as an independent “Layer 1.5” between Layers 1 and 2.

Clarification is a record type inside **Working Memory**.

When an AI Agent encounters non-trivial, high-impact uncertainty about authorial intent, core claims, key concepts, scope, inferential relations, section functions, key terminology, or source-language/English correspondence, it must not silently choose an interpretation and propagate it downstream.

The Agent should create a Clarification item in Working Memory with candidate interpretations, impact, severity, and the question requiring human resolution.

Open items are not long-term human commitments and may be marked `BLOCKING` or `NON-BLOCKING`.

After human resolution, perform Promotion:

`Working Memory -> Decision Log -> appropriate Long-Term Memory destination`

Human core content goes into Layer 1 Content Core and then propagates to Layer 2 Framework and Layer 3 Artifact; Form / Protocol decisions go to their corresponding durable Core; purely structural Framework decisions go to Layer 2.

After Promotion, the Working Memory entry leaves active state and retains only resolved/promoted pointers and audit information.

HARC should run a Working Memory / Clarification Scan before major phase transitions, Framework Approval, broad terminology propagation, formal translation, large-scale expansion, and Final Artifact Review.


## P20. Zero-context onboarding requires an explicit entry point and handshake

A HARC project should provide a **discoverable zero-context bootstrap entry** so that a new AI Agent with no old chat, platform memory, or prior project knowledge can reconstruct current research state in a deterministic order.

The entry should include at least:

- a root human/agent-readable `START_HERE` file;
- a root `AGENTS` contract;
- a machine-readable HARC manifest or equivalent index;
- an explicit mandatory read order;
- entry points for the Clarification Register, Framework Status, Working/Approved Framework, and Artifact status;
- a copyable bootstrap prompt for arbitrary AI agents.

Before substantive modification, a new AI Agent should complete an **Onboarding Handshake**: report protocol state, human-confirmed state, Form state, Blocking Clarifications, Framework/Artifact state, synchronization defects, and the permitted next action.

If the Agent cannot produce that report from repository state alone, the project has an onboarding/persistence defect that should be repaired before large-scale research or writing continues.

No protocol file can guarantee that every external platform automatically reads a particular filename. HARC therefore aims for **maximal discoverability plus verifiable onboarding** through root-level entry files, a general agent contract, a machine manifest, README navigation, and a copyable prompt, so that any repository-capable agent that follows project instructions can reconstruct the same workflow.


## P21. Session context should retain only a repository-access kernel, not a second authoritative project state

HARC durable state lives in the repository. After takeover, an AI Agent may retain a very small **Repository Resolver / Active Session Kernel** in the current conversation, but that kernel should contain only:

- that GitHub is the sole authoritative project-state source;
- where the manifest and context-interface are;
- Chinese-canonical / English-mirror priority;
- the current CONTENT / FORM / PROTOCOL route;
- when repository state must be refetched;
- how stale cache is invalidated after writes.

It should **not maintain long-lived copies** of Blocking Clarifications, Framework state, Artifact state, Core content, or other dynamic research state.

Dynamic state should be fetched on demand from the latest canonical GitHub revision. Earlier Onboarding Reports, session summaries, file excerpts, and model memory are non-authoritative cache.

Correct precedence is:

`Platform system/developer rules > HARC repository access kernel > ordinary task-level AI defaults`

This does not promote repository files into a true platform system prompt or claim to modify model weights or platform memory.



## P22. GitHub should serve as the authoritative external-context and working-state interface

HARC should support a **Repository-Backed Context Interface**:

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

A model still needs relevant information temporarily available during an inference, but it should not maintain a parallel long-lived authoritative copy of GitHub state.

Each substantive task should use:

`Resolve -> Fetch latest -> Reason -> Act -> Write-through -> Invalidate stale cache -> Refresh if needed`

Updates that must constrain future Agents are written only to GitHub; any session copy becomes stale immediately after repository changes.

Before high-impact judgments or writes, the Agent should reconfirm the latest revision of relevant canonical files. It should prefer direct GitHub API, MCP, connector/plugin, or equivalent tool access rather than requiring humans to paste repository content into chat.

HARC should provide a machine-readable context-interface manifest describing task routing, revision policy, cache invalidation, write-through behavior, and trust boundaries.


## P23. The three long-term memory layers must be distinguished from parallel Working Memory

HARC core research state uses three long-term memory layers:

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

- Layer 1 stores the human author's progressively expressed, corrected, confirmed, and refined foundations;
- Layer 2 is based on Layer 1 and stores the current argument framework, core propositions, key concepts, and reasoning structure; it is durable but more revisable;
- Layer 3 is primarily expanded from Layer 2 into the complete artifact while remaining constrained by Layer 1 and evidence.

Parallel to these layers, a project must maintain **Working Memory**.

Working Memory stores current stage, objective, plan, active tasks, completed work, next actions, TODOs, blockers, pending human decisions, clarifications, synchronization defects, and handoff notes.

Its purpose is to let any replacement human collaborator or AI Agent answer quickly:

> “Where is the project now, and where should work resume?”

It is not a fourth long-term semantic layer and must not replace durable truth sources.

Stable confirmed content in Working Memory must be promoted into the appropriate long-term memory destination. After Promotion, Working Memory retains only status, Decision ID, and destination pointers.

---

## Current scope

HARC v0.2 focuses on:

`Human Author + GitHub Repository + AI Agent(s)`

for sustained research and intellectual development.

Broader platform support is outside the initial scope.

## P18. Chinese is the canonical language; English is a synchronized mirror

All substantive HARC project documents should exist in Chinese and English.

The Chinese version is the **canonical source of meaning and editing authority**. Human review, correction, confirmation, and substantive editing are based on the Chinese version unless the human explicitly decides otherwise for a specific artifact.

The English version is a **synchronized translation mirror**. Any substantive edit to the Chinese canonical version must be propagated to the English counterpart in the same work cycle. An edit is not complete while the two language versions are materially out of sync.

If the Chinese and English versions conflict, the Chinese version governs and the English version must be repaired.

New substantive Markdown documents should be created as bilingual pairs from the beginning. Machine-neutral files such as BibTeX, schemas, source data, or code need not be duplicated merely for language, but their human-readable documentation should be bilingual.

The repository should make language status and canonical precedence discoverable to new AI agents.

For bilingual files that existed before the rule was established on 2026-09-18, if the English version had historically developed newer substantive content not yet absorbed by Chinese, perform a one-time legacy catch-up first: incorporate those English developments into Chinese so that Chinese represents the genuinely latest semantic state at cutover, then resynchronize English as the mirror. Canonical cutover is complete only after this reconciliation.

After canonical cutover, the normal substantive development direction is fixed as: `human decision -> Chinese canonical -> English synchronized mirror`. English must not continue as an independent substantive development branch.
