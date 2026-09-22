# AHICP Working Memory — Task Plan
## 动态任务计划

> **中文 canonical；英文 `task-plan.md` 为同步 mirror。**

**状态：** `ACTIVE TASK PLAN`

## 1. ACTIVE TASKS

- `WM-T013` — publication route / license 决定：`DEFERRED-HUMAN — POST-ACCEPTANCE / NOT A PRE-SUBMISSION BLOCKER`
- `WM-T014` — target publication venue：`COMPLETED — Ethics and Information Technology / AHICP-D032`
- `WM-T026` — methodology article Final Artifact review / venue preparation：`COMPLETED — AHICP-D034 FINAL ARTIFACT APPROVED`
- `WM-T029` — EIT blinded submission derivative + disclosure + checklist + CI：`COMPLETED / PR #29 MERGED — a789bbd3`
- `WM-T030` — EIT citation / publication-status audit：`COMPLETED / 2026-09-22 LIVE POLICY RECHECK PASS / FINAL PRE-SUBMISSION INTERFACE RECHECK PENDING`
- `WM-T031` — EIT DOCX build + visual QA：`COMPLETED / TRACEABLE + MASKED 20-PAGE QA PASS / AUTO PAGE NUMBERING + NON-SPLIT TABLE ROWS + ANONYMOUS METADATA GATES`
- `WM-T033` — EIT masked reviewer derivative + blinding review：`COMPLETED / HUMAN-CONFIRMED MASKED REVIEWER ROUTE / PUBLIC REPOSITORY NOT PROACTIVELY SUPPLIED`
- `WM-T034` — citation ↔ reference-list 一致性 validator：`COMPLETED / 18-of-18 + UNMAPPED-YEAR GUARD / EIT CI PASS`
- `WM-T032` — PR #30 post-merge verification + state write-back：`COMPLETED`
- `WM-T027` — Framework Approval -> scoped PR auto-merge semantics：`COMPLETED / AHICP-D032`

### Submission metadata progress — 2026-09-22

**状态：** `PARTIALLY PROVIDED — REMAINING FIELDS WAITING-HUMAN — DO NOT INFER`

人类已提供：刘崇 / Chong Liu、独立研究者、ORCID `0009-0009-8116-1255`、无基金、无利益冲突；后续同日确认由本人担任通讯作者、城市 / 国家为温州 / 中国、无致谢。人类随后回复“同意建议，请继续”，选定邮箱名称 `chong.liu.phil@outlook.com`。来源与对应英文措辞已保存在 `paper/submission/ethics-information-technology/TITLE_PAGE_METADATA_TEMPLATE.zh-CN.md` 和英文 mirror。

邮箱名称已选定，但地址持有权与正常收发仍为 `HUMAN-SELECTED — OWNERSHIP / SEND-RECEIVE VERIFICATION PENDING`；本轮未取得账户访问授权，未完成账户核验、未创建邮箱或发送测试邮件。Author Contributions 及实际界面要求的其他未提供事实（如必填州或省）仍待人类补全。不能从姓名、ORCID、连接账户或命名选择猜填。元数据工作表不是 reviewer-facing 文件，live interface 尚未完成；本次事实补充不构成 submission / publication / release authorization。“无致谢”不取消既有 substantive AI-use disclosure。

## 2. COMPLETED METHODOLOGY ARTICLE TASKS

- `WM-T015` — methodology Working Framework 整体审阅：`COMPLETED — MA-FW-001 APPROVED`
- `WM-T022` — methodology article project-memory structural rewrite：`COMPLETED`
- `WM-T023` — methodology paper validation + PR #26：`COMPLETED / MERGED — af3e7927`
- `WM-T024` — scholarly novelty / prior-art positioning audit：`COMPLETED / EVIDENCE-CONSTRAINED`
- `WM-T025` — T1–T13 scholarly review + MA-FW-001 Framework Approval：`COMPLETED / AHICP-D031`
- `WM-T028` — PR #26 post-merge verification + durable-state write-back：`COMPLETED`

完成范围：
- Decision Log：AHICP-D030 / D031 / D032 / D033 / D034；
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

1. 确认 / 核验作者持有已选邮箱且可正常收发，并由人类补全 Author Contributions 与实际界面要求的其他未提供事实（如必填州或省）；已确认的邮箱名称、通讯作者身份、温州 / 中国、无致谢及此前五项事实不重复请求，不从命名同意推断账户可用性或作者贡献；
2. 正式投稿前再次检查 EIT live submission interface；动态 EIT / SNAPP / ICMJE / Nature policy pages 已于 2026-09-22 复核，实际提交当刻仍需 final recheck；
3. 获得独立、明确的 submission authorization 后才可执行正式投稿；
4. submission 后续 publication / release 继续遵守独立授权；如文章被接受，再由人类选择 subscription 或 open access，并在 OA 情形选择适用 licence。

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
