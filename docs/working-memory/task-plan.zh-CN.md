# AHICP Working Memory — Task Plan
## 动态任务计划

> **中文 canonical；英文 `task-plan.md` 为同步 mirror。**

**状态：** `ACTIVE TASK PLAN`

## 1. ACTIVE TASKS

- `WM-T023` — project-memory-centered methodology paper validation + PR：`COMPLETED / CI-GATED`
- `WM-T015` — 重写后的 methodology Working Framework 整体审阅：`WAITING-HUMAN AFTER PR`
- `WM-T013` — license 决定：`WAITING-HUMAN`
- `WM-T014` — target publication venue / form constraints：`WAITING-HUMAN`

## 2. COMPLETED METHODOLOGY ARTICLE TASKS

- `WM-T022` — AHICP-D030 methodology article project-memory structural rewrite：`COMPLETED`
- `WM-T024` — methodology paper scholarly novelty / prior-art positioning audit：`COMPLETED / EVIDENCE-CONSTRAINED`

完成范围：

- Decision Log：记录 AHICP-D030；
- Content Core：新增 C17–C22；
- Working Argument Map：重构为 Project Memory Architecture 主轴；
- Chinese article：完成 13 节结构性重写；
- English article：完成同步镜像重写；
- Evidence layer：新增 Agent-memory / project-oriented memory / provenance 相关来源；
- BibTeX：新增对应参考文献；
- Framework Status：更新为 D030 后状态；
- Evaluation：纳入论文但保持 proposed / no-results 边界；
- bilingual semantic synchronization：本轮完成。

## 3. COMPLETED PROTOCOL / MIGRATION TASKS

- `WM-T016` — AHICP v0.3 repository-wide semantic migration：`COMPLETED`
- `WM-T017` — AHICP project templates/control-plane migration：`COMPLETED`
- `WM-T018` — structural validation + semantic bilingual parity + post-migration audit：`COMPLETED / PASS`
- `WM-T019` — AHICP-D027 external systems / tool discovery / authorization / human handoff governance：`COMPLETED`
- `WM-T020` — AHICP-D028 / D029 scoped authorization consolidation：`COMPLETED`
- `WM-T021` — PR #3 post-merge governance consistency repair：`COMPLETED / CI-GATED`

## 4. NEXT ACTIONS

1. 人类审阅新的 Working Framework 与正文；
2. 对当前完整 framework 作 `APPROVE / REVISE / REJECT`；
3. 如果后续整体 `APPROVE`，才创建 `MA-FW-001`；
6. formal release 前决定 license；
7. final submission/publication 前决定 target venue / form constraints，并重新核验时效性政策。

## 5. ARTICLE INVARIANTS

后续工作必须保持：

- one unified methodology article；
- Project Memory Architecture 是核心理论贡献；
- Working Memory = persistent continuity layer，不是心理学 working memory / hidden state / chain-of-thought；
- Human Decision Persistence 是 first-class project memory；
- Agent / Model substitution 是设计原则与 proposed stress test；
- Agent memory != Project memory；
- repository state outranks chat/model memory；
- evidence / inference / proposal / human-confirmed decision 必须可区分；
- memory curation / stale / conflict / selective retrieval 必须进入论证；
- proposed evaluation != completed empirical result；
- human responsibility / Framework Approval / Final Artifact Approval 边界保持；
- Chinese canonical / English synchronized mirror；
- `AHICP-D030 authorization != overall Framework Approval != Final Artifact Approval`.