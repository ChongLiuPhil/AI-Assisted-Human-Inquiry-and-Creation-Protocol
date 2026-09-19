# Clarification Workflow inside AHICP Working Memory
## AHICP 工作记忆中的澄清流程

> **本中文文件是规范性基准；英文 `CLARIFICATION_REGISTER.md` 是同步镜像。**

## 状态

原先将 Critical Clarification Register 描述为 “Layer 1.5” 的模型已经被 HARC-D021 取代。

Clarification 现在是 `Working Memory` 中的一种 item type，不再构成独立层。

当前活跃 Clarification / pending-decision 状态：

`docs/working-memory/task-plan.zh-CN.md`

Working Memory Index：

`docs/working-memory.zh-CN.md`

完整 Working Memory 规则：

`protocol/WORKING_MEMORY.zh-CN.md`

## 何时创建 Clarification item

当 AI 对下列内容存在高影响、非微不足道的不确定性时，应在 Working Memory 创建 Clarification：

- 作者意图；
- 核心命题；
- 关键概念；
- 范围 / 限定；
- 推论关系；
- 章节功能；
- 关键术语；
- 母语 / 英文对应；
- 新反馈与既有长期记忆的冲突。

不得自行猜测后静默传播。

## Clarification item 最小字段

- ID；
- 状态；
- `BLOCKING / NON-BLOCKING` severity；
- 类别；
- 不确定点；
- 候选解释；
- 为什么重要；
- 受影响的长期记忆目标；
- AI 建议（如有，`AI-PROPOSED`）；
- 需要人类回答的问题。

## Resolution / Promotion

人类确认后：

`Working Memory Clarification -> Decision Log -> appropriate Long-Term Memory destination`

如果涉及人类核心内容：

`Layer 1 Core -> Layer 2 Framework -> Layer 3 Artifact`

Form / Protocol 决定进入相应长期 Core；纯结构性 framework 结果进入 Layer 2。

完成 Promotion 后：

- item 标记 `RESOLVED / PROMOTED`；
- 记录 Decision ID；
- 记录长期目标文件；
- 从 Active Clarification 区退出。

## Compatibility

旧路径 `docs/clarification-register.zh-CN.md` 保留为兼容指针，以避免旧 Agent、旧链接或历史引用失效。

新的 active Clarification 状态只维护在 `docs/working-memory/task-plan.zh-CN.md`，不得同时维护两份 Clarification 真值源。
