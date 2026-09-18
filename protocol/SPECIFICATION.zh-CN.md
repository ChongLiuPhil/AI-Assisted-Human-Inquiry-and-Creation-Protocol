# HARC 协议规范

**Human–AI Research Collaboration Protocol（人类—AI 研究协作协议）**

**版本：** 0.2.0-draft  
**范围：** 以 GitHub 为中心，由人类作者与一个或多个 AI Agent 进行持续研究与长篇思想协作。

> **本中文版本是规范性基准；英文 `SPECIFICATION.md` 是同步镜像。**

---

## 1. 目的

HARC 定义一种持久、可审计的协作架构，用于人类思想方向与 AI 辅助研究、结构化、起草、修订、核验和格式处理长期共同发展的项目。

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
- 有意义的人类认知责任与认识责任。

HARC v0.2 假定 GitHub 是持久仓库基础设施。未来实现可以把相同逻辑角色映射到其他系统。

---

## 2. 规范性术语

- **MUST（必须）** — HARC 合规所要求。
- **SHOULD（应当）** — 强烈推荐，除非项目记录了偏离理由。
- **MAY（可以）** — 可选。

---

## 3. 核心原则

长期研究项目**不得**把一次临时 AI 对话当作唯一持久状态。

> **聊天是交互界面；仓库才是持久的共享研究记忆。**

重要项目状态必须外部化到显式、受版本控制的仓库成果中。

---

## 4. 角色

### 4.1 人类作者

人类作者提供、修订或确认实质性思想承诺与呈现意图。

人类作者可以把大量检索、综合、结构化、起草、编辑、形式化、检查与格式处理工作委托给 AI Agent。

认知劳动的委托不得自动被理解为认识责任的委托。

### 4.2 AI Agent

AI Agent 可以：

- 抽取并规范化人类决定；
- 维护仓库状态；
- 提出论证、反对意见、区分、例子、术语与结构；
- 在工具允许时开展研究与证据核验；
- 维护操作性论证表示；
- 把已批准结构扩写成文本或其他成果；
- 检测不一致、证据冲突和同步缺陷；
- 维护格式与渲染系统。

AI Agent 必须区分自己的提议与经人类批准的承诺。

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

### 5.4 Critical Clarification Register — `docs/clarification-register.zh-CN.md`

Critical Clarification Register 是 Layer 1 与 Layer 2 之间的桥接状态，用于管理**高影响且尚未经人类解决的不确定性**。

它 MUST 记录那些如果 AI 自行猜测，可能实质改变核心命题、关键概念、范围、主要推论关系、章节功能、关键术语/翻译、Framework Approval 或长期项目连续性的问题。

每个重要条目 SHOULD 包括：

- ID；
- 状态；
- `BLOCKING / NON-BLOCKING` 严重度；
- 类别；
- 不确定点；
- 候选解释；
- 影响说明；
- 受影响文件/命题/章节；
- AI 建议（如有，必须标为 `AI-PROPOSED`）；
- 需要人类回答的问题；
- 人类解决结果；
- 传播目标。

未解决 clarification MUST NOT 被视为人类承诺。

人类解决后，Agent MUST 执行 Resolution Promotion：

`Human resolution -> Decision Log -> appropriate Core -> Working Argument Map -> Derived Artifact`

Resolved entry 可以保留为审计痕迹，但规范答案必须进入适当 Core。

完整规则见 `protocol/CLARIFICATION_REGISTER.zh-CN.md`。

### 5.5 Working Argument Map — `docs/argument-map.zh-CN.md`

Working Argument Map 是长篇思想结构的主要操作性讨论界面。

它通常由 AI 维护，并且在人类批准之前必须被视为可变。

它应暴露：

- 研究问题；
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
5. 不得仅仅因为治理规则变化而改变研究内容。

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

HARC 区分：

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

## 14. 认知劳动委托与认识责任

HARC 区分**认知劳动的委托**与**认识责任的委托**。

AI 可以进行大量检索、综合、结构化、起草、形式化、一致性检查、修订和格式处理。

人类注意力应集中在高杠杆决定上，包括：

- 研究目标与问题；
- 核心承诺；
- 主要推论架构；
- 对重要 AI 提议的接受/拒绝；
- 关键证据冲突的处理；
- Framework Approval；
- 在需要时完成 Final Artifact Approval。

HARC 不主张文件结构本身能保证良好判断。批准机制是治理支架，不是人类能力与理解的替代物。

---

## 15. 持久记忆与上下文限制

HARC 提供的是持久项目记忆，而不是字面意义上的无限模型上下文。

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
- `HARC_MANIFEST.yaml` 或等价机器可读状态索引；
- 根 `AGENTS.zh-CN.md` / English mirror；
- 一个可发现的 Onboarding Handshake 规范。

新的 AI Agent 在实质性工作前 MUST 按启动入口定义的顺序读取当前状态，并 SHOULD 先输出 HARC Onboarding Report，说明协议状态、人类已确认状态、Form 状态、Blocking Clarifications、Framework/Artifact 状态、同步缺陷与当前允许的下一步。

如果 Agent 无法从仓库完成该报告，项目存在 onboarding/persistence defect。

### 16.2 常规接管读取

新的 AI Agent 至少应通过阅读以下内容继续正常项目工作：

1. `START_HERE.zh-CN.md` 与 `HARC_MANIFEST.yaml`；
2. 项目 `AGENTS.zh-CN.md`；
3. Content Core；
4. Form Core；
5. 最近的 Decision Log；
6. Critical Clarification Register；
7. Framework Status 与最新 Approved Framework；
8. Working Argument Map；
9. 当前相关成果与证据。

项目应记录所采用的 HARC version/tag/commit，避免把后续上游协议变化静默视为已经接受的治理规则。

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
10. 所有会阻塞 Framework Approval 的 Critical Clarification 都在 Clarification Register 中显式可见，而不是只存在于聊天或 AI 私下判断。

任一条件失败都构成显式同步缺陷。

---

## 19. 多轮审计与修复纪律

要求的多轮审计必须被解释为重复的审查—修复循环。

每一轮应执行：

`审查 -> 识别缺陷 -> 修复/实现 -> 验证修复`

如果要求三轮，就执行三次这种循环。如果要求修复后审计，则在三轮结束后再进行一轮独立审计，不能把三轮之一算作最终审计。

审计记录应说明发现了什么缺陷、使用什么仓库变化修复、以及如何验证修复。

---

## 20. 方法论文章作为受 HARC 治理的成果

HARC 项目本身应维护两个互相支撑的产出：

1. 可执行开放协议；
2. 解释并批判性发展协议的方法论文章。

方法论文章应讨论 AI 辅助研究的概念意义，包括人类认知/认识责任、可委托与不可委托的思想劳动、持久研究状态、semantic version control、framework-level authorship 与 publication accountability。

文章自身必须遵守 HARC：

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

## 22. 最小 HARC Profile

轻量合规项目至少应包括：

```text
START_HERE.zh-CN.md
AGENTS.zh-CN.md
HARC_MANIFEST.yaml
core/CONTENT_CORE.zh-CN.md
core/FORM_CORE.zh-CN.md
core/DECISION_LOG.zh-CN.md
docs/clarification-register.zh-CN.md
docs/argument-map.zh-CN.md
docs/framework-status.zh-CN.md
```

采用双语配置时，还应同时维护对应英文 mirror。

对于长篇或高风险项目，强烈推荐 evidence 目录、Approved Framework 快照、详细协议文件和审计记录。

---

## 23. 可迁移性

HARC v0.2 当前以 GitHub 为目标，但逻辑功能与精确文件名相分离。

未来实现可以把相同规范角色映射到其他受版本控制的协作系统，只要仍保留显式状态、人类/AI 来源区分、批准门、可检查历史和跨 Agent 交接。

---

## 24. 设计命题

HARC 把 AI 辅助研究中经常被混在一起的东西分开：

1. 人类思想意图；
2. 人类呈现意图；
3. AI 操作性表示；
4. 证据约束；
5. 批准状态；
6. 派生表达；
7. 历史决定。

协议把这种分离视为持久、可审计、人类治理的 AI 辅助研究之基础。

---

## 25. 双语规范同步

HARC 项目文档应以中文和英文双语维护。

对于 HARC 自身仓库以及采用双语 profile 的项目：

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
