# Content / Form / Protocol Routing

> **Language:** Chinese canonical: `FORM_CONTENT_ROUTING.zh-CN.md`; this English file is the synchronized mirror.

AHICP treats human feedback as durable project state only after it has been classified and written to the appropriate canonical layer.

## CONTENT

Use `CONTENT` when the instruction changes what the work means or argues.

Examples:

- revise a thesis;
- add a conceptual distinction;
- reject an interpretation;
- change scope;
- add or remove an argumentative premise;
- clarify what a chapter is meant to establish.

Route:

`Decision Log -> Content Core -> Argument Map -> Approved Framework (if re-approved) -> Artifact`

## FORM

Use `FORM` when the instruction changes how the artifact is presented without itself changing the substantive thesis.

Examples:

- artifact type;
- typography;
- margin/layout system;
- heading hierarchy;
- visual density;
- citation presentation;
- footnotes;
- figure/table style;
- language-presentation conventions;
- reusable author style preferences.

Route:

`Decision Log -> Form Core -> Rendering/Typesetting -> Artifact`

## PROTOCOL

Use `PROTOCOL` when the instruction changes how the human and AI collaborate.

Examples:

- required reading order;
- approval gates;
- persistence rules;
- agent handoff;
- branch/commit conventions;
- archive strategy;
- synchronization checks.

Route:

`Decision Log -> Protocol/Governance Files -> Agent Behavior`

## Multi-label cases

A single instruction may affect multiple domains.

Example:

> "Turn the paper into a book and reorganize the argument around three parts."

This is both:

- `FORM` because artifact type changes;
- `CONTENT` because the intellectual architecture changes.

Do not force single-label classification when it obscures the actual change.

## Pre-routing for high-impact uncertainty

Before writing human feedback directly into a durable Core, if the AI has high-impact uncertainty about its meaning, create a Clarification item in Working Memory rather than choosing one classified interpretation.

`Ambiguous high-impact feedback -> Working Memory / Clarification -> Human resolution -> Promotion -> CONTENT / FORM / PROTOCOL routing`

The resolved clarification may itself carry one or multiple labels.

## Temporary implementation defaults

AI agents often need to choose defaults before the human has specified a preference.

Examples:

- a default font in LaTeX;
- provisional citation style;
- placeholder section numbering;
- temporary page size.

Such choices MUST be treated as `TEMPORARY-DEFAULT`, not as human preference.

A temporary default becomes canonical only after explicit human acceptance.

## Cross-project form preferences

Some form decisions may be explicitly reusable across projects.

If the human states that a preference is intended to be general, classify it as:

`REUSABLE-AUTHOR-PREFERENCE`

A project may inherit such preferences while allowing project-specific or external publication constraints to override them.

## Practical routing test

Ask:

1. Does this change **what is being claimed**? -> `CONTENT`
2. Does this change **how it is expressed/rendered**? -> `FORM`
3. Does this change **how collaboration operates**? -> `PROTOCOL`

Apply all labels that genuinely fit.
