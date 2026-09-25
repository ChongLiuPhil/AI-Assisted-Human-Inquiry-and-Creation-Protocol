# HARC Project Working Memory — Task Plan

> **中文 canonical；英文 `task-plan.md` 为同步 mirror。**

**状态：** `ACTIVE TASK PLAN`

## ACTIVE TASKS

- `WM-T001 — ... — TODO / IN-PROGRESS / BLOCKED / WAITING-HUMAN`

## NEXT ACTIONS

1. `...`

## BLOCKERS

- `None / ...`

## PENDING HUMAN DECISIONS / CLARIFICATIONS

### CLR-001 — `...`

- Status: `WAITING-HUMAN`
- Severity: `BLOCKING / NON-BLOCKING`
- Uncertain point: `...`
- Candidate interpretations: `...`
- AI recommendation: `AI-PROPOSED — ...`
- Promotion destination: `Layer 1 / Layer 2 / Layer 3 / Form Core / Protocol Core`

## OPERATIONAL / PROVIDER STATE

- Project bootstrap state（存在时）：`project-bootstrap-state.yaml`
- 当前 pending human provider action：`None / ...`
- Agent resume condition：`None / ...`
- Memory write-back sync：`not-applicable / pending / synchronized`

规则：

- 人类进入 Provider UI 前，先把对应 human step 在 Bootstrap State 标记为 `waiting-human`，并在这里记录当前待办与恢复条件；
- 人类返回后先验证 actual Provider state，再把 Bootstrap State 写成 `completed / verified`；
- 如果 Bootstrap State 与 Provider actual state 不一致，把它记录为 SYNC DEFECT，不得用聊天内容覆盖。

## TODO / BACKLOG

- `...`

## SYNC DEFECTS

- `None / ...`

## COMPLETION RULE

任务完成后：

1. 从 active list 退出；
2. 将高层完成摘要写入 `work-log.zh-CN.md`；
3. 稳定规范结果 Promotion 到 Long-Term Memory；
4. 如当前目标改变，更新 Current Focus；
5. 如果任务改变了外部系统 / Provider 状态，同步 `project-bootstrap-state.yaml`；Provider/bootstrap 有实质推进时，在 Work Log 追加高层里程碑。
