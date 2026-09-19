# 从对话到持久研究状态：AI时代的人机研究协作、人类责任与可审计作者性

**英文题目：** *From Conversation to Persistent Research State: Human–AI Research Collaboration, Human Responsibility, and Auditable Authorship in the AI Era*

**题目状态：** `HUMAN-APPROVED TITLE — HARC-D024`（英文为同步翻译镜像；题目获批不等于 Framework Approval）  
**状态：** `DERIVED-PROVISIONAL`  
**框架状态：** `WORKING-FRAMEWORK — 尚未经人类作者正式确认`  
**协议：** AI-Assisted Human Inquiry and Creation Protocol (AHICP) v0.2.0-draft  
**上游内容核心：** `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`  
**形式核心：** `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`  
**框架状态：** `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`  
**证据核验：** `evidence/METHODOLOGY_SOURCES.zh-CN.md`

## 摘要

生成式人工智能正在显著改变研究工作的分工结构。文献检索、观点整理、论证重构、草稿生成、语言编辑、格式转换乃至部分形式化工作，都可以由 AI Agent 作为工具以远高于传统人工流程的速度执行或辅助完成。然而，研究者的阅读速度、理解能力、判断能力与责任承担能力并不会按同样比例增长。由此出现一个比“AI 是否可以写论文”更基础的方法论问题：当越来越多具体研究工作可以由 AI 工具辅助甚至自动执行时，谁仍然必须理解、确认和判断这些工作的目标与结论，并成为最终的责任承担主体？

本文提出 AI-Assisted Human Inquiry and Creation Protocol（AHICP）作为一种以 GitHub 为当前主要实现平台的持久、显性、可审计的人机研究协作架构。AHICP 不把聊天窗口或某个模型的私有上下文视为研究项目的长期记忆，而把经过版本控制的仓库文本视为持续发展的研究状态。协议把项目的长期研究记忆分为三层：Layer 1 的人类作者核心基础、Layer 2 的当前论述框架、Layer 3 的派生成果；同时维护一个与三层并行的 Working Memory，用来记录当前阶段、目标、任务、阻塞、待确认事项、clarification、TODO 与 handoff。Content Core、Decision Log、Working Argument Map、Approved Framework Snapshot 与 Working Memory 等文件共同形成可追踪的研究状态治理。

本文进一步提出：研究或创作项目的目的、核心问题与方向必须由人类给予、发起并持续导航或批准；AI Agent 在 AHICP 中是协作工具，可以执行或辅助大量工作，但不被作为认知主体或最终责任承担主体来描述。本文标题中的“人类责任”是一种简写；更精确的命题是：**在人机协作的研究与探究中，尤其当研究结果、论证或知识主张进入公开传播时，人类必须保持为责任主体。** 对于长篇成果，这一责任主体地位主要通过 Layer 2 Framework 落实：Framework 可以由 AI 辅助提出、组织和表达，但人类作者在 Framework Approval 前必须清楚理解、认真审核并明确确认其中实际呈现的全部实质内容。本文据此区分 framework-level defect 与 derived-expansion defect、Framework Approval 与 Final Artifact Approval，并讨论这种架构与扩展心灵、分布式认知、认识依赖、自动化依赖以及现有学术作者规范之间的关系。

**关键词：** 人机协作；生成式人工智能；研究方法论；责任主体；作者身份；分布式认知；版本控制；GitHub；AI Agent；学术诚信

---

## 一、问题不再只是“AI能不能写”，而是“研究状态由谁治理”

关于生成式 AI 与研究写作的讨论，经常围绕一个表层问题展开：AI 能否写出一篇合格的论文、报告或书稿？这个问题当然重要，但它并没有触及长期人机协作最困难的部分。

真正的结构性变化在于：**生成能力开始远快于人类审查能力。** 一个 AI Agent 可以在很短时间内产生多个论证版本、几十页扩写、文献摘要、替代表述和结构重组；但人类仍然需要时间去阅读、理解、比较、判断和承担后果。本文将这种差异暂称为“生成—验证不对称”（generation–verification asymmetry）。

如果研究协作仍然采用传统的“对话—生成全文—人类逐字检查”模式，那么随着项目规模增加，人类最终会面对两个不理想的选择：要么把大量时间重新投入逐字核查，使 AI 的效率优势大幅下降；要么减少核查，从而使作者逐渐无法清楚说明作品中的哪些命题是自己真正理解和确认过的。

因此，问题不只是文本生产效率，而是**认知治理**：一个持续几个月甚至数年的研究项目，如何保存它的思想状态？人类与 AI 的贡献边界怎样显性化？什么修改构成作者立场改变，什么只是 AI 的暂时解释？一个新的 Agent 接手时，怎样知道哪些内容已经得到人类确认，哪些只是旧 Agent 的建议？

AHICP 正是试图回答这些问题。

---

## 二、聊天窗口为什么不是合格的长期研究记忆

### 1. 上下文具有暂时性

AI 对话非常适合即时推理，却不是稳定的研究基础设施。不同模型具有不同上下文长度，平台记忆机制可能变化，账户级记忆不一定透明，也很难作为正式的研究审计记录。更重要的是，研究项目的寿命可能长于任何一次对话。

因此，AHICP 的基本原则是：

> **聊天是交互界面，仓库是持久研究状态。**

这里的“仓库”目前主要指 GitHub。选择 GitHub 并不是因为 GitHub 本身具有特殊的哲学地位，而是因为它提供了几个适合长期研究协作的性质：显式文件、版本历史、差异比较、分支、提交记录、跨设备访问，以及相对成熟的自动化与 Agent 接口。

### 2. 文本版本控制不足以解决语义漂移

Git 可以告诉我们某一段文字何时变化，却不能自动回答更重要的问题：

- 这是人类作者改变了立场吗？
- 还是 AI 为了让语言更流畅而改变了表达？
- 这是一个已被接受的新命题吗？
- 还是一个等待作者裁决的 AI 提案？
- 这是证据迫使我们做出的修正吗？
- 还是排版工具的临时默认值？

当这些状态不被区分时，会出现**语义漂移**：AI 生成的更成熟、更顺畅的版本逐渐取代人类最初真正想表达的内容，最后双方甚至难以追溯这种替换何时发生。

AHICP 因而需要的不只是 textual version control，而是一种**semantic version control（语义版本控制）**。

---

## 三、从“仓库”到“外显化研究状态”

把 GitHub 视为研究记忆，与“扩展心灵”和“分布式认知”的思想存在明显亲缘性，但 AHICP 并不需要承诺某一种强形而上学立场。

Clark 与 Chalmers 在“The Extended Mind”中提出，某些稳定、可靠、易于调用的外部资源可以在认知过程中承担与内部记忆类似的功能（Clark & Chalmers, 1998）。Hutchins 对航海团队的研究则强调，复杂认知活动可以分布在人、工具、表征和社会组织之间，而不应只从孤立个体内部理解（Hutchins, 1995）。

AHICP 可以借用这种思想来理解长期研究协作：论文或书籍的“当前认知状态”不必全部保存在作者大脑里，也不必全部保存在 AI 上下文里。它可以被外显化为一组结构明确、相互约束的文件。

但本文采取较弱的主张：**仓库至少是一种认知脚手架和外部研究状态载体。** 它是否进一步构成某种“集体认知主体”的一部分，并不是 AHICP 成立所必需的。

AHICP 的目标是可操作的：让项目的重要状态可以被读取、恢复、比较和审计。

---

## 四、AHICP 的核心架构：把“作者意图、AI表征和最终文本”分开

AHICP 将传统写作流程中常被混在一起的东西拆开。

### 1. Content Core：人类究竟要主张什么

Content Core 保存当前有效的人类内容意图：研究问题、核心命题、关键区分、范围限制、明确的保留意见以及尚未解决的问题。

这一层的意义在于建立**语义权威的上游**。AI 可以提出新观点，但新观点在被人类接受以前不能因为“写得很好”就自动变成作者立场。

### 2. Form Core：作品应该怎样呈现

形式偏好与研究内容是不同问题。字体、字号、章节风格、脚注、引文格式、页面布局、图表风格、书籍或论文的整体视觉规范，应由独立的 Form Core 管理。

这种分离可以避免另一种漂移：AI 为了暂时把 LaTeX 编译出来而选择某个字号，后来新 Agent 却把它误认为作者长期偏好。

AHICP 进一步允许形式偏好分层继承：作者跨项目偏好、作品类型模板、当前项目决定、外部期刊或出版社约束，以及 AI 的临时默认值应当能够彼此区分。

### 3. Decision Log：当前状态与历史状态分离

Content Core 和 Form Core 应保持简洁，因为新 Agent 需要快速理解“现在以什么为准”。但简洁不能以删除历史为代价。

Decision Log 因而保存决策轨迹：何时改变某个主张、何时接受或拒绝 AI 提案、何时修改形式要求、何时升级协作规范。

可以说：Core 表示当前有效状态，Log 表示我们如何走到这里。

### 4. Working Memory：把当前工作状态与高影响不确定性放在并行操作层

AHICP 不再把 Critical Clarification 理解为 Content/Form Core 与 Working Argument Map 之间的 “Layer 1.5”。

更准确的架构是：三个主要内容层都属于长期研究记忆。

第一层是 **Human Authorial Core**。它保存人类作者主动表达、纠正、确认和持续净化后的核心观点与长期承诺，是最稳定的语义基础。

第二层是 **Current Framework**。它保存当前论述结构、核心命题、关键概念、推论关系与章节功能。它以第一层为基础，但可以包含第一层没有逐项表达的结构化内容。它比第一层更可修改，却仍属于长期项目记忆。

第三层是 **Derived Artifact**。论文、书稿或报告主要由第二层展开生成，同时必须与第一层及证据约束保持兼容。

与这三个长期层并行，AHICP 维护 **Working Memory（工作记忆区）**。Working Memory 回答的不是“项目最终主张什么”，而是“项目现在做到哪里、下一步从哪里继续”。它记录当前阶段、工作目标、总体计划、active tasks、最近完成、next actions、TODO、blockers、pending human decisions、clarifications、同步缺陷与 handoff note。

高影响不确定性现在只是 Working Memory 中的一种 Clarification item。当 AI 对核心命题、关键概念、范围、推论关系、章节功能或关键术语存在多个合理解释时，不应自行选择，而应把问题放入 Working Memory 等待人类确认。

人类确认后，结果执行 Promotion：

`Working Memory -> Decision Log -> appropriate Long-Term Memory destination`

如果涉及人类核心内容，继续传播为：

`Layer 1 Core -> Layer 2 Framework -> Layer 3 Artifact`

因此，Working Memory 的功能不是成为第四个内容层，而是提供一个可续接的操作界面。进一步说，Working Memory 也不必固定为一个单体文档。AHICP 可以把它拆成三个逻辑角色：**Current Focus** 保存当前最近期最高优先级目标，**Task Plan** 保存动态任务、TODO、blockers、pending human decisions 与 clarifications，**Work Log** 则保存主要供人类作者日后回顾的阶段性历史纪要。

这种拆分对应两种不同需求。Current Focus + Task Plan 服务于“被中断后如何无缝继续工作”；Work Log 服务于“以后如何回顾项目和思想路径是怎样变化的”。因此新 Agent 默认只读取 Current Focus 与 Task Plan，而不需要为了继续当前工作加载整个 Work Log。完成任务退出 active Task Plan，并以高层摘要进入 Work Log；真正形成稳定规范内容的结果仍然 Promotion 到三层长期记忆。

Work Log 记录可审计的阶段进展、已表达的高层理由与方向变化，而不是 AI 的隐藏 chain-of-thought 或 scratchpad。这样，人类可以长期保留一条可阅读的研究历程，而 AI 的运行时上下文仍保持紧凑。

被解决的 Clarification 退出 active 状态；权威答案沉淀到长期记忆中，Working Memory 只保留必要的状态和指针。

### 5. Working Argument Map：真正适合人机讨论的中间层

完整论文或书籍可能太长，不适合作为每次结构讨论的直接对象。因此 AHICP 维护一个 AI 主导更新、但受 Content Core 约束的 Working Argument Map。

它应该比正文短得多，却要明确显示：

- 中心问题与命题；
- 主要概念；
- 支持与限制关系；
- 各节或各章承担的论证功能；
- 关键反对意见；
- 证据依赖；
- 等待人类裁决的问题；
- AI 尚未被接受的建议。

这个文件不是作者自动认可的内容。它首先是一种**操作性表征**。

---

## 五、从 Working Framework 到 Approved Framework：语义确认门

AHICP 的一个核心机制是区分：

1. **Working Framework**：AI 可以不断修改的工作结构；
2. **Approved Framework Snapshot**：人类实际阅读并明确确认过的结构版本。

一旦一个框架版本得到确认，它应当冻结为 `FW-001` 之类的版本化快照。此后如果中心论证发生实质变化，应产生 `FW-002`，而不是无痕覆盖旧框架。

这种机制的价值在于回答一个在长篇 AI 协作中非常重要的问题：

> 人类作者究竟确认过什么？

对于一本篇幅很大的书，人类可能没有能力在每次 AI 修改后重新逐字阅读全书，但仍有可能高强度审查一个压缩后的论证架构。这个框架应至少包括中心命题、主要推论关系、关键区分、章节角色、范围限制和明确保留的未决问题。

由此，AHICP 把框架确认视为**主要的实质性思想检查点**。

---

## 六、AI时代的人类作为责任主体：AI 可以承担工作，责任主体不能转移

首先需要明确 AHICP 对 AI 角色的描述方式：AI Agent 是研究协作工具，而不是本文需要赋予认知主体地位或最终责任主体地位的行动者。因此，本文不使用“AI 承担认知劳动”或“AI 承担认知任务”作为中心概念。更准确地说，AI 工具可以执行或辅助大量具体工作，例如：

- 搜索与初步筛选文献；
- 总结争论；
- 生成结构候选方案；
- 发现可能的反例；
- 草拟段落；
- 形式化某个论证；
- 检查内部不一致；
- 转换格式；
- 建立引文与参考文献；
- 比较不同版本。

但是，AI 能够执行这些工作，并不意味着研究或创作项目的目的、核心问题、方向与最终责任主体位置也随之转移给 AI。项目究竟要探究什么、为什么沿某一方向推进，以及哪些核心主张最终得到接受，必须由人类作者实际理解、导航和批准。

因此，“人类责任”在本文中不是一个无需解释的抽象属性。更准确的表达是：**人类是责任主体。** 这一点在研究和探究活动中都重要，而当论文、书籍、报告或其他成果把知识主张带入公开传播时尤其重要。AI 可以参与大量工作，但公开知识主张不能因此失去可识别的人类责任承担者。

对于长篇成果，AHICP 把这种责任主体地位主要落实到 Layer 2 Framework。Framework 可以由 AI 辅助提出、整理和表达，但它不能只是一个人类笼统点头的概要。Framework Approval 要求人类对其中实际呈现的全部实质内容形成清晰、完整的理解，并逐项审核和确认，包括核心命题、推论关系及其逻辑依赖、关键区分、范围条件、章节/小节功能，以及被纳入 framework 的具体措辞。

Hardwig 关于认识依赖的讨论可以帮助说明：研究实践本来就包含对外部资源、他人工作与中介信息的依赖（Hardwig, 1985）。但 AHICP 并不由此把 AI 当作一个与人类专家同构的认知主体，更不由此把最终责任主体位置转给 AI。这里更重要的问题是：当人类使用 AI 工具生成、整理或转换研究材料时，怎样让人类自己的理解、判断、授权与责任主体地位仍然保持可定位、可检查和可审计。

因此，AHICP 的责任模型不是“人类必须逐字亲自生产全文”，也不是“只要 AI 足够强，人类只需形式批准”。它要求人类明确承担项目目的与方向，并作为责任主体对 Approved Framework 中的实质内容负责；与此同时，具体公开版本仍必须经过 Final Artifact Approval，并满足事实准确性、研究诚信及目标发布渠道的要求。

---

## 七、框架缺陷与扩写缺陷不是同一种错误

如果 `FW-001` 明确包含一个错误的核心推论，例如结论并不能由其主要前提支持，那么这是**框架层缺陷**。因为这个错误位于人类明确确认过的思想架构中。

但如果框架本身没有这一错误，而 AI 在后续展开时加入了一个不恰当例子、错误过渡、重复段落或局部表达问题，这首先是**派生扩写缺陷**。

这种区分具有两层意义。

第一，它提高责任归因的精度。我们不应把 AI 局部生成错误倒推成人类已经确认过那个错误；同样也不能把一个已存在于 Approved Framework 的结构性错误归咎于“只是 AI 写得不好”。

第二，它帮助组织审查资源。框架层问题必须回到上游重新确认；扩写层问题则可以在下游修复，只要修复没有改变核心结构。

但是，这一区分不能被误解为“人类只需看框架，从此无需关心终稿”。以 ICMJE 和 Nature Portfolio 等有影响力的现行学术规范为例，最终发表仍与人类批准、判断和问责相联系。ICMJE 的现行作者标准明确包含“最终批准待发表版本”，并要求作者同意对工作各方面承担问责；Nature Portfolio 的当前 AI 政策则强调作者仍对原创性、准确性和完整性负责，相关判断不能简单委托给 AI。AHICP 因此区分两个确认门：Framework Approval 与 Final Artifact Approval。

---

## 八、两个确认门：思想架构与公开问责

### Gate A：Framework Approval

这里确认的是：

- 主要命题；
- 推论结构；
- 核心区分；
- 章节/小节的论证角色；
- 重要限制；
- 有意保留的开放问题。

这可以被理解为作品的**思想架构责任锚点**。

### Gate B：Final Artifact Approval

这里确认的是具体的发布版本。其审查程度必须服从实际学科、出版社、期刊、学校或机构的要求。

以 ICMJE 与 Nature Portfolio 当前规则为例，AI 工具不能替代人类作者所承担的批准、判断和问责角色。AHICP 不试图把这些具体规则普遍化为所有领域统一的 authorship law，也不试图绕开任何目标期刊、出版社或机构的要求。它所提供的是一种过程结构，使“人类最终负责”可以对应到明确的版本、确认节点和审计轨迹。

在 AHICP 中，框架确认负责建立真正被人理解和接受的思想基线，最终确认负责把具体公开版本与这个基线及外部规则重新连接起来。

---

## 九、Approved Framework 为什么必须投影到摘要、导论或总论

如果一个人类确认过的框架只存在于 GitHub 内部，而读者无法从文章本身看出这一框架，那么它就只是项目管理工具。

AHICP 要求更强的对应关系：Approved Framework 的核心结构应当被忠实地投影到读者可见的 overview 中。

对于学术论文，这通常意味着摘要和引言应当清楚说明主要问题、核心命题、主要论证动作和全文路线。对于书籍，则应在导论或总论以及章节路线图中体现。

这会形成一个很有用的漂移检测器：如果 `FW-001` 与最终导论已经明显不一致，那么至少有一项出了问题——框架过时、导论错误，或者正文已经在后续扩写中发生了实质性偏移。

---

## 十、可替换的 Agent 与不可丢失的研究状态

AHICP 的另一个设计原则可以概括为：

> **AI Agent 可以替换，研究状态不能随 Agent 一起丢失。**

这意味着一个项目不应该以“某个特定模型很了解我”为核心依赖。新的 Agent 应能通过读取仓库恢复：

- 当前人类内容立场；
- 当前形式偏好；
- 最近的重要决定；
- 哪个框架已经确认；
- 哪些 AI 建议仍未确认；
- 哪些证据冲突尚未解决；
- 当前全文是什么状态。

但仅仅“仓库里有这些文件”还不等于新的 Agent 会正确读取它们。不同 AI 平台对入口文件、自动上下文和仓库指令的发现机制并不完全一致。因此 AHICP 还需要一个**零上下文启动协议**：根目录 `START_HERE`、机器可读 manifest、明确的 mandatory read order，以及新 Agent 在实质工作前提交的 Onboarding Report。

这个握手把“Agent 是否真正理解项目”从一个隐含假设变成可观察检查。Agent 应先从 Working Memory 报告当前阶段、工作目标、active tasks、最近完成、next actions、blockers 与 pending human decisions，然后再按任务读取长期 Core、Framework 与 Artifact；如果这些内容无法从仓库恢复，就说明存在 persistence/onboarding defect，应先修复而不是继续大规模扩写。

更进一步，AHICP 不需要在聊天中再维护一份动态项目状态副本。更准确的机制是 **Repository-Backed Context Interface**：GitHub 同时承担权威外部记忆与工作状态库，而模型上下文只保存一个极小的 Repository Resolver，并按当前任务临时读取所需文件。

因此，Working Memory 与三层长期研究记忆的真实当前状态都保留在 GitHub。Working Memory 提供续接位置；Layer 1/2/3 提供长期思想与成果状态。Agent 在需要时从最新 canonical revision 获取相关内容；高影响判断或写入前重新确认 revision；更新直接写回仓库；写入后，之前进入模型上下文的旧摘录立即视为 stale。所谓 `AHICP CONTEXT REFRESH` 也不再意味着把整个项目重新复制进聊天，而是重新解析当前任务依赖并 fresh-fetch 相关文件。

这并不意味着模型能够“完全不使用上下文”。任何一次推理仍然需要相关信息临时进入模型可用上下文。AHICP 所改变的是权威位置和生命周期：**GitHub 是真值源，模型上下文只是当前任务对仓库状态的一次短期投影。**

这并不会创造“无限上下文”。随着项目变大，历史资料仍然可能远超任何一次模型上下文。因此 AHICP 让 Working Memory 保持短小而当前，让 Layer 1 Core 和 Layer 2 Framework 保持紧凑，并把详细日志、旧版本、证据和档案交给历史层与选择性检索。

这使项目从“依赖一个巨大对话”转变为“依赖可恢复的显性状态”。

---

## 十一、AHICP 与现有作者规范：从抽象责任到可操作责任

现有学术规范为 AHICP 提供了若干重要边界案例，而不是一套可以直接等同于 AHICP 的统一规则。

ICMJE 把作者身份与实质贡献、重要内容的起草或批判性审阅、最终批准和问责联系起来。Nature Portfolio 当前 AI 政策强调作者仍对原创性、准确性和完整性负责，并要求相关 AI 使用按适用规则透明披露。CRediT 则从另一个方向提供了启发：它通过 14 类贡献角色提高研究贡献透明度，但贡献角色分类与某一具体期刊或制度下的作者资格判断不是同一个问题。

这些例子说明，AI 时代至少需要同时处理两个不同问题：

1. 谁做了什么？
2. 谁理解、确认并对什么负责？

AHICP 更关注第二个问题的过程基础设施，同时也允许贡献记录与 AI 使用披露进入项目状态。

从这个角度看，AHICP 不是要重新定义某个期刊的 authorship policy，而是试图提供一种**作者责任的工程化实现**：让“我批准了”“我负责”“这是我的核心判断”能够对应到明确的版本、文件和审计轨迹。

---

## 十二、自动化依赖：为什么人类确认门不能沦为形式点击

框架确认本身并不能保证责任真实存在。一个人完全可以不认真阅读就点击“确认”。因此 AHICP 的最大风险之一，是把真正的认识判断变成新的形式主义。

这与经典自动化研究中所讨论的 over-reliance 有联系。Parasuraman 与 Riley（1997）把自动化误用（misuse）的一类风险描述为对自动化的过度依赖，并指出这可能与监控失败或决策偏差有关。

AHICP 因此不能仅靠文件存在来证明良好协作。未来的 conformance test 应当进一步研究：

- 人类是否能够用自己的语言解释 Approved Framework；
- 人类是否理解关键前提与限制；
- Agent 是否主动暴露不确定性与证据冲突；
- 框架是否足够压缩但没有把决定性问题隐藏掉；
- 最终文本是否仍然忠实于人类确认的结构。

换言之，AHICP 解决的是“如何建立可检查的责任结构”，而不是自动保证每一个使用者都进行了高质量判断。

---

## 十三、作为开源协议，AHICP 应当可被经验检验

如果 AHICP 只是一篇关于“应该怎样与 AI 合作”的文章，那么它仍然停留在规范建议层面。把它做成开源项目的价值在于，它可以被测试。

至少可以设计以下几类实验：

### 1. Agent handoff test

不给新 Agent 原始聊天，只给仓库，看它能否准确重建当前项目状态。

### 2. Semantic drift test

让多个 Agent 连续改写同一研究项目，比较有无 AHICP 时人类核心命题的漂移程度。

### 3. Framework fidelity test

比较 Approved Framework 与最终摘要、导论和正文的结构一致性。

### 4. Review-effort test

测量采用框架确认机制后，人类审查时间是否能够从低杠杆的逐字检查转移到高杠杆结构判断，同时不显著增加严重错误。

### 5. Cross-model portability test

让不同厂商、不同能力层级的 Agent 接管同一项目，观察仓库结构是否真正降低平台依赖。

因此，AHICP 本身既可以是规范项目，也可以成为一个关于 AI 辅助研究方法的持续实验平台。

---

## 十四、限制与反对意见

AHICP 至少面临以下限制。

第一，**框架压缩可能隐藏细节风险**。一个看起来正确的高层结构，不保证每一个实证引文、数学推导和事实陈述都正确。因此证据验证层不能被框架确认取代。

第二，**人类判断能力本身有限**。如果作者无法理解所研究领域，即使有结构化框架，也可能只是形式确认。AHICP 不能把缺乏专业能力转化为真正认识责任。

第三，**维护仓库有额外成本**。对于很短的项目，完整 AHICP 可能过重，因此协议需要 lightweight profile。

第四，**保密和数据治理问题不能由 GitHub 结构本身解决**。敏感数据、未公开同行评审材料和受约束文件仍需服从相应制度和平台政策。

第五，**不同领域的作者规范不同**。AHICP 必须被看作基础协作架构，而不是超越期刊、出版社、学校或法律要求的统一授权机制。

第六，**AI 能力持续变化**。协议需要保持逻辑层稳定，同时允许实现层随 Agent 能力、检索工具和自动化系统迭代。

---

## 十五、结论：从“AI替人写”转向“人如何作为责任主体治理 AI 扩展后的研究能力”

生成式 AI 使研究活动面对一种新的速度结构：AI 工具可以生成、组合、重述、整理和探索远多于人类能够逐字检查的材料。如果我们仍然把“真正的人类作者”理解为“亲自键入每个句子的人”，就无法描述现实的人机研究实践；但如果因为 AI 能执行更多工作，就把目的、判断、方向以及最终责任主体位置一并交给模型，也会使人类作者身份与研究责任逐渐失去实际内容。

AHICP 提出的方向是：**扩展研究工作的执行与表达能力，同时把人类作为责任主体这一点，以及人类目的、权威、记忆、证据、framework 确认和最终批准显性化。**

在这个模型中，AI Agent 作为工具可以执行或辅助大量工作，但研究或创作的目的、核心问题与方向必须由人类给予和导航；Working Framework 可以在 AI 帮助下形成，但只有在人类对其中实际呈现的全部实质内容形成清晰理解、逐项审核并明确确认后，才可能成为 Approved Framework；全文可以在这一结构之下由 AI 大量扩写，但扩写必须保持 framework 忠实，并在对外发布前通过相应的 Final Artifact Approval。

尤其当研究成果进入公共知识空间时，关键不只是“有没有人类参与”，而是是否仍有明确的人类责任主体对项目方向、核心思想结构和具体公开版本承担责任。

因此，AI 时代研究方法论的关键问题不必被表述为“机器是否参与了思考”，而可以更直接地表述为：

> **一个研究共同体能否清楚地说明：项目的目的和方向由谁给予，核心思想结构由谁理解并确认，哪些具体工作由 AI 工具执行或辅助，最终由哪些人类主体对知识主张和公开版本承担责任，以及当 Agent 被替换之后，这些责任关系和思想连续性是否仍然可追踪？**

AHICP 将这一问题转化为一个可以被实现、审计、测试和持续改进的开源协议问题。

---

## 参考文献与规范来源

- Clark, A., & Chalmers, D. (1998). The Extended Mind. *Analysis*, 58(1), 7–19. https://doi.org/10.1093/analys/58.1.7
- Hardwig, J. (1985). Epistemic Dependence. *The Journal of Philosophy*, 82(7), 335–349. https://doi.org/10.2307/2026523
- Hutchins, E. (1995). *Cognition in the Wild*. MIT Press. https://doi.org/10.7551/mitpress/1881.001.0001
- Parasuraman, R., & Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. *Human Factors*, 39(2), 230–253. https://doi.org/10.1518/001872097778543886
- International Committee of Medical Journal Editors (ICMJE). Defining the Role of Authors and Contributors. https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html
- Nature Portfolio. Editorial Policies, including Artificial Intelligence (AI) policies. https://www.nature.com/nature-portfolio/editorial-policies
- *Nature Methods*. (2026). Using AI responsibly in scientific publishing. *Nature Methods*, 23, 271. https://doi.org/10.1038/s41592-026-03020-1
- NISO. CRediT — Contributor Role Taxonomy; ANSI/NISO Z39.104-2022. https://credit.niso.org/ ; https://doi.org/10.3789/ansi.niso.z39.104-2022
- UNESCO. (2023). Guidance for Generative AI in Education and Research. https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research

完整的来源核验说明见 `evidence/METHODOLOGY_SOURCES.zh-CN.md`，BibTeX 元数据见 `paper/methodology-references.bib`。

## 当前文章开发说明

本文是 AHICP 项目的方法论文章第一版完整工作稿。它依据 `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md` 展开，但该框架尚未通过人类的正式 Framework Approval，因此本文应被视为 `DERIVED-PROVISIONAL`，而不是最终的人类确认稿。