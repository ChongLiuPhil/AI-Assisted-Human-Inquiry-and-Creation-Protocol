# HARC Bootstrap Prompt

> **本中文文件是规范性基准；英文 `BOOTSTRAP_PROMPT.md` 是同步镜像。**

下面这段提示词可以直接复制给任何能够读取项目仓库的 AI Agent。

---

> 你正在接手一个遵循 Human–AI Research Collaboration Protocol（HARC）的研究仓库。
>
> 你必须把 GitHub 仓库状态，而不是旧聊天、账号记忆、平台记忆、隐藏 scratchpad 或你自己的先验推断，作为项目的持久状态来源。
>
> 在进行任何实质性研究、结构修改、正文扩写、翻译、格式修改、Framework Approval 或 Final Artifact 判断之前：
>
> 1. 读取 `START_HERE.zh-CN.md`；
> 2. 读取 `HARC_MANIFEST.yaml`；
> 3. 读取 `HARC_CONTEXT_INTERFACE.yaml`；
> 4. 读取 `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`；
> 5. 读取 `AGENTS.zh-CN.md`；
> 6. 严格按照 manifest / context interface 的 task route 按需读取当前规范状态；
> 7. 中文是 canonical；英文只作为 synchronized mirror；
> 8. 仅在当前任务需要时读取并汇总 `BLOCKING` / `NON-BLOCKING` Clarifications；
> 9. 仅在当前任务需要时读取 Framework / Artifact / Evidence 的最新 canonical revision；
> 10. 在做任何实质性修改前，先按 `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` 输出 HARC Onboarding Report，并确认 `HARC REPOSITORY CONTEXT — ACTIVE`。后续动态状态不得依赖该报告副本，必须从 GitHub 按需 fresh-fetch。
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
> 如果某个不确定性可能显著影响核心命题、关键概念、术语/翻译、范围、主要推论关系、章节功能或整体论证结构，则先进入 Clarification Register：
>
> `ambiguity -> Clarification Register -> human resolution -> Decision Log -> appropriate Core -> Working Argument Map -> Derived Artifact`
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
