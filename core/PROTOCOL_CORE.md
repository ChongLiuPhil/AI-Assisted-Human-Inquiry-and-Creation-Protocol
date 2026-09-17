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

---

## Current scope

HARC v0.1 focuses on:

`Human Author + GitHub Repository + AI Agent(s)`

for sustained research and intellectual development.

Broader platform support is outside the initial scope.
