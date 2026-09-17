# Framework Approval and Responsibility Model

## 1. Two states of the operational framework

HARC distinguishes:

1. **Working Framework** — mutable, AI-maintained, open to discussion.
2. **Approved Framework Snapshot** — explicitly reviewed and confirmed by the human author.

The first is a tool for collaboration. The second is a durable record of the intellectual architecture the human actually accepted.

## 2. Framework Approval Gate

A framework is ready for approval when it compactly states:

- central question;
- thesis or thesis set;
- key concepts and distinctions;
- principal supporting claims;
- dependency relations among claims;
- major sections/chapters and their roles;
- important limitations;
- intentionally unresolved questions;
- known evidence conflicts that materially affect the argument.

When the human explicitly approves it, the agent should create:

`docs/frameworks/FW-001.md`

or the next available identifier.

The snapshot should record:

- approval identifier;
- date;
- approval state;
- source working-map state/commit where practical;
- complete approved framework.

An approved snapshot is immutable. Material change requires a new version.

## 3. What framework approval means

Framework approval is the project's main substantive intellectual checkpoint.

It indicates human acceptance of:

- central theses;
- major inferential relations;
- core distinctions;
- organization of the reasoning;
- intended role of major sections/chapters;
- declared limitations and unresolved issues.

It allows human attention to focus on the intellectual architecture rather than requiring line-by-line approval of every provisional AI expansion during development.

## 4. Derived expansion

After framework approval, AI agents may expand the framework into:

- prose;
- examples;
- transitions;
- literature discussion;
- explanatory detail;
- notes;
- supporting tables/figures;
- formatting and presentation.

This expansion remains constrained by:

- Content Core;
- Approved Framework;
- Form Core;
- evidence;
- scholarly accuracy.

Until final approval, the artifact should remain `DERIVED-PROVISIONAL`.

## 5. Framework fidelity

The derived artifact must preserve the approved framework in substance.

Material deviation includes:

- changing the central thesis;
- adding a new major conclusion;
- removing a premise essential to the approved inference;
- changing relations among major claims;
- altering scope in a way that changes the argument;
- reorganizing sections so the approved reasoning is no longer accurately represented.

When material deviation occurs, return upstream and create a new Working Framework for human review.

## 6. Overview projection

The final artifact should make the approved framework visible to readers through its overview sections.

Recommended mapping:

- **Academic paper:** abstract + introduction;
- **Article:** opening/introductory overview;
- **Book:** introduction/overview chapter + chapter roadmap;
- **Report:** executive summary + structure/method overview.

The wording may differ, but the intellectual structure should remain recoverable.

## 7. Final Artifact Approval Gate

Framework approval is not identical to release approval.

Before formal submission, publication, or public release under human authorship, the concrete release version should undergo the human review required by the applicable discipline, institution, publisher, or venue.

Recommended states:

- `WORKING-FRAMEWORK`
- `FRAMEWORK-APPROVED`
- `DERIVED-PROVISIONAL`
- `FINAL-REVIEW`
- `FINAL-APPROVED`

## 8. Responsibility distinction

HARC distinguishes:

### Intellectual-architecture responsibility

Anchored strongly in the human-approved framework.

### Derived-expression quality control

AI may produce much of the expansion; defects remain subject to checking and revision.

### Public scholarly accountability

The release/submission decision remains a human responsibility to the extent required by relevant external standards.

A concise formulation is:

> **Framework approval defines the center of substantive intellectual authorship; final artifact approval defines the threshold of public scholarly accountability.**
