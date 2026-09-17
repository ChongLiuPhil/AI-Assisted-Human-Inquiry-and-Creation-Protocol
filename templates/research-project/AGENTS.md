# AGENTS.md — Project HARC Contract

This project follows the Human–AI Research Collaboration Protocol.

## Protocol source

Record the protocol source used to initialize this project:

- Upstream repository: `ChongLiuPhil/Human-AI-Research-Collaboration-Protocol`
- HARC version: `0.1.0-draft` (replace with the actual adopted version/tag/commit)
- Adopted commit/tag: `UNRESOLVED — record when initializing`

A future agent should not silently assume that the latest upstream HARC rules were already adopted by this project. Protocol upgrades should be explicit project decisions.

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

Where applicable, distinguish reusable author preferences, artifact-type profiles, project-specific rules, external constraints, and temporary defaults.

## Framework rule

`docs/argument-map.md` is a working AI-maintained structure, not automatic human endorsement.

Create `docs/frameworks/FW-xxx.md` only after explicit human framework approval. Do not silently rewrite approved snapshots.

The approved framework is the primary substantive intellectual baseline. Distinguish framework-level defects from local defects introduced only during later AI expansion.

## Evidence rule

Surface conflicts between evidence and active human commitments. Do not conceal contrary evidence and do not silently rewrite the human position.

## Artifact status

AI-expanded prose remains `DERIVED-PROVISIONAL` until the relevant final human approval has been recorded.

## Handoff criterion

A new competent agent should be able to continue the project from repository state without the original chat transcript.
