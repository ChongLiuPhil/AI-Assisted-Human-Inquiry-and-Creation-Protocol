# AHICP 协议核心（Protocol Core）

> **本中文文件是规范性基准；英文 `PROTOCOL_CORE.md` 是同步镜像。**

## 目的

本文件记录定义 AI-Assisted Human Inquiry and Creation Protocol（AHICP）项目本身的、当前有效的人类原创设计承诺。

它是 AHICP “想要实现什么”的语义真值源。AI 可以扩展这些思想，但不得静默替换它们。

---

## P1. 以 GitHub 为中心的持久项目状态与 AI 辅助

协议应支持人在 GitHub 等持久仓库基础上开展长期探究与创作，并由一个或多个可替换 AI Agent 提供辅助。

重要项目状态应显式存入仓库文档，而不是依赖某一个 AI 平台或 Agent 的记忆或对话上下文。

初始协议以 GitHub 为目标平台；以后可以考虑其他平台。

## P2. 人类原创的实质性思想必须独立保存

讨论过程中，人类作者会表达、纠正、接受、拒绝、限定并发展实质性思想。

关于项目实质内容的人类持久决定应被抽取并写入基础内容文档。

AI 扩写不得静默违背或替代这层人类基础。

## P3. 形式/呈现意图必须与实质内容分离

人类关于字体、版式、视觉设计、引用呈现、写作格式、成果类型以及其他表现形式的指令，与实质性内容决定不同。

因此这些内容应存入独立的形式/呈现真值源。

在适当情况下，作者的跨项目偏好可以由未来项目继承。

## P4. 第二层应保存持久但高可修改性的当前操作框架

第二层属于长期项目记忆，但比第一层更可修改。它应以压缩、可检查的方式表示论文、书籍、创作或其他成果的当前实际结构。

这一层应包含核心命题、关键概念、推论关系、章节/小节功能、概念区分与当前结构状态。

第二层必须以第一层的人类作者核心基础为上游约束，但可以包含第一层没有逐项表达、而为项目展开所必需的结构化内容。

对于大型项目，它应成为人类与 AI 讨论结构问题的主要界面。Working Framework / Argument Map 与 Approved Framework snapshots 可以作为这一长期层的不同批准状态或项目类型实例。

## P5. 人类反馈必须先向上游传播

当人类作者作出实质性纠正或决定时，AI Agent 应先把人类决定持久化到相应基础文档，再更新操作性表示，最后才把变化传播到最终扩写成果。

## P6. 操作性框架可以成为经人类确认的责任锚点

AI 维护的 Working Framework 不自动等于人类认可。

当某一版本已经由人类作者明确阅读并确认后，应保存为版本化的 Approved Framework。

对于长篇作品，Approved Framework 是人类核心思想责任的主要结构性锚点。人类作者在批准前必须清楚理解、逐项审核并确认该 framework 中实际呈现的全部实质内容，包括中心主张、推论关系、关键区分、范围条件、章节/小节角色，以及被纳入 framework 的具体措辞。Framework 可以由 AI 辅助整理和表达，但获批版本必须真实体现人类作者理解并认同的思想结构。

## P7. 已批准框架应投影到最终成果的总览

经人类批准的核心思想结构应忠实投影到最终成果面向读者的总览中。

典型映射包括：

- 学术论文：摘要与引言；
- 普通文章：开篇/导论性概览；
- 书籍：导论/总览章节与章节路线图。

## P8. AI 可以大量扩写，但必须保持框架忠实性

Framework Approval 后，AI Agent 可以进行大量展开、起草、解释、文献整合与格式处理。

这种扩写仍是经人类治理结构的派生表达，不得静默引入重大偏离。

## P9. 项目记忆应可跨 Agent 恢复

新的 AI Agent 应能仅通过读取仓库状态接管项目，而无需完整原始对话历史。

仓库可以积累长期历史记忆，同时当前规范性摘要应保持足够紧凑，便于实际接管。

## P10. 对上下文窗口的独立来自外部化状态，而不是无限上下文

协议应通过把持久项目状态存入 GitHub 来减少对单一对话窗口的依赖。

它不应假设 AI 能一次性加载无限历史。大型项目应使用紧凑的当前状态、日志、归档、索引与选择性检索。

## P11. 协议应可复用、可迁移

AHICP 应作为一个独立开放项目存在，而不是依赖某一个研究主题，并应为新的探究、研究、论文、书籍、文章、报告、创作及其他长期项目提供可复用的规范和模板。

未来 AI Agent 应能检查本仓库，并针对新主题建立适合的项目结构，同时保持相同的协作逻辑。

## P12. 协议应明确人类主体性与 AI 辅助边界

系统至少应区分：

- 人类思想意图；
- 人类呈现意图；
- AI 操作性表示；
- AI 辅助的派生表达；
- 证据约束；
- 批准状态；
- 历史决定。

目的不是隐藏 AI 协助，而是让 AI 辅助可审计，并保持人的目的、判断、批准与责任位置清晰。

## P13. 应区分框架层责任与扩写层缺陷

在长篇协作中，经人类批准的 framework 是主要的实质性思想责任锚点。Framework Approval 表示人类已经对该 framework 中实际呈现的全部实质内容完成理解、审核与确认。

如果一个核心命题、推论关系、中心区分、范围条件、章节角色或被纳入 framework 的具体表述本身已经存在于被明确批准的 framework 中，那么它属于人类确认思想架构中的 framework-level content；其中的结构性缺陷因此也是 framework-level defect。

如果问题只在后续 AI 扩写中产生，例如措辞较弱、过渡较差、例子不必要或其他局部实现问题，则应当能够与 framework 本身的缺陷区分开。

这种区分不取消出版/投稿前可能适用的 Final Artifact Approval 与公开问责、事实准确性和研究诚信要求。

## P14. 形式偏好应支持作者级、成果类型级和项目级继承

形式系统应当可复用，而不是每个项目从零建立。

应能够区分并组合：

- 可复用的作者级呈现偏好；
- 诸如 `BOOK`、`ACADEMIC_PAPER`、`ARTICLE` 的成果类型 profile；
- 项目特有的形式决定；
- 外部发布平台约束；
- AI/工具临时默认值。

新项目初始化时应确定成果类型，并只继承明确适用的偏好。未确定的形式决定必须保持未确定，不能由 AI 猜测填充。

## P15. 审计必须是修复循环，而不是被动检查

当项目执行多轮整合审计时，每一轮都应是完整循环：

`审查 -> 识别缺陷 -> 修复/实现 -> 验证修复`

因此，所谓“三遍审查”意味着连续三轮审查—修复，而不是三次阅读之后只进行一次修复。

完成这些循环后，还应执行一次额外、独立的修复后审计，以发现剩余遗漏、回归或不一致。

## P16. AHICP 应同时产出可执行开放项目与方法论文章

AHICP 具有两个互相支撑的产出：

1. 一套可执行、可复用的开放协作协议，包括规范、模板、状态和治理规则；
2. 一篇方法论文章，解释协议的概念根据，并发展其对 AI 时代研究实践的意义。

文章应讨论包括但不限于：人类作为研究与探究责任主体的地位、人类对研究目的与方向的授权、AI 工具可以执行或辅助的工作范围、framework 层的人类思想责任、公开知识传播中的责任承担、AI 辅助扩写、认识依赖、持久外部研究记忆，以及人类问责仍然有意义的条件。

文章是协议的学术派生成果，应自身在 AHICP 风格的 framework 控制下发展，而不能作为无治理的说明性文章.

## P17. AI 是协作工具；人类是项目目的、方向与责任主体

AHICP 将 AI Agent 作为研究协作工具，而不是作为需要被赋予人类式认知主体地位或最终责任主体地位的参与者。协议不应把“AI 承担认知劳动”或“AI 承担认知任务”作为规范性描述；更准确地说，AI 可以执行或辅助大量检索、综合、起草、重组、核查、格式处理和其他工作。

研究或创作项目的目的、核心问题与方向应由人类发起、给予并持续导航或批准。AI 能够执行大量工作，并不构成把项目目的、核心判断或责任主体位置转移给 AI 的理由。

因此，AHICP 所说的“人类责任”应精确理解为：**在人机协作的研究与探究中，人类仍然是责任主体／责任承担者。** 尤其当研究结果、论证或知识主张通过论文、书籍、报告、网站或其他形式进入公开知识传播时，最终责任主体必须保持为人类。

对于长篇成果，这一责任主体地位主要通过 Layer 2 Current / Approved Framework 落实：人类作者必须对其中实际呈现的核心命题、推论关系、关键区分、范围条件、章节/小节功能及具体表述形成清楚理解，并在 Framework Approval 时认真审核和明确确认。AI 可以帮助提出、组织或表达该 framework，但不能替代人类对方向与思想架构的授权，也不能成为其最终责任承担者。

Framework Approval 不取消 Final Artifact Approval；具体公开版本仍必须由人类责任主体按照适用的学术、机构、出版商、发布渠道与研究诚信要求完成最终审阅和批准.

## P18. 中文是规范语言；英文是同步镜像

AHICP 项目的所有实质性文档应提供中文与英文版本。

中文版本是**语义与编辑权威基准**。除非人类对某一具体成果明确另作决定，人类审阅、纠正、确认与实质性编辑都以中文版本为基准。

英文版本是**同步翻译镜像**。对中文规范版本的任何实质性修改，都必须在同一工作轮次中传播到英文对应文件。只要两种语言仍存在实质不同步，该修改就不能视为完成。

如果中英文冲突，以中文为准，并必须修复英文。

新的实质性 Markdown 文档从创建时起就应以双语配对形式存在。BibTeX、schema、源数据或代码等语言中立文件无需仅为语言而复制，但它们的人类可读说明应双语。

仓库必须让新的 AI Agent 能够发现这种语言优先级与同步规则。

对于 2026-09-18 规则建立前已经存在的双语文件，如果英文版本在历史上已经形成了中文版尚未吸收的较新实质内容，应先执行一次性的历史追赶：把这些英文发展吸收到中文，使中文达到切换时真正的最新语义状态，再把英文整理为中文镜像。只有完成这一步，才算完成 canonical cutover。

canonical cutover 完成之后，正常实质性发展方向固定为：`人类决定 -> 中文 canonical -> 英文 synchronized mirror`。英文不得再作为独立的实质性发展分支。


## P19. 高影响不确定性必须进入 Working Memory 的 Clarification 队列

AHICP 不再把 Critical Clarification 视为 Layer 1 与 Layer 2 之间的独立“1.5 层”。

Clarification 是 **Working Memory（工作记忆）** 中的一种记录类型。

当 AI Agent 对作者意图、核心命题、关键概念、范围、推论关系、章节功能、关键术语或母语/英文对应存在非微不足道且高影响的不确定性时，不得静默选择一种解释并向下游传播。

Agent 应把该不确定性写入 Working Memory 的 Clarification 区，说明候选解释、影响范围、严重度以及需要人类确认的问题。

未解决条目不属于人类长期承诺，可以标记为 `BLOCKING` 或 `NON-BLOCKING`。

人类确认或纠正后，结果必须执行 Promotion：

`Working Memory -> Decision Log -> appropriate Long-Term Memory destination`

如果涉及人类核心内容，则进入 Layer 1 Content Core，再传播到 Layer 2 Framework 与 Layer 3 Artifact；Form / Protocol 决定进入对应长期 Core；纯结构性 Framework 决定进入 Layer 2。

Promotion 完成后，Working Memory 中的条目退出 active 状态，仅保留 resolved/promoted 指针与审计信息。

AHICP 应在重大阶段转换、Framework Approval、关键术语全篇传播、正式翻译、大规模章节扩写及 Final Artifact Review 前主动执行 Working Memory / Clarification Scan。


## P20. 零上下文接管必须有显式启动入口与接管握手

AHICP 项目应提供一个**从零上下文即可发现的启动入口**，使新的 AI Agent 在没有旧聊天、平台记忆或项目先验知识的情况下，能够按确定顺序重建当前研究状态。

该入口至少应包括：

- 根目录人类/Agent 可读的 `START_HERE` 文件；
- 根目录 `AGENTS` 契约；
- 机器可读的 AHICP manifest 或等价索引；
- 明确的 mandatory read order；
- Working Memory Index；
- Current Focus；
- Task Plan；
- Framework Status、Working/Approved Framework 与 Artifact 状态入口；
- 可直接复制给任意 AI Agent 的 bootstrap prompt。

新的 AI Agent 在进行实质性修改前，应完成一次 **Onboarding Handshake（接管握手）**。报告至少应说明：

- 当前最高优先级目标；
- primary blocker 与 immediate next action；
- active tasks、TODO / backlog；
- pending human decisions / Clarifications；
- Framework / Artifact 状态；
- 同步缺陷；
- 当前允许与被阻塞的下一步。

Work Log 默认不属于零上下文接管的必读材料；只有人类要求历史回顾、专门审计、方向变化重建或 current/history conflict 时才按需读取。

如果 Agent 无法仅凭仓库完成这一报告，项目存在 onboarding/persistence defect，应先修复，而不是继续大规模研究或写作。

协议不能保证任意外部平台会自动读取某个特定文件；因此 AHICP 的目标是**最大化可发现性与可验证接管**：通过根目录显眼入口、通用 Agent 契约、机器 manifest、README 导航和可复制 prompt，使任何具有仓库读取能力且愿意遵循项目指令的 Agent 都能重建同一工作流。


## P21. 会话上下文只保留仓库访问内核，不维护第二份权威项目状态

AHICP 的持久状态保存在仓库中。新的 AI Agent 在接管后可以在当前对话上下文中保留一个极小的 **Repository Resolver / Active Session Kernel**，但该内核只负责说明：

- GitHub 是唯一权威项目状态源；
- manifest 与 context-interface 在哪里；
- 中文 canonical / 英文 mirror 的优先级；
- 当前任务属于 CONTENT / FORM / PROTOCOL 哪一路；
- 何时必须重新读取仓库；
- 写入后如何使旧缓存失效。

它**不应长期复制** Current Focus、Task Plan、Framework 状态、Artifact 状态、Core 内容或其他动态项目状态。

这些动态内容在需要时应从 GitHub 最新 canonical revision 按需读取。任何较早的 Onboarding Report、会话摘要、文件摘录或模型记忆都只是非权威缓存。

正确优先级为：

`Platform system/developer rules > AHICP repository access kernel > ordinary task-level AI defaults`

该机制不把仓库文件提升为平台真正的 system prompt，也不声称能够修改模型参数或平台 memory。



## P22. GitHub 应作为权威外部上下文与工作状态接口

AHICP 应支持一种 **Repository-Backed Context Interface（仓库支撑的上下文接口）**：

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

模型在某次推理中仍需临时获取相关信息，但不得维护与 GitHub 平行的长期权威副本。

每个实质性任务应按需：

`Resolve -> Fetch latest -> Reason -> Act -> Write-through -> Invalidate stale cache -> Refresh if needed`

对未来 Agent 有约束力的更新只写入 GitHub；会话内旧副本在仓库更新后立即视为 stale。

高影响判断与写入前必须重新确认相关 canonical 文件的最新 revision。Agent 应尽量通过 GitHub API、MCP、connector/plugin 或等价工具直接读取/写入，而不是要求人类把文件内容复制进聊天。

AHICP 应提供机器可读的 context-interface manifest，描述 task routing、revision policy、cache invalidation、write-through 和 trust boundary。


## P23. 三层长期记忆与并行 Working Memory 必须明确区分

AHICP 的核心项目状态采用三层长期记忆：

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

其中：

- Layer 1 保存人类作者持续表达、纠正、确认和净化后的核心基础；
- Layer 2 以 Layer 1 为基础，保存当前操作框架、核心命题/要素、关键概念和结构关系，持久但更可修改；
- Layer 3 主要由 Layer 2 展开为完整成果，并同时受 Layer 1 与证据约束。

与三层长期记忆并行，项目必须维护 **Working Memory**。

Working Memory 记录当前阶段、目标、工作计划、active tasks、completed work、next actions、TODO、blockers、pending human decisions、clarifications、sync defects 与 handoff note。

Working Memory 的功能是让任何新的人类参与者或 AI Agent 能迅速回答：

> “项目现在做到哪里，下一步从哪里继续？”

它不是第四个长期语义层，也不得成为长期主张的替代真值源。

Working Memory 中获得稳定确认的内容必须 Promotion 到相应长期记忆；Promotion 后 Working Memory 只保留状态、Decision ID 与目标文件指针。


## P24. Working Memory 是功能区而不是固定单文件

Working Memory 的规范对象是**一组功能角色**，而不是某一个固定文件。

项目可以根据工程规模、AI Agent 性能、上下文成本与工作流便利性，把 Working Memory 实现为一个文件或多个文件。无论物理布局如何，至少应提供三种逻辑功能：

1. **Current Focus / 当前焦点**
   - 保存最近期、最高优先级的工作目标；
   - 说明当前阶段、本轮/当前任务要解决什么、最关键 blocker 与立即 next action；
   - 应保持极短，是新 Agent 接管时最高优先级的工作状态。

2. **Task Plan / 任务计划**
   - 保存动态计划、TODO、active tasks、blocked/waiting-human items、backlog 与 next actions；
   - 任务完成后应退出 active list；
   - 新任务随协作发展动态加入；
   - 已完成事项应被压缩进入 Work Log；其中形成稳定规范结果的内容还必须 Promotion 到对应长期记忆。

3. **Work Log / 工作日志**
   - 保存供人类作者日后阅读的阶段性历史纪要；
   - 记录大体进展、重要工作转折、思想/工作路径的变化、完成的任务批次与阶段里程碑；
   - 主要服务于人类回顾，不是常规 AI onboarding 的必读上下文；
   - Agent SHOULD 定期更新它，但默认不应为了正常继续当前工作而读取完整日志；
   - 当人类要求历史回顾、需要追溯变迁、当前状态与历史明显冲突或进行专门审计时，Agent MAY 按需读取。

Work Log 不应保存模型隐藏 chain-of-thought、scratchpad 或不可验证的内部推理；它只记录可审计的项目级变化、已表达的理由、决定、里程碑和高层总结。

Working Memory 可以有一个稳定的 Index / Resolver 文件，把上述逻辑角色映射到当前物理文件。一个轻量项目可以把多个角色映射到同一文件；复杂项目可以分拆。

推荐续接顺序：

`Working Memory Index -> Current Focus -> Task Plan -> task-relevant Long-Term Memory`

Work Log 默认不进入该必读链。

---

## P25. 外部系统操作应采用授权边界内的 machine-operable-first escalation

当 AI Agent 需要访问外部系统、账户或服务时，在已经具备适当人类授权的前提下，应先安全发现并验证当前可用的内建工具、connector/plugin、官方 MCP、provider API、官方 integration、仓库 automation 与已批准 adapter，再决定是否需要 human handoff。

工具被列为 installed / enabled / connected 不足以证明它真实可调用；在技术上可行且安全时，应以真实最小调用验证 capability。

Agent 不得要求人类把 password、token、private key 或其他 secret 粘贴到聊天。只有身份授权、账户所有者 consent、权限授予、不可委托的高影响决定，或当前工具能力确实无法完成的动作，才应升级给人类；交接必须最小化、面向非技术操作者，并在完成必要授权后由 Agent 恢复机器可执行工作。

对影响后续工作的外部操作，Agent 应验证 provider actual state，并把经验证的 durable result 写回 repository。Provider UI、聊天状态与模型记忆都不得成为与 repository 平行的 authoritative project state。

---

## 当前范围

AHICP v0.3 当前聚焦：

`人类 + 持久仓库 + AI Agent(s)`

用于**人类主导、AI 辅助**的持续探究、研究、推理、写作与创作。

当前 reference implementation 以 GitHub 为权威外部项目状态源；更广泛的平台支持可以后续映射相同逻辑角色。

AHICP 不定义出版基础设施。作品的 source / build / publish / release / archive 生命周期属于独立的 **Personal Publishing Framework（PPF）** 或其他兼容出版框架。