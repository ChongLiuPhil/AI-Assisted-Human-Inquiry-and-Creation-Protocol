# Zero-Context Onboarding Self-Test

**Date:** 2026-09-18  
**Status:** `PASS WITH EXPECTED BLOCKING CLARIFICATIONS`  
**Role:** AI-maintained onboarding/conformance audit, not a new normative truth source.  
**Language:** Chinese canonical: `ONBOARDING_SELF_TEST.zh-CN.md`; this English file is the synchronized mirror.

## 1. Method

Simulate a new AI Agent with no old chat or account memory, reconstructing current project state only from:

1. `HARC_MANIFEST.yaml`
2. `START_HERE.zh-CN.md`
3. `BOOTSTRAP_PROMPT.zh-CN.md`
4. `AGENTS.zh-CN.md`
5. Protocol / Decision / Clarification / Article state files referenced by the manifest.

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
  - `HARC_MANIFEST.yaml`
  - `AGENTS.zh-CN.md`
  - `protocol/ONBOARDING_HANDSHAKE.zh-CN.md`
  - `ONBOARDING_REPORT_TEMPLATE.zh-CN.md`
- current protocol commitments: P1–P20
- recent human protocol decisions: HARC-D015 through HARC-D018
- D018 was subsequently explicitly confirmed by the human founder and ordered for formal implementation.

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
- high-impact uncertainty enters the Layer 1.5 Critical Clarification Register;
- a replacement Agent must complete zero-context bootstrap + Onboarding Handshake before substantive work.

### B3. Methodology-article Form state

- artifact type: `ACADEMIC_PAPER / METHODOLOGY ARTICLE`
- Chinese: canonical
- English: synchronized mirror
- detailed typography, layout, citation style, target venue: `UNRESOLVED`
- current Markdown / author–year presentation: working defaults, not permanent author preferences.

## C. Critical Clarification state

### C1. Blocking

- `CLR-001` — central responsibility concept;
- `CLR-002` — strength of the Framework Responsibility Thesis;
- `CLR-005` — whether to retain/replace `responsibility concentration`.

These block `MA-FW-001`.

Also:

- `CLR-009` is `BLOCKING` for formal open licensing/release but does not block current methodology-framework discussion.

### C2. Non-blocking

- `CLR-003` — `semantic version control`;
- `CLR-004` — `generation–verification asymmetry`;
- `CLR-006` — theoretical status of extended/distributed cognition;
- `CLR-007` — empirical-validation plan;
- `CLR-008` — disciplinary/venue positioning.

## D. Framework state

- Working Framework: `WORKING-FRAMEWORK — REVIEW READY / CLARIFICATION GATE OPEN`
- latest Approved Framework: **none**
- next identifier: `MA-FW-001`
- Framework Approval: `NOT COMPLETED`
- Clarification Gate: `OPEN`
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
- present Clarification Register questions to the human;
- continue evidence/non-substantive maintenance not dependent on Blocking Clarifications;
- prepare candidate analysis without treating any candidate as accepted.

### Blocked

- create `MA-FW-001`;
- claim the methodology framework has human approval;
- lock the philosophical framing through large-scale rewriting based on unresolved `CLR-001 / 002 / 005`;
- Final Artifact Approval;
- describe the public repository as legally open-source/open-content before the license is decided.

## I. Onboarding conclusion

**`PASS`**

Because a new Agent can reconstruct from repository state:

- the human/AI authority boundary;
- Blocking Clarifications;
- the absence of an Approved Framework;
- the `DERIVED-PROVISIONAL` artifact state;
- Chinese-canonical / English-mirror governance;
- what work is currently gated.

Read-order numbering and standalone prompt/report discoverability defects found during implementation were repaired before this test.

---

# 3. Conformance conclusion

The current repository supports a working zero-context onboarding path:

`Repository access -> START_HERE / Manifest -> Agent Contract -> State Reconstruction -> Onboarding Report -> Gated Work`

This test shows that **the current repository can support one successful self-hosted takeover**. It does not prove every external AI platform will automatically discover the entry files.

For cross-platform use, the recommended explicit human startup instruction remains:

> **“Read BOOTSTRAP_PROMPT.zh-CN.md in this repository and execute it strictly.”**

Future work should repeat the test across different Agents/platforms as a cross-agent handoff benchmark.
