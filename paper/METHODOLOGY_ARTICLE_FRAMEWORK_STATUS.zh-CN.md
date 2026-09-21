# 方法论文章 — Framework Status

> 本中文文件是规范性基准；英文 `METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.md` 是同步镜像。

## 当前 Framework

当前工作入口：

`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`

状态：

`CURRENT-FRAMEWORK — ALIGNED WITH APPROVED MA-FW-001`

人类整体 Framework Approval：**已完成。**

授权与批准链：
- HARC-D023 / D024 / D025：责任、Framework 与 approval 相关基础决定；
- AHICP-D030：统一论文、project-memory-centered 结构重写与 proposed evaluation 方向；
- AHICP-D031：完成 scholarly review，并批准 `MA-FW-001`。

## 最新经人类批准的 Framework 快照

`MA-FW-001`

中文 canonical：

`paper/frameworks/MA-FW-001.zh-CN.md`

英文 synchronized mirror：

`paper/frameworks/MA-FW-001.md`

批准日期：2026-09-21

状态：

`APPROVED-FRAMEWORK — MA-FW-001`

`MA-FW-001` 是固定批准 baseline。后续如果核心 thesis、论证结构、scope、approval semantics 或主要 contribution boundary 发生实质修改，应创建新的 snapshot ID，例如 `MA-FW-002`，而不是静默改写 `MA-FW-001`。

## Scholarly review 结论

Framework scholarly review：

`PASS WITH BOUNDED REWORDING`

主要边界：

1. AHICP 不首创 organizational memory / project memory / design rationale / decision provenance / Agent long-term memory；
2. novelty 只表述为 governed, model-substitutable Project Memory Architecture 的 **candidate architectural synthesis**；
3. T2 / T3 / T7 / T8 / T13 是设计原则或架构规范，不是已验证效果定律；
4. T9 只作为 AHICP normative governance；
5. T10 正式采用 **Framework Approval as a Structured Human-Review Gate and Responsibility Anchor**；
6. T12 仍是 proposed empirical research agenda；
7. Final Artifact Approval 保持独立。

当前 review memo：

`paper/METHODOLOGY_ARTICLE_FRAMEWORK_REVIEW_MEMO.zh-CN.md`

## 当前派生文章

中文 canonical：

`paper/METHODOLOGY_ARTICLE.zh-CN.md`

英文 synchronized mirror：

`paper/METHODOLOGY_ARTICLE.en.md`

状态：

`DERIVED-FROM-MA-FW-001 — FINAL ARTIFACT APPROVAL PENDING`

当前正文已经：
- 完成 project-memory-centered 13 节结构；
- 与 `MA-FW-001` 的 T1–T13 对齐；
- 纳入 prior project-memory / Agent-memory / decision-provenance 等 related work；
- 保持 AHICP novelty 的 evidence-constrained 边界；
- 保持 proposed evaluation 与 empirical result 分离；
- 保持中英文同步。

Framework Approval **不等于** Final Artifact Approval。当前文章仍需 artifact-level 审阅、target-venue 核验、引用/格式收束与最终公开版本确认。

## 规范上游来源

- `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`
- `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`
- `core/PROTOCOL_CORE.zh-CN.md`
- `core/DECISION_LOG.zh-CN.md`
- `paper/frameworks/MA-FW-001.zh-CN.md`
- `docs/working-memory/current-focus.zh-CN.md`
- `docs/working-memory/task-plan.zh-CN.md`
- `evidence/METHODOLOGY_SOURCES.zh-CN.md`
- `paper/methodology-references.bib`

## 仍未完成的研究 / 发布状态

- `semantic version control`：解释性 / provisional label；
- `generation–verification asymmetry`：解释性 / heuristic label；
- extended / distributed cognition 的最终理论定位；
- specific benchmark implementation / samples / statistical design；
- 任何 AHICP effectiveness claim；
- target venue：`SELECTED — Ethics and Information Technology / AHICP-D032`；
- venue-specific form / double-blind / AI-use / authorship requirements：`ADOPTED — AHICP-D033`；
- blinded Markdown submission derivative：`PREPARED / PR #29 MERGED / CI PASS`；
- citation / publication-status audit：`COMPLETED — LIVE POLICY RECHECK PENDING`；
- Word/docx build pipeline：`READY — CI BUILD CANDIDATE / VISUAL QA PENDING`；
- search-based anonymization risk from `AHICP` name：`OPEN`；
- license；
- Final Artifact Approval。

## 当前同步状态

- Human decision -> Decision Log：`SYNC — AHICP-D033 RECORDED`
- EIT preparation PR #29：`MERGED — a789bbd3342b29ebb07caa9c0cd22da3315e7746`
- D030 direction -> Content Core：`SYNC — C17–C22`
- Scholarly review -> T9 / T10 / contribution boundaries：`SYNC`
- Approved Framework snapshot：`MA-FW-001 CREATED`
- Current Argument Map -> MA-FW-001：`ALIGNED`
- MA-FW-001 -> Chinese article：`DERIVED / STRUCTURALLY SYNCED`
- Chinese article -> English mirror：`SYNCED`
- External evidence -> related-work claims：`UPDATED 2026-09-21`
- Proposed evaluation -> empirical results：`NO RESULTS CLAIMED`
- Framework Approval：`COMPLETED`
- Final Artifact Approval：`NOT COMPLETED`

## 下一治理门

下一步不再是 Framework Approval。

下一治理门是：

`FINAL ARTIFACT REVIEW / ETHICS AND INFORMATION TECHNOLOGY SUBMISSION PACKAGE PREPARATION`

在 Final Artifact Approval 之前，文章可以继续做：
- 语言与逻辑精修；
- 引用核验；
- venue formatting；
- 图表/架构图；
- limitations / methods clarity；
- empirical study design。

但任何对 `MA-FW-001` 核心 thesis 或结构的实质修改，都应先进入新的 Working Framework，并在必要时创建 `MA-FW-002`。