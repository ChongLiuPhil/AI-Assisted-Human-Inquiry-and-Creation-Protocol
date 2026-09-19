# AHICP Working Memory — Task Plan

> **Chinese canonical: `task-plan.zh-CN.md`; this file is the synchronized English mirror.**

**Status:** `ACTIVE TASK PLAN`

## 1. ACTIVE TASKS

- `WM-T015` — methodology article overall Framework Approval: `WAITING-HUMAN`
- `WM-T013` — license decision: `WAITING-HUMAN`
- `WM-T014` — target publication venue / form constraints: `WAITING-HUMAN`

## 2. COMPLETED MIGRATION TASKS

- `WM-T016` — AHICP v0.3 repository-wide semantic migration: `COMPLETED`
- `WM-T017` — AHICP project templates/control-plane migration: `COMPLETED`
- `WM-T018` — structural validation + semantic bilingual parity + post-migration audit: `COMPLETED / PASS`

Validation summary:
- manifest path candidates: 33 / missing 0;
- Chinese Markdown pairs: 62 / missing English mirror 0;
- Protocol Core: 24 / 24 sections;
- Specification: 25 / 25 sections;
- AGENTS: 17 / 17 sections;
- Working Memory: 11 / 11 sections;
- Repository Context Interface: 16 / 16 sections;
- old live HARC control paths / full name / v0.2 identifiers: 0 across key normative files;
- final post-migration audit: PASS.

## 3. COMPLETED PROTOCOL GOVERNANCE TASKS

- `WM-T019` — AHICP-D027 external systems / tool discovery / authorization / human handoff governance: `COMPLETED`
- `WM-T020` — AHICP-D028 / D029 scoped authorization, initial authorization-mode human choice, and PR #3 normative consolidation: `COMPLETED`
- `WM-T021` — PR #3 post-merge review: restore the durable authorization record, §23.3 permission grants, Working Memory synchronization, and section-local contract validation: `COMPLETED / CI-GATED`

These tasks do not change the PPF publishing lifecycle and do not constitute a silent downstream adoption bump.

## 4. NEXT ACTIONS

1. await the human's overall `APPROVE / REVISE / REJECT` decision on the methodology Working Framework;
2. decide the license before formal release;
3. decide target venue / external form constraints before final submission/publication.

## 5. MIGRATION / GOVERNANCE INVARIANTS

Future AHICP v0.3 development must preserve:

- **AI-Assisted Human Inquiry and Creation Protocol**
- *A protocol for human-led inquiry, research, reasoning, writing, and creation with AI assistance.*
- humans retain purpose, direction, substantive judgment, approval, and ultimate responsibility;
- AI remains assistive;
- `AI proposal != human authorization`;
- `proposal != authorization != execution != verification != durable write-back`;
- reusable authorization policies require human selection and durable recording of scope / authorization provenance / escalation conditions;
- general pre-authorization cannot override human-reserved / non-delegable boundaries;
- repository state outranks chat memory;
- historical `HARC-D001`–`HARC-D025` remain historical identifiers;
- new protocol decisions use the AHICP prefix;
- AHICP and PPF retain their boundary;
- Chinese canonical / English synchronized mirror.