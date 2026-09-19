# AHICP Working Memory Index
## 工作记忆区索引

> **本中文文件是规范性基准；英文 `working-memory.md` 是同步 mirror。**

**角色：** Working Memory Area 的稳定解析入口。  
**注意：** 本文件不复制动态任务状态；它只说明各逻辑角色在哪里。

## 逻辑组件

### 1. Current Focus — 当前焦点

路径：

`docs/working-memory/current-focus.zh-CN.md`

用途：

- 当前阶段；
- 当前最核心目标；
- 本轮/最近期工作要点；
- 最重要 blocker；
- 立即 next action。

**新 Agent 接管时优先级最高。**

### 2. Task Plan — 动态任务计划

路径：

`docs/working-memory/task-plan.zh-CN.md`

用途：

- active tasks；
- TODO / backlog；
- WAITING-HUMAN / BLOCKED；
- pending human decisions / Clarifications；
- next actions；
- 当前同步缺陷。

任务完成后应退出 active list。完成事项的历史摘要进入 Work Log；稳定规范结果另行 Promotion 到 Long-Term Memory。

### 3. Work Log — 工作日志

路径：

`docs/working-memory/work-log.zh-CN.md`

用途：

- 供人类作者回顾项目发展史；
- 阶段性进展；
- 重要工作转折；
- 思想/工作路径变化；
- 完成的任务批次；
- 里程碑。

**默认不属于 AI onboarding 必读内容。**

AI 只有在下列情况才按需读取：

- 人类要求历史回顾；
- 需要重建工作/思想变迁；
- 当前状态与历史存在明显冲突；
- 专门审计。

Work Log 不保存 AI 隐藏 chain-of-thought 或 scratchpad。

## 默认接管顺序

`Manifest / Context Interface -> Working Memory Index -> Current Focus -> Task Plan -> task-relevant Long-Term Memory`

Work Log 不进入默认 mandatory-read chain。

## 权威边界

- 当前最重要目标：以 Current Focus 为准；
- 当前计划/任务/阻塞/待确认事项：以 Task Plan 为准；
- 历史纪要：以 Work Log 为准，但它不覆盖当前状态；
- 长期实质性主张：以 Layer 1 / Layer 2 / Layer 3 canonical 文件为准。

## 单文件兼容

轻量项目可以把 Index、Current Focus、Task Plan、Work Log 映射到同一文件；复杂项目可以拆分。Manifest 必须显式说明映射。
