# 方法论文章 — Form Core

**角色：** AHICP 方法论文章中，经人类确认的呈现决定的当前规范真值源。

> 本中文文件是规范性基准；英文 `METHODOLOGY_ARTICLE_FORM_CORE.md` 是同步镜像。

## 成果类型

`ACADEMIC_PAPER / METHODOLOGY ARTICLE`

## 题目

**中文 canonical 题目：**  
《从对话到持久研究状态：AI时代的人机研究协作、人类责任与可审计作者性》

**状态：** `HUMAN-APPROVED TITLE — HARC-D024`

英文题目作为中文 canonical 的同步翻译镜像维护：

*From Conversation to Persistent Research State: Human–AI Research Collaboration, Human Responsibility, and Auditable Authorship in the AI Era*

英文翻译措辞随中文题目同步维护。`MA-FW-001` 已依据 AHICP-D031 获得整体 Framework Approval；题目继续作为该已批准 Framework 的当前派生标题。

## 语言

**规范编辑语言：中文。**

AHICP 项目现已明确要求中英双语维护：

- 中文版本是规范性编辑与人类审阅基准；
- 英文版本是同步翻译镜像；
- 对中文的任何实质性编辑必须在同一工作轮次中同步到英文；
- 中英文冲突时，以中文为准，并修复英文。

因此，方法论文章最终至少应在项目内部持续维护中英双语版本，即使将来某个具体投稿渠道只接受一种语言。

## 文体 / register

人类已确认的详细文体偏好：`UNRESOLVED`。

当前草稿采用学术—解释性 register，属于 AI 工作默认值。除非人类明确确认，不要把它升级成永久作者偏好。

## 结构

文章应解释：

- AHICP 的问题背景；
- 协议架构；
- AI 辅助研究中的人类认知/认识责任与能力边界；
- 批准与问责机制；
- 局限与经验测试议程。

详细章节顺序由已批准的 `MA-FW-001` 与当前对齐的 Argument Map 管理；venue-specific submission derivative 不得实质改变该结构，除非重新进入 Framework review。

## 字体与版式

- 字体：`UNRESOLVED`
- 正文字号：`UNRESOLVED`
- 行距：`UNRESOLVED`
- 页面尺寸/页边距：`UNRESOLVED`
- 标题风格：`UNRESOLVED`

当前 Markdown 渲染属于 `TEMPORARY-DEFAULT`。

## 引用 / 参考文献呈现

引用样式：`EXTERNAL-CONSTRAINT — ETHICS AND INFORMATION TECHNOLOGY / AHICP-D033`。

投稿派生稿采用 author–year citation，并在最终 submission package 中按期刊当前要求核验 reference list：仅保留正文实际引用的 published / accepted works，按第一作者姓氏字母排序，DOI 可用时使用完整 DOI link。项目内部 `paper/methodology-references.bib` 继续作为工作基础设施。

## 目标发布渠道约束

`SELECTED — ETHICS AND INFORMATION TECHNOLOGY / AHICP-D032`。

当前 disciplinary positioning：以 **information-technology governance / human responsibility / governed project-memory architecture** 为主要外部定位，同时保持 methodology / architecture paper 属性。

## 外部约束

依据 AHICP-D033，采用 `Ethics and Information Technology` 当前官方 submission constraints 作为本次投稿派生约束：

- double-anonymous peer review；
- manuscript content 约 5,000–8,000 words，title / abstract / references 不计入 content word count；
- abstract 150–250 words；
- 4–6 keywords；
- blinded manuscript 与 blinded associated files 移除作者姓名、affiliation、contact information 与其他直接识别信息；
- acknowledgments、funding、author information 等放在 submission-system fields / title-page metadata，不进入 blinded manuscript；
- substantive LLM use 必须在 Methods 或适当替代位置透明披露；本项目的 generative drafting / restructuring 等使用不得误写为单纯 copy editing；
- original research 需要 Data Availability Statement；本稿当前不报告 empirical dataset / completed experiment，应据实说明；
- submission manuscript 以 Word/docx 为主要格式；仓库 Markdown submission derivative 是生成最终 docx 的上游；
- displayed headings 不超过三级；
- 直接 repository URL、内部 Decision IDs、Framework status / development metadata 不进入 blinded manuscript；
- `AHICP` 名称本身可能造成 search-based deanonymization，作为 submission blocker/risk 持续跟踪，正式提交前决定 masked-material / editorial clarification 路线。

## 状态

成果类型、中英双语治理、primary target venue 与当前 venue-specific 外部约束已经确定。`Final Artifact Approval`、license、最终 author/title-page metadata、anonymization-risk 处置和真实 submission authorization 仍未完成。
