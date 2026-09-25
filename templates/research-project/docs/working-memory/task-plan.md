# HARC Project Working Memory — Task Plan

> **Language:** Chinese canonical: `task-plan.zh-CN.md`; this English file is the synchronized mirror.

**Status:** `ACTIVE TASK PLAN`

## ACTIVE TASKS

- `WM-T001 — ... — TODO / IN-PROGRESS / BLOCKED / WAITING-HUMAN`

## NEXT ACTIONS

1. `...`

## BLOCKERS

- `None / ...`

## PENDING HUMAN DECISIONS / CLARIFICATIONS

### CLR-001 — `...`

- Status: `WAITING-HUMAN`
- Severity: `BLOCKING / NON-BLOCKING`
- Uncertain point: `...`
- Candidate interpretations: `...`
- AI recommendation: `AI-PROPOSED — ...`
- Promotion destination: `Layer 1 / Layer 2 / Layer 3 / Form Core / Protocol Core`

## OPERATIONAL / PROVIDER STATE

- Project bootstrap state (when present): `project-bootstrap-state.yaml`
- Current pending human provider action: `None / ...`
- Agent resume condition: `None / ...`
- Memory write-back sync: `not-applicable / pending / synchronized`

Rules:

- before the human enters a provider UI, mark the matching Bootstrap State human step `waiting-human` and record the pending action/resume condition here;
- after the human returns, verify actual provider state before writing `completed / verified` to Bootstrap State;
- if Bootstrap State disagrees with provider actual state, record a SYNC DEFECT instead of using chat content as the repair source.

## TODO / BACKLOG

- `...`

## SYNC DEFECTS

- `None / ...`

## COMPLETION RULE

When a task completes:

1. remove it from the active list;
2. write a high-level completion summary to `work-log.zh-CN.md`;
3. promote stable normative results into Long-Term Memory;
4. update Current Focus if the immediate objective changes;
5. if the task changed external/provider state, synchronize `project-bootstrap-state.yaml`; append a high-level Work Log milestone after material bootstrap progress.
