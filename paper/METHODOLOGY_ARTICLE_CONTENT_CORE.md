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

## C11. High-impact uncertainty must be explicitly submitted for human clarification

The article must explain HARC's Critical Clarification Layer: when AI has non-trivial uncertainty about authorial intent, core claims, key concepts, scope, inferential relations, section functions, or key terminology/translation that could materially change the argument structure, the AI should not guess. It should proactively register the issue in the Clarification Register and request human confirmation.

Open clarifications are not human commitments. After human confirmation or correction, the result should be promoted into the Decision Log and appropriate Core, then propagated into the Working Framework and final artifact.

This mechanism is especially important for core concepts in the author's primary language and their English correspondence, preventing translation or AI interpretation from hardening unconfirmed meaning into the article structure.

## C12. Cross-agent handoff requires an explicit bootstrap entry and verifiable handshake

The article should explain that storing state in a repository is not by itself sufficient to ensure correct takeover by a new AI Agent. A project also needs an explicit and discoverable zero-context bootstrap entry, a mandatory read order, and an Onboarding Report produced before substantive work to demonstrate that the Agent has correctly reconstructed human commitments, Clarification state, Framework state, Artifact state, and synchronization defects.

The mechanism does not assume every AI platform automatically reads the same filename. Instead, root-level entry files, an agent contract, a machine-readable manifest, and a human-copyable bootstrap prompt maximize cross-platform discoverability and make successful handoff observable and verifiable.

## C13. Durable repository state and an active session contract should form two-layer memory

The article should explain that repository persistence solves cross-session recoverability but does not guarantee that key rules remain sufficiently salient in the active generation context of a long conversation.

HARC therefore uses two layers:

1. **Durable Repository State** — auditable, recoverable, cross-agent long-term state;
2. **Active Session Contract** — a compressed operating contract regenerated from current repository state after onboarding and echoed into the Agent's own current reply.

The Session Contract is not the platform's true system prompt. It cannot override platform system/developer/safety instructions or permanently modify model memory. Its role is to reinject key HARC invariants, Blocking Clarifications, Framework/Artifact state, and the current task propagation path into the visible active conversation context.

After major state changes or suspected context loss, the Agent should regenerate a `HARC CONTEXT REFRESH` from repository state.

## Current unresolved authorial decisions

Operational state for high-impact unresolved issues is maintained in `docs/clarification-register.md`. Article-related entries are currently `CLR-001` through `CLR-008`; `CLR-001`, `CLR-002`, and `CLR-005` are currently `BLOCKING` clarifications before Framework Approval.

## Provenance correction

A prior version treated an explicit empirical testing program (handoff tests, semantic-drift tests, framework-fidelity tests, review-effort tests, cross-model portability tests) as if it were already part of the human-originated article foundation. That was too strong. The human founder required HARC to be practically implementable and reusable; the specific empirical test program was an AI-developed extension and remains provisional unless accepted.

## Status

Human-originated article foundation represented through the current founding discussion. Working article structure remains unapproved.