# AHICP in the Inquiry Publishing Stack

AHICP is the human-led inquiry and creation governance component. It is intentionally independent from publishing infrastructure, metadata interfaces, and any private project control plane.

For a complete project configuration, follow the [Starter ecosystem entrypoint](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/ECOSYSTEM.md) and read the PPF publishing layer:

- [PPF homepage](https://chongliuphil.github.io/Personal-Publishing-Framework/) · [repository](https://github.com/ChongLiuPhil/Personal-Publishing-Framework)
- [Vault Interface repository](https://github.com/ChongLiuPhil/Vault-interface)
- [Starter homepage](https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/) · [repository](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter)

The default new-project baseline is **full AHICP + full PPF**, with Vault Interface used only for the public metadata contract. A project records its actual adoption and pinned revisions instead of copying a second authoritative framework.

Original unpublished work, working memory, credentials, and project-specific copyright assets remain private by default. Continuous Web publication may expose only an approved rendered output and must use an access-control layer when the output is private or transitional.

Cloudflare deployment and reader-access operations must follow the [PPF/Starter operational guide](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.md). An AI agent must explain scope, credentials, data transmission, verification, and rollback before requesting a human Cloudflare action.
