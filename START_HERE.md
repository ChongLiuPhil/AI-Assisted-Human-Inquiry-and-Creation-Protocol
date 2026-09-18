# START HERE — HARC Zero-Context Onboarding Entry

> **Language:** Chinese canonical: `START_HERE.zh-CN.md`; this English file is the synchronized mirror.
>
> This file is for a new AI Agent starting with **zero prior context, no old chat, and no platform memory**.

## 0. First principle

Before substantive research, structural revision, drafting, translation, formatting, or approval judgment:

**reconstruct current repository state first; do not infer project state from the current chat.**

The durable truth source is the repository, not a previous agent's memory.

## 1. Required read order

Read Chinese canonical files in this order; use English only for parity checking:

1. `HARC_MANIFEST.yaml`
2. `BOOTSTRAP_PROMPT.zh-CN.md`
3. `AGENTS.zh-CN.md`
4. `protocol/ONBOARDING_HANDSHAKE.zh-CN.md`
3. `core/PROTOCOL_CORE.zh-CN.md`
4. recent `core/DECISION_LOG.zh-CN.md`
5. current project Content Core / Form Core
6. `docs/clarification-register.zh-CN.md`
7. Framework Status
8. latest Approved Framework, if any
9. Working Argument Map
10. evidence directly relevant to the task
11. derived artifact directly relevant to the task
12. corresponding English mirrors for bilingual parity

For the HARC methodology article, exact paths are listed in `HARC_MANIFEST.yaml`.

## 2. Do not act before onboarding

Before the onboarding handshake is complete, do not:

- infer canonical state from chat;
- promote AI proposals into human commitments;
- treat unresolved clarification as resolved;
- create an Approved Framework;
- perform large-scale framework restructuring;
- perform large-scale manuscript rewriting;
- use English mirrors to overwrite Chinese canonical state;
- ignore existing `BLOCKING` clarifications;
- infer author preferences from tool defaults.

## 3. Onboarding handshake: output a HARC Onboarding Report first

After the required reading, output the HARC Onboarding Report. Recommended template: `ONBOARDING_REPORT_TEMPLATE.zh-CN.md`.

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

### C. Critical Clarification state

- all current `BLOCKING` clarifications;
- task-relevant `NON-BLOCKING` clarifications;
- questions that require human resolution before proceeding.

### D. Framework / Artifact state

- Working Framework status;
- latest Approved Framework, if any;
- current derived-artifact status;
- Framework Approval / Final Artifact Approval status.

### E. Permitted next action

State what work may safely continue, what is blocked by clarification/approval gates, and which HARC propagation path applies to the current user request.

## 4. Standard propagation

For an explicit human decision:

`Human decision -> Decision Log -> appropriate Core -> clarification cleanup if needed -> Working Argument Map -> Derived Artifact -> bilingual parity check`

For high-impact ambiguity:

`Ambiguous high-impact input -> Clarification Register -> human resolution -> Decision Log -> appropriate Core -> Working Argument Map -> Derived Artifact`

AI proposals remain `AI-PROPOSED` until accepted.

## 5. Clarification-first rule

If uncertainty could materially affect a core position, central thesis, key concept, major inference, scope, section function, key primary-language terminology, translation correspondence, or framework structure, do not guess. Use the Clarification Register first.

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

> You are taking over a research repository governed by the Human–AI Research Collaboration Protocol (HARC). Do not rely on prior chat, account memory, or your own inference to reconstruct project state. First read `START_HERE.zh-CN.md` and `HARC_MANIFEST.yaml`, then follow the required read order. Chinese is canonical and English is the synchronized mirror. Before making any substantive change, output a HARC Onboarding Report covering human commitments, Form state, Blocking/Non-blocking Clarifications, Working/Approved Framework state, Artifact status, synchronization defects, and the permitted next step for the current request. If uncertainty could materially affect core claims, key concepts, terminology/translation, scope, inference, or argument structure, do not guess; register it in the Clarification Register and ask for human resolution. Every explicit human decision must first enter the Decision Log and appropriate Core before propagating to the Argument Map and derived artifact. Never treat a Working Framework as human-approved without explicit Framework Approval.
