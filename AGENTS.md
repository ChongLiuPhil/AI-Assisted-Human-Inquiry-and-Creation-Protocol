# AGENTS.md — HARC Agent Contract

This repository defines the **Human–AI Research Collaboration Protocol (HARC)**. AI agents working in this repository or using it as a template must treat repository state as the durable collaboration substrate.

## 0. Zero-context onboarding: read START_HERE first

Any AI Agent taking over this repository from zero context must, before substantive work, read:

1. `START_HERE.zh-CN.md`
2. `HARC_MANIFEST.yaml`

Then follow the mandatory read order and output a **HARC Onboarding Report** before large-scale structural edits, manuscript rewriting, Framework Approval, broad terminology propagation, or promotion of AI proposals into human commitments.

## 1. Do not depend on chat memory

A particular chat, model, vendor, account memory, hidden scratchpad, or local context is not the canonical project memory.

If a human instruction should constrain future work, persist it explicitly in the appropriate repository file.

## 2. Preserve three distinct domains

Before acting on substantive human feedback, classify it as one or more of:

- `CONTENT` — research meaning, claims, distinctions, assumptions, questions, conclusions;
- `FORM` — artifact type, prose presentation, typography, layout, citation style, visual system, rendering;
- `PROTOCOL` — collaboration rules, persistence, versioning, approval, handoff, synchronization.

Do not merge these domains merely for convenience.

## 3. Canonical precedence in a research project

### Content chain

`Human content decision > CONTENT_CORE > approved framework > working argument map > derived prose`

### Form chain

`Human form decision > FORM_CORE > external venue constraints / reusable profile > implementation default > rendered artifact`

### Protocol chain

`Human workflow decision > project protocol files > agent default behavior`

Lower layers must not silently contradict higher layers.

## 4. Upstream-first updates

### CONTENT

1. Record the human decision in `DECISION_LOG.md`.
2. Reconcile `CONTENT_CORE.md`.
3. Reconcile the working argument map.
4. If the change materially alters an already approved framework, mark the project out of sync and request/create a new framework version.
5. Only then propagate the change into derived prose.

### FORM

1. Record the decision.
2. Reconcile `FORM_CORE.md`.
3. Propagate into typesetting/rendering implementation.
4. Do not turn temporary AI defaults into human preferences.

### PROTOCOL

1. Record the decision.
2. Reconcile protocol/governance files.
3. Update reusable templates if the rule is intended to generalize.

## 5. Critical Clarification Register

When the AI has **high-impact, non-trivial uncertainty** about authorial intent or key content, it must not silently choose an interpretation and propagate it.

Record the issue in `docs/clarification-register.md`, including at least:

- the uncertain point;
- candidate interpretations;
- why it matters;
- `BLOCKING / NON-BLOCKING` severity;
- affected files / claims / sections;
- any explicitly `AI-PROPOSED` recommendation;
- the question requiring human resolution.

Pay particular attention to strong/weak readings of core claims, key concepts, scope/qualification, major inferential relations, section functions, primary-language/English terminology, translation-induced semantic change, and tension between new feedback and older Core/Framework state.

After human confirmation or correction, perform:

`Clarification Register -> Decision Log -> appropriate Core -> Working Argument Map -> Derived Artifact`

Marking an item resolved without updating the Core is incomplete.

Run a Clarification Scan before major phase transitions, Framework Approval, broad propagation of key terminology, formal translation, large-scale expansion, and Final Review.

## 6. AI proposals are proposals

An AI-generated thesis, distinction, reorganization, term, layout, or aesthetic choice is not a human commitment merely because the AI has written it.

Until accepted by the human:

- content proposals remain visibly `AI-PROPOSED` in the operational layer;
- form proposals remain outside `FORM_CORE.md`;
- protocol proposals remain proposals rather than silently becoming mandatory rules.

## 7. Working framework vs approved framework

The current argument map is mutable and AI-maintained.

Human endorsement occurs only through an explicit **Framework Approval Gate**. Once approved, create a versioned immutable snapshot such as `FW-001.md`.

Material intellectual changes require a new framework version.

## 8. Evidence conflicts

Human authorial authority concerns intended claims; it does not authorize suppression of evidence.

If evidence, formal reasoning, or source verification conflicts with an active human commitment:

1. preserve the authorial commitment as the current intention;
2. surface the conflict explicitly;
3. do not knowingly write a misleading downstream claim;
4. present the issue for human decision;
5. record the resulting decision.

## 9. Final artifact status

AI may produce extensive derived text after framework approval, but it remains `DERIVED-PROVISIONAL` until final human review.

Do not represent an artifact as submission-ready or human-approved unless the relevant final approval gate has actually been completed.

## 10. Memory scaling

Canonical files should remain compact enough for routine onboarding. Detailed history can grow in logs, evidence files, and archives.

When history becomes large:

- preserve originals;
- create indexes/summaries;
- keep current-state cores concise;
- retrieve historical detail selectively.

The goal is recoverable project memory, not forcing every agent to ingest the entire archive.

## 11. Handoff criterion

A new competent AI agent should be able to reconstruct the project's active state without access to the original conversation history.

If this is not possible, the project has a persistence defect.

## 12. Multi-pass audits are review-and-repair loops

If the human requests a multi-pass audit, each pass MUST include:

1. review;
2. identification of defects/omissions;
3. repair or implementation;
4. verification of the repair.

Do not interpret “review three times” as three passive readings followed by a single repair. After the requested cycles, perform a separate post-repair audit when requested.

## 13. Maintain the methodology article as a governed research artifact

This repository has two major outputs:

1. the executable HARC open protocol;
2. a methodology article explaining and critically developing the protocol.

For the methodology article, read in this order:

1. `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`
2. `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`
3. `docs/clarification-register.zh-CN.md`
4. `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`
5. `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`
6. `evidence/METHODOLOGY_SOURCES.zh-CN.md`
7. `paper/methodology-references.bib`
8. `paper/METHODOLOGY_ARTICLE.zh-CN.md`
9. corresponding English mirrors for bilingual parity

The article's argument map is a `WORKING-FRAMEWORK` until the human explicitly approves it. The prose draft is `DERIVED-PROVISIONAL` until the appropriate approval gates are completed.

The methodology article must obey the same HARC principles it describes. Do not treat AI-proposed terminology or article structure as human-approved merely because it appears in the draft. When research on authorship, AI policy, epistemic responsibility, automation, or cognition changes factual claims in the article, update the evidence layer first and keep normative HARC proposals distinct from external publication rules.

## 14. Audit records

Use the audit documents according to their roles:

- `docs/FOUNDING_IDEA_AUDIT.md` — founding-idea coverage inventory and traceability record;
- `docs/THREE_CYCLE_REPAIR_AUDIT.md` — the corrected three-cycle `review -> repair -> verify` execution record;
- `docs/FINAL_POST_REPAIR_AUDIT.md` — independent audit performed after all three repair cycles.
- `docs/BILINGUAL_PARITY_AUDIT.md` — repository-wide bilingual pairing and high-risk semantic synchronization audit.

If these documents conflict about process status, the later repair/final-audit records govern the interpretation of the audit procedure; founder decisions in `core/DECISION_LOG.md` remain canonical.

## 15. When using this repository as a template

Read, in order:

1. `protocol/SPECIFICATION.md`
2. `protocol/PERSISTENT_MEMORY.md`
3. `protocol/FRAMEWORK_APPROVAL.md`
4. `protocol/FORM_CONTENT_ROUTING.md`
5. `protocol/FORM_PROFILE_INHERITANCE.md`
6. `templates/research-project/README.md`

Then instantiate only the human decisions actually supplied for the new project. Unknowns should remain explicit rather than being filled with AI assumptions.

## 16. Chinese canonical / English synchronized mirror

HARC is a bilingual project.

For substantive Markdown content:

- the Chinese version is the canonical semantic and editing baseline;
- the English version is a synchronized translation mirror;
- every substantive edit to Chinese MUST be reflected in English in the same work cycle;
- an edit is not complete while the language pair is materially inconsistent;
- if Chinese and English conflict, Chinese governs and the English version MUST be repaired;
- new substantive documents SHOULD be created as bilingual pairs from the beginning.

Preferred naming:

- Chinese canonical: `NAME.zh-CN.md`
- English mirror: `NAME.md` when an existing GitHub-default path is useful, otherwise `NAME.en.md`.

Language-neutral technical files (for example BibTeX, schemas, code, raw data) need not be duplicated solely for translation, but human-readable guidance around them must remain bilingual.

When editing a bilingual pair, treat the two-file synchronization as one atomic task. Do not mark the work complete after updating only one language.

### Pre-cutover legacy exception

For files that existed before the bilingual rule was established on 2026-09-18, if historical English actually contains newer substantive development not yet absorbed by Chinese, first merge that development into Chinese so Chinese represents the latest state at cutover, then synchronize English. After this one-time legacy catch-up, the normal direction is fixed as:

`human decision -> Chinese canonical -> English synchronized mirror`

English must not independently develop substantive content after cutover.
