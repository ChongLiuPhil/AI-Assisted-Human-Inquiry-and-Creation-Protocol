# AHICP Working Memory — Task Plan
## 动态任务计划

> **中文 canonical；英文 `task-plan.md` 为同步 mirror。**

**状态：** `ACTIVE TASK PLAN`

## 1. ACTIVE TASKS

- `WM-T013` — license 决定：`WAITING-HUMAN`
- `WM-T014` — target publication venue：`COMPLETED — Ethics and Information Technology / AHICP-D032`
- `WM-T026` — methodology article Final Artifact review / venue preparation：`IN PROGRESS`
- `WM-T029` — EIT blinded submission derivative + disclosure + checklist + CI：`COMPLETED / PR #29 MERGED — a789bbd3`
- `WM-T030` — EIT citation / publication-status audit：`COMPLETED / LIVE POLICY RECHECK PENDING`
- `WM-T031` — EIT DOCX build + visual QA：`IN PROGRESS / TRACEABLE + MASKED BUILDS GENERATED / STRUCTURAL PASS / VISUAL QA PENDING`
- `WM-T033` — EIT masked reviewer derivative + blinding review：`IN PROGRESS / MASKED DERIVATIVE PREPARED / HUMAN-EDITORIAL CONFIRMATION PENDING`
- `WM-T034` — citation ↔ reference-list 双向一致性 validator：`COMPLETED / 18-of-18 / EIT CI PASS`
- `WM-T032` — PR #30 post-merge verification + state write-back：`COMPLETED`
- `WM-T027` — Framework Approval -> scoped PR auto-merge semantics：`COMPLETED / AHICP-D032`

## 2. COMPLETED METHODOLOGY ARTICLE TASKS

- `WM-T015` — methodology Working Framework 整体审阅：`COMPLETED — MA-FW-001 APPROVED`
- `WM-T022` — AHICP-D030 project-memory structural rewrite：`COMPLETED`
- `WM-T023` — methodology paper validation + PR #26：`COMPLETED / MERGED — af3e7927`
- `WM-T024` — scholarly novelty / prior-art positioning audit：`COMPLETED / EVIDENCE-CONSTRAINED`
- `WM-T025` — T1–T13 scholarly review + MA-FW-001 Framework Approval：`COMPLETED / AHICP-D031`
- `WM-T028` — PR #26 post-merge verification + durable-state write-back：`COMPLETED`

完成范围：
- Decision Log：AHICP-D030 / D031 / D032 / D033；
- Content Core：C17–C22；
- Working Argument Map：与 `MA-FW-001` 对齐；
- Approved Framework：`paper/frameworks/MA-FW-001.zh-CN.md` + English mirror；
- Review Memo：完成 scholarly review；
- Chinese / English article：derived from `MA-FW-001`；
- Evidence / BibTeX：Agent memory + prior Project Memory + decision provenance；
- Evaluation：proposed / no-results；
- bilingual synchronization：完成。

## 3. COMPLETED PROTOCOL / MIGRATION TASKS

- `WM-T016` — AHICP v0.3 repository-wide semantic migration：`COMPLETED`
- `WM-T017` — project templates/control-plane migration：`COMPLETED`
- `WM-T018` — structural validation + bilingual parity：`COMPLETED / PASS`
- `WM-T019` — AHICP-D027 external systems / authorization / handoff：`COMPLETED`
- `WM-T020` — AHICP-D028 / D029 scoped authorization consolidation：`COMPLETED`
- `WM-T021` — PR #3 governance consistency repair：`COMPLETED / CI-GATED`

## 4. NEXT ACTIONS

1. 人类/编辑部确认 masked reviewer route 并处理残余 deanonymization risk；
4. 决定 license；
5. 完成 Final Artifact-level academic edit；
6. 对 CI 生成的 Word/docx build candidate 做逐页视觉 QA；
7. 正式投稿前复核动态 policy pages；
8. 完成 Final Artifact Approval；
9. submission / publication / release 依独立授权执行。

## 5. ARTICLE INVARIANTS

后续工作必须保持：
- one unified methodology article；
- `MA-FW-001` 是当前批准 Framework baseline；
- AHICP 不声称首创 project memory；
- novelty 仅为 governed, model-substitutable Project Memory Architecture 的 candidate synthesis；
- Working Memory != psychological working memory / hidden state / chain-of-thought；
- Human Decision Persistence 是治理机制；
- Agent / Model substitution = design goal + proposed stress test；
- T9 = AHICP normative governance；
- T10 = structured human-review gate / responsibility anchor；
- Agent memory != Project Memory；
- repository authoritative state outranks chat/model memory for AHICP project governance；
- proposed evaluation != completed empirical result；
- Framework Approval != Final Artifact Approval；
- Chinese canonical / English synchronized mirror；
- `AHICP-D032 bounded Framework merge authorization != Final Artifact Approval != submission/publication/release authorization`.