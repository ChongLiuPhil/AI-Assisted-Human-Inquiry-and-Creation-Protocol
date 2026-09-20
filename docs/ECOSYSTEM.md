# AHICP in the Inquiry Publishing Stack

AHICP is the human-led inquiry and creation governance component. It is intentionally independent from publishing infrastructure, metadata interfaces, and any private project control plane.

## Two first entrypoints

The ecosystem deliberately has two different first entrypoints:

- **Human conceptual entry — AHICP:** the [Human Guide](HUMAN_GUIDE.md) and AHICP public homepage explain why the system exists, how it helps ordinary users, the habits it supports, and how the four components relate.
- **Machine/configuration entry — Starter:** the Starter ecosystem and Agent Retrieval Contract govern project composition, reconstruction, adoption, upgrade, deployment, and cross-component agent behavior.

This separation keeps the human explanation simple without weakening the machine contract. AHICP remains the human-method center; Starter remains the composition/configuration center.

### Delivery-provider independence

The current Human Entry is delivered through GitHub Pages. That URL is a delivery location, not the conceptual identity of the Human Entry. The canonical content remains the repository-tracked bilingual Human Guide. The public site may later move to Cloudflare or another provider without changing the human-entry role or the machine handoff contract.

The current stable Machine Entry landing is:
https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/agent/

For a complete project configuration, follow the [Starter ecosystem entrypoint](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/ECOSYSTEM.md) and read the PPF publishing layer:

- [PPF homepage](https://chongliuphil.github.io/Personal-Publishing-Framework/) · [repository](https://github.com/ChongLiuPhil/Personal-Publishing-Framework)
- [Vault Interface homepage](https://chongliuphil.github.io/Vault-interface/) · [repository](https://github.com/ChongLiuPhil/Vault-interface)
- [Starter homepage](https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/) · [repository](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter)

The default new-project baseline is **full AHICP + full PPF + Vault Interface**, with Vault Interface used only for the public metadata contract. Reduced profiles require explicit human selection. A project records its actual adoption and pinned revisions instead of copying a second authoritative framework.

Original unpublished work, working memory, credentials, and project-specific copyright assets remain private by default. Continuous Web may still be prepared, but unpublished or transitional output is restricted by default. Access-policy references may be stored in Git; actual reader credentials or secrets may not.

Cloudflare deployment and reader-access operations must follow the [PPF/Starter operational guide](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.md). An AI agent must explain scope, credentials, data transmission, verification, and rollback before requesting a human Cloudflare action.

For cross-component work, also read the [canonical agent retrieval contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.md). Public links support ecosystem reconstruction; they do not authorize private-state access.
