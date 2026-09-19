# AHICP Onboarding Report Template

> **Language:** Chinese canonical: `ONBOARDING_REPORT_TEMPLATE.zh-CN.md`; this English file is the synchronized mirror.

Before substantive work, a new AI Agent should report the state reconstructed from the repository using this template.

## A. Protocol state

- AHICP version:
- adopted commit/tag:
- canonical language:
- bootstrap / AGENTS / manifest status:
- protocol synchronization defects:

## B. Human-confirmed current state

### B1. Research purpose
- 

### B2. Main human commitments
- 

### B3. Form / presentation state
- 

### B4. Recent important human decisions
- 

## C. Working Memory state

### C1. Current Focus
- CURRENT_STAGE:
- CURRENT_OBJECTIVE:
- PRIMARY_BLOCKER:
- IMMEDIATE_NEXT_ACTION:

### C2. Task Plan
- ACTIVE_TASKS:
- NEXT_ACTIONS:
- TODO / BACKLOG:
- BLOCKERS:
- PENDING_HUMAN_DECISIONS / Clarifications:
- SYNC_DEFECTS:

### C3. Work Log
- skipped by default: `YES`
- read for historical review/audit in this onboarding: `YES / NO`
- if read, reason:

> Work Log history need not be restated in an ordinary Onboarding Report.

## D. Framework state

- Working Framework:
- latest Approved Framework:
- Framework Approval:
- blocked by Clarification Gate:
- known framework synchronization defects:

## E. Artifact state

- current primary Artifact:
- Artifact status:
- Final Artifact Approval:
- synchronization with Framework:

## F. Evidence / conflict state

- task-relevant evidence:
- known evidence conflict:
- time-sensitive sources requiring re-verification:

## G. Bilingual state

- Chinese canonical:
- English mirror:
- current parity:
- known translation/terminology clarifications:

## H. Permitted next action

### Safe to perform
- 

### Currently blocked
- 

### AHICP propagation path for this request
`...`

## I. Onboarding conclusion

- `PASS` — sufficient repository state reconstructed; permitted substantive work may begin;
- `FAIL` — onboarding/persistence defect; repair first;
- `PARTIAL` — limited work may proceed, but some work is blocked by clarification or missing state.

**Conclusion:**

## J. Repository Context Resolver

Following `AHICP_CONTEXT_INTERFACE.yaml` and `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`, the Agent must confirm:

`AHICP REPOSITORY CONTEXT — ACTIVE`

including at least:

- source of truth = GitHub;
- manifest / context-interface paths;
- canonical language;
- `repository-backed / selective retrieval / no authoritative session copy`;
- `read latest before high-impact action`;
- `read latest before write`;
- `invalidate touched cache after write`;
- current CONTENT / FORM / PROTOCOL route;
- authoritative refs as paths only, without duplicating dynamic state.

**Repository context active:** `YES / NO`

If `NO`, Onboarding must not be marked `PASS`.

> Blocking Clarifications, Framework, Artifact, and other summaries in this report exist only so the human can verify reconstruction. Later work must retrieve latest canonical GitHub state on demand rather than treating this report as authority.
