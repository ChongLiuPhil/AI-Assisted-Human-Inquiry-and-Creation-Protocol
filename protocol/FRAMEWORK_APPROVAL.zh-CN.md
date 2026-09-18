# Framework Approval 与责任模型

> **本中文文件是规范性基准；英文 `FRAMEWORK_APPROVAL.md` 是同步镜像。**

## 1. 操作性 framework 的两种状态

HARC 区分：

1. **Working Framework** — 可修改、由 AI 维护、用于讨论。
2. **Approved Framework Snapshot** — 已由人类作者明确审阅并确认。

前者是协作工具；后者是人类实际接受的思想架构的持久记录。

## 2. Framework Approval Gate

当 framework 能紧凑说明下列内容时，可以进入批准：

- 中心问题；
- 一个或多个核心命题；
- 关键概念与区分；
- 主要支持性主张；
- 主张之间的依赖关系；
- 主要章节/小节及其功能；
- 重要限制；
- 有意保留的未决问题；
- 对论证有实质影响的已知证据冲突。

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

如果人类明确选择暂缓某个问题，则应把它标记为 `DEFERRED`，并在 framework 中显式保留该未决状态，而不是假装问题已经解决。

Framework Approval 不应建立在 AI 私下猜测的关键解释上。

## 3. Framework Approval 意味着什么

Framework Approval 是项目主要的实质性思想检查点。

它表示人类接受：

- 中心命题；
- 主要推论关系；
- 核心区分；
- 推理组织方式；
- 主要章节/小节的预期角色；
- 已声明限制和未决问题。

它使人类注意力可以集中在思想架构上，而不要求开发阶段逐行批准每一份 provisional AI 扩写。

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

推荐状态：

- `WORKING-FRAMEWORK`
- `FRAMEWORK-APPROVED`
- `DERIVED-PROVISIONAL`
- `FINAL-REVIEW`
- `FINAL-APPROVED`

## 9. 责任区分

HARC 区分：

### 思想架构责任

主要锚定在人类批准 framework。

### 派生表达质量控制

AI 可以承担大量扩写；具体缺陷仍需检查与修订。

### 公开学术问责

发布/投稿决定在适用外部标准要求的范围内仍属于人类责任。

可以压缩为：

> **Framework Approval 界定实质性思想作者责任的中心；Final Artifact Approval 界定公开学术问责的发布门槛。**
