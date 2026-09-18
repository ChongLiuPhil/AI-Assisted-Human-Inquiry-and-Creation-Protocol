# HARC Session Context Bootstrap

> **Language:** Chinese canonical: `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`; this English file is the synchronized mirror.

## 0. Revised role

This file no longer asks an AI Agent to duplicate dynamic project state into the current conversation.

It loads only a minimal **Repository Resolver / Context Kernel** that tells the Agent:

- GitHub is the sole authoritative project-state source;
- where the manifest and context-interface live;
- Chinese-canonical / English-mirror priority;
- how to retrieve selectively by task;
- when latest revisions must be refetched;
- how stale cache is invalidated after writes.

Dynamic project state is not maintained here or as a long-lived session copy.

## 1. Minimal kernel

After bootstrap, the Agent should confirm:

```text
HARC REPOSITORY CONTEXT — ACTIVE

Source of truth:
- GitHub repository

Control files:
- HARC_MANIFEST.yaml
- HARC_CONTEXT_INTERFACE.yaml

Working Memory:
- index: docs/working-memory.zh-CN.md
- current focus: docs/working-memory/current-focus.zh-CN.md
- task plan: docs/working-memory/task-plan.zh-CN.md
- work log: docs/working-memory/work-log.zh-CN.md (human-retrospective; not default read)
- operational state only; not long-term semantic authority

Language:
- Chinese canonical
- English synchronized mirror

Context policy:
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

This block stores only control information and file references, not dynamic Blocking Clarifications, Framework, Artifact, or Core content.

## 2. Using dynamic state

If a task needs current Blocking Clarifications, Framework Status, latest Approved Framework, Artifact status, Core content, or recent human decisions, the Agent must read the latest canonical GitHub files directly.

Earlier appearance of those values in chat does not remove the need for fresh retrieval.

## 3. Context Refresh

`HARC CONTEXT REFRESH` means:

1. reread `HARC_MANIFEST.yaml`;
2. reread `HARC_CONTEXT_INTERFACE.yaml`;
3. fresh-fetch Working Memory Index + Current Focus + Task Plan and confirm the resume point;
4. skip Work Log by default;
5. resolve long-term-memory dependencies for the current task;
6. fresh-fetch those files;
7. discard stale cache;
8. continue work.

It does not mean copying the whole project state back into chat.

## 4. Revised two-layer model

Not:

`Repository State + Duplicated Session State`

but:

`Repository State + Minimal Session Resolver`

where repository is durable authoritative memory, the Session Resolver is control plane, and retrieved excerpts are transient non-authoritative cache.

## 5. Mandatory refresh points

Refetch relevant GitHub state:

- before high-impact decisions;
- before Clarification resolution;
- before Framework Approval;
- before Final Artifact Review;
- before writing a target file;
- after relevant repository changes;
- when cache may be stale;
- when revision tokens do not match expectations.

## 6. Post-write cache rule

After any canonical file changes:

- old excerpts become `STALE`;
- old onboarding summaries cannot remain authoritative;
- refetch if later reasoning depends on the file;
- do not maintain a second updated chat copy.

## 7. Platform precedence

This kernel is not a true platform system prompt.

`Platform system/developer rules > HARC Repository Resolver > ordinary AI defaults`

## 8. Principle

> **The session retains how to find memory, not another copy of memory.**
