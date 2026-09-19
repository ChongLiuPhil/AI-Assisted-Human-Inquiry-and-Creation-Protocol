# AHICP v0.3 Phase C Semantic Audit

**Status:** IN PROGRESS  
**Date:** 2026-09-19  
**Basis:** AHICP-D026 and the AHICP Semantic Migration Plan

## Purpose

This audit classifies how legacy HARC content should be treated in AHICP v0.3. Generalizing the protocol does not mean mechanically removing every occurrence of research-specific language.

## Four treatment classes

### 1. GENERALIZE

Use this when a rule is general protocol infrastructure that was written as research-specific only because HARC originally used research as its default setting.

Already identified:
- overall Protocol Core scope;
- README / Specification top-level definition;
- Agent contract and onboarding control chain;
- persistent project state / project memory;
- general Content / Form / Protocol routing;
- general Working Memory, handoff, and approval mechanisms.

### 2. RETAIN RESEARCH-SPECIFIC

Research/scholarly wording remains appropriate for:
- the methodology article itself;
- evidence and source verification;
- research integrity, academic authorship, and venue policy;
- research-paper and scholarly-book artifact profiles;
- `templates/research-project/` as a research specialization.

Migration must not flatten these into generic language merely for naming consistency.

### 3. PRESERVE HISTORICAL

Historical facts and audit identifiers remain unchanged:
- `HARC-D001`–`HARC-D025`;
- historical uses of the former project name in decisions or audits;
- completed audit snapshots.

New decisions use the AHICP prefix beginning with `AHICP-D026`.

### 4. MIGRATE LEGACY IDENTIFIER

Current control-plane, startup, template, and live-navigation identifiers must migrate:
- `HARC_MANIFEST.yaml` → `AHICP_MANIFEST.yaml`;
- `HARC_CONTEXT_INTERFACE.yaml` → `AHICP_CONTEXT_INTERFACE.yaml`;
- current README / Specification / AGENTS / START_HERE;
- template control files;
- old repository URL.

Legacy control files may remain temporarily as compatibility pointers but must not remain normative truth sources.

## Current finding

The stable core of AHICP is not “research collaboration” but:

> **human-led inquiry and creation with AI assistance**

Humans retain purpose, direction, substantive judgment, approval, and responsibility. AI may perform or assist substantial work without becoming a symmetric cognitive subject or ultimate bearer of responsibility. Repository-backed state keeps AI Agents replaceable, while mature structures such as Content / Form / Protocol routing, Working Memory, Framework Approval, and Final Artifact Approval remain.

## Boundary with PPF

AHICP does not define publishing infrastructure.

The **Personal Publishing Framework (PPF)** governs:
`SOURCE -> BUILD -> PUBLISH -> RELEASE -> ARCHIVE`

Projects may adopt AHICP only, PPF only, or AHICP + PPF.

## Remaining work

- migrate live Architecture / Roadmap / template navigation;
- repository-wide legacy-path scan;
- bilingual parity audit;
- zero-context onboarding test;
- post-migration repair audit;
- precise handling of the methodology article, whose subject remains research-specific even though the protocol name and scope have broadened.

## Merge condition

Phase C does not aim for “zero occurrences of HARC.”

Merge readiness requires:
1. all live control paths use AHICP;
2. historical HARC identifiers remain intelligible;
3. research-specific content has not been incorrectly generalized;
4. bilingual parity;
5. zero-context onboarding succeeds;
6. post-migration audit has no blocking defect.
