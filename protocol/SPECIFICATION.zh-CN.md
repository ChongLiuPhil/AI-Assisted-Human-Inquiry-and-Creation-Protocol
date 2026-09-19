# AHICP 协议规范

**AI-Assisted Human Inquiry and Creation Protocol（AI 辅助人类探究与创作协议）**

**版本：** 0.3.0-draft  
**范围：** 以 GitHub 为中心，在人类主导下，由一个或多个 AI Agent 辅助持续的探究、研究、推理、写作与创作工作。

> **本中文版本是规范性基准；英文 `SPECIFICATION.md` 是同步镜像。**

---

## 1. 目的

AHICP 定义一种持久、可审计、以人为主导的工作协议，用于组织 AI 对人的探究、研究、推理、写作与创作的辅助，包括检索、结构化、提出方案、起草、修订、核验、转换与项目状态维护。

协议旨在保存：

- 人类思想能动性；
- 语义连续性；
- 重要决定的显式来源；
- 人类意图与 AI 提议之间的区分；
- 内容与形式之间的区分；
- 可检查的论证结构；
- 受证据约束的可纠错性；
- 可扩展的项目记忆；
- 跨 Agent 连续性；
- 显式批准状态；
- 有意义的人类目的设定、理解、判断、确认与责任。

AHICP v0.3 的当前参考实现假定 GitHub 是持久仓库基础设施。未来实现可以把相同逻辑角色映射到其他系统。

---

## 2. 规范性术语

- **MUST（必须）** — AHICP 合规所要求。
- **SHOULD（应当）** — 强烈推荐，除非项目记录了偏离理由。
- **MAY（可以）** — 可选。

---

## 3. 核心原则

长期探究、研究或创作项目**不得**把一次临时 AI 对话当作唯一持久状态。

> **聊天是交互界面；仓库才是持久的共享项目记忆。**

重要项目状态必须外部化到显式、受版本控制的仓库成果中。

---

## 4. 角色

### 4.1 人类作者

人类作者提供、修订或确认实质性思想承诺与呈现意图。

研究或创作项目的目的、核心问题与方向必须由人类作者发起、给予或明确批准。

在 AHICP 中，人类作者不仅是内容授权者，也必须保持为**责任主体／责任承担者**。这一点适用于研究与探究过程，并在研究结果、论证或知识主张进入公开传播时尤其重要。

人类作者可以让 AI Agent 作为工具执行或辅助大量检索、综合、结构化、起草、编辑、形式化、检查与格式处理工作。此类工作分担不得被理解为项目目的、核心判断、framework 授权、公开知识传播责任或最终责任主体位置的转移.

### 4.2 AI Agent

AI Agent 是协作工具。规范性描述不应把 AI 表述为具有认知性的主体，也不应把“AI 承担认知劳动 / 认知任务”作为协议术语；应具体说明 AI 执行或辅助的工作。

AI Agent 可以：

- 抽取并规范化人类决定；
- 维护仓库状态；
- 提出论证、反对意见、区分、例子、术语与结构；
- 在工具允许时开展研究与证据核验；
- 维护操作性论证表示；
- 把已批准结构扩写成文本或其他成果；
- 检测不一致、证据冲突和同步缺陷；
- 维护格式与渲染系统。

AI Agent 必须区分自己的提议与经人类批准的承诺，并且不得被视为研究目的、framework 授权或公开知识传播的最终责任主体.

### 4.3 仓库

仓库是人类作者与 AI Agent 之间的持久共享状态。

它必须保存足够的当前状态与历史状态，使新的、能力合格的 AI Agent 可以在没有原始聊天历史的情况下重建项目。

---

## 5. 规范状态模型

### 5.1 Content Core — `core/CONTENT_CORE.zh-CN.md`

Content Core 包含人类作者当前有效的实质性承诺。

它应记录：

- 项目目的；
- 中心问题；
- 当前主张；
- 暂定主张；
- 核心区分；
- 范围限制；
- 明确尚未解决的作者问题。

它不得静默包含尚未被接受的 AI 提议。

### 5.2 Form Core — `core/FORM_CORE.zh-CN.md`

Form Core 包含有关“成果作为一个被表达对象”的当前人类决定。

它可以包括：

- 成果类型；
- 语言与文体；
- 字体；
- 页面版式；
- 标题层级；
- 脚注；
- 引用呈现；
- 表格和图示；
- 视觉系统；
- 可复用作者偏好；
- 外部发布渠道约束。

未知形式决定必须保持显式未知，不得从 AI 默认值中推断。

### 5.3 Decision Log — `core/DECISION_LOG.zh-CN.md`

Decision Log 是重要人类决定的历史审计轨迹。

每个条目应包括：标识符、日期、来源、分类、决定、受影响文件/层、被取代的旧决定（如有）以及实现状态。

当前 Core 可以重写以反映当前有效状态；Decision Log 保存历史连续性。

### 5.4 Working Memory Area

Working Memory 与三层 Long-Term Project Memory 并行，并且规范的是**逻辑功能**而非固定单文件。

项目 MUST 提供或等价实现以下逻辑角色：

- **Working Memory Index / Resolver** — 映射各组件；
- **Current Focus** — 最近期最高优先级目标、当前阶段、primary blocker、immediate next action；
- **Task Plan** — active tasks、next actions、TODO/backlog、blockers、pending human decisions、Clarifications、sync defects；
- **Work Log** — 主要供人类回顾的阶段性历史纪要。

项目 MAY 把多个角色映射到同一文件，也 MAY 拆成多个文件。Manifest MUST 显式记录实际映射。

Clarification 是 Task Plan / Working Memory 中的一种 item type。高影响不确定性如果可能改变核心命题、关键概念、范围、主要推论关系、章节功能、关键术语/翻译或 Framework Approval，则 MUST 创建 Clarification item，而不能由 AI 静默猜测。

未解决 Clarification MUST NOT 被视为人类承诺。

人类解决后：

`Working Memory -> human resolution -> Decision Log -> appropriate Long-Term Memory destination`

涉及人类核心内容时：

`Layer 1 Core -> Layer 2 Framework -> Layer 3 Artifact`

任务完成后应退出 Task Plan active list，并将高层历史摘要写入 Work Log；如果形成稳定规范结果，同时执行 Promotion。

Work Log MUST NOT 保存 AI 隐藏 chain-of-thought / scratchpad，MUST NOT 替代当前状态，并 SHOULD NOT 默认进入新 Agent onboarding 上下文。

完整规则见 `protocol/WORKING_MEMORY.zh-CN.md`。

### 5.5 Working Argument Map — `docs/argument-map.zh-CN.md`

Working Argument Map 是长篇思想结构的主要操作性讨论界面。

它通常由 AI 维护，并且在人类批准之前必须被视为可变。

它应暴露：

- 中心问题 / 项目问题；
- 当前命题集合；
- 概念词汇；
- 前提/支持性主张；
- 论证依赖关系；
- 章节/小节架构；
- 关键“不推出关系”；
- 反对意见；
- 证据依赖；
- 等待人类决定的问题；
- 等待人类回应的 AI 提议；
- 同步状态。

它应明显短于完整成果。

### 5.6 Approved Framework Snapshot — `docs/frameworks/FW-xxx.zh-CN.md`

只有在人类明确审阅并确认后，才能创建 Approved Framework Snapshot。

Framework Approval 要求人类作者清楚理解、逐项审核并明确确认拟批准 framework 中实际呈现的全部实质内容，包括核心命题、推论关系、关键区分、范围条件、章节/小节功能，以及被纳入 framework 的具体措辞。AI 可以辅助形成该表示，但不能代替人类对项目方向与思想架构的授权。

已批准快照不得被静默修改。

实质性思想变化必须产生新的 framework 版本。

### 5.7 Framework Status — `docs/framework-status.zh-CN.md`

该文件应说明：

- 当前 Working Framework 状态；
- 最新 Approved Framework 标识符；
- 当前成果状态；
- 尚未解决的同步缺陷；
- Final Artifact Approval 状态。

### 5.8 Evidence Layer — `evidence/`

证据文件可以包括文献笔记、来源核验、数据集、计算、形式推导、经验 notebook 与来源清单。

证据约束可以负责任地主张什么，但不得静默改写人类意图。

### 5.9 派生成果

论文、书籍、文章、报告、演示文稿或其他输出属于派生表达。

它必须与下列内容保持兼容：

- 当前 Content Core；
- 最新适用的 Approved Framework；
- Form Core；
- 已知证据约束。

如果派生成果进入公开传播，项目必须保留可识别的人类责任主体。AI 的生成、扩写或编辑参与不得消除或替代这一责任主体要求.

---

---

## 6. 人类反馈路由

在持久化实质性人类反馈之前，AI Agent 必须把它归为以下一个或多个类别：

### `CONTENT`

改变作品论证什么、意味着什么、假设什么、区分什么、质疑什么或得出什么结论。

传播路径：

`人类决定 -> Decision Log -> Content Core -> Working Argument Map -> 派生成果`

### `FORM`

改变成果如何被表达或渲染，例如成果类型、字体、版式、视觉系统、引用呈现、文体等。

传播路径：

`人类决定 -> Decision Log -> Form Core -> 渲染/实现 -> 成果`

### `PROTOCOL`

改变协作、持久化、交接、同步、批准或版本控制如何运作。

传播路径：

`人类决定 -> Decision Log -> 协议/治理 -> Agent 行为`

必须支持多标签反馈。

---

## 7. 上游优先更新规则

不得把下游层的变化当作人类已经批准上游变化的证据。

### 7.1 Content 更新循环

1. 识别人类决定；
2. 记录到 Decision Log；
3. 校准 Content Core；
4. 校准 Working Argument Map；
5. 判断既有 Approved Framework 是否仍然有效；
6. 检查证据/逻辑冲突；
7. 传播到派生成果；
8. 验证同步。

### 7.2 Form 更新循环

1. 识别人类形式决定；
2. 记录决定；
3. 校准 Form Core；
4. 仅在人类明确表示跨项目适用时更新可复用风格 profile；
5. 传播到实现；
6. 验证渲染。

### 7.3 Protocol 更新循环

1. 记录工作流决定；
2. 更新协议/治理文档；
3. 在适当情况下更新可复用模板；
4. 验证新 Agent 是否能发现新规则；
5. 不得仅仅因为治理规则变化而改变项目实质内容。

---

## 8. 提议与来源状态

在来源歧义会产生影响时，项目应区分：

### Content 状态

- `AUTHOR-ACTIVE`
- `AUTHOR-TENTATIVE`
- `AI-PROPOSED`
- `EVIDENCE-CONSTRAINT`
- `UNRESOLVED`

### Form 状态

- `AUTHOR-PREFERENCE`
- `REUSABLE-AUTHOR-PREFERENCE`
- `PROJECT-SPECIFIC`
- `EXTERNAL-CONSTRAINT`
- `TEMPORARY-DEFAULT`
- `UNRESOLVED`

AI 选择不得静默升级为人类作者状态。

---

## 9. Framework Approval Gate

在长篇成果被视为具有稳定思想基线之前，人类作者应审阅一个紧凑 framework。

Framework 应说明：

- 中心问题；
- 命题集合；
- 主要概念；
- 关键推论关系；
- 章节/小节角色；
- 重要限制；
- 有意保留的未决问题；
- 对论证实质重要的已知证据冲突。

人类明确批准后，Agent 必须：

1. 创建不可变的版本化快照；
2. 在 Decision Log 记录批准；
3. 更新 Framework Status；
4. 把该快照作为已批准思想基线。

---

## 10. Framework 忠实性与责任

Framework Approval 后，AI Agent 可以大量扩写作品。

未经重新向上游提交人类审阅，派生成果不得实质性偏离 Approved Framework。

实质性偏离包括：改变中心命题、新增重大结论、移除关键前提、改变主要主张之间的关系、以改变论证的方式改变范围，或重新组织成果以至于已批准推理不能被准确表示。

AHICP 区分：

- **framework-level defect** — 已经存在于人类批准思想架构中的缺陷；
- **derived-expansion defect** — 只在后续 AI 扩写或实现中引入的局部问题。

这种区分提高可追溯性，但不取消最终发布的问责要求。

---

## 11. Overview Projection

Approved Framework 应能从成果面向读者的总览中恢复。

默认映射：

- `ACADEMIC_PAPER`：摘要 + 引言；
- `ARTICLE`：开篇/导论性总览；
- `BOOK`：导论/总览章节 + 章节路线图；
- `REPORT`：执行摘要 + 结构/方法总览；
- 其他类型：由 Form Core 指定的类似高层总览。

总览不需要逐字复制 framework，但必须忠实表示它。

---

## 12. Final Artifact Approval Gate

Framework Approval 与 Final Artifact Approval 是不同的。

AI Agent 持续进行扩写、编辑、研究整合与格式处理时，成果可以保持 `DERIVED-PROVISIONAL`。

在以人类作者名义正式投稿、出版或公开发布之前，人类作者应按照相关学科、发布渠道、机构或作者标准的要求完成最终审阅。

推荐成果状态：

- `DERIVED-PROVISIONAL`
- `FINAL-REVIEW`
- `FINAL-APPROVED`

---

## 13. 证据冲突协议

如果可靠证据或形式推理与当前人类内容冲突：

1. 在人类修订前保留当前人类意图；
2. 显式标记冲突；
3. 区分证据、推论、不确定性与解释；
4. 不得隐瞒冲突；
5. 不得明知会误导仍向下游传播；
6. 必要时请求或等待人类解决；
7. 记录最终决定。

---

## 14. AI 工作分担与人类认识责任

AHICP 区分**AI 可以执行或辅助的工作分担**与**人类不能转移的认识判断和责任**。

AI 可以进行大量检索、综合、结构化、起草、形式化、一致性检查、修订和格式处理。

人类注意力应集中在高杠杆决定上，包括：

- 项目目的、研究目标与核心问题；
- 核心承诺；
- 主要推论架构；
- 对重要 AI 提议的接受/拒绝；
- 关键证据冲突的处理；
- Framework Approval；
- 在需要时完成 Final Artifact Approval。

AHICP 不主张文件结构本身能保证良好判断。批准机制是治理支架，不是人类能力与理解的替代物。

---

## 15. 持久记忆与上下文限制

AHICP 提供的是持久项目记忆，而不是字面意义上的无限模型上下文。

项目应通过以下方式扩展：

- 紧凑的当前 Core；
- 紧凑的操作性 map；
- 时间顺序日志；
- 建立索引的证据；
- 归档的历史细节；
- 选择性检索。

目标是**可恢复与可追溯**，而不是同时加载全部历史。

---

## 16. Agent 交接

### 16.1 Zero-context Bootstrap

项目 SHOULD 在根目录提供：

- `START_HERE.zh-CN.md` / English mirror；
- `BOOTSTRAP_PROMPT.zh-CN.md` / English mirror；
- `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` / English mirror；
- `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` / English mirror；
- `AHICP_MANIFEST.yaml`；
- `AHICP_CONTEXT_INTERFACE.yaml` 或等价机器可读 context policy；
- 根 `AGENTS.zh-CN.md` / English mirror；
- 一个可发现的 Onboarding Handshake 规范。

新的 AI Agent 在实质性工作前 MUST 按启动入口读取 control plane、Working Memory Index、Current Focus 与 Task Plan，并 SHOULD 先输出 AHICP Onboarding Report，说明当前最高优先级目标、primary blocker、immediate next action、active tasks、next actions、blockers、pending human decisions / clarifications、Framework/Artifact 状态、同步缺陷与当前允许的下一步。Work Log 默认不读取。Onboarding Report MUST 确认 `AHICP REPOSITORY CONTEXT — ACTIVE`。该确认只加载访问内核；Blocking Clarifications、Framework、Artifact 与 Core 等动态状态仍必须在后续任务中从 GitHub 最新 canonical revision 按需读取。

如果 Agent 无法从仓库完成该报告，项目存在 onboarding/persistence defect。

### 16.2 常规接管读取

新的 AI Agent 至少应通过阅读以下内容继续正常项目工作：

1. `START_HERE.zh-CN.md`、`AHICP_MANIFEST.yaml` 与 `AHICP_CONTEXT_INTERFACE.yaml`；
2. 项目 `AGENTS.zh-CN.md`；
3. Working Memory Index；
4. Current Focus；
5. Task Plan；
6. 当前任务相关的 Layer 1 Core / Decision Log；
7. 当前任务相关的 Layer 2 Framework Status / Working or Approved Framework；
8. 当前任务相关的 Layer 3 Artifact；
9. 当前相关 Evidence。

Work Log 仅在人类要求历史回顾、专门审计、变迁重建或 current/history conflict 时按需读取。

项目应记录所采用的 AHICP version/tag/commit，避免把后续上游协议变化静默视为已经接受的治理规则。

### 16.3 Repository-Backed Context

项目 SHOULD 使用 `AHICP_CONTEXT_INTERFACE.yaml` 或等价机制规定：

- GitHub 是唯一权威项目状态源；
- 模型上下文只是非权威临时缓存；
- 根据 CONTENT / FORM / PROTOCOL 任务选择性读取；
- 高影响判断前重新读取相关最新状态；
- 写入前确认最新 revision；
- 写入后使旧缓存失效；
- 所有持久更新 write-through 到 repository；
- Issue、PR comment、Discussion 等默认不属于规范权威状态。

完整规则见 `protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md`。

如果关键约束只存在于不可访问聊天或隐藏记忆中，项目在这些约束被外部化前属于不合规。

---

## 17. Form Profile 继承

可复用呈现状态应能够区分：

1. 可复用的作者级偏好；
2. `BOOK`、`ACADEMIC_PAPER`、`ARTICLE` 等成果类型 profile；
3. 项目特有的 Form Core 决定；
4. 外部发布渠道约束；
5. AI/工具临时默认值。

继承不得把未陈述偏好转化成人类作者偏好。

---

## 18. 同步不变量

在稳定检查点，应同时满足：

1. 成果主要主张与 Content Core 兼容；
2. 当前思想架构由 Working Argument Map 表示；
3. 存在 Approved Framework 时，派生内容忠实于它，或明确标记为不同步；
4. 重要呈现选择与 Form Core 兼容，或明确标为临时/外部；
5. 重要人类决定出现在 Decision Log；
6. 尚未接受的 AI 提议仍明确保持未接受；
7. 已知证据冲突可见；
8. 重要决定没有只滞留在聊天历史中；
9. 接管文档指向当前规范文件。
10. Current Focus 显式给出当前最高优先级目标与 immediate next action。
11. 所有当前 blocker、pending human decision 与 Clarification 都在 Task Plan 中显式可见，而不是只存在于聊天或 AI 私下判断。
12. 已完成任务退出 active Task Plan，并在适当粒度写入 Work Log。
13. Working Memory 的已解决稳定结果已经 Promotion 到对应长期记忆，且 Work Log 不继续充当规范答案。

任一条件失败都构成显式同步缺陷。

---

## 19. 多轮审计与修复纪律

要求的多轮审计必须被解释为重复的审查—修复循环。

每一轮应执行：

`审查 -> 识别缺陷 -> 修复/实现 -> 验证修复`

如果要求三轮，就执行三次这种循环。如果要求修复后审计，则在三轮结束后再进行一轮独立审计，不能把三轮之一算作最终审计。

审计记录应说明发现了什么缺陷、使用什么仓库变化修复、以及如何验证修复。

---

## 20. 方法论文章作为受 AHICP 治理的成果

AHICP 项目本身应维护两个互相支撑的产出：

1. 可执行开放协议；
2. 解释并批判性发展协议的方法论文章。

方法论文章应讨论 AI 辅助研究的概念意义，包括人类认知/认识责任、可委托与不可委托的思想劳动、持久研究状态、semantic version control、framework-level authorship 与 publication accountability。

文章自身必须遵守 AHICP：

- 维护 Working Framework；
- 区分 AI 提议与人类批准主张；
- 为具有时效性的政策主张维护证据/来源笔记；
- 在人类批准门完成前保持 `DERIVED-PROVISIONAL`。

---

## 21. 推荐 Commit 语义

建议前缀：

- `intent:` 人类内容/形式决定；
- `structure:` 论证架构；
- `draft:` 派生成果；
- `form:` 呈现/渲染；
- `evidence:` 来源/数据/形式核验；
- `protocol:` 工作流/治理；
- `audit:` 审查/修复记录；
- `release:` 已批准协议或成果发布。

---

## 22. 最小 AHICP Profile

轻量合规项目至少应包括：

```text
START_HERE.zh-CN.md
BOOTSTRAP_PROMPT.zh-CN.md
SESSION_CONTEXT_BOOTSTRAP.zh-CN.md
ONBOARDING_REPORT_TEMPLATE.zh-CN.md
AGENTS.zh-CN.md
AHICP_MANIFEST.yaml
AHICP_CONTEXT_INTERFACE.yaml
core/CONTENT_CORE.zh-CN.md
core/FORM_CORE.zh-CN.md
core/DECISION_LOG.zh-CN.md
docs/working-memory.zh-CN.md
docs/working-memory/current-focus.zh-CN.md
docs/working-memory/task-plan.zh-CN.md
docs/working-memory/work-log.zh-CN.md
docs/argument-map.zh-CN.md
docs/framework-status.zh-CN.md
```

采用双语配置时，还应同时维护对应英文 mirror。

一个单文件实现可以把上述多个 Working Memory 角色映射到同一路径；默认模板采用拆分实现。

旧 clarification-register 路径可作为兼容指针保留，但不属于 active state 的最小必需文件。

对于长篇或高风险项目，强烈推荐 evidence 目录、Approved Framework 快照、详细协议文件和审计记录。

---

## 23. 外部系统、工具发现、授权与人类交接

### 23.1 Machine-operable-first escalation

当任务需要访问外部系统、账户或服务，并且完成该任务所需的人类授权已经存在时，AI Agent **SHOULD** 先安全地发现并穷尽当前可用且已获授权的 machine-operable path，再把纯操作性步骤交还给人类。

可检查的路径至少包括：

- 平台内建工具；
- 已连接的 plugin / connector；
- 官方 MCP server 或等价官方工具接口；
- provider 官方 API；
- 官方 GitHub App 或其他 provider-managed integration；
- 仓库中已经存在并获准使用的 automation / workflow；
- 人类或项目治理已经明确批准的 adapter / plugin。

“installed”“enabled”“connected”或目录中可见，**不等于能力已经实际可调用**。当某项能力的可用性会影响执行路线或是否升级给人类时，Agent **MUST** 在技术上可行且安全的前提下进行一次真实、最小、优先只读的 capability probe。若当前 host 根本不暴露实际调用能力，Agent 必须把它记录为“当前环境不可调用/未验证”，不得把目录状态写成已验证能力。

### 23.2 授权与凭据安全

在功能等价时，Agent **SHOULD** 优先采用官方、OAuth、provider-managed、最少 secret handling 的连接路径，并在 provider 支持时优先选择满足任务所需的最小权限范围。

Agent **MUST NOT** 为了操作方便而要求人类把 password、API token、private key、recovery code 或其他 secret 粘贴到聊天。需要由人类创建或保存凭据时，交接应把 secret 留在 provider 或受控 secret store 中，并明确说明哪些值不得发送给 AI。

Agent 不得绕过：

- 身份验证；
- 账户所有者 consent；
- 权限授予；
- 人类保留的高影响或不可委托批准；
- 项目已经定义的 public / canonical cutover、release 或其他责任边界。

### 23.3 Human handoff

只有当下一步确实要求人类身份授权、账户所有者 consent、不可委托的高影响决定，或当前可用并获授权的工具能力无法完成该动作时，才应把该动作升级给人类。

此类 handoff **MUST**：

1. 将步骤压缩到完成当前 blocker 所需的最小集合；
2. 一次只要求当前必要的人类动作，不把后续可由 AI 执行的步骤一并外包；
3. 默认操作者没有技术背景，使用 provider UI 中可识别的名称和结果条件；
4. 明确指出 password、token、secret、private key 等哪些值不得发送给 AI；
5. 说明完成标准，使 AI 能在授权后独立检查是否成功。

人类完成必要动作后，Agent **SHOULD** 重新读取最新仓库状态、重新探测相关 capability，并从中断点恢复执行，而不是要求人类重新说明项目上下文或继续承担本可由机器执行的操作。

### 23.4 Provider actual state 与 repository durable state

Provider dashboard、临时 UI 页面、聊天状态与模型记忆都不是 authoritative project state。

外部操作完成后，Agent **SHOULD** 验证真实 provider state；如果该操作改变了会影响后续工作的持久项目状态，则 **MUST** 把经验证的结果 write-through 到 repository 中适当的 durable state。记录应按任务需要包含 observed state、验证证据或引用、有用的 build/deployment identifier、当前 blocker 与后续授权/cutover 状态，但不得保存 secret。

Provider 是其账户实时配置和运行结果的直接观察来源；repository 则保存项目对这些观察的持久、可审计状态。若二者不一致，Agent 必须重新检查 provider，并更新或标记 repository state 为 stale / unresolved，而不是依赖旧聊天、旧 UI 截图或模型记忆。

### 23.5 授权作用域与持久状态行动生命周期

**持久状态变化（durable-state change）**是指会超出当前交互而继续存在，并可能约束后续工作或影响外部主体的变化。持久化本身并不等于高影响。对于已经落在有效授权作用域内、风险较低且可逆的 repository/provider 写入，**不应**仅因为它会持久存在就升级给人类。

在机器执行之前，Agent **必须**保持以下状态彼此区分：

~~~text
proposal
!= authorization
!= execution
!= verification
!= durable write-back
~~~

proposal 可以描述或建议行动，但不等于授权；authorization 只允许其覆盖范围内的行动；execution 不证明目标状态已经实现；verification 用于确认实际观察到的状态；durable write-back 把经验证的结果写入持久项目状态，不能反过来补造授权。

当某项行动的授权边界具有实质意义时，repository-backed 的授权记录或策略**应当**按与风险相称的粒度明确：

- **action class**：允许执行哪一类行动；
- **target**：覆盖哪个 repository、branch、artifact、account、channel、endpoint、audience 或其他对象；
- **allowed side effects**：哪些副作用属于授权范围，而不是意外扩张；
- **reversibility / rollback assumptions**：行动是否可逆，以及预期如何回滚；
- **duration or occurrence bound**：一次行动、限定时间、指定 workflow 或其他明确边界；
- **escalation condition**：何种 scope、impact、不确定性或 provider state 变化需要重新交由人类判断；
- **authorization provenance**：授权所来源的人类决定或已经持久记录的人类批准策略。

有效授权可以来自：

1. 针对当前行动或状态转换的明确人类决定；或
2. 已经持久记录、由人类批准且其作用域确实覆盖当前行动的 pre-authorization policy。

pre-authorization policy **不得**覆盖 AHICP 或项目治理已经标记为 human-reserved / non-delegable 的行动类别；这类行动必须获得相应治理规则要求的人类授权。

Agent **不得**仅根据 AI proposal、技术能力、repository visibility、provider 配置、provider 可达性、build/deployment 成功、已有 endpoint、upstream branch/tag/version 变化或其他机器观察事实推断授权已经存在。

### 23.5.1 Provider-neutral 的高影响判断

如果一项行动的合理可预见效果会实质改变以下一个或多个边界，则应视为 high-impact：

- **人类/项目的外部承诺或公开代表行为**：包括以人类/项目名义进行的 release、publication、submission 或 communication；
- **access、confidentiality、security、identity、ownership 或 permission 边界**；
- **canonical identity、routing、production/public cutover，或对既有依赖身份/路由的 retirement**；
- **adopted governance authority**：包括后续工作采用哪个 protocol、framework、policy、version、tag 或 commit；
- **不可逆或实质上难以逆转的状态**，尤其是 deletion、destructive migration 或失去可靠 rollback 路径。

这些是 impact dimensions，不是 provider-specific 的操作名称。repository write、merge、deployment、email send、API call 或 configuration change **并不会**仅因其技术类别就自动属于同一个授权等级。例如，可逆的 branch write 可以在既有授权范围内作为常规机器操作，而 public release 或 canonical cutover 可能跨越 human-reserved 边界。同样，deployment 本身不等于 release、publication authorization 或 canonical cutover。

出现以下情况时，Agent **必须**升级请求人类授权：

- 行动属于 human-reserved / non-delegable；
- 没有有效授权来源覆盖当前行动；
- target 或 side effects 超出已记录作用域；或
- reversibility、impact 或 uncertainty 已经实质偏离原授权所依赖的假设。

对于已经授权、低风险、可逆的机器操作，Agent **不应**仅因为它会改变 durable state 就升级给人类。

执行后依照 §23.4：验证 provider actual state，并把经验证的 durable result 写回 repository。若验证失败，或观察到的影响超出授权范围，则停止继续传播，按需把状态标记为 unresolved/stale，并只升级当前新增的授权或判断问题。

如果项目采用 PPF 或其他 publishing framework，publication lifecycle 的具体状态语义由该框架定义。AHICP 只规范 authorization provenance、scope、escalation、execution/verification separation 与 durable write-back，不重新定义 publishing lifecycle。

---

## 24. 可迁移性

AHICP v0.3 当前参考实现以 GitHub 为目标，但逻辑功能与精确文件名相分离。

未来实现可以把相同规范角色映射到其他受版本控制的协作系统，只要仍保留显式状态、人类/AI 来源区分、批准门、可检查历史和跨 Agent 交接。

---

## 25. 设计命题

AHICP 把 AI 辅助探究、研究与创作中经常被混在一起的东西分开：

1. Layer 1 人类作者核心基础；
2. Layer 2 当前论述框架；
3. Layer 3 派生成果；
4. 与三层并行的 Working Memory；
5. 人类呈现意图；
6. 证据约束；
7. 批准状态；
8. 历史决定。

协议把这种分离视为持久、可审计、人类治理的 AI 辅助探究与创作之基础。

---

## 26. 双语规范同步

AHICP 项目文档应以中文和英文双语维护。

对于 AHICP 自身仓库以及采用双语 profile 的项目：

1. 中文是规范性的语义来源，也是人类编辑/审阅的第一基准。
2. 英文是同步翻译镜像。
3. 实质性修改必须在同一工作轮次中更新两种语言。
4. 当两个语言版本在主张、要求、批准状态、范围或未决问题上存在实质差异时，不得认为它们已同步。
5. 如果中英文冲突，以中文为准，直到英文镜像被修正。
6. 新的实质性 Markdown 文档应在创建时就产生双语配对版本。
7. 代码、BibTeX、schema 与原始数据等语言中立技术成果可以保持单份，但其人类可读说明必须双语。
8. Agent 交接文档必须让语言优先级规则可发现。
9. 对规则建立前的 legacy bilingual file，如果英文已经形成中文版尚未吸收的较新实质内容，必须先完成 English -> Chinese catch-up，使中文达到切换时真正的最新语义状态。
10. canonical cutover 完成后，正常实质性发展必须固定为 `Human decision -> Chinese canonical -> English mirror`；英文不得独立形成新的实质内容。

推荐命名：

- 中文 canonical：`NAME.zh-CN.md`
- 英文 mirror：在需要向后兼容或 GitHub 默认渲染时用 `NAME.md`，否则用 `NAME.en.md`。

稳定同步检查点应包括一次中英语义一致性检查。
