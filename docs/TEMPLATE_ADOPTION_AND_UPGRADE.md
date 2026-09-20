# AHICP Template Adoption and Upgrade

`templates/research-project/` is the installable reference implementation. `templates/template-manifest.yaml` defines machine-readable profiles and upgrade ownership boundaries.

Profiles:

- `research-lite` for a minimal durable collaboration layer;
- `research-standard` for sustained papers, books, and research workbenches;
- `research-full` for high-complexity programs with framework approval and evidence governance.

Existing reliable files should be functionally mapped before creating duplicate sources of truth.

Upgrade tooling must distinguish upstream-managed, merge-managed, and project-owned paths. Human-approved content, decisions, working memory, frameworks, evidence, and substantive artifacts are project-owned and must not be overwritten automatically.
