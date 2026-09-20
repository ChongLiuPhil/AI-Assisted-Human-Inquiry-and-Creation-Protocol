# 方法论文章 — Framework Status

> 本中文文件是规范性基准；英文 `METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.md` 是同步镜像。

## 当前 Working Framework

来源：`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`

状态：

`WORKING-FRAMEWORK — REVISED UNDER AHICP-D030 / HUMAN REVIEW PENDING`

人类整体 Framework Approval：**尚未完成。**

AHICP-D030 已明确授权对方法论文章进行结构性重写，并确认以下方向必须成为同一篇论文的核心内容：

- Project Memory Architecture；
- Working Memory as a continuity layer；
- Agent / Model substitution；
- Human Decision Persistence；
- multi-role project memory；
- memory curation / stale / conflict / selective retrieval；
- proposed empirical evaluation framework。

这项人类决定属于 **REVISE / STRUCTURAL REWRITE AUTHORIZED**，不是对重写后完整 framework 的整体 `APPROVE`。

## 当前 framework 的结构状态

当前 Working Framework 已从旧的责任/作者性主轴重新组织为 project-memory-centered 13 节结构，并与 AHICP-D030 对齐。

当前核心命题包括：

1. 长期人机项目的持久记忆应属于项目，而不是属于某一个模型；
2. Agent/conversational memory 与 Project memory 必须区分；
3. Working Memory 是跨 session / 跨 Agent 的 continuity layer；
4. Human Decision Persistence 是 first-class project memory；
5. Agent / Model Substitution 是架构压力测试；
6. Project Memory 必须具有 inspectability、versionability、provenance、curation 与 privacy/publication boundary；
7. Framework Approval / Final Artifact Approval 把项目记忆与人类责任连接起来；
8. proposed evaluation 必须保持“研究议程”状态，不得写成已完成实验。

## 最新经人类批准的 framework 快照

**尚无。**

目前没有方法论文章 framework 通过整体 Framework Approval Gate。

下一 framework 标识符仍为：

`MA-FW-001`

只有在人类明确审阅当前完整 Working Framework 并作整体 `APPROVE` 决定后，才能创建 `MA-FW-001`。

不得因为：
- AHICP-D030 已授权重写；
- 正文已完成结构同步；
- evidence / references 已补充；
- CI 通过；
- 人类认可其中某些中心命题；

而推断完整 Framework 已经批准。

## 当前派生文章

中文 canonical：

`paper/METHODOLOGY_ARTICLE.zh-CN.md`

英文 synchronized mirror：

`paper/METHODOLOGY_ARTICLE.en.md`

状态：

`DERIVED-PROVISIONAL — STRUCTURALLY REWRITTEN UNDER AHICP-D030`

当前正文已完成与新 Working Framework 的**结构同步**：

- 旧 15 部分结构已替换为 project-memory-centered 13 节结构；
- Project Memory / Working Memory / Decision Persistence / Agent Substitution 已进入摘要、正文主干与结论；
- Agent-memory / provenance 相关工作已进入 related-work / evidence layer；
- proposed evaluation 已进入正文，但明确没有实证结果；
- 中英文正文已同步重写。

“结构同步”不等于 Framework Approval，也不等于 Final Artifact Approval。后续人类审阅仍可要求调整理论结构、术语、文献定位、评价方案或表述。

## 规范上游来源

- `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`
- `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`
- `core/PROTOCOL_CORE.zh-CN.md`
- `core/DECISION_LOG.zh-CN.md`
- `docs/working-memory/current-focus.zh-CN.md`
- `docs/working-memory/task-plan.zh-CN.md`
- `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`
- `evidence/METHODOLOGY_SOURCES.zh-CN.md`
- `paper/methodology-references.bib`

## 当前 Clarification / research-status 边界

### 已经由人类决定的内容

- HARC-D023 / D024：人类作为责任主体、Framework responsibility、题目与责任措辞；
- HARC-D025：framework dependency 与 unresolved-item approval semantics；
- AHICP-D030：统一论文方向、project-memory-centered 核心贡献、评估框架应纳入正文。

### 仍然需要后续审阅或研究的内容

- `semantic version control`：仍是解释性 / provisional label；
- `generation–verification asymmetry`：仍是解释性 / provisional label；
- extended / distributed cognition 的最终理论定位；
- specific benchmark implementation / samples / statistical design；
- 任何 AHICP effectiveness claim；
- target venue / disciplinary positioning；
- venue-specific form / AI / authorship requirements。

## 当前同步状态

- Human decision -> Decision Log：`SYNC — AHICP-D030 RECORDED`
- Decision Log -> Article Content Core：`SYNC — C17–C22 ADDED`
- Content Core -> Working Framework：`SYNC — PROJECT-MEMORY-CENTERED REWRITE`
- Working Framework -> Chinese article：`STRUCTURALLY SYNCED / DERIVED-PROVISIONAL`
- Chinese article -> English mirror：`SYNCED IN CURRENT WORK CYCLE`
- External evidence -> related-work claims：`UPDATED 2026-09-20`
- Proposed evaluation -> empirical results：`NO RESULTS CLAIMED`
- Framework Approval：`NOT COMPLETED`
- Final Artifact Approval：`NOT COMPLETED`

## Framework Approval Gate

当前没有因为旧结构而产生的 blocker。

下一步不是再进行大规模 AI 自主扩写，而是由人类审阅新的：

`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`

以及重写后的：

`paper/METHODOLOGY_ARTICLE.zh-CN.md`

并决定：

- `APPROVE`
- `REVISE`
- `REJECT`

如果后续整体 `APPROVE`，才创建 `MA-FW-001`。在那之前，所有正文继续保持 `DERIVED-PROVISIONAL`。