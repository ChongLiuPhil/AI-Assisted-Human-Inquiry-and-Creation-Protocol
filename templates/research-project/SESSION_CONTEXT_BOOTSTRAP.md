# HARC Project Session Context Bootstrap

> **Language:** Chinese canonical: `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`; this English file is the synchronized mirror.

## Purpose

The current session loads only a minimal **Repository Resolver**, not a duplicate dynamic project state.

```text
HARC REPOSITORY CONTEXT — ACTIVE

Source of truth:
- GitHub repository

Control:
- HARC_MANIFEST.yaml
- HARC_CONTEXT_INTERFACE.yaml

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

Dynamic Blocking Clarifications, Framework, Artifact, and Core state are fetched from latest canonical GitHub revisions when needed.

## Context Refresh

`HARC CONTEXT REFRESH` means reread manifest/context-interface, resolve current task dependencies, fresh-fetch them, discard stale cache, and continue. It does not copy the whole project state into chat.

## Write rule

After a canonical write, older context excerpts are immediately `STALE`. Refetch if later reasoning still depends on them.

## Principle

> **The session retains how to find memory, not another copy of memory.**
