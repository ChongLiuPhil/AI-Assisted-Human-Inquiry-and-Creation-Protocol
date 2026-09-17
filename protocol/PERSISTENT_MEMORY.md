# Persistent Research Memory

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
| Current argument structure | `docs/argument-map.md` |
| Human-approved argument baseline | `docs/frameworks/FW-xxx.md` |
| Approval/synchronization state | `docs/framework-status.md` |
| Evidence and verification | `evidence/` |
| Collaboration rules | `AGENTS.md`, `protocol/` |
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

Keep routinely readable:

- Content Core;
- Form Core;
- recent decision entries;
- Working Argument Map;
- Framework Status;
- latest approved framework.

### Historical state

Allow to grow:

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

## New-agent reconstruction target

A new competent agent should be able to answer:

- What is the human currently trying to argue?
- What does the human currently want the artifact to look like?
- Which argument framework has actually been human-approved?
- Which AI suggestions remain unaccepted?
- Which issues remain unresolved?
- Which evidence conflicts matter?
- What should be changed next?

If the repository cannot answer these questions without the old chat, the persistence architecture is incomplete.
