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

- total Markdown files: **72**
- Chinese canonical files (`*.zh-CN.md`): **36**
- English mirrors: **36**
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

**Repair:** the Chinese historical white paper remains canonical and the English white paper was reset to a faithful mirror. Substantive English-only ideas that had become part of HARC were not lost because they already exist in Protocol Core, Specification, or the Methodology Article.

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

## 4. High-risk semantic mismatches repaired

The migration specifically repaired:

1. the English Methodology Form Core still saying English might be developed later;
2. English project templates still initializing HARC v0.1 / monolingual files;
3. the Chinese methodology article still linking upstream to old English paths;
4. the English methodology article pointing to a nonexistent `METHODOLOGY_SOURCES.en.md`;
5. Chinese and English white papers having structurally diverged;
6. Roadmap / Contributing not yet containing bilingual-governance requirements;
7. a stale version-scope line in the English Protocol Core;
8. agent onboarding not consistently prioritizing Chinese canonical files.

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
