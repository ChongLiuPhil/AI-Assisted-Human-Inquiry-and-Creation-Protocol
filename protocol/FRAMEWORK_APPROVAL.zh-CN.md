# Framework Approval 与责任模型

> **本中文文件是规范性基准；英文 `FRAMEWORK_APPROVAL.md` 是同步镜像。**

## 1. 操作性 framework 的两种状态

HARC 区分：

1. **Working Framework** — 可修改、由 AI 维护、用于讨论。
2. **Approved Framework Snapshot** — 已由人类作者明确审阅并确认。

前者是协作工具；后者是人类实际接受的思想架构的持久记录。

## 2. Framework Approval Gate

当 framework 能紧凑而充分地说明下列内容时，可以进入批准：

- 中心问题；
- 一个或多个核心命题；
- 关键概念与区分；
- 主要支持性主张；
- 主张之间的依赖关系；
- 主要章节/小节及其功能；
- 重要范围条件与限制；
- 有意保留的未决问题；
- 对论证有实质影响的已知证据冲突；
- 任何被选择纳入 framework、因而成为其思想表示一部分的具体措辞。

进入批准并不等于已经批准。Framework Approval 要求人类作者对**拟批准 framework 中实际呈现的全部实质内容**形成清楚理解，认真逐项审核，并明确确认。人类不能仅对标题、摘要或大意作笼统认可，再把 framework 中未理解或未审核的实质细节视为已批准内容。

AI Agent 可以帮助提出、整理、压缩和表达 Working Framework，但不能替代人类对项目目的、方向和思想架构的授权。

当人类明确批准后，Agent 应创建：

`docs/frameworks/FW-001.zh-CN.md`

或下一个可用标识符，并同步英文 mirror。

快照应记录：

- 批准标识；
- 日期；
- 批准状态；
- 在适当情况下记录来源 working-map state/commit；
- 完整批准 framework。

已批准快照不可变。实质性修改必须产生新版本。

## 2.5 Working Memory / Clarification Gate

Framework Approval 之前必须检查 `docs/working-memory/task-plan.zh-CN.md` 的 BLOCKERS、PENDING_HUMAN_DECISIONS 与 Clarifications，并检查 Current Focus 是否仍指向同一 gate。

原则上，不应在 Working Memory 中仍存在会改变中心命题、关键概念、主要推论关系、范围或章节功能的 `BLOCKING` item 时批准 framework。

Framework 可以保留明确标记为 `AI-PROPOSED`、`UNRESOLVED`、`NON-BLOCKING`、`DEFERRED` 或类似状态的项目，但必须满足两个条件：

1. 它们的未决/提议状态在 framework 中明确可见；
2. 它们不是批准当前核心思想架构所必需的、尚未解决的 blocking 前提。

当人类对包含这类项目的完整 framework 作整体 `APPROVE` 时，批准的是这些项目**作为未决/提议项目存在于 framework 中的位置、范围与处理方式**，而不是批准其尚未确认的实质内容。Framework Approval 不得自动改变这些项目的 provenance，也不得把 provisional terminology、经验计划、理论定位或其他 AI 提议 Promotion 为人类原创/确认观点。

只有后续独立的人类决定，才能改变这些项目的来源、批准或 Promotion 状态。

如果人类明确选择暂缓某个问题，则应把它标记为 `DEFERRED`，并在 framework 中显式保留该未决状态，而不是假装问题已经解决。

Framework Approval 不应建立在 AI 私下猜测的关键解释上.

## 3. Framework Approval 意味着什么

Framework Approval 是项目主要的实质性思想检查点，也是人类作为责任主体时，其核心思想责任的结构性锚点。

它表示人类已经理解、审核并接受 framework 中**作为当前承诺实际呈现的全部实质内容**，包括：

- 中心命题；
- 主要推论关系及其逻辑依赖；
- 核心区分；
- 推理组织方式；
- 主要章节/小节的预期角色；
- 范围条件；
- 已声明限制；
- 被纳入 framework 并作为当前承诺的具体措辞。

对于 framework 中明确标记为未决、provisional 或 AI-proposed 的项目，Framework Approval 表示人类理解并接受**其未决状态及其在当前架构中的位置和处理方式**，而不表示接受其尚未批准的实质内容。

因此，一个 Approved Framework 可以包含显式的 unresolved items；但这些 items 必须继续保留原 provenance / approval status，直至另一个明确的人类决定改变它们。

Framework Approval 使开发阶段不需要人类逐行批准每一份 provisional AI 扩写，但不意味着人类可以只批准一个高层概要而忽略 framework 自身的实质细节。

Framework Approval 是 HARC 的治理架构，不应自动被表述成所有学科、机构或出版制度下的一般 authorship theory.

## 4. 派生扩写

Framework Approval 后，AI Agent 可以把 framework 展开成：

- 正文；
- 例子；
- 过渡；
- 文献讨论；
- 解释性细节；
- 注释；
- 支持性表格/图示；
- 格式与呈现。

这些扩写仍受以下约束：

- Content Core；
- Approved Framework；
- Form Core；
- 证据；
- 学术准确性。

最终批准前，成果应保持 `DERIVED-PROVISIONAL`。

## 5. Framework 忠实性

派生成果必须在实质上保持对 Approved Framework 的忠实。

实质性偏离包括：

- 改变中心命题；
- 新增重大结论；
- 删除已批准推论所必需的前提；
- 改变主要主张之间关系；
- 以改变论证的方式改变范围；
- 重组章节以至于已批准推理不再被准确表示。

发生实质偏离时，应返回上游，建立新的 Working Framework 供人类审阅。

## 6. Framework defect 与 expansion defect

HARC 应分析性地区分两类缺陷。

### Framework-level defect

当问题已经存在于人类批准的思想架构中时，它属于 framework 层。例如：

- 中心命题错误或表述不足；
- 主要推论不成立；
- 缺少关键区分；
- 某章节被赋予错误论证角色；
- 缺少会改变主张含义的范围限制。

因为 Approved Framework 是人类确认的实质基线，所以这种问题是被确认思想架构本身的缺陷。

### Derived-expansion defect

当 Approved Framework 本身仍然成立，而后续 AI 实现才引入局部问题时，它只属于扩写层。例如：

- 措辞弱或有歧义；
- 例子不必要或不好；
- 过渡生硬；
- 格式错误；
- 不改变已批准结构的局部解释遗漏。

Final Artifact Approval 之前，不应把这种问题追溯归因到 Approved Framework。除非它暴露出更深层 framework 问题，否则可在下游直接修复。

这种区分允许长篇项目把高强度人类审阅集中到核心架构，同时保留独立的最终发布审阅要求。

## 7. Overview Projection

最终成果应通过 overview 部分让 Approved Framework 对读者可见。

推荐映射：

- **学术论文：** 摘要 + 引言；
- **普通文章：** 开篇/导论性总览；
- **书籍：** 导论/总览章节 + 章节路线图；
- **报告：** 执行摘要 + 结构/方法总览。

文字可以不同，但思想结构应可以恢复。

## 8. Final Artifact Approval Gate

Framework Approval 不等于 release approval。

在人类作者名义下正式投稿、出版或公开发布前，具体发布版本应接受相关学科、机构、出版商或发布渠道要求的人类审阅。

当成果进入公开知识传播时，Final Artifact Approval 的一个核心作用是确保：**最终公开版本仍有可识别的人类责任主体对其知识主张、准确性、完整性与发布决定承担责任。** AI Agent 可以参与生成、扩写、编辑和核查，但不能取代这一责任主体位置。

推荐状态：

- `WORKING-FRAMEWORK`
- `FRAMEWORK-APPROVED`
- `DERIVED-PROVISIONAL`
- `FINAL-REVIEW`
- `FINAL-APPROVED`

---

## 9. 责任主体与责任层级

HARC 区分：

### 项目目的与方向

研究或创作的目的、核心问题和方向由人类发起、给予并持续导航或批准。AI Agent 是协作工具，可以执行或辅助大量具体工作，但不能成为项目目的与方向的最终责任主体。

### 思想架构

责任主要锚定在人类批准的 framework。人类作为责任主体，对其中实际呈现的全部实质内容承担理解、审核、判断与确认责任。

### 派生表达质量控制

AI 可以执行或辅助大量扩写、重组和表达工作；后续派生文本中的具体事实、证据、表达与实现缺陷仍需检查与修订。AI 的工作参与不改变人类责任主体地位。

### 公开知识传播与学术问责

当研究结果、论证或知识主张进入公开传播时，必须保持可识别的人类责任主体。发布/投稿决定以及适用标准要求下的准确性、完整性、研究诚信与公开问责仍由人类承担，并由独立的 Final Artifact Approval Gate 处理。

可以压缩为：

> **HARC 允许 AI 工具广泛参与研究工作的执行，但人类始终保持为责任主体：人类给予并授权项目目的与方向，以其充分理解并批准的 framework 承担核心思想责任，并通过 Final Artifact Approval 对具体公开知识成果承担最终发布责任。**

这一表述是 HARC 的治理模型，不声称单凭 Framework Approval 就已经给出跨领域的一般作者身份理论.
