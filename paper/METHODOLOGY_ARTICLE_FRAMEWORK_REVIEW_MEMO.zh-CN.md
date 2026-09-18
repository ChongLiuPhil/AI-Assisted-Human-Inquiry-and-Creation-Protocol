# 方法论文章 — AI Framework Review Memo

**状态：** `AI-PROPOSED REVIEW AID`  
**权威性：** 非规范性；本文件不会修改 Article Content Core，也不构成人类批准。  
**目的：** 帮助人类作者在创建任何 `MA-FW-001` 快照之前审阅 `WORKING-FRAMEWORK — REVIEW READY`。

> 本中文文件是审阅备忘录的规范基准；英文 `METHODOLOGY_ARTICLE_FRAMEWORK_REVIEW_MEMO.md` 是同步镜像。  
> 但本备忘录整体仍然只是 AI 提议，并不因“中文是 canonical”而升级成人类承诺。

---

## Clarification Register 映射

本 memo 现在只作为**分析附件**。高影响未决问题的正式操作状态已经迁移到 `docs/clarification-register.zh-CN.md`：

- 原 D1 -> `CLR-001`
- 原 D2 -> `CLR-002`
- 原 D3 -> `CLR-003`、`CLR-004`、`CLR-005`
- 原 D4 -> `CLR-006`
- 原 D5 -> `CLR-007`
- 原 D6 -> `CLR-008`

如果本 memo 与 Clarification Register 在状态、严重度或人类答复上冲突，以 Clarification Register 为当前操作界面；最终人类决定仍必须提升到 Decision Log 与相应 Core。

# 1. 总体评估

当前 framework 已经足够连贯，可以进入人类审阅，但在六个问题得到明确决定之前，不宜整体批准。

最大的概念风险不是内部矛盾，而是**过度主张**：在论证与证据尚不足时，把为 HARC 设计的实际治理架构提升成关于作者身份或认识责任的普遍理论。

第一篇方法论文章完全可以在不作出这种更强普遍主张的情况下提出有力贡献。

因此建议总体姿态是：

> **对架构主张可以强；对普遍哲学结论应更谨慎。**

HARC 可以明确提出一种以仓库为中心、持久、可审计、由人类治理的研究协作方法；至于作者身份、认知或责任的本质，则可以作为仍开放的哲学问题。

---

# 2. D1 — 中心责任术语

## 方案 A — `epistemic responsibility` / 认识责任

### 优点

- 直接涉及研究者对什么有理由接受、主张、批准并承担责任；
- 与证据、推论、证言/依赖和学术问责自然连接；
- 能给方法论文章一个明确哲学中心。

### 风险

- 范围比所有认知能动性更窄；
- 可能让读者误以为文章已经拥有一套成熟完整的认识责任理论。

## 方案 B — `cognitive responsibility` / 认知责任

### 优点

- 更宽，更容易与任务分配、认知、记忆、规划和 AI 辅助联系。

### 风险

- 不是特别标准，概念边界较模糊；
- 可能混淆“执行认知工作”与“对主张负责”。

## 方案 C — 分层区分

使用：

- **cognitive labor（认知劳动）** 表示检索、综合、起草、检查、形式化、格式处理等；
- **epistemic responsibility（认识责任）** 表示对重要主张/推论进行理解、接受、拒绝、授权并承担问责。

### AI 建议

`AI-PROPOSED DEFAULT: 方案 C。`

它提供最清楚的区分：

> **认知劳动可以大规模委托；认识责任必须保持显式治理。**

这并不意味着人类必须独立重新推导每一个事实细节，而是明确 HARC 要治理的问题：当认知劳动被分布后，责任究竟在哪里、怎样被锚定。

---

# 3. D2 — Framework Responsibility Thesis 的强度

## 强版本

> 人类对 framework 的批准，一般性地构成 AI 辅助长篇成果中实质性思想作者身份的中心。

### 优点

- 哲学上大胆；
- 可能具有鲜明原创性。

### 风险

- 目前主张过强；
- 不同学科和文体可能以不同方式分配思想责任；
- 高层 framework 可能遗漏关键事实、数学、方法论或解释性错误；
- authorship 在制度与哲学上都存在争议。

## 中等版本

> 在 HARC 内部，一个经人类明确批准的 framework，是 AI 辅助长篇协作中主要的实质性思想责任锚点。

### 优点

- 直接由协议架构支持；
- 保留创始人“人类应对压缩后的论证结构承担高强度责任”的核心思想；
- 不假装已经解决作者身份的一般形而上学或伦理学问题。

### AI 建议

`AI-PROPOSED DEFAULT: 中等版本。`

文章以后可以进一步问：HARC 模型是否支持一个更普遍的 authorship theory；但协议本身不需要依赖那个更强结论。

建议措辞：

> **HARC 并不把 framework approval 当作完整的作者身份理论，而把它当作主要责任锚点：一个版本化时刻，在此人类明确接受作品的中心主张、推论架构、概念区分、范围与结构性承诺。**

---

# 4. D3 — AI 提议术语

## A. `semantic version control`

### 评估

这个术语有用，因为普通 Git 记录文本发生了什么变化，而 HARC 还记录变化是人类决定、AI 提议、证据约束、临时默认值还是已批准 framework 修订。

### 风险

读者可能误以为它已经是成熟技术领域或正式标准。

### AI 建议

`ACCEPT AS HARC COINAGE / WORKING TERM`，但应明确给出定义，并且不声称它是现有文献中的既定术语。

建议表达：

> HARC 使用 **semantic version control（语义版本控制）** 作为项目术语，指的不只是对文本进行版本控制，还包括对意义、决定、提议与批准的状态和权威进行版本化管理。

---

## B. `generation–verification asymmetry`

### 评估

作为直观问题描述很有用：AI 辅助生成可以比人类审阅扩展得更快。

### 风险

如果没有经验测量，把它称为一般性“不对称”可能听起来像一个已证明的定量规律。

### AI 建议

`KEEP AS A HEURISTIC LABEL`，不要作为已经证明的经验定律。

建议表达：

> 文章把这种实践压力称为 **generation–verification asymmetry（生成—验证不对称）**：这是一个工作标签，用来描述 AI 能显著降低候选研究内容的生产与转换成本，而仔细的人类理解和核验仍然昂贵。

---

## C. `responsibility concentration`

### 评估

它试图表达创始人关于“人类注意力应集中在压缩 framework，而不是反复审查每一份中间扩写”的想法。

### 风险

“concentration” 容易被误读成允许忽略下游准确性，并在修辞上与独立的 Final Artifact Approval Gate 产生冲突。

### AI 建议

`REPLACE OR DEMOTE。`

更好的候选：

- **epistemic responsibility anchoring（认识责任锚定）**；
- **responsibility architecture（责任架构）**；
- **high-leverage human review（高杠杆人类审阅）**。

其中第一项尤其适合 Approved Framework 概念。

---

# 5. D4 — 与 extended/distributed cognition 的关系

## 方案 A — 中心理论基础

把 HARC 作为 extended/distributed cognition 的应用或扩展。

### 风险

这会不必要地让 HARC 依赖心灵哲学与认知科学中的有争议命题。

## 方案 B — 次级概念比较

这些文献帮助解释为什么认知可以受到外部成果支撑、并分布在人与工具之间；但 HARC 在方法论上不依赖更强形而上学结论。

## 方案 C — 最小背景

只作简短提及。

### AI 建议

`AI-PROPOSED DEFAULT: 方案 B。`

这样既有理论深度，又不会让 HARC 是否成立取决于 extended-mind thesis 是否为真。

推荐立场：

> HARC 与外在主义和分布式认知方法相容，但它只需要一个更弱的实践命题：显式外部表示可以保存并协调研究状态。

---

# 6. D5 — 经验验证计划

## 方案 A — 核心贡献

文章同时提出 HARC 与正式实验研究计划。

### 优点

使 HARC 具有较强可测试性。

### 风险

当前项目尚无经验结果，可能导致文章承诺超过实际证明。

## 方案 B — 未来研究议程

主文是方法论/规范性文章；经验测试作为可证伪或可操作的后续工作。

## 方案 C — 省略

让文章保持纯概念性。

### AI 建议

`AI-PROPOSED DEFAULT: 方案 B。`

这样保留“HARC 应可测试”的重要思想，同时不假装其有效性已经得到证明。

推荐表达：

> HARC 的实践主张产生一个经验研究议程，而不是已经建立的性能结果。

---

# 7. D6 — 学科定位

## Philosophy of technology / epistemology

如果文章重点是责任、认识依赖、扩展认知、作者身份和委托，这是最合适方向。

## Research methodology

如果重点是工作流架构、有效性、可审计性和可复现研究实践，更适合此方向。

## Scholarly communication / research integrity

如果重点是 authorship policy、来源、贡献披露、问责与出版治理，更适合此方向。

## Interdisciplinary AI governance

受众最广，但可能牺牲概念精度。

### AI 建议

`AI-PROPOSED DEFAULT: 跨学科研究方法论 + philosophy-of-technology core。`

对第一版草稿的实际含义：

- 以方法论问题开篇；
- 把认识责任作为概念中心；
- 把作者身份/研究诚信规则作为约束，而不是唯一主题；
- 保留足够篇幅说明操作性协议，使论文不能被简化成抽象伦理讨论。

目标期刊可以在思想 framework 稳定后再选。

---

# 8. 推荐的批准候选

如果人类作者接受上述默认建议，第一个 Approved Framework 可以围绕以下压缩命题建立：

> **AI 辅助研究应围绕显式、受版本控制的研究状态组织，并区分人类承诺、AI 表示、证据约束、批准状态与派生表达。认知劳动可以被广泛委托，但认识责任必须通过可识别的高杠杆决定保持在人类治理之下。在 HARC 中，经人类批准的思想 framework 作为长篇协作的主要责任锚点，而独立的 Final Artifact Approval Gate 保留公开发布问责。**

`AI-PROPOSED SYNTHESIS — NOT HUMAN APPROVED。`

这一综合命题有意比普遍 authorship theory 更窄。它足以为协议提供论证动机，同时为以后更深入的哲学发展保留空间。

---

# 9. 批准纪律

人类审阅可能产生：

- 接受整个 framework；
- 接受但要求修订；
- 拒绝个别命题/术语；
- 把 AI 提议术语提升成人类批准状态；
- 把一个命题降级到未来研究；
- 重构文章。

只有**明确的整体 framework 批准**才能触发 `MA-FW-001`。

对本 memo 中一个或多个建议表示同意，不自动等同于对整个 framework 的批准。
