# HARC Protocol Specification

**Human–AI Research Collaboration Protocol**

**Version:** 0.2.0-draft  
**Scope:** GitHub-centered research and long-form intellectual collaboration between a human author and one or more AI agents.

---

## 1. Purpose

HARC defines a persistent, auditable collaboration architecture for projects in which human intellectual direction and AI-assisted research, structuring, drafting, revision, verification, and formatting develop over time.

The protocol is designed to preserve:

- human intellectual agency;
- semantic continuity;
- explicit provenance of important decisions;
- distinction between human intention and AI proposal;
- distinction between content and form;
- inspectable argument structure;
- evidence-based corrigibility;
- scalable project memory;
- cross-agent continuity;
- explicit approval states;
- meaningful human cognitive and epistemic responsibility.

HARC v0.2 assumes GitHub as the persistent repository substrate. Future implementations may map the same logical roles to other systems.

---

## 2. Normative terms

- **MUST** — required for HARC compliance.
- **SHOULD** — strongly recommended unless a project records a reason to deviate.
- **MAY** — optional.

---

## 3. Core maxim

A long-running research project MUST NOT treat a transient AI conversation as its sole durable state.

> **Chat is an interaction surface; the repository is durable shared research memory.**

Important project state MUST be externalized into explicit, version-controlled repository artifacts.

---

## 4. Roles

### 4.1 Human Author

The Human Author supplies, revises, or confirms substantive intellectual commitments and presentation intentions.

The Human Author MAY delegate extensive search, synthesis, structuring, drafting, editing, formalization, checking, and formatting to AI agents.

Delegation of cognitive labor MUST NOT be treated as automatic delegation of epistemic responsibility.

### 4.2 AI Agent

The AI Agent MAY:

- extract and normalize human decisions;
- maintain repository state;
- propose arguments, objections, distinctions, examples, terminology, and structure;
- conduct research and evidence checks when tools permit;
- maintain operational argument representations;
- expand approved structures into prose or other artifacts;
- detect inconsistencies, evidence conflicts, and synchronization defects;
- maintain formatting and rendering systems.

The AI Agent MUST distinguish its proposals from human-approved commitments.

### 4.3 Repository

The Repository is the durable shared state among the Human Author and AI Agents.

It MUST preserve enough current and historical state that a new competent AI agent can reconstruct the project without access to the original chat history.

---

## 5. Canonical state model

### 5.1 Content Core — `core/CONTENT_CORE.md`

The Content Core contains the Human Author's active substantive commitments.

It SHOULD record:

- project purpose;
- central questions;
- active theses;
- tentative theses;
- central distinctions;
- scope limitations;
- explicitly unresolved authorial questions.

It MUST NOT silently contain unaccepted AI proposals.

### 5.2 Form Core — `core/FORM_CORE.md`

The Form Core contains active human decisions about the artifact as an expressed object.

It MAY include:

- artifact type;
- language and prose register;
- typography;
- page layout;
- heading hierarchy;
- footnotes;
- citation presentation;
- tables and figures;
- visual system;
- reusable author preferences;
- external venue constraints.

Unknown form decisions MUST remain explicit unknowns rather than being inferred from AI defaults.

### 5.3 Decision Log — `core/DECISION_LOG.md`

The Decision Log is the historical audit trail of important human decisions.

Each entry SHOULD include identifier, date, source, classification, decision, affected files/layers, superseded decision if any, and implementation status.

Current cores may be rewritten to represent active state; the Decision Log preserves historical continuity.

### 5.4 Critical Clarification Register — `docs/clarification-register.md`

The Critical Clarification Register is Layer 1.5 bridge state for **high-impact uncertainty not yet resolved by the human**.

It MUST capture uncertainties that, if guessed by the AI, could materially alter core claims, key concepts, scope, major inferential relations, section functions, important terminology/translation, Framework Approval, or long-term project continuity.

Important entries SHOULD include identifier, status, `BLOCKING / NON-BLOCKING` severity, category, uncertain point, candidate interpretations, impact, affected files/claims/sections, any explicitly `AI-PROPOSED` recommendation, the question for the human, human resolution, and propagation targets.

Open clarifications MUST NOT be treated as human commitments.

After human resolution, the Agent MUST perform Resolution Promotion:

`Human resolution -> Decision Log -> appropriate Core -> Working Argument Map -> Derived Artifact`

Resolved entries may remain as audit traces, but the normative answer must be promoted into the appropriate Core.

See `protocol/CLARIFICATION_REGISTER.md`.

### 5.5 Working Argument Map — `docs/argument-map.md`

The Working Argument Map is the primary operational discussion interface for long-form intellectual structure.

It is normally AI-maintained and MUST be treated as mutable until human approval.

It SHOULD expose:

- research question;
- current thesis set;
- conceptual vocabulary;
- premises/supporting claims;
- argument dependencies;
- section/chapter architecture;
- crucial non-entailments;
- objections;
- evidence dependencies;
- unresolved human decisions;
- AI proposals awaiting human response;
- synchronization status.

It SHOULD remain substantially shorter than the full artifact.

### 5.6 Approved Framework Snapshots — `docs/frameworks/FW-xxx.md`

An Approved Framework Snapshot is created only after explicit human review and confirmation.

A snapshot MUST NOT be silently modified after approval.

Material intellectual change MUST create a new framework version.

### 5.7 Framework Status — `docs/framework-status.md`

This file SHOULD state:

- current Working Framework status;
- latest approved framework identifier;
- current artifact status;
- unresolved synchronization defects;
- final artifact approval status.

### 5.8 Evidence Layer — `evidence/`

Evidence files MAY include literature notes, source checks, datasets, calculations, formal derivations, empirical notebooks, and source inventories.

Evidence constrains what can responsibly be claimed but MUST NOT silently rewrite human intention.

### 5.9 Derived Artifact

The paper, book, article, report, presentation, or other output is a derived expression.

It MUST remain compatible with:

- the active Content Core;
- the latest applicable Approved Framework;
- the Form Core;
- known evidence constraints.

---

## 6. Feedback routing

Before persisting substantive human feedback, the AI Agent MUST classify it as one or more of:

### `CONTENT`

Changes what the work argues, means, assumes, distinguishes, questions, or concludes.

Propagation path:

`Human decision -> Decision Log -> Content Core -> Working Argument Map -> Derived Artifact`

### `FORM`

Changes how the artifact is expressed or rendered: artifact type, typography, layout, visual system, citation presentation, prose presentation, etc.

Propagation path:

`Human decision -> Decision Log -> Form Core -> Rendering/Implementation -> Artifact`

### `PROTOCOL`

Changes how collaboration, persistence, handoff, synchronization, approval, or versioning operates.

Propagation path:

`Human decision -> Decision Log -> Protocol/Governance -> Agent Behavior`

Multi-label feedback MUST be supported.

---

## 7. Upstream-first update rule

A lower layer MUST NOT be treated as evidence that the human endorsed a higher-level change.

### 7.1 Content update cycle

1. identify the human decision;
2. record it in the Decision Log;
3. reconcile the Content Core;
4. reconcile the Working Argument Map;
5. determine whether an existing Approved Framework remains valid;
6. inspect evidence/logical conflicts;
7. propagate into the derived artifact;
8. verify synchronization.

### 7.2 Form update cycle

1. identify the human form decision;
2. record it;
3. reconcile the Form Core;
4. update reusable style profile only if explicitly cross-project;
5. propagate into implementation;
6. verify rendering.

### 7.3 Protocol update cycle

1. record the workflow decision;
2. update protocol/governance documents;
3. update reusable templates where applicable;
4. verify that new rules are discoverable by future agents;
5. do not alter research content merely because governance changed.

---

## 8. Proposal and provenance status

Where ambiguity would matter, projects SHOULD distinguish:

### Content statuses

- `AUTHOR-ACTIVE`
- `AUTHOR-TENTATIVE`
- `AI-PROPOSED`
- `EVIDENCE-CONSTRAINT`
- `UNRESOLVED`

### Form statuses

- `AUTHOR-PREFERENCE`
- `REUSABLE-AUTHOR-PREFERENCE`
- `PROJECT-SPECIFIC`
- `EXTERNAL-CONSTRAINT`
- `TEMPORARY-DEFAULT`
- `UNRESOLVED`

AI choices MUST NOT be silently promoted into human-author statuses.

---

## 9. Framework Approval Gate

The Human Author SHOULD review a compact framework before a large-scale artifact is treated as having a stable intellectual baseline.

The framework SHOULD state:

- central problem;
- thesis set;
- major concepts;
- main inferential relations;
- section/chapter roles;
- important limitations;
- intentionally unresolved issues;
- known evidence conflicts material to the argument.

Upon explicit approval, the Agent MUST:

1. create an immutable versioned snapshot;
2. record approval in the Decision Log;
3. update Framework Status;
4. treat the snapshot as the approved intellectual baseline.

---

## 10. Framework fidelity and responsibility

After framework approval, AI Agents MAY expand the work substantially.

The derived artifact MUST NOT materially depart from the approved framework without returning upstream for new human review.

Material deviation includes changing the central thesis, adding a new major conclusion, removing an essential premise, changing relations among major claims, altering scope in a way that changes the argument, or restructuring the work so the approved reasoning is no longer accurately represented.

HARC distinguishes:

- **framework-level defect** — a defect already present in the human-approved intellectual architecture;
- **derived-expansion defect** — a local problem introduced only during later AI expansion or implementation.

The distinction improves traceability but does not remove final-release accountability requirements.

---

## 11. Overview projection

The approved framework SHOULD be recoverable from the artifact's reader-facing overview.

Default mappings:

- `ACADEMIC_PAPER`: abstract + introduction;
- `ARTICLE`: opening/introductory overview;
- `BOOK`: introduction/overview chapter + chapter roadmap;
- `REPORT`: executive summary + structure/method overview;
- other types: analogous high-level overview specified in Form Core.

The overview need not reproduce the framework verbatim, but MUST represent it faithfully.

---

## 12. Final Artifact Approval Gate

Framework approval and final artifact approval are distinct.

The artifact MAY remain `DERIVED-PROVISIONAL` while AI Agents continue expansion, editing, research integration, and formatting.

Before formal submission, publication, or public release under human authorship, the Human Author SHOULD perform the final review required by the relevant discipline, venue, institution, or authorship standard.

Recommended artifact states:

- `DERIVED-PROVISIONAL`;
- `FINAL-REVIEW`;
- `FINAL-APPROVED`.

---

## 13. Evidence-conflict protocol

If reliable evidence or formal reasoning conflicts with active human content:

1. preserve the current human intention until the human revises it;
2. flag the conflict explicitly;
3. distinguish evidence, inference, uncertainty, and interpretation;
4. do not conceal the conflict;
5. do not knowingly propagate a misleading claim downstream;
6. request or await human resolution where necessary;
7. record the resulting decision.

---

## 14. Cognitive delegation and epistemic responsibility

HARC distinguishes **delegation of cognitive labor** from **delegation of epistemic responsibility**.

AI MAY perform extensive search, synthesis, structuring, drafting, formalization, consistency checking, revision, and formatting.

Human attention SHOULD be concentrated on high-leverage decisions, including:

- research aims and questions;
- core commitments;
- major inferential architecture;
- acceptance/rejection of material AI proposals;
- treatment of decisive evidence conflicts;
- Framework Approval;
- Final Artifact Approval where required.

HARC does not claim that file structure alone guarantees good judgment. Approval mechanisms are governance scaffolds, not substitutes for human competence and understanding.

---

## 15. Persistent memory and context limits

HARC provides persistent project memory, not literal infinite model context.

Projects SHOULD scale through:

- concise active cores;
- concise operational maps;
- chronological logs;
- indexed evidence;
- archived historical detail;
- selective retrieval.

The objective is **recoverability and traceability**, not simultaneous loading of all history.

---

## 16. Agent handoff

A new AI Agent SHOULD be able to continue normal project work by reading, at minimum:

1. project `AGENTS.md`;
2. Content Core;
3. Form Core;
4. recent Decision Log entries;
5. Working Argument Map;
6. Framework Status and latest Approved Framework;
7. relevant current artifact and evidence.

A project SHOULD record the HARC version/tag/commit it adopted so later upstream protocol changes are not silently treated as already accepted governance.

If essential constraints exist only in an unavailable chat or hidden memory, the project is non-compliant until they are externalized.

---

## 17. Form-profile inheritance

Reusable presentation state SHOULD be able to distinguish:

1. reusable author-level preferences;
2. artifact-type profiles such as `BOOK`, `ACADEMIC_PAPER`, and `ARTICLE`;
3. project-specific Form Core decisions;
4. external venue constraints;
5. temporary AI/tool defaults.

Inheritance MUST NOT transform an unstated preference into an author preference.

---

## 18. Synchronization invariant

At a stable checkpoint, all of the following SHOULD be true:

1. major artifact claims are compatible with Content Core;
2. current intellectual architecture is represented by the Working Argument Map;
3. where an Approved Framework exists, derived content remains faithful to it or is marked out of sync;
4. important presentation choices are compatible with Form Core or explicitly marked temporary/external;
5. important human decisions appear in the Decision Log;
6. unaccepted AI proposals remain visibly unaccepted;
7. known evidence conflicts are visible;
8. important decisions are not stranded only in chat history;
9. onboarding documents point to current canonical files.

Failure of any condition creates an explicit synchronization defect.

---

## 19. Multi-pass audit and repair discipline

A requested multi-pass audit MUST be interpreted as repeated review-and-repair cycles.

Each cycle SHOULD execute:

`review -> identify defect -> repair/implement -> verify repair`.

If three passes are requested, perform three such cycles. If a post-repair audit is requested, perform a further independent audit after all three cycles rather than counting one of the three cycles as the final audit.

Audit records SHOULD state what defect was found, what repository change repaired it, and how the repair was verified.

---

## 20. Methodology article as a governed HARC artifact

The HARC project itself SHOULD maintain two mutually supporting outputs:

1. an executable open protocol;
2. a methodology article explaining and critically developing the protocol.

The methodology article SHOULD address the conceptual implications of AI-assisted research, including human cognitive/epistemic responsibility, delegable and non-delegable intellectual work, persistent research state, semantic version control, framework-level authorship, and publication accountability.

The article MUST itself follow HARC discipline:

- maintain a Working Framework;
- separate AI proposals from human-approved claims;
- maintain evidence/source notes for time-sensitive policy claims;
- remain `DERIVED-PROVISIONAL` until human approval gates are completed.

---

## 21. Recommended commit semantics

Suggested prefixes:

- `intent:` human content/form decisions;
- `structure:` argument architecture;
- `draft:` derived artifact;
- `form:` presentation/rendering;
- `evidence:` sources/data/formal verification;
- `protocol:` workflow/governance;
- `audit:` review/repair records;
- `release:` approved protocol or artifact release.

---

## 22. Minimal HARC profile

A lightweight compliant project SHOULD contain at least:

```text
AGENTS.md
core/CONTENT_CORE.md
core/FORM_CORE.md
core/DECISION_LOG.md
docs/argument-map.md
docs/framework-status.md
```

For long or high-stakes projects, evidence directories, Approved Framework snapshots, detailed protocol files, and audit records are strongly recommended.

---

## 23. Portability

HARC v0.2 targets GitHub but separates logical functions from exact filenames.

Future implementations MAY map the same canonical roles to other versioned collaboration systems while preserving explicit state, human/AI provenance distinctions, approval gates, inspectable history, and cross-agent handoff.

---

## 24. Design thesis

HARC separates things that AI-assisted research often collapses:

1. human intellectual intention;
2. human presentation intention;
3. AI operational representation;
4. evidence constraints;
5. approval state;
6. derived expression;
7. historical decisions.

The protocol treats this separation as the basis for durable, auditable, human-governed AI-assisted research.

## 25. Bilingual canonical synchronization

HARC project documentation SHOULD be maintained bilingually in Chinese and English.

For HARC's own repository, and for projects that adopt the bilingual profile:

1. Chinese is the canonical semantic source and primary human editing/review baseline.
2. English is a synchronized translation mirror.
3. A substantive edit MUST update both language versions within the same work cycle.
4. A language pair MUST NOT be treated as synchronized when they differ materially in claims, requirements, approval state, scope, or unresolved issues.
5. If the two versions conflict, the Chinese version governs until the English mirror is corrected.
6. New substantive Markdown documents SHOULD be created as bilingual pairs at creation time.
7. Language-neutral technical artifacts such as code, BibTeX, schemas, and raw data MAY remain single-copy, provided their human-facing instructions are bilingual.
8. Agent handoff documentation MUST make the canonical-language rule discoverable.
9. For legacy bilingual files predating the rule, if English contains newer substantive development not yet present in Chinese, an English -> Chinese catch-up MUST be completed so Chinese represents the genuinely latest semantic state at cutover.
10. After canonical cutover, normal substantive development MUST follow `Human decision -> Chinese canonical -> English mirror`; English MUST NOT independently develop new substantive content.

Recommended naming convention:

- Chinese canonical: `NAME.zh-CN.md`
- English mirror: `NAME.md` where backward compatibility or GitHub default rendering matters; otherwise `NAME.en.md`.

A stable synchronization checkpoint SHOULD include a bilingual parity check.
