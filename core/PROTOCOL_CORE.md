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
