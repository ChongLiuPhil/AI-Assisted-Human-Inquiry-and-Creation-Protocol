# AHICP Project Bootstrap Prompt

> **本中文文件是规范性基准；英文 `BOOTSTRAP_PROMPT.md` 是同步镜像。**

> 你正在接手一个 AHICP-governed research repository。
>
> 在任何实质工作前：
>
> 1. 读取 `START_HERE.zh-CN.md`；
> 2. 读取 `AHICP_MANIFEST.yaml`；
> 3. 读取 `AHICP_CONTEXT_INTERFACE.yaml`；
> 4. 读取 `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`；
> 5. 读取 `AGENTS.zh-CN.md`；
> 6. 读取 `docs/working-memory.zh-CN.md`（Index）；
> 7. 读取 `docs/working-memory/current-focus.zh-CN.md`；
> 8. 读取 `docs/working-memory/task-plan.zh-CN.md`；
> 9. 如果存在 `project-bootstrap-state.yaml`，读取它恢复最近一次已验证的外部运行状态；
> 10. 默认跳过 Work Log；只有历史回顾、审计、变迁重建或 current/history conflict 时才读取；
> 11. 按 manifest / context-interface 的 task route 从三层长期记忆按需读取项目状态；
> 12. 按 `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` 输出 AHICP Onboarding Report，并确认 `AHICP REPOSITORY CONTEXT — ACTIVE`。
>
> 中文是 canonical；英文是 synchronized mirror。
>
> 不得把 AI 提议当成人类承诺，不得把 Working Framework 当 Approved Framework，不得忽略 `BLOCKING` clarification。
>
> 高影响不确定性执行：
>
> `ambiguity -> Working Memory / Clarification -> human resolution -> Promotion -> Decision Log -> appropriate Long-Term Memory destination`
>
> 人类明确决定执行：
>
> `human decision -> Decision Log -> appropriate Core -> Argument Map -> Artifact -> bilingual parity`
>
> 如果无法仅凭仓库重建当前状态，停止大规模工作并报告 onboarding/persistence defect。Provider/UI 配置状态也不例外：不得用聊天记忆替代 `project-bootstrap-state.yaml` 或 Working Memory 写回。
