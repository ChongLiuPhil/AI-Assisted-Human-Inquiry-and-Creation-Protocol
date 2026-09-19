# AHICP Working Memory — Task Plan

> **Chinese canonical: `task-plan.zh-CN.md`; this file is the synchronized English mirror.**

**Status:** `ACTIVE TASK PLAN`

## 1. ACTIVE TASKS

- `WM-T016` — AHICP v0.3 repository-wide semantic migration: `IN PROGRESS`
- `WM-T017` — AHICP project templates/control-plane migration: `COMPLETED`
- `WM-T018` — v0.3 structural validation completed; semantic bilingual parity + post-migration audit: `IN PROGRESS`
- `WM-T015` — methodology article overall Framework Approval: `WAITING-HUMAN / PARALLEL`
- `WM-T013` — license decision: `WAITING-HUMAN`
- `WM-T014` — target publication venue / form constraints: `WAITING-HUMAN`

## 2. NEXT ACTIONS

1. precisely handle the former project name in the methodology article and evidence layer, distinguishing historical HARC references from current AHICP references;
2. perform semantic bilingual parity on key normative files, not merely file-pair checks;
3. check remaining live navigation / repository URLs / identifiers for migration;
4. perform an independent post-migration repair audit;
5. merge only after these checks pass.

Structural validation completed:
- 33 manifest path candidates checked, 0 missing;
- 62 Chinese `*.zh-CN.md` files checked, 0 missing English mirrors;
- zero-context control chain points entirely to AHICP control files;
- research-project template migrated to the AHICP control plane while remaining a research specialization.

## 3. MIGRATION INVARIANTS

- Name: **AI-Assisted Human Inquiry and Creation Protocol**.
- Subtitle: **A protocol for human-led inquiry, research, reasoning, writing, and creation with AI assistance.**
- Humans retain purpose, direction, substantive judgment, approval, and ultimate responsibility.
- AI is assistive; extensive execution does not make it a symmetric cognitive subject.
- Historical facts are not rewritten merely because the project was renamed.
- Research-specific content remains research-specific where appropriate.
- AHICP does not duplicate PPF publishing-lifecycle rules.
- Chinese-canonical / English-mirror governance remains in force.

## 4. PARALLEL METHODOLOGY ARTICLE GATES

Unchanged:
- overall Framework Approval: `WAITING-HUMAN`;
- `CLR-009` license: blocking before formal release;
- `CLR-010` target venue / publication form: blocking before final publication.

## 5. COMPLETION RULE

Migration completion requires:

`semantic migration complete + bilingual parity + control-path consistency + zero-context onboarding pass + post-migration audit pass`

A repository rename or README rename alone is not completion.
