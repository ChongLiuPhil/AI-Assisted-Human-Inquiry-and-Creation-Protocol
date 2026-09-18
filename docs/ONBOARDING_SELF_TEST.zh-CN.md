# Zero-Context Onboarding Self-Test
## 零上下文接管自举测试

**日期：** 2026-09-18  
**状态：** `PASS WITH EXPECTED BLOCKING CLARIFICATIONS`  
**性质：** AI 维护的 onboarding/conformance 审计，不是新的规范真值源。  
**语言：** 中文 canonical；英文 `ONBOARDING_SELF_TEST.md` 是同步 mirror。

## 1. 测试方法

模拟一个没有旧聊天、没有账号记忆的新 AI Agent，仅按照：

1. `HARC_MANIFEST.yaml`
2. `HARC_CONTEXT_INTERFACE.yaml`
3. `START_HERE.zh-CN.md`
4. `BOOTSTRAP_PROMPT.zh-CN.md`
5. `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
6. `AGENTS.zh-CN.md`
7. manifest/context-interface 按当前任务解析出的 Protocol / Decision / Clarification / Article 状态文件

重建当前项目。

本测试不把当前对话中的未持久化信息作为状态来源。

---

# 2. 模拟 HARC Onboarding Report

## A. 协议状态

- HARC version：`0.2.0-draft`
- canonical language：`zh-CN`
- English：synchronized mirror
- 零上下文入口：
  - `START_HERE.zh-CN.md`
  - `BOOTSTRAP_PROMPT.zh-CN.md`
  - `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
  - `HARC_MANIFEST.yaml`
  - `HARC_CONTEXT_INTERFACE.yaml`
  - `AGENTS.zh-CN.md`
  - `protocol/ONBOARDING_HANDSHAKE.zh-CN.md`
  - `ONBOARDING_REPORT_TEMPLATE.zh-CN.md`
- 当前主要协议决定：P1–P22
- 最近人类协议决定：HARC-D015 至 HARC-D020
- D018、D019 与 D020 已由人类明确确认并实施；D020 将 D019 的动态 Session Contract 收缩为最小 Repository Resolver。

**协议状态结论：** 可从仓库发现并重建。

## B. 人类已确认的当前状态

### B1. HARC 项目目的

HARC 是独立、GitHub-centered、可复用的人机研究协作协议，同时产出：

1. 可执行开放协议/模板；
2. 受 HARC 自身治理的方法论文章。

### B2. 当前主要人类承诺

仓库可恢复至少以下已确认原则：

- 项目持久状态必须外部化到仓库，而不是依赖聊天/Agent 记忆；
- Content 与 Form 分离；
- 人类决定上游优先传播；
- AI 维护 Working Argument Map，但不自动获得人类认可；
- Framework Approval 与 Final Artifact Approval 分离；
- AI 扩写必须保持 framework fidelity；
- 中文 canonical / 英文 synchronized mirror；
- 高影响不确定性进入 Layer 1.5 Critical Clarification Register；
- 新 Agent 必须经过 zero-context bootstrap + Onboarding Handshake 才进入实质工作。

### B3. 方法论文章 Form 状态

- 成果类型：`ACADEMIC_PAPER / METHODOLOGY ARTICLE`
- 中文：canonical
- 英文：synchronized mirror
- 详细字体、版式、引用样式、目标发布渠道：`UNRESOLVED`
- 当前 Markdown / author–year 样式：工作默认值，不是永久作者偏好。

## C. Critical Clarification 状态

### C1. 当前 Blocking

- `CLR-001` — 方法论文章中心责任概念；
- `CLR-002` — Framework Responsibility Thesis 强度；
- `CLR-005` — `responsibility concentration` 是否保留/替换。

这些条目阻塞 `MA-FW-001`。

此外：

- `CLR-009` 对正式开放许可 / release 是 `BLOCKING`，但不阻塞当前方法论文章 framework 讨论。

### C2. 当前 Non-blocking

- `CLR-003` — `semantic version control`；
- `CLR-004` — `generation–verification asymmetry`；
- `CLR-006` — extended/distributed cognition 理论地位；
- `CLR-007` — 经验验证计划；
- `CLR-008` — 学科/投稿方向。

## D. Framework 状态

- Working Framework：`WORKING-FRAMEWORK — REVIEW READY / CLARIFICATION GATE OPEN`
- 最新 Approved Framework：**无**
- 下一标识符：`MA-FW-001`
- Framework Approval：`NOT COMPLETED`
- Clarification Gate：`OPEN`
- 允许创建 `MA-FW-001`：**否**

**正确行为：** 先解决或由人类明确 defer `CLR-001 / CLR-002 / CLR-005`，再进行整体 Framework Approval。

## E. Artifact 状态

- 中文：`paper/METHODOLOGY_ARTICLE.zh-CN.md`
- 英文：`paper/METHODOLOGY_ARTICLE.en.md`
- 状态：`DERIVED-PROVISIONAL`
- Working Framework -> 当前正文：`PARTIALLY SYNC`
- Final Artifact Approval：`NOT COMPLETED`

**正确行为：** 当前不应进行假定 framework 已批准的大规模结构性重写，也不得描述为最终可投稿稿。

## F. Evidence 状态

- 主要 evidence 文件：`evidence/METHODOLOGY_SOURCES.zh-CN.md`
- 当前政策/文献核验状态：`RECHECKED 2026-09-17`
- 目标渠道确定后仍需重新核验 venue-specific 时效性政策。

## G. 双语状态

- 中文 canonical；
- 英文 synchronized mirror；
- 当前仓库要求任何实质性中文编辑在同一工作轮次同步英文；
- legacy English-ahead catch-up 仅为历史迁移例外，不适用于正常新工作。

## H. 当前允许的下一步

### 可以安全执行

- 继续协议实现、审计与 onboarding infrastructure 改进；
- 向人类呈现 Clarification Register 中的问题；
- 对不依赖 Blocking Clarification 的证据、非实质性维护和一致性检查继续工作；
- 在不假定答案的前提下准备候选分析。

### 当前被阻塞

- 创建 `MA-FW-001`；
- 宣称方法论文章 framework 已获人类批准；
- 基于未解决 `CLR-001 / 002 / 005` 大规模锁定文章哲学 framing；
- Final Artifact Approval；
- 在许可未决定前把公开仓库描述为已完成法律意义上的 open-source/open-content 授权。

## J. Repository Context Resolver

测试 Agent 根据 `HARC_CONTEXT_INTERFACE.yaml` 与 `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` 激活：

```text
HARC REPOSITORY CONTEXT — ACTIVE

Source of truth:
- GitHub repository

Control:
- HARC_MANIFEST.yaml
- HARC_CONTEXT_INTERFACE.yaml

Policy:
- repository-backed
- selective retrieval
- no authoritative session copy
- read latest before high-impact action
- read latest before write
- invalidate touched cache after write
- write-through to repository

Current task:
- route: PROTOCOL
- authoritative refs:
  - core/PROTOCOL_CORE.zh-CN.md
  - core/DECISION_LOG.zh-CN.md
  - protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md
```

**Repository context active：`YES`**

动态 Blocking Clarifications、Framework 与 Artifact 状态仍由测试 Agent从相应 GitHub canonical 文件 fresh-fetch；没有复制进 resolver。

## I. Onboarding 结论

**`PASS`**

理由：

- 新 Agent 可仅凭仓库识别人类/AI 权威边界；
- 可发现 Blocking Clarifications；
- 可正确判断没有 Approved Framework；
- 可正确判断当前 Artifact 为 `DERIVED-PROVISIONAL`；
- 可识别中文 canonical / 英文 mirror；
- 可判断哪些下一步被 gate 阻塞；
- 可激活 Repository Resolver，而不复制动态项目状态；
- 可根据任务从 GitHub latest canonical revision fresh-fetch 当前状态；
- 可把会话旧摘录正确视为非权威缓存。

测试中发现的入口编号和 standalone prompt/report 可发现性缺陷已在测试前修复。

---

# 3. Conformance 结论

当前 HARC 仓库已经具备一个可工作的 zero-context onboarding 路径：

`Repository access -> Manifest / Context Interface -> Selective Retrieval -> Onboarding Report -> Repository Resolver -> Gated Work`

该测试只能证明**当前仓库状态可以支持一次成功的自举接管**，不能证明所有外部 AI 平台都会自动发现入口文件。

因此实际跨平台使用仍建议人类显式给出一句启动指令：

> **“请读取本仓库的 BOOTSTRAP_PROMPT.zh-CN.md 并严格执行。”**

未来应使用多个不同 Agent / 平台重复该测试，形成 cross-agent handoff benchmark。
