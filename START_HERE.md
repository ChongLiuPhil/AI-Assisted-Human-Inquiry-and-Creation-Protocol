# START HERE — HARC Zero-Context Onboarding Entry

> **Language:** Chinese canonical: `START_HERE.zh-CN.md`; this English file is the synchronized mirror.
>
> This file is for a new AI Agent starting with **zero prior context, no old chat, and no platform memory**.

## 0. First principle

Before substantive research, structural revision, drafting, translation, formatting, or approval judgment:

**reconstruct current repository state first; do not infer project state from the current chat.**

HARC's durable truth source is the repository, not a previous Agent's memory.

## 1. Required read order

Read Chinese canonical files in this order; use English only for parity checking:

1. `HARC_MANIFEST.yaml`
2. `HARC_CONTEXT_INTERFACE.yaml`
3. `BOOTSTRAP_PROMPT.zh-CN.md`
4. `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
5. `AGENTS.zh-CN.md`
6. `docs/working-memory.zh-CN.md` — Working Memory Index
7. `docs/working-memory/current-focus.zh-CN.md` — determine the highest-priority objective, blocker, and immediate next action
8. `docs/working-memory/task-plan.zh-CN.md` — retrieve dynamic tasks, TODOs, pending decisions, and plan
9. `protocol/ONBOARDING_HANDSHAKE.zh-CN.md`
10. task-relevant Layer 1 canonical Core / Decision Log
11. task-relevant Layer 2 Framework state
12. task-relevant Layer 3 Artifact / Evidence
13. corresponding English mirrors only for parity checking

The old `docs/clarification-register.zh-CN.md` is only a compatibility pointer and no longer carries active state.

`docs/working-memory/work-log.zh-CN.md` is primarily for human retrospective review and is outside the mandatory read order by default. Retrieve it only for historical review, audit, change reconstruction, or current/history conflict.

For the HARC methodology article, exact paths are listed in `HARC_MANIFEST.yaml`.

## 2. Do not act before onboarding

Before the onboarding handshake is complete, do not:

- infer canonical state from chat;
- promote AI proposals into human commitments;
- treat unresolved Clarification as resolved;
- create an Approved Framework;
- perform large-scale Working Argument Map restructuring;
- perform large-scale manuscript rewriting;
- use English mirrors to overwrite Chinese canonical state;
- ignore existing `BLOCKING` Clarifications;
- infer author preferences from tool defaults.

## 3. Onboarding handshake: output a HARC Onboarding Report first

After the required reading, output a concise but structured **HARC Onboarding Report**. Recommended template: `ONBOARDING_REPORT_TEMPLATE.zh-CN.md`. The report must also follow `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` and confirm:

`HARC REPOSITORY CONTEXT — ACTIVE`

This loads only the repository-access kernel, not a duplicate dynamic project state. The report summary is for human verification only; later work must refetch latest canonical repository state on demand.

### A. Protocol state

- adopted HARC version / commit if recorded;
- canonical language;
- applicable protocol files;
- any protocol-version or synchronization defect.

### B. Human-confirmed state

- current research purpose;
- main human commitments;
- active form/presentation decisions;
- recent important human decisions.

### C. Working Memory state

- Current Focus: CURRENT_STAGE / CURRENT_OBJECTIVE / PRIMARY_BLOCKER / IMMEDIATE_NEXT_ACTION;
- Task Plan: ACTIVE_TASKS / NEXT_ACTIONS / TODO / BACKLOG;
- BLOCKERS;
- PENDING_HUMAN_DECISIONS / Clarifications;
- SYNC_DEFECTS;
- questions requiring human resolution before continuing.

Work Log need not be restated in the Onboarding Report.

### D. Framework / Artifact state

- Working Framework status;
- latest Approved Framework, if any;
- current derived-artifact status;
- Framework Approval / Final Artifact Approval status.

### E. Permitted next action

State what work may safely continue, what is blocked by Clarification/approval gates, and which HARC propagation path applies to the current request.

## 4. Standard propagation

For an explicit human decision:

`Human decision -> Decision Log -> appropriate Core -> Clarification cleanup if needed -> Working Argument Map -> Derived Artifact -> bilingual parity check`

For high-impact ambiguity:

`Ambiguous high-impact input -> Working Memory / Clarification -> human resolution -> Promotion -> Decision Log -> appropriate Long-Term Memory destination`

AI proposals remain `AI-PROPOSED` until accepted.

## 5. Clarification-first rule

If uncertainty could materially affect a core position, central thesis, key concept, major inference, scope, section function, key primary-language terminology, translation correspondence, or framework structure, do not guess. Put it into the Clarification queue in Task Plan first:

`docs/working-memory/task-plan.zh-CN.md`

## 6. Bilingual rule

Normal direction:

`Human decision -> Chinese canonical -> English synchronized mirror`

Pre-cutover English-ahead legacy catch-up is a historical migration exception, not a normal workflow.

## 7. Successful onboarding criterion

Onboarding is complete only if the Agent can answer from repository state alone:

1. What has the human actually confirmed?
2. What remains AI-proposed?
3. Which high-impact issues await human clarification?
4. What is the Working / Approved Framework state?
5. What is the artifact approval state?
6. What may proceed and what is blocked?
7. Are Chinese canonical and English mirror synchronized?

If not, repair the onboarding/persistence defect before large-scale work.

---

# Copyable bootstrap prompt

> You are taking over a research repository governed by the Human–AI Research Collaboration Protocol (HARC). Do not rely on prior chat, account memory, or your own inference to reconstruct project state. First read `START_HERE.zh-CN.md` and `HARC_MANIFEST.yaml`, then follow the required read order. Chinese is canonical and English is the synchronized mirror. Before making any substantive change, output a HARC Onboarding Report covering human commitments, Form state, Current Focus, Task Plan, Blocking/Non-blocking Clarifications, Working/Approved Framework state, Artifact status, synchronization defects, and the permitted next step for the current request. If uncertainty could materially affect core claims, key concepts, terminology/translation, scope, inference, or argument structure, do not guess; write it into the Clarification queue in `docs/working-memory/task-plan.zh-CN.md` and ask for human resolution. Every explicit human decision must first enter the Decision Log and appropriate Core before propagating to the Argument Map and derived artifact. Never treat a Working Framework as human-approved without explicit Framework Approval.
