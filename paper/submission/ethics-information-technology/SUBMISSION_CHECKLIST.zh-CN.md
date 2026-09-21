# Ethics and Information Technology — 投稿检查清单

**状态：** `ACTIVE — FINAL ARTIFACT APPROVAL PENDING`  
**官方指南核验：** 2026-09-21  
**官方页面：** https://link.springer.com/journal/10676/submission-guidelines

## 稿件形式

- [x] 当前按 Original Research Paper / conceptual-methodological original research 准备。
- [x] blinded manuscript 与项目 canonical article 分离。
- [x] 按仓库 validator 粗略计算，正文内容约 5,000–8,000 words。
- [x] 摘要 150–250 words。
- [x] 关键词 4–6 个。
- [x] displayed heading 不超过三级。
- [x] 采用 author–year 引用。
- [x] 投稿派生 reference list 已移除未在正文引用、仅服务内部 evidence infrastructure 的条目。
- [x] 已建立可重复的 Word/docx CI 构建流程。
- [x] traceable / masked 两份 Word/docx build candidates 均已生成、完成结构校验并上传 workflow artifacts。
- [x] table-caption 更新后已重新渲染并逐页检查 traceable / masked 两份 Word/docx build candidates（20 页 + 20 页）；Table 1 / Table 2 caption 均与对应表格同页，未发现 clipping / overlap 或异常分页。
- [x] DOCX 自动页码、普通字体、footer、表格跨页与匿名 core metadata 已检查；CI 同时验证 PAGE field、non-split table rows 与禁止身份 metadata。

## Double-anonymous review

- [x] blinded manuscript 不含作者姓名。
- [x] 不含 affiliation / contact details。
- [x] 不含 AHICP 内部 Decision IDs、Framework IDs、development status、Working Memory IDs。
- [x] 不含直接 GitHub URL。
- [x] 已准备 masked reviewer derivative，并移除 `AHICP`、协议全称、direct GitHub URL 与内部 IDs。
- [ ] 人类/编辑部确认采用 masked reviewer route；残余 search-based deanonymization risk 已明确接受或进一步处理。
- [ ] 提供给 reviewer 的 repository / supplementary materials 使用适当匿名或 masked 路线。
- [x] self-citation 表述已检查；reviewer manuscript 未发现以 “our previous work”等自指措辞暴露作者身份的写法。

## AI / LLM disclosure

- [x] 正文真实披露 substantive generative-AI use。
- [x] 明确区分 generative drafting/restructuring 与 copy editing。
- [x] AI 不列为 author。
- [x] 明确最终 claim、source、citation、manuscript 责任由人类承担。
- [ ] 如果最终期刊/编辑流程要求，按真实项目记录补全具体 model/tool 名称、可获得的版本与实质使用日期。

## Research data 与声明

- [x] 已加入 Data Availability Statement。
- [x] 如实说明当前不报告 original empirical dataset / completed empirical experiment。
- [ ] 人类在当前 submission interface 完成 Competing Interests。
- [ ] 人类完成 Funding statement。
- [ ] 如要求，人类完成 Author Contribution。
- [ ] Acknowledgements 在 blinded manuscript 之外完成。
- [ ] 如适用，完成 ORCID / corresponding-author metadata。

## 学术终审

- [x] latest-head EIT CI 已确认 traceable / masked 两稿的 18 组 citation ↔ reference-list 映射全部通过。
- [x] reference list 的 publication/acceptance status 与核心元数据已核验；见 `CITATION_AUDIT.md`。
- [x] 主要 DOI / proceedings / standards identifiers 已核验；动态 policy URL 仍需正式投稿前复核。
- [x] 完成 artifact-level 英文与论证流程审阅；masked 机械替换语法已修复。
- [x] claim boundaries 已与 `MA-FW-001` 核验；未改批准 Framework。
- [x] 未引入实证性效果主张；evaluation 仍明确为 proposed / future work。
- [x] venue adaptation 未改变核心 Framework thesis、主要推论、scope 或 contribution boundary。
- [ ] 记录 Final Artifact Approval。
- [ ] 另行记录 submission authorization。

## Submission integrity

- [ ] 人类确认稿件没有同时投给其他期刊。
- [ ] 人类确认所有作者/合作者需要的 submission approval。
- [ ] 正式提交前再次检查 live submission interface；实际字段可能与静态指南不同。
