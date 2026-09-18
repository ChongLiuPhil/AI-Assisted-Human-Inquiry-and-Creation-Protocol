# 双语一致性审计

**日期：** 2026-09-18  
**审计对象：** HARC 仓库中文 canonical / 英文 synchronized mirror 迁移  
**规范规则：** `protocol/BILINGUAL_SYNC.zh-CN.md`  
**状态：** `INITIAL MIGRATION PASS`

> **本中文文件是规范性基准；英文 `BILINGUAL_PARITY_AUDIT.md` 是同步镜像。**

## 1. 审计目的

2026-09-18，人类项目发起人明确要求：

- HARC 项目所有实质性内容采用中英双语；
- 中文是规范性编辑、人类审阅和语义权威基准；
- 英文是同步翻译镜像；
- 任何实质性编辑都必须在同一工作轮次更新两种语言；
- 中英文冲突时以中文为准并修复英文。

本审计检查既有仓库从早期“混合单语/双语”状态迁移到统一双语治理后，是否已经形成完整文件配对，以及已知高风险语义漂移是否得到修复。

## 2. 全树配对扫描

使用当前 `main` 分支递归文件树检查所有 Markdown。

扫描结果：

- Markdown 文件总数：**102**
- 中文 canonical（`*.zh-CN.md`）：**51**
- 英文 mirror：**51**
  - 绝大多数使用既有 `*.md`
  - 方法论文章完整正文使用 `METHODOLOGY_ARTICLE.en.md`
- 缺少英文 mirror 的中文文件：**0**
- 缺少中文 canonical 的英文文件：**0**

**结构配对结果：`PASS`。**

## 3. 本轮完成的主要迁移

### 3.1 协议与治理

已建立或同步：

- `AGENTS.zh-CN.md` / `AGENTS.md`
- `core/PROTOCOL_CORE.zh-CN.md` / English mirror
- `core/DECISION_LOG.zh-CN.md` / English mirror
- `protocol/SPECIFICATION.zh-CN.md` / English mirror
- `protocol/BILINGUAL_SYNC.zh-CN.md` / English mirror
- Persistent Memory、Framework Approval、Routing、Form Inheritance 的双语文件对。

### 3.2 方法论文章

已建立：

- Content Core 双语对；
- Form Core 双语对；
- Framework Status 双语对；
- Argument Map 双语对；
- Framework Review Memo 双语对；
- Evidence notes 双语对；
- 完整中文方法论文章与完整英文 mirror。

文章批准状态没有因为翻译而改变：仍为 `WORKING-FRAMEWORK / DERIVED-PROVISIONAL`。

### 3.3 白皮书

发现旧的中英白皮书已经独立发展：

- 中文：10 节早期概念版本；
- 英文：后来扩展的 14 节版本。

这违反新的 canonical/mirror 规则。

**初始处理存在方向性错误：** 曾先把英文版本重置为较旧中文版的镜像。人类随后明确了 cutover 原则：规则建立前已经在英文中发展的较新实质内容，应先进入中文，而不是被旧中文覆盖。

**最终修复：** 从 Git 历史恢复规则建立前的英文 14 节最新白皮书，识别其中中文旧版没有的实质发展（包括 Presentation Drift、Agent Handoff Failure、Evidence Layer、Derived Artifact、Semantic Version Control 专节、Self-hosting / Protocol Evolution 以及更完整的 limitations/future development），将这些内容完整吸收到中文 canonical；随后再把英文恢复为该最新中文版本的同步镜像。

因此白皮书现已完成正确的：

`pre-cutover English development -> Chinese catch-up -> parity -> Chinese canonical cutover`。

### 3.3.1 规则建立前既有双语文件核查

对规则切换前已经同时存在中英文版本的主要入口文档进行了历史核对：

- **README：** 完整英文版创建于 2026-09-18 01:28:50Z，完整中文版紧接着于 01:28:52Z 建立，章节结构对应，没有发现类似白皮书的独立内容分叉；
- **WHITEPAPER：** 确认存在英文后续发展而中文未追上的真实分叉，已按上述 catch-up 程序修复；
- **Methodology Article：** 规则建立前只有完整中文正文，不存在英文先行发展的风险；
- 本次迁移中后来新建的其他中文 canonical 治理文件，均以当时最新英文治理文件为来源进行翻译，因此已吸收切换前英文状态。

**legacy reconciliation 结果：`PASS`。**

### 3.4 审计、证据和项目治理

已双语化：

- Architecture；
- Founding-Idea Audit；
- Three-Cycle Repair Audit；
- Final Post-Repair Audit；
- Methodology Evidence；
- CONTRIBUTING；
- ROADMAP；
- LICENSE-DECISION；
- README。

### 3.5 可复用模板

已双语化：

- AUTHOR_PROFILE；
- BOOK；
- ACADEMIC_PAPER；
- ARTICLE；
- research-project AGENTS / README；
- Content Core / Form Core / Decision Log；
- Argument Map / Framework Status。

新项目模板现在默认创建中文 canonical + 英文 mirror，而不是事后补翻译。

### 3.6 Critical Clarification Layer

2026-09-18 后续新增的人类原创治理要求已经形成三组新的双语文件对：

- `protocol/CLARIFICATION_REGISTER.zh-CN.md` / English mirror；
- `docs/clarification-register.zh-CN.md` / English mirror；
- `templates/research-project/docs/clarification-register.zh-CN.md` / English mirror。

当前全树重新扫描仍为缺失配对 **0**。

### 3.7 Zero-context Bootstrap

新增两组双语启动文件：

- 根目录 `START_HERE.zh-CN.md` / `START_HERE.md`；
- 模板 `templates/research-project/START_HERE.zh-CN.md` / English mirror。

同时新增语言中立的机器可读：

- `HARC_MANIFEST.yaml`
- `templates/research-project/HARC_MANIFEST.yaml`

YAML manifest 是路径、读取顺序和不变量索引，不需要仅为语言复制；其人类可读规则已经在双语 START_HERE / AGENTS / Specification 中表达。

### 3.8 Onboarding Handshake 与独立启动资产

在 P20 / HARC-D018 经人类明确确认后，新增并双语化：

- `BOOTSTRAP_PROMPT.zh-CN.md` / English mirror；
- `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` / English mirror；
- `protocol/ONBOARDING_HANDSHAKE.zh-CN.md` / English mirror；
- `templates/research-project/BOOTSTRAP_PROMPT.zh-CN.md` / English mirror；
- `templates/research-project/ONBOARDING_REPORT_TEMPLATE.zh-CN.md` / English mirror；
- `docs/ONBOARDING_SELF_TEST.zh-CN.md` / English mirror。

当前递归文件树重新扫描为 **96 个 Markdown = 48 个中文 canonical + 48 个英文 mirror，缺失配对 0**。

### 3.9 Session Context Bootstrap

新增并双语化：

- `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` / English mirror；
- `templates/research-project/SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` / English mirror。

该机制后来经 HARC-D020 收缩为最小 Repository Resolver：会话只保留“如何访问 GitHub”的控制内核，不再复制动态项目状态。

### 3.10 Repository-Backed Context Interface

新增并双语化：

- `protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md` / English mirror。

新增语言中立机器接口：

- `HARC_CONTEXT_INTERFACE.yaml`；
- `templates/research-project/HARC_CONTEXT_INTERFACE.yaml`。

HARC-D020 将上下文模型正式调整为：

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

Session Context Bootstrap 已同步收缩为 Repository Resolver；动态 Blocking Clarifications、Framework、Artifact 与 Core 等状态必须从 GitHub 最新 canonical revision 按需读取。

最新递归扫描为 **102 个 Markdown = 51 个中文 canonical + 51 个英文 mirror，缺失配对 0**。

## 4. 已修复的高风险语义不同步

本轮特别修复了：

1. 英文 Methodology Form Core 仍写“英文以后再开发”的旧状态；
2. 英文模板仍按 HARC v0.1 / 单语文件初始化；
3. 中文方法论文章的上游链接仍指向旧英文路径；
4. 英文方法论文章错误指向不存在的 `METHODOLOGY_SOURCES.en.md`；
5. 英文 Whitepaper 与中文 Whitepaper 结构已经分叉；
6. Roadmap / Contributing 尚未包含双语治理要求；
7. English Protocol Core 残留旧版本范围说明；
8. Agent onboarding 尚未统一优先读取中文 canonical。

## 5. 一致性边界

本次审计确认：

- 文件配对完整；
- 已知高风险结构/状态差异已修复；
- 规范文件明确中文优先级；
- 新项目模板已经继承双语规则。

但应明确：

> **文件配对不等于数学上证明两种语言永远语义等价。**

翻译仍可能产生细微语义偏差。因此未来每一次实质编辑都必须把 parity check 作为完成条件。自动语义 parity 工具属于后续 Roadmap。

## 6. 以后每次修改的完成标准

一次实质性修改只有在以下条件满足时才能标记完成：

1. 中文 canonical 已更新；
2. 英文 mirror 已更新；
3. 主张、范围、批准状态、未决问题与引用关系没有实质不一致；
4. 上游/下游需要同步的状态文件已经同步；
5. 如发现冲突，以中文为准修复英文。

## 7. 结论

HARC 初始仓库级双语迁移已经完成。

**审计状态：`PASS — INITIAL BILINGUAL MIGRATION COMPLETE`**

HARC-D015 可以从“implementation in progress”更新为“implemented”，但这一状态表示**初始历史迁移完成**，不意味着未来修改可以跳过双语同步。

后续每次 Agent 工作仍必须遵守：

> **先维护中文 canonical，再在同一工作轮次维护英文 synchronized mirror。**
