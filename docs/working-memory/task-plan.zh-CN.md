# AHICP Working Memory — Task Plan
## 动态任务计划

> **中文 canonical；英文 `task-plan.md` 为同步 mirror。**

**状态：** `ACTIVE TASK PLAN`

## 1. ACTIVE TASKS

- `WM-T016` — AHICP v0.3 repository-wide semantic migration：`SUBSTANTIALLY COMPLETED`
- `WM-T017` — AHICP project templates/control-plane migration：`COMPLETED`
- `WM-T018` — v0.3 structural validation completed；semantic bilingual parity + post-migration audit：`IN PROGRESS`
- `WM-T015` — 方法论文章整体 Framework Approval：`WAITING-HUMAN / PARALLEL`
- `WM-T013` — license 决定：`WAITING-HUMAN`
- `WM-T014` — target publication venue / form constraints：`WAITING-HUMAN`

## 2. NEXT ACTIONS

1. 对关键中英文规范文件执行语义级 parity 审计，而不仅是文件配对；
2. 检查剩余 live navigation / repository URL / identifier 是否需要迁移；
3. 执行独立 post-migration repair audit；
4. 上述检查通过后，PR 才具备合并条件。

已完成的结构验证：
- `AHICP_MANIFEST.yaml` 路径候选 33，缺失 0；
- 中文 `*.zh-CN.md` 文件 62，缺失英文 mirror 0；
- zero-context control chain 已全部指向 AHICP 控制文件；
- research-project template 已迁移到 AHICP 控制面并保留 research specialization。

## 3. MIGRATION INVARIANTS

- 名称：**AI-Assisted Human Inquiry and Creation Protocol**。
- Subtitle：**A protocol for human-led inquiry, research, reasoning, writing, and creation with AI assistance.**
- 人类保持目的、方向、实质判断、批准与最终责任。
- AI 是辅助系统；大量执行工作不等于成为对称认知主体。
- 历史事实不因重命名而重写。
- research-specific 内容不因范围泛化而被错误去学术化。
- AHICP 不复制 PPF 的 publishing lifecycle 规则。
- 中文 canonical / 英文 mirror 同步治理继续有效。

## 4. PARALLEL METHODOLOGY ARTICLE GATES

仍未改变：
- overall Framework Approval：`WAITING-HUMAN`;
- `CLR-009` license：formal release 前 blocking；
- `CLR-010` target venue / publication form：final publication 前 blocking。

## 5. COMPLETION RULE

迁移完成必须同时满足：

`semantic migration complete + bilingual parity + control-path consistency + zero-context onboarding pass + post-migration audit pass`

仅完成仓库重命名或 README 改名不算完成。
