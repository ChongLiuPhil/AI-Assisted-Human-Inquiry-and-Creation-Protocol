# Human–AI Research Collaboration Protocol

**HARC Protocol** is a GitHub-centered, platform-independent workflow for sustained research and intellectual collaboration between a human author and interchangeable AI agents.

The central idea is simple:

> **AI agents may be replaceable; the research state must not be.**

A chat window is an interaction surface, not the durable memory of a long research project. Important human decisions, argument structures, presentation requirements, evidence constraints, and approval states should be externalized into explicit, version-controlled repository files so that a new competent AI agent can continue the work without needing the original conversation history.

## What problem does this solve?

Long AI-assisted projects face several recurring failures:

- **semantic drift** — polished AI prose gradually replaces or weakens what the human originally meant;
- **authorship ambiguity** — it becomes unclear which claims were human commitments and which were AI suggestions;
- **context-window dependence** — important decisions remain trapped in one conversation or one platform's memory;
- **structural opacity** — the human must reread a long manuscript to understand what the project currently argues;
- **presentation drift** — temporary AI formatting choices become mistaken for the author's enduring preferences;
- **handoff failure** — a new model or agent cannot reliably reconstruct the project's current state.

HARC addresses these problems by separating **human intention**, **operational representation**, **evidence**, **form**, and **derived expression**.

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
│   ├── argument-map.md
│   ├── framework-status.md
│   └── frameworks/
├── evidence/
├── protocol/
└── paper/ | book/ | article/ | report/ | ...
```

### 1. Content Core

`CONTENT_CORE.md` records the human author's current substantive commitments: what the work means to claim, distinguish, question, preserve, or leave open.

AI proposals do **not** enter this file merely because they are useful or polished. They enter only after human acceptance or modification.

### 2. Form Core

`FORM_CORE.md` records how the human wants the artifact expressed: artifact type, typography, layout, citation presentation, visual system, language presentation, and reusable style preferences.

Research content and presentation preferences are deliberately kept separate.

### 3. Decision Log

`DECISION_LOG.md` is the chronological audit trail of substantive human decisions across content, form, and collaboration protocol.

### 4. Operational Argument Map

`docs/argument-map.md` is a compact, AI-maintained representation of the current intellectual structure. It is the preferred human–AI discussion interface for long-form research.

It should be much shorter than the manuscript and should expose:

- central questions and theses;
- conceptual distinctions;
- argument dependencies;
- section or chapter architecture;
- evidence dependencies;
- open objections;
- unresolved human decisions;
- AI proposals awaiting human acceptance.

### 5. Approved Framework Snapshots

The working argument map is not automatically human-endorsed. When the human explicitly reviews and approves a framework, it is frozen as a versioned snapshot such as:

`docs/frameworks/FW-001.md`

Material changes require a new approved framework version rather than silent rewriting.

### 6. Derived Artifact

The paper, book, report, or other final output is a **derived expression** constrained by the content core, approved framework, form core, and evidence.

AI may perform substantial drafting and expansion, but downstream prose must not silently redefine upstream human-approved meaning.

## Three-way routing of human feedback

Every substantive instruction is classified before persistence:

- **CONTENT** — changes what the work argues or means;
- **FORM** — changes how the work is presented;
- **PROTOCOL** — changes how the collaboration itself operates.

A message may carry more than one label.

The normal propagation paths are:

```text
CONTENT:
Human decision -> Decision Log -> Content Core -> Argument Map -> Artifact

FORM:
Human decision -> Decision Log -> Form Core -> Rendering / Typesetting -> Artifact

PROTOCOL:
Human decision -> Decision Log -> Protocol Documents -> Agent Behavior
```

## Two human approval gates

HARC distinguishes two different forms of human review.

### Gate A — Framework Approval

The human reviews and accepts the work's core intellectual architecture: main theses, argument relations, distinctions, section roles, limitations, and intentionally unresolved questions.

This is the project's primary **substantive intellectual checkpoint**.

### Gate B — Final Artifact Approval

Before formal submission, publication, or public release under human authorship, the human approves the concrete release version to the degree required by the relevant venue, institution, discipline, or authorship standard.

Framework approval concentrates human attention on the intellectual architecture; it does not automatically waive final publication accountability.

## Persistent memory principle

> **Chat is temporary interaction context. The repository is durable shared research memory.**

Not every chat sentence must be stored. But if losing a human instruction would change how a new agent should continue the project, that instruction should be **promoted** into an appropriate canonical repository file.

This does not create infinite model context. Instead it supports scalable memory through:

- compact current-state cores;
- chronological logs;
- structural maps;
- detailed evidence and archives;
- selective retrieval when historical detail becomes relevant.

## Repository status

This repository is the standalone development home of HARC Protocol. It contains:

- the normative specification;
- implementation guidance;
- reusable project templates;
- a conceptual white paper;
- a roadmap for future development.

The protocol currently targets **GitHub + human author + AI agent** workflows. Broader platform support may be considered later.

## Start here

For humans:

1. Read [`paper/WHITEPAPER.md`](paper/WHITEPAPER.md) for the rationale and conceptual model.
2. Read [`protocol/SPECIFICATION.md`](protocol/SPECIFICATION.md) for the normative workflow.
3. Use [`templates/research-project/`](templates/research-project/) to bootstrap a new project.

For AI agents:

1. Read [`AGENTS.md`](AGENTS.md).
2. Read [`protocol/SPECIFICATION.md`](protocol/SPECIFICATION.md).
3. Apply the template without inventing human commitments that have not been stated.

## Design principle

HARC is not a system for making AI the hidden author of a human-labelled work. It is a system for making the relationship among **human intention, AI transformation, evidence, approval, and final expression explicit and auditable**.

## Version

Working specification: **v0.1.0**.

## Licensing

The project is intended for open reuse. Exact licensing terms are recorded in `LICENSE-DECISION.md` and should be finalized explicitly rather than inferred from repository visibility.
