# AHICP 研究项目模板

> **本中文文件是规范性基准；英文 `README.md` 是同步 mirror。**

使用本目录作为新的 AHICP 治理项目的概念性初始化模板。

## 协议来源

初始化时，记录项目采用的 AHICP version/tag/commit。上游 AHICP 仓库以后发生变化，不应自动改变本项目治理。

默认上游：

`ChongLiuPhil/AI-Assisted-Human-Inquiry-and-Creation-Protocol`

协议来源字段见 `AGENTS.zh-CN.md`。

## 默认语言治理

本模板默认采用：

- **中文 canonical** — 内容、形式、framework 与人类批准的规范编辑/审阅基准；
- **英文 synchronized mirror** — 必须在同一工作轮次与中文同步。

如果人类明确选择其他语言治理方式，应在 Decision Log 中记录并更新项目协议。

## 初始化顺序

1. 创建/确认 `START_HERE.zh-CN.md`、英文 mirror、`AHICP_MANIFEST.yaml` 与 `AHICP_CONTEXT_INTERFACE.yaml`，记录采用的 AHICP version/commit、mandatory read order 与 repository-backed context policy。
2. 确定成果类型：paper、book、article、report、thesis 等。
3. 仅把人类实际表达的实质性承诺提取到 `core/CONTENT_CORE.zh-CN.md`，并同步英文 mirror。
4. 确定明确适用的 reusable author form profile 与 artifact-type profile。
5. 仅把人类明确的呈现决定提取到 `core/FORM_CORE.zh-CN.md`；保持 inherited、external、project-specific 与 temporary-default 可区分，并同步英文 mirror。
6. 把初始化决定记录到 `core/DECISION_LOG.zh-CN.md` 与英文 mirror。
7. 创建 Working Memory Area：Index、Current Focus、Task Plan、Work Log 及其英文 mirror。默认模板使用拆分文件；轻量项目可以在 manifest 中把多个角色映射到同一文件。
8. Current Focus 保存当前最重要的目标；Task Plan 保存动态任务、TODO、blockers、pending decisions / Clarifications；Work Log 主要供人类日后回顾，默认不属于 AI onboarding 必读内容。
9. 保留 `docs/clarification-register.zh-CN.md` 作为兼容指针；新的 clarification 作为 Task Plan / Working Memory item 管理。
10. 建立 `docs/argument-map.zh-CN.md` 作为 AI 维护的工作表示，并同步英文 mirror。AI 可以帮助提出、组织和表达 framework，但不要把 AI 描述为认知主体或说它“承担认知劳动 / 认知任务”；AI 可以分担工作，但人类必须保持为责任主体。
11. 初始化 `docs/framework-status.zh-CN.md` 为 `WORKING-FRAMEWORK`；除非人类明确批准，否则没有 Approved Snapshot。Framework Approval 要求人类清楚理解、认真审核并确认拟批准 framework 中实际呈现的全部实质内容；如果成果进入公开传播，Final Artifact Approval 还必须确保有可识别的人类责任主体。
12. 创建适合项目的成果目录。
13. 研究核验、数据、计算或来源相关时创建 `evidence/`，其中人类可读说明双语化。
14. 未知项保持明确未知，不要用 AI 假设填充。

## 最小模板树

```text
project/
├── START_HERE.zh-CN.md
├── START_HERE.md
├── BOOTSTRAP_PROMPT.zh-CN.md
├── BOOTSTRAP_PROMPT.md
├── SESSION_CONTEXT_BOOTSTRAP.zh-CN.md
├── SESSION_CONTEXT_BOOTSTRAP.md
├── ONBOARDING_REPORT_TEMPLATE.zh-CN.md
├── ONBOARDING_REPORT_TEMPLATE.md
├── AHICP_MANIFEST.yaml
├── AHICP_CONTEXT_INTERFACE.yaml
├── AGENTS.zh-CN.md
├── AGENTS.md
├── core/
│   ├── CONTENT_CORE.zh-CN.md
│   ├── CONTENT_CORE.md
│   ├── FORM_CORE.zh-CN.md
│   ├── FORM_CORE.md
│   ├── DECISION_LOG.zh-CN.md
│   └── DECISION_LOG.md
├── docs/
│   ├── working-memory.zh-CN.md
│   ├── working-memory.md
│   ├── working-memory/
│   │   ├── current-focus.zh-CN.md
│   │   ├── current-focus.md
│   │   ├── task-plan.zh-CN.md
│   │   ├── task-plan.md
│   │   ├── work-log.zh-CN.md
│   │   └── work-log.md
│   ├── clarification-register.zh-CN.md
│   ├── clarification-register.md
│   ├── argument-map.zh-CN.md
│   ├── argument-map.md
│   ├── framework-status.zh-CN.md
│   ├── framework-status.md
│   └── frameworks/
├── evidence/
└── paper/ | book/ | article/ | report/
```

## Form-profile 继承

上游 AHICP 仓库提供：

- `templates/form-profiles/AUTHOR_PROFILE.zh-CN.md`
- `templates/form-profiles/BOOK.zh-CN.md`
- `templates/form-profiles/ACADEMIC_PAPER.zh-CN.md`
- `templates/form-profiles/ARTICLE.zh-CN.md`

仅使用适用于新项目的 profile。不要通过猜测作者喜好来填充未决字段。

## 给 AI Agent 的建议指令

> 使用 AHICP Protocol 初始化本项目。把 GitHub 直接当作权威外部记忆库与工作状态库；模型上下文只保留 Repository Resolver 和当前任务所需的临时缓存。区分 CONTENT、FORM 和 PROTOCOL 决定。规范文件只写入人类实际提供的承诺。确定成果类型与适用形式 profile，但不要发明偏好。用 Working Memory Area 维护协作状态：Current Focus 只保留现在最重要的目标和 immediate next action；Task Plan 维护动态任务、TODO、blockers、pending human decisions 与 clarifications；完成任务退出 active list，并把阶段性摘要写入 Work Log；Work Log 主要供我日后回顾，不要默认加载到 AI 上下文。对任何可能重大影响核心命题、关键概念、术语/翻译或论证结构的高影响不确定性，创建 Working Memory Clarification item 并向我确认；不要自行猜测。把 AI Agent 作为协作工具描述：可以执行或辅助检索、综合、起草、重组、核查等工作，但不要把 AI 描述为认知主体，也不要使用“AI 承担认知劳动 / 认知任务”作为规范术语。研究或创作的目的、核心问题与方向必须由人类发起或明确批准；人类必须保持为责任主体，AI 可以分担工作但不能成为研究目的、framework 授权或公开知识传播的最终责任主体。Argument Map 在我明确批准 framework snapshot 前始终属于 AI 生成的工作结构；Framework Approval 前，我必须清楚理解、认真审核并明确确认其中实际呈现的全部实质内容。实质性变化上游优先传播。记录项目采用的 AHICP version/commit。中文是 canonical；任何修改必须同步英文 mirror。

## 未知项是合法状态

新项目无需一开始解决所有问题。

写：

`UNRESOLVED — 尚未指定作者偏好`

而不是发明偏好。
