# Methodology Article — Content Core

> Chinese `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md` is canonical; this English file is its synchronized mirror. Every substantive change must update both versions.

**Role:** canonical human-originated substantive foundation for the AHICP methodology article.

This file contains only human-originated commitments that have been stated or clearly confirmed in the founding discussion. AI-generated terminology, stronger theses, literature interpretations, empirical research programs, and article structure remain outside this file until explicitly accepted by the human author.

## C1. The article must explain AHICP's methodological significance in research settings

The AHICP project should not only be an executable open protocol. It should also produce a methodology article that explains the project's ideas, architecture, and implications for human–AI research collaboration.

## C2. The article must address human purpose, direction, and responsibility-bearing status when AI tools participate

The article should treat humans as the source, initiator, and navigator of the purpose of a research or creative project. What problem the project is trying to solve, what direction it takes, and whether its core outcome is ultimately endorsed must be given, understood, and approved by humans.

“Human responsibility” should not be treated here as an unexplained abstract property. The more precise core claim is: **in human–AI collaborative research and inquiry, humans remain the bearers of responsibility.**

Within AHICP, an AI Agent is treated as a collaboration tool. It may perform or assist with extensive search, synthesis, structuring, drafting, revision, restructuring, checking, formatting, and related work. The article should not characterize AI as a cognitive subject or use “AI performs cognitive labor” or “AI performs cognitive tasks” as its central conceptual language.

The relevant question is instead which concrete work AI tools may perform or assist, and which acts of purpose-setting, understanding, judgment, confirmation, and responsibility must be borne by humans as the responsibility-bearing subjects.

## C3. The article must explain persistent repository-based collaboration

The article should explain why durable research state should be externalized into GitHub repository documents rather than depend on one AI agent, platform memory, account context, or chat window.

## C4. The article must explain the separation of human intention, AI representation, and derived text

It should explain the Content Core / Form Core / Decision Log / Working Framework / Approved Framework / Derived Artifact architecture and why AI expansion must remain subordinate to human-confirmed upstream state.

## C5. The article must explain humans as the responsibility-bearing subjects at the framework layer

For long-form work, the Layer 2 Current / Approved Framework is the primary structural carrier of core intellectual responsibility borne by humans.

Before Framework Approval, the human author must form a clear and complete understanding of every substantive element actually represented in the framework, and must carefully review and explicitly confirm those elements item by item. This includes at least the core theses, inferential relations, key distinctions, scope conditions, section/chapter functions, and any specific wording included in the framework.

AI may assist in proposing, organizing, and expressing the framework, but the approved version must genuinely represent the human author’s core ideas and endorsed positions. Humans bear responsibility for the originality, understanding, judgment, and intellectual commitments carried by that framework; AI cannot become the bearer of this responsibility.

The article should still distinguish a framework-level defect already present in the approved architecture from a derived-expansion defect introduced only in later AI elaboration. Treating the framework as the primary intellectual responsibility anchor does not remove Final Artifact Approval or the factual-accuracy, research-integrity, and venue requirements that apply to the final work.

## C6. The article must explain two different approval gates

Framework Approval and Final Artifact Approval are distinct. Framework Approval concerns the intellectual architecture. Final Artifact Approval concerns the concrete release/submission version and must respect applicable scholarly, institutional, publisher, or venue requirements.

## C7. The approved framework should be represented in the reader-facing overview

The human-confirmed intellectual structure should be meaningfully reflected in the final work's abstract, introduction, opening overview, book introduction/roadmap, or analogous reader-facing section so that the public-facing work remains structurally faithful to the framework the human actually approved.

## C8. AI agents should be replaceable while project state remains durable

The methodology should explain that long-term research continuity should reside in human-governed, explicit repository state rather than in the private context of one particular AI agent. A competent replacement agent should be able to reconstruct the active project from the repository without requiring the original chat history.

## C9. The protocol must be practically implementable and reusable

The AHICP project is not intended as a purely abstract philosophical proposal. Its file hierarchy, update rules, approval states, and templates should be concrete enough to instantiate in future research projects. The empirical research direction for evaluating AHICP is now human-confirmed through AHICP-D030, including handoff/resumption, Agent/Model substitution, decision persistence, semantic drift/framework fidelity, review effort, stale/conflict handling, and memory-curation/retrieval-efficiency. Specific benchmark implementations, samples, statistical designs, and effectiveness conclusions remain future research.

## C10. The article must not overstate unconfirmed AI proposals

`generation–verification asymmetry` and `semantic version control` remain explanatory, provisional AI-formulated labels rather than established field-standard terms. AHICP-D030 explicitly accepts inclusion of an empirical evaluation framework in the paper, while specific benchmark implementations, metric details, and any effectiveness conclusions remain unconfirmed until actually studied.

`responsibility concentration` has been explicitly rejected by the human as the current central term. Future drafts should use descriptive language such as human purpose and direction and the framework as a responsibility anchor, unless the human later adopts a new central term.

## C11. High-impact uncertainty should be managed as Clarification items inside Working Memory

The article must explain that Clarification is not an independent “Layer 1.5” between Layers 1 and 2. It is an item type inside Working Memory.

When AI encounters non-trivial uncertainty about authorial intent, core claims, key concepts, scope, argument relations, section functions, or important terminology/translation that could materially change the argument structure, it should not guess. It should place the issue in the Working Memory Clarification queue and request human confirmation.

Open clarifications are not durable human commitments. After human confirmation or correction, the result must be promoted through the Decision Log into the appropriate Long-Term Memory destination and then propagated through Framework and Artifact as applicable.

This mechanism is especially important for key concepts in the author's primary language and their English correspondence.

## C12. Cross-agent handoff requires an explicit bootstrap entry and verifiable handshake

The article should explain that repository storage alone does not guarantee correct takeover. A new Agent should first read Working Memory to identify current stage, objective, tasks, blockers, pending decisions, and next actions, then selectively retrieve authoritative state from the three Long-Term Memory layers.

The mechanism does not assume every AI platform automatically reads the same filename. Instead, root-level entry files, an agent contract, a machine-readable manifest, and a human-copyable bootstrap prompt maximize cross-platform discoverability and make successful handoff observable and verifiable.

## C13. GitHub should serve as the authoritative external-memory and working-state interface

The article should explain that AHICP does not need to maintain a long-lived project-state copy in chat parallel to GitHub.

A more accurate architecture is:

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

A model still needs relevant information temporarily available for an individual response, but it should retrieve the minimum necessary state on demand from latest canonical GitHub revisions according to the current task.

The session retains only a minimal Repository Resolver. Working Memory and all three Long-Term Memory layers remain in GitHub: Working Memory supplies resumable operational state, while Layers 1/2/3 supply durable research state. None should be maintained as a second authoritative chat copy.

All state changes that should constrain future work write directly back to GitHub; after a write, older context copies become stale. Relevant latest revisions should be reconfirmed before high-impact judgments and writes.

This makes GitHub the cross-agent memory and working store, while model context is only a temporary projection of repository state for the current task.

## C14. The three Long-Term Research Memory layers should be distinguished from parallel Working Memory

The article should explicitly distinguish:

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

from parallel:

`Working Memory = current stage / goals / tasks / blockers / clarifications / TODO / handoff`

The three layers describe durable intellectual and artifact state; Working Memory describes the current position in the work process.

Layer 2 remains Long-Term Memory even though it is more revisable: it stores the current framework, core propositions, key concepts, and structure.

Human-resolved Working Memory content must be promoted into the appropriate long-term layer, after which Working Memory retains only status and pointers.

## C15. Working Memory should separate operational resume state from human retrospective history

The article should explain that Working Memory need not be one fixed document. It may be split into logical roles according to engineering needs.

At minimum distinguish:

- **Current Focus** — the highest-priority immediate objective and next action;
- **Task Plan** — dynamic tasks, TODOs, blockers, pending human decisions, Clarifications, and next actions;
- **Work Log** — a stage-level historical chronicle primarily for later human review.

Current Focus + Task Plan form the operational resume state required for cross-Agent takeover. Work Log instead preserves how the project reached its current position, how important directions changed, and which task batches were completed.

Work Log should not be default required context for ordinary AI onboarding and should not store hidden model chain-of-thought. Completed tasks should leave active Task Plan and receive appropriately granular historical summaries in Work Log; stable normative results still require Promotion into the appropriate Long-Term Memory destination.

This design separates “seamless continuation of work” from “later human review of the development of the project and the author's thought”.

## C16. Public dissemination of knowledge must retain human bearers of responsibility

When research, inquiry, arguments, or knowledge claims enter public circulation through papers, books, reports, presentations, websites, or other forms, humans must remain the bearers of responsibility.

AI Agents may participate as tools in search, organization, analytic assistance, drafting, expansion, checking, and presentation, but they cannot be treated as the bearers of ultimate responsibility for public knowledge dissemination.

This principle is operationalized through human authorization of project purpose and direction, Framework Approval, and Final Artifact Approval where applicable.

## C17. The article remains one unified paper with Project Memory Architecture as a core theoretical contribution

The methodology article will not be split into separate protocol and memory papers. The existing article should integrate AHICP protocol design, project-memory architecture, Working Memory, Agent substitution, human decision persistence, framework approval, and auditable authorship within one paper.

One central thesis is:

> **The durable memory of a long-running human–AI project should belong to the project, not to a particular model.**

“Belong to the project” is an engineering and governance claim: important project state should be stored in external state that humans can inspect, edit, version, and migrate rather than being available only through model-internal or platform-private memory.

## C18. Working Memory is a continuity layer, not psychological working memory or model hidden state

The article must define the conceptual boundary of AHICP Working Memory.

Working Memory is a persistent operational representation of the project's current epistemic and task state. It answers where the project is now, what problem is active, what should happen next, and which blockers / Clarifications / pending human decisions remain.

It is a cross-session / cross-Agent continuity layer, not:
- a simulation of human psychological working memory;
- model hidden state;
- chain-of-thought;
- the complete long-term archive.

Current Focus + Task Plan are the default resume state; Work Log supports selective historical review.

## C19. Human Decision Persistence is a first-class component of Project Memory

The article must treat human decision state as first-class project memory.

At minimum it should distinguish:
- PROPOSED: suggested by AI or another source but not accepted;
- CONFIRMED / APPROVED: explicitly confirmed by the human;
- REJECTED: explicitly rejected and not to be reopened merely because a new Agent takes over;
- DEFERRED / OPEN: intentionally left for later resolution;
- AUTHORIZED: permitted within an explicit scope for action or state transition.

Decision persistence does not prevent future revision. It requires future changes to preserve provenance, version, rationale, and renewed authorization rather than allowing Agent replacement to erase the decision history.

## C20. Agent / Model Substitution is an architectural stress test

The article must treat Agent / Model substitution as an important evaluation criterion for the AHICP project-memory architecture.

If the current Agent, current chat history, and platform-private memory are removed, a competent replacement Agent should be able to reconstruct through explicit entrypoints, Working Memory, Long-Term Memory, Decision Log, evidence, and the manifest:
- project purpose;
- current questions and scope;
- known evidence and important uncertainty;
- confirmed / rejected / open decisions;
- current framework / artifact state;
- active tasks, blockers, and next actions;
- privacy and publication-authorization boundaries.

Failure to recover this state should be treated as a persistence / onboarding defect rather than requiring the human to narrate the entire history again.

## C21. Project Memory should be described as a multi-role functional architecture with memory governance

The article should discuss functional project-memory roles including:
- normative memory;
- epistemic / evidence memory;
- decision memory;
- working / operational memory;
- handoff memory;
- publication / authorization memory.

These roles may map to one or multiple physical files; the model does not require one memory role per file.

The article must also address memory curation. A project should neither save everything nor inject its entire history into every model context. It should manage:
- active vs archived state;
- current vs stale state;
- conflicting memory;
- selective retrieval;
- summaries / indexes;
- promotion / write-back;
- history growth / memory bloat;
- privacy / disclosure boundaries.

## C22. The paper includes a proposed evaluation framework but must not fabricate results

The article should treat AHICP as an empirically testable design architecture and propose at least:
- zero-context handoff / resumption tests;
- agent/model substitution tests;
- decision-persistence tests;
- semantic-drift / framework-fidelity tests;
- review-effort studies;
- stale/conflict-handling tests;
- memory-curation / retrieval-efficiency tests.

These are currently research designs and future empirical work. Unless experiments have actually been executed and recorded, the article must not claim that AHICP has been proven to improve accuracy, completeness, efficiency, research integrity, or review burden.

AHICP-D030 makes inclusion of this evaluation framework a human-confirmed article direction; specific benchmarks, samples, statistical methods, and conclusions still require future research design and actual data.

## Current unresolved authorial decisions

Current resume state is maintained through Working Memory Index, Current Focus, and Task Plan; active high-impact unresolved issues live in `docs/working-memory/task-plan.zh-CN.md`. Work Log primarily serves human retrospective review.

`CLR-001`, `CLR-002`, and `CLR-005` were resolved and promoted through HARC-D023. The main article-related Clarifications still pending are `CLR-003`, `CLR-004`, `CLR-006`, `CLR-007`, and `CLR-008`; `CLR-010` continues to constrain final submission/publication form rather than current Framework Approval readiness.

## Provenance correction

A prior version treated an explicit empirical testing program as if it were already part of the human-originated article foundation. That was too strong at the time; it was then an AI-developed extension. AHICP-D030 changes that status: the human founder has now explicitly accepted handoff/resumption, Agent/Model substitution, decision persistence, semantic drift/framework fidelity, review effort, stale/conflict handling, and memory-curation/retrieval-efficiency as a proposed evaluation framework within the same paper. This confirms that these questions should be studied; it does not create empirical results or pre-approve specific benchmark implementations, samples, statistical methods, or effectiveness conclusions.

## Status

Human-originated article foundation represented through the current founding discussion. Working article structure remains unapproved.