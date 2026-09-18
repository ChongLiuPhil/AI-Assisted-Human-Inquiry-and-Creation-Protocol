# 方法论文章 — Content Core

**角色：** HARC 方法论文章中，人类原创实质性思想的规范基础。

本文件只包含创始讨论中由人类明确提出或明确确认的承诺。AI 生成的术语、更强的命题、文献解释、经验研究计划和文章结构，在人类明确接受之前，都不属于本文件的规范内容。

## C1. 文章必须把 HARC 解释为一种研究协作方法论

HARC 项目不能只是一套可执行的开放协议。它还应产出一篇方法论文章，解释该项目的思想、架构以及它对人机研究协作的意义。

## C2. 文章必须讨论 AI 工具参与下的人类目的、方向与责任

文章应以人类作为研究或创作项目的目的来源、发起与导航主体。项目要解决什么问题、朝什么方向推进，以及最终核心成果是否得到认可，必须由人类给予、理解并批准；最终成果的核心责任由人类承担。

AI Agent 在 HARC 中被视为协作工具，可以执行或辅助检索、综合、结构化、起草、修订、重组、核查、格式处理等大量工作。但文章不应把 AI 描述为具有认知性的主体，也不应使用“AI 承担认知劳动”或“AI 承担认知任务”作为核心概念。

真正需要讨论的是：哪些具体工作可以由 AI 工具执行或辅助，以及哪些目的设定、理解、判断、确认和责任必须保持在人类治理之下。

## C3. 文章必须解释基于仓库的持久协作

文章应说明，为什么持久研究状态应被外部化到 GitHub 仓库文档中，而不是依赖某一个 AI Agent、平台记忆、账号上下文或聊天窗口。

## C4. 文章必须解释人类意图、AI 表示与派生文本的分离

文章应解释三层长期研究记忆——Layer 1 Human Authorial Core、Layer 2 Current Framework、Layer 3 Derived Artifact——以及与三层并行的 Working Memory。AI 扩写必须服从经人类确认的上游长期状态；Working Memory 只负责当前阶段、目标、任务、阻塞、待确认事项和续接。

## C5. 文章必须解释 framework 层的人类责任

对于长篇成果，Layer 2 Current / Approved Framework 是人类核心思想责任的主要结构性承载点。

人类作者在 Framework Approval 前必须对 framework 中实际呈现的全部实质内容形成清晰、完整的理解，并逐项认真审核和明确确认。这至少包括核心命题、推论关系、关键区分、范围条件、章节/小节功能，以及被纳入 framework 的具体措辞。

Framework 可以由 AI 辅助提出、组织和表达，但获批版本必须真实体现人类作者的核心思想与认同。人类对该 framework 所承载的原创性、理解、判断和思想责任负责。

文章仍应区分已经存在于被批准架构中的 framework-level defect，与后续 AI 扩写中才局部引入的 derived-expansion defect。Framework 作为主要思想责任锚点并不取消 Final Artifact Approval，也不取消事实准确性、研究诚信及适用发布渠道规则对最终成果的要求。

## C6. 文章必须解释两个不同的批准门

Framework Approval 与 Final Artifact Approval 是不同的。Framework Approval 涉及思想架构；Final Artifact Approval 涉及具体的公开发布/投稿版本，并必须尊重适用的学术、机构、出版商或发布渠道要求。

## C7. 已批准 framework 应在面向读者的总览中被表示

经人类确认的思想结构应有意义地反映在最终成果的摘要、引言、开篇概览、书籍导论/路线图或类似面向读者的部分中，使公开成果在结构上忠实于人类实际批准的 framework。

## C8. AI Agent 应可替换，而项目状态应持久

方法论应说明：长期研究连续性应存在于人类治理、显式的仓库状态中，而不是某一个 AI Agent 的私有上下文中。新的、能力合格的 Agent 应能通过仓库重建项目当前状态，而无需原始聊天历史。

## C9. 协议必须可以实际实施和复用

HARC 不是一个纯粹抽象的哲学提案。其文件层级、更新规则、批准状态与模板应具体到足以在未来研究项目中实例化。

用于评价 HARC 的精确经验 benchmark 方案目前尚不是人类确认的核心承诺。

## C10. 文章不得夸大尚未确认的 AI 提议

`generation–verification asymmetry`、`semantic version control` 以及某一特定经验测试套件等术语和更强命题，可能是有用的 AI 表述，但在人类明确接受之前仍属于 provisional。

`responsibility concentration` 已被人类明确决定不作为当前中心术语继续使用。后续应使用“人类目的与方向”“framework 责任锚点”等描述性表达来说明责任模型，除非人类以后重新决定采用新的中心术语。

## C11. 高影响不确定性应作为 Working Memory 中的 Clarification 管理

文章必须解释：Clarification 不是 Layer 1 与 Layer 2 之间的独立“1.5 层”，而是 Working Memory 中的一种 item。

当 AI 对作者意图、核心命题、关键概念、范围、论证关系、章节功能或关键术语/翻译存在可能重大改变论证结构的非微不足道不确定性时，AI 不应自行猜测，而应把问题放入 Working Memory 的 Clarification 队列，向人类作者请求确认。

未解决 clarification 不是人类长期承诺。人类确认或纠正后，其结果必须通过 Promotion 进入 Decision Log 与相应长期记忆，再传播到 Framework 和 Artifact。

这一机制尤其适用于作者母语中的核心概念及其英文对应。

## C12. 跨 Agent 接管必须通过显式启动入口和可验证握手

文章应解释：仅仅把状态写进仓库，并不足以保证新的 AI Agent 会正确接管。项目还需要显式零上下文入口与 Onboarding Report。新 Agent 应先读取 Working Memory，确认当前阶段、目标、任务、阻塞、待确认事项和下一步，再从三层长期记忆按需读取权威状态。

这一机制的目的不是假设所有 AI 平台都会自动读取同一文件名，而是通过根目录入口、Agent 契约、机器可读 manifest 与人类可复制 bootstrap prompt，最大化跨平台可发现性，并把“接管是否成功”变成可观察、可验证的步骤。

## C13. GitHub 应作为权威外部记忆与工作状态接口

文章应解释：HARC 不需要在聊天上下文中长期维护一份与 GitHub 平行的项目状态副本。

更准确的架构是：

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

模型在某一次回答中仍需要临时读取相关信息，但应根据当前任务从 GitHub 最新 canonical revision 按需获取最小必要内容。

会话只保留一个极小的 Repository Resolver。Working Memory 与三层长期记忆都保存在 GitHub：Working Memory 提供当前续接状态，Layer 1/2/3 提供长期研究状态。它们都不应被长期复制成第二份聊天权威副本。

所有影响未来工作的状态改变直接写回 GitHub；写入后，先前读取到上下文中的旧版本立即视为 stale。高影响判断和写入前应重新确认相关最新 revision。

这一机制使 GitHub 真正成为跨 Agent 的记忆库和工作库，而模型上下文只是当前任务对仓库状态的一次临时投影。

## C14. 三层长期研究记忆应与并行 Working Memory 区分

文章应明确区分：

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

与并行的：

`Working Memory = current stage / goals / tasks / blockers / clarifications / TODO / handoff`

前三层描述项目的长期思想与成果状态；Working Memory 描述当前工作过程的位置。

Layer 2 虽然名称中含有 “Working”，但它仍属于长期项目记忆：它保存当前论述框架、核心命题、关键概念和结构，并比 Layer 1 更可修改。

Working Memory 中获得人类确认的内容必须 Promotion 到相应长期层，随后 Working Memory 只保留状态和指针。

## C15. Working Memory 应区分运行时续接状态与人类回顾历史

文章应说明，Working Memory 不必固定为一个文档，而可以根据工程需要拆成多个逻辑角色。

至少应区分：

- **Current Focus** — 当前最近期、最高优先级目标与 immediate next action；
- **Task Plan** — 动态任务、TODO、blockers、pending human decisions、Clarifications 与 next actions；
- **Work Log** — 主要供人类作者以后回顾的阶段性历史纪要。

Current Focus + Task Plan 构成跨 Agent 接管时需要的 operational resume state；Work Log 则主要保存项目如何发展到当前位置、重要方向怎样变化、哪些任务批次已经完成。

Work Log 不应成为普通 AI onboarding 的必读上下文，也不应保存模型隐藏 chain-of-thought。完成任务应退出 active Task Plan，并在 Work Log 中形成适当粒度的历史摘要；稳定规范结果仍必须 Promotion 到对应 Long-Term Memory。

这一设计使“无缝继续工作”与“人类以后回顾自己的思想/项目变化”成为两个不同但相互关联的记忆功能。

## 当前尚未解决的人类决定

当前续接状态由 Working Memory Index、Current Focus 与 Task Plan 维护；高影响未决问题的 active state 位于 `docs/working-memory/task-plan.zh-CN.md`。Work Log 主要供人类回顾。

`CLR-001`、`CLR-002`、`CLR-005` 已通过 HARC-D023 解决并 Promotion。与文章直接相关、仍处于 pending 的主要 clarification 为 `CLR-003`、`CLR-004`、`CLR-006`、`CLR-007`、`CLR-008`；`CLR-010` 仍影响最终投稿/发布形式，而不是当前 Framework Approval readiness。

## 来源纠正

此前一个版本把明确的经验测试计划（handoff test、semantic-drift test、framework-fidelity test、review-effort test、cross-model portability test）写得像是已经属于人类原创文章基础，这是过强的。

人类发起人明确要求的是：HARC 必须可实际实施、可复用；具体经验测试计划是 AI 后续发展的扩展，在被人类接受前仍属于 provisional。

## 双语规则

本中文文件是规范性基准。英文 `METHODOLOGY_ARTICLE_CONTENT_CORE.md` 是同步镜像。任何实质性修改必须同步到英文。

## 状态

当前创始讨论中的人类原创文章基础已经得到表示。Working article structure 仍未被人类批准。
