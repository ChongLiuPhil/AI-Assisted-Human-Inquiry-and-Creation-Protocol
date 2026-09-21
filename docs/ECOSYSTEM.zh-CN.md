# AHICP 在 Inquiry Publishing Stack 中的位置

AHICP 负责探究与创作中的方法、判断和协作规则。它独立于出版基础设施、元数据接口和具体项目的私有控制层。

## 两个入口，各有不同用途

整个体系设置两个入口，分别服务于“理解”和“配置”：

- **面向读者的介绍入口 — AHICP：** [使用指南](HUMAN_GUIDE.zh-CN.md) 与 AHICP 公共主页负责解释为什么需要这套体系、它怎样帮助长期思考与创作，以及四个组件怎样协作。
- **机器/配置入口 — Starter：** Starter ecosystem 与 Agent Retrieval Contract 负责项目组合、状态恢复、采用、升级、部署和跨组件 Agent 行为。

这样，读者可以先从问题和使用方式理解体系，而不必先接触技术配置；同时机器契约仍保持完整。AHICP 继续负责思考、判断和协作方法，Starter 负责组合与配置。

### 承载网站的平台可以替换

当前面向读者的网站仍由 GitHub Pages 提供；Cloudflare Pages 已确定为首选迁移目标，GitHub 继续作为权威源文件、版本历史和 CI 平台。在 Cloudflare 部署、目标域名、机器交接和跨项目链接全部验证完成以前，现有 URL 仍然是正式入口。

这个网址只是当前承载位置，不等于入口本身。迁移应遵循 [Cloudflare 公共站点迁移说明](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CLOUDFLARE_PUBLIC_DELIVERY_MIGRATION.zh-CN.md)；不能因为 Cloudflare staging project 已经创建，就提前修改 Human Entry URL。

当前稳定的机器入口：
https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/agent/

要完成一个项目的完整配置，请先阅读 [Starter 体系入口](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/ECOSYSTEM.zh-CN.md)，再阅读 PPF 发布层：

- [PPF 主页](https://chongliuphil.github.io/Personal-Publishing-Framework/) · [仓库](https://github.com/ChongLiuPhil/Personal-Publishing-Framework)
- [Vault Interface 主页](https://chongliuphil.github.io/Vault-interface/) · [仓库](https://github.com/ChongLiuPhil/Vault-interface)
- [Starter 主页](https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/) · [仓库](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter)

新项目的默认基线是 **完整 AHICP + 完整 PPF + Vault Interface**，Vault Interface 只负责公共元数据契约。精简配置（profile）必须由使用者明确选择。项目应记录实际采用状态和固定版本，而不是复制出第二个权威规范。

原创未发布作品、工作记忆、凭据和项目特定版权资产默认保持 private。Continuous Web 仍可同时准备，但未发布或过渡阶段输出默认 restricted。Git 只保存 access-policy reference，不保存真实阅读凭据或其他秘密。

Cloudflare 部署与读者访问操作应遵循 [PPF/Starter 操作指南](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.zh-CN.md)。AI Agent 在要求使用者执行 Cloudflare 操作前，必须说明操作范围、凭据边界、数据传输、验证方法和回滚方式。

跨组件工作还必须阅读 [权威 Agent 调取契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.zh-CN.md)。公共链接只用于恢复生态关系，不授权私人状态访问。
