# HARC Working Memory Index

> **Language:** Chinese canonical: `working-memory.zh-CN.md`; this English file is the synchronized mirror.

**Role:** stable resolver for the Working Memory Area.  
**Note:** this file does not duplicate dynamic task state; it only maps logical roles to their locations.

## Logical components

### 1. Current Focus

Path:

`docs/working-memory/current-focus.zh-CN.md`

Purpose:

- current stage;
- most important current objective;
- immediate/current-conversation work focus;
- most important blocker;
- immediate next action.

**Highest-priority Working Memory read during takeover.**

### 2. Task Plan

Path:

`docs/working-memory/task-plan.zh-CN.md`

Purpose:

- active tasks;
- TODO / backlog;
- WAITING-HUMAN / BLOCKED items;
- pending human decisions / Clarifications;
- next actions;
- current synchronization defects.

Completed tasks leave the active list. Their historical summary goes into Work Log; stable normative results are separately promoted into Long-Term Memory.

### 3. Work Log

Path:

`docs/working-memory/work-log.zh-CN.md`

Purpose:

- human retrospective review;
- stage-level progress;
- major work transitions;
- changes in intellectual/work direction;
- completed task batches;
- milestones.

**Not default required reading for AI onboarding.**

Retrieve it only when the human requests historical review, when change history must be reconstructed, when current state conflicts with history, or during dedicated audit.

Work Log does not store hidden model chain-of-thought or scratchpads.

## Default takeover sequence

`Manifest / Context Interface -> Working Memory Index -> Current Focus -> Task Plan -> task-relevant Long-Term Memory`

Work Log is outside the default mandatory-read chain.

## Authority boundary

- most important current objective: Current Focus;
- current plan/tasks/blockers/pending decisions: Task Plan;
- historical chronicle: Work Log, but it does not override current state;
- durable substantive claims: Layer 1 / Layer 2 / Layer 3 canonical files.

## Single-file compatibility

A lightweight project may map Index, Current Focus, Task Plan, and Work Log to one file; a complex project may split them. The manifest must state the mapping explicitly.
