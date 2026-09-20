**人类第一入口：** [《从这里开始：一个普通人的探究、创作与 AI 协作指南》](docs/HUMAN_GUIDE.zh-CN.md) · [English mirror](docs/HUMAN_GUIDE.md)

**公共项目入口：** [AHICP 主页](https://chongliuphil.github.io/AI-Assisted-Human-Inquiry-and-Creation-Protocol/) · [PPF 主页](https://chongliuphil.github.io/Personal-Publishing-Framework/) · [Vault Interface 主页](https://chongliuphil.github.io/Vault-interface/) · [Starter 主页](https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/)\n\n**体系与 Agent 入口：** [docs/ECOSYSTEM.zh-CN.md](docs/ECOSYSTEM.zh-CN.md) · [ecosystem.yaml](ecosystem.yaml) · [llms.txt](docs/llms.txt) · [统一 Agent 调取契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.zh-CN.md)\n\n# AI 辅助人类探究与创作协议

[English](README.md) | [中文](README.zh-CN.md)

**体系与 Agent 入口：** [`docs/ECOSYSTEM.zh-CN.md`](docs/ECOSYSTEM.zh-CN.md) · [`ecosystem.yaml`](ecosystem.yaml) · [Starter 统一指南](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/ECOSYSTEM.zh-CN.md)

**语言治理：中文是规范性基准（canonical source）；英文是同步镜像（synchronized mirror）。任何实质性修改都必须在同一工作轮次同步两种语言。冲突时以中文为准。**

**AI-Assisted Human Inquiry and Creation Protocol（AHICP）** 是一个以 GitHub 为中心的协议，用于在人类主导下，借助 AI 持续进行探究、研究、推理、写作与创作。

> **AI Agent 可以被替换，但人的目的与持久项目状态不能丢失。**

聊天窗口只是交互界面，并不是长期探究或创作项目的持久记忆。重要的人类决策、论证结构、呈现要求、证据约束与批准状态，应被外化为明确、受版本控制的仓库文件，使一个新的、有能力的 AI Agent 即使没有原始聊天记录，也可以继续工作。

## 规范性方向

AHICP 是一套**人类主导、AI 辅助**的协议。人类始终是项目目的、实质判断、批准与最终责任的承担者。AI 系统可以大量辅助检索、比较、结构化、提出方案、起草、检查、转换和仓库维护，但 AI 的提议不会仅仅因为有用或表达成熟就自动成为人的承诺。

AHICP 规范 AI 如何辅助人的探究与创作；它**不定义出版基础设施**。需要可迁移的 source-to-publication 工作流时，项目可以另外采用 **Personal Publishing Framework（PPF）**。

## AI Agent 从零接管：先从这里开始

新的 AI Agent **不要直接从 README 或正文开始工作**。

只把本 README 当作项目说明页。零上下文接管时，先打开 [`START_HERE.zh-CN.md`](START_HERE.zh-CN.md)，随后严格按照 `START_HERE.zh-CN.md` 与 `AHICP_MANIFEST.yaml` 当前声明的读取顺序和 task routing 执行。README 不再复制另一份 mandatory read order，以避免多个入口之间发生状态漂移。

先从 Working Memory 确定当前续接点，再按任务选择性重建三层长期记忆，并在做任何实质性修改前完成 **AHICP Onboarding Report**。

当前仓库的自举验证见 [`docs/ONBOARDING_SELF_TEST.zh-CN.md`](docs/ONBOARDING_SELF_TEST.zh-CN.md)。

这使“Agent 是否真正理解当前项目状态”变成一个可观察、可检查的握手步骤，而不是假定。

在握手之后，`SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` 只加载一个最小 Repository Resolver；`AHICP_CONTEXT_INTERFACE.yaml` 则规定按需读取、revision freshness、write-through 与 cache invalidation。动态项目状态不复制成第二份聊天真值源。

## 两类项目输出

AHICP 有意设计为一个双重输出项目：

1. **可执行的开放协议** — 规范、治理规则、模板、批准状态、形式配置、记忆架构以及未来的一致性工具。
2. **方法论论文** — 一篇解释该协议并讨论人类对研究目的、方向与思想架构的责任、AI 工具的工作分担、可审计作者性、持久研究记忆以及 AI 中介研究协作边界的学术论文。

当前方法论论文文件：

- [`docs/working-memory.zh-CN.md`](docs/working-memory.zh-CN.md) — Working Memory Index / Resolver。
- [`docs/working-memory/current-focus.zh-CN.md`](docs/working-memory/current-focus.zh-CN.md) — 当前最近期最高优先级目标。
- [`docs/working-memory/task-plan.zh-CN.md`](docs/working-memory/task-plan.zh-CN.md) — 动态任务、TODO、blockers 与 pending decisions。
- [`docs/working-memory/work-log.zh-CN.md`](docs/working-memory/work-log.zh-CN.md) — 主要供人类回顾的工作历史纪要，默认不进入 AI onboarding。
- [`docs/clarification-register.zh-CN.md`](docs/clarification-register.zh-CN.md) — 旧路径兼容指针，不再承载 active state。
- [`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`](paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md) — 当前方法论文章的 `WORKING-FRAMEWORK`。其实时批准状态、blocker 与 gate **不在 README 中复制维护**；请以 `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`、Current Focus 与 Task Plan 的最新 canonical 状态为准。
- [`paper/METHODOLOGY_ARTICLE.zh-CN.md`](paper/METHODOLOGY_ARTICLE.zh-CN.md) — 中文 canonical、`DERIVED-PROVISIONAL` 草稿。
- [`paper/METHODOLOGY_ARTICLE.en.md`](paper/METHODOLOGY_ARTICLE.en.md) — 英文完整镜像。
- [`paper/methodology-references.bib`](paper/methodology-references.bib) — 参考文献源文件。
- [`evidence/METHODOLOGY_SOURCES.zh-CN.md`](evidence/METHODOLOGY_SOURCES.zh-CN.md) — 来源核验与证据约束。

较早的白皮书继续作为概念性导论保留；方法论论文的目标是发展为一项独立的学术研究成果。

## 双语治理

AHICP 项目的所有实质性人类可读文档都采用中英双语维护：

- 中文 `*.zh-CN.md` 是编辑、人类审阅和语义权威基准；
- 英文 `*.md` / `*.en.md` 是同步翻译镜像；
- 新文件从创建时起即应双语配对；
- 只修改一种语言不算完成；
- BibTeX、代码、schema、原始数据等语言中立技术文件可以保持单份，但其说明文档仍须双语。

完整规则见 [`protocol/BILINGUAL_SYNC.zh-CN.md`](protocol/BILINGUAL_SYNC.zh-CN.md)。

## AHICP 解决什么问题？

长期 AI 辅助项目反复面临以下失败：

- **语义漂移（semantic drift）** — 流畅的 AI 文本逐渐替代或弱化人类最初真正想表达的内容；
- **作者性模糊（authorship ambiguity）** — 哪些主张是人类承诺、哪些只是 AI 建议变得不清楚；
- **上下文窗口依赖（context-window dependence）** — 重要决定被困在某一次对话或某个平台记忆中；
- **结构不透明（structural opacity）** — 人类必须重新通读长篇手稿，才能理解项目当前到底在论证什么；
- **呈现漂移（presentation drift）** — AI 临时选择的格式被误认为作者长期偏好；
- **交接失败（handoff failure）** — 新模型或 Agent 无法可靠重建项目当前状态；
- **生成—验证不对称（generation–verification asymmetry）** — AI 生成、重组工作的速度快于人类持续验证的速度。

AHICP 通过区分**人类意图、操作性表示、证据、形式、批准、历史与派生表达**来处理这些问题。

## 权威架构

一个典型的 AHICP 项目通常包含：

```text
project/
├── START_HERE.zh-CN.md
├── START_HERE.md
├── BOOTSTRAP_PROMPT.zh-CN.md
├── BOOTSTRAP_PROMPT.md
├── SESSION_CONTEXT_BOOTSTRAP.zh-CN.md
├── SESSION_CONTEXT_BOOTSTRAP.md
├── ONBOARDING_REPORT_TEMPLATE.zh-CN.md
├── ONBOARDING_REPORT_TEMPLATE.md
├── AHICP_MANIFEST.yaml
├── AHICP_CONTEXT_INTERFACE.yaml
├── AGENTS.zh-CN.md
├── AGENTS.md
├── core/
│   ├── CONTENT_CORE.md
│   ├── FORM_CORE.md
│   └── DECISION_LOG.md
├── docs/
│   ├── working-memory.zh-CN.md
│   ├── working-memory.md
│   ├── clarification-register.zh-CN.md
│   ├── clarification-register.md
│   ├── argument-map.md
│   ├── framework-status.md
│   └── frameworks/
├── evidence/
└── paper/ | book/ | article/ | report/ | ...
```

### 零上下文启动入口

`START_HERE.zh-CN.md` 与 `AHICP_MANIFEST.yaml` 定义一个新 Agent 的第一读取顺序和 Onboarding Handshake。它们不保存新的研究主张，而负责让新的 Agent 正确找到权威状态并证明自己已经重建项目。

### 内容核心

`CONTENT_CORE.md` 记录人类作者当前的实质性承诺：作品想要主张什么、区分什么、质疑什么、保留什么，或者有意保持哪些问题开放。

AI 提案不会仅因为有用或写得漂亮，就自动成为作者承诺。

### 形式核心

`FORM_CORE.md` 记录人类希望成果如何表达：成果类型、字体、版式、引用呈现、视觉系统、语言呈现方式以及可复用的风格偏好。

研究内容与表达偏好被有意分离。

### 决策日志

`DECISION_LOG.md` 是人类在内容、形式和协作协议方面作出实质性决定的时间顺序审计轨迹。

### Working Memory Area

Working Memory 是一个功能区，而不是固定单文件。当前 AHICP 参考实现拆为 Index、Current Focus、Task Plan 与 Work Log。

三层长期记忆是：

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

Working Memory 不属于 Layer 1.5。Current Focus 保存“现在最重要的事”；Task Plan 保存“接下来怎么推进”；Work Log 保存“我们是怎么走到这里的”，主要面向人类作者回顾。

Clarification 是 Working Memory 中的一种 item。人类解决后执行 Promotion：

`Working Memory -> Decision Log -> appropriate Long-Term Memory destination`

旧 `docs/clarification-register.zh-CN.md` 仅保留为兼容指针。

### 操作性论证图

`docs/argument-map.md` 是一个由 AI 维护的紧凑表示，用于表达当前知识结构。对于长篇研究，它是人机讨论时的首选接口。当前 blocker、pending human decision 与高影响 clarification 应引用 Working Memory，而不是在 Argument Map 中重复维护全部细节。

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

AHICP 区分两类缺陷：一种已经存在于获批架构中，另一种只是在后续 AI 扩写中局部引入。

### Gate B — 最终成果批准

在以人类作者身份正式投稿、出版或公开发布之前，人类应按照相关期刊、机构、学科或作者规范所要求的程度批准具体发布版本。

框架批准把人类注意力集中在知识架构上，但并不免除最终发表责任。

## AI 工具分工与人类责任主体

AHICP 并不假设人的价值在于亲手写出每一个句子。AI Agent 作为工具，可以执行或辅助大量检索、综合、起草、重组、一致性检查和格式处理工作。

AHICP 不把 AI 描述为认知主体，也不把“AI 承担认知劳动 / 认知任务”作为规范性表述。研究或创作的目的、核心问题和方向由人类发起、导航并批准。

这里的关键不是把“人类责任”当作一个抽象属性，而是明确：**人类必须保持为责任主体／责任承担者。** 这一点适用于研究与探究全过程，并在论文、书籍、报告或其他成果进入公开知识传播时尤其重要。AI 可以分担工作，但不能成为项目目的、核心判断、framework 授权或公开知识传播的最终责任主体。

对于长篇成果，这一责任主体地位主要通过 Layer 2 Framework 落实：人类在 Framework Approval 前必须清楚理解、认真审核并明确确认 framework 中实际呈现的全部实质内容。AI 可以帮助提出和整理 framework，但不能替代人类对项目方向与思想架构的授权。Final Artifact Approval 仍然是独立要求，用来确保具体公开版本继续由可识别的人类责任主体承担发布责任。

这一责任模型在方法论文章中进一步发展.

## 可复用形式配置

AHICP 支持跨项目继承表达形式：

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

AHICP 的多轮审计是一系列**审阅—修复循环**：

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
2. 先阅读 [`docs/working-memory.zh-CN.md`](docs/working-memory.zh-CN.md)，确认项目当前阶段、目标、任务、阻塞与下一步。
3. 再阅读 [`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`](paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md)，检查论文当前 Working Framework。
4. 阅读 [`protocol/SPECIFICATION.zh-CN.md`](protocol/SPECIFICATION.zh-CN.md)，查看规范性工作流。
5. 阅读 [`docs/THREE_CYCLE_REPAIR_AUDIT.zh-CN.md`](docs/THREE_CYCLE_REPAIR_AUDIT.zh-CN.md) 和 [`docs/FINAL_POST_REPAIR_AUDIT.zh-CN.md`](docs/FINAL_POST_REPAIR_AUDIT.zh-CN.md)，了解当前整合审计状态。
6. 使用 [`templates/research-project/`](templates/research-project/) 启动新项目。

### 对 AI Agent

1. 从 [`START_HERE.zh-CN.md`](START_HERE.zh-CN.md) 开始。
2. 以 `AHICP_MANIFEST.yaml` / `AHICP_CONTEXT_INTERFACE.yaml` 的最新 task routing 为读取依据，不把 README 的说明性文字当作第二份启动规范。
3. 先恢复 Working Memory 的当前续接点，再只读取当前任务所需的 Core / Decision / Framework / Evidence / Artifact 状态。
4. 不要虚构人类从未表达过的承诺；写入前重新确认相关 canonical revision。
5. 新项目应记录所采用的 AHICP 版本／tag／commit，避免把后续上游变更静默视为已经接受的治理规则。

## 仓库状态

本仓库是 AHICP Protocol 的独立开发主仓库，包含：

- 规范性协议；
- 实施指南；
- 可复用的研究项目模板；
- 可复用的形式配置模板；
- 概念性白皮书；
- 受 AHICP 框架控制的方法论论文；
- 方法论论文的证据层；
- 初始思想与修复审计；
- 未来开发路线图。

当前协议的目标环境是 **GitHub + 人类作者 + AI Agent**。未来可以考虑支持更多平台。

## 设计原则

AHICP 不是一个让 AI 成为“以人类署名作品的隐藏作者”的系统。它要做的是让**人类意图、AI 转化、证据、批准、责任与最终表达之间的关系变得明确并可审计**。

## 版本

工作规范：**v0.3.0-draft**。

## 许可

本仓库采用**非商业双重许可模式**，目的是支持个人学习、教育、研究、公益以及其他非商业复用，同时保留商业授权权利。

- 软件、脚本、Schema、自动化、机器可读配置和可执行模板：**PolyForm Noncommercial License 1.0.0**；
- 说明文档、规范、图示、教育材料与方法论内容：**CC BY-NC-SA 4.0**；
- 商业使用需要另行取得商业许可。

仓库级权威许可边界见 [LICENSE.md](LICENSE.md) 与 [COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md)。

## 与综合 Starter 的关系

如果希望把 AHICP、PPF 与公开 Vault Interface 组合到新项目，或对既有 GitHub 项目进行可审计升级，可使用：

https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter

Starter 只负责组合、版本锁定、检查与升级计划；本仓库继续是自身规范／模板的权威来源。
