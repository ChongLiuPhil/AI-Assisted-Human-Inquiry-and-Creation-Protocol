# HARC Project Working Memory Index

> **Language:** Chinese canonical: `working-memory.zh-CN.md`; this English file is the synchronized mirror.

Working Memory is a functional area and does not have to be a single file.

The default template uses:

- Current Focus: `docs/working-memory/current-focus.zh-CN.md`
- Task Plan: `docs/working-memory/task-plan.zh-CN.md`
- Work Log: `docs/working-memory/work-log.zh-CN.md`

## Default takeover

1. read this Index;
2. read Current Focus;
3. read Task Plan;
4. if `project-bootstrap-state.yaml` exists and infrastructure/provider work is relevant, read the latest verified bootstrap state;
5. retrieve the three Long-Term Memory layers as required by the current task;
6. skip Work Log by default.

## Roles

- **Current Focus:** what matters most now;
- **Task Plan:** how work proceeds next;
- **Work Log:** helps the human later review how the project got here.
- **External Operational State** (when present): `project-bootstrap-state.yaml` stores the latest verified non-secret provider/bootstrap projection; the current blocker and next action are still mirrored into Current Focus / Task Plan.

Work Log is not a substantive truth source and does not record hidden AI chain-of-thought.

A lightweight project may merge multiple roles into one file, but the mapping must be explicit in `HARC_MANIFEST.yaml`.
