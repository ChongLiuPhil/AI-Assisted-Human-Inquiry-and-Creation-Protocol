# HARC Research Project Template

Use this directory as the conceptual bootstrap for a new HARC-governed project.

## Initialization sequence

1. Identify the artifact type: paper, book, article, report, thesis, etc.
2. Extract only the human's actual substantive commitments into `core/CONTENT_CORE.md`.
3. Extract only explicit human presentation decisions into `core/FORM_CORE.md`.
4. Record initialization decisions in `core/DECISION_LOG.md`.
5. Build `docs/argument-map.md` as an AI-maintained working representation.
6. Initialize `docs/framework-status.md` as `WORKING-FRAMEWORK` with no approved snapshot unless the human has explicitly approved one.
7. Create the artifact directory appropriate to the project.
8. Keep unknowns explicit. Do not fill them with AI assumptions.

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

## Suggested instruction to an AI agent

> Initialize this project using HARC Protocol. Treat GitHub as the durable project memory. Separate CONTENT, FORM, and PROTOCOL decisions. Seed canonical files only with human-provided commitments. Maintain the argument map as AI-generated working structure until I explicitly approve a framework snapshot. Propagate substantive changes upstream-first.

## Unknowns are valid state

A new project does not need every decision in advance.

Write:

`UNRESOLVED — no author preference specified yet`

rather than inventing a preference.
