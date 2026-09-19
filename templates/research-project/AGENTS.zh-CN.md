# AGENTS.md — 项目 AHICP 契约

本项目遵循 AI-Assisted Human Inquiry and Creation Protocol。

> **语言：** 中文文件为规范性基准；英文 `AGENTS.md` 为同步 mirror。采用本模板的新项目默认使用中文 canonical + 英文 synchronized mirror，除非人类明确选择其他语言治理方式。

## 零上下文接管

任何新 AI Agent 在实质性工作前必须先读取：

1. `START_HERE.zh-CN.md`
2. `AHICP_MANIFEST.yaml`
3. `AHICP_CONTEXT_INTERFACE.yaml`
4. `BOOTSTRAP_PROMPT.zh-CN.md`
5. `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
6. `docs/working-memory.zh-CN.md`
7. `docs/working-memory/current-focus.zh-CN.md`
8. `docs/working-memory/task-plan.zh-CN.md`

随后先用 Working Memory Index -> Current Focus -> Task Plan 确定续接点，再按 manifest / context interface 从三层长期记忆按需重建当前任务所需状态，并使用 `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` 输出 AHICP Onboarding Report；报告必须确认 `AHICP REPOSITORY CONTEXT — ACTIVE`。后续动态状态一律从 GitHub 最新 canonical revision 按需读取。

完成接管握手前，不得进行大规模结构修改、Framework Approval 或把 AI 提议提升为人类承诺。

## Working Memory

Working Memory Area 由 Index、Current Focus、Task Plan 与 Work Log 组成。Current Focus 保存“现在最重要的事”；Task Plan 保存动态任务、TODO、blockers、pending human decisions、clarifications 与 sync defects；Work Log 保存主要供人类回顾的阶段历史。

**Work Log 默认不属于新 Agent 的 onboarding 必读上下文。** 只有人类要求历史回顾、专门审计、方向变化重建或 current/history conflict 时才按需读取。

Clarification 是 Working Memory item，不是 Layer 1.5。人类解决后，执行 Promotion 到对应长期记忆，并把 item 标记为 `RESOLVED / PROMOTED`。

每个较大工作循环结束和 handoff 前更新 Current Focus / Task Plan；在阶段转换、重要决定或任务批次完成时，以适当粒度更新 Work Log。

## Repository-backed context

- GitHub 是唯一权威项目状态源；
- 会话中的摘要/摘录只是非权威缓存；
- 根据当前 CONTENT / FORM / PROTOCOL route 选择性读取；
- 高影响判断与写入前 fresh-fetch；
- 写入后使相关缓存失效；
- 不维护聊天内第二份动态真值源。

## 外部系统、工具发现与人类交接

当任务需要外部系统、账户或服务时：

- 在已有适当人类授权的前提下，先检查当前可用并获授权的 built-in tools、plugins/connectors、官方 MCP、provider API、官方 integration、repository automation 与 approved adapters；
- installed / enabled / connected 不等于真实 callable；在技术上可行且安全时，先做真实最小 capability probe；
- 优先 official / OAuth / provider-managed / least-secret-handling 路线；
- 不得要求人类把 password、token、private key 或其他 secret 粘贴到聊天；
- 只有身份授权、账户所有者 consent、权限授予、不可委托高影响决定，或当前工具确实无法完成的动作才 handoff；
- handoff 必须最少步骤、一次只要求当前必要动作、假定无技术背景、明确不能发给 AI 的值，并给出可验证完成标准；
- 授权完成后由 Agent fresh-read repository、重新验证 provider actual state，并恢复后续 machine-operable work；
- 影响未来工作的 external operation 必须验证并把 durable result 写回 repository。

Provider UI、聊天状态和模型记忆都不是项目的持久权威状态。

## 持久状态行动的授权作用域

保持 `proposal != authorization != execution != verification != durable write-back`。

durable state 并不自动等于 high-impact。对于授权边界具有实质意义的行动，应按与风险相称的粒度明确 action class、target、allowed side effects、reversibility assumptions、authorization source 与 escalation conditions。

不得根据 capability、repository/provider state、build/deployment 成功、已有 endpoint 或 upstream change 等技术事实推断授权。durable human-approved pre-authorization policy 只在其已记录作用域内有效，并且不能覆盖 human-reserved / non-delegable 边界。

第一次配置可重复使用的 authorization policy 时，由 AI 先提出适合当前场景的授权方式；在适用时区分 per-action authorization、bounded pre-authorization 与 mixed policy，并说明 scope 与 escalation conditions。人类必须先选择、修改或拒绝该方案，最终选择及 authorization provenance 写入 repository durable state 后，AI 才能依赖该 policy 继续配置与执行。

只有当授权确实缺失、行动属于 non-delegable、将超出 scope，或 impact/reversibility 实质变化时才升级给人类；否则继续已经授权的 machine-operable execution，验证 actual state，并把经验证的结果写回 repository durable state。

## 协议来源

初始化项目时记录所采用的协议来源：

- 上游仓库：`ChongLiuPhil/AI-Assisted-Human-Inquiry-and-Creation-Protocol`
- AHICP 版本：`0.3.0-draft`（替换成实际采用的 version/tag/commit）
- Adopted commit/tag：`UNRESOLVED — 初始化时记录`

未来 Agent 不得静默假定上游 AHICP 最新规则已经被本项目采用。协议升级必须成为明确项目决定。

## 任务相关长期状态读取

完成 Working Memory Index -> Current Focus -> Task Plan 后，再根据任务路由按需读取：

1. `core/CONTENT_CORE.zh-CN.md`（CONTENT 任务）；
2. `core/FORM_CORE.zh-CN.md`（FORM 任务）；
3. 最近相关的 `core/DECISION_LOG.zh-CN.md`；
4. `docs/framework-status.zh-CN.md`；
5. 最新 Approved Framework（如有）；
6. `docs/argument-map.zh-CN.md`；
7. 相关成果与 evidence 文件；
8. 需要时读取英文 mirror 核验双语同步。

旧 `docs/clarification-register.zh-CN.md` 仅为兼容指针，不属于 active-state 必读链。

## 仓库状态高于聊天记忆

不要把旧 Agent 的聊天上下文当成规范项目状态。持久的人类决定必须提升到仓库文件。

## 路由人类反馈

把实质性指令分类为：

- `CONTENT`
- `FORM`
- `PROTOCOL`
- 或多标签。

先持久化，再上游优先传播。

## Content 规则

人类内容决定高于 AI 草拟。AI 提议在被接受前必须明显保持 pending。

AI Agent 在项目中作为协作工具。不要把 AI 描述为具有认知性的主体，也不要把“AI 承担认知劳动 / 认知任务”作为规范性术语；应具体说明 AI 执行或辅助的检索、综合、起草、重组、核查等工作。

研究或创作的目的、核心问题与方向必须来源于人类或得到人类明确授权。更精确地说，人类必须保持为责任主体／责任承担者；AI 可以分担工作，但不能成为项目目的、核心判断、framework 授权或公开知识传播的最终责任主体.

## Form 规则

人类形式决定高于渲染默认值。不得从临时工具选择推断长期作者偏好。

在适当情况下，区分 reusable author preference、artifact-type profile、project-specific rule、external constraint 与 temporary default。

## Clarification 规则

如果对核心观点、关键概念、术语/翻译、范围、主要推论关系或章节功能存在高影响不确定性，先写入 `docs/working-memory/task-plan.zh-CN.md` 的 Clarification 区，不得自行选择一种解释后传播。

条目应标明 `BLOCKING / NON-BLOCKING`。人类解决后执行 Promotion：`Task Plan / Clarification -> Decision Log -> appropriate Long-Term Memory`，再按需更新 Argument Map 与成果。

Framework Approval、正式翻译、大规模扩写和 Final Review 前主动执行 Working Memory / Clarification Scan。

## Framework 规则

`docs/argument-map.zh-CN.md` 是 AI 维护的工作结构，不自动等于人类认可。

只有在人类明确 Framework Approval 后才能创建 `docs/frameworks/FW-xxx.zh-CN.md`，并同步创建英文 mirror。不得静默修改已批准快照。

Approved Framework 是主要实质性思想基线，也是人类作为责任主体时核心思想责任的结构性锚点。Framework Approval 前，人类必须清楚理解、认真审核并明确确认拟批准 framework 中实际呈现的全部实质内容，包括核心命题、推论关系、关键区分、范围条件、章节/小节功能及被纳入 framework 的具体措辞。应区分 framework-level defect 与后续 AI 扩写才引入的局部缺陷.

AI 可以帮助构造 framework，但不能成为其中思想责任的最终承担主体.

## Evidence 规则

证据与当前人类承诺冲突时，必须显式呈现。不得隐瞒反面证据，也不得静默改写人类立场。

## 成果状态

AI 扩写正文在相应最终人类批准被记录前保持 `DERIVED-PROVISIONAL`。

如果成果将公开发布，Final Artifact Approval 必须保留可识别的人类责任主体。AI 的生成、扩写、编辑或核查参与不得被理解为把最终公开知识传播责任转移给 AI.

## 双语同步规则

- 中文 canonical 是人类编辑和审阅基准；
- 英文 mirror 必须在同一工作轮次同步；
- 中英文冲突时，以中文为准；
- 双语不同步构成同步缺陷；
- 新的实质性 Markdown 文件创建时即应配对。

## 交接标准

新的、能力合格的 Agent 应能在没有原始聊天 transcript 的情况下，仅根据仓库状态继续项目。
