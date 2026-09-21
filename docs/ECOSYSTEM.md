# AHICP in the Inquiry Publishing Stack

AHICP defines how a long-running inquiry or creative project keeps questions, evidence, decisions, project memory, and AI collaboration clear. It remains independent from publishing infrastructure, public metadata interfaces, and private deployment state.

## Understanding the stack vs configuring a project

The stack separates understanding the method from configuring a project:

- **Understand the stack through AHICP:** the [complete guide](HUMAN_GUIDE.md) and public homepage explain what the system is for, how project memory works, and how the four components relate.
- **Configure through Starter:** the Starter ecosystem and Agent Retrieval Contract govern project composition, reconstruction, adoption, upgrades, deployment, and cross-component agent behavior.

This separation keeps the explanation readable while preserving a precise machine contract. AHICP owns the inquiry and collaboration method; Starter owns composition and configuration mechanics.

### The public website can move without changing the role

The current public introduction is still delivered through GitHub Pages. Cloudflare Pages is now the preferred delivery target, while GitHub remains the canonical source/version-control provider. The current URL remains authoritative until the Cloudflare deployment, target domain, machine handoff, and cross-project links have been verified.

The URL is a delivery location, not the identity of the method. Follow the [coordinated Cloudflare public-delivery migration](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CLOUDFLARE_PUBLIC_DELIVERY_MIGRATION.md); do not replace the Human Entry URL merely because a Cloudflare staging project exists.

The current stable machine entry is:
https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/agent/

For a complete project configuration, follow the [Starter ecosystem entrypoint](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/ECOSYSTEM.md) and read the PPF publishing layer:

- [PPF homepage](https://chongliuphil.github.io/Personal-Publishing-Framework/) · [repository](https://github.com/ChongLiuPhil/Personal-Publishing-Framework)
- [Vault Interface homepage](https://chongliuphil.github.io/Vault-interface/) · [repository](https://github.com/ChongLiuPhil/Vault-interface)
- [Starter homepage](https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/) · [repository](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter)

The default new-project baseline is **full AHICP + full PPF + Vault Interface**, with Vault Interface used only for the public metadata contract. Reduced profiles require explicit human selection. A project records its actual adoption and pinned revisions instead of copying a second authoritative framework.

Original unpublished work, working memory, credentials, and project-specific copyright assets remain private by default. Continuous Web may still be prepared, but unpublished or transitional output is restricted by default. Access-policy references may be stored in Git; actual reader credentials or secrets may not.

Cloudflare deployment and reader-access operations must follow the [PPF/Starter operational guide](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.md). An AI agent must explain scope, credentials, data transmission, verification, and rollback before requesting a human Cloudflare action.

For cross-component work, also read the [canonical agent retrieval contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.md). Public links support ecosystem reconstruction; they do not authorize private-state access.
