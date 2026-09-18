# Critical Clarification Register Protocol
## 关键澄清登记册协议

> **本中文文件是规范性基准；英文 `CLARIFICATION_REGISTER.md` 是同步镜像。**

## 1. 目的

HARC 在“人类已经确认的规范内容”和“AI 当前维护的论证结构”之间增加一个显式的**关键澄清层（Critical Clarification Layer）**。

它专门处理以下情况：

- AI 对人类意图的理解存在重要不确定性；
- 两种或多种解释都会显著改变核心命题或论证结构；
- 关键概念、术语、翻译或双语对应尚未确认；
- 范围、限定条件、因果/逻辑关系或章节功能存在歧义；
- AI 准备作出的实现选择可能把一个尚未确认的解释固化进 Argument Map 或最终文本；
- 某一问题如果处理错误，会导致后续大量扩写建立在错误理解上。

其目标不是收集所有小疑问，而是把**高影响不确定性**从聊天中显式提升出来，交给人类作者确认。

## 2. 架构位置

Clarification Register 是一个 **1.5 层桥接文档**：

```text
Layer 1 — Human-authoritative state
  Content Core / Form Core / Protocol Core / Decision Log
                    ^
                    |
            human resolution
                    |
Layer 1.5 — Critical Clarification Register
                    ^
                    |
       AI detects high-impact ambiguity
                    |
Layer 2 — Working Argument Map / operational structure
                    |
Layer 3 — Derived Artifact
```

Clarification Register 中的未决条目**不是人类已批准观点**。

它的作用是防止 AI 在不确定时自行选择一种解释，并让这种解释静默进入第二层或第三层。

## 3. 何时必须创建澄清条目

当同时满足以下两个条件时，AI Agent **MUST** 创建或更新 Clarification Register 条目：

1. **不确定性不是微不足道的**：存在至少两个合理解释、术语方案、翻译方案、范围理解或结构理解；并且
2. **影响较高**：不同选择可能实质改变核心命题、主要推论关系、关键概念、framework 结构、读者对中心思想的理解、批准状态或长期项目连续性。

典型触发器包括：

- “我不确定作者这里说的 A 是指 X 还是 Y”；
- 某个关键词有多种哲学/技术含义；
- 中英文关键术语存在多个不等价译法；
- 一个句子可被理解成强命题或弱命题；
- 一个范围条件没有明确；
- 一个章节到底是提供证据、定义概念还是推出结论尚不清楚；
- 人类最新反馈与旧 Core/Framework 存在可能的张力；
- AI 发现自己需要做一个会影响全篇的解释性选择。

## 4. AI 必须主动提出，而不是等待人类发现

AI Agent 不仅在被问到时才记录不确定性。

在以下节点，Agent SHOULD 主动执行 **Clarification Scan**：

- 开始新的重大研究阶段前；
- 大规模重构 Argument Map 前；
- Framework Approval 前；
- 把新术语/概念推广到全文前；
- 从母语稿生成正式外语版本前；
- 大规模扩写章节前；
- 发现新证据可能改变中心解释时；
- Final Artifact Review 前。

如果发现高影响不确定性，应先登记并向人类提出，而不是静默继续。

## 5. Blocking 与 Non-blocking

不是所有未决问题都必须停止全部工作。

每个条目应标记：

- `BLOCKING` — 在人类解决前，不应继续相关结构性传播或大规模扩写；
- `NON-BLOCKING` — 可以继续不依赖该问题的其他工作，但不得把某一未确认答案写成人类立场。

判断标准是：错误选择是否可能造成高成本语义漂移或重大返工。

## 6. 推荐条目 schema

每个条目至少包含：

- **ID：** `CLR-001`
- **状态：** `OPEN / HUMAN-CONFIRMED / HUMAN-CORRECTED / DEFERRED / SUPERSEDED`
- **严重度：** `BLOCKING / NON-BLOCKING`
- **类别：** `CONCEPT / CLAIM / INFERENCE / SCOPE / STRUCTURE / TERMINOLOGY / TRANSLATION / FORM / PROTOCOL / EVIDENCE`
- **触发来源：** 人类陈述、AI 检测、证据冲突、翻译问题等；
- **不确定点：** 当前无法安全确定的内容；
- **候选解释：** 如适用，列出主要候选；
- **为什么重要：** 若选错会影响什么；
- **受影响文件/命题/章节：** traceability；
- **AI 当前建议：** 可选，必须明确标为 `AI-PROPOSED`；
- **需要人类回答的问题：** 尽量压缩成可直接确认/纠正的问题；
- **人类解决结果：** 解决后填写；
- **传播目标：** Content Core / Form Core / Protocol Core / Decision Log / Argument Map / artifact；
- **解决日期 / 决定 ID：** 如适用。

## 7. 关键概念与双语术语

Clarification Register 特别适合处理：

- 核心概念的定义边界；
- 母语术语与英文术语的对应；
- 一个英文词是否过强或过弱；
- 是否保留原文术语；
- 同一术语在不同章节是否保持一致；
- 翻译是否改变哲学、法律、统计、技术或方法论含义。

当术语经过人类确认后：

- 与研究意义相关的概念/术语进入 Content Core；
- 主要属于表达/翻译约定的进入 Form Core；
- 如具有项目级长期治理意义，记录到 Decision Log；
- Working Argument Map 与派生文本随后同步。

## 8. Resolution Promotion Rule

一条 clarification 被人类解决后，**不能只把状态改成 RESOLVED 就结束**。

必须执行：

`Human resolution -> Decision Log -> appropriate Core -> Argument Map -> Derived Artifact`

也就是说，Clarification Register 是**决策入口与历史痕迹**，不是最终规范真值源。

已解决条目可以保留在 Register 中，以记录“曾经不确定什么、由谁如何解决”，但当前权威答案必须进入适当 Core。

## 9. 与 Decision Log 的区别

- **Clarification Register** 记录：当前有哪些高影响问题还需要人类判断，以及它们如何被解决；
- **Decision Log** 记录：人类最终作出了什么持久决定。

前者以“不确定性治理”为中心；后者以“决定历史”为中心。

## 10. 与 Working Argument Map 的区别

Argument Map 可以列出未决问题，但不应承担全部澄清治理功能。

Clarification Register 提供：

- 严重度；
- 来源；
- 候选解释；
- 人类确认状态；
- 传播目标；
- 双语/术语决策；
- 解决后的审计轨迹。

Argument Map 只需要引用相关 `CLR-xxx`，避免在多个文件重复维护完整澄清内容。

## 11. 完成条件

一个高影响澄清只有在以下条件全部满足时才算关闭：

1. 人类给出明确确认、纠正、延后或拒绝；
2. 结果记录在 Clarification Register；
3. 持久决定进入 Decision Log；
4. 相应 Core 已更新；
5. Working Argument Map 已同步；
6. 受影响派生成果已同步或明确标为待同步；
7. 中英文版本已完成 parity。

## 12. 原则

> **当不确定性可能改变意义时，AI 的职责不是猜得更自信，而是把不确定性提升为可由人类治理的显式对象。**
