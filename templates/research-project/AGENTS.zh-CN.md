# AGENTS.md — 项目 HARC 契约

本项目遵循 Human–AI Research Collaboration Protocol。

> **语言：** 中文文件为规范性基准；英文 `AGENTS.md` 为同步 mirror。采用本模板的新项目默认使用中文 canonical + 英文 synchronized mirror，除非人类明确选择其他语言治理方式。

## 零上下文接管

任何新 AI Agent 在实质性工作前必须先读取：

1. `START_HERE.zh-CN.md`
2. `HARC_MANIFEST.yaml`
3. `BOOTSTRAP_PROMPT.zh-CN.md`
4. `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`

随后按 manifest 重建项目状态，并使用 `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` 输出 HARC Onboarding Report；报告必须回显 `HARC ACTIVE SESSION CONTRACT — LOADED`。

完成接管握手前，不得进行大规模结构修改、Framework Approval 或把 AI 提议提升为人类承诺。

## 协议来源

初始化项目时记录所采用的协议来源：

- 上游仓库：`ChongLiuPhil/Human-AI-Research-Collaboration-Protocol`
- HARC 版本：`0.2.0-draft`（替换成实际采用的 version/tag/commit）
- Adopted commit/tag：`UNRESOLVED — 初始化时记录`

未来 Agent 不得静默假定上游 HARC 最新规则已经被本项目采用。协议升级必须成为明确项目决定。

## 必读顺序

进行实质性工作前读取：

1. `core/CONTENT_CORE.zh-CN.md`
2. `core/FORM_CORE.zh-CN.md`
3. 最近的 `core/DECISION_LOG.zh-CN.md`
4. `docs/clarification-register.zh-CN.md`
5. `docs/framework-status.zh-CN.md`
6. 最新 Approved Framework（如有）
7. `docs/argument-map.zh-CN.md`
8. 相关成果与 evidence 文件
9. 需要时再读取英文 mirror 以核验双语同步

## 仓库状态高于聊天记忆

不要把旧 Agent 的聊天上下文当成规范项目状态。持久的人类决定必须提升到仓库文件。

## 路由人类反馈

把实质性指令分类为：

- `CONTENT`
- `FORM`
- `PROTOCOL`
- 或多标签。

先持久化，再上游优先传播。

## Content 规则

人类内容决定高于 AI 草拟。AI 提议在被接受前必须明显保持 pending。

## Form 规则

人类形式决定高于渲染默认值。不得从临时工具选择推断长期作者偏好。

在适当情况下，区分 reusable author preference、artifact-type profile、project-specific rule、external constraint 与 temporary default。

## Clarification Register 规则

如果对核心观点、关键概念、术语/翻译、范围、主要推论关系或章节功能存在高影响不确定性，先写入 `docs/clarification-register.zh-CN.md`，不得自行选择一种解释后传播。

条目应标明 `BLOCKING / NON-BLOCKING`。人类解决后，把结果写入 Decision Log 和相应 Core，再更新 Argument Map 与成果。

Framework Approval、正式翻译、大规模扩写和 Final Review 前主动执行 Clarification Scan。

## Framework 规则

`docs/argument-map.zh-CN.md` 是 AI 维护的工作结构，不自动等于人类认可。

只有在人类明确 Framework Approval 后才能创建 `docs/frameworks/FW-xxx.zh-CN.md`，并同步创建英文 mirror。不得静默修改已批准快照。

Approved Framework 是主要实质性思想基线。应区分 framework-level defect 与后续 AI 扩写才引入的局部缺陷。

## Evidence 规则

证据与当前人类承诺冲突时，必须显式呈现。不得隐瞒反面证据，也不得静默改写人类立场。

## 成果状态

AI 扩写正文在相应最终人类批准被记录前保持 `DERIVED-PROVISIONAL`。

## 双语同步规则

- 中文 canonical 是人类编辑和审阅基准；
- 英文 mirror 必须在同一工作轮次同步；
- 中英文冲突时，以中文为准；
- 双语不同步构成同步缺陷；
- 新的实质性 Markdown 文件创建时即应配对。

## 交接标准

新的、能力合格的 Agent 应能在没有原始聊天 transcript 的情况下，仅根据仓库状态继续项目。
