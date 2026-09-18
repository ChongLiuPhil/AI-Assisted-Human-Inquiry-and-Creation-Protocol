# Form Profile 继承

> **本中文文件是规范性基准；英文 `FORM_PROFILE_INHERITANCE.md` 是同步镜像。**

## 目的

HARC 把研究内容与呈现形式分开。本文件使形式偏好能够跨多个项目与成果类型复用。

人类原创设计目标是：作者可以随时间形成稳定的呈现偏好，同时允许书籍、学术论文、普通文章、报告和具体项目采用不同形式。

## 1. 形式层

一个项目可以从五类来源获得形式约束：

1. **Reusable Author Profile** — 人类明确希望跨项目复用的偏好。
2. **Artifact-Type Profile** — `BOOK`、`ACADEMIC_PAPER`、`ARTICLE` 等特定类型的约定或作者决定。
3. **Project-Specific Form Core** — 仅当前项目适用的决定。
4. **External Constraint** — 期刊、出版商、机构、style guide 或发布渠道规定。
5. **Temporary Default** — 因为尚无人类规则而由 AI/工具临时选取的 provisional 默认值。

这些来源不得混同。

## 2. 推荐冲突解决顺序

发生规则冲突时，先识别来源，不要静默选择。

实用优先顺序：

`mandatory external constraint -> explicit project-specific human decision -> applicable artifact-type profile -> reusable author preference -> temporary default`

如果强制外部约束与人类偏好冲突，应显式记录冲突，而不是改写偏好仿佛作者改变了主意。

## 3. 可复用作者 profile

只有人类明确把偏好推广到一个项目之外时，才使用 reusable profile。

例子：

- 标题密度偏好；
- 经常使用的字体选择；
- 脚注理念；
- 公式呈现；
- 视觉克制程度；
- 双语术语约定。

不得从某一次偶然实现或 AI 生成结果推断跨项目偏好。

模板：

`templates/form-profiles/AUTHOR_PROFILE.zh-CN.md`

## 4. 成果类型 profiles

HARC 为常见成果类型提供独立模板。

初始 profiles：

- `templates/form-profiles/BOOK.zh-CN.md`
- `templates/form-profiles/ACADEMIC_PAPER.zh-CN.md`
- `templates/form-profiles/ARTICLE.zh-CN.md`

这些文件有意保留大量未决项。目的在于提供正确的决策字段，而不是替作者发明偏好。

项目可以增加 `REPORT`、`THESIS`、`PRESENTATION` 等 profile。

## 5. 项目初始化

初始化时，AI Agent 应：

1. 确定成果类型；
2. 读取明确适用的 reusable author profile；
3. 读取相应 artifact-type profile；
4. 创建项目 `core/FORM_CORE.zh-CN.md` 与英文 mirror；
5. 记录项目特有覆盖规则与外部约束；
6. 未指定字段保留为 `UNRESOLVED`；
7. 工具生成的 fallback 标记为 `TEMPORARY-DEFAULT`。

## 6. 持久化规则

人类形式纠正按以下路径传播：

`Human decision -> Decision Log -> FORM_CORE -> reusable/type profile（仅在人类明确一般化时） -> rendering implementation -> artifact`

不能仅仅因为当前项目改变，就更新 reusable profile。必须由人类说明偏好应被一般化。

## 7. 可迁移性

Form-profile 系统与研究主题无关。它可以跨研究项目复用，而不会携带任何实质性研究主张。
