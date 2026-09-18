# Content / Form / Protocol 路由

> **本中文文件是规范性基准；英文 `FORM_CONTENT_ROUTING.md` 是同步镜像。**

HARC 只有在人类反馈被分类并写入适当规范层后，才把它当作持久项目状态。

## CONTENT

当指令改变作品“论证什么或意味着什么”时，使用 `CONTENT`。

例子：

- 修订一个命题；
- 增加概念区分；
- 拒绝一种解释；
- 改变范围；
- 增删论证前提；
- 澄清某章要建立什么结论。

路由：

`Decision Log -> Content Core -> Argument Map -> Approved Framework（如重新批准） -> Artifact`

## FORM

当指令改变成果如何呈现，而本身不改变实质性命题时，使用 `FORM`。

例子：

- 成果类型；
- 字体；
- 页边距/版式系统；
- 标题层级；
- 视觉密度；
- 引用呈现；
- 脚注；
- 图/表样式；
- 语言呈现约定；
- 可复用作者风格偏好。

路由：

`Decision Log -> Form Core -> Rendering/Typesetting -> Artifact`

## PROTOCOL

当指令改变人类与 AI 如何协作时，使用 `PROTOCOL`。

例子：

- 必读顺序；
- 批准门；
- 持久化规则；
- Agent 交接；
- branch/commit 约定；
- 归档策略；
- 同步检查；
- 双语 canonical/mirror 规则。

路由：

`Decision Log -> Protocol/Governance Files -> Agent Behavior`

## 多标签情况

一条指令可能影响多个领域。

例如：

> “把论文改造成书，并围绕三个部分重新组织论证。”

这同时是：

- `FORM`：成果类型改变；
- `CONTENT`：思想架构改变。

不要为了形式上的单标签而掩盖真实变化。

## 临时实现默认值

在用户尚未指定偏好前，AI Agent 往往必须选一些默认值。

例如：

- LaTeX 默认字体；
- provisional citation style；
- 占位章节编号；
- 临时页面尺寸。

这些必须标为 `TEMPORARY-DEFAULT`，不能当成人类偏好。

只有在人类明确接受后，临时默认值才能进入规范状态。

## 跨项目形式偏好

某些形式决定可能被人类明确指定为跨项目可复用。

如果人类说明一项偏好具有一般性，把它分类为：

`REUSABLE-AUTHOR-PREFERENCE`

项目可以继承这些偏好，同时允许项目特有或外部发布约束覆盖它们。

## 实用路由测试

问：

1. 这是否改变**主张的内容**？→ `CONTENT`
2. 这是否改变**表达/渲染方式**？→ `FORM`
3. 这是否改变**协作如何运作**？→ `PROTOCOL`

应用所有真实适用的标签。
