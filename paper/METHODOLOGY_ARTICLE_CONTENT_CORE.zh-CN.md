# 方法论文章 — Content Core

**角色：** AHICP 方法论文章中，人类原创实质性思想的规范基础。

本文件只包含创始讨论中由人类明确提出或明确确认的承诺。AI 生成的术语、更强的命题、文献解释、经验研究计划和文章结构，在人类明确接受之前，都不属于本文件的规范内容。

## C1. 文章必须解释 AHICP 在研究场景中的方法论意义

AHICP 不能只是一套可执行的开放协议。它还应产出一篇研究取向的方法论文章，解释该协议的思想、架构，以及它在 AI 辅助研究与长篇思想工作中的方法论意义。文章可以保持 research-specific，而协议本身的适用范围更广。

## C2. 文章必须讨论 AI 工具参与下的人类目的、方向与责任主体地位

文章应以人类作为研究或创作项目的目的来源、发起与导航主体。项目要解决什么问题、朝什么方向推进，以及最终核心成果是否得到认可，必须由人类给予、理解并批准。

这里不应把“人类责任”当作一个无需进一步说明的抽象属性。更精确的核心命题是：**在人机协作的研究与探究中，人类仍然是责任主体／责任承担者。**

AI Agent 在 AHICP 中被视为协作工具，可以执行或辅助检索、综合、结构化、起草、修订、重组、核查、格式处理等大量工作。但文章不应把 AI 描述为具有认知性的主体，也不应使用“AI 承担认知劳动”或“AI 承担认知任务”作为核心概念。

真正需要讨论的是：哪些具体工作可以由 AI 工具执行或辅助，以及哪些目的设定、理解、判断、确认和责任必须由人类作为责任主体承担。

## C3. 文章必须解释基于仓库的持久协作

文章应说明，为什么持久研究状态应被外部化到 GitHub 仓库文档中，而不是依赖某一个 AI Agent、平台记忆、账号上下文或聊天窗口。

## C4. 文章必须解释人类意图、AI 表示与派生文本的分离

文章应解释三层长期研究记忆——Layer 1 Human Authorial Core、Layer 2 Current Framework、Layer 3 Derived Artifact——以及与三层并行的 Working Memory。AI 扩写必须服从经人类确认的上游长期状态；Working Memory 只负责当前阶段、目标、任务、阻塞、待确认事项和续接。

## C5. 文章必须解释 framework 层的人类责任主体地位

对于长篇成果，Layer 2 Current / Approved Framework 是人类作为责任主体时，其核心思想责任的主要结构性承载点。

人类作者在 Framework Approval 前必须对 framework 中实际呈现的全部实质内容形成清晰、完整的理解，并逐项认真审核和明确确认。这至少包括核心命题、推论关系、关键区分、范围条件、章节/小节功能，以及被纳入 framework 的具体措辞。

Framework 可以由 AI 辅助提出、组织和表达，但获批版本必须真实体现人类作者的核心思想与认同。人类对该 framework 所承载的原创性、理解、判断和思想责任负责；AI 不能成为这一责任的承担主体。

文章仍应区分已经存在于被批准架构中的 framework-level defect，与后续 AI 扩写中才局部引入的 derived-expansion defect。Framework 作为主要思想责任锚点并不取消 Final Artifact Approval，也不取消事实准确性、研究诚信及适用发布渠道规则对最终成果的要求。

## C6. 文章必须解释两个不同的批准门

Framework Approval 与 Final Artifact Approval 是不同的。Framework Approval 涉及思想架构；Final Artifact Approval 涉及具体的公开发布/投稿版本，并必须尊重适用的学术、机构、出版商或发布渠道要求。

## C7. 已批准 framework 应在面向读者的总览中被表示

经人类确认的思想结构应有意义地反映在最终成果的摘要、引言、开篇概览、书籍导论/路线图或类似面向读者的部分中，使公开成果在结构上忠实于人类实际批准的 framework。

## C8. AI Agent 应可替换，而项目状态应持久

方法论应说明：长期研究连续性应存在于人类治理、显式的仓库状态中，而不是某一个 AI Agent 的私有上下文中。新的、能力合格的 Agent 应能通过仓库重建项目当前状态，而无需原始聊天历史。

## C9. 协议必须可以实际实施和复用

AHICP 不是一个纯粹抽象的哲学提案。其文件层级、更新规则、批准状态与模板应具体到足以在未来研究项目中实例化。

用于评价 AHICP 的经验研究方向已经通过 AHICP-D030 获得人类确认，包括 handoff/resumption、Agent/Model substitution、decision persistence、semantic drift/framework fidelity、review effort、stale/conflict handling 与 memory curation/retrieval efficiency。具体 benchmark 实现、样本、统计设计与效果结论仍需后续研究。

## C10. 文章不得夸大尚未确认的 AI 提议

`generation–verification asymmetry` 与 `semantic version control` 仍是解释性、provisional 的 AI 表述，不应写成成熟领域标准术语。AHICP-D030 已明确接受把一套经验评估框架纳入论文，但具体 benchmark 实现、指标细节与任何效果性结论仍不得未经研究而被提升为事实。

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

文章应解释：AHICP 不需要在聊天上下文中长期维护一份与 GitHub 平行的项目状态副本。

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

## C16. 公开知识传播必须保留人类责任主体

当研究、探究、论证或知识主张通过论文、书籍、报告、演示、网站或其他形式进入公开传播时，人类必须保持为责任主体。

AI Agent 可以作为工具参与搜索、整理、分析辅助、起草、扩写、核查和呈现，但不能被当作承担最终知识传播责任的主体。

这一原则通过人类对项目目的与方向的授权、Framework Approval 以及适用时的 Final Artifact Approval 共同落实。

## C17. 论文作为一篇统一论文发展，并以 Project Memory Architecture 为核心理论贡献

方法论文章不拆分为独立的“协议论文”和“记忆论文”。现有 article 应在同一篇论文中整合 AHICP 的协议设计、项目记忆架构、工作记忆、Agent 替换、人类决定持久化、framework approval 与可审计作者性。

中心命题之一是：

> **长期人机项目的持久记忆应属于项目，而不是属于某个具体模型。**

这里的“属于项目”是工程与治理意义上的表述：关键项目状态应保存在人类可检查、可编辑、可版本控制、可迁移的外部状态中，而不是只能依赖模型内部或平台私有记忆。

## C18. Working Memory 是连续性层，不是心理学 working memory 或模型隐藏状态

论文必须明确说明 AHICP Working Memory 的概念边界。

Working Memory 是对项目当前认识状态与任务状态的持久操作表示，用来回答“现在做到哪里、正在解决什么、下一步是什么、有哪些 blocker / clarification / pending human decision”。

它是 cross-session / cross-Agent continuity layer，而不是：
- 对人类心理工作记忆的模拟；
- 模型隐藏状态；
- chain-of-thought；
- 全量长期档案。

Current Focus + Task Plan 是默认续接状态；Work Log 服务于按需历史回顾。

## C19. Human Decision Persistence 是 Project Memory 的一等组成部分

论文必须把人类决定状态作为 first-class project memory 来讨论。

至少应区分：
- PROPOSED：AI 或其他来源提出但尚未被接受；
- CONFIRMED / APPROVED：已经被人类明确确认；
- REJECTED：已被人类拒绝，后续 Agent 不应因换模型而把它重新当成未决建议；
- DEFERRED / OPEN：明确保留为以后处理；
- AUTHORIZED：在明确 scope 内允许执行的行动或状态转换。

Decision persistence 的作用不是禁止未来改变决定，而是要求未来变化保留来源、版本、理由与新的授权，不允许“换了 Agent 就失忆”。

## C20. Agent / Model Substitution 是架构压力测试

论文必须把 Agent / Model 替换能力作为 AHICP project-memory architecture 的重要评估标准。

如果移除当前 Agent、当前聊天历史与平台私有记忆，一个新的合格 Agent 应能通过显式入口、Working Memory、长期记忆层、Decision Log、evidence 与 manifest 恢复：
- 项目目的；
- 当前问题与范围；
- 已知证据与关键不确定性；
- 已确认 / 已拒绝 / 待确认的决定；
- 当前 framework / artifact 状态；
- 当前任务、blocker 与 next action；
- 隐私与发布授权边界。

无法恢复时，应视为 persistence / onboarding defect，而不是要求人类重新讲一遍所有历史。

## C21. Project Memory 应以多角色功能架构讨论，并包含记忆治理

论文应从功能上讨论以下 project-memory roles：
- normative memory；
- epistemic / evidence memory；
- decision memory；
- working / operational memory；
- handoff memory；
- publication / authorization memory。

这些角色可以映射到一个或多个实际文件，不要求“一种 memory = 一个文件”。

论文还必须讨论 memory curation：项目不应保存一切，也不应把全部历史每次塞进模型上下文。需要处理：
- active vs archived state；
- current vs stale state；
- conflicting memory；
- selective retrieval；
- summary / index；
- promotion / write-back；
- history growth / memory bloat；
- privacy / disclosure boundary。

## C22. 论文纳入明确的 proposed evaluation framework，但不得虚构结果

论文应把 AHICP 作为可被经验检验的设计架构，并提出至少以下评估：
- zero-context handoff / resumption test；
- agent/model substitution test；
- decision-persistence test；
- semantic drift / framework fidelity test；
- review-effort study；
- stale/conflict handling test；
- memory-curation / retrieval-efficiency test。

这些评估目前属于研究设计与 future empirical work。除非真实实验已经执行并记录，不得写成 AHICP 已经被证明提高准确性、完整性、效率、research integrity 或减少审查负担。

AHICP-D030 使“在论文中纳入上述评估框架”成为人类确认的文章方向；具体 benchmark、样本、统计方法和结论仍需后续研究设计与实际数据。

## 当前尚未解决的人类决定

当前续接状态由 Working Memory Index、Current Focus 与 Task Plan 维护；高影响未决问题的 active state 位于 `docs/working-memory/task-plan.zh-CN.md`。Work Log 主要供人类回顾。

`CLR-001`、`CLR-002`、`CLR-005` 已通过 HARC-D023 解决并 Promotion。与文章直接相关、仍处于 pending 的主要 clarification 为 `CLR-003`、`CLR-004`、`CLR-006`、`CLR-007`、`CLR-008`；`CLR-010` 仍影响最终投稿/发布形式，而不是当前 Framework Approval readiness。

## 来源纠正

此前一个版本把明确的经验测试计划写得像是已经属于人类原创文章基础，这是过强的；当时它确实只是 AI 后续发展的扩展。AHICP-D030 已改变这一状态：人类发起人现已明确接受把 handoff/resumption、Agent/Model substitution、decision persistence、semantic drift/framework fidelity、review effort、stale/conflict handling 与 memory-curation/retrieval-efficiency 纳入同一篇论文的 proposed evaluation framework。这个更新只确认“应当研究这些问题”，并不构成任何实证结果，也不预先批准具体 benchmark 实现、样本、统计方法或效果结论。

## 双语规则

本中文文件是规范性基准。英文 `METHODOLOGY_ARTICLE_CONTENT_CORE.md` 是同步镜像。任何实质性修改必须同步到英文。

## 状态

当前创始讨论中的人类原创文章基础已经得到表示。Working article structure 仍未被人类批准。
