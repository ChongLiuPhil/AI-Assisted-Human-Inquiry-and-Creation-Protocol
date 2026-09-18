# Methodology Article — Content Core

> Chinese `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md` is canonical; this English file is its synchronized mirror. Every substantive change must update both versions.

**Role:** canonical human-originated substantive foundation for the HARC methodology article.

This file contains only human-originated commitments that have been stated or clearly confirmed in the founding discussion. AI-generated terminology, stronger theses, literature interpretations, empirical research programs, and article structure remain outside this file until explicitly accepted by the human author.

## C1. The article must explain HARC as a research-collaboration methodology

The HARC project should not only be an executable open protocol. It should also produce a methodology article that explains the project's ideas, architecture, and implications for human–AI research collaboration.

## C2. The article must address human cognitive responsibility in the AI era

The article should examine what human researchers remain responsible for when AI agents can perform substantial searching, structuring, drafting, revising, and other cognitive work.

It should distinguish what kinds of cognitive work may be delegated from what kinds of understanding, judgment, confirmation, and responsibility must still remain meaningfully human-governed.

## C3. The article must explain persistent repository-based collaboration

The article should explain why durable research state should be externalized into GitHub repository documents rather than depend on one AI agent, platform memory, account context, or chat window.

## C4. The article must explain the separation of human intention, AI representation, and derived text

It should explain the Content Core / Form Core / Decision Log / Working Framework / Approved Framework / Derived Artifact architecture and why AI expansion must remain subordinate to human-confirmed upstream state.

## C5. The article must explain framework-level human responsibility

For long works, the human-approved compact framework should function as a primary substantive intellectual responsibility anchor: the human author should understand and confirm core theses, inferential relations, key distinctions, and section/chapter roles.

The article should distinguish defects already present in that approved architecture from local defects introduced only during later AI expansion.

## C6. The article must explain two different approval gates

Framework Approval and Final Artifact Approval are distinct. Framework Approval concerns the intellectual architecture. Final Artifact Approval concerns the concrete release/submission version and must respect applicable scholarly, institutional, publisher, or venue requirements.

## C7. The approved framework should be represented in the reader-facing overview

The human-confirmed intellectual structure should be meaningfully reflected in the final work's abstract, introduction, opening overview, book introduction/roadmap, or analogous reader-facing section so that the public-facing work remains structurally faithful to the framework the human actually approved.

## C8. AI agents should be replaceable while project state remains durable

The methodology should explain that long-term research continuity should reside in human-governed, explicit repository state rather than in the private context of one particular AI agent. A competent replacement agent should be able to reconstruct the active project from the repository without requiring the original chat history.

## C9. The protocol must be practically implementable and reusable

The HARC project is not intended as a purely abstract philosophical proposal. Its file hierarchy, update rules, approval states, and templates should be concrete enough to instantiate in future research projects. The exact empirical benchmarking program for evaluating HARC is not yet a human-confirmed commitment.

## C10. The article must not overstate unconfirmed AI proposals

Terms and stronger claims such as `generation–verification asymmetry`, `semantic version control`, `responsibility concentration`, and a specific empirical test suite may be useful AI-generated formulations, but they remain provisional unless explicitly accepted by the human author.

## C11. High-impact uncertainty should be managed as Clarification items inside Working Memory

The article must explain that Clarification is not an independent “Layer 1.5” between Layers 1 and 2. It is an item type inside Working Memory.

When AI encounters non-trivial uncertainty about authorial intent, core claims, key concepts, scope, argument relations, section functions, or important terminology/translation that could materially change the argument structure, it should not guess. It should place the issue in the Working Memory Clarification queue and request human confirmation.

Open clarifications are not durable human commitments. After human confirmation or correction, the result must be promoted through the Decision Log into the appropriate Long-Term Memory destination and then propagated through Framework and Artifact as applicable.

This mechanism is especially important for key concepts in the author's primary language and their English correspondence.

## C12. Cross-agent handoff requires an explicit bootstrap entry and verifiable handshake

The article should explain that repository storage alone does not guarantee correct takeover. A new Agent should first read Working Memory to identify current stage, objective, tasks, blockers, pending decisions, and next actions, then selectively retrieve authoritative state from the three Long-Term Memory layers.

The mechanism does not assume every AI platform automatically reads the same filename. Instead, root-level entry files, an agent contract, a machine-readable manifest, and a human-copyable bootstrap prompt maximize cross-platform discoverability and make successful handoff observable and verifiable.

## C13. GitHub should serve as the authoritative external-memory and working-state interface

The article should explain that HARC does not need to maintain a long-lived project-state copy in chat parallel to GitHub.

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

## Current unresolved authorial decisions

Current resume state is maintained through Working Memory Index, Current Focus, and Task Plan; active high-impact unresolved issues live in `docs/working-memory/task-plan.zh-CN.md`. Work Log primarily serves human retrospective review. Article-related entries are currently `CLR-001` through `CLR-008`; `CLR-001`, `CLR-002`, and `CLR-005` are currently `BLOCKING` clarifications before Framework Approval.

## Provenance correction

A prior version treated an explicit empirical testing program (handoff tests, semantic-drift tests, framework-fidelity tests, review-effort tests, cross-model portability tests) as if it were already part of the human-originated article foundation. That was too strong. The human founder required HARC to be practically implementable and reusable; the specific empirical test program was an AI-developed extension and remains provisional unless accepted.

## Status

Human-originated article foundation represented through the current founding discussion. Working article structure remains unapproved.