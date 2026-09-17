# HARC Protocol Specification

**Human–AI Research Collaboration Protocol**

**Version:** 0.1.0-draft  
**Scope:** GitHub-centered research and long-form intellectual collaboration between a human author and one or more AI agents.

---

## 1. Purpose

HARC defines a persistent, auditable collaboration architecture for projects in which human intellectual direction and AI-assisted research, structuring, drafting, revision, and formatting develop over time.

The protocol is designed to preserve:

- human intellectual agency;
- semantic continuity;
- explicit provenance of important decisions;
- distinction between author intention and AI proposal;
- distinction between content and form;
- inspectable argument structure;
- cross-agent continuity;
- evidence-based corrigibility;
- scalable project memory;
- clear approval states.

The protocol does **not** require one specific AI platform. Version 0.1 assumes GitHub as the persistent repository substrate.

---

## 2. Normative terms

Within this specification:

- **MUST** means required for HARC compliance.
- **SHOULD** means strongly recommended unless the project records a reason to deviate.
- **MAY** means optional.

---

## 3. Core principle

A long-running research project MUST NOT treat a transient AI conversation as its sole durable state.

Important project state MUST be externalized into explicit, version-controlled repository artifacts.

The central operational maxim is:

> **Chat is an interaction surface; the repository is durable shared research memory.**

---

## 4. Roles

### 4.1 Human Author

The Human Author supplies or confirms the project's substantive intellectual commitments and final public accountability decisions.

The Human Author MAY delegate extensive research assistance, structuring, drafting, editing, formalization, and formatting to AI agents.

### 4.2 AI Agent

The AI Agent may:

- extract and normalize human decisions;
- maintain project state;
- propose arguments, objections, distinctions, examples, terminology, and structure;
- conduct research and evidence checks when tools permit;
- maintain the operational argument representation;
- expand approved structures into prose or other artifacts;
- detect inconsistencies, evidence conflicts, and synchronization defects.

The AI Agent MUST distinguish its proposals from human-approved commitments.

### 4.3 Repository

The Repository is the durable shared state between Human Author and AI Agents.

It MUST preserve enough current and historical state that a new competent AI agent can reconstruct the project without access to the original chat history.

---

## 5. Canonical state model

A HARC research project SHOULD implement the following canonical state.

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

It SHOULD remain compact enough for routine onboarding.

### 5.2 Form Core — `core/FORM_CORE.md`

The Form Core contains active human decisions about the artifact as an expressed object.

It MAY include:

- artifact type;
- language;
- prose/register preferences;
- typography;
- page layout;
- heading hierarchy;
- footnotes;
- citation presentation;
- tables/figures;
- visual system;
- reusable author style preferences;
- external venue constraints.

Unknown form decisions MUST remain explicit unknowns rather than being inferred from AI defaults.

### 5.3 Decision Log — `core/DECISION_LOG.md`

The Decision Log is the historical audit trail of important human decisions.

Each entry SHOULD include:

- identifier;
- date;
- source;
- classification (`CONTENT`, `FORM`, `PROTOCOL`, or multi-label);
- decision/instruction;
- affected files or layers;
- superseded decision, if any;
- implementation status.

Current cores may be rewritten to represent active state; the Decision Log preserves historical continuity.

### 5.4 Working Argument Map — `docs/argument-map.md`

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

### 5.5 Approved Framework Snapshots — `docs/frameworks/FW-xxx.md`

An Approved Framework Snapshot is created only after explicit human review and confirmation.

A snapshot MUST NOT be silently modified after approval.

Material changes to the intellectual architecture MUST create a new framework version.

### 5.6 Framework Status — `docs/framework-status.md`

This file SHOULD state:

- current working framework status;
- latest approved framework identifier;
- current artifact status;
- unresolved synchronization defects;
- final artifact approval status.

### 5.7 Evidence Layer — `evidence/`

Evidence files MAY include:

- literature notes;
- source checks;
- datasets;
- calculations;
- formal derivations;
- empirical notebooks;
- source inventories.

Evidence constrains what can responsibly be claimed but MUST NOT silently rewrite human intention.

### 5.8 Derived Artifact

The paper, book, article, report, presentation, or other output is a derived expression.

It MUST remain compatible with:

- the active Content Core;
- the latest applicable Approved Framework;
- the Form Core;
- known evidence constraints.

---

## 6. Feedback routing

Before persisting substantive human feedback, the AI Agent MUST classify it.

### 6.1 CONTENT

Use when the instruction changes:

- claims;
- arguments;
- definitions;
- distinctions;
- scope;
- interpretation;
- examples that carry substantive meaning;
- questions or conclusions.

Propagation path:

`Human decision -> Decision Log -> Content Core -> Working Argument Map -> Derived Artifact`

### 6.2 FORM

Use when the instruction changes:

- artifact type;
- writing/presentation style;
- typography;
- page layout;
- visual system;
- citation presentation;
- structural presentation conventions that do not themselves change the intellectual claim.

Propagation path:

`Human decision -> Decision Log -> Form Core -> Implementation/Rendering -> Artifact`

### 6.3 PROTOCOL

Use when the instruction changes:

- collaboration workflow;
- persistence rules;
- agent behavior;
- approval mechanics;
- repository organization;
- handoff;
- synchronization or versioning.

Propagation path:

`Human decision -> Decision Log -> Protocol/Governance -> Agent Behavior`

### 6.4 Multi-label feedback

The Agent MUST support multi-label classification when a human instruction genuinely affects more than one domain.

---

## 7. Upstream-first rule

A lower layer MUST NOT be treated as authoritative evidence that the human endorsed a higher-level change.

Therefore substantive changes flow from authoritative state downward.

### 7.1 Content update

1. identify the human decision;
2. log it;
3. update Content Core;
4. update Working Argument Map;
5. determine whether approved framework remains valid;
6. inspect evidence conflicts;
7. propagate into derived artifact;
8. verify synchronization.

### 7.2 Form update

1. identify the human form decision;
2. log it;
3. update Form Core;
4. update reusable style profile only if explicitly cross-project;
5. propagate into implementation;
6. verify rendering.

### 7.3 Protocol update

1. log the workflow decision;
2. update protocol/governance documents;
3. update templates if reusable;
4. avoid changing substantive content merely because the workflow changed.

---

## 8. Proposal status

A HARC project MUST distinguish at least the following statuses where ambiguity would matter:

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

## 10. Framework fidelity

After framework approval, AI Agents MAY expand the work substantially.

The derived artifact MUST NOT materially depart from the approved framework without returning upstream for new human review.

Material deviation includes:

- changing the central thesis;
- adding a new major conclusion;
- removing an essential premise;
- altering the relation among major claims;
- changing scope in a way that changes the argument;
- restructuring the work so the approved reasoning is no longer accurately represented.

---

## 11. Overview projection

The approved framework SHOULD be recoverable from the artifact's reader-facing overview.

Default mappings:

- `ACADEMIC_PAPER`: abstract + introduction;
- `ARTICLE`: opening/introductory overview;
- `BOOK`: introduction/overview chapter + chapter roadmap;
- `REPORT`: executive summary + methodology/structure overview;
- other types: analogous high-level overview specified in Form Core.

The overview need not reproduce the framework verbatim, but MUST represent it faithfully.

---

## 12. Final Artifact Approval Gate

Framework approval and final artifact approval are distinct.

The artifact MAY remain `DERIVED-PROVISIONAL` while AI Agents continue expansion, editing, research integration, and formatting.

Before formal submission, publication, or public release under human authorship, a Human Author SHOULD perform the final review required by the relevant discipline, venue, institution, or authorship standard.

The repository SHOULD record whether the release version is:

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
6. request or await human resolution when necessary;
7. record the resulting decision.

---

## 14. Persistent memory and context limits

HARC provides persistent project memory, not literal infinite model context.

Projects SHOULD scale through:

- concise active cores;
- concise operational maps;
- chronological logs;
- indexed evidence;
- archived historical detail;
- selective retrieval.

The success criterion is **recoverability and traceability**, not simultaneous loading of all history.

---

## 15. Agent handoff

A new AI Agent SHOULD be able to continue normal project work by reading, at minimum:

1. project `AGENTS.md`;
2. Content Core;
3. Form Core;
4. recent Decision Log entries;
5. Working Argument Map;
6. Framework Status and latest approved framework;
7. relevant current artifact and evidence.

If essential constraints exist only in an unavailable chat or hidden memory, the project is non-compliant until they are externalized.

---

## 16. Synchronization invariant

At a stable checkpoint, all of the following SHOULD be true:

1. major artifact claims are compatible with Content Core;
2. current intellectual architecture is represented by the Working Argument Map;
3. where an approved framework exists, derived content remains faithful to it or is marked out of sync;
4. important form decisions are compatible with Form Core;
5. important human decisions appear in the Decision Log;
6. unaccepted AI proposals are visibly unaccepted;
7. known evidence conflicts are visible;
8. important decisions are not stranded only in chat history.

Failure of any condition creates an explicit synchronization defect.

---

## 17. Recommended commit semantics

Suggested prefixes:

- `intent:` human content/form decisions;
- `structure:` argument architecture;
- `draft:` derived artifact;
- `form:` presentation/rendering;
- `evidence:` source/data/formal verification;
- `protocol:` workflow/governance;
- `release:` approved protocol or artifact release.

---

## 18. Minimal HARC profile

A lightweight compliant project SHOULD contain at least:

```text
AGENTS.md
core/CONTENT_CORE.md
core/FORM_CORE.md
core/DECISION_LOG.md
docs/argument-map.md
docs/framework-status.md
```

For long or high-stakes projects, evidence directories, approved framework snapshots, and detailed protocol files are strongly recommended.

---

## 19. Portability

HARC v0.1 targets GitHub but separates logical functions from exact filenames.

Future implementations MAY map the same canonical roles to other versioned collaboration systems while preserving:

- explicit state;
- human/AI provenance distinctions;
- approval gates;
- inspectable history;
- cross-agent handoff.

---

## 20. Design thesis

HARC separates four things often collapsed in AI-assisted research:

1. **human intellectual intention**;
2. **human presentation intention**;
3. **AI operational representation**;
4. **derived expression**.

Evidence and history constrain these layers without erasing their different roles.

The protocol treats this separation as the foundation for durable, auditable, human-governed AI-assisted research.
