# AHICP Working Memory — Work Log

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

## 2026-09-18 — HARC-D024 — Title approval and clarification of humans as the bearers of responsibility

**Related:** HARC-D024; further clarification of HARC-D023.

**Human decision summary:**

- the Chinese title “从对话到持久研究状态：AI时代的人机研究协作、人类责任与可审计作者性” is explicitly approved;
- title approval is a title/form-content decision only and does not constitute Framework Approval of the complete Working Framework;
- “human responsibility / 人类责任” is not treated as a self-explanatory independent central concept;
- the more precise core claim is that in human–AI collaborative research and inquiry, humans remain the bearers of responsibility;
- this responsibility-bearing requirement becomes especially important when research results, arguments, or knowledge claims enter public circulation;
- AI may share extensive work as a tool but cannot become the ultimate bearer of responsibility for research purpose, core judgment, framework authorization, or public dissemination of knowledge;
- all other HARC-D023 decisions remain in force.

**Propagation result:**

- added HARC-D024 to Decision Log;
- recorded the human-approved title in Article Form Core;
- added/strengthened the responsibility-bearing and public-knowledge-dissemination commitments in Article Content Core;
- synchronized title status, central problem, T3 / T4, core distinctions, and Section VI in the Working Argument Map;
- synchronized the methodology draft's abstract, Section 6, conclusion, and keywords;
- synchronized Protocol Core, Framework Approval, Specification, README, root/template Agent contracts, and research-project templates;
- removed the stale duplicate responsibility-model block from the tail of Framework Approval;
- updated Working Memory and Framework Status to distinguish title approval from still-pending overall Framework Approval.

**Current state:**

`PASS FOR HUMAN FRAMEWORK REVIEW` remains unchanged; `MA-FW-001` has not been created.

---

## 2026-09-18 — HARC-D025 — Framework dependency repair and unresolved-item approval semantics

**Related:** HARC-D025.

**Human confirmation:**

- repair the methodology Working Framework's T1–T13 dependency graph so later Working Memory, zero-context onboarding, repository-backed context, and related theses enter the correct governance/implementation relations;
- synchronize the T3 dependency label to “AI Tool Work / Humans as Bearers of Responsibility”;
- clarify that overall Framework Approval may include explicit unresolved / AI-PROPOSED / NON-BLOCKING items, but approves their architectural place, scope, and treatment as unresolved items rather than their still-unconfirmed substantive content;
- unresolved AI proposals are not automatically promoted into human commitments by overall Framework Approval;
- this confirmation is not overall Framework Approval and does not create `MA-FW-001`.

**Execution result:**

- repaired the bilingual Working Argument Map dependency graph;
- added unresolved-item approval semantics to the Framework Approval protocol;
- synchronized Framework Status, Current Focus, and Task Plan;
- the current gate remains `WAITING-HUMAN: overall Framework Approval decision`.

---

## Current log boundary

This log currently contains high-level historical summaries backfilled from Decision Log and canonical protocol files. Future entries should be appended at meaningful milestones rather than reproducing conversations verbatim.

---

## 2026-09-18 — Repository-wide collaboration architecture audit: from rule completeness to complexity governance

**Role:** AI-maintained audit on the PROTOCOL route; does not create a new Human Protocol Decision.

**Scope reviewed:**

- root zero-context entry points;
- Manifest / Context Interface control plane;
- AGENTS / README / Onboarding Handshake;
- Working Memory;
- methodology-article governance entry points;
- bilingual synchronization;
- historical audits/self-tests;
- reusable research-project template;
- open-release readiness.

**Synchronization defects repaired directly:**

- README duplicated a second onboarding read order that could drift; it now points to START_HERE / Manifest authoritative routing instead;
- README copied stale live Clarification Gate state; it now points to Framework Status / Current Focus / Task Plan for live state;
- ONBOARDING_SELF_TEST displayed old blockers from test time and could be mistaken for live state; it is now explicitly marked as a historical snapshot / live state superseded, with future tests expected to record tested revisions.

**AI-PROPOSED architecture upgrades still awaiting human decision:**

Recorded in Task Plan as `WM-PROP-001..008`, including:

- lightweight onboarding;
- Manifest / Context Interface separation and compatibility versioning;
- strict static-navigation / live-state separation;
- scalable Decision Log indexing;
- bilingual synchronization automation;
- formal open-release infrastructure;
- machine-verifiable conformance;
- template de-duplication.

**Overall judgment:**

HARC's main problem is no longer missing governance rules. The next risk comes from rapid growth in governance assets: entry-point complexity, copied state, manual synchronization cost, and stale-state regressions. The next phase should prioritize complexity governance rather than adding more parallel explanatory files.

**Normative status:**

These architecture upgrades remain `AI-PROPOSED`. Other than synchronization repairs, no new architecture proposal was promoted into Protocol Core / Decision Log.


---

## 2026-09-19 — AHICP v0.3 semantic migration: control plane, templates, and structural validation

Completed in this work cycle:
- migrated Protocol Core, live protocol files, Architecture, Roadmap, and Working Memory under `AHICP-D026`;
- established `AHICP_MANIFEST.yaml` / `AHICP_CONTEXT_INTERFACE.yaml`, with legacy `HARC_*` files reduced to compatibility pointers;
- migrated `templates/research-project/` to the AHICP control plane while retaining it as a research specialization;
- added the Phase C semantic audit and v0.3 migration validation record;
- manifest path check: 33 candidates, 0 missing;
- bilingual physical pairing check: 62 Chinese files, 0 missing English mirrors;
- zero-context entry-chain check passed with no live legacy control-file references.

Remaining:
- distinguish historical HARC references from current AHICP references in the methodology article/evidence layer;
- semantic bilingual parity on key normative files;
- independent post-migration repair audit.

Separately, PPF now has its first Quarto + GitHub Actions + Cloudflare Workers Static Assets reference-implementation PR. PPF publishing-lifecycle rules were not duplicated into AHICP.

---

## 2026-09-19 — External systems / human handoff normative migration

Under AHICP-D027, this work cycle promotes lessons from real external-provider collaboration into provider-neutral protocol rules:

- add machine-operable-first escalation;
- require real minimal invocation to verify installed/enabled/connected capability rather than trusting directory state alone;
- prefer official/OAuth/provider-managed/least-secret-handling paths;
- keep secrets out of chat;
- reserve human handoff for identity authorization, account consent, permission grants, non-delegable high-impact decisions, or genuine tool-capability absence;
- require minimal nontechnical handoff and Agent resumption after authorization;
- verify provider actual state after external operations and write durable results affecting future work back to the repository;
- keep AHICP provider-neutral without copying PPF provider lifecycle or Cloudflare-specific details.

Chinese canonical and English mirror, root AGENTS, and the research-project template were synchronized in the same work cycle.

---

## 2026-09-20 — Scoped authorization governance consolidation and post-merge repair

**Related:** AHICP-D027, AHICP-D028, AHICP-D029; PR #3.

**Stage progress:**

- D027 established provider-neutral machine-operable-first execution, tool discovery, authorization / human handoff, provider actual-state verification, and repository write-back governance;
- D028 established that initial configuration of a reusable authorization policy begins with AI-proposed authorization patterns and human selection/modification/rejection, with the final choice recorded together with scope, authorization provenance, and escalation conditions in repository durable state;
- D029 approved the overall scoped-authorization direction and authorized PR #3 to merge after green CI on the latest head;
- PR #3 completed normative consolidation. An independent post-merge review found no architectural issue requiring rollback, but identified several propagation and operational-state gaps.

**Repair in this work cycle:**

- restored the complete D028 durable authorization record across the Specification, Protocol Core, root AGENTS, and research-project template so a stored policy cannot omit its scope / escalation boundary;
- restored `permission grants` to the Specification §23.3 Human handoff enumeration, aligning it with §23.2, P25, AGENTS, and D027;
- refreshed Current Focus / Task Plan so D027–D029, PR #3, and the post-merge review are recoverable operational history;
- corrected the live Work Log title from HARC to AHICP while preserving historical HARC-D001–HARC-D025 identifiers;
- strengthened Protocol Contract CI from file-wide marker presence to a section-local authorization-record invariant for §23.5.1.

**Boundary:**

- no change to the PPF publishing lifecycle;
- no Vault modification;
- no textbook change;
- no downstream adoption bump;
- this work is propagation and consistency repair of already approved D028/D029 semantics, not a new Human Protocol Decision.

## 2026-09-20 — Methodology article Project Memory Architecture structural upgrade

**Authority:** AHICP-D030

This work cycle keeps the existing methodology article as one unified paper and completes the following structural upgrade:

- promotes Project Memory Architecture to the central article axis;
- defines Working Memory as a persistent continuity layer;
- treats Human Decision Persistence as first-class Project memory;
- treats Agent / Model Substitution as an architectural stress test and proposed evaluation;
- distinguishes Agent/conversational memory from Project memory;
- adds memory curation, stale/conflict handling, selective retrieval, and privacy/publication boundaries;
- connects Framework Approval / Final Artifact Approval to Project memory and human responsibility;
- adds related work/evidence on Generative Agents, MemGPT, Agent-memory surveys, LongMemEval, MemBench, RealMem, and W3C PROV;
- rewrites the Chinese canonical article and synchronized English mirror;
- updates Content Core, Working Argument Map, Framework Status, and Working Memory;
- retains `DERIVED-PROVISIONAL` / `WORKING-FRAMEWORK` status and does not create `MA-FW-001`;
- explicitly reports no empirical results for the proposed evaluation framework.

**Result:** structural rewrite completed; proceeding to consistency validation / PR / human review.

## 2026-09-21 — Second scholarly novelty / prior-art audit of the methodology article

**Object:** project-memory-centered methodology article  
**Authority:** AHICP-D030; this review does not create overall Framework Approval.

The second review focused on whether the paper mistakenly presented prior concepts as AHICP inventions. Newly added and verified lineage includes:

- Walsh & Ungson (1991) — Organizational Memory;
- Weiser & Morrison (1998) — *Project Memory: Information Management for Project Teams*;
- Mariano & Awazu (2024) — project memory in large-scale projects;
- Lee (1992) — design rationale management;
- Weinreich & Groher (2016) — Software Architecture Knowledge Management;
- Singh, Cobbe & Norval (2019) — Decision Provenance.

Primary repairs:

- explicitly states that AHICP **does not originate** organizational memory / project memory / design rationale / decision provenance / Agent long-term memory;
- narrows novelty to a **candidate architectural synthesis**:
  a governed, model-substitutable Project Memory Architecture;
- adds an explicit design research question and novelty boundary to the abstract/introduction/related work;
- upgrades the two-way Agent-memory comparison to a three-way comparison of prior project memory / Agent memory / AHICP governed Project Memory;
- updates T1, T11, and the related-work boundary in the Working Argument Map;
- expands the evidence layer and BibTeX and removes a stray Markdown separator from the BibTeX file;
- strengthens Methodology Article CI against unsupported “first / unique / AHICP originated project memory” claims.

**Status:** scholarly-positioning repair completed; latest CI pending at the time of this log entry.

---

## 2026-09-21 — MA-FW-001 Framework Approval completed

**Authority:** AHICP-D031

This work cycle completed the scholarly review of T1–T13 and created the first Approved Framework using bounded, evidence-constrained wording:

- `paper/frameworks/MA-FW-001.zh-CN.md`
- `paper/frameworks/MA-FW-001.md`

Key review outcomes:

- T1 / T11 preserve prior-art and novelty boundaries;
- T9 is explicitly scoped to AHICP normative governance;
- T10 formally becomes **Framework Approval as a Structured Human-Review Gate and Responsibility Anchor**;
- T12 remains a proposed empirical research agenda;
- all approved architecture principles remain distinct from empirical effectiveness claims;
- the article status is now `DERIVED-FROM-MA-FW-001 — FINAL ARTIFACT APPROVAL PENDING`.

`MA-FW-001` is the fixed approval baseline. Later substantive framework changes should create a new snapshot rather than rewrite it.

**Governance boundary:** this Framework Approval is not Final Artifact Approval and does not automatically authorize PR merge, publication, or release.

**Result:** Framework work complete; the next phase is Final Artifact Review / target-venue preparation.

---

## 2026-09-21 — AHICP-D032: bounded Framework auto-merge + primary target venue

The human project founder explicitly approved two governance/publication decisions:

1. Framework Approval also constitutes **bounded auto-merge authorization** for a dedicated PR when strict scope / latest-head CI / blocking-review / base-sync / provider-protection conditions hold;
2. `Ethics and Information Technology` is selected as the current methodology article primary target venue, with `Science and Engineering Ethics` retained as the secondary candidate.

Protocol propagation completed in this work cycle:

- AHICP-D032 recorded in the Decision Log;
- bounded auto-merge principle added to Protocol Core P6;
- Framework Approval protocol gains §3.5;
- corresponding rule added to the Specification Framework Approval Gate;
- repository AGENTS contract and research-project template AGENTS synchronized;
- Working Memory marks WM-T027 complete and WM-T014 venue-selected;
- Target Venue Review moves from AI recommendation to HUMAN-SELECTED;
- Framework Status advances to Ethics and Information Technology preparation;
- Methodology / Protocol CI gains D032 regression guards.

**Governance boundary:** bounded merge authorization is not Final Artifact Approval and does not authorize submission / publication / release / deployment / secret handling.

**PR #26:** D032 explicitly includes the current methodology PR within scoped merge authorization; actual auto-merge still depends on final latest-head condition verification.

---

## 2026-09-21 — PR #26 bounded auto-merge execution and verification

Under `AHICP-D032`, PR #26 passed the following pre-merge checks:

- dedicated methodology / Framework scope;
- Framework work and subsequent D032 direct governance/venue synchronization were human-authorized;
- latest-head Methodology Article CI: PASS;
- latest-head Protocol Contract CI: PASS;
- latest-head Ecosystem validation: PASS;
- unresolved review threads: 0;
- branch vs `main`: behind = 0;
- GitHub reported `mergeable=true`;
- merge executed through the standard GitHub merge API without bypassing provider-side protection.

Execution result:

- PR: #26 `Reframe AHICP methodology article around project memory architecture`
- result: `merged=true`
- merge commit: `af3e7927a5bc1a275fdcd9eb5fa47b2b0902a210`
- post-merge verification: `main` confirmed to contain AHICP-D032, `MA-FW-001`, and the `Ethics and Information Technology` target-venue state.

**Conclusion:** the D032 bounded auto-merge authorization has completed its first actual execution; the methodology Framework work is now in `main`.

---

## 2026-09-21 — Ethics and Information Technology submission derivative preparation

**Authority:** AHICP-D033

This work cycle prepared the first venue-specific submission package:

- `paper/submission/ethics-information-technology/MANUSCRIPT_BLINDED.md`;
- bilingual submission checklist;
- bilingual AI / LLM use disclosure;
- title / submission metadata template;
- cover-letter draft;
- dedicated EIT submission validator / CI.

Current machine-checked blinded-manuscript metrics:

- abstract: 185 words;
- content: approximately 5,367 words;
- keywords: 6;
- displayed heading levels: maximum 3;
- internal Decision / Framework / Working-Memory IDs: none detected;
- direct GitHub URL: none detected;
- substantive AI-use disclosure: present;
- Data Availability Statement: present;
- empirical effectiveness result: not claimed.

Venue-level reference cleanup:

- canonical evidence infrastructure remains unchanged;
- the submission derivative removes uncited CRediT / UNESCO / Nature Methods entries;
- because MemGPT remains an arXiv/CoRR preprint while the EIT guideline says the reference list should contain works cited in the text that are published or accepted, the blinded derivative removes the MemGPT example/reference; the related-work argument remains supported by Generative Agents, the Agent-memory survey, LongMemEval, MemBench, RealMem, and other published work.

Open blockers:

- the distinctive `AHICP` name may enable search-based deanonymization through public project materials;
- final Word/docx has not yet been generated;
- citation / DOI / publication-status item-by-item final review remains pending;
- Final Artifact Approval remains pending;
- submission authorization has not occurred.

**Status:** submission derivative prepared; CI / PR validation next.

---

## 2026-09-21 — EIT citation audit and DOCX build pipeline

**Authority:** AHICP-D033

After PR #29 merged, this work cycle continued venue-specific Final Artifact review:

- PR #29 merged into `main`, merge commit:
  `a789bbd3342b29ebb07caa9c0cd22da3315e7746`;
- completed publication-status / metadata / DOI / standards audit for the blinded manuscript's current reference set;
- added `CITATION_AUDIT.md`;
- separated ICMJE / Nature Portfolio as dynamic policy sources requiring recheck immediately before actual submission;
- normalized W3C PROV-DM as the 30 April 2013 W3C Recommendation;
- normalized LongMemEval to the ICLR 2025 proceedings record;
- added `tools/build_eit_docx.py` for reproducible blinded Markdown -> Word/docx generation;
- EIT Submission CI now generates and uploads a `MANUSCRIPT_BLINDED.docx` build candidate and checks its ZIP/package structure;
- a successful CI build does not make the DOCX a Final Artifact: page-by-page visual QA remains an explicit unresolved gate.

Current remaining blockers:

1. final bidirectional citation ↔ reference-list consistency check;
2. search-based deanonymization risk from the distinctive `AHICP` name;
3. page-by-page visual QA of the CI-generated Word/docx;
4. license;
5. Final Artifact Approval;
6. formal submission authorization;
7. final live-policy recheck immediately before submission.

**Status:** citation audit completed; reproducible DOCX build ready; visual QA pending.

---

## 2026-09-21 — PR #30 EIT final-review merge and DOCX build verification

Under AHICP-D033, PR #30 passed the following pre-merge checks:

- branch vs `main`: behind = 0;
- unresolved review threads: 0;
- Ecosystem validation: PASS;
- Methodology Article CI: PASS;
- EIT Submission CI: PASS;
- EIT validator: PASS;
- DOCX build: PASS;
- DOCX ZIP/package structural validation: PASS;
- workflow artifact upload: PASS.

Execution result:

- PR #30: `Audit EIT references and add reproducible DOCX build`
- merge result: `merged=true`
- merge commit: `b2e450baf5001f4879f740e67e21264aef115d5a`
- generated artifact: `eit-manuscript-blinded-docx`
- artifact size: approximately 53 KB
- retention: 30 days

**Boundary:** generating and structurally validating a build candidate is not page-by-page visual QA and is not Final Artifact Approval. Remaining work includes bidirectional citation ↔ reference-list final consistency review, the `AHICP` search-based deanonymization risk, Word visual QA, license, Final Artifact Approval, and separate submission authorization.

**Status:** PR #30 merged; DOCX build candidate structurally verified; visual QA pending.

---

## 2026-09-21 — EIT masked reviewer derivative and bidirectional citation-reference validation

**Authority:** AHICP-D033  
**Nature:** venue-specific Final Artifact preparation; no new Framework decision.

This work cycle identified and mitigated a double-anonymous-review risk. Although the baseline blinded manuscript already removed author names, affiliations, GitHub URLs, and internal project IDs, it still contained many occurrences of `AHICP` / the full protocol name. Because the protocol has public project materials, the distinctive name may allow ordinary search-based identification of the author/repository.

Execution:

- retain `MANUSCRIPT_BLINDED.md` as the traceable blinded baseline;
- add `MANUSCRIPT_BLINDED_MASKED.md` as a reviewer-facing masked derivative;
- preserve the same title / argument structure / citations / references / AI-use disclosure / Data Availability in the masked derivative;
- replace only the protocol proper name with neutral formulations such as `the proposed protocol`, `the protocol`, and `the proposed Project Memory Architecture`;
- masked-manuscript machine checks:
  - `AHICP`: 0;
  - full protocol name: 0;
  - direct GitHub URL: 0;
  - internal Decision / Framework / Working-Memory IDs: 0;
- add bilingual `BLINDING_REVIEW` records, explicitly refusing to claim perfect anonymity; human/editorial confirmation of the reviewer-manuscript route remains pending;
- extend EIT validation to both traceable and masked manuscripts;
- define an explicit 18-entry citation ↔ reference-list mapping so every current reference entry must have a corresponding in-text citation;
- require the masked and unmasked reference sections to be identical;
- extend EIT CI to build both traceable and masked DOCX candidates and independently validate/upload them.

**Governance boundary:**

- no change to `MA-FW-001`;
- no change to the canonical bilingual article;
- the masked derivative is a review-anonymization derivative, not a permanent renaming of the scholarly object;
- Final Artifact Approval has not occurred;
- submission authorization has not occurred;
- visual QA remains separate from CI structural validation.

**Current status:** masked mitigation prepared; latest-head CI verification pending.

---

## 2026-09-21 — EIT masked/citation CI verification passed

On an intermediate head of PR #32, EIT Submission CI completed and passed:

- traceable blinded manuscript validation: PASS;
- masked blinded manuscript validation: PASS;
- masked prohibition checks for `AHICP` / full protocol name / direct GitHub URL / internal IDs: PASS;
- explicit 18-entry citation ↔ reference-list mapping: PASS;
- masked / unmasked reference-section equality: PASS;
- traceable DOCX build: PASS;
- masked DOCX build: PASS;
- both DOCX ZIP/package structural validations: PASS;
- traceable artifact upload: PASS;
- masked artifact upload: PASS.

Generated workflow artifacts:

- `eit-manuscript-blinded-docx` — 53,268 bytes;
- `eit-manuscript-blinded-masked-docx` — 53,256 bytes.

**Boundary:**

- CI structural validation does not replace page-by-page visual QA;
- the masked reviewer route still requires human/editorial confirmation;
- residual discoverability must not be described as “perfect anonymity”;
- Final Artifact Approval / submission authorization has not occurred.

**Status:** citation consistency verified; masked mitigation technically validated; final-head revalidation pending after state write-back.
