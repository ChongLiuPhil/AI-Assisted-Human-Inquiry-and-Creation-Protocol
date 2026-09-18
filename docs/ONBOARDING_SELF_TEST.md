# Zero-Context Onboarding Self-Test

**Date:** 2026-09-18  
**Status:** `PASS — HISTORICAL SNAPSHOT; LIVE STATE SUPERSEDED`  
**Role:** AI-maintained historical onboarding/conformance snapshot, not current dynamic state and not a new normative truth source.  
**Language:** Chinese canonical: `ONBOARDING_SELF_TEST.zh-CN.md`; this English file is the synchronized mirror.

> **Important:** this file preserves the simulated Current Focus / blockers / Clarifications that existed when the test was run. Project state has continued to evolve, so these dynamic values MUST NOT be used to reconstruct the present. Fresh-fetch `docs/working-memory/current-focus.zh-CN.md`, `docs/working-memory/task-plan.zh-CN.md`, and the relevant Framework Status for live state. Future onboarding self-tests should record the tested commit/revision so the snapshot boundary is machine-verifiable.

## 1. Method

Simulate a new AI Agent with no old chat or account memory, reconstructing current project state only from:

1. `HARC_MANIFEST.yaml`
2. `HARC_CONTEXT_INTERFACE.yaml`
3. `START_HERE.zh-CN.md`
4. `BOOTSTRAP_PROMPT.zh-CN.md`
5. `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
6. `AGENTS.zh-CN.md`
7. `docs/working-memory.zh-CN.md` (Index);
8. `docs/working-memory/current-focus.zh-CN.md`;
9. `docs/working-memory/task-plan.zh-CN.md`;
10. task-relevant state from the three Long-Term Memory layers / Evidence resolved by the manifest/context interface.

`docs/working-memory/work-log.zh-CN.md` is skipped by default.

No unpersisted information from the current chat is treated as project state.

---

# 2. Simulated HARC Onboarding Report

## A. Protocol state

- HARC version: `0.2.0-draft`
- canonical language: `zh-CN`
- English: synchronized mirror
- zero-context entry set:
  - `START_HERE.zh-CN.md`
  - `BOOTSTRAP_PROMPT.zh-CN.md`
  - `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
  - `HARC_MANIFEST.yaml`
  - `HARC_CONTEXT_INTERFACE.yaml`
  - `AGENTS.zh-CN.md`
  - `protocol/ONBOARDING_HANDSHAKE.zh-CN.md`
  - `ONBOARDING_REPORT_TEMPLATE.zh-CN.md`
- current protocol commitments: P1–P24
- recent human protocol decisions: HARC-D015 through HARC-D022
- D018–D022 are human-confirmed; D021 replaces Layer 1.5 with parallel Working Memory and D022 modularizes Working Memory into Current Focus / Task Plan / Work Log.

**Protocol conclusion:** discoverable and reconstructable from repository state.

## B. Human-confirmed current state

### B1. HARC purpose

HARC is an independent, GitHub-centered, reusable human–AI research collaboration protocol with two outputs:

1. an executable open protocol/template system;
2. a methodology article governed by HARC itself.

### B2. Main confirmed commitments

Repository state supports at least:

- durable project state lives in the repository rather than chat/agent memory;
- Content and Form are separated;
- human decisions propagate upstream-first;
- AI maintains a Working Argument Map that is not automatically human-approved;
- Framework Approval is distinct from Final Artifact Approval;
- AI expansion must preserve framework fidelity;
- Chinese canonical / English synchronized mirror;
- the three content layers are Long-Term Research Memory;
- Working Memory runs in parallel with the three long-term layers;
- Current Focus stores the highest-priority objective, Task Plan stores dynamic tasks/blockers/pending decisions, and Work Log primarily supports human retrospective review;
- Work Log is outside default AI onboarding context;
- Clarification is a Task Plan / Working Memory item, not Layer 1.5;
- a replacement Agent must complete zero-context bootstrap + Onboarding Handshake before substantive work.

### B3. Methodology-article Form state

- artifact type: `ACADEMIC_PAPER / METHODOLOGY ARTICLE`
- Chinese: canonical
- English: synchronized mirror
- detailed typography, layout, citation style, target venue: `UNRESOLVED`
- current Markdown / author–year presentation: working defaults, not permanent author preferences.

## C. Working Memory state

### C1. Current Focus

- CURRENT_STAGE: HARC v0.2 Working Memory Area is modularized; methodology article is in human clarification / Framework Approval preparation;
- CURRENT_OBJECTIVE: resolve `CLR-001 / CLR-002 / CLR-005` so `MA-FW-001` can be reassessed;
- PRIMARY_BLOCKER: `WAITING-HUMAN: CLR-001 / CLR-002 / CLR-005`;
- IMMEDIATE_NEXT_ACTION: present the three blockers together to the human and await resolution.

### C2. Task Plan — Blockers / Pending Human Decisions

Framework Approval blockers:

- `CLR-001`
- `CLR-002`
- `CLR-005`

Formal release blocker:

- `CLR-009`

Non-blocking pending items:

- `CLR-003`
- `CLR-004`
- `CLR-006`
- `CLR-007`
- `CLR-008`
- `CLR-010`

### C3. Handoff / next actions

- prioritize `CLR-001 / CLR-002 / CLR-005`;
- after resolution, perform Promotion and synchronize Article Content Core / Argument Map / Draft;
- do not treat Working Memory summaries as durable substantive authority; substantive judgments still use latest canonical Layer 1/2/3 state.

## D. Framework state

- Working Framework: `WORKING-FRAMEWORK — REVIEW READY / WORKING-MEMORY CLARIFICATION GATE OPEN`
- latest Approved Framework: **none**
- next identifier: `MA-FW-001`
- Framework Approval: `NOT COMPLETED`
- Working Memory / Clarification Gate: `OPEN`
- permission to create `MA-FW-001`: **no**

**Correct action:** resolve or explicitly defer `CLR-001 / CLR-002 / CLR-005`, then perform overall Framework Approval.

## E. Artifact state

- Chinese: `paper/METHODOLOGY_ARTICLE.zh-CN.md`
- English: `paper/METHODOLOGY_ARTICLE.en.md`
- status: `DERIVED-PROVISIONAL`
- Working Framework -> current manuscript: `PARTIALLY SYNC`
- Final Artifact Approval: `NOT COMPLETED`

**Correct action:** do not perform a large structural rewrite that assumes framework approval, and do not describe the manuscript as final/submission-ready.

## F. Evidence state

- main evidence file: `evidence/METHODOLOGY_SOURCES.zh-CN.md`
- current policy/literature verification: `RECHECKED 2026-09-17`
- venue-specific time-sensitive policy must be rechecked once a target venue is chosen.

## G. Bilingual state

- Chinese canonical;
- English synchronized mirror;
- every substantive Chinese edit must synchronize English in the same work cycle;
- legacy English-ahead catch-up is a historical migration exception, not a normal workflow.

## H. Permitted next action

### Safe

- continue protocol implementation, auditing, and onboarding-infrastructure work;
- present pending human decisions / Clarifications from Working Memory to the human;
- continue evidence/non-substantive maintenance not dependent on Blocking Clarifications;
- prepare candidate analysis without treating any candidate as accepted.

### Blocked

- create `MA-FW-001`;
- claim the methodology framework has human approval;
- lock the philosophical framing through large-scale rewriting based on unresolved `CLR-001 / 002 / 005`;
- Final Artifact Approval;
- describe the public repository as legally open-source/open-content before the license is decided.

## J. Repository Context Resolver

The test Agent activates from `HARC_CONTEXT_INTERFACE.yaml` and `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`:

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
- route: PROTOCOL
- authoritative refs:
  - core/PROTOCOL_CORE.zh-CN.md
  - core/DECISION_LOG.zh-CN.md
  - protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md
```

**Repository context active: `YES`**

Working Memory Index + Current Focus + Task Plan are fresh-fetched for resumption; Work Log is skipped by default; substantive Layer 1 / Layer 2 / Layer 3 state is still retrieved from its canonical files rather than copied into the resolver.

## I. Onboarding conclusion

**`PASS`**

Because a new Agent can reconstruct from repository state:

- the human/AI authority boundary;
- current stage / highest-priority objective / primary blocker / immediate next action from Current Focus;
- active tasks / blockers / pending decisions from Task Plan;
- blocking Clarifications and their long-term impact;
- the absence of an Approved Framework;
- the `DERIVED-PROVISIONAL` artifact state;
- Chinese-canonical / English-mirror governance;
- what work is currently gated;
- how to activate the Repository Resolver without duplicating dynamic project state;
- how to fresh-fetch current state from latest canonical GitHub revisions;
- how to treat older session excerpts as non-authoritative cache.

Read-order numbering and standalone prompt/report discoverability defects found during implementation were repaired before this test.

---

# 3. Conformance conclusion

The current repository supports a working zero-context onboarding path:

`Repository access -> Manifest / Context Interface -> WM Index -> Current Focus -> Task Plan -> Selective Long-Term Retrieval -> Onboarding Report -> Repository Resolver -> Gated Work`

This test shows that **the current repository can support one successful self-hosted takeover**. It does not prove every external AI platform will automatically discover the entry files.

For cross-platform use, the recommended explicit human startup instruction remains:

> **“Read BOOTSTRAP_PROMPT.zh-CN.md in this repository and execute it strictly.”**

Future work should repeat the test across different Agents/platforms as a cross-agent handoff benchmark.
