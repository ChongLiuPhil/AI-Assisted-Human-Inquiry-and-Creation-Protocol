# Persistent Research Memory

> **Language:** Chinese canonical: `PERSISTENT_MEMORY.zh-CN.md`; this English file is the synchronized mirror.

## Principle

> **Chat is temporary interaction context. The repository is durable shared research memory.**

HARC externalizes project-relevant state so that continuity does not depend on one model, one account, one vendor, or one conversation window.

## Promotion test

Not every sentence in a conversation needs to be committed.

A human instruction SHOULD be promoted into repository state when the answer to this question is **yes**:

> If a new AI agent took over tomorrow without this conversation, would losing this instruction change how it should continue the project?

If yes, persist it.

## What belongs where

| Durable state | Canonical location |
|---|---|
| Research meaning, theses, distinctions | `core/CONTENT_CORE.md` |
| Form, layout, style, artifact type | `core/FORM_CORE.md` |
| Historical human decisions | `core/DECISION_LOG.md` |
| Working Memory index | `docs/working-memory.zh-CN.md` |
| Highest-priority current objective | `docs/working-memory/current-focus.zh-CN.md` |
| Dynamic tasks/plans/pending decisions | `docs/working-memory/task-plan.zh-CN.md` |
| Human retrospective work log | `docs/working-memory/work-log.zh-CN.md` (not default AI context) |
| Current argument structure | `docs/argument-map.md` |
| Human-approved argument baseline | `docs/frameworks/FW-xxx.md` |
| Approval/synchronization state | `docs/framework-status.md` |
| Evidence and verification | `evidence/` |
| Zero-context bootstrap and repository context interface | `START_HERE.zh-CN.md`, `BOOTSTRAP_PROMPT.zh-CN.md`, `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`, `HARC_MANIFEST.yaml`, `HARC_CONTEXT_INTERFACE.yaml`, `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` |
| Collaboration rules | `AGENTS.zh-CN.md`, `protocol/` |
| Expanded output | `paper/`, `book/`, `article/`, etc. |

## No hidden dependency rule

A stable project decision MUST NOT exist only in:

- a transient chat turn;
- account-level AI memory;
- a model's inaccessible reasoning;
- an undocumented local formatting choice;
- one agent's private notes.

If it matters to future continuity, give it an explicit repository representation.

## Context-window independence is not infinite context

HARC does not claim that a model can read an indefinitely growing repository in one prompt.

Instead use **layered compression**.

### Active state

For routine takeover, keep the operational resume path concise:

- Working Memory Index;
- Current Focus;
- Task Plan;
- task-relevant Content/Form/Protocol Core;
- relevant recent decision entries;
- Working Argument Map;
- Framework Status;
- latest approved framework.

Work Log is historical state primarily for human retrospective review and is skipped by default during AI onboarding.

### Historical state

Allow to grow:

- Work Log and archived Work Log partitions;
- full logs;
- evidence notes;
- source inventories;
- archived drafts;
- older framework versions;
- analysis artifacts.

### Scaling procedure

When historical files become large:

1. preserve originals;
2. create dated archives or partitions;
3. create compact indexes and summaries;
4. keep active cores focused on current state;
5. retrieve historical detail only when relevant.

The objective is **recoverability**, not universal simultaneous ingestion.

## Repository-backed memory model

HARC now uses:

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

This means:

- GitHub stores the sole authoritative project state;
- the session does not maintain long-lived copies of Current Focus, Task Plan, Framework, Artifact, Core, or other dynamic state;
- the Agent selectively retrieves latest canonical files according to the current task;
- file excerpts in active context are temporary non-authoritative cache;
- relevant latest revisions are refetched before high-impact judgments and writes;
- after canonical writes, older cache becomes `STALE`;
- refetch when needed rather than synchronizing a second chat copy.

Session Context Bootstrap therefore retains only a Repository Resolver: how to find memory, not another copy of memory.

See `protocol/REPOSITORY_CONTEXT_INTERFACE.md` and `HARC_CONTEXT_INTERFACE.yaml`.

## New-agent reconstruction target

Before answering these questions, a new Agent should complete the Onboarding Handshake, activate `HARC REPOSITORY CONTEXT — ACTIVE`, read Working Memory Index -> Current Focus -> Task Plan for the operational resume point, then selectively retrieve authoritative state from the three long-term layers. Work Log is skipped unless historical reconstruction is required.

A new competent agent should be able to answer:

- What is the human currently trying to argue?
- What does the human currently want the artifact to look like?
- Which argument framework has actually been human-approved?
- Which AI suggestions remain unaccepted?
- Which high-impact uncertainties are awaiting human clarification?
- Which other issues remain unresolved?
- Which evidence conflicts matter?
- What should be changed next?

If the repository cannot answer these questions without the old chat, the persistence architecture is incomplete.
