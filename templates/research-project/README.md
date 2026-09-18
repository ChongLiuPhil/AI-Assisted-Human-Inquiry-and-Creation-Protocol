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

1. Identify the artifact type: paper, book, article, report, thesis, etc.
2. Extract only the human's actual substantive commitments into `core/CONTENT_CORE.zh-CN.md plus English mirror`.
3. Identify any explicitly reusable author form profile and the applicable artifact-type profile.
4. Extract only explicit human presentation decisions into `core/FORM_CORE.zh-CN.md plus English mirror`; keep inherited, external, project-specific, and temporary-default rules distinguishable.
5. Record initialization decisions in `core/DECISION_LOG.zh-CN.md plus English mirror`.
6. Build `docs/argument-map.zh-CN.md plus English mirror` as an AI-maintained working representation.
7. Initialize `docs/framework-status.zh-CN.md plus English mirror` as `WORKING-FRAMEWORK` with no approved snapshot unless the human has explicitly approved one.
8. Create the artifact directory appropriate to the project.
9. Create `evidence/` when research verification, data, calculations, or sources are relevant.
10. Keep unknowns explicit. Do not fill them with AI assumptions.

## Minimum template tree

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

> Initialize this project using HARC Protocol. Treat GitHub as the durable project memory. Separate CONTENT, FORM, and PROTOCOL decisions. Seed canonical files only with human-provided commitments. Identify the artifact type and applicable form profiles without inventing preferences. Maintain the argument map as AI-generated working structure until I explicitly approve a framework snapshot. Propagate substantive changes upstream-first. Record which HARC version/commit this project adopts.

## Unknowns are valid state

A new project does not need every decision in advance.

Write:

`UNRESOLVED — no author preference specified yet`

rather than inventing a preference.
