# AGENTS.md — Project HARC Contract

> **Language:** Chinese canonical: `AGENTS.zh-CN.md`; this English file is the synchronized mirror.

This project follows the Human–AI Research Collaboration Protocol.

## Zero-context onboarding

Any new AI Agent must first read:

1. `START_HERE.zh-CN.md`
2. `HARC_MANIFEST.yaml`

Then reconstruct project state according to the manifest and output a HARC Onboarding Report before substantive work.

Before the onboarding handshake is complete, do not perform large-scale structural changes, Framework Approval, or promote AI proposals into human commitments.

## Protocol source

Record the protocol source used to initialize this project:

- Upstream repository: `ChongLiuPhil/Human-AI-Research-Collaboration-Protocol`
- HARC version: `0.2.0-draft` (replace with the actual adopted version/tag/commit)
- Adopted commit/tag: `UNRESOLVED — record when initializing`

A future agent should not silently assume that the latest upstream HARC rules were already adopted by this project. Protocol upgrades should be explicit project decisions.

## Chinese canonical / English mirror

This template defaults to Chinese as the canonical editing/review language and English as the synchronized mirror. Substantive changes must update both in the same work cycle. If the versions conflict, Chinese governs until English is repaired.

## Required reading order

Before substantive work, read:

1. `core/CONTENT_CORE.zh-CN.md`
2. `core/FORM_CORE.zh-CN.md`
3. recent `core/DECISION_LOG.zh-CN.md`
4. `docs/clarification-register.zh-CN.md`
5. `docs/framework-status.zh-CN.md`
6. latest approved framework, if any
7. `docs/argument-map.zh-CN.md`
8. relevant artifact and evidence files
9. corresponding English mirrors for bilingual parity

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

## Clarification Register rule

If high-impact uncertainty concerns a core position, key concept, terminology/translation, scope, major inference, or section function, record it first in `docs/clarification-register.zh-CN.md`; do not silently select an interpretation.

Mark entries `BLOCKING / NON-BLOCKING`. After human resolution, promote the result into the Decision Log and appropriate Core, then update the Argument Map and artifact.

Run a Clarification Scan before Framework Approval, formal translation, large-scale expansion, and Final Review.

## Framework rule

`docs/argument-map.zh-CN.md` is a working AI-maintained structure, not automatic human endorsement.

Create `docs/frameworks/FW-xxx.zh-CN.md` plus its English mirror only after explicit human framework approval. Do not silently rewrite approved snapshots.

The approved framework is the primary substantive intellectual baseline. Distinguish framework-level defects from local defects introduced only during later AI expansion.

## Evidence rule

Surface conflicts between evidence and active human commitments. Do not conceal contrary evidence and do not silently rewrite the human position.

## Artifact status

AI-expanded prose remains `DERIVED-PROVISIONAL` until the relevant final human approval has been recorded.

## Handoff criterion

A new competent agent should be able to continue the project from repository state without the original chat transcript.


## Bilingual synchronization rule

Chinese is canonical. Every substantive change must update the English mirror in the same work cycle. A bilingual mismatch is a synchronization defect.
