# AHICP in the Inquiry Publishing Stack

AHICP defines how a long-running inquiry or creative project keeps questions, evidence, decisions, project memory, and AI collaboration clear. It remains independent from publishing infrastructure, public metadata interfaces, and private deployment state.

## Understanding the stack vs configuring a project

The stack separates understanding the method from configuring a project:

- **Understand the stack through AHICP:** the [complete guide](HUMAN_GUIDE.md) and public homepage explain what the system is for, how project memory works, and how the four components relate.
- **Configure through Starter:** the Starter ecosystem, Agent Retrieval Contract, and Project Provisioning Contract govern project composition, reconstruction, adoption, low-touch provisioning, upgrades, deployment, and cross-component agent behavior.

This separation keeps the explanation readable while preserving a precise machine contract. AHICP owns the inquiry and collaboration method; Starter owns composition and provisioning orchestration, while PPF remains authoritative for executable publishing/provider infrastructure.

### The public website can move without changing the role

The public human introduction now uses the verified Cloudflare Worker at https://inquirystack.philohub.workers.dev/. GitHub remains the canonical source/version-control provider; the former GitHub Pages sites have been retired.

The URL is a delivery location, not the identity of the method. The approved cutover and rollback are recorded in the [coordinated Cloudflare public-delivery migration](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CLOUDFLARE_PUBLIC_DELIVERY_MIGRATION.md).

The current stable machine entry is:
https://inquirystack.philohub.workers.dev/agent/

For a complete project configuration, follow the [Starter ecosystem entrypoint](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/ECOSYSTEM.md) and read the PPF publishing layer:

- [PPF homepage](https://inquirystack.philohub.workers.dev/ppf/) · [repository](https://github.com/ChongLiuPhil/Personal-Publishing-Framework)
- [Vault Interface homepage](https://inquirystack.philohub.workers.dev/vault-interface/) · [repository](https://github.com/ChongLiuPhil/Vault-interface)
- [Starter homepage](https://inquirystack.philohub.workers.dev/starter/) · [repository](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter)

The default new-project baseline is **full AHICP + full PPF + Vault Interface**, with Vault Interface used only for the public metadata contract. Reduced profiles require explicit human selection. After verified platform bootstrap, the preferred infrastructure profile is `agent-provisioned-external-ci`: private GitHub source, an account-wide Access-protected Worker, a trusted Secret Broker, and GitHub Actions deployment with a project-scoped Worker credential. Verified standing authorization may cover ordinary private/restricted project creation inside the approved scopes; public release, reader expansion, domains/DNS, provider-scope expansion, and paid-plan changes remain human-reserved. A project records its actual adoption and pinned revisions instead of copying a second authoritative framework.

Original unpublished work, working memory, credentials, and project-specific copyright assets remain private by default. Continuous Web may still be prepared, but unpublished or transitional output is restricted by default. Access-policy references may be stored in Git; actual reader credentials or secrets may not.

Cloudflare deployment and reader-access operations must follow the [Starter Project Provisioning Contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/PROJECT_PROVISIONING_CONTRACT.md) and the [PPF/Starter operational guide](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.md). Where verified standing authorization already covers ordinary restricted setup, the Agent should continue machine-operable work without repeatedly returning it to the human. Deployment-token plaintext must remain inside the trusted Secret Broker, never chat/model context.

For cross-component work, also read the [canonical agent retrieval contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.md). Public links support ecosystem reconstruction; they do not authorize private-state access.
