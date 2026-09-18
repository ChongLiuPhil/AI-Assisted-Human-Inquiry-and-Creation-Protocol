# HARC Research Project Template

> **Language:** Chinese canonical: `README.zh-CN.md`; this English file is the synchronized mirror.

Use this directory as the conceptual bootstrap for a new HARC-governed project.

## Protocol source

At initialization, record which HARC version/tag/commit the project adopts. A project should not silently change governance merely because the upstream HARC repository later evolves.

Default upstream reference:

`ChongLiuPhil/Human-AI-Research-Collaboration-Protocol`

See `AGENTS.md` for the protocol-source fields.

## Default language governance

This template defaults to a bilingual profile:

- Chinese canonical — semantic, editing, and human-review baseline;
- English synchronized mirror — updated in the same work cycle.

A different language-governance choice must be an explicit human/project decision.

## Initialization sequence

1. Create/confirm `START_HERE.zh-CN.md`, its English mirror, `HARC_MANIFEST.yaml`, and `HARC_CONTEXT_INTERFACE.yaml`; record the adopted HARC version/commit, mandatory read order, and repository-backed context policy.
2. Identify the artifact type: paper, book, article, report, thesis, etc.
3. Extract only the human's actual substantive commitments into `core/CONTENT_CORE.zh-CN.md` and synchronize the English mirror.
4. Identify any explicitly reusable author form profile and the applicable artifact-type profile.
5. Extract only explicit human presentation decisions into `core/FORM_CORE.zh-CN.md`; keep inherited, external, project-specific, and temporary-default rules distinguishable and synchronize English.
6. Record initialization decisions in `core/DECISION_LOG.zh-CN.md` and its English mirror.
7. Create `docs/working-memory.zh-CN.md` and its English mirror as the parallel Working Memory for current stage, objective, tasks, blockers, pending decisions, Clarifications, TODOs, and handoff.
8. Keep `docs/clarification-register.zh-CN.md` only as a compatibility pointer; manage new Clarifications as Working Memory items.
9. Build `docs/argument-map.zh-CN.md` and its English mirror as an AI-maintained Layer 2 working representation.
10. Initialize `docs/framework-status.zh-CN.md` as `WORKING-FRAMEWORK` with no approved snapshot unless the human has explicitly approved one.
11. Create the artifact directory appropriate to the project.
12. Create `evidence/` when research verification, data, calculations, or sources are relevant.
13. Keep unknowns explicit. Do not fill them with AI assumptions.

## Minimum template tree

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
│   ├── CONTENT_CORE.zh-CN.md
│   ├── CONTENT_CORE.md
│   ├── FORM_CORE.zh-CN.md
│   ├── FORM_CORE.md
│   ├── DECISION_LOG.zh-CN.md
│   └── DECISION_LOG.md
├── docs/
│   ├── working-memory.zh-CN.md
│   ├── working-memory.md
│   ├── clarification-register.zh-CN.md
│   ├── clarification-register.md
│   ├── argument-map.zh-CN.md
│   ├── argument-map.md
│   ├── framework-status.zh-CN.md
│   ├── framework-status.md
│   └── frameworks/
├── evidence/
└── paper/ | book/ | article/ | report/
```

## Form-profile inheritance

The upstream HARC repository provides:

- `templates/form-profiles/AUTHOR_PROFILE.zh-CN.md`
- `templates/form-profiles/BOOK.zh-CN.md`
- `templates/form-profiles/ACADEMIC_PAPER.zh-CN.md`
- `templates/form-profiles/ARTICLE.zh-CN.md`

Use only profiles applicable to the new project. Do not populate unresolved fields by guessing the author's tastes.

## Suggested instruction to an AI agent

> Initialize this project using HARC Protocol. Treat GitHub directly as the authoritative external-memory and working-state store; model context should retain only the Repository Resolver and task-relevant transient cache. Maintain `docs/working-memory.zh-CN.md` as the resume index for current stage, objectives, tasks, completion state, next actions, blockers, pending human decisions, Clarifications, TODOs, synchronization defects, and handoff. Treat the three content layers as Long-Term Research Memory: Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact. For high-impact uncertainty, create a Working Memory Clarification item and ask me rather than guessing. After human resolution, promote the stable result into the appropriate long-term destination. Separate CONTENT, FORM, and PROTOCOL decisions. Record the adopted HARC version/commit. Chinese is canonical and English must remain synchronized.

## Unknowns are valid state

A new project does not need every decision in advance.

Write:

`UNRESOLVED — no author preference specified yet`

rather than inventing a preference.
