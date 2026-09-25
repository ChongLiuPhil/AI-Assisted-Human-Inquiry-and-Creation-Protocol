# HARC Project Working Memory Index

> **本中文文件是规范性基准；英文 `working-memory.md` 是同步 mirror。**

Working Memory 是一个功能区，不要求必须是单一文件。

默认模板采用：

- Current Focus：`docs/working-memory/current-focus.zh-CN.md`
- Task Plan：`docs/working-memory/task-plan.zh-CN.md`
- Work Log：`docs/working-memory/work-log.zh-CN.md`

## 默认接管

1. 读本 Index；
2. 读 Current Focus；
3. 读 Task Plan；
4. 如果存在 `project-bootstrap-state.yaml` 且当前任务涉及基础设施 / Provider，读取最近 verified bootstrap state；
5. 按当前任务读取三层 Long-Term Memory；
6. 默认不读 Work Log。

## 角色

- **Current Focus**：现在最重要的事；
- **Task Plan**：接下来怎么推进；
- **Work Log**：供人类以后回顾“我们怎么走到这里”。
- **External Operational State**（存在时）：`project-bootstrap-state.yaml` 保存外部 Provider bootstrap 的最近 verified 非秘密状态；当前 blocker / next action 仍镜像到 Current Focus / Task Plan。

Work Log 不是长期实质性真值源，也不记录 AI 隐藏 chain-of-thought。

轻量项目可把多个角色合并到一个文件，但必须在 `HARC_MANIFEST.yaml` 中显式映射。
