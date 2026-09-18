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

**状态：** 已确认，实施中。
