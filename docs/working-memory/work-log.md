# HARC Working Memory — Work Log

> **Language:** Chinese canonical: `work-log.zh-CN.md`; this English file is the synchronized mirror.
>
> **Primary reader: the human author.**
>
> This log supports retrospective review of project development, stage-level progress, and changes in intellectual/work direction. It is not default required reading for AI onboarding and is not the authority for durable substantive claims.

## Usage rules

- record high-level project changes, expressed reasons, milestones, and completed task batches;
- do not record hidden model chain-of-thought, scratchpads, or unverifiable internal reasoning;
- AI may update it periodically after milestones, phase transitions, completed task batches, and major human decisions;
- replacement Agents do not need to read the full log during normal takeover;
- retrieve it on demand for human historical review, audit, or change reconstruction.

---

## 2026-09-17 — HARC becomes an independent project

**Stage:** protocol founding.

**Progress summary:**

- separated HARC from a specific research project;
- established GitHub as the persistent collaboration substrate;
- established upstream/downstream relations among human authorial foundations, AI-maintained operational framework, and derived artifacts;
- established CONTENT / FORM / PROTOCOL routing;
- established separate Framework Approval and Final Artifact Approval gates.

**Direction change:** from a collaboration practice inside one study to a reusable human–AI research collaboration protocol.

---

## 2026-09-18 — Bilingual canonical governance established

**Progress summary:**

- Chinese became canonical;
- English became a synchronized mirror;
- newer historical English content was first backfilled into Chinese before canonical cutover;
- subsequent substantive development follows `Human decision -> Chinese canonical -> English mirror`.

**Direction change:** from bilingual coexistence to one explicit semantic authority plus synchronized translation.

---

## 2026-09-18 — From chat-state duplication to Repository-Backed Context

**Related:** HARC-D018–D020.

**Progress summary:**

- established zero-context onboarding;
- initially used an Active Session Contract as a second session-level safeguard;
- then narrowed it into a Repository Resolver;
- formally defined GitHub as authoritative external memory + working state;
- model context became transient retrieval cache + control plane.

**Direction change:** from “repository + duplicated session state” to “repository as sole authority with on-demand retrieval”.

---

## 2026-09-18 — From Layer 1.5 to parallel Working Memory

**Related:** HARC-D021.

**Progress summary:**

- retired Critical Clarification as an independent Layer 1.5;
- clarified the three content layers as Long-Term Research Memory:
  `Layer 1 -> Layer 2 -> Layer 3`;
- introduced Working Memory in parallel;
- made Clarification a Working Memory item;
- stable human resolutions are promoted into appropriate Long-Term Memory;
- Working Memory became the resume index across Agents and human collaborators.

**Direction change:** semantic hierarchy and current work state were separated.

---

## 2026-09-18 — Working Memory becomes a functional area

**Related:** HARC-D022.

**Progress summary:**

Working Memory was further separated into three logical functions:

1. Current Focus — the highest-priority immediate objective;
2. Task Plan — the dynamic task/plan state;
3. Work Log — a human-oriented historical chronicle.

The former `docs/working-memory.zh-CN.md` becomes an Index / Resolver.

**Direction change:**

from:

`one Working Memory document`

to:

`Working Memory Area = Index + Current Focus + Task Plan + Work Log`

Work Log is excluded from default AI context and retrieved only for historical review or audit.

**Implementation completed:**

- Protocol Core / Decision Log / Working Memory Protocol synchronized;
- Manifest / Context Interface map all four logical roles;
- START_HERE / AGENTS / Bootstrap / Session Resolver / Onboarding synchronized;
- project templates use the same split;
- methodology article includes C15 / T13 and synchronized draft changes;
- Framework Gate / Clarification workflow now read Task Plan;
- bilingual regression: `120 Markdown = 60 Chinese canonical + 60 English mirrors; missing pairs = 0`.

---

## 2026-09-18 — Current full-discussion coverage review

**Type:** one complete `review -> repair -> verify` pass.

**Coverage result:**

- the three Long-Term Research Memory layers, parallel Working Memory, and Current Focus / Task Plan / Work Log are implemented;
- Clarification / Promotion, Repository-Backed Context, zero-context onboarding, bilingual canonical/mirror governance, Framework/Final Approval, form inheritance, and methodology-article self-hosting all have normative and executable entry points;
- no new core architectural omission was found.

**Repairs made in this pass:**

- stale Clarification Register and read-order logic in root START_HERE / AGENTS English mirrors;
- numbering regression and legacy Clarification routing in project-template START_HERE;
- active-state use of legacy clarification-register in project-template AGENTS;
- English Onboarding Handshake;
- a few older formulations in Bootstrap Prompt / Persistent Memory;
- stale bilingual-migration status in Founding Idea Audit itself;
- the target-venue / venue-specific form constraint already known to the final audit but not separately represented in Task Plan, now added as `CLR-010`.

**Conclusion:** `PASS AFTER REPAIR`.

**Still requiring human decision:** methodology article `CLR-001 / CLR-002 / CLR-005`; `CLR-009` licensing before formal release.

---

---

## 2026-09-18 — HARC-D023 — Human purpose, AI tool role, and Framework responsibility model

**Related:** HARC-D023; CLR-001 / CLR-002 / CLR-005.

**Human decision summary:**

- the purpose, central problem, and direction of a research or creative project originate with humans and remain under human initiation, navigation, and approval; humans bear core responsibility for the resulting work;
- within HARC, an AI Agent is a collaboration tool that may perform or assist extensive concrete work, but it should not be characterized as a cognitive subject and “AI performs cognitive labor / cognitive tasks” is not used as the normative central concept;
- for long-form work, the Layer 2 Current / Approved Framework is the primary structural carrier of human core intellectual responsibility;
- Framework Approval requires the human to clearly understand, carefully review item by item, and explicitly confirm every substantive element actually represented in the framework, including core theses, inferential relations, key distinctions, scope conditions, section/chapter functions, and any specific wording included in the framework;
- `responsibility concentration` is no longer retained as the current central term;
- treating an Approved Framework as a possible scholarly human–AI collaboration attachment remains only a possible future direction, not a current mandatory HARC rule.

**Promotion / propagation in this work cycle:**

- added `HARC-D023` to Decision Log;
- synchronized Protocol Core / Framework Approval / Specification / root Agent Contract / README / research-project templates in Chinese and English;
- promoted the decision into the Article Content Core at Layer 1;
- updated T3 / T4, core distinctions, dependencies, and Clarification state in the Working Argument Map at Layer 2;
- selectively synchronized the methodology draft's abstract, Section 6, and conclusion at Layer 3; the full article remains `DERIVED-PROVISIONAL` and no major structural rewrite was performed early;
- moved `CLR-001 / CLR-002 / CLR-005` out of active blocking state in Task Plan while preserving `RESOLVED / PROMOTED` pointers.

**Framework readiness review:**

`PASS FOR HUMAN FRAMEWORK REVIEW`

The previous blocking Clarification gate is cleared. There is no active blocking Clarification preventing overall Framework Approval review.

**Not yet done:**

- `MA-FW-001` has not been created;
- overall Framework Approval has not occurred;
- the full 15-part -> 10-part structural rewrite has not been performed.

**Next stage:**

The human reviews `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md` as a whole and explicitly decides `APPROVE / REVISE / REJECT`.

---

## Current log boundary

This log currently contains high-level historical summaries backfilled from Decision Log and canonical protocol files. Future entries should be appended at meaningful milestones rather than reproducing conversations verbatim.
