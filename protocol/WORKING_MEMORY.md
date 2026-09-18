# HARC Working Memory Protocol

> **Language:** Chinese canonical: `WORKING_MEMORY.zh-CN.md`; this English file is the synchronized mirror.

## 1. Definition

HARC distinguishes two kinds of project memory.

### A. Long-Term Research Memory

This stores what the project is, its durable intellectual structure, and the artifacts that constitute its long-term state.

It has three layers:

1. **Layer 1 — Human Authorial Core**
   - human-originated, corrected, confirmed, qualified, and progressively refined commitments;
   - Content Core / Form Core / Protocol Core;
   - Decision Log preserves historical decisions.

2. **Layer 2 — Current Framework**
   - current argument structure, core propositions, key concepts, inferential relations, and section functions;
   - constrained by Layer 1;
   - may contain structural material not stated item-by-item in Layer 1;
   - more mutable than Layer 1 while remaining durable project state;
   - Working Argument Map and Approved Framework snapshots represent different approval states within this layer.

3. **Layer 3 — Derived Artifact**
   - paper, book, report, article, or other complete artifact;
   - primarily expanded from Layer 2;
   - must remain compatible with Layer 1 and evidence constraints;
   - may pass through DERIVED-PROVISIONAL -> FINAL-REVIEW -> FINAL-APPROVED.

### B. Working Memory

Working Memory is **parallel** to the three layers. It is not Layer 1.5 and not a fourth long-term semantic layer.

It answers:

- what stage is the project in?
- what is the current objective?
- what is being worked on now?
- what has been completed?
- what remains?
- what comes next?
- what is waiting for human confirmation?
- what is blocking progress?
- what synchronization defects, TODOs, and handoff notes remain?

Principle:

> **Long-term memory stores what the project is; Working Memory stores where the project currently is in its work.**

## 2. Typical contents

Working Memory SHOULD contain:

- `CURRENT_STAGE`;
- `CURRENT_OBJECTIVE`;
- `ACTIVE_TASKS`;
- `NEXT_ACTIONS`;
- `RECENTLY_COMPLETED`;
- `BACKLOG / TODO`;
- `BLOCKERS`;
- `PENDING_HUMAN_DECISIONS`;
- `CLARIFICATIONS`;
- `SYNC_DEFECTS`;
- `HANDOFF_NOTE`.

Temporary analysis may appear only when clearly marked non-authoritative and disposable.

## 3. Authority boundary

Working Memory is durable **operational state**, but not the final authority for substantive long-term claims.

If it conflicts with canonical long-term files, the canonical long-term state governs and Working Memory must be repaired.

Working Memory should primarily store status plus pointers rather than duplicate fully promoted normative content.

## 4. Clarification is no longer an independent layer

Critical Clarification is a record type inside Working Memory, not an independent Layer 1.5.

When high-impact uncertainty is detected:

`ambiguity -> Working Memory / Clarification item -> human resolution`

Unresolved clarification is not a human commitment and may be `BLOCKING` or `NON-BLOCKING`.

## 5. Promotion from Working Memory to Long-Term Memory

When an item receives human resolution or becomes a stable result, perform **Promotion**.

### 5.1 Human core claim / concept / scope

`Working Memory -> Decision Log -> Layer 1 Content Core -> Layer 2 Framework -> Layer 3 Artifact`

### 5.2 Form decision

`Working Memory -> Decision Log -> Form Core -> affected Framework/Artifact if applicable`

### 5.3 Protocol decision

`Working Memory -> Decision Log -> Protocol Core / Specification -> Agent behavior / templates`

### 5.4 Pure framework-structural decision

If a structural decision is not itself a foundational human-content claim but becomes part of the current research architecture:

`Working Memory -> Decision Log when human-confirmed -> Layer 2 Working Framework / Approved Framework`

Do not promote temporary AI inference into Layer 1 merely to clear Working Memory.

## 6. After Promotion

After Promotion, the Working Memory item should:

- leave `ACTIVE / WAITING-HUMAN / BLOCKED`;
- become `RESOLVED / PROMOTED`;
- record its Decision ID;
- record destination paths;
- move to a compact Recently Resolved / Archive section.

The authoritative answer then lives in long-term memory, not in the Working Memory entry.

## 7. Work-state lifecycle

Recommended statuses:

- `TODO`
- `IN-PROGRESS`
- `WAITING-HUMAN`
- `BLOCKED`
- `RESOLVED`
- `PROMOTED`
- `SUPERSEDED`
- `ARCHIVED`

Clarification severity may still use `BLOCKING` / `NON-BLOCKING`.

## 8. Update points

Update Working Memory when:

- a clear work objective begins;
- a task completes;
- the human gives an important decision;
- a new clarification/blocker appears;
- a clarification is resolved and promoted;
- Framework status changes;
- Artifact stage changes;
- a substantial work cycle ends;
- before Agent handoff;
- onboarding detects stale Working Memory.

## 9. Onboarding / Handoff

Recommended order for a replacement Agent or human collaborator:

1. read the control plane: `HARC_MANIFEST.yaml`, `HARC_CONTEXT_INTERFACE.yaml`, START_HERE / AGENTS;
2. read `docs/working-memory.zh-CN.md`;
3. learn current stage, objective, tasks, blockers, and pending decisions;
4. selectively retrieve latest canonical state from the three long-term layers for the current task;
5. never treat Working Memory as the long-term semantic truth source.

Working Memory is the **resume index**; long-term memory is the **authoritative research state**.

## 10. Scaling

Keep Working Memory short, current, and scannable.

As history grows:

- keep only current work in Active;
- compress resolved/promoted items into an index;
- move detailed history to archives;
- rely on Decision Log and Git history for durable audit.

## 11. Principle

> **The three long-term layers describe the research and its artifacts; Working Memory describes the current state of the research process.**

`Long-Term Memory = L1 Authorial Core -> L2 Current Framework -> L3 Derived Artifact`

Parallel:

`Working Memory <-> current goals / tasks / clarifications / blockers / handoff`

Promotion:

`Working Memory resolution -> appropriate Long-Term Memory destination`
