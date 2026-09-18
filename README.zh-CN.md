# 人机研究协作协议

[English](README.md) | [中文](README.zh-CN.md)

**语言治理：中文是规范性基准（canonical source）；英文是同步镜像（synchronized mirror）。任何实质性修改都必须在同一工作轮次同步两种语言。冲突时以中文为准。**

**HARC Protocol** 是一个以 GitHub 为中心的工作流，用于人类作者与可替换 AI Agent 之间持续进行研究与知识协作。

> **AI Agent 可以被替换，但研究状态不能丢失。**

聊天窗口只是交互界面，并不是长期研究项目的持久记忆。重要的人类决策、论证结构、呈现要求、证据约束与批准状态，应被外化为明确、受版本控制的仓库文件，使一个新的、有能力的 AI Agent 即使没有原始聊天记录，也可以继续工作。

## 两类项目输出

HARC 有意设计为一个双重输出项目：

1. **可执行的开放协议** — 规范、治理规则、模板、批准状态、形式配置、记忆架构以及未来的一致性工具。
2. **方法论论文** — 一篇解释该协议并讨论人类认知／认识责任、向 AI 委托、可审计作者性、持久研究记忆以及 AI 中介研究协作边界的学术论文。

当前方法论论文文件：

- [`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`](paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md) — `WORKING-FRAMEWORK`，尚未由人类批准。
- [`paper/METHODOLOGY_ARTICLE.zh-CN.md`](paper/METHODOLOGY_ARTICLE.zh-CN.md) — 中文 canonical、`DERIVED-PROVISIONAL` 草稿。
- [`paper/METHODOLOGY_ARTICLE.en.md`](paper/METHODOLOGY_ARTICLE.en.md) — 英文完整镜像。
- [`paper/methodology-references.bib`](paper/methodology-references.bib) — 参考文献源文件。
- [`evidence/METHODOLOGY_SOURCES.zh-CN.md`](evidence/METHODOLOGY_SOURCES.zh-CN.md) — 来源核验与证据约束。

较早的白皮书继续作为概念性导论保留；方法论论文的目标是发展为一项独立的学术研究成果。

## 双语治理

HARC 项目的所有实质性人类可读文档都采用中英双语维护：

- 中文 `*.zh-CN.md` 是编辑、人类审阅和语义权威基准；
- 英文 `*.md` / `*.en.md` 是同步翻译镜像；
- 新文件从创建时起即应双语配对；
- 只修改一种语言不算完成；
- BibTeX、代码、schema、原始数据等语言中立技术文件可以保持单份，但其说明文档仍须双语。

完整规则见 [`protocol/BILINGUAL_SYNC.zh-CN.md`](protocol/BILINGUAL_SYNC.zh-CN.md)。

## HARC 解决什么问题？

长期 AI 辅助项目反复面临以下失败：

- **语义漂移（semantic drift）** — 流畅的 AI 文本逐渐替代或弱化人类最初真正想表达的内容；
- **作者性模糊（authorship ambiguity）** — 哪些主张是人类承诺、哪些只是 AI 建议变得不清楚；
- **上下文窗口依赖（context-window dependence）** — 重要决定被困在某一次对话或某个平台记忆中；
- **结构不透明（structural opacity）** — 人类必须重新通读长篇手稿，才能理解项目当前到底在论证什么；
- **呈现漂移（presentation drift）** — AI 临时选择的格式被误认为作者长期偏好；
- **交接失败（handoff failure）** — 新模型或 Agent 无法可靠重建项目当前状态；
- **生成—验证不对称（generation–verification asymmetry）** — AI 生成、重组工作的速度快于人类持续验证的速度。

HARC 通过区分**人类意图、操作性表示、证据、形式、批准、历史与派生表达**来处理这些问题。

## 权威架构

一个典型的 HARC 项目通常包含：

```text
project/
├── AGENTS.md
├── core/
│   ├── CONTENT_CORE.md
│   ├── FORM_CORE.md
│   └── DECISION_LOG.md
├── docs/
│   ├── argument-map.md
│   ├── framework-status.md
│   └── frameworks/
├── evidence/
└── paper/ | book/ | article/ | report/ | ...
```

### 内容核心

`CONTENT_CORE.md` 记录人类作者当前的实质性承诺：作品想要主张什么、区分什么、质疑什么、保留什么，或者有意保持哪些问题开放。

AI 提案不会仅因为有用或写得漂亮，就自动成为作者承诺。

### 形式核心

`FORM_CORE.md` 记录人类希望成果如何表达：成果类型、字体、版式、引用呈现、视觉系统、语言呈现方式以及可复用的风格偏好。

研究内容与表达偏好被有意分离。

### 决策日志

`DECISION_LOG.md` 是人类在内容、形式和协作协议方面作出实质性决定的时间顺序审计轨迹。

### 操作性论证图

`docs/argument-map.md` 是一个由 AI 维护的紧凑表示，用于表达当前知识结构。对于长篇研究，它是人机讨论时的首选接口。

### 已批准框架快照

工作论证图不会自动获得人类认可。当人类明确审阅并批准某个框架后，它会被冻结为版本化快照，例如 `docs/frameworks/FW-001.md`。

实质性变化应产生新的已批准框架版本，而不是静默改写旧版本。

### 派生学术成果

论文、著作、报告或其他最终成果，是受内容核心、已批准框架、形式核心与证据共同约束的**派生表达**。

## 人类反馈的三路路由

每条实质性指令在持久化之前先分类：

- **CONTENT** — 改变作品论证什么或意味着什么；
- **FORM** — 改变作品如何呈现；
- **PROTOCOL** — 改变协作本身如何运作。

一条消息可以同时具有多个标签。

```text
CONTENT:
Human decision -> Decision Log -> Content Core -> Argument Map -> Artifact

FORM:
Human decision -> Decision Log -> Form Core -> Rendering / Typesetting -> Artifact

PROTOCOL:
Human decision -> Decision Log -> Protocol Documents -> Agent Behavior
```

## 两个人类批准门槛

### Gate A — 框架批准

人类审阅并接受作品的核心知识架构：主要命题、论证关系、概念区分、章节功能、限制，以及有意保持未解决的问题。

这是项目最主要的**实质性知识检查点**。

HARC 区分两类缺陷：一种已经存在于获批架构中，另一种只是在后续 AI 扩写中局部引入。

### Gate B — 最终成果批准

在以人类作者身份正式投稿、出版或公开发布之前，人类应按照相关期刊、机构、学科或作者规范所要求的程度批准具体发布版本。

框架批准把人类注意力集中在知识架构上，但并不免除最终发表责任。

## 认知委托与认识责任

HARC 并不假设人的价值在于亲手写出每一个句子。AI 可以承担大量检索、综合、起草、重组、一致性检查和格式处理工作。

但委托认知劳动，并不自动等于委托认识责任。HARC 把人类注意力集中到高杠杆决策上：研究目标、核心承诺、主要推理架构、关键证据冲突、框架批准，以及在需要时对最终发布版本的批准。

这一责任模型在方法论论文中进一步发展。

## 可复用形式配置

HARC 支持跨项目继承表达形式：

`可复用作者配置 -> 成果类型配置 -> 项目 Form Core -> 外部约束 -> 实现`

详见：

- `protocol/FORM_PROFILE_INHERITANCE.zh-CN.md`
- `templates/form-profiles/AUTHOR_PROFILE.zh-CN.md`
- `templates/form-profiles/BOOK.zh-CN.md`
- `templates/form-profiles/ACADEMIC_PAPER.zh-CN.md`
- `templates/form-profiles/ARTICLE.zh-CN.md`

## 持久记忆原则

> **聊天是临时交互上下文。仓库才是持久的共享研究记忆。**

不需要保存聊天中的每一句话。但如果遗失某条人类指令会改变一个新 Agent 应该如何继续项目，那么这条指令就应被提升到适当的权威仓库文件中。

这并不会创造无限模型上下文。它通过紧凑的当前状态核心、按时间记录的日志、结构图、详细证据／档案、索引以及选择性检索来实现可扩展记忆。

## 审计纪律

HARC 的多轮审计是一系列**审阅—修复循环**：

`review -> identify defect -> repair/implement -> verify repair`

要求三轮审计，意味着需要完成三次这样的循环。若另要求修复后审计，则应在其后再进行独立的第四次检查。

审计记录：

- [`docs/FOUNDING_IDEA_AUDIT.zh-CN.md`](docs/FOUNDING_IDEA_AUDIT.zh-CN.md) — 初始思想可追溯性。
- [`docs/THREE_CYCLE_REPAIR_AUDIT.zh-CN.md`](docs/THREE_CYCLE_REPAIR_AUDIT.zh-CN.md) — 明确的三轮审阅／修复记录。
- [`docs/FINAL_POST_REPAIR_AUDIT.zh-CN.md`](docs/FINAL_POST_REPAIR_AUDIT.zh-CN.md) — 独立修复后审计。
- [`docs/BILINGUAL_PARITY_AUDIT.zh-CN.md`](docs/BILINGUAL_PARITY_AUDIT.zh-CN.md) — 中文 canonical / 英文 mirror 的仓库级一致性审计。

## 从这里开始

### 对人类

1. 阅读 [`paper/METHODOLOGY_ARTICLE.zh-CN.md`](paper/METHODOLOGY_ARTICLE.zh-CN.md)，了解正在形成的学术论证。
2. 阅读 [`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`](paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md)，检查论文当前的工作框架与未决问题。
3. 阅读 [`protocol/SPECIFICATION.zh-CN.md`](protocol/SPECIFICATION.zh-CN.md)，查看规范性工作流。
4. 阅读 [`docs/THREE_CYCLE_REPAIR_AUDIT.zh-CN.md`](docs/THREE_CYCLE_REPAIR_AUDIT.zh-CN.md) 和 [`docs/FINAL_POST_REPAIR_AUDIT.zh-CN.md`](docs/FINAL_POST_REPAIR_AUDIT.zh-CN.md)，了解当前整合审计状态。
5. 使用 [`templates/research-project/`](templates/research-project/) 启动新项目。

### 对 AI Agent

1. 阅读 [`AGENTS.zh-CN.md`](AGENTS.zh-CN.md)。
2. 阅读 [`core/PROTOCOL_CORE.zh-CN.md`](core/PROTOCOL_CORE.zh-CN.md) 和最近的 [`core/DECISION_LOG.zh-CN.md`](core/DECISION_LOG.zh-CN.md)。
3. 阅读 [`protocol/SPECIFICATION.zh-CN.md`](protocol/SPECIFICATION.zh-CN.md)。
4. 应用相关的持久化、框架批准、路由、证据与形式继承规则。
5. 不要虚构人类从未表达过的承诺。
6. 新项目应记录所采用的 HARC 版本／tag／commit，避免将后续上游变更静默视为已经接受的治理规则。

## 仓库状态

本仓库是 HARC Protocol 的独立开发主仓库，包含：

- 规范性协议；
- 实施指南；
- 可复用的研究项目模板；
- 可复用的形式配置模板；
- 概念性白皮书；
- 受 HARC 框架控制的方法论论文；
- 方法论论文的证据层；
- 初始思想与修复审计；
- 未来开发路线图。

当前协议的目标环境是 **GitHub + 人类作者 + AI Agent**。未来可以考虑支持更多平台。

## 设计原则

HARC 不是一个让 AI 成为“以人类署名作品的隐藏作者”的系统。它要做的是让**人类意图、AI 转化、证据、批准、责任与最终表达之间的关系变得明确并可审计**。

## 版本

工作规范：**v0.2.0-draft**。

## 许可

项目目标是开放复用。具体许可条款记录在 `LICENSE-DECISION.zh-CN.md` 中，应通过明确决定最终确定，而不能根据仓库是否公开来推断。
