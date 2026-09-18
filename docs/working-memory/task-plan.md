# HARC Working Memory — Task Plan

> **Language:** Chinese canonical: `task-plan.zh-CN.md`; this English file is the synchronized mirror.

**Status:** `ACTIVE TASK PLAN`  
**Principle:** maintain only current plans here. Completed items leave the active list and are summarized into Work Log; stable normative results are separately promoted.

## 1. ACTIVE TASKS

- `WM-T015` — human overall review of the current methodology-article Working Framework and APPROVE / REVISE / REJECT decision for `MA-FW-001`: `WAITING-HUMAN`
- `WM-T013` — CLR-009 licensing decision before formal release: `WAITING-HUMAN`
- `WM-T014` — CLR-010 target venue and venue-specific form constraints: `WAITING-HUMAN`

## 2. NEXT ACTIONS

1. Human reviews `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md` as a whole, especially the current thesis set, dependency structure, section functions, and the HARC-D023 / HARC-D024 revisions to T3 / T4; the title itself is human-approved through HARC-D024, but this does not constitute overall Framework Approval;
2. human explicitly decides `APPROVE / REVISE / REJECT`;
3. only after explicit `APPROVE`, the Agent creates the `MA-FW-001` Approved Framework Snapshot and updates Framework Status;
4. after Framework Approval, perform the major structural synchronization/rewrite of the current draft while retaining a separate Final Artifact Approval gate;
5. resolve `CLR-009` before formal release;
6. resolve `CLR-010` before freezing final submission/publication form.

## 3. BLOCKERS / GATES

### Framework Approval

`CLR-001 / CLR-002 / CLR-005` have been resolved and promoted through HARC-D023.

There is currently **no blocking Clarification** preventing overall Framework Approval review.

However, `MA-FW-001` has not been created because explicit overall human approval of the complete Working Framework is still missing. Current gate:

`WAITING-HUMAN: overall Framework Approval decision`

### Formal release

- `CLR-009` — license unresolved.

### Final submission / publication form

- `CLR-010` — target venue and venue-specific citation, length, layout, AI-disclosure, and related constraints are unresolved.

## 4. PENDING HUMAN DECISIONS / CLARIFICATIONS

### Framework Approval overall decision

**Status:** `WAITING-HUMAN`  
**Type:** human approval decision, not a new Clarification.

The current Working Framework requires an overall:

- `APPROVE`
- `REVISE`
- `REJECT`

Acceptance of local wording does not automatically constitute overall approval.

### CLR-003 — `semantic version control`

**Status:** `WAITING-HUMAN`  
**Severity:** `NON-BLOCKING`

**AI-PROPOSED:** use as a clearly qualified HARC working term/coinage, not an established standard.

### CLR-004 — `generation–verification asymmetry`

**Status:** `WAITING-HUMAN`  
**Severity:** `NON-BLOCKING`

**AI-PROPOSED:** heuristic label only, not an established empirical law.

### CLR-006 — Relation to extended / distributed cognition

**Status:** `WAITING-HUMAN`  
**Severity:** `NON-BLOCKING`

Candidates: central foundation / secondary comparison / minimal background.  
**AI-PROPOSED:** secondary conceptual comparison.

**HARC-D023 constraint:** whatever comparison strength is chosen, it must not be written as presupposing that AI itself is a cognitive subject.

### CLR-007 — Status of empirical validation plans

**Status:** `WAITING-HUMAN`  
**Severity:** `NON-BLOCKING`

Candidates: core contribution / Future Research / omit.  
**AI-PROPOSED:** Future Research Agenda.

### CLR-008 — Primary disciplinary positioning

**Status:** `WAITING-HUMAN`  
**Severity:** `NON-BLOCKING`

Candidates: philosophy of technology / epistemology; research methodology; scholarly communication / research integrity; interdisciplinary AI governance.

**AI-PROPOSED:** interdisciplinary research methodology with philosophy of technology / epistemology as the theoretical core.

### CLR-009 — HARC open license

**Status:** `WAITING-HUMAN`  
**Severity:** formal release = `BLOCKING`; methodology framework = `NON-BLOCKING`

Candidates: documentation CC BY 4.0 + code MIT / Apache-2.0 / MIT / other.

Related: `LICENSE-DECISION.zh-CN.md`

### CLR-010 — Target venue and venue-specific form constraints

**Status:** `WAITING-HUMAN`  
**Severity:** Framework Approval = `NON-BLOCKING`; Final submission/publication form = `BLOCKING`

Question: what publication venue will the methodology article target, and what concrete form constraints follow from that venue?

Pending items include:

- target journal / conference / preprint / other venue;
- citation and bibliography style;
- word/length limits;
- typography, layout, and page constraints where applicable;
- venue-specific AI disclosure / authorship / research-integrity requirements;
- whether the venue accepts only one language and what output is required from the internally bilingual project.

Distinction from `CLR-008`:

- `CLR-008` concerns **disciplinary / intellectual positioning**;
- `CLR-010` concerns **specific venue / external form constraints**.

**AI-PROPOSED:** select the concrete venue after the Working Framework stabilizes; until then, do not promote current citation/layout defaults into human Form commitments.

**Promotion target:** Article Form Core -> external constraints / final rendering / submission checklist.

## 5. RESOLVED / PROMOTED POINTERS

- `CLR-001` — `RESOLVED / PROMOTED` via `HARC-D023` + `HARC-D024`: do not use “AI cognitive labor / cognitive tasks” as central language; do not treat “human responsibility” as a self-sufficient concept. The core claim is that in human–AI collaborative research, inquiry, and especially public dissemination of knowledge, humans remain the bearers of responsibility.
- `CLR-002` — `RESOLVED / PROMOTED` via `HARC-D023`: adopt the human's third Framework Responsibility Thesis; the Layer 2 Framework is the primary structural carrier of core intellectual responsibility, and the human must understand, review, and confirm all substantive content represented in it.
- `CLR-005` — `RESOLVED / PROMOTED` via `HARC-D023`: `responsibility concentration` is not retained as the current central term.

- `HARC-D024` — `RESOLVED / PROMOTED`: the current Chinese title is human-approved; English is the synchronized translation mirror; title approval is not overall Framework Approval.

## 6. BACKLOG

- automated onboarding / conformance checks;
- study context cost and stale-state behavior under repository-backed context;
- study Working Memory update granularity, compression, and handoff efficiency;
- cross-Agent / cross-platform takeover tests.

## 7. SYNC DEFECTS

`NONE RECORDED`

## 8. COMPLETION RULE

When a task completes:

1. remove/exit it from this active list;
2. add a high-level completion summary to Work Log;
3. perform Promotion if it created a durable normative result;
4. update Current Focus when appropriate;
5. do not accumulate long completed-history here.
