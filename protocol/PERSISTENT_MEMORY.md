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
| High-impact unresolved clarifications | `docs/clarification-register.md` |
| Current argument structure | `docs/argument-map.md` |
| Human-approved argument baseline | `docs/frameworks/FW-xxx.md` |
| Approval/synchronization state | `docs/framework-status.md` |
| Evidence and verification | `evidence/` |
| Zero-context bootstrap and handshake | `START_HERE.zh-CN.md`, `BOOTSTRAP_PROMPT.zh-CN.md`, `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`, `HARC_MANIFEST.yaml`, `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` |
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

Keep routinely readable:

- Content Core;
- Form Core;
- recent decision entries;
- current Critical Clarification Register;
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

## Two-layer memory model

HARC now distinguishes:

- **Durable Repository State** — recoverable, auditable long-term project state in GitHub;
- **Active Session Contract** — a compressed operating contract regenerated from the repository and echoed into the current conversation context.

The repository provides persistence; the session contract provides salience. If the session contract is lost, rebuild it from the repository rather than treating remembered conversation state as authoritative.

## New-agent reconstruction target

Before answering these questions, a new Agent should complete the Onboarding Handshake defined in `START_HERE.zh-CN.md` and reconstruct current state using the read order in `HARC_MANIFEST.yaml`.

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
