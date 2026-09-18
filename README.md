# Human–AI Research Collaboration Protocol

[English](README.md) | [中文](README.zh-CN.md)

**Language governance: Chinese is the canonical source; English is the synchronized mirror. Every substantive edit must update both languages in the same work cycle. If they conflict, Chinese governs.**


**HARC Protocol** is a GitHub-centered workflow for sustained research and intellectual collaboration between a human author and interchangeable AI agents.

> **AI agents may be replaceable; the research state must not be.**

A chat window is an interaction surface, not the durable memory of a long research project. Important human decisions, argument structures, presentation requirements, evidence constraints, and approval states should be externalized into explicit, version-controlled repository files so that a new competent AI agent can continue the work without needing the original conversation history.

## AI Agent zero-context onboarding: start here

A new AI Agent should **not begin substantive work directly from the README or manuscript**.

Read first:

1. [`START_HERE.zh-CN.md`](START_HERE.zh-CN.md)
2. [`BOOTSTRAP_PROMPT.zh-CN.md`](BOOTSTRAP_PROMPT.zh-CN.md)
3. [`SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`](SESSION_CONTEXT_BOOTSTRAP.zh-CN.md)
4. `HARC_MANIFEST.yaml`
5. `HARC_CONTEXT_INTERFACE.yaml`
6. [`AGENTS.zh-CN.md`](AGENTS.zh-CN.md)
7. [`docs/working-memory.zh-CN.md`](docs/working-memory.zh-CN.md)
8. [`ONBOARDING_REPORT_TEMPLATE.zh-CN.md`](ONBOARDING_REPORT_TEMPLATE.zh-CN.md)

Then use Working Memory to identify the resume point, selectively reconstruct task-relevant long-term state, and submit a **HARC Onboarding Report** before making substantive changes.

See [`docs/ONBOARDING_SELF_TEST.md`](docs/ONBOARDING_SELF_TEST.md) for the repository's current self-hosted onboarding validation.

This makes correct project reconstruction an observable handshake rather than an assumption.

After the handshake, `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` loads only a minimal Repository Resolver, while `HARC_CONTEXT_INTERFACE.yaml` defines selective retrieval, revision freshness, write-through, and cache invalidation. Dynamic project state is not maintained as a second chat truth source.

## Two project outputs

HARC is intentionally a dual-output project:

1. **Executable open protocol** — specifications, governance rules, templates, approval states, form profiles, memory architecture, and future conformance tooling.
2. **Methodology article** — a scholarly argument explaining the protocol and examining human responsibility for research purpose, direction, and intellectual architecture, the division of work with AI tools, auditable authorship, persistent research memory, and the limits of AI-mediated research collaboration.

Current methodology-article files:

- [`docs/working-memory.zh-CN.md`](docs/working-memory.zh-CN.md) — Working Memory Index / Resolver; [`English mirror`](docs/working-memory.md).
- [`docs/working-memory/current-focus.zh-CN.md`](docs/working-memory/current-focus.zh-CN.md) — highest-priority immediate objective.
- [`docs/working-memory/task-plan.zh-CN.md`](docs/working-memory/task-plan.zh-CN.md) — dynamic tasks, TODOs, blockers, and pending decisions.
- [`docs/working-memory/work-log.zh-CN.md`](docs/working-memory/work-log.zh-CN.md) — human-retrospective work history, outside default AI onboarding.
- [`docs/clarification-register.zh-CN.md`](docs/clarification-register.zh-CN.md) — legacy compatibility pointer; no active state.
- [`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`](paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md) — canonical Chinese `WORKING-FRAMEWORK`; the Working Memory / Clarification Gate remains open; [`English mirror`](paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.md).
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
├── START_HERE.zh-CN.md
├── START_HERE.md
├── BOOTSTRAP_PROMPT.zh-CN.md
├── BOOTSTRAP_PROMPT.md
├── SESSION_CONTEXT_BOOTSTRAP.zh-CN.md
├── SESSION_CONTEXT_BOOTSTRAP.md
├── ONBOARDING_REPORT_TEMPLATE.zh-CN.md
├── ONBOARDING_REPORT_TEMPLATE.md
├── HARC_MANIFEST.yaml
├── HARC_CONTEXT_INTERFACE.yaml
├── AGENTS.zh-CN.md
├── AGENTS.md
├── core/
│   ├── CONTENT_CORE.md
│   ├── FORM_CORE.md
│   └── DECISION_LOG.md
├── docs/
│   ├── working-memory.zh-CN.md
│   ├── working-memory.md
│   ├── clarification-register.zh-CN.md
│   ├── clarification-register.md
│   ├── argument-map.md
│   ├── framework-status.md
│   └── frameworks/
├── evidence/
└── paper/ | book/ | article/ | report/ | ...
```

### Zero-context bootstrap entry

`START_HERE.zh-CN.md` and `HARC_MANIFEST.yaml` define the first read order and Onboarding Handshake for a replacement Agent. They do not create new research claims; they route the Agent to authoritative state and make successful reconstruction observable.

### Content Core

`CONTENT_CORE.md` records the human author's current substantive commitments: what the work means to claim, distinguish, question, preserve, or leave open.

AI proposals do **not** become author commitments merely because they are useful or polished.

### Form Core

`FORM_CORE.md` records how the human wants the artifact expressed: artifact type, typography, layout, citation presentation, visual system, language presentation, and reusable style preferences.

Research content and presentation preferences are deliberately kept separate.

### Decision Log

`DECISION_LOG.md` is the chronological audit trail of substantive human decisions across content, form, and collaboration protocol.

### Working Memory Area

Working Memory is a functional area rather than one fixed file. The current HARC reference implementation splits it into Index, Current Focus, Task Plan, and Work Log.

The long-term layers are:

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

Working Memory is not Layer 1.5. Current Focus stores “what matters most now”; Task Plan stores “how work proceeds next”; Work Log stores “how we got here” primarily for later human review.

Clarification is an item type inside Working Memory. After human resolution:

`Working Memory -> Decision Log -> appropriate Long-Term Memory destination`

The old `docs/clarification-register.zh-CN.md` remains only as a compatibility pointer.

### Operational Argument Map

`docs/argument-map.md` is a compact, AI-maintained representation of the current intellectual structure. It is the preferred human–AI discussion interface for long-form research. Current blockers, pending human decisions, and high-impact Clarifications should reference Working Memory rather than being duplicated in the Argument Map.

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

## AI-supported work and human bearers of responsibility

HARC does not assume that human value lies in manually producing every sentence. An AI Agent, used as a tool, may perform or assist with substantial search, synthesis, drafting, restructuring, consistency checking, and formatting.

HARC does not characterize AI as a cognitive subject or use “AI performs cognitive labor / cognitive tasks” as normative language. The purpose, central problem, and direction of research or creative work originate with humans and remain under human navigation and approval.

The key point is not to treat “human responsibility” as an abstract property, but to make explicit that **humans must remain the bearers of responsibility.** This applies throughout research and inquiry and becomes especially important when papers, books, reports, or other outputs enter public knowledge circulation. AI may share work, but it cannot become the ultimate bearer of responsibility for project purpose, core judgment, framework authorization, or public dissemination of knowledge.

For long-form work, this responsibility-bearing status is operationalized primarily through the Layer 2 Framework: before Framework Approval, the human must clearly understand, carefully review, and explicitly confirm every substantive element actually represented in the framework. AI may help propose and organize the framework, but it cannot replace human authorization of the project's direction and intellectual architecture. Final Artifact Approval remains a separate requirement, ensuring that the concrete public version retains identifiable human bearers of responsibility for release.

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
2. Read [`docs/working-memory.zh-CN.md`](docs/working-memory.zh-CN.md) first for current stage, objective, tasks, blockers, and next actions.
3. Then read [`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`](paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md) to inspect the current Working Framework.
4. Read the canonical Chinese [`protocol/SPECIFICATION.zh-CN.md`](protocol/SPECIFICATION.zh-CN.md) for the normative workflow.
5. Read [`docs/THREE_CYCLE_REPAIR_AUDIT.md`](docs/THREE_CYCLE_REPAIR_AUDIT.md) and [`docs/FINAL_POST_REPAIR_AUDIT.md`](docs/FINAL_POST_REPAIR_AUDIT.md) for the current integration audit state.
6. Use [`templates/research-project/`](templates/research-project/) to bootstrap a new project.

### For AI agents

1. Read canonical [`AGENTS.zh-CN.md`](AGENTS.zh-CN.md), then use [`AGENTS.md`](AGENTS.md) as the English mirror.
2. Read [`docs/working-memory.zh-CN.md`](docs/working-memory.zh-CN.md) to determine the resume point.
3. Read canonical [`core/PROTOCOL_CORE.zh-CN.md`](core/PROTOCOL_CORE.zh-CN.md) and recent [`core/DECISION_LOG.zh-CN.md`](core/DECISION_LOG.zh-CN.md).
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
