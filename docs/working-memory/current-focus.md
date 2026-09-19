# AHICP Working Memory — Current Focus

> **Chinese canonical: `current-focus.zh-CN.md`; this file is the synchronized English mirror.**

**Status:** `ACTIVE`  
**Last updated:** 2026-09-20

## CURRENT_STAGE

**The AHICP v0.3 semantic migration is complete; the later external-system authorization / human-handoff and scoped-authorization governance have also completed normative consolidation.**

Migration authority: `AHICP-D026`.  
Later authorization-governance authority: `AHICP-D027`, `AHICP-D028`, and `AHICP-D029`.

Completed:
- formal name and fixed subtitle;
- human-led / AI-assisted / repository-grounded normative direction;
- Protocol Core, Specification, AGENTS, and live protocol migration;
- `AHICP_MANIFEST.yaml` / `AHICP_CONTEXT_INTERFACE.yaml` control plane;
- zero-context onboarding migration;
- research-project specialization template migration;
- methodology article/evidence current protocol identity migration while preserving research-specific subject matter;
- semantic parity of key bilingual normative files;
- final post-migration repair audit;
- provider-neutral machine-operable-first escalation, authorization / human handoff, and provider actual-state write-back;
- scoped authorization lifecycle: `proposal != authorization != execution != verification != durable write-back`;
- initial configuration of reusable authorization policies through AI proposal, human selection, and durable recording of the selected scope / provenance / escalation conditions;
- independent post-merge consistency review and propagation repair after PR #3.

The latest protocol repair closes:
- weakening of the D028 durable authorization record during downstream propagation;
- omission of `permission grants` from Specification §23.3;
- Working Memory not reflecting D028/D029 and the PR #3 milestone;
- Protocol Contract CI checking §23.5.1 only through file-wide markers rather than a section-local invariant.

## CURRENT_OBJECTIVE

### WM-OBJ-003 — Methodology article overall Framework Approval

After protocol maintenance, the repository's principal unresolved work gates remain:

- methodology article Working Framework: `WAITING-HUMAN`
- license: `WAITING-HUMAN`
- target publication venue / form constraints: `WAITING-HUMAN`

Current Chinese Working Framework:

`paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`

## IMMEDIATE_NEXT_ACTION

When the human is ready to continue the methodology article, make an overall Working Framework decision:

- `APPROVE`
- `REVISE`
- `REJECT`

No Approved Framework snapshot is created before that decision.

## PRIMARY_BLOCKER

`WAITING-HUMAN: methodology article overall Framework Approval`

This does not block the completed AHICP protocol migration or authorization-governance maintenance.

## HANDOFF

A replacement AI Agent should use the AHICP control plane and treat the latest repository `main` revision as the sole project-state source. D027–D029 are current authorization-governance authority; legacy HARC live identifiers must not be reintroduced into current normative files.