# HARC 研究项目模板

> **本中文文件是规范性基准；英文 `README.md` 是同步 mirror。**

使用本目录作为新的 HARC 治理项目的概念性初始化模板。

## 协议来源

初始化时，记录项目采用的 HARC version/tag/commit。上游 HARC 仓库以后发生变化，不应自动改变本项目治理。

默认上游：

`ChongLiuPhil/Human-AI-Research-Collaboration-Protocol`

协议来源字段见 `AGENTS.zh-CN.md`。

## 默认语言治理

本模板默认采用：

- **中文 canonical** — 内容、形式、framework 与人类批准的规范编辑/审阅基准；
- **英文 synchronized mirror** — 必须在同一工作轮次与中文同步。

如果人类明确选择其他语言治理方式，应在 Decision Log 中记录并更新项目协议。

## 初始化顺序

1. 创建/确认 `START_HERE.zh-CN.md`、英文 mirror 与 `HARC_MANIFEST.yaml`，记录采用的 HARC version/commit 和 mandatory read order。
2. 确定成果类型：paper、book、article、report、thesis 等。
3. 仅把人类实际表达的实质性承诺提取到 `core/CONTENT_CORE.zh-CN.md`，并同步英文 mirror。
4. 确定明确适用的 reusable author form profile 与 artifact-type profile。
5. 仅把人类明确的呈现决定提取到 `core/FORM_CORE.zh-CN.md`；保持 inherited、external、project-specific 与 temporary-default 可区分，并同步英文 mirror。
6. 把初始化决定记录到 `core/DECISION_LOG.zh-CN.md` 与英文 mirror。
7. 创建 `docs/clarification-register.zh-CN.md` 与英文 mirror，作为高影响不确定性的 Layer 1.5 操作界面。
8. 建立 `docs/argument-map.zh-CN.md` 作为 AI 维护的工作表示，并同步英文 mirror。
9. 初始化 `docs/framework-status.zh-CN.md` 为 `WORKING-FRAMEWORK`；除非人类明确批准，否则没有 Approved Snapshot。
10. 创建适合项目的成果目录。
11. 研究核验、数据、计算或来源相关时创建 `evidence/`，其中人类可读说明双语化。
12. 未知项保持明确未知，不要用 AI 假设填充。

## 最小模板树

```text
project/
├── START_HERE.zh-CN.md
├── START_HERE.md
├── HARC_MANIFEST.yaml
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

上游 HARC 仓库提供：

- `templates/form-profiles/AUTHOR_PROFILE.zh-CN.md`
- `templates/form-profiles/BOOK.zh-CN.md`
- `templates/form-profiles/ACADEMIC_PAPER.zh-CN.md`
- `templates/form-profiles/ARTICLE.zh-CN.md`

仅使用适用于新项目的 profile。不要通过猜测作者喜好来填充未决字段。

## 给 AI Agent 的建议指令

> 使用 HARC Protocol 初始化本项目。把 GitHub 当作持久项目记忆。区分 CONTENT、FORM 和 PROTOCOL 决定。规范文件只写入人类实际提供的承诺。确定成果类型与适用形式 profile，但不要发明偏好。对任何可能重大影响核心命题、关键概念、术语/翻译或论证结构的高影响不确定性，先写入 Clarification Register 并向我确认；不要自行猜测。Argument Map 在我明确批准 framework snapshot 前始终属于 AI 生成的工作结构。实质性变化上游优先传播。记录项目采用的 HARC version/commit。中文是 canonical；任何修改必须同步英文 mirror。

## 未知项是合法状态

新项目无需一开始解决所有问题。

写：

`UNRESOLVED — 尚未指定作者偏好`

而不是发明偏好。
