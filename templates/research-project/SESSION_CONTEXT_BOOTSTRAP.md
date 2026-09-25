# AHICP Project Session Context Bootstrap

> **Language:** Chinese canonical: `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`; this English file is the synchronized mirror.

## Purpose

The current session loads only a minimal **Repository Resolver**, not a duplicate dynamic project state.

```text
AHICP REPOSITORY CONTEXT — ACTIVE

Source of truth:
- GitHub repository

Control:
- AHICP_MANIFEST.yaml
- AHICP_CONTEXT_INTERFACE.yaml

Working Memory:
- index: docs/working-memory.zh-CN.md
- current focus: docs/working-memory/current-focus.zh-CN.md
- task plan: docs/working-memory/task-plan.zh-CN.md
- work log: docs/working-memory/work-log.zh-CN.md (human-retrospective; not default read)
- operational state only; not long-term semantic authority

External operational state (when present):
- project bootstrap/provider projection: project-bootstrap-state.yaml
- repository-backed, non-secret, last-verified state only
- pending human provider action must also appear in Task Plan / Current Focus

Policy:
- repository-backed
- selective retrieval
- no authoritative session copy
- read latest before high-impact action
- read latest before write
- invalidate touched cache after write
- write-through to repository

Current task:
- route: CONTENT / FORM / PROTOCOL
- authoritative refs: [paths only]
```

Fresh-fetch Working Memory first when needed to determine the current stage and resume point; then selectively retrieve authoritative Layer 1 / Layer 2 / Layer 3 / Evidence state from latest canonical GitHub revisions.

## Context Refresh

`AHICP CONTEXT REFRESH` means reread manifest/context-interface, fresh-fetch Working Memory, fresh-fetch `project-bootstrap-state.yaml` when present and relevant, resolve long-term-memory dependencies for the current task, fresh-fetch those canonical files, discard stale cache, and continue. It does not copy the whole project state into chat.

## Write rule

After a canonical or `project-bootstrap-state.yaml` write, older context excerpts are immediately `STALE`. Refetch if later reasoning still depends on them. Before human provider-UI handoff, persist pending state; after the human returns, verify actual state before writing completion.

## Principle

> **The session retains how to find memory, not another copy of memory.**
