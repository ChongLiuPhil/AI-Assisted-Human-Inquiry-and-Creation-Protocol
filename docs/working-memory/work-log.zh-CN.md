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
- Protocol Core / Framework Approval / Specification / 根 Agent Contract / README / research-project templates 完成中英文同步；
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

## 2026-09-18 — HARC-D024 — 题目批准与“人类作为责任主体”的精确化

**对应：** HARC-D024；进一步精确化 HARC-D023。

**人类决定摘要：**

- 中文题目《从对话到持久研究状态：AI时代的人机研究协作、人类责任与可审计作者性》获得明确认可；
- 题目认可只属于 title/form-content 决定，不等于完整 Working Framework 已获 Framework Approval；
- “人类责任 / human responsibility” 不作为无需说明的独立中心概念；
- 更精确的核心命题是：在人机协作的研究与探究中，人类保持为责任主体／责任承担者；
- 当研究结果、论证或知识主张进入公开传播时，这一责任主体要求尤其重要；
- AI 可以作为工具分担大量工作，但不能成为研究目的、核心判断、framework 授权或公开知识传播的最终责任主体；
- HARC-D023 的其他决定继续有效。

**传播结果：**

- Decision Log 新增 HARC-D024；
- Article Form Core 记录 human-approved title；
- Article Content Core 新增/强化责任主体与公开知识传播要求；
- Working Argument Map 的标题状态、中心问题、T3 / T4、核心区分与 Section VI 已同步；
- 方法论正文摘要、第六节、结论与关键词已同步；
- Protocol Core、Framework Approval、Specification、README、根/模板 Agent Contract 与 research-project template 已同步；
- Framework Approval 文件尾部遗留的旧责任模型重复段落已删除；
- Working Memory 与 Framework Status 已明确：title approved，但 overall Framework Approval 仍未完成。

**当前状态：**

`PASS FOR HUMAN FRAMEWORK REVIEW` 保持不变；`MA-FW-001` 尚未创建。

---

## 2026-09-18 — HARC-D025 — Framework 依赖修复与未决项批准语义

**对应：** HARC-D025。

**人类确认：**

- 修复方法论 Working Framework 的 T1–T13 依赖图，使后加入的 Working Memory、zero-context onboarding、repository-backed context 等命题进入正确的治理/实现关系；
- 将 T3 dependency label 同步为“AI 工具工作分担 / 人类责任主体”；
- 明确整体 Framework Approval 可以包含显式 unresolved / AI-PROPOSED / NON-BLOCKING 项目，但批准的是它们作为未决项目的架构位置、范围和处理方式，不是其尚未确认的实质内容；
- 未决 AI 提议不会因整体 Framework Approval 自动 Promotion 为人类观点；
- 本次确认不等于整体 Framework Approval，不创建 `MA-FW-001`。

**执行结果：**

- Working Argument Map 中英文 dependency graph 已修复；
- Framework Approval protocol 已加入未决项批准语义；
- Framework Status、Current Focus、Task Plan 已同步；
- 当前 gate 仍为 `WAITING-HUMAN: overall Framework Approval decision`。

---

## 当前日志边界

本日志目前包含根据 Decision Log 和规范文件回填的高层历史摘要。后续应在阶段性里程碑形成时持续追加，而不是把聊天逐字转录进来。

---

## 2026-09-18 — 仓库级协作架构审计：从“规则完整”转向“复杂度治理”

**性质：** PROTOCOL 路径下的 AI 维护审计；不产生新的 Human Protocol Decision。

**本轮检查范围：**

- 根目录 zero-context 启动入口；
- Manifest / Context Interface 控制面；
- AGENTS / README / Onboarding Handshake；
- Working Memory；
- 方法论文章治理入口；
- 双语同步；
- 历史 audit/self-test；
- reusable project template；
- open-source release readiness。

**发现并直接修复的同步问题：**

- README 复制了一套会漂移的 onboarding read order；已改为只指向 START_HERE / Manifest 的 authoritative routing；
- README 复制了已经过时的 live Clarification Gate 状态；已改为只指向 Framework Status / Current Focus / Task Plan；
- ONBOARDING_SELF_TEST 仍展示测试时的旧 blockers，容易被误读为 live state；已明确标记为 historical snapshot / live state superseded，并要求未来 self-test 记录 tested revision。

**AI-PROPOSED、尚待人类决定的架构升级：**

已写入 Task Plan 的 `WM-PROP-001..008`，包括：

- 轻量化 onboarding；
- Manifest / Context Interface 控制面职责分离与版本兼容；
- 静态导航 / 动态状态彻底解耦；
- Decision Log 可扩展索引；
- 双语同步自动化；
- 正式开放发布基础设施；
- machine-verifiable conformance；
- 模板去复制化。

**总体判断：**

HARC 当前主要问题不再是缺少治理规则，而是治理资产数量快速增长后产生的入口复杂度、重复状态、手工同步成本与 stale-state 风险。下一阶段应优先做 complexity governance，而不是继续增加平行说明文件。

**规范状态：**

上述架构升级仍为 `AI-PROPOSED`。除同步修复外，没有把任何新架构建议 Promotion 到 Protocol Core / Decision Log。


---

## 2026-09-19 — AHICP v0.3 语义迁移：控制面、模板与结构验证

本轮完成：
- 依据 `AHICP-D026` 迁移 Protocol Core、live protocol 文件、Architecture、Roadmap 与 Working Memory；
- 建立 `AHICP_MANIFEST.yaml` / `AHICP_CONTEXT_INTERFACE.yaml`，旧 `HARC_*` 文件降为 compatibility pointer；
- 把 `templates/research-project/` 迁移到 AHICP 控制面，同时明确其为 research specialization；
- 建立 Phase C semantic audit 与 v0.3 migration validation record；
- manifest 路径检查：33 个候选，缺失 0；
- 双语物理配对检查：62 个中文文件，缺失英文 mirror 0；
- zero-context 入口链检查通过，未发现 live 旧控制文件引用。

仍待完成：
- 方法论文章/evidence 中 historical HARC 与 current AHICP 语义区分；
- 关键规范文件的语义级双语 parity；
- 独立 post-migration repair audit。

PPF 方面已另行建立第一套 Quarto + GitHub Actions + Cloudflare Workers Static Assets reference implementation PR；未把 PPF publishing lifecycle 规则复制进 AHICP。
