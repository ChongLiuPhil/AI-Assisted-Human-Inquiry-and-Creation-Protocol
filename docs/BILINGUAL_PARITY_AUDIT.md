# Bilingual Parity Audit

**Date:** 2026-09-18  
**Audit target:** migration of HARC to Chinese-canonical / English-synchronized-mirror governance  
**Normative rule:** `protocol/BILINGUAL_SYNC.zh-CN.md`  
**Status:** `INITIAL MIGRATION PASS`

> Chinese `BILINGUAL_PARITY_AUDIT.zh-CN.md` is canonical; this English file is the synchronized mirror.

## 1. Purpose

On 2026-09-18, the human founder explicitly required that:

- all substantive HARC content be maintained in Chinese and English;
- Chinese be the canonical editing, human-review, and semantic authority baseline;
- English be the synchronized translation mirror;
- every substantive edit update both languages in the same work cycle;
- Chinese govern conflicts until the English version is repaired.

This audit checks whether the pre-existing repository has been migrated from a mixed monolingual/bilingual state into complete bilingual governance and whether known high-risk semantic drift has been repaired.

## 2. Repository-wide pairing scan

The current `main` tree was recursively scanned for Markdown files.

Results:

- total Markdown files: **120**
- Chinese canonical files (`*.zh-CN.md`): **60**
- English mirrors: **60**
  - most retain existing `*.md` paths;
  - the complete methodology article uses `METHODOLOGY_ARTICLE.en.md`;
- Chinese files without English mirrors: **0**
- English files without Chinese canonical counterparts: **0**

**Structural pairing result: `PASS`.**

## 3. Major migration work completed

### 3.1 Protocol and governance

Bilingual pairs now exist for:

- AGENTS;
- Protocol Core;
- Decision Log;
- Specification;
- Bilingual Sync Policy;
- Persistent Memory;
- Framework Approval;
- Content/Form/Protocol Routing;
- Form Profile Inheritance.

### 3.2 Methodology article

Bilingual pairs now exist for the article's:

- Content Core;
- Form Core;
- Framework Status;
- Argument Map;
- Framework Review Memo;
- evidence notes;
- complete Chinese article and complete English mirror.

Translation did not change approval state: the article remains `WORKING-FRAMEWORK / DERIVED-PROVISIONAL`.

### 3.3 White paper

The earlier Chinese and English white papers had evolved independently:

- Chinese: an earlier 10-section conceptual version;
- English: a later expanded 14-section version.

That violated the new canonical/mirror rule.

**Initial handling had the wrong direction:** the English version was first reset to the older Chinese version. The human then clarified the cutover principle: substantive developments that had already occurred in English before the rule existed must first be absorbed into Chinese rather than discarded by an older Chinese text.

**Final repair:** the pre-rule 14-section English white paper was recovered from Git history. Its substantive English-only developments—including Presentation Drift, Agent Handoff Failure, an Evidence Layer, Derived Artifact, a dedicated Semantic Version Control section, Self-hosting / Protocol Evolution, and fuller limitations/future-development material—were incorporated into the Chinese canonical version. English was then restored as the synchronized mirror of that updated Chinese version.

The white paper therefore completed the correct sequence:

`pre-cutover English development -> Chinese catch-up -> parity -> Chinese canonical cutover`.

### 3.3.1 Audit of bilingual files that already existed before cutover

The main documents that already had both language versions before the rule change were checked historically:

- **README:** the complete English version was created at 2026-09-18 01:28:50Z and the complete Chinese version followed at 01:28:52Z with corresponding section structure; no white-paper-like independent content divergence was found;
- **WHITEPAPER:** a real English-ahead divergence was confirmed and repaired through the catch-up procedure above;
- **Methodology Article:** before the rule, the complete manuscript existed only in Chinese, so there was no English-ahead risk;
- other Chinese canonical governance files created during this migration were translated from the then-current English governance files, so they already absorbed the pre-cutover English state.

**Legacy reconciliation result: `PASS`.**

### 3.4 Audits, evidence, and project governance

Bilingualized:

- Architecture;
- Founding-Idea Audit;
- Three-Cycle Repair Audit;
- Final Post-Repair Audit;
- Methodology Evidence;
- CONTRIBUTING;
- ROADMAP;
- LICENSE-DECISION;
- README.

### 3.5 Reusable templates

Bilingualized:

- AUTHOR_PROFILE;
- BOOK;
- ACADEMIC_PAPER;
- ARTICLE;
- research-project AGENTS / README;
- Content Core / Form Core / Decision Log;
- Argument Map / Framework Status.

New-project templates now initialize Chinese canonical + English mirror instead of requiring later translation.

### 3.6 Critical Clarification mechanism (historical stage; superseded by Working Memory)

A later human-originated governance requirement added three new bilingual file pairs:

- `protocol/CLARIFICATION_REGISTER.zh-CN.md` / English mirror;
- `docs/clarification-register.zh-CN.md` / English mirror;
- `templates/research-project/docs/clarification-register.zh-CN.md` / English mirror.

A fresh repository-tree scan still reports **0** missing language counterparts.

### 3.7 Zero-context Bootstrap

Two bilingual startup pairs were added:

- root `START_HERE.zh-CN.md` / `START_HERE.md`;
- template `templates/research-project/START_HERE.zh-CN.md` / English mirror.

Language-neutral machine-readable manifests were also added:

- `HARC_MANIFEST.yaml`
- `templates/research-project/HARC_MANIFEST.yaml`

The YAML manifests are path/read-order/invariant indexes and need not be duplicated solely for language; their human-readable rules are expressed in bilingual START_HERE / AGENTS / Specification files.

### 3.8 Onboarding Handshake and standalone startup assets

After P20 / HARC-D018 received explicit human confirmation, the following were added and bilingualized:

- `BOOTSTRAP_PROMPT.zh-CN.md` / English mirror;
- `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` / English mirror;
- `protocol/ONBOARDING_HANDSHAKE.zh-CN.md` / English mirror;
- `templates/research-project/BOOTSTRAP_PROMPT.zh-CN.md` / English mirror;
- `templates/research-project/ONBOARDING_REPORT_TEMPLATE.zh-CN.md` / English mirror;
- `docs/ONBOARDING_SELF_TEST.zh-CN.md` / English mirror.

The current recursive tree scan reports **96 Markdown files = 48 Chinese canonical + 48 English mirrors, with 0 missing counterparts**.

### 3.9 Session Context Bootstrap

Added and bilingualized:

- `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` / English mirror;
- `templates/research-project/SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` / English mirror.

The mechanism was later narrowed by HARC-D020 into a minimal Repository Resolver: the session keeps only the control kernel for accessing GitHub and no longer duplicates dynamic project state.

### 3.10 Repository-Backed Context Interface

Added and bilingualized:

- `protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md` / English mirror.

Added language-neutral machine interfaces:

- `HARC_CONTEXT_INTERFACE.yaml`;
- `templates/research-project/HARC_CONTEXT_INTERFACE.yaml`.

HARC-D020 formalizes:

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

Session Context Bootstrap is now a Repository Resolver; dynamic Blocking Clarifications, Framework, Artifact, and Core state must be retrieved on demand from latest canonical GitHub revisions.

The latest recursive scan reports **102 Markdown files = 51 Chinese canonical + 51 English mirrors, with 0 missing counterparts**.

### 3.11 Working Memory

HARC-D021 retires the independent “Layer 1.5” model and adds three bilingual Working Memory pairs:

- `protocol/WORKING_MEMORY.zh-CN.md` / English mirror;
- `docs/working-memory.zh-CN.md` / English mirror;
- `templates/research-project/docs/working-memory.zh-CN.md` / English mirror.

Legacy `docs/clarification-register*` paths remain as compatibility pointers but no longer carry active state.

The new memory model is:

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

in parallel with:

`Working Memory = stage / goals / tasks / blockers / pending decisions / clarifications / TODO / handoff`

Clarification is now a Working Memory item; human-resolved stable content is promoted into the appropriate Long-Term Memory destination.

The latest recursive scan reports **108 Markdown files = 54 Chinese canonical + 54 English mirrors, with 0 missing counterparts**.

### 3.12 Modular Working Memory

HARC-D022 further develops Working Memory from a logical area typically carried by one file into an explicitly modular functional area.

The current HARC reference implementation and project template add three bilingual pairs:

- `working-memory/current-focus.zh-CN.md` / English mirror;
- `working-memory/task-plan.zh-CN.md` / English mirror;
- `working-memory/work-log.zh-CN.md` / English mirror.

The root `working-memory.zh-CN.md` is now the Index / Resolver.

Default AI onboarding reads:

`Index -> Current Focus -> Task Plan`

Work Log primarily serves human retrospective review and is outside default AI context.

The latest recursive scan reports **120 Markdown files = 60 Chinese canonical + 60 English mirrors, with 0 missing counterparts**.

### 3.13 Semantic-mirror repairs from the current review

The 2026-09-18 full-discussion coverage review found that complete file pairing did not guarantee that every English mirror had absorbed the latest modular Working Memory changes.

This pass repaired:

- root `START_HERE.md`;
- root `AGENTS.md`;
- `protocol/ONBOARDING_HANDSHAKE.md`;
- project-template `START_HERE.md`;
- project-template `AGENTS.md`;
- a few older Bootstrap / Persistent Memory formulations.

The main repairs remove the legacy Clarification Register as active state, enforce `Index -> Current Focus -> Task Plan` for normal takeover, keep Work Log outside default AI context, and synchronize methodology-article reading order with the modular Working Memory model.

## 4. High-risk semantic mismatches repaired

The migration specifically repaired:

1. the English Methodology Form Core still saying English might be developed later;
2. English project templates still initializing HARC v0.1 / monolingual files;
3. the Chinese methodology article still linking upstream to old English paths;
4. the English methodology article pointing to a nonexistent `METHODOLOGY_SOURCES.en.md`;
5. Chinese and English white papers having structurally diverged;
6. Roadmap / Contributing not yet containing bilingual-governance requirements;
7. a stale version-scope line in the English Protocol Core;
8. agent onboarding not consistently prioritizing Chinese canonical files;
9. the full-discussion coverage review found semantic lag in root `START_HERE.md`, root `AGENTS.md`, the English Onboarding Handshake, and project-template `AGENTS.md` regarding modular Working Memory and Task Plan Clarification rules; these were resynchronized from Chinese canonical.

## 5. Limits of the audit

This audit establishes:

- complete file pairing;
- repair of known high-risk structural/status differences;
- discoverable Chinese canonical precedence;
- bilingual inheritance in new-project templates.

But:

> **File pairing is not a mathematical proof of permanent semantic equivalence.**

Translation can still introduce subtle semantic drift. Therefore a parity check remains a completion requirement for every future substantive edit. Automated semantic-parity tooling belongs on the future Roadmap.

## 6. Completion condition for future changes

A substantive edit is complete only when:

1. the Chinese canonical file is updated;
2. the English mirror is updated;
3. claims, scope, approval states, unresolved issues, and reference relationships are materially consistent;
4. affected upstream/downstream state files are synchronized;
5. any conflict is repaired using Chinese as the governing source.

## 7. Conclusion

The initial repository-wide bilingual migration is complete.

**Audit status: `PASS — INITIAL BILINGUAL MIGRATION COMPLETE`**

HARC-D015 may now move from “implementation in progress” to “implemented.” This means only that the initial historical migration is complete; it does not waive bilingual synchronization for future edits.

Every future agent work cycle must continue to follow:

> **Maintain Chinese canonical first, then maintain the English synchronized mirror in the same work cycle.**
