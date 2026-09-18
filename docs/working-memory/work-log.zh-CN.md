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

## 2026-09-18 — 当前全讨论覆盖复核

**性质：** 一轮完整的 `审查 -> 修复 -> 验证`。

**复核结果：**

- 三层 Long-Term Research Memory、并行 Working Memory、Current Focus / Task Plan / Work Log 均已落实；
- Clarification / Promotion、Repository-Backed Context、zero-context onboarding、双语 canonical/mirror、Framework/Final Approval、form inheritance、方法论文章自托管等已形成规范与执行入口；
- 未发现新的核心架构缺失。

**本轮实际修复：**

- 根 START_HERE / AGENTS 英文 mirror 的旧 Clarification Register 与旧读取顺序；
- project-template START_HERE 的编号回归和旧 Clarification 路由；
- project-template AGENTS 的 legacy clarification-register active-state 用法；
- English Onboarding Handshake；
- Bootstrap Prompt / Persistent Memory 中少量旧表述；
- Founding Idea Audit 自身过时的双语迁移状态；
- 最终终审已记录、但 Task Plan 未单列的“目标发布渠道与渠道特定形式约束”，现补为 `CLR-010`。

**结论：** `PASS AFTER REPAIR`。

**仍需人类决定：** 方法论文章 `CLR-001 / CLR-002 / CLR-005`；formal release 前 `CLR-009` license。

---

---

## 2026-09-18 — HARC-D023 — 人类目的、AI 工具地位与 Framework 责任模型

**对应：** HARC-D023；CLR-001 / CLR-002 / CLR-005。

**人类决定摘要：**

- 研究或创作项目的目的、核心问题与方向由人类发起、给予并持续导航/批准；最终成果的核心责任由人类承担；
- AI Agent 在 HARC 中作为协作工具，可以执行或辅助大量具体工作，但不应被描述为具有认知性的主体，也不使用“AI 承担认知劳动 / 认知任务”作为规范性中心概念；
- 对长篇成果，Layer 2 Current / Approved Framework 成为人类核心思想责任的主要结构性承载点；
- Framework Approval 要求人类对 framework 中实际呈现的全部实质内容形成清晰理解、逐项认真审核并明确确认，包括核心命题、推论关系、关键区分、范围条件、章节/小节功能及被纳入 framework 的具体措辞；
- `responsibility concentration` 不再作为当前中心术语；
- “未来可把 Approved Framework 作为学术人机协作附件提交”仅保留为可能发展方向，不是当前强制协议要求。

**本轮 Promotion / 传播：**

- Decision Log 新增 `HARC-D023`；
- Protocol Core / Specification / README / research-project templates 完成中英文同步；
- Article Content Core 完成 Layer 1 Promotion；
- Working Argument Map 的 T3 / T4、核心区分、依赖关系与 clarification 状态完成 Layer 2 更新；
- 方法论正文摘要、第六节和结论完成定向 Layer 3 同步；全文仍保持 `DERIVED-PROVISIONAL`，未提前执行大规模结构重写；
- Task Plan 将 `CLR-001 / CLR-002 / CLR-005` 退出 active blocking state，并保留 `RESOLVED / PROMOTED` 指针。

**Framework readiness review：**

`PASS FOR HUMAN FRAMEWORK REVIEW`

此前 blocking clarification gate 已清除。当前没有 active blocking clarification 阻止整体 Framework Approval 审阅。

**尚未发生：**

- 尚未创建 `MA-FW-001`；
- 尚未完成整体 Framework Approval；
- 尚未执行全文 15 部分 -> 10 部分的结构性重写。

**下一阶段：**

人类整体审阅 `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`，并明确作出 `APPROVE / REVISE / REJECT` 决定。

---

## 当前日志边界

本日志目前包含根据 Decision Log 和规范文件回填的高层历史摘要。后续应在阶段性里程碑形成时持续追加，而不是把聊天逐字转录进来。
