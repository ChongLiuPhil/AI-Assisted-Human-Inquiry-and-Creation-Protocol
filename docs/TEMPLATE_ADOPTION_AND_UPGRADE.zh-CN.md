# AHICP 模板采用与升级

AHICP 的 `templates/research-project/` 是可安装参考实现；`templates/template-manifest.yaml` 是机器可读的 profile 与升级边界。

## Profiles

- `research-lite`：只引入长期协作所必需的角色。
- `research-standard`：适合持续论文、书稿与研究工作台。
- `research-full`：适合需要正式 framework approval、evidence layer 与更完整审计的高复杂度项目。

Profile 表示治理复杂度，不表示项目价值。

## Legacy functional mapping

已有项目若已有可靠的知识核心、Working Memory、handoff、decision log 或 agent rules，应优先把这些文件映射到 AHICP 角色。不要仅为了文件名一致性复制第二套真值源。

## 升级

升级工具必须区分：

- upstream-managed：可按固定 upstream revision 更新；
- merge-managed：必须比较旧模板、项目当前版本和新模板；
- project-owned：不得由协议升级自动覆盖。

人类批准的内容、framework、决定、Working Memory 与项目实质成果始终属于项目，而不属于模板。
