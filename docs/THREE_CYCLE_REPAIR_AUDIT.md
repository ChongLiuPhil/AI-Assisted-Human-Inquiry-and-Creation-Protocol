# Three-Cycle Review-and-Repair Audit

**Date:** 2026-09-17  
**Scope:** integration of the founder's stated HARC ideas plus the requirement that HARC itself produce a methodology article.  
**Interpretation:** each cycle is `review -> identify defects -> repair/implement -> verify repair`.

This document supersedes any interpretation of the earlier “three-pass audit” as three passive readings followed by one repair stage.

---

## Cycle 1 — Semantic/source-of-truth repair

### Review question

Are all human-originated design commitments explicitly represented in canonical founder-level state, or are some important ideas present only in explanatory prose?

### Defects found

1. The audit procedure itself was underspecified: “three-pass review” had previously been treated too much like repeated inspection rather than three complete repair loops.
2. The newly explicit dual-output requirement was not yet founder-level state: HARC must be both an executable open project and a methodology article project.
3. Human cognitive responsibility and the distinction between delegation of cognitive labor and delegation of epistemic responsibility needed to become an explicit project commitment, not only an implication of framework approval.

### Repairs implemented

- Added `P15` to `core/PROTOCOL_CORE.md`: multi-pass audits are review-and-repair cycles, followed by an independent post-repair audit when requested.
- Added `P16`: HARC has two mutually supporting outputs—an executable open protocol and a methodology article.
- Added `P17`: cognitive labor may be delegated extensively while high-leverage epistemic responsibility remains human-governed.
- Added `HARC-D013` and `HARC-D014` to `core/DECISION_LOG.md`.

### Verification

Founder-level canonical state now explicitly contains these commitments. They no longer depend on the current chat or on AI inference from the white paper.

**Cycle 1 status:** `REPAIRED AND VERIFIED`.

---

## Cycle 2 — Operational/artifact repair

### Review question

Are the founder-level commitments executable through concrete files and states, especially the requirement to produce a genuine methodology article?

### Defects found

1. HARC contained conceptual white papers, but the methodology article was not yet a distinct governed scholarly artifact.
2. There was no article-specific Working Framework separating human-confirmed ideas from AI-proposed terminology and structure.
3. The article needed an explicit status preventing an AI-generated first draft from being misrepresented as a human-approved scholarly position.

### Repairs implemented

Created:

- `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.md`
  - status: `WORKING-FRAMEWORK`;
  - records the current thesis set, argument structure, evidence anchors, human decisions needed, and AI-proposed terminology.
- `paper/METHODOLOGY_ARTICLE.zh-CN.md`
  - first complete Chinese methodology-article draft;
  - status: `DERIVED-PROVISIONAL`;
  - develops HARC as a methodology of persistent research state, semantic version control, cognitive delegation, epistemic responsibility, framework approval, and auditable authorship.

The draft also introduces and distinguishes:

- delegation of cognitive labor vs delegation of epistemic responsibility;
- framework defect vs derived-expansion defect;
- Framework Approval vs Final Artifact Approval;
- persistent external state vs single-run context;
- contribution transparency vs authorship/accountability.

### Evidence added to the article

The draft is anchored to relevant literature/policies including:

- Clark & Chalmers on the extended mind;
- Hutchins on distributed cognition;
- Hardwig on epistemic dependence;
- Parasuraman & Riley on automation reliance;
- ICMJE authorship/accountability requirements;
- Nature/Springer Nature AI and authorship policies;
- CRediT contributor-role taxonomy;
- UNESCO guidance on human-centred generative-AI governance.

### Verification

The methodology article now exists as an independent scholarly artifact and is itself governed by the protocol it describes. The working framework is not falsely labelled as human-approved, and the prose is not falsely labelled final.

**Cycle 2 status:** `REPAIRED AND VERIFIED`.

---

## Cycle 3 — Discoverability/handoff repair

### Review question

If the original conversation disappears and a new AI agent receives only the repository, will it discover the audit discipline, methodology article, article status, and relevant protocol extensions without relying on search luck?

### Defects found

1. Root `AGENTS.md` did not explicitly require the new review-and-repair interpretation of multi-pass audits.
2. Root `AGENTS.md` did not explicitly identify the methodology article as a governed HARC artifact.
3. Root `README.md` did not prominently present the protocol and methodology article as two co-equal project outputs.
4. The new article files and audit files needed to be reachable from normal human/agent onboarding paths.

### Repairs implemented

Updated `AGENTS.md` to:

- define multi-pass audits as repair loops;
- identify the methodology article and its Working Framework;
- preserve `DERIVED-PROVISIONAL` status until human approval;
- add form-profile inheritance to the agent reading order.

Updated `README.md` to:

- present HARC as a dual-output project;
- link the methodology article and its argument map;
- explain cognitive delegation vs epistemic responsibility;
- expose the audit discipline;
- link the repair-audit and final-audit documents;
- provide explicit human and AI onboarding paths.

### Verification

A new agent starting at `README.md` or `AGENTS.md` can now discover:

- the executable protocol;
- founder-level source of truth;
- the methodology article;
- the article's approval status;
- the review-and-repair audit requirement;
- reusable templates and form-profile inheritance.

**Cycle 3 status:** `REPAIRED AND VERIFIED`.

---

# State after three repair cycles

The three requested cycles are complete.

Each cycle included:

1. review;
2. defect identification;
3. repository repair/implementation;
4. verification of the repair.

The next required step is an independent **post-repair audit**, performed after these fixes rather than folded into any of the three cycles.
