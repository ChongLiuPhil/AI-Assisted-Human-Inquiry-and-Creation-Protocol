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

## 2. Working Memory is a functional area, not a fixed file

Working Memory specifies **logical roles**. A physical implementation may use one file or multiple files.

A compliant implementation should cover at least:

### 2.1 Working Memory Index / Resolver

A stable entry point mapping where Current Focus, Task Plan, and Work Log live; what is mandatory for onboarding; and what is retrieved only on demand.

The Index SHOULD avoid duplicating dynamic state.

### 2.2 Current Focus

The shortest, highest-salience operational state.

It should state at least:

- `CURRENT_STAGE`;
- `CURRENT_OBJECTIVE`;
- immediate/current-conversation work focus;
- `PRIMARY_BLOCKER`;
- `IMMEDIATE_NEXT_ACTION`;
- minimal handoff pointers.

It should let a replacement Agent recover direction quickly after an interruption.

### 2.3 Task Plan

Dynamic planning and TODO state.

It may contain:

- `ACTIVE_TASKS`;
- `NEXT_ACTIONS`;
- `TODO / BACKLOG`;
- `BLOCKERS`;
- `WAITING-HUMAN`;
- `PENDING_HUMAN_DECISIONS`;
- `CLARIFICATIONS`;
- `SYNC_DEFECTS`.

Completed tasks should leave the active list rather than accumulating indefinitely.

### 2.4 Work Log

A historical chronicle primarily for later human review.

It may record stage-level progress, milestones, completed task batches, direction changes, changes in intellectual/work path, expressed high-level reasons, and important phase transitions.

Work Log:

- SHOULD be updated periodically;
- SHOULD use high-level stage summaries;
- MUST NOT store hidden AI chain-of-thought, scratchpads, or unverifiable internal reasoning;
- MUST NOT serve as current normative state;
- SHOULD NOT be default required reading for AI onboarding;
- MAY be retrieved for human historical review, audit, change reconstruction, or investigation of historical/current-state conflicts.

### 2.5 Adaptable physical layout

A lightweight project may map:

`Index = Current Focus = Task Plan = Work Log = one file`

A complex project may use:

`Index + Current Focus + Task Plan + Work Log (+ archives)`

The manifest MUST explicitly map the actual roles.

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
- leave the active Task Plan;
- add a high-level historical completion summary to Work Log;
- retain Decision ID and durable destination paths where useful for audit.

The authoritative answer then lives in Long-Term Memory, not in the Working Memory item or Work Log.

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

## 8. Update discipline

### Current Focus

Update when the highest-priority objective, blocker, immediate task/conversation focus, or project phase changes, and before handoff.

### Task Plan

Update when tasks are created or change state, new clarifications/blockers appear, important human decisions occur, tasks complete, or Framework/Artifact gates change.

Completed items should leave the active list promptly.

### Work Log

Update periodically rather than after every micro-action.

Recommended write points include completed task batches, major protocol/research milestones, major human decisions that change direction, Framework/Artifact phase transitions, longer work-cycle completion, and explicit human requests for a stage chronicle.

Work Log is a **retrospective history**, not a real-time event stream.

## 9. Onboarding / Handoff

Recommended order:

1. control plane: Manifest / Context Interface / START_HERE / AGENTS;
2. Working Memory Index;
3. Current Focus;
4. Task Plan;
5. task-relevant three-layer Long-Term Memory;
6. required Evidence / Artifact.

**Skip Work Log by default.**

Read Work Log only when the human requests review, the reason for a direction change must be reconstructed, current state appears stale/inconsistent, or a dedicated audit/provenance reconstruction requires it.

Thus:

> **Current Focus tells the Agent what matters most now; Task Plan tells the Agent how to proceed; Work Log tells the human how the project got here.**

## 10. Scaling

Keep **Current Focus + Task Plan** short, current, and scannable.

Work Log may grow, but should use stage-level entries, split/archive by phase or year when necessary, retain an index, and remain outside default AI context.

Work Log, Decision Log, and Git history have different roles: human narrative review, normative-decision audit, and exact version history respectively.

## 11. Principle

> **The three long-term layers describe the research and its artifacts; Working Memory describes the current state of the research process.**

`Long-Term Memory = L1 Authorial Core -> L2 Current Framework -> L3 Derived Artifact`

Parallel:

`Working Memory Area = Index + Current Focus + Task Plan + Work Log`

where:

`Current Focus + Task Plan = operational resume state`

`Work Log = human retrospective history`

Promotion:

`Working Memory resolution -> appropriate Long-Term Memory destination`
