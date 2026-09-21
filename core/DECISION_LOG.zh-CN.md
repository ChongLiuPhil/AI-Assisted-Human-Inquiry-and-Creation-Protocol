# HARC 决策日志

> **本中文文件是规范性基准；英文 `DECISION_LOG.md` 是同步镜像。**

本文件是有关 HARC 协议项目的人类实质性决定的时间顺序审计轨迹。

## 条目格式

- 日期
- 标识符
- 来源
- 分类
- 决定
- 受影响组件
- 状态

---

## 2026-09-17 — HARC-D001

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** 建立一个独立、开放的 GitHub 项目，专门用于 Human–AI Research Collaboration Protocol，并与任何特定研究论文或主题分离。

**受影响组件：** 仓库范围、README、规范、白皮书、模板

**状态：** 已实现。

---

## 2026-09-17 — HARC-D002

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** 初始实现以 GitHub 作为人类与 AI Agent(s) 之间的持久协作平台。以后可考虑其他平台。

**受影响组件：** 范围与架构

**状态：** 已实现。

---

## 2026-09-17 — HARC-D003

**来源：** 人类项目发起人  
**分类：** CONTENT, PROTOCOL

**决定：** 人机讨论必须产生一个持久的基础记录，保存人类作者的实质性主张、纠正、确认与修订。AI 扩写必须受到该基础约束。

**受影响组件：** Content Core 模型、上游优先规则

**状态：** 已实现。

---

## 2026-09-17 — HARC-D004

**来源：** 人类项目发起人  
**分类：** FORM, PROTOCOL

**决定：** 呈现与格式指令必须与研究内容指令分离，并存入独立的形式/呈现基础文档。适当情况下，作者的跨项目偏好应可复用。

**受影响组件：** Form Core、路由模型、模板

**状态：** 已实现。

---

## 2026-09-17 — HARC-D005

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** AI Agent 应维护文章/书籍论证的紧凑操作性表示。该表示是结构性协作的主要讨论界面，并且必须服从人类基础状态。

**受影响组件：** Working Argument Map

**状态：** 已实现。

---

## 2026-09-17 — HARC-D006

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** 人类纠正必须先向上游传播：先持久化人类修改，再更新操作性表示，最后更新扩写成果。

**受影响组件：** 更新循环

**状态：** 已实现。

---

## 2026-09-17 — HARC-D007

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** AI 维护的 Working Framework 不自动等于人类认可。经人类确认的版本应显式保存，并由这些 Approved Framework 约束后续扩写。

**受影响组件：** Framework Approval Gate、版本化 framework 快照

**状态：** 已实现。

---

## 2026-09-17 — HARC-D008

**来源：** 人类项目发起人  
**分类：** CONTENT, FORM, PROTOCOL

**决定：** 经人类批准的核心 framework 应反映在最终成果的总览中，例如论文的摘要/引言、普通文章的开篇/总览、书籍的导论/章节路线图。

**受影响组件：** overview projection rule

**状态：** 已实现。

---

## 2026-09-17 — HARC-D009

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** 项目连续性必须明确依赖仓库状态，而不是某一个 AI 平台的上下文或记忆。重要讨论结果必须提升为 GitHub 文档。

**受影响组件：** 持久记忆模型、交接要求

**状态：** 已实现。

---

## 2026-09-17 — HARC-D010

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** 仓库可以积累长期项目记忆，但当前摘要应保持紧凑，使新 Agent 能通过选择性阅读重建项目，而无需一次加载全部历史。

**受影响组件：** 记忆扩展

**状态：** 已实现。

---

## 2026-09-17 — HARC-D011

**来源：** 人类项目发起人  
**分类：** CONTENT, PROTOCOL

**决定：** 对于长篇成果，经人类批准的操作性 framework 应作为主要实质性思想责任锚点。人类作者应明确理解并批准核心命题、推论关系、主要区分以及章节/小节角色。已批准架构中的缺陷应能与后续 AI 扩写中才产生的局部缺陷区分。该机制不取代投稿/出版前另行要求的最终发布审阅。

**受影响组件：** Protocol Core、Framework Approval 模型、责任模型

**状态：** 在创始思想修复审计后已实现。

---

## 2026-09-17 — HARC-D012

**来源：** 人类项目发起人  
**分类：** FORM, PROTOCOL

**决定：** 形式与呈现偏好应跨项目复用，并支持成果类型区分。新项目应确定是书籍、学术论文、普通文章、报告还是其他成果类型，然后组合作者可复用偏好、成果类型规则和项目特定规则，而不是每次从零建立呈现系统。

**受影响组件：** Form Core 模型、form-profile 继承、模板

**状态：** 在创始思想修复审计后已实现。

---

## 2026-09-17 — HARC-D013

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** “三遍审查”必须解释成三轮完整的审查—修复循环。每一轮中，Agent 都要检查项目、识别遗漏/缺陷、修复并实现必要变化，然后验证修复，再进入下一轮。三轮之后还要进行一次额外、独立的修复后审计。

**受影响组件：** Protocol Core、审计程序、审计文档

**状态：** 已实现。

---

## 2026-09-17 — HARC-D014

**来源：** 人类项目发起人  
**分类：** CONTENT, FORM, PROTOCOL

**决定：** HARC 应同时成为高质量开放项目并产出独立的方法论文章。文章应解释 HARC 的概念架构，并讨论人类认知责任、向 AI 委托思想劳动的范围与边界、框架层作者性、持久研究记忆以及 AI 时代人机协作的相关问题。

**受影响组件：** 项目目的、README、方法论文章、文章 framework、证据层、路线图

**状态：** 已建立第一版受治理的方法论文章 framework 与完整中文 provisional 草稿；人类 Framework Approval 与之后的 Final Artifact Approval 仍未完成。

---

## 2026-09-18 — HARC-D015

**来源：** 人类项目发起人  
**分类：** FORM, PROTOCOL

**决定：** Human–AI Research Collaboration Protocol 项目的所有实质性内容必须同时维护中文与英文版本。中文是规范性的编辑与审阅基准。任何实质性编辑都必须在同一工作轮次中同步更新英文版本。如果中英文发生偏离，以中文为准并修复英文镜像。新项目文件应从创建时起就双语化。

**受影响组件：** Protocol Core、Specification、AGENTS 契约、README、方法论文章、证据笔记、审计、模板、未来文件

**状态：** 已实现初始仓库级双语迁移；后续每次实质性编辑仍必须持续执行同步。详见 `docs/BILINGUAL_PARITY_AUDIT.zh-CN.md`。

---

## 2026-09-18 — HARC-D016

**来源：** 人类项目发起人  
**分类：** CONTENT, FORM, PROTOCOL

**决定：** 中文 canonical / 英文 synchronized mirror 规则建立时，不能机械地用当时较旧的中文版覆盖规则建立前已经在英文版中形成的较新实质内容。对于这种 legacy divergence，应先把英文较新内容吸收到中文版，使中文达到切换时真正的最新状态；完成中英 parity 后，再正式切换为“中文发展、英文同步”的长期方向。切换完成后，英文不得再独立发展实质内容。

**受影响组件：** Bilingual Sync Policy、Protocol Core、AGENTS、Whitepaper、Parity Audit、未来 legacy migration

**状态：** 已实现。白皮书已完成 English -> Chinese catch-up，再恢复为 Chinese -> English 同步关系。

---

## 2026-09-18 — HARC-D017

**来源：** 人类项目发起人  
**分类：** CONTENT, FORM, PROTOCOL

**决定：** HARC 应增加一个专门治理高影响不确定性的文档层。AI Agent 对作者意图、核心观点、关键命题、概念、术语、母语/英文对应、范围或论证结构存在重要不确定性时，应主动登记并向人类作者提出确认，而不是自行选择一种解释后继续落实。经人类确认或纠正的结果，应沉淀进相应的基础 Core / Decision Log，并进一步更新论证结构与最终成果。该层应特别保护那些一旦误解就会显著改变第二层论证结构或核心表达的内容。

**架构决定：** 采用 `Critical Clarification Register`，定位为 Layer 1 与 Layer 2 之间的 **Layer 1.5 bridge**。未解决条目不是人类承诺；解决后必须执行 Resolution Promotion。

**受影响组件：** Protocol Core、Specification、AGENTS、Architecture、project template、methodology article governance、framework review workflow

**状态：** 已实现。

---

## 2026-09-18 — HARC-D018

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** HARC 应为任何从零开始接手项目的 AI Agent 提供显式的前置启动入口与提示机制，使 Agent 在最初阶段就能理解项目层级、读取顺序、Clarification 机制、Framework/Artifact 状态和强制传播流程。Agent 在进行实质性工作前应先完成接管握手，向人类报告其根据仓库重建出的当前状态。应同时提供人类可读启动文件、可复制 bootstrap prompt、Agent 契约与机器可读 manifest，以降低不同 AI 平台之间的发现差异。

**限定：** 仓库文件无法技术上保证任意外部 AI 平台会自动读取某一文件；HARC 的合规目标是最大化入口可发现性，并通过 Onboarding Report 验证 Agent 是否真正理解和遵循工作流。

**受影响组件：** START_HERE、HARC_MANIFEST、AGENTS、README、Specification、Persistent Memory、项目模板、Agent handoff

**人类后续确认：** 人类项目发起人明确确认上述理解“基本准确”，并要求正式落实。该确认支持把 zero-context bootstrap、独立启动提示词、manifest、Onboarding Handshake 与 Onboarding Report 作为正式 HARC 协议组成部分。

**状态：** 已确认并实现。

---

## 2026-09-18 — HARC-D019

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** 在新的 AI Agent 读取 GitHub 仓库并完成 onboarding 后，应进一步把关键 HARC 规则和当前项目状态压缩成一份会话级操作契约，并由 Agent 明确写入自己的当前回复，使这些规则重新进入本轮对话上下文，形成“仓库持久状态 + 当前会话活动契约”的双层保险。该文件应主动提示 Agent 执行这一操作，并在重大状态变化或上下文可能丢失时刷新。

**限定：** 该机制不得声称把仓库文件提升成平台真正的 system prompt，也不得声称能够修改模型参数、隐藏记忆或平台级 memory。平台 system/developer/safety 指令始终高于 HARC Session Contract。

**实现：** 新增 `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` / English mirror，并接入 START_HERE、Bootstrap Prompt、Manifest、Onboarding Report、Agent contract 与项目模板。

**状态：** 已确认并实施。

---

## 2026-09-18 — HARC-D020

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：** HARC 应进一步把 GitHub 直接作为 AI Agent 的权威外部记忆库和工作状态库。Agent 不需要在聊天上下文中长期维护一份重复的项目状态镜像，而应根据当前任务从 GitHub 按需读取最新 canonical 文件；所有应影响未来工作的更新直接写回 GitHub。模型上下文只保留最小访问内核和当前任务所需的临时缓存。

**接口原则：**

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

写入后旧上下文副本立即失效；高影响判断和写入前必须重新确认最新 revision。优先通过 GitHub API、MCP、connector/plugin 或等价工具完成按需读取和 write-through。

**对 HARC-D019 / P21 的修订：** Active Session Contract 不再承担动态项目状态副本；它被收缩为 Repository Resolver / access kernel。动态 Blocking Clarifications、Framework、Artifact 和 Core 状态需要时直接从仓库最新版本读取。

**实现：** 新增 `protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md`、英文 mirror 与机器可读 `HARC_CONTEXT_INTERFACE.yaml`，并接入启动链、manifest、Agent contract 和项目模板。

**状态：** 已确认并实施。

---

## 2026-09-18 — HARC-D021

**来源：** 人类项目发起人  
**分类：** PROTOCOL, CONTENT

**决定：** 原来的 “Layer 1.5 / Critical Clarification Layer” 模型不再使用。HARC 应明确区分三层**长期研究记忆**与一个并行的 **Working Memory（工作记忆区）**。

三层长期记忆为：

1. Layer 1 — 人类作者核心基础：持续沉淀、纠正、净化的人类核心观点与长期承诺；
2. Layer 2 — 当前论述框架：以 Layer 1 为基础的核心命题、关键概念、论述结构和推论关系；持久但更可修改，并可包含 Layer 1 未逐项表达的结构性内容；
3. Layer 3 — 派生成果：主要基于 Layer 2 展开的完整成果。

Working Memory 与三层并行，记录当前阶段、工作目标、总体规划、active tasks、已完成/未完成、next actions、TODO、blockers、待人类确认事项、clarifications、同步缺陷与 handoff 信息。

Clarification 是 Working Memory 中的一种 item，而不是独立层。问题获得人类确认后，规范结果应 Promotion 到相应长期记忆；Working Memory 中该项退出 active 状态，只保留 resolved/promoted 指针与审计痕迹。

**受影响组件：** Protocol Core、Persistent Memory、Architecture、Clarification workflow、Working Memory、Onboarding/Handoff、Manifest、Context Interface、Specification、AGENTS、项目模板、方法论文章

**状态：** 已实现。

---

## 2026-09-18 — HARC-D022

**来源：** 人类项目发起人  
**分类：** PROTOCOL, CONTENT

**决定：** Working Memory 不应被固定理解为单一文档，而应被定义为可以根据工程需要实现为一个或多个文件的功能区。其核心逻辑至少包括：

1. `Current Focus` — 当前最近期、最高优先级工作目标；
2. `Task Plan` — 动态任务/计划清单；
3. `Work Log` — 主要供人类日后回顾的阶段性历史纪要。

Task Plan 中完成的事项应退出 active list，并适度沉淀到 Work Log；如果完成事项形成稳定规范结果，还必须 Promotion 到相应长期记忆。

Work Log 需要定期更新，保存大体进展、工作/思想路径的变化和里程碑，但它默认不应成为 AI Agent 日常 onboarding 的必读上下文。它服务于人类作者回顾项目的发展史。需要历史回顾、审计或冲突追溯时，AI 才按需读取。

Current Focus 应保持最短、显著度最高，使任何工作流被突然中断后，新 Agent 能立即知道“现在最重要的事情是什么”。

**实现原则：** 功能角色固定，物理文件布局可变；manifest 应显式映射各角色。

**状态：** 已确认并实施。


---

## 2026-09-18 — HARC-D023

**来源：** 人类项目发起人  
**分类：** CONTENT, PROTOCOL

**决定：** HARC 对 AI 辅助研究与创作中的人类责任采用以下原则：

1. 研究或创作项目的目的、核心问题与方向应由人类发起、给予并持续导航/批准；最终成果的核心责任由人类承担。
2. AI Agent 在 HARC 中作为工具参与协作，可以执行或辅助检索、综合、结构化、起草、重组、核查、格式处理等大量工作，但协议与方法论文章不应把 AI 描述为具有认知性的主体，也不应把“AI 承担认知劳动 / 认知任务”作为规范性表述。
3. 对长篇成果，Layer 2 Current / Approved Framework 是人类核心思想责任的主要结构性承载点。人类作者在 Framework Approval 前必须清楚理解、认真审核并明确确认 framework 中实际呈现的全部实质内容，包括核心命题、推论关系、关键区分、范围条件、章节/小节功能，以及被纳入 framework 的具体措辞。
4. Framework 可以由 AI 辅助整理和表达，但其获批版本必须真实体现人类作者的核心思想与认同。人类对该 framework 所承载的原创性、理解、判断与思想责任负责；这不取消 Final Artifact Approval，也不取消具体发布渠道、学科、机构或研究诚信规则对最终成果的要求。
5. `responsibility concentration` 不作为当前中心术语继续使用。责任模型应优先以“人类目的与方向 + framework 责任锚点”等描述性方式表达，而不强制建立新的单一术语。
6. 将 Approved Framework 作为未来学术人机协作规范中的可提交附件，是一个可能的发展方向，但当前尚未被确立为 HARC 的强制协议要求。

**受影响组件：** Protocol Core、Specification、research-project templates、README、方法论文章 Content Core / Working Argument Map / Derived Artifact、Framework Status、Working Memory

**解决的 Clarifications：** `CLR-001`、`CLR-002`、`CLR-005`

**状态：** 已确认；本轮执行 Promotion 与双语传播。


---

## 2026-09-18 — HARC-D024

**来源：** 人类项目发起人  
**分类：** CONTENT, FORM, PROTOCOL

**决定：**

1. 方法论文章中文题目 **《从对话到持久研究状态：AI时代的人机研究协作、人类责任与可审计作者性》** 得到人类明确认可。英文题目作为中文 canonical 的同步翻译镜像维护；该题目认可不等于对完整 Working Framework 的 Framework Approval。
2. 对 HARC-D023 的责任表述作进一步精确化：`人类责任 / human responsibility` 不应被当作一个无需解释的独立中心概念。更准确的核心命题是：**人类是责任主体**。
3. 在研究、探究活动中，尤其当研究结果、论证或知识主张以论文、书籍、报告或其他方式进入公开知识传播时，人类必须保持为责任承担主体。AI Agent 可以作为工具执行或辅助大量工作，但不能成为承担研究目的、核心判断、framework 授权或公开知识传播最终责任的主体。
4. 后续文档可以在标题或一般叙述中使用“人类责任”作为简写，但在理论定义、协议规则与关键论证处应明确其含义是“人类作为责任主体 / 人类仍是责任承担者”。
5. HARC-D023 的其他已确认内容继续有效。

**关系：** 本决定精确化 HARC-D023，不撤销其其他内容。

**受影响组件：** Article Form Core、Article Content Core、Working Argument Map、methodology article、Protocol Core、Framework Approval、Specification、README、Agent contracts/templates、Framework Status、Working Memory

**状态：** 已确认；本轮执行双语 Promotion 与传播。


---

## 2026-09-18 — HARC-D025

**来源：** 人类项目发起人  
**分类：** CONTENT, PROTOCOL

**决定：**

1. 批准对方法论文章 Working Framework 的依赖图作结构性修复，使 T9–T13 正确进入 T1/T2/T7/T8 的治理、续接与可执行性支持关系，并将 T3 的节点名称同步为“AI 工具工作分担 / 人类责任主体”。
2. Framework Approval 可以包含明确标记为 `AI-PROPOSED`、`UNRESOLVED`、`NON-BLOCKING` 或类似状态的项目，但**整体批准只批准这些项目以“未决/提议状态”存在于 framework 中的位置、范围与处理方式，不自动批准这些项目的实质内容**。
3. 因此，对一个含有显式未决项的 framework 作整体 `APPROVE`，不应把其中的 provisional terminology、经验计划、理论定位或其他 AI 提议 Promotion 为人类原创/确认观点；只有后续单独的人类决定才能改变这些项目的来源/批准状态。
4. 本决定本身不是对当前完整 Working Framework 的整体 Framework Approval，也不得据此创建 `MA-FW-001`。

**受影响组件：** Working Argument Map dependency structure；Framework Approval protocol；Framework Status；Working Memory。

**状态：** 已确认；双语传播执行。


---

## 2026-09-19 — AHICP-D026

**来源：** 人类项目发起人  
**分类：** PROTOCOL, CONTENT, FORM

**决定：**

1. 原 **Human–AI Research Collaboration Protocol (HARC)** 正式迁移为 **AI-Assisted Human Inquiry and Creation Protocol (AHICP)**。
2. 固定副标题为：**A protocol for human-led inquiry, research, reasoning, writing, and creation with AI assistance.**
3. 协议的规范性方向明确为：**human-led, AI-assisted, repository-grounded**。
4. AI 不被规范性描述为与人对称的认知主体、知识劳动主体或最终责任主体。AI 可以执行或辅助大量检索、比较、结构化、提出方案、起草、核验、转换与仓库维护工作；人的目的、方向、实质判断、批准和最终责任位置保持不可转移。
5. 协议适用范围从以 research 为主要默认场景，上位化为 inquiry / research / reasoning / writing / creation。真正只讨论研究证据、研究诚信、学术论文或研究政策的部分可以继续保持 research-specific，不进行机械替换。
6. HARC v0.2.x 的核心治理结构继续继承；迁移目标版本为 **AHICP v0.3.0-draft**。
7. 历史 Decision IDs（如 HARC-D001–HARC-D025）保持原样，作为历史审计标识；新决定从本条开始采用 AHICP 前缀。
8. AHICP 与 **Personal Publishing Framework (PPF)** 保持边界：AHICP 规范 AI 如何辅助人的探究与创作；PPF 规范作品的 source / build / publish / release / archive 生命周期。二者可独立采用，也可组合采用。

**状态：** 人类已明确确认；正在通过 v0.3 semantic migration 分支传播。

---

## 2026-09-19 — AHICP-D027

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：**

1. AHICP 正式加入通用的 **External Systems, Tool Discovery, Authorization, and Human Handoff** 治理规则。
2. 当任务需要外部系统、账户或服务，并且适当的人类授权已经存在时，AI Agent 应先安全发现并穷尽当前可用且已获授权的 machine-operable path，再把纯操作步骤交还给人类。
3. 可发现路径应覆盖平台内建工具、已连接 plugin/connector、官方 MCP、provider API、官方 GitHub App/integration、现有 repository automation 与明确批准的 adapter/plugin。
4. “installed / enabled / connected” 不构成 capability 已真正可调用的证据；当能力状态影响执行路线或是否升级给人类时，在技术上可行且安全的情况下必须以真实最小调用验证。
5. 功能等价时优先 official、OAuth、provider-managed、least-secret-handling 的连接方式。不得为了便利要求人类把 password、token、private key 或其他 secret 粘贴到聊天。
6. 只有身份授权、账户所有者 consent、权限授予、不可委托的高影响决定，或当前已授权工具能力确实无法完成的动作，才升级给人类。Human handoff 必须最少步骤、一次只要求当前必要动作、默认无技术背景，并明确哪些值不得发送给 AI。
7. 必要人类动作完成后，AI Agent 应重新读取仓库、重新验证 capability/provider actual state，并恢复后续 machine-operable work。
8. 影响未来项目工作的 external operation 必须验证真实 provider state，并把经验证的 durable result 写回 repository；provider UI、聊天状态和模型记忆不得成为与 repository 平行的 authoritative project state。
9. 该规则是 provider-neutral 的 AHICP execution/escalation governance，不把 Cloudflare 或任何其他具体 provider 写入 normative core，也不改变 PPF 的 publishing lifecycle 边界。

**受影响组件：** Protocol Core、Specification、AGENTS、research-project template、后续 adoption/conformance 审计。

**状态：** 人类已明确要求执行；本决定授权本轮规范传播。

---

## 2026-09-20 — AHICP-D028

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：**

1. 当项目第一次配置某个 integration、automation 或 workflow，且后续机器操作将依赖可重复使用的 authorization policy 时，AI Agent 应先分析场景并提出适合的人类授权方式，再由人类选择之后继续配置。
2. AI 可以推荐授权方式、解释差异与适用范围，但 **AI proposal != human authorization**；Agent 不得替人类静默采用默认授权方式，也不得先完成建立授权策略的配置，再根据技术结果反推人类已经授权。
3. 在适用时，方案应至少区分：
   - `per-action authorization`：由人类逐次确认被指定为需要单独授权的行动或状态转换；
   - `bounded pre-authorization`：人类预先批准明确且有限的 action class / target / side-effect / duration scope，AI 可在 scope 内重复执行；
   - `mixed policy`：部分低风险行动可预授权，而指定 high-impact 或 human-reserved 行动继续逐次由人类决定。
4. 人类可以选择、修改或拒绝 AI 提出的方案。最终选择必须连同 scope、authorization provenance 与 escalation conditions 写入 repository durable state，之后 AI 才能依赖该策略执行后续配置与机器操作。
5. 后续行动如果超出已选择的 action class、target、allowed side effects、duration，或 impact / reversibility 发生实质变化，则必须重新取得相应的人类选择或授权。
6. 本决定精确化 AHICP-D027 的 authorization / human-handoff 语义，并授权把这一规则传播到当前 PR #3；它**不构成对 PR #3 其余 AI-proposed 规范内容的整体批准，也不授权自动 merge**。

**受影响组件：** Specification §23.5、Protocol Core P26、AGENTS、research-project template、Protocol Contract CI。

**状态：** 人类已明确确认本项原则；授权在当前 PR #3 中传播。

---

## 2026-09-20 — AHICP-D029

**来源：** 人类项目发起人  
**分类：** PROTOCOL

**决定：**

1. 人类项目发起人批准当前 PR #3 所提出的 **scoped authorization for durable-state actions** 规范方向及其当前实质内容，包括：
   - `proposal != authorization != execution != verification != durable write-back`；
   - authorization scope / provenance 的显式建模；
   - durability 本身不自动等于 high-impact；
   - provider-neutral 的 high-impact 判断；
   - 对已授权、低风险、可逆机器操作避免不必要的人类升级；
   - AHICP-D028 所确认的首次配置 authorization-mode human choice gate。
2. 批准保留 human-reserved / non-delegable 边界：bounded pre-authorization 不得覆盖治理规则明确保留给人类的行动。
3. 批准 AHICP 与 PPF 的边界保持不变：AHICP 规范 authorization provenance、scope、selection、escalation、execution/verification separation 与 durable write-back；PPF 或其他 publishing framework 继续拥有 publication-lifecycle state semantics。
4. 本决定授权把 PR #3 从 draft 收束为可合并状态，并在最新 head 的 Protocol Contract CI 成功且未出现新的实质冲突后合并到 `main`。
5. 合并、CI 成功或其他机器执行结果本身不构成新的授权；本条人类决定是本次规范 promotion / merge 的 authorization provenance。

**受影响组件：** Specification §23.5、Protocol Core P26、AGENTS、research-project template、Decision Log、Protocol Contract CI。

**状态：** 人类已明确批准；授权完成当前 PR #3 的规范收束，并在 CI green 后合并。

---

## 2026-09-20 — AHICP-D030

**来源：** 人类项目发起人  
**分类：** CONTENT, PROTOCOL, FORM

**决定：**

1. AHICP 的现有 methodology article 继续作为**一篇统一论文**发展，不拆分为“协议论文”和“记忆论文”两篇。
2. 论文应进行实质性结构升级，把以下内容提升为核心理论贡献，而不是边缘说明：
   - **Project Memory Architecture**：长期人机项目的持久记忆应属于项目，而不是依赖某个具体模型、Agent、聊天或平台记忆；
   - **Working Memory as a continuity layer**：Working Memory 是项目当前认识/任务状态的持久操作表示和跨会话连续性层，不应与心理学意义上的人类 working memory 或模型隐藏状态混同；
   - **Agent / Model Substitution**：AI Agent 与模型应可替换，替换后仍能从仓库恢复项目目标、依据、决定、当前状态与下一步；这种可替换性应作为架构有效性的重要压力测试；
   - **Human Decision Persistence**：人类已经确认、拒绝、保留或授权的决定本身是项目记忆的一等组成部分，不能在后续 Agent 接管时退化为无来源的文本或重新变成待猜测状态。
3. 论文应把 AHICP 的记忆体系作为一个**多角色、分层且可治理的项目记忆架构**来论述。除三层 Long-Term Research Memory 与并行 Working Memory 外，还应从功能上讨论 normative memory、epistemic/evidence memory、decision memory、operational memory、handoff memory 与 publication/authorization memory；这些是功能角色，不要求机械对应为独立物理文件。
4. 论文应明确区分 **agent memory / conversational memory** 与 **project memory**。现有 Agent-memory 研究主要关注 Agent 如何存储、检索、更新并利用过去信息；AHICP 的核心问题是长期项目如何拥有独立于 Agent 的、可检查、可版本化、可追溯、可迁移的权威状态。
5. 论文必须讨论：
   - inspectability / editability / versionability / provenance；
   - evidence、inference、proposal、human-confirmed decision 的区分；
   - stale state、conflicting memory、memory curation、选择性检索与记忆膨胀；
   - Working Memory 的 promotion / resolution / write-back；
   - 隐私、未公开内容与 publication authorization 作为项目状态边界；
   - 人类责任、Framework Approval 与 Final Artifact Approval 如何与持久项目记忆连接。
6. 人类项目发起人接受将此前讨论的评估思路纳入同一篇论文，包括 handoff/resumption test、agent/model substitution test、decision-persistence test、semantic-drift/fidelity test、review-effort test，以及 memory curation/conflict handling 的评估设计。**这些当前属于 proposed evaluation / research agenda，不得伪装成已经完成的实证结果。**
7. 论文应与当前 Agent-memory、long-term interactive memory、provenance、distributed cognition / extended-mind、epistemic dependence、automation reliance 与作者/问责规范展开明确对话，同时避免声称这些文献已经证明 AHICP 的设计有效。
8. 现有题目继续保留；本决定授权对 Working Framework 和 DERIVED-PROVISIONAL 正文进行大规模结构性重写，以落实上述方向。该授权**不等于对重写后完整 Framework 的整体 Framework Approval，也不等于 Final Artifact Approval**。
9. 中文继续作为 canonical 学术稿，英文作为 synchronized mirror；本轮结构性修改必须同步维护两种语言。
10. 本决定只改变方法论文章的内容与结构方向，不撤销或替代 `AHICP-D027`–`AHICP-D029` 已生效的 external-system、authorization、human-handoff 与 scoped-authorization 治理；这些规则继续约束本项目及后续 Agent 的机器操作。

**受影响组件：** Article Content Core、Working Argument Map、Framework Status、methodology article、evidence layer、bibliography、Working Memory、Decision Log。

**状态：** 人类明确确认；授权本轮结构重构与论文升级。

---

## 2026-09-21 — AHICP-D031

**来源：** 人类项目发起人  
**分类：** CONTENT, FORM, GOVERNANCE

**决定：**

1. 人类项目发起人对“完成 methodology article 的 Framework scholarly review，并把经得住当前证据与边界约束的内容进入首个 Approved Framework snapshot”的方案明确表示 **“同意，完成”**。
2. 依据该授权以及 2026-09-21 完成的 scholarly review，当前方法论文章 framework 通过整体 **Framework Approval**，批准快照标识为：
   - `MA-FW-001`
   - 中文 canonical：`paper/frameworks/MA-FW-001.zh-CN.md`
   - 英文 mirror：`paper/frameworks/MA-FW-001.md`
3. T1–T13 按 scholarly review 中的 evidence-constrained / bounded wording 进入 `MA-FW-001`。其中：
   - T1 / T11：不得把 AHICP 写成 project memory、organizational memory、design rationale、decision provenance 或 Agent long-term memory 的首创；
   - T2 / T3 / T7 / T8 / T13：作为设计原则或架构规范批准，而不是已经验证的普遍效果定律；
   - T4：Working Memory 明确不是心理学 working memory、模型 hidden state、scratchpad 或 chain-of-thought；
   - T5：Human Decision Persistence 作为治理机制批准，并承认 decision/rationale/provenance 的既有文献前史；
   - T6：Agent / Model Substitution 作为设计目标与 proposed stress test 批准，不构成已验证鲁棒性结果；
   - T9：只作为 AHICP normative governance 批准，不扩张为所有领域的普遍作者身份或认知责任理论；
   - T10：正式采用 **Framework Approval as a Structured Human-Review Gate and Responsibility Anchor**，不再使用会暗示效率已被证明的 “Compressed Responsibility Interface” 作为批准框架名称；
   - T12：仅作为 proposed empirical research agenda 批准，没有实证结果。
4. Framework Approval 表示人类批准当前思想架构、论证边界与研究议程；它不表示当前长篇论文逐句最终批准，也不表示 citation/style 已符合特定 venue。
5. 当前正文应从 `DERIVED-PROVISIONAL` 更新为：
   `DERIVED-FROM-MA-FW-001 — FINAL ARTIFACT APPROVAL PENDING`
6. `MA-FW-001` 是批准时点的固定 baseline。后续如果对核心 thesis、论证结构、scope 或 approval semantics 作实质修改，应形成新的 framework snapshot，而不是静默改写 `MA-FW-001`。
7. 本决定**不构成 Final Artifact Approval，不选择 target venue，也不自动授权 PR merge / publication / release**。这些仍是独立治理动作。
8. AHICP-D027–D030 的 external-system、authorization、human-handoff、scoped-authorization 与 methodology structural-direction 决定继续有效；D031 只完成当前 methodology article 的 Framework Approval。

**受影响组件：** Methodology Article Framework snapshot、Working Argument Map、Framework Status、methodology article status、Working Memory、Methodology Article CI、Decision Log。

**状态：** 人类明确批准；`MA-FW-001` Framework Approval 完成。

---

## 2026-09-21 — AHICP-D032

**来源：** 人类项目发起人  
**分类：** GOVERNANCE, FORM, PUBLICATION

**决定：**

1. 人类项目发起人明确同意将 **Framework Approval** 解释为对满足严格范围条件的专用 PR 的 **bounded auto-merge authorization**。
2. 该授权只在以下条件全部满足时生效：
   - PR 是为某个已批准 Framework 及其直接同步/治理落地而建立的专用 PR；
   - PR 不包含超出已批准范围的未授权实质性 scope expansion；
   - Framework Approval 后若出现新的实质性修改，这些修改必须已有明确人类授权，或仅属于验证、状态同步、引用/格式修复等非实质性 follow-up；
   - latest-head required CI / validation 全部通过；
   - 不存在 unresolved blocking review / review thread；
   - branch 不落后于目标 base，或已经完成无冲突同步；
   - merge 不绕过 provider-side 必需保护、权限或明确的人类保留门。
3. 满足以上条件时，不需要为了“把同一批已批准内容写入 main”再次请求重复 merge approval。Framework Approval 本身携带该专用 PR 的 scoped merge authorization。
4. 该规则**不**意味着任何 Framework Approval 可以授权同一 PR 中后来混入的无关功能、部署、外部副作用、secret handling、publication/release 或其他未批准 scope。
5. 对当前 PR #26，本次人类确认同时明确批准：
   - `MA-FW-001` 的 Framework scope；
   - Framework Approval 后的直接治理同步；
   - 当前 target-venue review 与本决定本身的记录/状态传播；
   因而 PR #26 在 latest-head diff 不再出现新的未批准实质性 scope、CI 全绿且无 blocking review 时，可按本规则自动 merge。
6. 人类项目发起人同时批准将 **Ethics and Information Technology** 设为当前方法论文章的**第一投稿目标（primary target venue）**。
7. **Science and Engineering Ethics** 保留为当前第二候选。AI & Society 与 Journal of Documentation 不作为当前 primary target，除非其政策适配性后续发生变化或编辑部给出明确可接受反馈。
8. 选择 target venue 不等于 Final Artifact Approval，也不等于 publication/submission authorization。后续仍需完成 venue-specific manuscript preparation、AI-use disclosure、citation/style 核验与最终 Artifact Approval。
9. AHICP-D027–D031 继续有效；本决定新增 merge-authorization semantics 与 target-venue selection，不撤销既有 proposal / authorization / execution / verification / write-back 分离原则。

**受影响组件：** merge governance、Working Memory、Target Venue Review、methodology PR #26、Final Artifact preparation。

**状态：** 人类明确批准。

---

## 2026-09-21 — AHICP-D033

**来源：** 人类项目发起人  
**分类：** FORM, PUBLICATION, GOVERNANCE

**决定：**

1. 人类项目发起人明确同意继续执行 `Ethics and Information Technology` 的 venue-specific Final Artifact preparation。
2. 在不修改 `MA-FW-001` 核心 thesis / scope / approval semantics 的前提下，允许建立独立的投稿派生包，并采用该刊当前官方外部约束：
   - double-anonymous peer review；
   - manuscript content 约 5,000–8,000 words，title / abstract / references 不计入该内容字数；
   - abstract 150–250 words；
   - 4–6 keywords；
   - author-identifying information 从 blinded manuscript 与相关 blinded files 中移除；
   - substantive LLM / generative-AI use 必须在 Methods 或合适替代位置透明披露；不得把本项目真实的 drafting / restructuring / literature organization 等使用缩减描述为 copy editing；
   - original research submission 需要 Data Availability Statement；本稿不报告 empirical dataset / completed experiment，应据实说明；
   - references 使用 author–year 方式并按 venue 规则进行最终一致性核验；
   - Word/docx 是当前主要提交格式，期刊也允许有数学内容时使用 LaTeX；仓库可以先保留 Markdown canonical / submission derivative，再生成最终 docx。
3. canonical bilingual article 继续作为项目 scholarly state；venue-specific blinded manuscript、submission checklist、title-page metadata template、AI-use disclosure 和 cover-letter draft 均属于**派生 submission artifacts**，不得静默替代 canonical article。
4. 当前人类批准的题目继续有效；本轮不另行修改论文核心题目。
5. 双盲匿名化不得通过虚假陈述实现。由于 `AHICP` 名称本身可能指向公开仓库，本轮必须把该问题记录为 **anonymization risk**：先移除直接 GitHub URL、作者身份、内部 Decision IDs / development-status metadata；在正式 submission 前仍需决定是否需要 masked repository、editorial clarification 或其他匿名数据/材料路线。
6. AI-use disclosure 应真实说明 AI 工具参与 iterative drafting、restructuring、literature organization、bilingual synchronization、consistency checking 与 repository-oriented implementation support，同时说明 human author(s) 负责研究方向、核心 Framework、claim boundaries、最终判断、引用核验与最终稿责任。AI 不列为 author。
7. 本决定授权进行 venue-specific formatting、匿名化、非实质性语言精修、引用清理、submission-package 构建与对应验证。
8. 若审阅发现需要改变 `MA-FW-001` 的核心 thesis、主要推论关系、scope 或 contribution boundary，必须返回新的 Working Framework / 必要时创建 `MA-FW-002`；不得以“期刊适配”为理由静默修改批准 Framework。
9. 本决定**不构成 Final Artifact Approval，也不构成 submission / publication / release authorization**。正式提交仍需独立人类批准。
10. 本轮 venue-specific preparation 的 PR 在只包含上述已授权派生准备、状态同步与验证、latest-head CI 全绿、无 blocking review、branch 不落后 base 的条件下，视为已具有 scoped merge authorization；这属于 D029/D032 授权模型下的本次明确人类授权，而不是 publication authorization。

**受影响组件：** Article Form Core、submission derivative package、Working Memory、Decision Log、venue validation。

**状态：** 人类明确批准；venue-specific preparation authorized。
