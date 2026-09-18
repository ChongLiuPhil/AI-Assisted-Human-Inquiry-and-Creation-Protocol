# Human–AI Research Collaboration Protocol

[English](README.md) | [中文](README.zh-CN.md)

**Language governance: Chinese is the canonical source; English is the synchronized mirror. Every substantive edit must update both languages in the same work cycle. If they conflict, Chinese governs.**


**HARC Protocol** is a GitHub-centered workflow for sustained research and intellectual collaboration between a human author and interchangeable AI agents.

> **AI agents may be replaceable; the research state must not be.**

A chat window is an interaction surface, not the durable memory of a long research project. Important human decisions, argument structures, presentation requirements, evidence constraints, and approval states should be externalized into explicit, version-controlled repository files so that a new competent AI agent can continue the work without needing the original conversation history.

## Two project outputs

HARC is intentionally a dual-output project:

1. **Executable open protocol** — specifications, governance rules, templates, approval states, form profiles, memory architecture, and future conformance tooling.
2. **Methodology article** — a scholarly argument explaining the protocol and examining human cognitive/epistemic responsibility, delegation to AI, auditable authorship, persistent research memory, and the limits of AI-mediated research collaboration.

Current methodology-article files:

- [`docs/clarification-register.zh-CN.md`](docs/clarification-register.zh-CN.md) — canonical interface for current high-impact human clarifications; [`English mirror`](docs/clarification-register.md).
- [`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`](paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md) — canonical Chinese `WORKING-FRAMEWORK`; the Clarification Gate remains open; [`English mirror`](paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.md).
- [`paper/METHODOLOGY_ARTICLE.zh-CN.md`](paper/METHODOLOGY_ARTICLE.zh-CN.md) — canonical Chinese `DERIVED-PROVISIONAL` draft; [`English mirror`](paper/METHODOLOGY_ARTICLE.en.md).
- [`paper/methodology-references.bib`](paper/methodology-references.bib) — bibliography source file.
- [`evidence/METHODOLOGY_SOURCES.zh-CN.md`](evidence/METHODOLOGY_SOURCES.zh-CN.md) — canonical source verification and evidence constraints; [`English mirror`](evidence/METHODOLOGY_SOURCES.md).

The earlier white papers remain conceptual introductions; the methodology article is intended to become a standalone scholarly research output.

## Bilingual governance

All substantive human-readable HARC documentation is maintained in Chinese and English:

- Chinese `*.zh-CN.md` is the semantic, editing, and human-review baseline;
- English `*.md` / `*.en.md` is the synchronized translation mirror;
- new substantive files should be bilingual from creation;
- an edit is incomplete if only one language is updated;
- language-neutral BibTeX, code, schemas, and raw data may remain single-copy, while their human-facing documentation remains bilingual.

See [`protocol/BILINGUAL_SYNC.md`](protocol/BILINGUAL_SYNC.md) and the canonical Chinese [`protocol/BILINGUAL_SYNC.zh-CN.md`](protocol/BILINGUAL_SYNC.zh-CN.md).

## What problem does HARC address?

Long AI-assisted projects face recurring failures:

- **semantic drift** — polished AI prose gradually replaces or weakens what the human originally meant;
- **authorship ambiguity** — it becomes unclear which claims were human commitments and which were AI suggestions;
- **context-window dependence** — important decisions remain trapped in one conversation or one platform's memory;
- **structural opacity** — the human must reread a long manuscript to understand what the project currently argues;
- **presentation drift** — temporary AI formatting choices become mistaken for enduring author preferences;
- **handoff failure** — a new model or agent cannot reliably reconstruct the project's current state;
- **generation–verification asymmetry** — AI can generate and restructure work faster than humans can continuously verify it.

HARC addresses these problems by separating **human intention**, **operational representation**, **evidence**, **form**, **approval**, **history**, and **derived expression**.

## Canonical architecture

A HARC project normally contains:

```text
project/
├── AGENTS.md
├── core/
│   ├── CONTENT_CORE.md
│   ├── FORM_CORE.md
│   └── DECISION_LOG.md
├── docs/
│   ├── clarification-register.md
│   ├── argument-map.md
│   ├── framework-status.md
│   └── frameworks/
├── evidence/
└── paper/ | book/ | article/ | report/ | ...
```

### Content Core

`CONTENT_CORE.md` records the human author's current substantive commitments: what the work means to claim, distinguish, question, preserve, or leave open.

AI proposals do **not** become author commitments merely because they are useful or polished.

### Form Core

`FORM_CORE.md` records how the human wants the artifact expressed: artifact type, typography, layout, citation presentation, visual system, language presentation, and reusable style preferences.

Research content and presentation preferences are deliberately kept separate.

### Decision Log

`DECISION_LOG.md` is the chronological audit trail of substantive human decisions across content, form, and collaboration protocol.

### Critical Clarification Register

`docs/clarification-register.md` is **Layer 1.5** between human-confirmed Core state and the AI-maintained Working Argument Map. When AI has high-impact uncertainty about core claims, key concepts, scope, inferential relations, section functions, or important terminology/translation, it must register the issue for human confirmation rather than guess.

After resolution: `Clarification Register -> Decision Log -> Core -> Argument Map -> Artifact`.

### Operational Argument Map

`docs/argument-map.md` is a compact, AI-maintained representation of the current intellectual structure. It is the preferred human–AI discussion interface for long-form research. High-impact unresolved issues should reference the Clarification Register rather than duplicating the full clarification record.

### Approved Framework Snapshots

The Working Argument Map is not automatically human-endorsed. When the human explicitly reviews and approves a framework, it is frozen as a versioned snapshot such as `docs/frameworks/FW-001.md`.

Material changes require a new approved framework version rather than silent rewriting.

### Derived Artifact

The paper, book, report, or other final output is a **derived expression** constrained by the Content Core, Approved Framework, Form Core, and evidence.

## Three-way routing of human feedback

Every substantive instruction is classified before persistence:

- **CONTENT** — changes what the work argues or means;
- **FORM** — changes how the work is presented;
- **PROTOCOL** — changes how the collaboration itself operates.

A message may carry more than one label.

```text
CONTENT:
Human decision -> Decision Log -> Content Core -> Argument Map -> Artifact

FORM:
Human decision -> Decision Log -> Form Core -> Rendering / Typesetting -> Artifact

PROTOCOL:
Human decision -> Decision Log -> Protocol Documents -> Agent Behavior
```

## Two human approval gates

### Gate A — Framework Approval

The human reviews and accepts the work's core intellectual architecture: main theses, argument relations, distinctions, section roles, limitations, and intentionally unresolved questions.

This is the project's primary **substantive intellectual checkpoint**.

HARC distinguishes a defect already present in this approved architecture from a local defect introduced only during later AI expansion.

### Gate B — Final Artifact Approval

Before formal submission, publication, or public release under human authorship, the human approves the concrete release version to the degree required by the relevant venue, institution, discipline, or authorship standard.

Framework approval concentrates human attention on intellectual architecture; it does not waive final publication accountability.

## Cognitive delegation vs epistemic responsibility

HARC does not assume that human value lies in manually producing every sentence. AI may perform substantial search, synthesis, drafting, restructuring, consistency checking, and formatting.

But delegation of cognitive labor is not automatically delegation of epistemic responsibility. HARC concentrates human attention on high-leverage decisions: research aims, core commitments, major inferential architecture, decisive evidence conflicts, framework approval, and final release approval where required.

This responsibility model is developed in the methodology article.

## Reusable form profiles

HARC supports form inheritance across projects:

`reusable author profile -> artifact-type profile -> project Form Core -> external constraints -> implementation`

See:

- `protocol/FORM_PROFILE_INHERITANCE.md`
- `templates/form-profiles/AUTHOR_PROFILE.md`
- `templates/form-profiles/BOOK.md`
- `templates/form-profiles/ACADEMIC_PAPER.md`
- `templates/form-profiles/ARTICLE.md`

## Persistent memory principle

> **Chat is temporary interaction context. The repository is durable shared research memory.**

Not every chat sentence must be stored. But if losing a human instruction would change how a new agent should continue the project, that instruction should be promoted into an appropriate canonical repository file.

This does not create infinite model context. It supports scalable memory through compact current-state cores, chronological logs, structural maps, detailed evidence/archives, indexes, and selective retrieval.

## Audit discipline

A multi-pass HARC audit is a sequence of **review-and-repair cycles**:

`review -> identify defect -> repair/implement -> verify repair`

A requested three-pass audit means three such cycles. A requested post-repair audit is performed afterward as a separate fourth check.

Audit records:

- [`docs/FOUNDING_IDEA_AUDIT.md`](docs/FOUNDING_IDEA_AUDIT.md) — founding-idea traceability.
- [`docs/THREE_CYCLE_REPAIR_AUDIT.md`](docs/THREE_CYCLE_REPAIR_AUDIT.md) — explicit three-cycle review/repair record.
- [`docs/FINAL_POST_REPAIR_AUDIT.md`](docs/FINAL_POST_REPAIR_AUDIT.md) — independent post-repair audit.
- [`docs/BILINGUAL_PARITY_AUDIT.md`](docs/BILINGUAL_PARITY_AUDIT.md) — repository-wide Chinese-canonical / English-mirror parity audit.

## Start here

### For humans

1. Read the canonical Chinese [`paper/METHODOLOGY_ARTICLE.zh-CN.md`](paper/METHODOLOGY_ARTICLE.zh-CN.md) for the emerging scholarly argument.
2. Read the canonical Chinese [`docs/clarification-register.zh-CN.md`](docs/clarification-register.zh-CN.md) first for current high-impact unresolved issues.
3. Then read [`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`](paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md) to inspect the current Working Framework.
4. Read the canonical Chinese [`protocol/SPECIFICATION.zh-CN.md`](protocol/SPECIFICATION.zh-CN.md) for the normative workflow.
5. Read [`docs/THREE_CYCLE_REPAIR_AUDIT.md`](docs/THREE_CYCLE_REPAIR_AUDIT.md) and [`docs/FINAL_POST_REPAIR_AUDIT.md`](docs/FINAL_POST_REPAIR_AUDIT.md) for the current integration audit state.
6. Use [`templates/research-project/`](templates/research-project/) to bootstrap a new project.

### For AI agents

1. Read canonical [`AGENTS.zh-CN.md`](AGENTS.zh-CN.md), then use [`AGENTS.md`](AGENTS.md) as the English mirror.
2. Read canonical [`core/PROTOCOL_CORE.zh-CN.md`](core/PROTOCOL_CORE.zh-CN.md) and recent [`core/DECISION_LOG.zh-CN.md`](core/DECISION_LOG.zh-CN.md).
3. Read canonical [`protocol/SPECIFICATION.zh-CN.md`](protocol/SPECIFICATION.zh-CN.md).
4. Apply the relevant persistence, framework-approval, routing, evidence, and form-inheritance rules.
5. Do not invent human commitments that have not been stated.
6. Record the HARC version/tag/commit adopted by a new project so later upstream changes are not silently treated as already accepted governance.

## Repository status

This repository is the standalone development home of HARC Protocol. It contains:

- the normative specification;
- implementation guidance;
- reusable research-project templates;
- reusable form-profile templates;
- a conceptual white paper;
- a methodology article under HARC framework control;
- an evidence layer for the methodology article;
- founding-idea and repair audits;
- a roadmap for future development.

The protocol currently targets **GitHub + human author + AI agent(s)**. Broader platform support may be considered later.

## Design principle

HARC is not a system for making AI the hidden author of a human-labelled work. It is a system for making the relationship among **human intention, AI transformation, evidence, approval, responsibility, and final expression explicit and auditable**.

## Version

Working specification: **v0.2.0-draft**.

## Licensing

The project is intended for open reuse. Exact licensing terms are recorded in `LICENSE-DECISION.md` and should be finalized explicitly rather than inferred from repository visibility.
