# 方法论文章 — Working Argument Map

**状态：** `WORKING-FRAMEWORK — REVIEW READY / CLARIFICATION GATE OPEN`  
**成果类型：** 方法论文章  
**人类批准：** 尚未完成  
**派生草稿状态：** `DERIVED-PROVISIONAL`

> **本中文文件是规范性基准；英文 `METHODOLOGY_ARTICLE_ARGUMENT_MAP.md` 是同步镜像。**

## 规范上游文件

- `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`
- `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`
- `core/PROTOCOL_CORE.zh-CN.md`
- `core/DECISION_LOG.zh-CN.md`
- `docs/clarification-register.zh-CN.md`
- `evidence/METHODOLOGY_SOURCES.zh-CN.md`

## 来源状态图例

- `HUMAN-ORIGINATED` — 实质性承诺由人类发起人明确提出或明确确认。
- `HUMAN-ORIGINATED / AI-FORMULATED` — 实质思想来自人类，但当前措辞或概念压缩由 AI 生成。
- `AI-PROPOSED` — 尚未进入人类批准的思想架构。
- `EVIDENCE-CONSTRAINT` — 外部来源约束一个主张可以怎样负责任地表达；它本身不自动成为人类承诺。

这些标签的目的，是防止成熟的 AI 术语被误认为创始人亲自提出的理论。

---

## 工作标题

**从对话到持久研究状态：AI时代的人机研究协作、认识责任与可审计作者性**  
*From Conversation to Persistent Research State: Human–AI Research Collaboration, Epistemic Responsibility, and Auditable Authorship in the AI Era*

`AI-PROPOSED TITLE` — 文章主题由人类要求，但当前标题尚未被明确批准。

---

# 1. 中心问题

`HUMAN-ORIGINATED / AI-FORMULATED`

AI Agent 可以承担越来越多的检索、结构化、起草、修订、形式化、检查与格式处理工作；人的阅读、理解、判断和责任并不会自动按同样速度扩展。因此，方法论文章提出：

> **一个长期 AI 辅助研究项目，怎样既扩展人的认知能力，又保持人类对意义、判断、批准、证据与责任的持久控制？**

短语 **generation–verification asymmetry（生成—验证不对称）** 是 `AI-PROPOSED` 的问题标签，尚不是经批准的中心术语。

---

# 2. 可供审阅的命题集合

## T1 — 持久研究状态命题

**来源：** `HUMAN-ORIGINATED`

长期人机研究项目的思想连续性，不应依赖于某一个聊天窗口、某一个模型、某一个账号记忆或某一个 Agent 的私有上下文。与项目相关的持久状态应当被外部化到显式、受版本控制的仓库文档中。

**创始依据：** Article Content Core C3、C8；HARC Protocol Core P1、P9、P10。

---

## T2 — 分层语义治理命题

**来源：** `HUMAN-CONFIRMED / AI-FORMULATED`

项目至少应区分并分别保存：

1. 人类实质性承诺；
2. 人类形式/呈现意图；
3. 人类历史决定；
4. AI 维护的操作性表示；
5. 证据约束；
6. 批准状态；
7. 派生文本/成果。

修改应当上游优先传播，使下游 AI 表达不能静默重新定义上游人类意图。

表达 **semantic version control（语义版本控制）** 是对这一架构的 `AI-PROPOSED` 术语；底层的分离和传播规则来自人类。

**创始依据：** Article Content Core C4；HARC Protocol Core P2–P5、P12。

---

## T3 — 认知劳动委托 / 人类治理命题

**来源：** `HUMAN-ORIGINATED / AI-FORMULATED`

大量认知劳动可以委托给 AI，但这并不意味着人类理解、判断、确认或责任可以整体委托。一个由人类治理的研究过程必须识别：哪些高层思想决定仍然需要有意义地处于人类控制中。

候选高杠杆责任节点包括：

- 研究目的与问题选择；
- 核心主张的接受/拒绝；
- 主要推论关系；
- 关键证据冲突的处理；
- 对重要 AI 提议的接受；
- Framework Approval；
- 适用时的 Final Artifact Approval。

表达 **responsibility concentration（责任集中）** 是 `AI-PROPOSED`；关于“人类责任与能力边界”的底层问题来自人类。

**创始依据：** Article Content Core C2；HARC Protocol Core P17。

---

## T4 — Framework Responsibility Thesis

**来源：** `HUMAN-ORIGINATED`，但**适用强度仍未解决**。

对于长篇成果，一份经过人类审阅并批准的紧凑思想架构表示，应作为主要实质性责任锚点。它应暴露人类实际理解并接受的核心命题、推论关系、关键区分、范围条件及章节/小节功能。

**尚未决定的强度：**

- **强版本：** Framework Approval 一般性地构成 AI 辅助长篇成果中实质性思想作者身份的中心。
- **中等版本：** Framework Approval 是 HARC 提出的、用于集中实质性人类审阅的治理架构，而不声称自己已经给出作者身份的一般理论。

在人类明确选择之前，不得把更强版本归于人类作者。

**创始依据：** Article Content Core C5；HARC Protocol Core P6、P13。

---

## T5 — 双批准门命题

**来源：** `HUMAN-ORIGINATED` + `EVIDENCE-CONSTRAINT`

Framework Approval 与 Final Artifact Approval 是两个不同的门槛。

- **Framework Approval** 确认思想架构。
- **Final Artifact Approval** 涉及具体发布/投稿版本，并必须满足适用的学术、机构、出版商或发布渠道要求。

这一机制允许 AI 在 provisional 状态下大量扩写，而不假定 framework approval 本身就自动满足公开作者身份/问责要求。

**创始依据：** Article Content Core C6。

**证据约束：** 当前 ICMJE 与部分 Nature Portfolio 政策把人类作者身份与最终批准/问责联系起来；这些政策约束文章的表达，但不是关于作者身份的普遍法律。

---

## T6 — Framework Projection Thesis

**来源：** `HUMAN-ORIGINATED`

经人类批准的 framework 应当可以从最终成果面向读者的总览中恢复。论文中通常表现为摘要/引言；书籍中表现为导论/总览及章节路线图；其他成果使用相应高层概览。

这提供一个实用忠实性检查：读者被告知的作品结构，是否与人类实际批准的 framework 对应。

**创始依据：** Article Content Core C7；HARC Protocol Core P7。

---

## T7 — 可替换 Agent / 持久项目命题

**来源：** `HUMAN-ORIGINATED`

AI Agent 应当可替换，而不破坏项目连续性。项目的持久身份应存在于人类治理的仓库状态中，而不是某个模型的隐藏上下文中。

这并不意味着无限上下文。长期记忆应通过紧凑当前状态、历史日志/归档、索引与选择性检索扩展。

**创始依据：** Article Content Core C3、C8；HARC Protocol Core P9–P10。

---

## T8 — 实际可复用命题

**来源：** `HUMAN-ORIGINATED`

HARC 应能够在未来论文、书籍、文章、报告及长期思想项目中实际实施并复用。因此其架构必须具体到可通过仓库文件、模板、更新规则和批准状态实例化。

**创始依据：** Article Content Core C9；HARC Protocol Core P11。

### 经验验证扩展

`AI-PROPOSED`

HARC 可以进一步发展成经验方法论研究计划，例如 handoff test、semantic-drift test、framework-fidelity test、review-effort study 与 cross-model portability test。

它目前属于研究议程提议，不属于人类批准的核心命题。

---

## T9 — Critical Clarification Governance Thesis

**来源：** `HUMAN-ORIGINATED`

当 AI 对作者意图、核心命题、关键概念、范围、主要推论关系、章节功能或关键术语/翻译存在可能重大影响作品结构的非微不足道不确定性时，AI 不应自行选择一种解释，而应把问题提升到 Critical Clarification Register，由人类确认或纠正。

未解决 clarification 不是人类承诺。解决结果必须进入 Decision Log 与适当 Core，再传播到 Working Framework 与派生文本。

**创始依据：** Article Content Core C11；HARC Protocol Core P19。

---

## T10 — Zero-context Onboarding Thesis

**来源：** `HUMAN-ORIGINATED / AI-FORMULATED`

持久仓库状态只有在新的 AI Agent 能够可靠发现并按正确顺序读取它时，才能真正支持跨 Agent 连续性。因此，HARC 应提供显式零上下文入口、mandatory read order、机器可读 manifest 与 Onboarding Handshake。

成功接管不应被假定，而应通过 Agent 向人类报告当前规范状态、Blocking Clarifications、Framework/Artifact 状态和同步缺陷来验证。

**创始依据：** Article Content Core C12；HARC Protocol Core P20。

---

# 3. 文章必须保留的核心区分

### 人类原创区分

- 人类研究内容意图 vs 人类形式/呈现意图；
- 人类意图 vs AI 操作性表示；
- Working Framework vs Approved Framework；
- framework defect vs derived-expansion defect；
- Framework Approval vs Final Artifact Approval；
- 持久仓库状态 vs 临时 Agent/聊天上下文；
- 当前规范状态 vs 历史状态。

### 若提升为中心术语则仍需确认的 AI 表述

- cognitive labor vs epistemic responsibility；
- contribution transparency vs authorship/accountability；
- semantic version control vs 普通文本版本控制；
- responsibility concentration vs 持续逐行人类生产。

---

# 4. 修订后的文章架构

早期 12 部分结构在持久状态、Agent 替换和批准/责任部分存在重叠。下面提出更紧凑的 10 部分结构。

## I. 引言 — AI 扩展生产能力的速度快于人类审阅

**功能：** 定义方法论问题，说明核心不是“AI 能不能生成文本”，而是研究状态与判断如何治理。

`AI-PROPOSED TERM`：generation–verification asymmetry。

## II. 为什么以聊天为中心的研究协作在结构上脆弱

**功能：** 建立问题场景：semantic drift、context dependence、authorship ambiguity、presentation drift、Agent handoff failure。

支持 T1 与 T7。

## III. 以仓库为中心的持久研究状态

**功能：** 说明 GitHub 作为当前实现基础；区分 persistent memory 与 infinite context；引入当前状态与历史状态的压缩结构；进一步说明新的 Agent 必须通过 zero-context bootstrap、manifest 和 Onboarding Handshake 才能可靠接管。

支持 T1、T7 与 T10。

## IV. 分层语义治理

**功能：** 引入 Content Core、Form Core、Decision Log、Critical Clarification Register、evidence、provenance status、upstream-first propagation，以及人类承诺与 AI 提议的区分；说明高影响不确定性为何必须先由人类解决再进入 framework。

支持 T2、T8 与 T9。

`AI-PROPOSED TERM`：semantic version control。

## V. 操作性 Framework 与人类确认

**功能：** 解释 Working Argument Map、Approved Framework snapshot、不可变/版本化规则，以及为什么紧凑 framework 是主要结构讨论界面。

支持 T4。

## VI. 认知劳动委托与人类认识责任

**功能：** 处理文章的哲学中心：AI 可以做什么、人类必须理解/授权什么，以及为什么“工作委托”不能自动解决“责任委托”。

支持 T3。

`HUMAN DECISION REQUIRED`：中心术语与规范命题强度。

## VII. 两类缺陷、两个批准门与一个公开结构

**功能：** 整合 framework defect vs expansion defect、Framework Approval vs Final Artifact Approval，以及 framework 向摘要/引言/概览的投影。

支持 T5 与 T6。

## VIII. 既有思想与制度背景

**功能：** 谨慎比较 HARC 与 extended/distributed cognition、epistemic dependence、automation reliance、contribution taxonomy 及当前部分 authorship/AI policy。

文献的作用是给 HARC 提供背景并限制其主张；不能借此暗示 HARC 自己的概念已经被这些文献证明。

## IX. 局限、反对意见与可能的验证

**功能：** 讨论 rubber-stamp approval、压缩损失、证据/细节错误、能力限制、仓库开销、隐私/保密、领域差异及 AI 能力变化。

可能的经验测试套件在此属于 `AI-PROPOSED FUTURE RESEARCH`，除非人类明确把它提升为文章核心命题。

## X. 结论 — 从 AI 文本生成走向扩展认知的治理

**功能：** 重申中心提议：AI 可以扩展研究活动规模，但只有在意义、权威、证据、批准与责任保持显式可审计时，这种扩展才具有可治理性。

---

# 5. 依赖结构

```text
T1 持久研究状态
├── 使 T7 可替换 Agent / 持久项目成为可能
└── 为 T2 分层语义治理提供基础设施

T2 分层语义治理
├── 防止 AI 静默漂移替代人类意图
├── 通过 T9 把高影响不确定性送入人类澄清
└── 使可检查 Working Framework 成为可能

T3 认知劳动委托 / 人类治理
└── 为 T4 Framework Responsibility 提供动机

T4 Framework Responsibility
├── 需要 T5 双批准门
└── 需要 T6 Framework Projection 以保证公开成果忠实性

T1 + T2 + T4 + T5 + T6 + T7
└── 共同支持 T8 作为可执行协作协议的实际可复用性
```

该依赖图由 AI 组织，属于 `AI-FORMULATED`，在人类批准前仍需审阅。

---

# 6. 证据/文献角色

文章目前使用：

- Clark & Chalmers (1998) — 可能的外部认知比较；
- Hutchins (1995) — distributed cognition 背景；
- Hardwig (1985) — epistemic dependence；
- Parasuraman & Riley (1997) — automation reliance；
- ICMJE — 当前部分 authorship/final-approval/accountability 要求；
- Nature Portfolio — 当前部分 AI/authorship policy 约束；
- CRediT — contribution-role transparency 与 authorship determination 的区分；
- UNESCO — 以人为中心的生成式 AI 治理背景。

核验过的来源笔记维护在 `evidence/METHODOLOGY_SOURCES.zh-CN.md`；参考文献元数据维护在 `paper/methodology-references.bib`。

**证据规则：** 上述任何来源都不能单独证明 HARC 所提出的 framework 架构、`semantic version control`、`responsibility concentration` 或其经验有效性。

---

# 7. 创建 `MA-FW-001` 之前需要的人类澄清

高影响未决问题现在统一维护在 `docs/clarification-register.zh-CN.md`。

### 当前 Blocking Clarifications

- `CLR-001` — 中心责任概念；
- `CLR-002` — Framework Responsibility Thesis 强度；
- `CLR-005` — `responsibility concentration` 是否保留/替换。

这些问题必须在 `MA-FW-001` 前由人类明确解决，或明确标为 `DEFERRED` 并在 framework 中保留其未决状态。

### 当前 Non-blocking Clarifications

- `CLR-003` — `semantic version control`；
- `CLR-004` — `generation–verification asymmetry`；
- `CLR-006` — extended/distributed cognition 的理论地位；
- `CLR-007` — 经验验证计划；
- `CLR-008` — 学科/投稿方向。

完整候选解释、AI 建议、影响范围和人类答复字段见 Clarification Register；Argument Map 不再重复维护同一澄清的全部细节。

---

# 8. 当前同步状态

- Founder commitments -> Article Content Core：`SYNC AFTER PROVENANCE CORRECTION`。
- Article Content Core -> 本 map：`SYNC`，并已加入 T9 Critical Clarification Governance。
- 本 map -> 方法论文章草稿：`PARTIALLY SYNC`；当前草稿仍反映较早 12 部分组织与部分更强 AI 术语，因此在人类审阅 framework 之前不应进行结构性重写。
- Evidence layer -> policy/literature claims：`RECHECKED 2026-09-17`；投稿前必须重新核验目标渠道的时效性政策。
- Clarification Gate：`OPEN — CLR-001 / CLR-002 / CLR-005 BLOCKING`。
- Framework Approval：`NOT YET COMPLETED`。
- Final Artifact Approval：`NOT YET COMPLETED`。
- 中文与英文：`BILINGUAL SYNC REQUIRED`；中文是规范基准。

批准状态另见 `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`。
