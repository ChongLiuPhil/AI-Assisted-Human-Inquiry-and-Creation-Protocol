# AGENTS.md — Project HARC Contract

This project follows the Human–AI Research Collaboration Protocol.

## Required reading order

Before substantive work, read:

1. `core/CONTENT_CORE.md`
2. `core/FORM_CORE.md`
3. recent `core/DECISION_LOG.md`
4. `docs/framework-status.md`
5. latest approved framework, if any
6. `docs/argument-map.md`
7. relevant artifact and evidence files

## Repository state outranks chat memory

Do not rely on a previous agent's chat context as canonical project state. Promote durable human decisions into repository files.

## Route human feedback

Classify substantive instructions as:

- `CONTENT`
- `FORM`
- `PROTOCOL`
- or multi-label.

Persist and propagate upstream-first.

## Content rule

Human content decisions outrank AI drafting. AI proposals remain visibly pending until accepted.

## Form rule

Human form decisions outrank rendering defaults. Do not infer enduring preferences from provisional tool choices.

## Framework rule

`docs/argument-map.md` is a working AI-maintained structure, not automatic human endorsement.

Create `docs/frameworks/FW-xxx.md` only after explicit human framework approval. Do not silently rewrite approved snapshots.

## Evidence rule

Surface conflicts between evidence and active human commitments. Do not conceal contrary evidence and do not silently rewrite the human position.

## Artifact status

AI-expanded prose remains `DERIVED-PROVISIONAL` until the relevant final human approval has been recorded.

## Handoff criterion

A new competent agent should be able to continue the project from repository state without the original chat transcript.
