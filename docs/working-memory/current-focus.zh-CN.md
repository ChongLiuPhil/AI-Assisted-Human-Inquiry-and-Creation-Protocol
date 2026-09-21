# AHICP Working Memory — Current Focus
## 当前焦点

> **中文 canonical；英文 `current-focus.md` 为同步 mirror。**

**状态：** `ACTIVE`  
**最后更新：** 2026-09-21

## CURRENT_STAGE

**方法论文章已依据 AHICP-D030 完成 project-memory-centered 结构性升级；当前进入人类审阅与框架确认阶段。**

### 仍然有效的协议治理依据

本轮论文工作不替代既有协议治理。当前仍然有效并必须继续遵守：

- `AHICP-D027` — external systems / tool discovery / authorization / human handoff；
- `AHICP-D028` — reusable authorization policy 首次配置时由 AI 提出方案、人类选择；
- `AHICP-D029` — scoped authorization、proposal / authorization / execution / verification / durable write-back 分离；
- `AHICP-D030` — 本轮 methodology article 的 project-memory-centered 结构升级授权。

因此，论文成为当前工作焦点，不表示 D027–D029 的执行与授权规则失效。

本轮已经完成：

- 记录 `AHICP-D030`：现有 methodology article 保持为一篇统一论文；
- 将 Project Memory Architecture、Working Memory continuity、Agent/Model substitution、Human Decision Persistence 提升为核心理论贡献；
- 在 Article Content Core 中新增 C17–C22；
- 把 Working Argument Map 重构为 13 节 project-memory-centered framework；
- 重写中文 methodology article；
- 同步重写英文镜像；
- 补充 Generative Agents、MemGPT、Agent-memory survey、LongMemEval、MemBench、RealMem 与 W3C PROV 相关 evidence / references；
- 完成第二轮 scholarly novelty audit：加入 organizational memory、Weiser & Morrison (1998) Project Memory、Mariano & Awazu (2024)、design rationale / Software Architecture Knowledge Management 与 decision provenance 前史；
- 明确 AHICP 不首创 project memory；当前 novelty 只以 governed, model-substitutable Project Memory Architecture 的 candidate synthesis 表述；
- 把经验测试方案从旧的 AI-proposed 状态更新为 AHICP-D030 已确认应纳入论文的 proposed evaluation framework；
- 明确没有实证结果，不得提出已验证 effectiveness claim；
- 更新 Framework Status，使仓库不再保留“整体批准前禁止结构性重写”的旧指令。

## CURRENT_OBJECTIVE

### WM-OBJ-004 — Project-memory-centered methodology article human review

当前主要对象：

1. `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`
2. `paper/METHODOLOGY_ARTICLE.zh-CN.md`
3. `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`

当前 framework 状态：

`WORKING-FRAMEWORK — REVISED UNDER AHICP-D030 / HUMAN REVIEW PENDING`

当前文章状态：

`DERIVED-PROVISIONAL — STRUCTURALLY REWRITTEN UNDER AHICP-D030`

## IMMEDIATE_NEXT_ACTION

本轮机器工作完成后：

1. 人类审阅新的 project-memory-centered framework 与论文；
2. 后续明确选择：
   - `APPROVE`
   - `REVISE`
   - `REJECT`

在整体 `APPROVE` 前，不创建 `MA-FW-001`。

## PRIMARY_BLOCKER

当前没有阻止完成本轮结构性重写的 blocker。

下一治理门是：

`WAITING-HUMAN: review of revised methodology framework and article`

另外仍存在：
- license：`WAITING-HUMAN`
- target publication venue / form constraints：`WAITING-HUMAN`

## HANDOFF

新的 AI Agent 应知道：

- AHICP-D030 已授权并完成本轮论文结构重写；
- “论文必须等 Framework Approval 才能结构性重写”是旧状态，不得恢复；
- 重写后的 framework **尚未整体批准**；
- evaluation framework 已被确认应纳入论文，但没有实证结果；
- 中文论文为 canonical，英文为 synchronized mirror；
- 下一步是验证、PR、人类审阅，而不是继续无边界扩写。