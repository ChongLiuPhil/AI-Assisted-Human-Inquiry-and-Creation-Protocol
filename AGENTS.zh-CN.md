# AGENTS.md — HARC Agent 协作契约

本仓库定义 **Human–AI Research Collaboration Protocol（HARC，人类—AI 研究协作协议）**。任何在本仓库中工作、或把本仓库作为模板使用的 AI Agent，都必须把仓库状态视为持久的协作基础设施。

> **语言规则：本文件的中文版本是规范性基准；英文 `AGENTS.md` 是同步镜像。**

## 1. 不依赖聊天记忆

任何特定聊天、模型、厂商、账号记忆、隐藏 scratchpad 或本地上下文，都不是项目的规范性记忆。

如果一条人类指令应当约束未来工作，就必须把它显式持久化到适当的仓库文件中。

## 2. 保持三个不同的领域

在处理实质性人类反馈之前，先将其归类为以下一个或多个类别：

- `CONTENT` — 研究意义、主张、区分、假设、问题、结论；
- `FORM` — 成果类型、文本呈现、字体、版式、引用样式、视觉系统、渲染方式；
- `PROTOCOL` — 协作规则、持久化、版本、批准、交接、同步。

不要为了方便而把这些领域混在一起。

## 3. 研究项目中的规范性优先级

### 内容链

`人类内容决定 > CONTENT_CORE > 已批准框架 > Working Argument Map > 派生文本`

### 形式链

`人类形式决定 > FORM_CORE > 外部发布约束 / 可复用配置 > 实现默认值 > 渲染成果`

### 协议链

`人类工作流决定 > 项目协议文件 > Agent 默认行为`

下游层不得静默违背上游层。

## 4. 上游优先更新

### CONTENT

1. 在 `DECISION_LOG.md` 记录人类决定。
2. 校准 `CONTENT_CORE.md`。
3. 校准 Working Argument Map。
4. 如果修改实质性改变了已经批准的 framework，将项目标为不同步，并请求/创建新的 framework 版本。
5. 之后才能把修改传播到派生正文。

### FORM

1. 记录决定。
2. 校准 `FORM_CORE.md`。
3. 传播到排版/渲染实现。
4. 不要把 AI 的临时默认值升级成人类偏好。

### PROTOCOL

1. 记录决定。
2. 校准协议/治理文件。
3. 如果规则具有通用性，更新可复用模板。

## 5. 关键澄清登记册

当 AI 对作者意图或关键内容存在**高影响、非微不足道的不确定性**时，不得自行选择一种解释后继续传播。

应把问题写入 `docs/clarification-register.zh-CN.md`，至少说明：

- 不确定点；
- 候选解释；
- 为什么重要；
- `BLOCKING / NON-BLOCKING`；
- 受影响文件 / 命题 / 章节；
- AI 建议（如有，标为 `AI-PROPOSED`）；
- 需要人类回答的问题。

特别关注：

- 核心观点或命题的强/弱解释；
- 关键概念；
- 范围与限定条件；
- 主要推论关系；
- 章节功能；
- 作者母语术语与英文对应；
- 翻译可能造成的语义改变；
- 新反馈与旧 Core / Framework 的潜在冲突。

人类确认或纠正后，必须执行：

`Clarification Register -> Decision Log -> appropriate Core -> Working Argument Map -> Derived Artifact`

仅把条目标记为 resolved 而不更新 Core，不算完成。

在重大阶段转换、Framework Approval、关键术语全篇传播、正式翻译、大规模扩写与 Final Review 前，主动进行 Clarification Scan。

## 6. AI 提议只是提议

AI 生成的论点、区分、重组、术语、版式或审美选择，不会因为已经写进文件就自动成为人类承诺。

在人类接受之前：

- 内容提议应在操作层明确标为 `AI-PROPOSED`；
- 形式提议不得进入 `FORM_CORE.md`；
- 协议提议应保持提议状态，不得静默变成强制规则。

## 7. Working Framework 与 Approved Framework

当前 Argument Map 是可变的、由 AI 维护的工作框架。

只有通过显式的 **Framework Approval Gate（框架批准门）** 才产生人类认可。批准后，创建诸如 `FW-001.md` 的版本化不可变快照。

实质性思想变化要求产生新的框架版本。

## 8. 证据冲突

人类作者权威涉及“作者想主张什么”，不意味着可以压制证据。

如果证据、形式推理或来源核验与当前人类承诺冲突：

1. 保留当前作者意图；
2. 显式呈现冲突；
3. 不得明知有问题仍在下游写成误导性主张；
4. 把问题提交人类决定；
5. 记录最终决定。

## 9. 最终成果状态

Framework Approval 后，AI 可以生成大量派生文本，但在最终人类审阅前仍属于 `DERIVED-PROVISIONAL`。

除非相应的最终批准门已经完成，否则不得把成果描述为“可投稿”或“已经由人类批准”。

## 10. 记忆扩展

规范性文件应保持足够紧凑，使 Agent 可以日常接管。详细历史可以增长在日志、证据文件和归档中。

当历史变大时：

- 保留原始记录；
- 创建索引/摘要；
- 让当前状态核心保持简洁；
- 按需检索历史细节。

目标是可恢复的项目记忆，而不是强迫每个 Agent 一次性加载整个档案。

## 11. 交接标准

一个新的、能力合格的 AI Agent 应当无需原始对话历史，只通过仓库即可重建项目当前状态。

如果做不到，项目存在持久化缺陷。

## 12. 多轮审计是“审查—修复”循环

如果人类要求多轮审计，每一轮都必须包含：

1. 审查；
2. 识别缺陷/遗漏；
3. 修复或实现；
4. 验证修复。

不要把“审核三遍”解释成三次被动阅读然后只修一次。若人类要求，完成指定轮次后，再进行一次独立的修复后审计。

## 13. 把方法论文章作为受治理的研究成果维护

本仓库有两个主要产出：

1. 可执行的 HARC 开放协议；
2. 一篇解释并批判性发展该协议的方法论文章。

方法论文章应按以下顺序读取：

1. `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`
2. `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`
3. `docs/clarification-register.zh-CN.md`
4. `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`
5. `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`
6. `evidence/METHODOLOGY_SOURCES.zh-CN.md`
7. `paper/methodology-references.bib`
8. `paper/METHODOLOGY_ARTICLE.zh-CN.md`

在中文 framework 未被人类明确批准之前，文章 Argument Map 仍是 `WORKING-FRAMEWORK`。在相关批准门完成之前，正文仍是 `DERIVED-PROVISIONAL`。

方法论文章必须遵守它所描述的 HARC 原则。不能因为 AI 提议的术语或结构已经写进草稿，就把它当成人类批准。涉及作者身份、AI 政策、认识责任、自动化或认知的外部研究发生变化时，应先更新证据层，并区分规范性的 HARC 提案与外部出版规则。

## 14. 审计记录

按以下角色使用审计文件：

- `docs/FOUNDING_IDEA_AUDIT.zh-CN.md` — 创始思想覆盖清单与可追溯记录；
- `docs/THREE_CYCLE_REPAIR_AUDIT.zh-CN.md` — 三轮 `审查 -> 修复 -> 验证` 的执行记录；
- `docs/FINAL_POST_REPAIR_AUDIT.zh-CN.md` — 三轮修复完成后的独立终审。
- `docs/BILINGUAL_PARITY_AUDIT.zh-CN.md` — 双语文件配对与高风险语义同步审计。

若这些文件在流程状态上冲突，以较后的修复/终审记录解释流程；`core/DECISION_LOG.zh-CN.md` 中的人类决定仍然具有规范权威。

## 15. 当本仓库被用作模板

依次读取：

1. `protocol/SPECIFICATION.zh-CN.md`
2. `protocol/PERSISTENT_MEMORY.zh-CN.md`
3. `protocol/FRAMEWORK_APPROVAL.zh-CN.md`
4. `protocol/FORM_CONTENT_ROUTING.zh-CN.md`
5. `protocol/FORM_PROFILE_INHERITANCE.zh-CN.md`
6. `protocol/BILINGUAL_SYNC.zh-CN.md`
7. `templates/research-project/README.zh-CN.md`

然后只实例化新项目中人类实际提供的决定。未知项保持显式未知，不要用 AI 假设填满。

## 16. 中文规范基准 / 英文同步镜像

HARC 是一个中英双语项目。

对于实质性 Markdown 内容：

- 中文版本是规范性的语义与编辑基准；
- 英文版本是同步翻译镜像；
- 对中文的任何实质性修改，必须在同一工作轮次中同步到英文；
- 中英文存在实质性不一致时，工作不得标记为完成；
- 如中英文冲突，以中文为准，并必须修复英文；
- 新的实质性文档应从创建时即生成中英文配对版本。

推荐命名：

- 中文 canonical：`NAME.zh-CN.md`
- 英文 mirror：如果为了 GitHub 默认渲染或兼容既有路径，可使用 `NAME.md`；否则使用 `NAME.en.md`。

语言中立的技术文件（如 BibTeX、schema、代码、原始数据）无需只为翻译而复制，但围绕它们的人类可读说明仍须双语。

编辑双语文件时，把“两种语言同步”视为一个原子任务。只更新一种语言不得标记为完成。

### 规则切换前的 legacy exception

对于 2026-09-18 双语规则建立前已经存在的文件，如果英文历史版本实际上包含中文版尚未吸收的较新实质内容，应先把这些英文发展合并进中文，使中文达到切换时的最新状态，再同步英文。完成这一 legacy catch-up 后，正常方向固定为：

`人类决定 -> 中文 canonical -> 英文 synchronized mirror`

此后英文不得独立发展实质内容。
