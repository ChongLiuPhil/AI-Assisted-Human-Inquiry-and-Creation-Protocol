# AHICP Working Memory — Task Plan

> **Chinese canonical: `task-plan.zh-CN.md`; this file is the synchronized English mirror.**

**Status:** `ACTIVE TASK PLAN`

## 1. ACTIVE TASKS

- `WM-T013` — license decision: `WAITING-HUMAN`
- `WM-T014` — target publication venue / form constraints: `WAITING-HUMAN`
- `WM-T026` — methodology article Final Artifact review / venue preparation: `IN PROGRESS`
- `WM-T027` — Framework Approval -> scoped PR auto-merge semantics: `PROPOSED / WAITING-HUMAN CONFIRMATION`

## 2. COMPLETED METHODOLOGY ARTICLE TASKS

- `WM-T015` — overall methodology Working Framework review: `COMPLETED — MA-FW-001 APPROVED`
- `WM-T022` — AHICP-D030 project-memory structural rewrite: `COMPLETED`
- `WM-T023` — methodology paper validation + PR: `COMPLETED / CI-GATED`
- `WM-T024` — scholarly novelty / prior-art positioning audit: `COMPLETED / EVIDENCE-CONSTRAINED`
- `WM-T025` — T1–T13 scholarly review + MA-FW-001 Framework Approval: `COMPLETED / AHICP-D031`

Completed scope:
- Decision Log: AHICP-D030 / D031;
- Content Core: C17–C22;
- Working Argument Map: aligned with `MA-FW-001`;
- Approved Framework: `paper/frameworks/MA-FW-001.zh-CN.md` + English mirror;
- Review Memo: scholarly review completed;
- Chinese / English article: derived from `MA-FW-001`;
- Evidence / BibTeX: Agent memory + prior Project Memory + decision provenance;
- Evaluation: proposed / no-results;
- bilingual synchronization: completed.

## 3. COMPLETED PROTOCOL / MIGRATION TASKS

- `WM-T016` — AHICP v0.3 repository-wide semantic migration: `COMPLETED`
- `WM-T017` — project templates/control-plane migration: `COMPLETED`
- `WM-T018` — structural validation + bilingual parity: `COMPLETED / PASS`
- `WM-T019` — AHICP-D027 external systems / authorization / handoff: `COMPLETED`
- `WM-T020` — AHICP-D028 / D029 scoped authorization consolidation: `COMPLETED`
- `WM-T021` — PR #3 governance consistency repair: `COMPLETED / CI-GATED`

## 4. NEXT ACTIONS

1. decide target publication venue / disciplinary positioning (current AI-researched default: `Ethics and Information Technology`; see `paper/TARGET_VENUE_REVIEW.md`);
2. confirm or revise the proposed `WM-T027` scoped auto-merge rule: when a dedicated PR contains only implementation of an approved Framework and direct synchronization, has no scope expansion, has green latest-head CI, has no unresolved blocking review, and contains no new substantive unapproved diff after approval, Framework Approval also carries bounded authorization to merge that PR;
3. decide the license;
3. perform Final Artifact-level academic editing and citation verification;
4. verify venue-specific AI / authorship / disclosure rules;
5. complete Final Artifact Approval;
6. execute publication / release / merge only under their separate authorization.

## 5. ARTICLE INVARIANTS

Future work must preserve:
- one unified methodology article;
- `MA-FW-001` as the current approved Framework baseline;
- AHICP does not claim to originate project memory;
- novelty remains the candidate synthesis of a governed, model-substitutable Project Memory Architecture;
- Working Memory != psychological working memory / hidden state / chain-of-thought;
- Human Decision Persistence is a governance mechanism;
- Agent / Model substitution = design goal + proposed stress test;
- T9 = AHICP normative governance;
- T10 = structured human-review gate / responsibility anchor;
- Agent memory != Project Memory;
- repository authoritative state outranks chat/model memory for AHICP project governance;
- proposed evaluation != completed empirical result;
- Framework Approval != Final Artifact Approval;
- Chinese canonical / English synchronized mirror;
- `AHICP-D031 Framework Approval != Final Artifact Approval != merge/publication authorization`.