# AHICP Bootstrap Prompt

> **本中文文件是规范性基准；英文 `BOOTSTRAP_PROMPT.md` 是同步镜像。**

下面这段提示词可以直接复制给任何能够读取项目仓库的 AI Agent。

---

> 你正在接手一个遵循 AI-Assisted Human Inquiry and Creation Protocol（AHICP）的研究仓库。
>
> 你必须把 GitHub 仓库状态，而不是旧聊天、账号记忆、平台记忆、隐藏 scratchpad 或你自己的先验推断，作为项目的持久状态来源。
>
> 在进行任何实质性研究、结构修改、正文扩写、翻译、格式修改、Framework Approval 或 Final Artifact 判断之前：
>
> 1. 读取 `START_HERE.zh-CN.md`；
> 2. 读取 `AHICP_MANIFEST.yaml`；
> 3. 读取 `AHICP_CONTEXT_INTERFACE.yaml`；
> 4. 读取 `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`；
> 5. 读取 `AGENTS.zh-CN.md`；
> 6. 读取 `docs/working-memory.zh-CN.md`（Index）；
> 7. 读取 `docs/working-memory/current-focus.zh-CN.md`，确定当前最重要目标、primary blocker 与 immediate next action；
> 8. 读取 `docs/working-memory/task-plan.zh-CN.md`，确定 active tasks、TODO、blockers、pending human decisions 与 next actions；
> 9. 默认不要读取 Work Log；只有历史回顾、审计、变迁重建或 current/history conflict 时才按需读取；
> 10. 严格按照 manifest / context interface 的 task route 从三层长期记忆按需读取当前规范状态；
> 11. 中文是 canonical；英文只作为 synchronized mirror；
> 12. 从 Task Plan 读取与当前任务相关的 blockers / clarifications，并在需要时核验其长期目标文件；
> 13. 仅在当前任务需要时读取 Layer 1 / Layer 2 / Layer 3 / Evidence 的最新 canonical revision；
> 14. 在做任何实质性修改前，输出 AHICP Onboarding Report，报告 Current Focus + Task Plan 的当前续接状态，并确认 `AHICP REPOSITORY CONTEXT — ACTIVE`。
>
> 你不得：
>
> - 把 AI 提议当成人类承诺；
> - 把 Working Framework 当成人类已批准 Framework；
> - 在存在高影响不确定性时自行猜测；
> - 忽略 `BLOCKING` clarification；
> - 用英文 mirror 覆盖中文 canonical；
> - 把临时工具默认值推断成人类偏好；
> - 在接管握手完成前进行大规模结构修改或正文重写。
>
> 如果某个不确定性可能显著影响核心命题、关键概念、术语/翻译、范围、主要推论关系、章节功能或整体论证结构，则先进入 Task Plan 中的 Clarification 队列：
>
> `ambiguity -> Working Memory / Clarification -> human resolution -> Promotion -> Decision Log -> appropriate Long-Term Memory destination`
>
> 如果人类给出明确决定，则执行：
>
> `human decision -> Decision Log -> appropriate Core -> clarification cleanup if needed -> Working Argument Map -> Derived Artifact -> bilingual parity check`
>
> 完成 Onboarding Report 后，只执行报告中被判定为安全、未被 blocking clarification 或 approval gate 阻塞的下一步。
>
> 如果你无法仅凭仓库重建当前项目状态，请停止大规模工作，并把它报告为 onboarding/persistence defect。

---

## 使用说明

推荐的人类启动方式：

> “请读取本仓库的 `BOOTSTRAP_PROMPT.zh-CN.md` 并严格执行。”

如果某个平台不会自动读取仓库文件，可以直接复制上面的提示词。
