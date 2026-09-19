# AHICP Working Memory — Task Plan
## 动态任务计划

> **中文 canonical；英文 `task-plan.md` 为同步 mirror。**

**状态：** `ACTIVE TASK PLAN`

## 1. ACTIVE TASKS

- `WM-T016` — AHICP v0.3 repository-wide semantic migration：`IN PROGRESS`
- `WM-T017` — AHICP project templates/control-plane migration：`IN PROGRESS`
- `WM-T018` — v0.3 bilingual parity + onboarding + post-migration audit：`PENDING`
- `WM-T015` — 方法论文章整体 Framework Approval：`WAITING-HUMAN / PARALLEL`
- `WM-T013` — license 决定：`WAITING-HUMAN`
- `WM-T014` — target publication venue / form constraints：`WAITING-HUMAN`

## 2. NEXT ACTIONS

1. 完成 live protocol/core/template 中的 AHICP identifier 迁移；
2. 保留历史 HARC Decision IDs 和明确的历史叙述；
3. 把 `templates/research-project/` 明确为 research specialization，并迁移其控制文件；
4. 建立 Phase C audit，列出 GENERALIZE / RETAIN / PRESERVE / MIGRATE 四类；
5. 检查 broken references 与旧 repo URL；
6. 执行 bilingual parity；
7. 执行 zero-context onboarding self-test；
8. 执行独立 post-migration audit；
9. 上述检查通过后，PR 才具备合并条件。

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
