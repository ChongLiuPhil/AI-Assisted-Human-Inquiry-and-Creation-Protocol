# Critical Clarification Register
## 关键澄清登记册

**状态：** `ACTIVE CLARIFICATION INTERFACE`  
**角色：** Layer 1 与 Layer 2 之间的高影响不确定性桥接文档。  
**语言：** 中文 canonical；英文 `clarification-register.md` 是同步 mirror。

> 未解决条目不是人类已批准观点。  
> 人类解决后，必须把结果提升到 Decision Log 与相应 Core，再更新 Argument Map 和派生成果。

## 使用规则

AI Agent 应在以下情况下主动创建条目：

- 对作者意图有两个以上合理解释；
- 关键术语、概念或翻译尚未确认；
- 强/弱命题、范围、限定条件或推论关系不清；
- 某一选择可能实质改变核心论证结构；
- 新反馈与旧 Core / Framework 可能冲突；
- 如果猜错，会导致高成本返工或长期 semantic drift。

重大阶段、Framework Approval、正式翻译、大规模扩写和 Final Review 前应执行 Clarification Scan。

---

## OPEN

### CLR-001 — 示例

**状态：** `OPEN`  
**严重度：** `BLOCKING / NON-BLOCKING`  
**类别：** `CONCEPT / CLAIM / INFERENCE / SCOPE / STRUCTURE / TERMINOLOGY / TRANSLATION / FORM / PROTOCOL / EVIDENCE`

**触发来源：**  
`...`

**不确定点：**  
`...`

**候选解释：**

1. `...`
2. `...`

**为什么重要：**  
`...`

**受影响文件 / 命题 / 章节：**

- `...`

**AI 当前建议：**  
`AI-PROPOSED — ...`

**需要人类回答的问题：**  
`...`

**人类解决结果：**  
`PENDING`

**传播目标：**

- Decision Log
- `CONTENT_CORE / FORM_CORE / PROTOCOL`
- Argument Map
- Derived Artifact

---

## RESOLVED

已解决条目可以保留在这里作为审计痕迹，但权威答案必须已经进入适当 Core。

### CLR-000 — 示例已解决条目

**状态：** `HUMAN-CONFIRMED`  
**人类解决结果：** `...`  
**Decision ID：** `Dxxx`  
**已传播至：** `...`

---

## 术语 / 翻译特别规则

对于核心术语，应显式记录：

- 作者母语表达；
- 候选英文表达；
- 不同译法之间的语义差异；
- 是否存在强弱差别、学科惯例或误导风险；
- 人类最终确认的对应关系。

一旦确认：

- 概念意义进入 Content Core；
- 主要属于表达习惯的翻译约定进入 Form Core；
- 长期项目决定进入 Decision Log；
- Argument Map 与正文同步。

## 完成条件

一条 clarification 只有在以下全部完成后才可关闭：

- [ ] 人类已经明确确认 / 纠正 / 延后 / 拒绝；
- [ ] Register 已记录结果；
- [ ] Decision Log 已记录持久决定；
- [ ] 相关 Core 已更新；
- [ ] Argument Map 已同步；
- [ ] 派生成果已同步或明确标记 pending；
- [ ] 中文 / 英文 mirror 已同步。
