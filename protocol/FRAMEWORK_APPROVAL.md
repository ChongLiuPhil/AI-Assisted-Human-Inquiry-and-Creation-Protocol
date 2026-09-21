# Framework Approval and Responsibility Model

> **Language:** Chinese canonical: `FRAMEWORK_APPROVAL.zh-CN.md`; this English file is the synchronized mirror.

## 1. Two states of the operational framework

AHICP distinguishes:

1. **Working Framework** — mutable, AI-maintained, open to discussion.
2. **Approved Framework Snapshot** — explicitly reviewed and confirmed by the human author.

The first is a tool for collaboration. The second is a durable record of the intellectual architecture the human actually accepted.

## 2. Framework Approval Gate

A framework is ready to enter approval review when it compactly but adequately states:

- central question;
- thesis or thesis set;
- key concepts and distinctions;
- principal supporting claims;
- dependency relations among claims;
- major sections/chapters and their roles;
- important scope conditions and limitations;
- intentionally unresolved questions;
- known evidence conflicts that materially affect the argument;
- any specific wording deliberately included in the framework and therefore made part of its intellectual representation.

Being ready for approval is not the same as being approved. Framework Approval requires the human author to clearly understand, carefully review item by item, and explicitly confirm **every substantive element actually represented in the proposed framework**. The human cannot give only a blanket approval to headings, a summary, or the general idea and then treat substantive framework details that were not understood or reviewed as approved.

An AI Agent may assist in proposing, organizing, compressing, and expressing the Working Framework, but it cannot replace human authorization of project purpose, direction, and intellectual architecture.

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

## 2.5 Working Memory / Clarification Gate

Before Framework Approval, inspect BLOCKERS, PENDING_HUMAN_DECISIONS, and Clarifications in `docs/working-memory/task-plan.zh-CN.md`, and verify that Current Focus still points to the same gate.

As a rule, a framework should not be approved while a `BLOCKING` item remains unresolved if it could alter a central thesis, key concept, major inferential relation, scope, or section function.

A framework may retain items explicitly marked `AI-PROPOSED`, `UNRESOLVED`, `NON-BLOCKING`, `DEFERRED`, or equivalent, provided that:

1. their unresolved/provisional status is explicit in the framework; and
2. they are not unresolved blocking premises required in order to approve the current core intellectual architecture.

When the human gives an overall `APPROVE` decision on a complete framework containing such items, the approval covers **their place, scope, and treatment as unresolved/provisional items within the framework**, not their unconfirmed substantive content. Framework Approval MUST NOT automatically change their provenance or promote provisional terminology, empirical plans, theoretical positioning, or other AI proposals into human-originated or human-confirmed commitments.

Only a later independent human decision may change their provenance, approval, or Promotion status.

If the human explicitly chooses to defer an issue, mark it `DEFERRED` and preserve that unresolved status explicitly in the framework rather than pretending it is resolved.

Framework Approval must not rest on key interpretations that the AI privately guessed.

## 3. What framework approval means

Framework Approval is the project's main substantive intellectual checkpoint and the structural anchor of core intellectual responsibility borne by humans.

It indicates that the human has understood, reviewed, and accepted every substantive element **actually represented as a current commitment** in the framework, including:

- central theses;
- major inferential relations and their logical dependencies;
- core distinctions;
- organization of the reasoning;
- intended role of major sections/chapters;
- scope conditions;
- declared limitations;
- specific wording included in the framework as a current commitment.

For items explicitly marked unresolved, provisional, or AI-proposed, Framework Approval indicates that the human understands and accepts **their unresolved status and their place and treatment within the current architecture**; it does not indicate acceptance of their still-unapproved substantive content.

An Approved Framework may therefore contain explicit unresolved items, but those items MUST retain their existing provenance / approval status until another explicit human decision changes them.

Framework Approval allows development to proceed without requiring human line-by-line approval of every provisional AI expansion, but it does not permit the human to approve only a high-level summary while ignoring substantive details inside the framework itself.

Framework Approval is a AHICP governance architecture; it should not automatically be presented as a universal theory of authorship across all disciplines, institutions, or publication regimes.

### 3.5 Framework Approval and bounded auto-merge authorization

When a dedicated PR contains only:

- implementation of an Approved Framework;
- direct synchronization/governance changes related to that Framework and explicitly authorized by the human;
- non-substantive validation, citation, formatting, or state repair;

and all of the following are true:

- latest-head required CI / validation is green;
- no unresolved blocking review / review thread remains;
- no unauthorized substantive scope expansion exists beyond the approved scope;
- any substantive change added after Framework Approval has separate explicit human authorization;
- the branch is synchronized with its target base, or has been synchronized without unresolved conflict;
- the merge does not bypass provider-side required protections, permissions, or human-reserved gates;

then Framework Approval may also constitute **bounded auto-merge authorization** for that dedicated PR.

The purpose is to avoid requesting a second, duplicative merge approval merely to move the same approved work into `main`.

It does not authorize:

- publication / release / submission;
- deployment or other external side effects;
- secret handling;
- later-added unrelated features;
- scope-expanded changes;
- Final Artifact Approval.

If any condition ceases to hold, the auto-merge authorization expires and the Agent must return to the ordinary authorization flow.

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

## 6. Framework defect versus expansion defect

AHICP should keep two kinds of defect analytically separate.

### Framework-level defect

A problem belongs to the framework level when it is already present in the human-approved intellectual architecture, for example:

- a central thesis is mistaken or inadequately formulated;
- a major inference does not follow;
- an essential distinction is missing;
- a chapter or section is assigned the wrong argumentative role;
- a scope limitation is absent in a way that changes the claim.

Because the approved framework is the human-confirmed substantive baseline, such a defect is a defect in the confirmed intellectual architecture.

### Derived-expansion defect

A problem belongs only to the expansion level when the approved framework remains sound but later AI-generated implementation introduces a local flaw, for example:

- weak or ambiguous wording;
- an unnecessary or poor example;
- a clumsy transition;
- a formatting mistake;
- a local explanatory omission that does not alter the approved structure.

Before final artifact approval, such a defect should not be retroactively attributed to the approved framework. It should be corrected downstream unless it reveals a deeper framework problem.

This distinction allows long-form projects to concentrate high-intensity human review on core intellectual architecture while still preserving a separate final-release review requirement.

## 7. Overview projection

The final artifact should make the approved framework visible to readers through its overview sections.

Recommended mapping:

- **Academic paper:** abstract + introduction;
- **Article:** opening/introductory overview;
- **Book:** introduction/overview chapter + chapter roadmap;
- **Report:** executive summary + structure/method overview.

The wording may differ, but the intellectual structure should remain recoverable.

## 8. Final Artifact Approval Gate

Framework Approval is not identical to release approval.

Before formal submission, publication, or public release under human authorship, the concrete release version should undergo the human review required by the applicable discipline, institution, publisher, or venue.

When an artifact enters public knowledge circulation, a core function of Final Artifact Approval is to ensure that **identifiable human bearers of responsibility remain answerable for its knowledge claims, accuracy, integrity, and release decision.** AI Agents may participate in generation, expansion, editing, and checking, but they cannot replace this responsibility-bearing position.

Recommended states:

- `WORKING-FRAMEWORK`
- `FRAMEWORK-APPROVED`
- `DERIVED-PROVISIONAL`
- `FINAL-REVIEW`
- `FINAL-APPROVED`

---

## 9. Responsibility-bearing subjects and layers of responsibility

AHICP distinguishes:

### Project purpose and direction

The purpose, central problem, and direction of research or creative work originate with humans and remain under human initiation, navigation, or approval. AI Agents are collaboration tools that may perform or assist substantial concrete work, but they cannot become the ultimate bearers of responsibility for project purpose and direction.

### Intellectual architecture

Responsibility is anchored primarily in the human-approved framework. Humans, as the bearers of responsibility, are responsible for understanding, reviewing, judging, and confirming every substantive element actually represented there.

### Derived-expression quality control

AI may perform or assist extensive expansion, restructuring, and expression work; concrete factual, evidential, expressive, and implementation defects in later derived text remain subject to checking and revision. AI participation does not alter the human responsibility-bearing status.

### Public knowledge dissemination and scholarly accountability

When research results, arguments, or knowledge claims enter public circulation, identifiable human bearers of responsibility must remain. Release/submission decisions, together with accuracy, integrity, research-integrity obligations, and public accountability required by applicable standards, remain human responsibilities and are handled through the separate Final Artifact Approval Gate.

A concise formulation is:

> **AHICP permits extensive AI participation in carrying out research work, while humans remain the bearers of responsibility: humans supply and authorize project purpose and direction, bear core intellectual responsibility through a framework they fully understand and approve, and bear final release responsibility for concrete public knowledge artifacts through Final Artifact Approval.**

This is AHICP's governance model. It does not claim that Framework Approval by itself supplies a universal cross-domain theory of authorship.
