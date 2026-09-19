# 方法论文章 — Working Argument Map

**状态：** `WORKING-FRAMEWORK — REVIEW READY / BLOCKING CLARIFICATIONS RESOLVED; HUMAN APPROVAL PENDING`  
**成果类型：** 方法论文章  
**人类批准：** 尚未完成  
**派生草稿状态：** `DERIVED-PROVISIONAL`

> **本中文文件是规范性基准；英文 `METHODOLOGY_ARTICLE_ARGUMENT_MAP.md` 是同步镜像。**

## 规范上游文件

- `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`
- `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`
- `core/PROTOCOL_CORE.zh-CN.md`
- `core/DECISION_LOG.zh-CN.md`
- `docs/working-memory.zh-CN.md`
- `evidence/METHODOLOGY_SOURCES.zh-CN.md`

## 来源状态图例

- `HUMAN-ORIGINATED` — 实质性承诺由人类发起人明确提出或明确确认。
- `HUMAN-ORIGINATED / AI-FORMULATED` — 实质思想来自人类，但当前措辞或概念压缩由 AI 生成。
- `AI-PROPOSED` — 尚未进入人类批准的思想架构。
- `EVIDENCE-CONSTRAINT` — 外部来源约束一个主张可以怎样负责任地表达；它本身不自动成为人类承诺。

这些标签的目的，是防止成熟的 AI 术语被误认为创始人亲自提出的理论。

---

## 工作标题

**从对话到持久研究状态：AI时代的人机研究协作、人类责任与可审计作者性**  
*From Conversation to Persistent Research State: Human–AI Research Collaboration, Human Responsibility, and Auditable Authorship in the AI Era*

`HUMAN-APPROVED TITLE — HARC-D024` — 中文题目已由人类明确认可；英文为同步翻译镜像。题目获批不等于完整 Working Framework 已获 Framework Approval.

---

# 1. 中心问题

`HUMAN-ORIGINATED / AI-FORMULATED`

AI Agent 可以执行或辅助越来越多的检索、结构化、起草、修订、形式化、检查与格式处理工作；人的阅读、理解、判断与责任承担能力并不会自动按同样速度扩展。因此，方法论文章提出：

> **一个长期 AI 辅助研究项目，怎样在扩展研究工作的执行与表达能力时，仍确保项目目的、方向、核心判断与公开知识传播最终由人类作为责任主体来理解、批准和承担责任？**

这里的“人类责任”不是一个未经定义的抽象属性，而是“**人类仍是责任主体／责任承担者**”的简写。尤其当研究、探究结果或知识主张进入公开传播时，不能把最终责任主体位置转移给 AI。

短语 **generation–verification asymmetry（生成—验证不对称）** 是 `AI-PROPOSED` 的问题标签，尚不是经批准的中心术语.

---

# 2. 可供审阅的命题集合

## T1 — 持久研究状态命题

**来源：** `HUMAN-ORIGINATED`

长期人机研究项目的思想连续性，不应依赖于某一个聊天窗口、某一个模型、某一个账号记忆或某一个 Agent 的私有上下文。与项目相关的持久状态应当被外部化到显式、受版本控制的仓库文档中。

**创始依据：** Article Content Core C3、C8；AHICP Protocol Core P1、P9、P10。

---

## T2 — 分层语义治理命题

**来源：** `HUMAN-CONFIRMED / AI-FORMULATED`

项目至少应区分：

1. Layer 1 — 人类作者核心基础；
2. Layer 2 — 当前论述框架；
3. Layer 3 — 派生成果；
4. 与三层并行的 Working Memory；
5. 人类形式/呈现意图；
6. 历史决定；
7. 证据约束；
8. 批准状态。

前三层构成长时研究记忆；Working Memory 保存当前阶段、目标、任务、阻塞、clarification、TODO 与 handoff。

修改应当上游优先传播，使下游 AI 表达不能静默重新定义上游人类意图。

表达 **semantic version control（语义版本控制）** 是对这一架构的 `AI-PROPOSED` 术语；底层的分离和传播规则来自人类。

**创始依据：** Article Content Core C4；AHICP Protocol Core P2–P5、P12。

---

## T3 — AI 工具工作分担 / 人类责任主体命题

**来源：** `HUMAN-ORIGINATED / AI-FORMULATED`

研究或创作项目的目的、核心问题与方向应由人类给予、发起并持续导航或批准。AI Agent 在 AHICP 中作为工具，可以执行或辅助大量检索、综合、结构化、起草、重组、核查、格式处理和其他工作，但不应被描述为具有认知性的主体，也不应使用“AI 承担认知劳动 / 认知任务”作为中心表述。

AI 能够执行大量工作，并不意味着项目目的、核心判断或最终责任主体位置可以转移给 AI。更精确地说，AHICP 要求**人类保持为责任主体**。

这一责任主体地位至少体现在：

- 研究目的、问题与方向的发起、理解与授权；
- 核心主张的接受/拒绝；
- 主要推论关系；
- 关键证据冲突的处理；
- 对重要 AI 提议的接受；
- Framework Approval；
- 适用时的 Final Artifact Approval；
- 特别是在论文、书籍、报告或其他形式的公开知识传播中，对最终知识主张与公开版本承担责任。

`responsibility concentration` 不再作为当前中心术语。“人类责任”在标题或一般叙述中可以作为简写，但理论上应解释为“人类是责任主体 / humans remain the bearers of responsibility”。

**创始依据：** Article Content Core C2、C16；AHICP Protocol Core P17；HARC-D023、HARC-D024.

## T4 — Framework Responsibility Thesis

**来源：** `HUMAN-ORIGINATED`；HARC-D024 对 HARC-D023 的责任措辞作进一步精确化。

对于 AI 辅助的长篇研究或创作成果，Layer 2 Current / Approved Framework 应作为**人类作为责任主体时，其核心思想责任的主要结构性承载点**。它不是仅供 AI 使用的摘要，而是人类作者必须真正理解、审核并明确确认的思想结构。

Framework Approval 前，人类作者必须对其中实际呈现的全部实质内容形成清晰、完整的理解，并逐项审核和确认，包括：

- 核心命题；
- 推论关系及其逻辑依赖；
- 关键区分；
- 范围条件；
- 章节/小节功能；
- 被纳入 framework 的具体措辞。

Framework 可以由 AI 辅助提出、组织和表达，但获批版本必须真实体现人类作者的核心思想与认同。人类承担该 framework 所承载的原创性、理解、判断与思想责任；AI 不能成为这一责任的承担主体。

这一命题是 AHICP 的治理架构，并不声称 Framework Approval 自动构成所有领域的一般作者身份理论，也不取消 Final Artifact Approval、事实准确性、研究诚信或目标渠道规则。尤其在公开传播知识主张时，责任主体仍必须是人类。

**创始依据：** Article Content Core C5、C16；AHICP Protocol Core P6、P13、P17；HARC-D023、HARC-D024.

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

**创始依据：** Article Content Core C7；AHICP Protocol Core P7。

---

## T7 — 可替换 Agent / 持久项目命题

**来源：** `HUMAN-ORIGINATED`

AI Agent 应当可替换，而不破坏项目连续性。项目的持久身份应存在于人类治理的仓库状态中，而不是某个模型的隐藏上下文中。

这并不意味着无限上下文。长期记忆应通过紧凑当前状态、历史日志/归档、索引与选择性检索扩展。

**创始依据：** Article Content Core C3、C8；AHICP Protocol Core P9–P10。

---

## T8 — 实际可复用命题

**来源：** `HUMAN-ORIGINATED`

AHICP 应能够在未来论文、书籍、文章、报告及长期思想项目中实际实施并复用。因此其架构必须具体到可通过仓库文件、模板、更新规则和批准状态实例化。

**创始依据：** Article Content Core C9；AHICP Protocol Core P11。

### 经验验证扩展

`AI-PROPOSED`

AHICP 可以进一步发展成经验方法论研究计划，例如 handoff test、semantic-drift test、framework-fidelity test、review-effort study 与 cross-model portability test。

它目前属于研究议程提议，不属于人类批准的核心命题。

---

## T9 — Working Memory / Clarification Governance Thesis

**来源：** `HUMAN-CONFIRMED / AI-FORMULATED`

当 AI 对作者意图、核心命题、关键概念、范围、主要推论关系、章节功能或关键术语/翻译存在高影响不确定性时，不应自行选择一种解释，而应把它作为 Working Memory 中的 Clarification item 提交人类确认。

Clarification 不是 Layer 1.5。未解决 item 不是人类长期承诺。

人类解决后，应执行 Promotion：

`Working Memory -> Decision Log -> appropriate Long-Term Memory destination`

如果涉及人类核心内容，则继续：

`Layer 1 Core -> Layer 2 Framework -> Layer 3 Artifact`

**创始依据：** Article Content Core C11、C14；AHICP Protocol Core P19、P23；HARC-D021。

---

## T10 — Zero-context Onboarding Thesis

**来源：** `HUMAN-ORIGINATED / AI-FORMULATED`

持久仓库状态只有在新的 AI Agent 能够可靠发现并按正确顺序读取它时，才能真正支持跨 Agent 连续性。因此，AHICP 应提供显式零上下文入口、mandatory read order、机器可读 manifest 与 Onboarding Handshake。

成功接管不应被假定。Agent 应先从 Working Memory 报告当前阶段、目标、active tasks、最近完成、next actions、blockers 与 pending human decisions，再按任务读取 Framework/Artifact 等长期状态。

**创始依据：** Article Content Core C12；AHICP Protocol Core P20。

---

## T11 — Repository-Backed Context Thesis

**来源：** `HUMAN-CONFIRMED / AI-FORMULATED`

跨 Agent 连续性不要求在聊天上下文中维护第二份动态项目状态。

AHICP 应把 GitHub 作为权威外部记忆与工作状态接口：

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

Agent 根据当前任务按需读取最新 canonical 文件；高影响判断和写入前重新确认 revision；更新直接 write-through 到 GitHub；写入后旧上下文缓存立即失效。

会话中只保留最小 Repository Resolver。Working Memory 与三层长期记忆都留在 GitHub，并按需读取，而不是复制成聊天内长期副本。

**创始依据：** Article Content Core C13；AHICP Protocol Core P21–P22；HARC-D020。


---

## T12 — Long-Term / Working Memory Separation Thesis

**来源：** `HUMAN-ORIGINATED / AI-FORMULATED`

AHICP 的三个内容层都是 Long-Term Research Memory：

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

其中 Layer 2 虽然更可修改，却仍属于长期项目记忆，因为它保存当前稳定的论述结构、核心命题与关键概念。

与三层并行的 Working Memory 保存当前阶段、目标、任务、完成状态、下一步、TODO、blockers、pending human decisions、clarifications 与 handoff。

Working Memory 中形成稳定人类确认的内容必须 Promotion 到相应长期层。

**创始依据：** Article Content Core C14；AHICP Protocol Core P23；HARC-D021。

---

## T13 — Operational / Retrospective Working Memory Separation Thesis

**来源：** `HUMAN-ORIGINATED / AI-FORMULATED`

Working Memory 不应被固定成一个不断膨胀的单体状态文档。它至少应区分：

`Current Focus + Task Plan = operational resume state`

与：

`Work Log = human retrospective history`

Current Focus 让新 Agent 知道当前最重要的事情；Task Plan 让新 Agent 知道如何继续推进；Work Log 让人类作者以后回顾项目与思想路径如何变化。

因此 Work Log 默认不属于 AI onboarding 必读上下文。它应定期生成阶段性纪要，但不保存 AI 隐藏推理，也不替代长期规范状态。

**创始依据：** Article Content Core C15；AHICP Protocol Core P24；HARC-D022。

---

# 3. 文章必须保留的核心区分

### 人类原创区分

- 人类研究内容意图 vs 人类形式/呈现意图；
- 人类意图 vs AI 操作性表示；
- AI 工具可以执行/辅助的工作 vs 谁是责任承担主体；
- AI 作为协作工具 vs 人类作为项目目的与方向的发起/授权主体及责任主体；
- “人类责任”作为一般简写 vs “人类是责任主体”这一更精确命题；
- Working Framework vs Approved Framework；
- framework defect vs derived-expansion defect；
- Framework Approval vs Final Artifact Approval；
- 三层 Long-Term Research Memory vs 并行 Working Memory；
- Current Focus / Task Plan 的 operational resume state vs Work Log 的 human retrospective history；
- 权威仓库状态 vs 临时 Agent 检索缓存；
- 当前规范状态 vs 历史状态。

### 若提升为中心术语则仍需确认的 AI 表述

- contribution transparency vs authorship/accountability；
- semantic version control vs 普通文本版本控制；
- generation–verification asymmetry 作为 heuristic label 的地位。

`responsibility concentration` 已由人类决定不作为当前中心术语；“cognitive labor / 认知劳动”也不应用来描述 AI 所承担的工作.

# 4. 修订后的文章架构

早期 12 部分结构在持久状态、Agent 替换和批准/责任部分存在重叠。下面提出更紧凑的 10 部分结构。

## I. 引言 — AI 扩展生产能力的速度快于人类审阅

**功能：** 定义方法论问题，说明核心不是“AI 能不能生成文本”，而是研究状态与判断如何治理。

`AI-PROPOSED TERM`：generation–verification asymmetry。

## II. 为什么以聊天为中心的研究协作在结构上脆弱

**功能：** 建立问题场景：semantic drift、context dependence、authorship ambiguity、presentation drift、Agent handoff failure。

支持 T1 与 T7。

## III. 以仓库为中心的持久研究状态

**功能：** 说明 GitHub 作为当前实现基础；区分三层 Long-Term Research Memory、并行 Working Memory 与 infinite context；说明新 Agent 先从 Working Memory 找到续接点，再通过 repository-backed selective retrieval 读取长期状态。

支持 T1、T7、T10、T11、T12 与 T13。

## IV. 分层语义治理

**功能：** 引入 Layer 1 Core、Layer 2 Framework、Layer 3 Artifact、Working Memory、Decision Log、evidence、provenance status 与 upstream-first propagation；说明 Clarification 为什么属于 Working Memory，以及稳定结果怎样 Promotion 到长期记忆。

支持 T2、T8 与 T9。

`AI-PROPOSED TERM`：semantic version control。

## V. 操作性 Framework 与人类确认

**功能：** 解释 Working Argument Map、Approved Framework snapshot、不可变/版本化规则，以及为什么紧凑 framework 是主要结构讨论界面。

支持 T4。

## VI. AI 工具工作分担与人类责任主体 / Framework 责任

**功能：** 处理文章的哲学中心：AI 工具可以执行或辅助哪些研究工作；为什么项目目的、问题与方向必须由人类给予、导航和批准；为什么在人机协作的研究、探究以及尤其公开知识传播中，人类必须保持为责任主体；以及为什么这一责任主体地位在长篇成果中主要通过其真正理解并确认的 Layer 2 Framework 落实。

本节不得把 AI 描述为具有认知性的主体，也不得以“AI 承担认知劳动 / 认知任务”为中心概念。

支持 T3 与 T4.

## VII. 两类缺陷、两个批准门与一个公开结构

**功能：** 整合 framework defect vs expansion defect、Framework Approval vs Final Artifact Approval，以及 framework 向摘要/引言/概览的投影。

支持 T5 与 T6。

## VIII. 既有思想与制度背景

**功能：** 谨慎比较 AHICP 与 extended/distributed cognition、epistemic dependence、automation reliance、contribution taxonomy 及当前部分 authorship/AI policy。

文献的作用是给 AHICP 提供背景并限制其主张；不能借此暗示 AHICP 自己的概念已经被这些文献证明。

## IX. 局限、反对意见与可能的验证

**功能：** 讨论 rubber-stamp approval、压缩损失、证据/细节错误、能力限制、仓库开销、隐私/保密、领域差异及 AI 能力变化。

可能的经验测试套件在此属于 `AI-PROPOSED FUTURE RESEARCH`，除非人类明确把它提升为文章核心命题。

## X. 结论 — 从 AI 文本生成走向 AI 扩展研究能力的治理

**功能：** 重申中心提议：AI 工具可以扩展研究活动的执行规模与表达能力，但项目目的、方向、意义、证据约束、framework 批准与最终责任必须保持在人类治理下，并以显式、可审计的仓库状态呈现。

# 5. 依赖结构

```text
T1 持久研究状态
├── 使 T7 可替换 Agent / 持久项目成为可能
├── 为 T10 Zero-context Onboarding 提供需要被发现和重建的持久状态
└── 为 T11 Repository-Backed Context 提供权威外部状态基础

T2 分层语义治理
├── 防止 AI 静默漂移替代人类意图
├── 通过 T9 把高影响不确定性放入 Working Memory
├── 通过 T12 区分 Long-Term Research Memory 与 Working Memory
│   └── T13 进一步区分 operational resume state 与 human retrospective history
└── 使可检查的 Working Framework 与上游优先传播成为可能

T7 可替换 Agent / 持久项目
├── 与 T10 一起保证新 Agent 能找到正确续接入口
└── 与 T11 一起保证 Agent 通过按需读取最新 canonical state 接续项目

T3 AI 工具工作分担 / 人类责任主体
└── 为 T4 Framework Responsibility 提供人类主体与责任基础

T4 Framework Responsibility
├── 需要 T5 双批准门区分思想架构批准与公开版本批准
└── 需要 T6 Framework Projection 检查公开成果是否忠实反映获批思想架构

T9 + T10 + T11 + T12 + T13
└── 把 T1 / T2 / T7 的持久状态、治理与跨 Agent 连续性转化为可执行工作流程

T1 + T2 + T3 + T4 + T5 + T6 + T7 + T9 + T10 + T11 + T12 + T13
└── 共同构成 T8 “AHICP 可实际实施并复用”的主要实现条件
```

该依赖图由 AI 组织，但其结构性修复已经通过 `HARC-D025` 获得人类确认。它表示命题之间的主要支持与实现关系，不声称所有箭头都是形式逻辑上的严格蕴涵。

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

**证据规则：** 上述任何来源都不能单独证明 AHICP 所提出的 framework 架构、`semantic version control` 或其经验有效性。HARC-D023 关于 AI 工具地位与人类 Framework 责任的规范主张属于人类作者的协议/方法论立场，而不是由这些文献直接证明的经验结论。

---

# 7. Framework Approval 前的 Clarification 状态

### 已解决并 Promotion

- `CLR-001` — 中心责任概念：经 HARC-D024 进一步精确化，不把“人类责任”视为自足术语；核心命题是在人机协作研究、探究与尤其公开知识传播中，**人类仍是责任主体／责任承担者**。AI 工具可以分担工作，但不能成为最终责任主体。
- `CLR-002` — Framework Responsibility Thesis：采用 HARC-D023 的第三种人类表述；Layer 2 Framework 是人类核心思想责任的主要结构性承载点，人类必须理解、审核并确认其中全部实质内容。
- `CLR-005` — `responsibility concentration`：不作为当前中心术语继续使用。

### 当前 Non-blocking Clarifications

- `CLR-003` — `semantic version control`；
- `CLR-004` — `generation–verification asymmetry`；
- `CLR-006` — extended/distributed cognition 的理论地位；任何比较都不得被写成 AI 本身具有认知性的前提；
- `CLR-007` — 经验验证计划；
- `CLR-008` — 学科/投稿方向；
- `CLR-010` — 最终发布渠道与渠道特定形式约束（对 Framework Approval 非阻塞）。

**Framework Approval 对未决项的语义（HARC-D025）：** 如果完整 framework 中保留明确标记为 `AI-PROPOSED`、`UNRESOLVED`、`NON-BLOCKING` 或类似状态的项目，整体 `APPROVE` 只批准这些项目作为“未决/提议项目”在 framework 中的位置、范围与处理方式，不批准其实质内容，也不改变其 provenance。后续只有单独的人类决定才能把这些项目 Promotion 为人类确认观点。

完整 active state 见 Task Plan。当前已无 `CLR-001 / CLR-002 / CLR-005` 造成的 Framework Approval blocker；但整体 Working Framework 仍需人类明确批准、修订或拒绝，才能创建 `MA-FW-001`.

# 8. 当前同步状态

- Founder commitments -> Article Content Core：`SYNC — HARC-D023 PROMOTED`。
- Article Content Core -> 本 map：`SYNC — responsibility model updated`。
- 本 map -> 方法论文章草稿：`PARTIALLY SYNC — responsibility terminology/model corrected in this work cycle; full structural rewrite remains deferred pending human Framework Approval`。
- Evidence layer -> policy/literature claims：`RECHECKED 2026-09-17`；投稿前必须重新核验目标渠道的时效性政策。
- Clarification Gate：`BLOCKING CLARIFICATIONS CLEARED — CLR-001 / CLR-002 / CLR-005 RESOLVED/PROMOTED`。
- Framework Approval：`NOT YET COMPLETED — overall human review pending`。
- Final Artifact Approval：`NOT YET COMPLETED`。
- 中文与英文：`BILINGUAL SYNC REQUIRED`；中文是规范基准。

批准状态另见 `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`。
