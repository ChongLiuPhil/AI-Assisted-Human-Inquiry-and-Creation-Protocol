# Founding-Idea Integration Audit

> **Language:** Chinese canonical: `FOUNDING_IDEA_AUDIT.zh-CN.md`; this English file is the synchronized mirror.

**Audit date:** 2026-09-17  
**Scope:** Human-originated ideas stated during the conversations that led to HARC.  
**Status:** Three-pass audit completed.

> This document is an AI-maintained audit of coverage. It is not itself a replacement for `core/PROTOCOL_CORE.md` or the human decision log.

---

## Audit method

The founding discussions were checked three times using different criteria.

### Pass 1 — Semantic coverage

Question: **Has each distinct human-originated collaboration idea been represented somewhere in HARC without being silently replaced by an AI reinterpretation?**

#### F21 — Bilingual Chinese/English governance

**Founding idea (added 2026-09-18):** all substantive HARC project content must be maintained in Chinese and English; Chinese is the canonical editing/review baseline; every substantive edit must synchronize the English mirror; Chinese governs conflicts.

**Implemented in:**

- Protocol Core P18
- HARC-D015
- `protocol/BILINGUAL_SYNC.zh-CN.md`
- Specification bilingual synchronization section
- AGENTS bilingual contract
- repository-wide bilingual migration

**Status:** FULLY INTEGRATED AFTER BILINGUAL PARITY AUDIT.

---

# Pass 2 — Operational coverage

Question: **Is each idea merely described, or can a project actually execute it through files, states, templates, update paths, and approval rules?**

##### Gap D — Bilingual governance required retrofitting legacy single-language files

**Fix:** added Chinese-canonical / English-mirror governance and initiated repository-wide migration. Final status is verified by a dedicated bilingual parity audit.

---

# Pass 3 — New-agent handoff simulation

Question: **If the original chat disappears and a new competent AI agent receives only the repository, can it reconstruct and continue the intended collaboration model?**

---

# Pass 1 — Semantic coverage

## F01 — GitHub as persistent collaborative research memory

**Founding idea:** project continuity should live explicitly in GitHub text/version state rather than depend on one AI account, platform memory, model, or chat context.

**Implemented in:**

- `core/PROTOCOL_CORE.md` P1, P9, P10
- `protocol/PERSISTENT_MEMORY.md`
- `protocol/SPECIFICATION.md` §§3, 14, 15
- project `AGENTS.md`

**Status:** FULLY INTEGRATED.

---

## F02 — Preserve human research-content intentions in a foundational text

**Founding idea:** human statements, corrections, confirmations, rejections, and revisions that matter to the research topic should be deposited into a basic canonical content document.

**Implemented in:**

- `core/PROTOCOL_CORE.md` P2
- HARC `Content Core` model
- `templates/research-project/core/CONTENT_CORE.md`
- Decision Log + upstream-first rules

**Status:** FULLY INTEGRATED.

---

## F03 — AI expansion must remain subordinate to the human content foundation

**Founding idea:** AI elaboration should not silently contradict, replace, or drift away from the human author's foundational thought.

**Implemented in:**

- Protocol Core P2, P5, P8
- Specification §§7, 8, 10, 16
- Framework fidelity rules

**Status:** FULLY INTEGRATED.

---

## F04 — Maintain a second operational text extracted/structured by AI

**Founding idea:** AI should maintain a compressed representation of the actual argument of the article/book, exposing claims, relations, section/chapter roles, and open issues.

**Implemented in:**

- Protocol Core P4
- `docs/argument-map.md` model
- `templates/research-project/docs/argument-map.md`
- Specification §5.4

**Status:** FULLY INTEGRATED.

---

## F05 — Make the operational framework the main human–AI discussion interface

**Founding idea:** for large works, human–AI structural discussion should primarily operate on the compact framework rather than repeatedly rereading the full expanded manuscript.

**Implemented in:**

- Protocol Core P4
- Specification §5.4
- Chinese and English white papers
- project-agent template

**Status:** FULLY INTEGRATED.

---

## F06 — Human changes propagate upstream first

**Founding idea:** after substantive human feedback, first persist the human decision in the foundational layer, then update the operational framework, then revise/expand the final artifact.

**Implemented in:**

- Protocol Core P5
- Specification §7
- `CONTENT / FORM / PROTOCOL` routes
- template AGENTS contract

**Status:** FULLY INTEGRATED.

---

## F07 — Separate research content from form/presentation

**Founding idea:** claims and arguments are different from typography, layout, visual design, citation presentation, formatting, and artifact form; agents should classify the instruction before persistence.

**Implemented in:**

- Protocol Core P3
- `protocol/FORM_CONTENT_ROUTING.md`
- Specification §§5.1–5.2 and §6
- separate Content Core and Form Core templates

**Status:** FULLY INTEGRATED.

---

## F08 — Form preferences should be reusable across projects

**Founding idea:** an author may develop recurring presentation habits/preferences that can be reused across books, papers, or articles rather than being rebuilt from scratch.

**Implemented in:**

- Protocol Core P3 and P14
- `protocol/FORM_PROFILE_INHERITANCE.md`
- `templates/form-profiles/AUTHOR_PROFILE.md`

**Status:** FULLY INTEGRATED AFTER AUDIT FIX.

---

## F09 — Different artifact types need different form profiles

**Founding idea:** a book, academic paper, and ordinary article can share author-level preferences while requiring different artifact-type formatting structures.

**Implemented in:**

- Protocol Core P14
- `protocol/FORM_PROFILE_INHERITANCE.md`
- `templates/form-profiles/BOOK.md`
- `templates/form-profiles/ACADEMIC_PAPER.md`
- `templates/form-profiles/ARTICLE.md`

**Status:** FULLY INTEGRATED AFTER AUDIT FIX.

---

## F10 — AI defaults must not become fake author preferences

**Founding idea:** temporary implementation choices should be distinguishable from genuine human form decisions.

**Implemented in:**

- Form Core model
- Specification §8
- `TEMPORARY-DEFAULT` status
- form-profile inheritance protocol

**Status:** FULLY INTEGRATED.

---

## F11 — Working Framework and Human-Approved Framework must be distinct

**Founding idea:** the AI-maintained operational representation is not automatically endorsed by the human. A version becomes authoritative only after explicit human reading/confirmation.

**Implemented in:**

- Protocol Core P6
- `protocol/FRAMEWORK_APPROVAL.md`
- `docs/framework-status.md` model
- immutable `FW-xxx` snapshot convention

**Status:** FULLY INTEGRATED.

---

## F12 — Approved framework is the primary substantive intellectual responsibility anchor

**Founding idea:** in a long AI-expanded work, the human author's highest-intensity substantive responsibility should concentrate on understanding and confirming the core thesis set, argument relations, distinctions, and section/chapter functions represented by the approved framework.

**Implemented in:**

- Protocol Core P6 and P13
- Decision HARC-D011
- `protocol/FRAMEWORK_APPROVAL.md`
- white paper responsibility model

**Status:** FULLY INTEGRATED AFTER AUDIT CLARIFICATION.

---

## F13 — Distinguish framework defects from AI-expansion defects

**Founding idea:** a defect in the human-confirmed argument structure is different from a local defect introduced in later AI prose/implementation; the two should not be conflated.

**Implemented in:**

- Protocol Core P13
- `protocol/FRAMEWORK_APPROVAL.md` §6
- `DERIVED-PROVISIONAL` state

**Status:** FULLY INTEGRATED AFTER AUDIT CLARIFICATION.

**Qualification:** HARC also preserves a separate final-artifact approval gate before public submission/release under human authorship, because framework approval does not by itself satisfy every external authorship/accountability requirement.

---

## F14 — Approved framework must project into reader-facing overview

**Founding idea:** the confirmed intellectual architecture should appear in the final work's abstract/introduction, opening overview, or book introduction/chapter roadmap as appropriate.

**Implemented in:**

- Protocol Core P7
- Specification §11
- Framework Approval overview-projection rule
- artifact-type form profiles

**Status:** FULLY INTEGRATED.

---

## F15 — Repository memory can grow while active state stays compact

**Founding idea:** externalized project memory should allow long-term accumulation beyond one chat context, while new agents should not be forced to load the entire history at once.

**Implemented in:**

- Protocol Core P9, P10
- `protocol/PERSISTENT_MEMORY.md`
- Specification §14
- active-state / historical-state separation

**Status:** FULLY INTEGRATED.

---

## F16 — New AI agents should be able to take over without original chat history

**Founding idea:** the collaboration model should be platform/agent independent at the project-state level; a replacement agent should reconstruct the current project from GitHub.

**Implemented in:**

- Protocol Core P1, P9
- Persistent-memory handoff target
- Specification §15
- project `AGENTS.md` template

**Status:** FULLY INTEGRATED.

---

## F17 — The workflow should be a reusable template for future research projects

**Founding idea:** a future project can point a new AI agent to HARC and ask it to create topic-appropriate directories/files while preserving the collaboration logic.

**Implemented in:**

- Protocol Core P11
- `templates/research-project/`
- bootstrap README
- form-profile templates

**Status:** FULLY INTEGRATED.

---

## F18 — Initial scope should be GitHub-centered, with other platforms deferred

**Founding idea:** local/other systems may be considered later, but the present protocol should focus on GitHub + human + AI agent(s).

**Implemented in:**

- Protocol Core P1 and scope section
- Specification §§1 and 19
- HARC-D002

**Status:** FULLY INTEGRATED.

---

## F19 — HARC should become an independent project, not depend on a specific research topic

**Founding idea:** separate the collaboration methodology from the objective-probability paper and make it independently reusable.

**Implemented in:**

- standalone HARC repository
- HARC-D001
- Protocol Core P11

**Status:** FULLY INTEGRATED.

---

## F20 — The independent project should contain both an explanatory paper and executable protocol/templates

**Founding idea:** HARC should explain the collaboration model like an article/open project while also being practically usable.

**Implemented in:**

- `paper/WHITEPAPER.md`
- `paper/WHITEPAPER.zh-CN.md`
- `protocol/SPECIFICATION.md`
- `templates/`
- architecture and contribution docs

**Status:** FULLY INTEGRATED.

---

# Pass 2 — Operational coverage

The second pass asked whether the above principles can actually be executed.

## Operational elements confirmed

- canonical Content Core template exists;
- canonical Form Core template exists;
- Decision Log template exists;
- Working Argument Map template exists;
- Framework Status template exists;
- immutable approved-framework convention exists;
- feedback routing rules exist;
- upstream-first propagation exists;
- persistent-memory promotion test exists;
- evidence-conflict procedure exists;
- `DERIVED-PROVISIONAL` and final-approval states exist;
- new-agent AGENTS contract exists;
- artifact-type form profiles now exist;
- reusable author form profile now exists.

## Gaps discovered and fixed during this audit

### Gap A — Form reuse was specified but not fully executable

Before this audit, HARC described reusable author preferences and artifact types, but provided only a generic project Form Core.

**Fix:** added `protocol/FORM_PROFILE_INHERITANCE.md` plus reusable author, book, academic-paper, and article profile templates.

### Gap B — Responsibility distinction existed but was not explicit enough in founder state

The white paper/framework document contained the general idea, but the founder core and decision log did not independently preserve the distinction between a framework-level intellectual defect and a local AI-expansion defect.

**Fix:** added Protocol Core P13, HARC-D011, and a dedicated section in `FRAMEWORK_APPROVAL.md`.

### Gap C — New projects did not explicitly pin their adopted HARC version

A future agent could otherwise read a newer upstream protocol and assume its rules had automatically become project decisions.

**Fix:** project `AGENTS.md` and bootstrap README now include protocol-source/version/commit fields. This is an implementation safeguard added by the AI audit; it is not claimed as an original founder idea.

---

# Pass 3 — New-agent handoff simulation

Assumption: the original conversation is unavailable. The new agent receives only this HARC repository and a target project/topic.

## Can the agent determine what to do?

**Yes.** It can reconstruct the intended workflow from:

1. HARC root `README.md` / `AGENTS.md`;
2. `protocol/SPECIFICATION.md`;
3. `protocol/PERSISTENT_MEMORY.md`;
4. `protocol/FORM_CONTENT_ROUTING.md`;
5. `protocol/FRAMEWORK_APPROVAL.md`;
6. `protocol/FORM_PROFILE_INHERITANCE.md`;
7. `templates/research-project/`;
8. `templates/form-profiles/`.

## Can the agent initialize a new project without inventing human views?

**Yes.** The templates explicitly require unknowns to remain unresolved and prohibit silently filling canonical human state with AI conjecture.

## Can the agent distinguish human content, human form, AI structure, and derived prose?

**Yes.** The canonical state model and routing system make these roles explicit.

## Can the agent know which framework the human actually approved?

**Yes, if the project follows the snapshot rule.** `FW-xxx` files and Framework Status preserve this distinction.

## Can the agent recover long history without loading everything at once?

**Yes in principle.** The persistent-memory protocol defines active state, historical state, indexes, archives, and selective retrieval.

## Can the agent determine which language is authoritative?

**Yes.** The Chinese-canonical / English-mirror rule is now explicit in Protocol Core, Specification, AGENTS, and the bilingual synchronization policy.

## Can the agent tell whether current prose is merely provisional?

**Yes.** Artifact states distinguish `DERIVED-PROVISIONAL`, `FINAL-REVIEW`, and `FINAL-APPROVED`.

---

# Later human-confirmed developments

This section does not retroactively present later design evolution as part of the original 2026-09-17 founding discussion. It records later protocol commitments explicitly proposed and confirmed by the human project founder.

## E01 — GitHub as authoritative external memory and working-state interface

**Later human decision:** do not maintain a second long-lived project-state copy inside chat. Treat GitHub directly as authoritative external memory + working state; model context retains only a Repository Resolver and task-relevant transient retrieval cache.

**Implemented in:**

- Protocol Core P21–P22
- HARC-D020
- `protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md`
- `HARC_CONTEXT_INTERFACE.yaml`
- project-template context interface
- methodology article C13 / T11

**Status:** IMPLEMENTED.

## E02 — Three-layer Long-Term Research Memory plus parallel Working Memory

**Later human decision:** retire the former “Layer 1.5” model. All three content layers are Long-Term Research Memory:

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

Maintain Working Memory in parallel for current stage, objective, active tasks, completion state, next actions, TODOs, blockers, pending human decisions, Clarifications, synchronization defects, and handoff.

Clarification is a Working Memory item. Stable human-resolved content must be promoted into the appropriate Long-Term Memory destination; after leaving active state, Working Memory retains only status, Decision ID, and destination pointers.

**Implemented in:**

- Protocol Core P19, P23
- HARC-D021
- `protocol/WORKING_MEMORY.zh-CN.md`
- `docs/working-memory.zh-CN.md`
- Manifest / Context Interface / Onboarding / AGENTS
- project templates
- methodology article C11, C14 / T9, T12 / draft

**Status:** IMPLEMENTED.

---

## E03 — Modular Working Memory: Current Focus / Task Plan / Work Log

**Later human decision:** Working Memory is a functional area rather than one mandatory document. A project may use one or multiple files according to engineering needs, AI capability, and workflow convenience, but should provide at least three logical roles:

- Current Focus — the highest-priority immediate objective;
- Task Plan — dynamic tasks, plans, TODOs, blockers, pending decisions / Clarifications;
- Work Log — broad progress, milestones, and changes in intellectual/work direction primarily for later human review.

Completed tasks leave active Task Plan and receive appropriately granular summaries in Work Log; stable normative results still require Promotion into Long-Term Memory.

Work Log should be maintained periodically but is outside default AI onboarding context. It does not store hidden AI chain-of-thought or scratchpads.

**Implemented in:**

- Protocol Core P24
- HARC-D022
- `protocol/WORKING_MEMORY.zh-CN.md`
- `docs/working-memory.zh-CN.md` (Index)
- `docs/working-memory/current-focus.zh-CN.md`
- `docs/working-memory/task-plan.zh-CN.md`
- `docs/working-memory/work-log.zh-CN.md`
- Manifest / Context Interface / Onboarding / AGENTS
- project templates
- methodology article C15 / T13 / draft

**Status:** IMPLEMENTED.

---

## E04 — Current full-discussion coverage review

**Review date:** 2026-09-18  
**Scope:** one additional `review -> repair -> verify` pass over the HARC design commitments recoverable from the current human–AI discussion and repository state.

### Coverage result

The following discussed requirements all have a normative commitment, executable mechanism, and discoverable entry point:

- GitHub as durable shared research memory and authoritative working state;
- replaceable AI Agents with project continuity independent of one chat/model;
- CONTENT / FORM / PROTOCOL routing and upstream-first propagation;
- Layer 1 Human Authorial Core;
- Layer 2 Current Framework;
- Layer 3 Derived Artifact;
- three-layer Long-Term Research Memory separated from parallel Working Memory;
- Working Memory as a functional area implementable in one or multiple files;
- Current Focus / Task Plan / Work Log logical roles;
- Work Log primarily for human retrospective review, maintained periodically and outside default AI onboarding;
- high-impact uncertainty routed into Task Plan / Clarification;
- Promotion into appropriate Long-Term Memory after human resolution;
- zero-context START_HERE / Bootstrap Prompt / Onboarding Handshake;
- Repository-Backed Context with only a Resolver and transient cache in model context;
- Chinese canonical / English synchronized mirror;
- pre-cutover English-ahead content absorbed into Chinese before canonical cutover;
- distinct Framework Approval and Final Artifact Approval gates;
- framework-level vs derived-expansion defects;
- Approved Framework projection into reader-facing overview;
- evidence as a horizontal constraint that does not silently rewrite human intention;
- author / artifact-type / project form-profile inheritance;
- HARC as both an executable protocol and a methodology article governed by HARC itself;
- human cognitive/epistemic responsibility and the boundary between delegable cognitive labor and non-silent delegation of responsibility;
- three review-repair-verify cycles plus an independent post-repair audit;
- HARC self-hosting, zero-context takeover, and template inheritance.

### Residual defects found and repaired in this pass

1. root `START_HERE` English mirror still treated the legacy Clarification Register as active;
2. root `AGENTS.md` retained legacy Clarification Register logic, an older methodology-article read order, and incomplete Repository-Backed Context details;
3. project-template `START_HERE` had numbering regression and legacy Clarification Register routing;
4. project-template `AGENTS` still used legacy clarification-register as an active read/write target;
5. English Onboarding Handshake did not fully mirror the Current Focus / Task Plan model;
6. Persistent Memory and Bootstrap Prompt retained a few older monolithic Working Memory / Clarification formulations;
7. this audit's own bilingual-migration status statement was stale.

All were repaired and bilingual mirrors synchronized in this review.

### Scope boundary

This confirms that **all explicitly discussed HARC design requirements recoverable from the current conversation/repository context are represented as implemented mechanisms or explicit human-decision boundaries.**

It cannot prove coverage of deleted, inaccessible, or never-persisted historical conversations.

**Status:** `PASS AFTER REPAIR`.

---

---

# Remaining unresolved item

## Open-source licensing

The founder explicitly intends HARC to be an open project. The repository is public and contains contribution infrastructure, but a public GitHub repository is not automatically an open-source/open-content license grant.

The exact license has not yet been human-confirmed.

`LICENSE-DECISION.md` currently records candidate licensing approaches.

**Status:** HUMAN DECISION STILL REQUIRED.

This is the only material founding intention identified in this audit that is not yet fully completed at the legal/licensing layer. The protocol content and reusable implementation are present; formal open licensing remains unresolved until the founder selects the license terms.

---

# Audit conclusion

After the three-pass review and the fixes made during it:

- all substantive collaboration concepts identified from the founding discussions are represented in the HARC architecture;
- previously partial operationalization of form-profile reuse has been completed;
- framework-vs-expansion responsibility has been made explicit in founder-level state;
- new-agent handoff has been strengthened with protocol-version pinning;
- no specific objective-probability research content is required by HARC;
- open-source licensing remains an unresolved founder-level implementation decision; the initial repository-wide bilingual migration/parity audit is complete, while bilingual synchronization remains mandatory for every future substantive edit.

Future audits should compare new founder decisions against this document and update the Protocol Core/Decision Log first when a genuine new design commitment appears.
