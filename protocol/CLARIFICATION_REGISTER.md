# Clarification Workflow inside HARC Working Memory

> **Language:** Chinese canonical: `CLARIFICATION_REGISTER.zh-CN.md`; this English file is the synchronized mirror.

## Status

The former model treating Critical Clarification Register as “Layer 1.5” has been superseded by HARC-D021.

Clarification is now an item type inside `Working Memory`, not an independent layer.

Current active Working Memory:

`docs/working-memory.zh-CN.md`

Full Working Memory protocol:

`protocol/WORKING_MEMORY.zh-CN.md`

## When to create a Clarification item

Create a Working Memory Clarification when high-impact, non-trivial uncertainty concerns authorial intent, core claims, key concepts, scope, inferential relations, section functions, key terminology, source-language/English correspondence, or conflict between new feedback and durable memory.

Do not silently guess and propagate.

## Minimum fields

- ID;
- status;
- `BLOCKING / NON-BLOCKING` severity;
- category;
- uncertain point;
- candidate interpretations;
- why it matters;
- affected long-term-memory destinations;
- AI recommendation if any, marked `AI-PROPOSED`;
- question for the human.

## Resolution / Promotion

After human resolution:

`Working Memory Clarification -> Decision Log -> appropriate Long-Term Memory destination`

For human core content:

`Layer 1 Core -> Layer 2 Framework -> Layer 3 Artifact`

Form / Protocol decisions go to their durable Cores; purely structural framework results go to Layer 2.

After Promotion:

- mark the item `RESOLVED / PROMOTED`;
- record Decision ID;
- record destination files;
- remove it from the active Clarification queue.

## Compatibility

The old `docs/clarification-register.zh-CN.md` path remains as a compatibility pointer so old Agents, links, and historical references do not break.

Active Clarification state must live only in `docs/working-memory.zh-CN.md`. Do not maintain two Clarification truth sources.
