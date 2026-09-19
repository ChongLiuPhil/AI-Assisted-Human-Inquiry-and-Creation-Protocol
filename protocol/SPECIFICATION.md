# AHICP Protocol Specification

**AI-Assisted Human Inquiry and Creation Protocol**

**Version:** 0.3.0-draft  
**Scope:** GitHub-centered, human-led inquiry, research, reasoning, writing, and creation with assistance from one or more AI agents.

---

## 1. Purpose

AHICP defines a persistent, auditable, human-led protocol for organizing AI assistance in inquiry, research, reasoning, writing, and creation, including retrieval, structuring, proposal generation, drafting, revision, verification, transformation, and project-state maintenance.

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
- meaningful human purpose-setting, understanding, judgment, confirmation, and responsibility.

AHICP v0.3 currently uses GitHub as the persistent repository substrate in its reference implementation. Future implementations may map the same logical roles to other systems.

---

## 2. Normative terms

- **MUST** — required for AHICP compliance.
- **SHOULD** — strongly recommended unless a project records a reason to deviate.
- **MAY** — optional.

---

## 3. Core maxim

A sustained inquiry, research, or creation project MUST NOT treat a transient AI conversation as its sole durable state.

> **Chat is an interaction surface; the repository is durable shared project memory.**

Important project state MUST be externalized into explicit, version-controlled repository artifacts.

---

## 4. Roles

### 4.1 Human Author

The Human Author supplies, revises, or confirms substantive intellectual commitments and presentation intentions.

The purpose, central problem, and direction of a research or creative project MUST originate with the Human Author or be explicitly authorized by the Human Author.

Within AHICP, the Human Author is not only a source of content authorization but must also remain a **bearer of responsibility**. This applies throughout research and inquiry and becomes especially important when research results, arguments, or knowledge claims enter public circulation.

The Human Author MAY use AI Agents as tools to perform or assist with extensive search, synthesis, structuring, drafting, editing, formalization, checking, and formatting. This division of work MUST NOT be treated as a transfer of project purpose, core judgment, framework authorization, responsibility for public knowledge dissemination, or the position of ultimate responsibility.

### 4.2 AI Agent

The AI Agent is a collaboration tool. Normative AHICP language SHOULD NOT characterize AI as a cognitive subject or use “AI performs cognitive labor / cognitive tasks” as protocol terminology; it should identify the concrete work AI performs or assists.

The AI Agent MAY:

- extract and normalize human decisions;
- maintain repository state;
- propose arguments, objections, distinctions, examples, terminology, and structure;
- conduct research and evidence checks when tools permit;
- maintain operational argument representations;
- expand approved structures into prose or other artifacts;
- detect inconsistencies, evidence conflicts, and synchronization defects;
- maintain formatting and rendering systems.

The AI Agent MUST distinguish its proposals from human-approved commitments and MUST NOT be treated as the ultimate bearer of responsibility for research purpose, framework authorization, or public dissemination of knowledge.

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

### 5.4 Working Memory Area

Working Memory is parallel to the three Long-Term Project Memory layers and specifies **logical functions**, not one mandatory physical file.

A project MUST provide or equivalently implement:

- **Working Memory Index / Resolver** — maps the components;
- **Current Focus** — highest-priority immediate objective, current stage, primary blocker, and immediate next action;
- **Task Plan** — active tasks, next actions, TODO/backlog, blockers, pending human decisions, Clarifications, and sync defects;
- **Work Log** — a stage-level historical chronicle primarily for human retrospective review.

A project MAY map several roles to one file or split them across multiple files. The Manifest MUST state the actual mapping.

Clarification is an item type inside Task Plan / Working Memory. High-impact uncertainty that could alter core claims, key concepts, scope, major inferential relations, section functions, important terminology/translation, or Framework Approval MUST become a Clarification item rather than being silently guessed.

Open Clarifications MUST NOT be treated as human commitments.

After human resolution:

`Working Memory -> human resolution -> Decision Log -> appropriate Long-Term Memory destination`

For human core content:

`Layer 1 Core -> Layer 2 Framework -> Layer 3 Artifact`

Completed tasks leave the active Task Plan and receive a high-level historical summary in Work Log; if they create durable normative results, Promotion also occurs.

Work Log MUST NOT store hidden AI chain-of-thought/scratchpads, MUST NOT replace current state, and SHOULD NOT be default required context for new-Agent onboarding.

See `protocol/WORKING_MEMORY.md`.

### 5.5 Working Argument Map — `docs/argument-map.md`

The Working Argument Map is the primary operational discussion interface for long-form intellectual structure.

It is normally AI-maintained and MUST be treated as mutable until human approval.

It SHOULD expose:

- central question / project problem;
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

Framework Approval requires the Human Author to clearly understand, review item by item, and explicitly confirm every substantive element actually represented in the proposed framework, including core theses, inferential relations, key distinctions, scope conditions, section/chapter functions, and any specific wording included in the framework. AI may assist in creating the representation, but it cannot replace human authorization of the project’s direction and intellectual architecture.

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

If a derived artifact enters public circulation, the project MUST retain identifiable human bearers of responsibility. AI generation, expansion, or editing MUST NOT eliminate or replace this responsibility-bearing requirement.

---

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
5. do not alter substantive project content merely because governance changed.

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

AHICP distinguishes:

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

## 14. AI work delegation and human epistemic responsibility

AHICP distinguishes **work that AI may perform or assist** from **human epistemic judgment and responsibility that cannot be transferred**.

AI MAY perform extensive search, synthesis, structuring, drafting, formalization, consistency checking, revision, and formatting.

Human attention SHOULD be concentrated on high-leverage decisions, including:

- project purpose, research aims, and central questions;
- core commitments;
- major inferential architecture;
- acceptance/rejection of material AI proposals;
- treatment of decisive evidence conflicts;
- Framework Approval;
- Final Artifact Approval where required.

AHICP does not claim that file structure alone guarantees good judgment. Approval mechanisms are governance scaffolds, not substitutes for human competence and understanding.

---

## 15. Persistent memory and context limits

AHICP provides persistent project memory, not literal infinite model context.

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

### 16.1 Zero-context Bootstrap

A project SHOULD provide at repository root:

- `START_HERE.zh-CN.md` / English mirror;
- `BOOTSTRAP_PROMPT.zh-CN.md` / English mirror;
- `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` / English mirror;
- `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` / English mirror;
- `AHICP_MANIFEST.yaml`;
- `AHICP_CONTEXT_INTERFACE.yaml` or equivalent machine-readable context policy;
- root `AGENTS.zh-CN.md` / English mirror;
- a discoverable Onboarding Handshake specification.

Before substantive work, a new AI Agent MUST read the control plane, Working Memory Index, Current Focus, and Task Plan, then SHOULD output a AHICP Onboarding Report covering the highest-priority objective, primary blocker, immediate next action, active tasks, next actions, blockers, pending human decisions/Clarifications, Framework/Artifact state, synchronization defects, and permitted next action. Work Log is skipped by default. The Onboarding Report MUST confirm `AHICP REPOSITORY CONTEXT — ACTIVE`. This loads only the access kernel; dynamic Blocking Clarifications, Framework, Artifact, and Core state must still be retrieved on demand from latest canonical GitHub revisions.

If the Agent cannot produce this report from repository state, the project has an onboarding/persistence defect.

### 16.2 Normal handoff reading

A new AI Agent SHOULD be able to continue normal project work by reading, at minimum:

1. `START_HERE.zh-CN.md`, `AHICP_MANIFEST.yaml`, and `AHICP_CONTEXT_INTERFACE.yaml`;
2. project `AGENTS.zh-CN.md`;
3. Working Memory Index;
4. Current Focus;
5. Task Plan;
6. task-relevant Layer 1 Core / Decision Log;
7. task-relevant Layer 2 Framework Status / Working or Approved Framework;
8. task-relevant Layer 3 Artifact;
9. relevant Evidence.

Work Log is read only when the human requests historical review, during dedicated audit/change reconstruction, or when current state conflicts with history.

A project SHOULD record the AHICP version/tag/commit it adopted so later upstream protocol changes are not silently treated as already accepted governance.

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
9. onboarding documents point to current canonical files;
10. Current Focus explicitly states the highest-priority objective and immediate next action;
11. all current blockers, pending human decisions, and Clarifications are explicitly visible in Task Plan rather than existing only in chat or private AI judgment;
12. completed tasks leave active Task Plan and are summarized into Work Log at an appropriate granularity;
13. stable resolved Working Memory results have been promoted into appropriate Long-Term Memory, and Work Log does not serve as the normative answer.

Failure of any condition creates an explicit synchronization defect.

---

## 19. Multi-pass audit and repair discipline

A requested multi-pass audit MUST be interpreted as repeated review-and-repair cycles.

Each cycle SHOULD execute:

`review -> identify defect -> repair/implement -> verify repair`.

If three passes are requested, perform three such cycles. If a post-repair audit is requested, perform a further independent audit after all three cycles rather than counting one of the three cycles as the final audit.

Audit records SHOULD state what defect was found, what repository change repaired it, and how the repair was verified.

---

## 20. Methodology article as a governed AHICP artifact

The AHICP project itself SHOULD maintain two mutually supporting outputs:

1. an executable open protocol;
2. a methodology article explaining and critically developing the protocol.

The methodology article SHOULD address the conceptual implications of AI-assisted research, including human cognitive/epistemic responsibility, delegable and non-delegable intellectual work, persistent research state, semantic version control, framework-level authorship, and publication accountability.

The article MUST itself follow AHICP discipline:

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

## 22. Minimal AHICP profile

A lightweight compliant project SHOULD contain at least:

```text
START_HERE.zh-CN.md
START_HERE.md
BOOTSTRAP_PROMPT.zh-CN.md
BOOTSTRAP_PROMPT.md
SESSION_CONTEXT_BOOTSTRAP.zh-CN.md
SESSION_CONTEXT_BOOTSTRAP.md
ONBOARDING_REPORT_TEMPLATE.zh-CN.md
ONBOARDING_REPORT_TEMPLATE.md
AGENTS.zh-CN.md
AGENTS.md
AHICP_MANIFEST.yaml
AHICP_CONTEXT_INTERFACE.yaml
core/CONTENT_CORE.zh-CN.md
core/CONTENT_CORE.md
core/FORM_CORE.zh-CN.md
core/FORM_CORE.md
core/DECISION_LOG.zh-CN.md
core/DECISION_LOG.md
docs/working-memory.zh-CN.md
docs/working-memory.md
docs/working-memory/current-focus.zh-CN.md
docs/working-memory/current-focus.md
docs/working-memory/task-plan.zh-CN.md
docs/working-memory/task-plan.md
docs/working-memory/work-log.zh-CN.md
docs/working-memory/work-log.md
docs/argument-map.zh-CN.md
docs/argument-map.md
docs/framework-status.zh-CN.md
docs/framework-status.md
```

The Chinese files are canonical and the English files are synchronized mirrors.

A single-file implementation may map multiple Working Memory roles to the same path; the default template uses the split layout.

The legacy clarification-register path may be retained as a compatibility pointer but is not required as an active state file.

For long or high-stakes projects, evidence directories, Approved Framework snapshots, detailed protocol files, and audit records are strongly recommended.

---

## 23. External Systems, Tool Discovery, Authorization, and Human Handoff

### 23.1 Machine-operable-first escalation

When a task requires an external system, account, or service and the human authorization needed for that task already exists, an AI Agent **SHOULD** first safely discover and exhaust currently available and authorized machine-operable paths before handing routine operational steps back to the human.

Paths to inspect include at least:

- platform built-in tools;
- connected plugins / connectors;
- official MCP servers or equivalent official tool interfaces;
- official provider APIs;
- official GitHub Apps or other provider-managed integrations;
- existing repository automation / workflows that are approved for use;
- adapters / plugins explicitly approved by the human or project governance.

Being shown as “installed,” “enabled,” “connected,” or present in a directory **does not prove that a capability is actually callable**. When capability availability affects the execution route or a decision to escalate to a human, the Agent **MUST**, when technically possible and safe, perform a real, minimal, preferably read-only capability probe. If the current host does not expose an actual invocation path, the Agent must record the capability as unavailable or unverified in the current environment rather than treating directory state as verified capability.

### 23.2 Authorization and credential safety

Where functionally equivalent paths exist, the Agent **SHOULD** prefer official, OAuth, provider-managed, least-secret-handling integrations and, where the provider supports it, the minimum permission scope needed for the task.

The Agent **MUST NOT** ask a human to paste passwords, API tokens, private keys, recovery codes, or other secrets into chat merely to simplify execution. When a credential must be created or stored by a human, the handoff should keep the secret inside the provider or an approved secret store and explicitly state which values must not be sent to the AI.

The Agent must not bypass:

- identity verification;
- account-owner consent;
- permission grants;
- human-reserved high-impact or non-delegable approvals;
- project-defined public / canonical cutover, release, or other responsibility boundaries.

### 23.3 Human handoff

An action should be escalated to a human only when the next step genuinely requires human identity authorization, account-owner consent, a non-delegable high-impact decision, or an action that the currently available and authorized tool capabilities cannot perform.

Such a handoff **MUST**:

1. reduce the instructions to the minimum set needed to clear the current blocker;
2. request only the human action that is necessary now, rather than delegating later machine-operable steps;
3. assume no technical background and use provider UI names and observable completion conditions;
4. state explicitly which passwords, tokens, secrets, private keys, or similar values must not be sent to the AI;
5. define a completion condition that the AI can independently verify after authorization.

After the human completes the necessary action, the Agent **SHOULD** re-read current repository state, re-probe the relevant capability, and resume from the interruption point rather than asking the human to restate project context or continue performing machine-operable steps.

### 23.4 Provider actual state and repository durable state

Provider dashboards, transient UI screens, chat state, and model memory are not authoritative project state.

After an external action, the Agent **SHOULD** verify actual provider state. If that action changes durable project state that will affect future work, the Agent **MUST** write the verified result through to the appropriate repository-backed durable state. As needed, the record should include observed state, verification evidence or references, useful build/deployment identifiers, current blockers, and authorization/cutover status, but it must not contain secrets.

The provider is the direct observation source for its live account configuration and runtime results; the repository stores the project's durable, auditable interpretation of those observations. If the two disagree, the Agent must re-check the provider and update or mark repository state stale / unresolved rather than relying on old chat, old UI captures, or model memory.

### 23.5 Authorization scope and durable-state action lifecycle

A **durable-state change** is a change that survives the current interaction and can constrain later work or affect external parties. Durability alone does not make an action high-impact. A routine, reversible repository or provider write that is already within a valid authorization scope **SHOULD NOT** be escalated merely because it persists.

Before machine execution, the Agent **MUST** keep the following states distinct:

~~~text
proposal
!= authorization
!= execution
!= verification
!= durable write-back
~~~

A proposal may describe or recommend an action without authorizing it. Authorization permits only the covered action. Execution does not prove that the intended state was reached. Verification establishes observed actual state. Durable write-back records the verified result for future work; it does not retroactively create authorization.

For an action whose authorization boundary matters, the repository-backed authorization record or policy **SHOULD** identify, to a level proportionate to the risk:

- **action class** — what kind of action is permitted;
- **target** — the repository, branch, artifact, account, channel, endpoint, audience, or other object covered;
- **allowed side effects** — effects that are inside the authorization rather than incidental surprises;
- **reversibility / rollback assumptions** — whether and how the action can be undone;
- **duration or occurrence bound** — one action, a bounded period, a named workflow, or another clear limit;
- **escalation condition** — what change in scope, impact, uncertainty, or provider state requires renewed human review;
- **authorization provenance** — the human decision or durable human-approved policy from which authority derives.

Valid authorization may come from:

1. an explicit human decision for the current action or transition; or
2. a durable human-approved pre-authorization policy whose scope actually covers the action.

A pre-authorization policy **MUST NOT** override an action class that AHICP or project governance marks as human-reserved / non-delegable. Such an action requires the human authorization specified by that governing rule.

An Agent **MUST NOT** infer authorization merely from AI proposal, technical capability, repository visibility, provider configuration, provider reachability, build/deployment success, an existing endpoint, an upstream branch/tag/version change, or any other machine-observed fact.

### 23.5.1 Human choice of authorization mode at initial configuration

When first configuring an integration, automation, or workflow whose later machine actions will rely on a reusable authorization policy, the Agent **MUST NOT** silently choose the authorization mode for the human, and must not first establish that policy through configuration and then treat the resulting technical state as authorization.

Before continuing configuration that depends on such a policy, the Agent **MUST**:

1. analyze the expected action classes, targets, allowed side effects, reversibility, and high-impact boundaries;
2. propose one or more authorization patterns appropriate to the situation, explaining their scope, convenience, control boundary, and escalation conditions;
3. when applicable, distinguish at least:
   - **per-action authorization** — each action or state transition designated as requiring separate authorization is confirmed by the human when it occurs;
   - **bounded pre-authorization** — the human approves a clearly bounded action-class / target / side-effect / duration scope in advance, within which the Agent may act repeatedly;
   - **mixed policy** — selected low-risk actions use bounded pre-authorization while specified high-impact or human-reserved actions continue to require per-action human decisions;
4. require the human to select, modify, or reject the proposed pattern;
5. record the final choice and its authorization provenance in repository durable state before later operations rely on it.

The AI recommendation is a proposal, not a human commitment. After the human selects the policy, the Agent may continue machine-operable configuration and later operations that fall within the selected scope. If future action class, target, side effects, impact, reversibility, or duration exceeds that choice, renewed human selection/authorization is required.

### 23.5.2 Provider-neutral high-impact test

An action is high-impact when its reasonably foreseeable effect can materially alter one or more of these boundaries:

- **human/project external commitment or public representation** — including release, publication, submission, or communication performed on behalf of the human/project;
- **access, confidentiality, security, identity, ownership, or permission boundaries**;
- **canonical identity, routing, production/public cutover, or retirement of a previously relied-on identity/route**;
- **adopted governance authority** — including which protocol, framework, policy, version, tag, or commit governs later work;
- **irreversible or materially difficult-to-reverse state**, especially deletion, destructive migration, or loss of a reliable rollback path.

These are impact dimensions, not provider-specific action names. A repository write, merge, deployment, email send, API call, or configuration change is **not automatically** one authorization level merely because of its technical category. For example, a reversible branch write may be routine within scope, while a public release or canonical cutover may cross a human-reserved boundary. Likewise, deployment is not by itself equivalent to release, publication authorization, or canonical cutover.

The Agent **MUST** escalate for human authorization when:

- the action is human-reserved / non-delegable;
- no valid authorization source covers the action;
- the target or side effects exceed the recorded scope; or
- reversibility, impact, or uncertainty has materially changed beyond the assumptions under which authorization was granted.

The Agent **SHOULD NOT** escalate a low-risk, reversible, already-authorized machine operation solely because it changes durable state.

After execution, follow §23.4: verify actual state and write the verified durable result back to the repository. If verification fails or observed effects exceed authorization, stop further propagation, mark state unresolved/stale as appropriate, and escalate only the new authorization or judgment that is actually required.

If a project adopts PPF or another publishing framework, that framework defines publication-lifecycle state semantics. AHICP governs authorization provenance, scope, escalation, execution/verification separation, and durable write-back; it does not redefine the publishing lifecycle.

---

## 24. Portability

AHICP v0.3 currently targets GitHub in its reference implementation but separates logical functions from exact filenames.

Future implementations MAY map the same canonical roles to other versioned collaboration systems while preserving explicit state, human/AI provenance distinctions, approval gates, inspectable history, and cross-agent handoff.

---

## 25. Design thesis

AHICP separates things that AI-assisted inquiry, research, and creation often collapse:

1. Layer 1 — Human Authorial Core;
2. Layer 2 — Current Framework;
3. Layer 3 — Derived Artifact;
4. Working Memory in parallel with the three long-term layers;
5. human presentation intention;
6. evidence constraints;
7. approval state;
8. historical decisions.

The protocol treats this separation as the basis for durable, auditable, human-governed AI-assisted inquiry and creation.

## 26. Bilingual canonical synchronization

AHICP project documentation SHOULD be maintained bilingually in Chinese and English.

For AHICP's own repository, and for projects that adopt the bilingual profile:

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
