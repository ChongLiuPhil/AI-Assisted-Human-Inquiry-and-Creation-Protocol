# AHICP Working Memory — Current Focus
## 当前焦点

> **中文 canonical；英文 `current-focus.md` 为同步 mirror。**

**状态：** `ACTIVE`  
**最后更新：** 2026-09-19

## CURRENT_STAGE

仓库正在执行 **HARC → AHICP v0.3 语义迁移**。

本次迁移由 `AHICP-D026` 明确授权，不是简单改名。目标是保留现有成熟治理架构，同时把协议的默认范围从 research 上位化为 human-led inquiry / research / reasoning / writing / creation with AI assistance，并确保规范语言不把 AI 表述为与人对称的认知主体或最终责任主体。

已完成：
- 新正式名称与 subtitle；
- README / Specification / AGENTS / onboarding 入口第一阶段迁移；
- `AHICP_MANIFEST.yaml` 与 `AHICP_CONTEXT_INTERFACE.yaml`；
- 旧 `HARC_*` 控制文件降级为 compatibility pointer；
- 双语 semantic migration plan；
- Protocol Core 初步泛化；
- `AHICP-D026` 进入 Decision Log。

## CURRENT_OBJECTIVE

### WM-OBJ-004 — 完成 AHICP v0.3 repository-wide semantic migration

当前目标是逐文件完成 Phase C：

1. **GENERALIZE** — 原本只是因为旧项目默认 research 而使用的研究限定语言；
2. **RETAIN RESEARCH-SPECIFIC** — 真正讨论证据、研究诚信、方法论文章、学术政策等内容；
3. **PRESERVE HISTORICAL** — HARC-D001–HARC-D025 等历史审计标识与历史事实；
4. **MIGRATE LEGACY IDENTIFIER** — 当前控制文件、模板、启动链中的 HARC 名称与路径。

## IMMEDIATE_NEXT_ACTION

- 迁移 research-project template 的控制文件到 AHICP 名称，同时保留其作为 **research-specific specialization**；
- 为通用 inquiry / creation template 预留独立层，而不是把 research template 强行改成所有项目唯一模板；
- 更新 Architecture / Roadmap / Working Memory 中的 live references；
- 生成 Phase C semantic audit record；
- 最后执行 bilingual parity + zero-context onboarding + post-migration audit。

## PRIMARY_BLOCKER

`NONE` — 当前迁移有明确的人类授权。

## PARALLEL WAITING-HUMAN ITEMS

方法论文章仍保持：
- overall Working Framework Approval：`WAITING-HUMAN`;
- license：`WAITING-HUMAN`;
- target publication venue / form constraints：`WAITING-HUMAN`.

这些状态没有被 AHICP 迁移自动批准、拒绝或取消。

## HANDOFF

新的 AI Agent 应先读取本文件与 Task Plan，然后读取 `docs/AHICP_SEMANTIC_MIGRATION_PLAN.zh-CN.md`、`AHICP-D026` 和任务相关文件。

不得把“仓库已经重命名”误解成“语义迁移已经完成”。
