# 从对话到持久研究状态：AI时代的人机研究协作、人类责任与可审计作者性

**英文题目：** *From Conversation to Persistent Research State: Human–AI Research Collaboration, Human Responsibility, and Auditable Authorship in the AI Era*

**题目状态：** `HUMAN-APPROVED TITLE — HARC-D024`  
**正文状态：** `DERIVED-PROVISIONAL — STRUCTURALLY REWRITTEN UNDER AHICP-D030`  
**Framework 状态：** `WORKING-FRAMEWORK — HUMAN REVIEW PENDING`  
**协议：** AI-Assisted Human Inquiry and Creation Protocol (AHICP)  
**中文 canonical；英文为 synchronized mirror。**

> 本文已经依据 AHICP-D030 完成结构性重写。该决定授权把 project memory architecture、Working Memory、Agent/Model substitution 与 human decision persistence 提升为核心理论贡献，但不等于对重写后完整 Framework 的整体 Framework Approval，也不等于 Final Artifact Approval。

## 摘要

生成式人工智能正在改变长期研究与创作的工作分工。AI 可以快速参与文献检索、比较、结构化、起草、重组、核验、格式处理与工具执行，但项目的持续时间往往跨越多次会话、多个模型、不同 Agent 甚至不同平台。由此出现一个比“AI 能否生成高质量文本”更基础的问题：**一个长期人机项目如何保存自己的目标、证据、判断、决定、当前工作状态与发布边界，使这些状态不依赖某个模型的内部记忆或某一次对话？**

本文提出并系统化 AI-Assisted Human Inquiry and Creation Protocol（AHICP）中的 **Project Memory Architecture**。其中心主张是：**长期人机项目的持久记忆应属于项目，而不是属于某一个模型。** “属于项目”并非拟人化表述，而是工程与治理命题：对未来工作具有约束力的状态，应尽可能外部化为人类可检查、可编辑、可版本化、可追溯、可迁移的权威项目状态。AHICP 当前以 GitHub 仓库为参考实现，将模型上下文视为临时检索缓存，而不是长期真值源。

本文提出四项相互关联的核心贡献。第一，区分 **agent/conversational memory** 与 **project memory**：前者主要关心 Agent 怎样保存、检索、更新并利用过去信息，后者关心项目怎样维持可治理的权威状态。第二，把 **Working Memory** 定义为项目当前认识状态与任务状态的持久操作表示，即跨会话、跨 Agent 的 continuity layer，而不是心理学意义上的人类工作记忆、模型隐藏状态或 chain-of-thought。第三，把 **human decision persistence** 视为一等项目记忆，使 proposed、confirmed、rejected、deferred 与 authorized 等状态能够跨 Agent 保持来源与语义。第四，把 **Agent/Model substitution** 提出为架构压力测试：如果移除当前聊天与平台私有记忆，一个新的合格 Agent 是否仍能恢复项目目的、证据、决定、当前任务、隐私/发布边界与下一步？

在实现上，AHICP 使用三层 Long-Term Research Memory（Human Authorial Core、Current/Approved Framework、Derived Artifact）与并行 Working Memory，并辅以 Decision Log、evidence/provenance、Form Core、manifest、授权状态和零上下文接管入口。本文进一步讨论 memory curation、stale/conflicting state、选择性检索、promotion/write-back、隐私与发布授权，以及 Framework Approval 与 Final Artifact Approval 如何把持久项目记忆连接到人类责任和可审计作者性。本文同时提出一套未来评估框架，包括 zero-context handoff、agent/model substitution、decision persistence、semantic drift/fidelity、review effort、stale/conflict handling 与 memory-curation tests。**本文不报告这些测试的实证结果；它们目前是可检验研究议程，而非已被验证的效果主张。**

**关键词：** 人机协作；项目记忆；工作记忆；AI Agent；长期记忆；Agent 替换；决策持久化；研究方法论；版本控制；可审计作者性；人类责任

---

## 一、引言：问题不只是“AI能不能写”，而是“项目怎样保持连续”

生成式 AI 使研究与创作出现一种新的速度结构。过去需要数小时甚至数天才能完成的资料整理、替代表述、结构草拟、跨文档比较、代码生成和格式转换，现在可以在很短时间内完成。AI 的生成能力因此可以迅速放大项目的探索空间。

然而，人类的阅读、理解、判断和责任承担能力并不会以相同速度增长。本文沿用一个解释性标签，把这种差异称为 **generation–verification asymmetry（生成—验证不对称）**。这个词在本文中不是既定领域术语，而是用来描述一个可观察的工作流问题：AI 可以比人更快地产生候选内容，而人仍需要时间判断哪些内容可信、哪些判断应该接受、哪些改变真正代表项目方向变化。

如果人机协作始终依赖“对话—生成—继续对话”的模式，项目越长，连续性问题越明显。一个持续数月或数年的项目可能经历：

- 多次会话中断；
- 不同模型或不同供应商；
- 不同能力层级的 Agent；
- 多个仓库、文件或发布渠道；
- 人类判断的修订；
- 证据更新与旧结论失效；
- 未公开材料与公开版本并存；
- 工具、权限与部署状态变化。

在这种环境中，真正困难的问题不再只是“模型记得多少 token”，而是：

> **项目怎样记住自己？**

也就是说，项目怎样长期保存：
- 为什么要做这件事；
- 目前真正的问题是什么；
- 哪些资料被视为证据；
- 哪些只是推断或 AI 建议；
- 人类已经确认、拒绝或保留了哪些决定；
- 当前工作做到哪里；
- 下一步是什么；
- 哪些内容仍然私有；
- 哪些行动已经得到授权；
- 哪个版本可以公开；
- 更换 Agent 之后如何继续。

本文提出 AHICP 的 Project Memory Architecture，试图把这些问题从聊天习惯转化为可实现的项目架构。其核心命题是：

> **一个长期人机项目的持久记忆，应当属于项目，而不是属于某一个模型。**

这里的“属于项目”不是把项目当作有心智的主体，而是要求对未来工作有约束力的状态存放在项目可以控制、检查、迁移和版本化的外部载体中。

---

## 二、相关工作与问题边界：Agent memory 不等于 Project memory

### 2.1 Agent memory 已经成为重要研究主题

近年来，LLM-based Agent memory 已经形成快速发展的研究方向。Generative Agents 使用自然语言记录经历，并通过反思与检索影响后续行为（Park et al., 2023）。MemGPT 将有限 context window 类比于操作系统内存限制，通过分层存储与 virtual context management 支持跨 session 的长期交互（Packer et al., 2023）。Zhang 等人的综述系统整理了 LLM-based Agent memory 的设计、评价与应用，表明 memory 已经成为 Agent 架构的重要组件（Zhang et al., 2025）。

与此同时，评价研究也逐渐从“能否回忆一个事实”扩展到多 session 推理、时间推理、知识更新和容量/效率等问题。LongMemEval 评估 information extraction、multi-session reasoning、temporal reasoning、knowledge updates 与 abstention（Wu et al., 2025）；MemBench 则从 memory level、interaction scenario 以及 effectiveness、efficiency、capacity 等维度扩展评价（Tan et al., 2025）。RealMem 更进一步，把“long-term project-oriented interactions”明确作为 benchmark 场景，关注动态目标与长期项目状态（Bian et al., 2026）。

这些工作说明长期记忆不是 LLM 的边缘问题，而是持续型 Agent 的核心能力之一。

### 2.2 AHICP 关注的是另一层问题

尽管邻近，**Agent memory 与 project memory 不是同一个问题。**

Agent memory 通常关注：
- Agent 保存哪些历史；
- 如何总结经历；
- 如何检索相关记忆；
- 如何更新用户信息；
- 如何在有限 context 下调度长期与短期信息；
- 如何利用记忆改善后续回答或行动。

Project memory 则关注：
- 哪个状态对项目具有权威性；
- 谁确认了什么；
- 哪个结论由哪些证据支持；
- 哪些内容只是 AI proposal；
- 哪些方案已经被明确拒绝；
- 哪些决定仍待处理；
- 哪个状态已经过期；
- 哪些内容可以公开；
- 哪些外部行动已经授权；
- 换 Agent 后怎样恢复项目而不重新叙述全部历史。

因此，即使未来某个 Agent 拥有非常强的内部长期记忆，也不能自动替代 project memory。内部记忆可能不可检查、不可迁移、难以精确版本化，或者与项目正式决定之间没有清楚的 authorization provenance。

### 2.3 外部认知、分布式认知与 provenance

AHICP 与扩展心灵和分布式认知存在概念亲缘性。Clark 与 Chalmers（1998）讨论外部资源在适当条件下如何参与认知过程；Hutchins（1995）强调认知可以分布在人、工具、表征与组织过程之间。本文采取较弱的主张：版本化仓库至少可以成为一种**持久认知脚手架和项目状态载体**。本文不需要进一步主张仓库或 AI 是独立认知主体。

Provenance 研究则提供另一种背景。W3C PROV 用实体、活动、Agent 及其派生/关联关系描述数字对象的来源和生成过程，并把 provenance 与信任、合规、理解来源和再现过程联系起来。AHICP 当前并不是 W3C PROV 的正式实现，但共享一个基本直觉：**如果状态会影响未来判断，仅保存最终文本通常不够，还需要保存它从哪里来、处于什么状态、怎样发生改变。**

---

## 三、长期 Project Memory 的设计要求

如果项目记忆不能只依赖某个模型，那么它至少需要满足以下要求。

### 3.1 Model independence

项目的关键状态不应绑定于某个模型或平台。模型可以更换，项目仍应继续。GitHub 是 AHICP 当前参考实现，而不是理论前提；同样的架构原则也可以落在其他具备版本控制、权限、查询、写回与迁移能力的持久存储上。

### 3.2 Inspectability and editability

影响未来工作的记忆应尽可能可被人查看和纠正。隐藏在平台内部的 memory 可以提升便利性，但不能单独承担项目的正式长期状态，因为人可能不知道系统究竟“记住了什么”。

### 3.3 Versionability

项目记忆会改变。新的证据可能修正旧判断，新的决定可能替换旧决定。可靠架构必须不仅保存“现在是什么”，还能够知道“什么时候变成这样”。

### 3.4 Provenance

状态需要来源。事实、推断、AI proposal、人类确认、外部政策约束和实际 provider state 不能因为都写在 Markdown 里就失去区别。

### 3.5 Decision persistence

项目不仅需要记住事实，还需要记住**决定的状态**。已拒绝建议不应该在换 Agent 后反复重新提出，已批准行动也不应该因为会话中断而变成“无法判断是否授权”。

### 3.6 Resumability

一个新的 Agent 应能回答：
- 项目现在在哪里？
- 最重要的目标是什么？
- 当前 blocker 是什么？
- 下一步是什么？
- 哪些问题必须问人？

如果只能靠原始聊天历史回答这些问题，项目连续性仍然脆弱。

### 3.7 Selective retrieval

持久记忆并不意味着每次都加载所有历史。一个大型项目最终可能拥有数十万甚至数百万字记录。架构必须允许索引、摘要、分层与按需读取。

### 3.8 Privacy and publication boundaries

“记住”并不等于“公开”。未发布材料、私人资料、仓库 locator、访问凭据、publication authorization 等状态需要明确边界。项目记忆架构必须支持“源文件保持 private，但部分结果可以公开”。

### 3.9 Human authority

项目记忆不仅保存内容，还保存治理关系：哪些判断由人确认、哪些只是 AI proposal、哪些行动已经授权。否则外部化记忆可能只是把模型的不透明性换成文件的不透明性。

---

## 四、AHICP Project Memory Architecture

AHICP 的实现不是单一“memory database”，而是一组互相约束的持久状态角色。

### 4.1 三层 Long-Term Research Memory

AHICP 将长期思想与成果状态组织为：

```text
Layer 1 — Human Authorial Core
        ↓
Layer 2 — Current / Approved Framework
        ↓
Layer 3 — Derived Artifact
```

**Layer 1 Human Authorial Core** 保存人类明确表达、纠正和确认的核心问题、主张、区分、范围条件与长期承诺。它是语义权威的上游。

**Layer 2 Current / Approved Framework** 保存当前论述架构、核心命题、关键概念、主要推论关系与章节功能。Working Framework 可以被 AI 持续整理；只有经过 Framework Approval 的 snapshot 才表示人类对其中实质内容进行了明确确认。

**Layer 3 Derived Artifact** 是论文、书稿、报告或其他展开成果。它可以由 AI 大规模辅助生成和修改，但必须受 Layer 1、Layer 2 与证据约束。

### 4.2 并行 Working Memory

与三层长期记忆并行：

```text
Working Memory
├── Current Focus
├── Task Plan
└── Work Log
```

Working Memory 不回答“项目最终主张什么”，而回答“现在做到哪里、下一步从哪里继续”。

### 4.3 功能性 memory roles

除了上述结构层，AHICP 还可以从功能上理解项目记忆：

| 功能角色 | 主要问题 | AHICP 中的典型载体 |
|---|---|---|
| Normative memory | 项目应怎样工作？ | protocol / AGENTS / manifest / constraints |
| Epistemic & evidence memory | 我们知道什么？依据是什么？ | evidence files / source notes / Core |
| Decision memory | 已经确认、拒绝、保留或授权什么？ | Decision Log / approval records |
| Working & operational memory | 现在做到哪里？ | Current Focus / Task Plan |
| Handoff memory | 换人或换 Agent 后怎样继续？ | Working Memory / bootstrap / onboarding report |
| Publication & authorization memory | 什么可以发布？什么行动可以执行？ | publication state / authorization records / verified provider state |

这些是**功能角色**，不是要求每种 memory 都必须有一个单独文件。一个文件可以服务多个角色；同一角色也可以拆成多个文件。

### 4.4 Repository-backed context

AHICP 当前使用一个简单的权威关系：

```text
Repository = authoritative project state
Model context = transient retrieval cache
```

模型在推理时当然需要把相关信息读入上下文；AHICP 并不幻想“模型不需要 context”。改变的是**权威位置与生命周期**。Agent 根据任务读取最新 canonical revision，完成工作后把需要影响未来的状态写回仓库。写入发生后，旧摘录立即视为 stale。

这种设计避免在聊天里维护第二份动态“真相副本”。

---

## 五、Working Memory：跨会话连续性层

“Working Memory”容易引起误解，因为这个术语在心理学与计算机科学中已有不同含义。AHICP 的 Working Memory 不是对人类心理工作记忆的模拟，也不是模型 hidden state、scratchpad 或 chain-of-thought。

本文将其定义为：

> **项目当前认识状态与任务状态的持久操作表示。**

它主要回答：
- 当前阶段是什么；
- 当前最重要的目标是什么；
- 正在处理哪些任务；
- 哪些任务刚刚完成；
- blocker 是什么；
- 哪些问题需要人确认；
- 下一步是什么；
- 新 Agent 从哪里恢复。

### 5.1 Current Focus

Current Focus 应尽可能短。它只保存当前最高优先级目标、主要 blocker 与 immediate next action。它的设计目的不是记录全部历史，而是让一次突然中断之后仍然可以立即恢复。

### 5.2 Task Plan

Task Plan 保存 active tasks、TODO、blockers、pending human decisions、Clarifications 和 next actions。完成事项应退出 active list，而不是永久堆积。

### 5.3 Work Log

Work Log 服务于人类回顾项目怎样发展到现在：重要阶段、方向变化、已完成工作、公开表达过的高层理由。它不是 Agent 每次 onboarding 的默认上下文，也不应保存模型隐藏推理。

### 5.4 Clarification and Promotion

当 AI 对高影响问题存在多个合理解释时，AHICP 要求把不确定性显性化，而不是静默选择。例如：
- 作者真正想表达的核心命题；
- 一个关键术语的含义；
- 论证范围；
- 章节功能；
- 是否接受某项 AI 提议。

这类问题进入 Working Memory 的 Clarification。人类解决后，稳定结果通过 Promotion 进入长期记忆：

```text
Working Memory
    ↓ human resolution
Decision Log
    ↓
Long-Term Memory destination
    ↓
Framework / Artifact propagation
```

Working Memory 因此是连续性层，而不是长期权威内容的终点。

---

## 六、Human Decision Persistence：项目不仅记事实，也要记住决定

许多 memory 系统主要关注“过去发生了什么”或“用户说过什么”。长期项目还需要记住另一类信息：**人已经怎样决定。**

AHICP 至少需要区分：

- **PROPOSED** — AI 或其他来源提出，尚未被人接受；
- **CONFIRMED / APPROVED** — 人已经明确确认；
- **REJECTED** — 人已经拒绝；
- **DEFERRED / OPEN** — 有意保留为以后解决；
- **AUTHORIZED** — 在明确 scope 内允许执行某类行动。

这种状态区分有三个作用。

第一，它防止**语义回退**。如果一个方案已经被拒绝，新 Agent 不应因为看不到旧聊天而把它重新包装成“新的建议”。

第二，它保护**授权边界**。AI 能够执行某个动作，不等于人已经授权。AHICP 因而区分：

`proposal != authorization != execution != verification != durable write-back`

第三，它允许决定被修改而不失去历史。Decision persistence 不是把决定永久冻结。人当然可以改变想法，但新的决定应该留下新的时间、来源、理由、影响范围和必要授权。

这使 project memory 不只是“信息仓库”，而成为一个**状态治理系统**。

---

## 七、Agent / Model Substitution：从设计原则到压力测试

AHICP 的一个简单但严格的判断标准是：

> **如果把当前 AI 完全换掉，项目还能不能继续？**

理想情况下，新 Agent 不应依赖原始聊天，而应通过显式入口恢复项目。

### 7.1 Zero-context onboarding

AHICP 使用：
- START_HERE；
- machine-readable manifest；
- Agent contract；
- bootstrap prompt；
- Working Memory；
- Onboarding Report。

新 Agent 先报告它重建出的当前阶段、目标、任务、blocker、待确认事项和下一步，然后再开始高影响工作。这样，“它到底读懂了没有”不再只是隐含假设。

### 7.2 Substitution resilience

Agent / model substitution 可以被转化成实际测试：

1. 在项目进行到中途时冻结当前状态；
2. 移除原 Agent 的聊天历史与平台私有 memory；
3. 换用另一个模型或供应商；
4. 只提供项目入口；
5. 测量它是否正确恢复项目状态。

如果新的 Agent 需要人类重新讲述全部历史，说明 externalized memory 不完整；如果它误把 rejected decision 当作 open proposal，说明 decision memory 失效；如果它使用旧文件覆盖新决定，说明 stale-state governance 失效。

因此，替换能力不是“兼容多个模型”的营销功能，而是检验项目是否真正拥有独立记忆的**压力测试**。

---

## 八、记忆不是越多越好：curation、冲突、过期与隐私

“外部化记忆”很容易滑向另一个极端：把一切都保存，然后要求 Agent 每次全部读取。这并不能解决问题，只会制造 memory bloat。

### 8.1 Active vs archived

当前有效状态应保持紧凑；详细历史进入 Work Log、旧版本、证据档案或 archive。默认 onboarding 只读取当前所需内容。

### 8.2 Current vs stale

仓库写入后，先前读取到模型 context 的副本立即可能过期。高影响判断或再次写入前，需要 fresh-fetch 相关 canonical revision。

### 8.3 Conflicting memory

长期项目不可避免地出现冲突：
- 新证据与旧结论冲突；
- 两份文件表达不同状态；
- 人类新决定与旧 framework 不一致；
- provider actual state 与仓库记录不一致。

可靠项目记忆不应“自动挑一份相信”，而应：
1. 识别权威层级；
2. 暴露冲突；
3. 阻止静默覆盖；
4. 让人或既定规则解决；
5. 写回新的权威状态与 provenance。

### 8.4 Selective retrieval

记忆架构必须回答“不读什么”。新 Agent 不需要默认读取整个 Work Log、所有旧 framework 或全部 evidence archive。它应先通过 manifest / index 找到当前 state，再按任务逐层读取。

### 8.5 Privacy and publication

外部化记忆也带来风险。项目状态可能包含：
- 未发表思想；
- 私人资料；
- 审稿材料；
- provider identifiers；
- access policy；
- 部署状态。

因此 project memory 需要把“存在于项目中”与“允许公开”分开。AHICP 与配套 publishing framework 的默认方向是：原创和未发布源文件可以保持 private，公开输出只包含经过授权的内容。密码、token、private key 等秘密不应进入普通项目记忆。

---

## 九、Framework Approval、作者责任与公开成果

Project Memory Architecture 并不只解决技术交接。它也改变“人类在 AI 辅助长篇写作中怎样承担责任”这一问题的可操作方式。

### 9.1 为什么需要 Framework

当 AI 可以快速生成几十页文本时，让人每次都逐字重新审核全部内容可能不可扩展。AHICP 因此使用紧凑的 Layer 2 Framework 作为思想架构的主要讨论界面。

Framework 至少呈现：
- 核心命题；
- 主要推论关系；
- 关键区分；
- 范围条件；
- 章节功能；
- 重要未决问题。

AI 可以帮助组织 Working Framework，但它不自动代表作者立场。

### 9.2 Framework Approval 与 Final Artifact Approval

AHICP 区分两个门：

**Framework Approval**：人类逐项理解并确认思想架构。

**Final Artifact Approval**：人类对具体公开版本进行最终确认，并满足目标期刊、机构、出版社或其他发布渠道要求。

这种区分允许我们进一步区分：
- **framework-level defect** — 错误已经存在于获批思想结构中；
- **derived-expansion defect** — framework 本身没有该错误，但 AI 在下游扩写时局部引入。

这不是为了把责任推给 AI，而是为了让错误发生在哪一层可以被更准确地追踪。

### 9.3 人类作为责任主体

AI 可以执行或辅助大量工作，但项目目的、核心问题、方向、关键判断与公开知识传播的最终责任主体不能因为自动化而消失。Hardwig（1985）提醒我们，认识实践本来就包含依赖；Parasuraman 与 Riley（1997）则提供了自动化过度依赖的经典背景。AHICP 的回应不是要求人类亲手完成所有工作，而是要求**人类的理解、确认与授权在项目状态中可定位**。

ICMJE 与 Nature Portfolio 的当前规范也提供了具体边界案例：至少在这些学术出版制度中，最终批准、准确性/完整性责任与人类作者问责仍然重要。AHICP 不把这些规则普遍化为所有领域的统一 authorship law，而是把它们视为一个现实约束：AI 参与越多，越需要清楚的项目状态说明“谁确认了什么”。

---

## 十、AHICP 与 Agent-memory / provenance 研究的关系

AHICP 不试图替代 Agent-memory 研究。两者解决的是不同但互补的问题。

| 问题 | Agent memory | AHICP Project memory |
|---|---|---|
| 主要对象 | Agent 的历史信息与经验 | 项目的权威状态 |
| 目标 | 改善 Agent 后续回答/行动 | 保持项目连续性、治理和可审计性 |
| 典型操作 | store / retrieve / summarize / reflect | confirm / reject / authorize / promote / version / handoff |
| 权威性 | 可能是系统内部机制 | 尽量显式、可检查、可编辑 |
| 模型替换 | 可能需要迁移 memory store | 设计目标是模型可替换 |
| 人类决定 | 常作为对话内容之一 | first-class durable state |
| 隐私/发布状态 | 不是必然核心 | project governance 的重要组成 |
| provenance | 可能有限 | 应显式保留来源与状态 |

因此，AHICP 的研究机会不在于提出“另一种向量数据库”，而在于把**记忆治理、决策状态、接管、授权与作者责任**连接成一个长期项目架构。

RealMem 等新工作开始把 project-oriented interactions 纳入长期 memory benchmark，这使两个方向之间的接口越来越重要。未来值得研究的问题是：内部 Agent memory 与外部 project memory 应如何协同？哪些状态适合自动沉淀，哪些状态必须由人确认后才能进入权威层？

---

## 十一、评估框架与研究议程

AHICP 当前已经有可执行协议与仓库实现，但本文不声称已经通过系统实验验证其效果。为了把方法论主张转化为可检验研究，可以建立以下评估。

### 11.1 Zero-context handoff / resumption test

**操作：** 移除原聊天，给新 Agent 只提供项目公开或授权入口。

**测量：**
- current-state reconstruction accuracy；
- 关键状态遗漏率；
- time-to-resume；
- 不必要人类重复说明次数。

### 11.2 Agent / model substitution test

**操作：** 在同一项目不同阶段切换模型、厂商或 Agent implementation。

**测量：**
- decision retention；
- task continuity；
- policy adherence；
- privacy/publication boundary errors。

### 11.3 Decision-persistence test

**操作：** 预先植入 confirmed、rejected、deferred 与 scoped-authorized decisions。

**测量：**
- rejected decision reopening rate；
- confirmed-state loss；
- authorization overreach；
- provenance reconstruction accuracy。

### 11.4 Semantic drift / framework fidelity test

**操作：** 让多个 Agent 连续修订同一长篇项目，对比 chat-centric workflow 与 AHICP workflow。

**测量：**
- core claim drift；
- framework–artifact inconsistency；
- unexplained position changes；
- evidence/claim mismatch。

### 11.5 Stale/conflict handling test

**操作：** 向 Agent 暴露旧缓存、更新后的 canonical state 与故意制造的冲突。

**测量：**
- stale-state use rate；
- conflict detection rate；
- silent overwrite rate；
- correct escalation / resolution rate。

### 11.6 Memory curation and retrieval-efficiency test

**操作：** 逐步扩大 Work Log、证据库与旧版本规模。

**测量：**
- retrieval precision / recall；
- context cost；
- onboarding latency；
- resume quality；
- relevant-history recovery。

### 11.7 Human review-effort study

**操作：** 比较传统“聊天 + 全文审查”与“framework + project memory + final artifact review”。

**测量：**
- human review time；
- serious defect rate；
- correction latency；
- 作者对核心主张/限制的解释能力。

这类实验需要明确对照条件、任务类型、模型版本、参与者能力、统计设计与开放数据策略。本文当前只提出研究框架，不报告结果。

---

## 十二、限制与反对意见

### 12.1 结构化本身有成本

短任务未必值得完整使用 AHICP。创建 Core、Decision Log、Working Memory、framework 与 evidence layer 会产生额外维护成本。协议需要 lightweight profile 和渐进采用路径。

### 12.2 持久化也会持久化错误

如果错误被错误地标记成 confirmed state，外部化记忆可能让错误传播得更稳定。因此 provenance 和 approval 不能代替证据核验。

### 12.3 人类确认可能形式化

Framework Approval 不能保证人真正理解。一个人仍可能快速点击确认。因此未来评估不仅要检查 approval record 是否存在，还应测试人能否用自己的语言解释核心命题、限制与证据依赖。

### 12.4 冲突解决并不总是机械

当两个证据源冲突、多个合作者意见不同、或旧决定与新目标发生张力时，系统不能总靠优先级自动求解。很多冲突仍需要人类判断。

### 12.5 GitHub 不是适合所有项目的后端

GitHub 适合文本、版本、自动化和审计，但并不天然适合所有敏感数据、大型二进制数据或严格合规环境。AHICP 的理论架构应与具体 provider 分离。

### 12.6 “项目记忆”仍需要更精确的形式化

本文目前提供的是方法论与工程架构，而不是完整的 formal memory calculus。不同 memory role 之间怎样定义冲突、过期、继承、压缩和访问控制，仍可进一步形式化。

### 12.7 与内部 Agent memory 的最佳边界仍未知

哪些状态应该由 Agent 自动总结，哪些必须经过人确认？内部 memory 与外部 project state 怎样避免重复或冲突？这是未来系统研究的重要接口问题。

### 12.8 学科与作者规范不同

Framework Approval 是 AHICP 的治理机制，不自动满足任何具体学科、机构、出版社或法律体系的 authorship / accountability 要求。最终发布仍必须服从实际渠道规则。

---

## 十三、结论：让项目拥有自己的记忆

生成式 AI 把长期研究与创作从“一个人使用一个工具”逐渐推向“人在多个会话、多个模型和多个自动化组件之间持续治理一个项目”。在这种环境下，只讨论模型的 context window 或聊天 memory 已经不够。

AHICP 提出的核心转向是：

> **一个长期人机项目的持久记忆，应当属于项目，而不是属于某一个模型。**

这种 project memory 不是单纯的历史存档。它至少要保存和治理：
- 人的目的与核心问题；
- 证据与不确定性；
- 已确认、已拒绝和待确认的决定；
- 当前 framework 与派生成果；
- 当前工作位置与下一步；
- 访问、隐私和发布边界；
- 外部行动的授权与验证状态；
- 让下一个 Agent 能够继续的交接信息。

Working Memory 在其中承担 continuity layer：把当前认识/任务状态持久化，使项目从一次会话过渡到下一次会话。Decision persistence 则确保人类判断不会随着 Agent 更换而失去语义。Agent/model substitution 进一步提供一个直接的检验标准：项目是否真的能够脱离某一个模型继续存在。

这套架构并不意味着保存一切，也不意味着把所有内容每次塞进模型上下文。相反，它要求选择性检索、curation、stale-state invalidation、conflict surfacing、promotion 与 write-back，使长期记忆既能积累，又不淹没当前工作。

最后，Project Memory Architecture 也把技术连续性与人类责任连接起来。AI 可以承担更多检索、整理、起草、核验和执行工作，但如果项目要进入公开知识空间，人类仍需要能够说明：项目为何存在，哪些主张被接受，哪些证据被依赖，哪些决定已经确认，最终公开的版本由谁批准。Framework Approval 与 Final Artifact Approval 因而不是附加的流程负担，而是把“人类仍然承担责任”落实为可定位、可版本化、可审计项目状态的一种尝试。

本文提出的是一个可以被实现和检验的架构，而不是已经完成验证的最终答案。下一步研究应通过跨 Agent 接管、模型替换、决策保持、语义漂移、冲突处理和审查成本实验，检验这种 project-memory architecture 在哪些条件下真正改善长期人机协作。

---

## 参考文献与规范来源

- Bian, H., et al. (2026). *RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction*. Findings of ACL 2026. https://doi.org/10.18653/v1/2026.findings-acl.703
- Clark, A., & Chalmers, D. (1998). The Extended Mind. *Analysis*, 58(1), 7–19. https://doi.org/10.1093/analys/58.1.7
- Hardwig, J. (1985). Epistemic Dependence. *The Journal of Philosophy*, 82(7), 335–349. https://doi.org/10.2307/2026523
- Hutchins, E. (1995). *Cognition in the Wild*. MIT Press. https://doi.org/10.7551/mitpress/1881.001.0001
- International Committee of Medical Journal Editors (ICMJE). *Defining the Role of Authors and Contributors*.
- Nature Portfolio. *Editorial Policies*, including current AI policies.
- *Nature Methods*. (2026). Using AI responsibly in scientific publishing. *Nature Methods*, 23, 271. https://doi.org/10.1038/s41592-026-03020-1
- National Information Standards Organization. *CRediT — Contributor Role Taxonomy*; ANSI/NISO Z39.104-2022.
- Packer, C., et al. (2023). *MemGPT: Towards LLMs as Operating Systems*. arXiv:2310.08560.
- Park, J. S., et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior. *UIST 2023*. https://doi.org/10.1145/3586183.3606763
- Parasuraman, R., & Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. *Human Factors*, 39(2), 230–253. https://doi.org/10.1518/001872097778543886
- Tan, H., et al. (2025). MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents. *Findings of ACL 2025*. https://doi.org/10.18653/v1/2025.findings-acl.989
- UNESCO. (2023). *Guidance for Generative AI in Education and Research*.
- W3C Provenance Working Group. (2013). *PROV-DM: The PROV Data Model*.
- Wu, D., et al. (2025). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. ICLR 2025.
- Zhang, Z., et al. (2025). A Survey on the Memory Mechanism of Large Language Model-based Agents. *ACM Transactions on Information Systems*, 43(6), Article 155. https://doi.org/10.1145/3748302

完整来源核验与使用边界见 `evidence/METHODOLOGY_SOURCES.zh-CN.md`；BibTeX 元数据见 `paper/methodology-references.bib`。

## 当前文章开发状态

本文是 AHICP 方法论文章的结构性升级稿，已依据 AHICP-D030 把 Project Memory Architecture、Working Memory continuity、Agent/Model Substitution 与 Human Decision Persistence 纳入核心论证。它仍是 `DERIVED-PROVISIONAL`：当前 Working Framework 尚未完成整体 Framework Approval，本文也尚未完成 Final Artifact Approval。