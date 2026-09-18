# START HERE — HARC 零上下文接管入口

> **本中文文件是规范性基准；英文 `START_HERE.md` 是同步镜像。**
>
> 本文件面向一个**从零上下文开始、没有旧聊天记录、没有平台记忆**的新 AI Agent。

## 0. 第一原则

在进行任何实质性研究、结构修改、正文扩写、翻译、格式修改或批准判断之前：

**先重建仓库当前状态，不要从当前聊天猜测项目状态。**

HARC 的持久真值源在仓库，不在旧 Agent 的记忆中。

## 1. 强制读取顺序

按以下顺序读取中文 canonical；英文仅用于同步核验：

1. `HARC_MANIFEST.yaml`
2. `HARC_CONTEXT_INTERFACE.yaml`
3. `BOOTSTRAP_PROMPT.zh-CN.md`
4. `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
5. `AGENTS.zh-CN.md`
6. `protocol/ONBOARDING_HANDSHAKE.zh-CN.md`
7. `core/PROTOCOL_CORE.zh-CN.md`
8. 最近的 `core/DECISION_LOG.zh-CN.md`
9. 根据当前任务按需读取 Content/Form/Protocol Core
10. `docs/clarification-register.zh-CN.md`（如任务相关）
11. Framework Status / Approved Framework / Working Argument Map（如任务相关）
12. 与当前任务直接相关的 evidence / artifact
13. 对应英文 mirror，仅用于 parity 核验

对于 HARC 方法论文章，具体路径由 `HARC_MANIFEST.yaml` 给出。

## 2. 零上下文接管时禁止做的事

在完成接管握手之前，不得：

- 假设聊天中的表述已经进入规范状态；
- 把 AI 提议写成人类承诺；
- 把未解决 clarification 当作已解决；
- 创建 Approved Framework；
- 大规模重构 Working Argument Map；
- 大规模改写正文；
- 依据英文 mirror 覆盖中文 canonical；
- 忽略已有 `BLOCKING` clarification；
- 根据工具默认值推断作者偏好。

## 3. 接管握手：必须先输出 Onboarding Report

完成强制读取后，新 Agent 应先向人类输出一个简短但结构化的 **HARC Onboarding Report**。推荐直接使用：`ONBOARDING_REPORT_TEMPLATE.zh-CN.md`。报告中还必须根据 `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` 确认：

`HARC REPOSITORY CONTEXT — ACTIVE`

它只加载仓库访问内核，不复制动态项目状态。Onboarding Report 中的状态摘要仅用于人类验证；后续不得把该摘要当作权威状态，必须按需读取 GitHub 最新 canonical revision。至少包含：

### A. 协议状态

- 当前采用的 HARC version / commit（如记录）；
- canonical language；
- 当前适用的主要协议文件；
- 是否发现协议版本或文件同步缺陷。

### B. 人类当前已确认的状态

- 当前核心研究目的；
- 当前主要人类承诺；
- 当前形式/呈现决定；
- 最近的重要人类决定。

### C. Critical Clarification 状态

- 当前所有 `BLOCKING` clarification；
- 与当前任务有关的 `NON-BLOCKING` clarification；
- 哪些问题必须先问人类才能继续。

### D. Framework / Artifact 状态

- Working Framework 状态；
- 最新 Approved Framework（如有）；
- 当前派生成果状态；
- Framework Approval / Final Artifact Approval 是否完成。

### E. 当前允许的下一步

Agent 应说明：

- 可以安全继续哪些工作；
- 哪些工作被 blocking clarification 或 approval gate 阻塞；
- 当前用户请求将通过哪条 HARC propagation path 落实。

## 4. 人类反馈进入项目后的标准流程

### 如果人类给出明确决定

`Human decision -> Decision Log -> appropriate Core -> Clarification cleanup if needed -> Working Argument Map -> Derived Artifact -> bilingual parity check`

### 如果人类表达存在高影响歧义

`Ambiguous high-impact input -> Clarification Register -> human resolution -> Decision Log -> appropriate Core -> Working Argument Map -> Derived Artifact`

### 如果只是 AI 提议

保持 `AI-PROPOSED`，不得提升到人类 Core，除非人类明确接受。

## 5. Clarification 优先规则

如果 Agent 对以下任何内容存在非微不足道且高影响的不确定性，应先进入 Clarification Register：

- 核心观点；
- 中心命题；
- 关键概念；
- 主要推论关系；
- 范围与限定；
- 章节功能；
- 作者母语中的关键术语；
- 母语与英文的对应；
- 会改变 framework 的结构性解释。

不要因为“最可能是这样”就跳过人类确认。

## 6. 双语规则

默认情况下：

`Human decision -> Chinese canonical -> English synchronized mirror`

中文先发展，英文同步。

切换前历史文件若存在英文领先，只适用一次性的 legacy catch-up；不要把该例外用于正常新工作。

## 7. 接管成功标准

只有当新 Agent 能够仅根据仓库回答以下问题，才算接管完成：

1. 人类当前究竟确认了什么？
2. 哪些内容仍只是 AI 提议？
3. 哪些高影响问题正在等待人类澄清？
4. 当前 Working / Approved Framework 是什么状态？
5. 当前成果处于什么批准状态？
6. 下一步哪些工作允许进行，哪些被阻塞？
7. 中文 canonical 与英文 mirror 是否同步？

如果不能回答，先修复 onboarding / persistence defect，不要继续大规模研究工作。

---

# 可直接复制给任意 AI Agent 的启动提示词

> 你正在接手一个遵循 Human–AI Research Collaboration Protocol（HARC）的研究仓库。不要依赖旧聊天、账号记忆或你自己的先验推断来重建项目状态。首先读取仓库根目录的 `START_HERE.zh-CN.md` 和 `HARC_MANIFEST.yaml`，然后严格按照其中的 required read order 读取规范状态。中文是 canonical，英文是同步 mirror。完成读取后，在做任何实质性修改之前，先向我输出一份 HARC Onboarding Report：说明当前人类承诺、Form 状态、Blocking/Non-blocking Clarifications、Working/Approved Framework 状态、Artifact 状态、同步缺陷，以及当前请求允许的下一步。如果遇到可能显著影响核心命题、关键概念、术语/翻译、范围、推论关系或论证结构的不确定性，不要猜测；先写入 Clarification Register 并向我确认。任何人类明确决定都必须先进入 Decision Log 与相应 Core，再传播到 Argument Map 和派生成果。未经显式 Framework Approval，不得把 Working Framework 当作人类已批准结构。
