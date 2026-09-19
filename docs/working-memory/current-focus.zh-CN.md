# AHICP Working Memory — Current Focus
## 当前焦点

> **中文 canonical；英文 `current-focus.md` 为同步 mirror。**

**状态：** `ACTIVE`  
**最后更新：** 2026-09-20

## CURRENT_STAGE

**AHICP v0.3 语义迁移已完成；后续 external-system authorization / human-handoff 与 scoped authorization 治理也已完成规范收束。**

迁移依据：`AHICP-D026`。  
后续授权治理依据：`AHICP-D027`、`AHICP-D028`、`AHICP-D029`。

已完成：
- 正式名称与固定 subtitle；
- human-led / AI-assisted / repository-grounded 规范方向；
- Protocol Core、Specification、AGENTS 与 live protocol 文档迁移；
- `AHICP_MANIFEST.yaml` / `AHICP_CONTEXT_INTERFACE.yaml` 控制面；
- zero-context onboarding 控制链迁移；
- research-project specialization template 迁移；
- 方法论文章/evidence 的当前协议身份迁移，同时保留 research-specific 主题；
- 关键双语规范 semantic parity；
- final post-migration repair audit；
- provider-neutral machine-operable-first escalation、authorization / human handoff 与 provider actual-state write-back；
- scoped authorization lifecycle：`proposal != authorization != execution != verification != durable write-back`；
- 首次配置 reusable authorization policy 时由 AI 提出方案、人类选择，选择及其 scope / provenance / escalation conditions 持久记录；
- PR #3 合并后的独立 consistency review 与传播修复。

最近的 protocol repair 已关闭以下问题：
- D028 的 durable authorization record 在下游规范中被弱化；
- Specification §23.3 漏列 `permission grants`；
- Working Memory 未记录 D028/D029 与 PR #3 milestone；
- Protocol Contract CI 对 §23.5.1 只做全文件 marker 检查、未校验 section-local invariant。

## CURRENT_OBJECTIVE

### WM-OBJ-003 — 方法论文章整体 Framework Approval

protocol maintenance 完成后，仓库的主要未决工作门仍为：

- 方法论文章 Working Framework：`WAITING-HUMAN`
- license：`WAITING-HUMAN`
- target publication venue / form constraints：`WAITING-HUMAN`

当前中文 Working Framework：

`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`

## IMMEDIATE_NEXT_ACTION

人类在准备继续方法论文章时，对当前 Working Framework 作：

- `APPROVE`
- `REVISE`
- `REJECT`

在此之前，不创建 Approved Framework snapshot。

## PRIMARY_BLOCKER

`WAITING-HUMAN: methodology article overall Framework Approval`

这不阻塞已经完成的 AHICP protocol migration 与 authorization-governance maintenance。

## HANDOFF

新的 AI Agent 应按 AHICP control plane 接管，并以 repository `main` 的最新 revision 为唯一项目状态来源。D027–D029 已是当前授权治理依据；旧 HARC live identifiers 不应重新进入当前规范文件。