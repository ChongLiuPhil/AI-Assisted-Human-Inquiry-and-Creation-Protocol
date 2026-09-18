# HARC Working Memory — Work Log
## 工作日志

> **中文 canonical；英文 `work-log.md` 为同步 mirror。**
>
> **主要读者：人类作者。**
>
> 本日志用于回顾项目的发展、阶段性进展与思想/工作路径变化。它不是正常 AI onboarding 的必读文件，也不是长期实质性主张的权威来源。

## 使用规则

- 记录高层项目变化、已表达的理由、里程碑和任务批次；
- 不记录 AI 隐藏 chain-of-thought、scratchpad 或不可验证的内部推理；
- 可由 AI 在重要里程碑、阶段转换、任务批次完成、重大人类决定后定期更新；
- 新 Agent 正常接管时无需完整读取；
- 人类要求回顾、需要审计或追溯变迁时再按需读取。

---

## 2026-09-17 — HARC 独立项目形成

**阶段：** 协议创立。

**进展摘要：**

- 从具体研究项目中抽离出独立 HARC 协作协议；
- 确立 GitHub 作为持久协作基础；
- 建立人类作者基础内容、AI 维护的操作性 framework、派生成果之间的上游—下游关系；
- 建立 Content / Form / Protocol 分流；
- 建立 Framework Approval 与 Final Artifact Approval 的双门结构。

**方向变化：** 项目从“某篇研究中的协作做法”转向“可复用的人机研究协作协议”。

---

## 2026-09-18 — 双语 canonical 治理建立

**进展摘要：**

- 中文被确立为 canonical；
- 英文改为 synchronized mirror；
- 历史英文较新内容先回填中文，再完成 canonical cutover；
- 后续实质性发展固定为 `Human decision -> Chinese canonical -> English mirror`。

**方向变化：** 从双语文件共存转向明确单一语义权威与同步镜像。

---

## 2026-09-18 — 从聊天状态副本转向 Repository-Backed Context

**对应：** HARC-D018–D020。

**进展摘要：**

- 建立 zero-context onboarding；
- 初期曾采用 Active Session Contract 作为第二层会话保险；
- 随后进一步收缩为 Repository Resolver；
- GitHub 被正式定义为 authoritative external memory + working state；
- 模型上下文只作为 transient retrieval cache + control plane。

**方向变化：** 从“仓库 + 会话状态副本”转向“仓库唯一权威，模型按需检索”。

---

## 2026-09-18 — 从 Layer 1.5 转向并行 Working Memory

**对应：** HARC-D021。

**进展摘要：**

- 取消 Critical Clarification 作为独立 Layer 1.5；
- 三个内容层重新明确为 Long-Term Research Memory：
  `Layer 1 -> Layer 2 -> Layer 3`；
- 新增与三层并行的 Working Memory；
- Clarification 成为 Working Memory item；
- 已确认结果通过 Promotion 进入相应长期记忆；
- Working Memory 成为跨 Agent / 人类协作者的 resume index。

**方向变化：** 将“语义层级”与“当前工作状态”彻底分离。

---

## 2026-09-18 — Working Memory 从单文件发展为功能区

**对应：** HARC-D022。

**进展摘要：**

Working Memory 被进一步拆分为三个逻辑功能：

1. Current Focus — 最近期最高优先级目标；
2. Task Plan — 动态任务/计划；
3. Work Log — 面向人类回顾的历史纪要。

原 `docs/working-memory.zh-CN.md` 收缩为 Index / Resolver。

**方向变化：**

从：

`one Working Memory document`

转向：

`Working Memory Area = Index + Current Focus + Task Plan + Work Log`

其中 Work Log 不再占据日常 Agent 上下文，只在需要历史回顾或审计时读取。

**实现完成：**

- Protocol Core / Decision Log / Working Memory Protocol 已同步；
- Manifest / Context Interface 已映射四个逻辑角色；
- START_HERE / AGENTS / Bootstrap / Session Resolver / Onboarding 已同步；
- project templates 已采用相同拆分；
- 方法论文章已加入 C15 / T13 并同步正文；
- Framework Gate / Clarification workflow 已改为读取 Task Plan；
- 双语回归：`120 Markdown = 60 Chinese canonical + 60 English mirror; missing pairs = 0`。

---

## 当前日志边界

本日志目前包含根据 Decision Log 和规范文件回填的高层历史摘要。后续应在阶段性里程碑形成时持续追加，而不是把聊天逐字转录进来。
