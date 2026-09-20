# AGENTS.md — AHICP Agent 辅助契约

本仓库定义 **AI-Assisted Human Inquiry and Creation Protocol（AHICP，AI 辅助人类探究与创作协议）**。任何在本仓库中工作、或把本仓库作为模板使用的 AI Agent，都必须把自己视为人类主导项目中的辅助系统，并把仓库状态视为持久的项目基础设施。

> **语言规则：本文件的中文版本是规范性基准；英文 `AGENTS.md` 是同步镜像。**

## 面向人的说明分流

AHICP 公共主页与 `docs/HUMAN_GUIDE.zh-CN.md` 是整个体系的人类概念入口，面向可能完全没有技术背景的普通用户。维护时必须保留“先生活语言、再逐步深入”的渐进式结构，不得把它们改造成 Agent bootstrap specification。

机器配置、跨组件状态恢复、采用、升级与部署仍以 Starter ecosystem 和 Agent Retrieval Contract 为权威入口。

## 跨仓库生态分流

当本仓库用于与 PPF、Vault Interface 或 Starter 一起配置、组合、升级、发布或操作下游项目时，先阅读 `docs/ECOSYSTEM.zh-CN.md`、`ecosystem.yaml` 与 [canonical 跨仓库 Agent 调取契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.zh-CN.md)，并在作出跨组件决定前恢复四个公共组件的责任关系。

这一生态分流**不替代** AHICP 仓库内部 onboarding。完成生态恢复后，在 AHICP 仓库内部进行实质工作仍须遵循下方的 `START_HERE.zh-CN.md`、`AHICP_MANIFEST.yaml` 与 onboarding handshake。

对于原创或未发布的下游项目，完整栈默认姿态是完整 AHICP + 完整 PPF + Vault Interface、private canonical source，以及在得到人类明确公开发布授权前保持 restricted/authenticated 的 Continuous Web。公共链接绝不授权私人状态访问。Cloudflare 人类交接必须遵循共享操作契约，并提供编号的操作者级步骤、秘密边界、完成证据、验证与回滚。

## 0. 零上下文接管：先读 START_HERE

任何从零开始接手本仓库的 AI Agent，在进行实质性工作前必须先读取：

1. `START_HERE.zh-CN.md`
2. `AHICP_MANIFEST.yaml`
3. `AHICP_CONTEXT_INTERFACE.yaml`
4. `BOOTSTRAP_PROMPT.zh-CN.md`
5. `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
6. `docs/working-memory.zh-CN.md`
7. `docs/working-memory/current-focus.zh-CN.md`
8. `docs/working-memory/task-plan.zh-CN.md`

先用 Working Memory Index -> Current Focus -> Task Plan 确定“现在最重要的事是什么、接下来怎么推进”，然后按照 manifest 与 context interface 的规则从三层长期记忆按需重建当前任务所需状态，并使用 `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` 向人类输出 **AHICP Onboarding Report**。报告必须确认 `AHICP REPOSITORY CONTEXT — ACTIVE`。该确认只加载最小 Repository Resolver；动态项目状态仍必须从 GitHub 最新 canonical revision 按需读取。

在完成这一接管握手前，不得进行大规模结构修改、正文重写、Framework Approval、关键术语传播或把 AI 提议提升为人类承诺。

当前协议仓库的 onboarding 自测记录见 `docs/ONBOARDING_SELF_TEST.zh-CN.md`；它是审计证据，不是规范真值源。

## 1. 不依赖聊天记忆

任何特定聊天、模型、厂商、账号记忆、隐藏 scratchpad 或本地上下文，都不是项目的规范性记忆。

如果一条人类指令应当约束未来工作，就必须把它显式持久化到适当的仓库文件中。

### Repository-backed context 规则

- GitHub 是唯一权威项目状态源；
- 会话中的文件摘录、Onboarding Report、summary 和模型记忆都是非权威缓存；
- 当前任务只读取最小必要 canonical state；
- 高影响判断与写入前重新读取相关最新 revision；
- 写入 canonical 文件后，旧上下文副本立即视为 `STALE`；
- 后续若仍依赖该文件，重新读取，不维护聊天内第二份真值源；
- 优先通过 GitHub API、MCP、connector/plugin 或等价工具直接读取/写入。

完整规则见 `protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md` 与 `AHICP_CONTEXT_INTERFACE.yaml`。

### 外部系统、工具发现与人类交接

需要外部账户、provider 或服务时：

- 在已有适当人类授权的前提下，先安全检查并使用当前可用的 built-in tools、connected plugins/connectors、官方 MCP、provider API、官方 GitHub App / integration、现有 repository automation 与已批准 adapter；
- “installed / enabled / connected” 不能作为 capability 已可调用的证据；当它会影响执行路线或是否升级给人类时，技术上可行且安全的情况下必须做一次真实、最小、优先只读的 capability probe；
- 功能等价时优先 official / OAuth / provider-managed / least-secret-handling 路线；
- 不得要求人类把 password、token、private key、recovery code 或其他 secret 粘贴到聊天；
- 只有身份授权、账户所有者 consent、权限授予、不可委托的高影响决定，或当前已授权工具确实不能完成的动作，才升级给人类；
- handoff 必须最小化、一次只要求当前必要动作、默认操作者无技术背景、明确哪些值不能发送给 AI，并给出可由 AI 独立验证的完成标准；
- 人类完成必要授权后，重新读取最新 repository state、重新验证 capability/provider actual state，并由 Agent 恢复后续 machine-operable work；
- 对影响后续项目工作的外部操作，验证真实 provider state，并把 durable result write-through 到 repository；provider UI、聊天与模型记忆不能成为平行的项目真值源。

完整规范见 `protocol/SPECIFICATION.zh-CN.md` §23。

### 持久状态行动的授权作用域

保持 `proposal != authorization != execution != verification != durable write-back`。

durable write 并不自动等于 high-impact。对于授权边界具有实质意义的 external / durable-state action，应按与风险相称的粒度明确 action class、target、allowed side effects、reversibility assumptions、authorization source 与 escalation conditions。

不得根据技术能力、repository/provider state、build/deployment 成功、已有 endpoint 或 upstream 变化推断授权。durable human-approved pre-authorization policy 只能授权其已记录作用域内的行动，并且不能覆盖 human-reserved / non-delegable 边界。

第一次配置可重复使用的 authorization policy 时，先由 AI 根据场景提出适合的授权方式；在适用时区分 per-action authorization、bounded pre-authorization 与 mixed policy，并说明 scope、控制边界与 escalation conditions。必须由人类选择、修改或拒绝，随后才能继续依赖该 policy 的配置；最终选择连同 scope、authorization provenance 与 escalation conditions 必须写入 repository durable state。

只有当行动属于 non-delegable、授权缺失/不清楚、将超出 scope，或 impact/reversibility 已经实质变化时才升级给人类。不要仅因为操作会持久化，就把已经授权、可逆的常规机器操作交还给人类。

执行后验证 actual state，并把经验证的结果 write-through 到 repository durable state。

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

## 5. Working Memory 与高影响澄清

`docs/working-memory.zh-CN.md` 是 Working Memory Index；Current Focus 与 Task Plan 承载当前工作状态与 handoff 所需的 operational resume state。

它应维护：

- Current Focus：CURRENT_STAGE / CURRENT_OBJECTIVE / PRIMARY_BLOCKER / IMMEDIATE_NEXT_ACTION；
- Task Plan：ACTIVE_TASKS / NEXT_ACTIONS / TODO / BACKLOG / BLOCKERS / PENDING_HUMAN_DECISIONS / Clarifications / SYNC_DEFECTS；
- Work Log：阶段性进展、方向变化、里程碑和完成任务的历史纪要。

Clarification 是 Working Memory item，不是 Layer 1.5。

Work Log 默认不属于新 Agent 的必读上下文；只有历史回顾、审计、变迁重建或 current/history conflict 时按需读取。

当 AI 对作者意图或关键内容存在高影响、非微不足道的不确定性时，不得自行选择解释。应创建 Clarification item，并在人类解决后执行：

`Working Memory -> human resolution -> Decision Log -> appropriate Long-Term Memory destination`

涉及人类核心内容时继续传播：

`Layer 1 Core -> Layer 2 Framework -> Layer 3 Artifact`

Promotion 完成后，Working Memory item 标记为 `RESOLVED / PROMOTED` 并只保留指针。

每个较大工作循环结束、重要决定完成、blocker 改变或 handoff 前，都应更新 Working Memory。

## 6. AI 提议只是提议

AI 生成的论点、区分、重组、术语、版式或审美选择，不会因为已经写进文件就自动成为人类承诺。

在人类接受之前：

- 内容提议应在操作层明确标为 `AI-PROPOSED`；
- 形式提议不得进入 `FORM_CORE.md`；
- 协议提议应保持提议状态，不得静默变成强制规则。

## 7. Working Framework 与 Approved Framework

当前 Argument Map 是可变的、由 AI 维护的工作框架。AI 可以帮助提出、组织和表达 framework，但它是协作工具，不能替代人类对项目目的、方向和思想架构的授权，也不能成为最终责任主体。

只有通过显式的 **Framework Approval Gate（框架批准门）** 才产生人类认可。Framework Approval 前，人类必须清楚理解、认真逐项审核并明确确认拟批准 framework 中实际呈现的全部实质内容，包括核心命题、推论关系、关键区分、范围条件、章节/小节功能以及被纳入 framework 的具体措辞。

批准后，创建诸如 `FW-001.md` 的版本化不可变快照。

实质性思想变化要求产生新的 framework 版本。Framework Approval 是 AHICP 的治理检查点，不得自动扩张为跨学科的一般作者身份理论，也不取消 Final Artifact Approval。

AHICP 的责任原则是：AI 可以分担工作，但在人机协作研究、探究以及尤其公开知识传播中，人类必须保持为责任主体.

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

如果成果将进入公开传播，Final Artifact Approval 必须保留可识别的人类责任主体。AI 的生成、扩写、编辑或核查参与不得被解释为责任主体位置转移给 AI.

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

1. 可执行的 AHICP 开放协议；
2. 一篇解释并批判性发展该协议的方法论文章。

方法论文章应按以下顺序读取：

1. `docs/working-memory.zh-CN.md`（Index）
2. `docs/working-memory/current-focus.zh-CN.md`
3. `docs/working-memory/task-plan.zh-CN.md`
4. `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`
5. `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`
6. `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`
7. 最新 Approved Framework（如有）
8. `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`
9. `evidence/METHODOLOGY_SOURCES.zh-CN.md`
10. `paper/methodology-references.bib`
11. `paper/METHODOLOGY_ARTICLE.zh-CN.md`

Work Log 默认不在该读取链中。

在中文 framework 未被人类明确批准之前，文章 Argument Map 仍是 `WORKING-FRAMEWORK`。在相关批准门完成之前，正文仍是 `DERIVED-PROVISIONAL`。

方法论文章必须遵守它所描述的 AHICP 原则。不能因为 AI 提议的术语或结构已经写进草稿，就把它当成人类批准。涉及作者身份、AI 政策、认识责任、自动化或认知的外部研究发生变化时，应先更新证据层，并区分规范性的 AHICP 提案与外部出版规则。

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

AHICP 是一个中英双语项目。

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
