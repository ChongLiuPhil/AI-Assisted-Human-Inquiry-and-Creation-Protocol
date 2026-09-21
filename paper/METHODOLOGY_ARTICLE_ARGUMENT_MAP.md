# Methodology Article — Working Argument Map

**Status:** `CURRENT-FRAMEWORK — ALIGNED WITH APPROVED MA-FW-001`  
**Title:** *From Conversation to Persistent Research State: Human–AI Research Collaboration, Human Responsibility, and Auditable Authorship in the AI Era*  
**Canonical upstream:** `METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`  
**Authorization:** `AHICP-D030` + `AHICP-D031`  
**Note:** This current map is aligned with the approved snapshot `paper/frameworks/MA-FW-001.md`. `MA-FW-001` is the fixed approval baseline; later substantive framework revision should create a new snapshot rather than rewrite the approved one.

---

## 1. Central problem

Generative AI can participate at scale in retrieval, organization, comparison, drafting, restructuring, verification, formatting, and execution. Yet long-running projects face a problem that is not automatically solved by longer context windows:

> **How can a project lasting months or years preserve its purpose, evidence, judgments, decisions, active state, and publication boundaries without depending on one conversation, one model, or one platform memory system?**

The paper reframes the problem from “how can AI remember more?” to “how can a project possess durable memory of its own?”

Core engineering thesis:

> **The durable memory of a long-running human–AI project should belong to the project, not to a particular model.**

“Belong to the project” means that important state is externalized into authoritative state that humans can inspect, edit, version, trace, and migrate rather than existing only in model context, platform-private memory, or opaque internal mechanisms.

---

## 2. Main theoretical contributions

### T1 — Governed Project Memory Thesis
**Source: HUMAN-CONFIRMED D030 + LITERATURE-CONSTRAINED**

Long-running human–AI collaboration requires **governed Project Memory** to be distinguished from conversational / Agent memory. However, project memory itself is not an AHICP invention: organizational-memory theory, Weiser & Morrison's (1998) Project Memory, later project-memory practice research such as Mariano & Awazu (2024), and design-rationale / architecture-knowledge-management traditions all form a clear prior lineage.

AHICP's candidate contribution should therefore be stated more narrowly: organizing project memory for replaceable LLM Agents as **authoritative, inspectable, versioned, human-governed project state**, integrated with Working Memory continuity, human decision status, authorization/publication boundaries, and approval gates.

### T2 — Model-Independent Memory Thesis
**Source: HUMAN-CONFIRMED — AHICP-D030**

Critical durable state should be as independent as practical from a particular model, vendor, chat, or platform-private memory. Model context is a transient projection for the current task, not the source of truth.

### T3 — Layered Project-Memory Architecture
**Source: HUMAN-CONFIRMED + EXISTING AHICP ARCHITECTURE**

AHICP uses three Long-Term Research Memory layers plus parallel Working Memory:

`Layer 1 Human Authorial Core -> Layer 2 Current/Approved Framework -> Layer 3 Derived Artifact`

Parallel:

`Working Memory = current stage / focus / tasks / blockers / clarifications / next actions / handoff`

Functionally it also distinguishes normative, epistemic/evidence, decision, working/operational, handoff, and publication/authorization memory. Functional roles need not map one-to-one to physical files.

### T4 — Working Memory as Continuity Layer
**Source: HUMAN-CONFIRMED — AHICP-D030**

AHICP Working Memory is not psychological working memory, model hidden state, or chain-of-thought. It is a persistent operational representation of the project's current epistemic/task state and a cross-session, cross-Agent continuity layer.

Current Focus + Task Plan are the default resume state; Work Log supports selective historical review.

### T5 — Human Decision Persistence
**Source: HUMAN-CONFIRMED — AHICP-D030**

Human decisions are first-class project memory. The system should distinguish at least PROPOSED, CONFIRMED / APPROVED, REJECTED, DEFERRED / OPEN, and AUTHORIZED-within-scope states.

Replacing an Agent should not turn rejected proposals back into unknowns or erase the provenance of confirmed decisions. Decisions may change, but later change requires new provenance, rationale, version, and authorization.

### T6 — Agent / Model Substitution Resilience
**Source: HUMAN-CONFIRMED — AHICP-D030**

Agents and models should be replaceable without destroying project continuity. After removing the current Agent, original chat, and platform-private memory, a replacement Agent should still recover project purpose, evidence, decisions, framework, active tasks, privacy/publication boundaries, and next actions.

This is both a design principle and an empirical stress test.

### T7 — Inspectable and Provenance-Aware State
**Source: HUMAN-CONFIRMED — AHICP-D030 + existing AHICP**

Memory that constrains future work should be inspectable, editable, versionable, and provenance-aware. Git commit history alone does not express semantic state, so Decision Logs, evidence/provenance, approval status, and upstream-first propagation remain necessary.

### T8 — Memory Dynamics and Curation
**Source: HUMAN-CONFIRMED — AHICP-D030**

Reliable project memory does not mean “save everything.” It must govern active vs archived, current vs stale, conflicting memory, selective retrieval, summaries/indexes, promotion/resolution/write-back, history growth, and privacy/disclosure boundaries.

Model context should retrieve the minimum authoritative state required by the task; after write-back, stale excerpts are invalidated.

### T9 — Human Authority and Responsibility as AHICP Normative Governance
**Source: HUMAN-CONFIRMED — HARC-D023/D024 + AHICP-D030**

Within AHICP governance, project purpose, core questions, direction, substantive judgment, key approvals, and final public-release responsibility remain on the human side, while AI may perform or assist extensive retrieval, organization, drafting, checking, and technical execution. Decision persistence makes that governance durable rather than merely conversational.

**Boundary:** this is an AHICP normative governance principle, constrained by actual research-integrity, publication, and domain rules; it is not presented as a universal philosophical law for every cognitive system, domain, or theory of authorship.

### T10 — Framework Approval as a Structured Human-Review Gate and Responsibility Anchor
**Source: HUMAN-CONFIRMED — HARC-D023/D024; SCHOLARLY REVIEW REWORDED 2026-09-21**

For long-form work, Layer 2 Framework is a structured human-review interface that exposes core claims, inferential relations, key distinctions, scope conditions, and structural commitments. Within AHICP, Framework Approval functions as an important responsibility anchor; Final Artifact Approval remains a separate gate for the concrete public version.

**Boundary:** no current empirical evidence establishes that Framework Approval reduces total review cost, and it does not substitute for Final Artifact Approval or factual review of the full artifact.

### T11 — Prior Project Memory, Agent Memory, and the AHICP Integration Boundary
**Source: HUMAN-CONFIRMED D030 + LITERATURE-CONSTRAINED**

Prior organizational/project-memory research already addresses project history, knowledge, context, rationale, and newcomer continuity; design-rationale / architecture-knowledge-management / decision-provenance research addresses decision reasons and origin; Generative Agents, MemGPT, agent-memory surveys, LongMemEval / MemBench, and RealMem bring long-term memory into LLM Agents and project-oriented interaction.

AHICP therefore should not compete over who first proposed project memory or who makes an Agent remember more. Its candidate contribution is the integration of these traditions into a governed Project Memory architecture: even with strong internal Agent memory, the project maintains independent authoritative state and unifies Working Memory, human decision status, authorization/publication boundaries, and cross-Agent substitution as governance mechanisms.

### T12 — Empirical Evaluation Framework
**Source: HUMAN-CONFIRMED AS RESEARCH AGENDA — AHICP-D030**

The paper proposes, without fabricating results: zero-context handoff/resumption, agent/model substitution, decision persistence, semantic drift/framework fidelity, review effort, stale/conflict handling, and memory curation/retrieval-efficiency tests.

### T13 — Provider Neutrality
**Source: EXISTING AHICP + D030**

GitHub is the current reference implementation, not a theoretical prerequisite. The architecture requires a versionable, queryable, writable, migratable, access-controlled authoritative project-state substrate.

---

## 3. Boundary with existing research

### 3.1 Organizational / Project Memory
Walsh & Ungson's organizational memory, Weiser & Morrison's Project Memory, and Mariano & Awazu's work on memory practices in large-scale projects establish that organization- and project-level memory, history, context, rationale, and continuity predate AHICP.

AHICP does not use Project Memory itself as a novelty claim. It focuses on the combination of **authoritative project state + human governance + Agent/model substitution** in AI-assisted inquiry.

### 3.2 Agent Memory
Existing research examines experience storage, retrieval, reflection, long/short-term memory management, multi-session recall, temporal reasoning, and knowledge updates. Its primary target is Agent memory capability.

AHICP does not require replacing internal Agent memory. It treats such memory as a potentially useful auxiliary layer while refusing to let it automatically become authoritative project state.

### 3.3 Design Rationale / Architecture Knowledge Management / Decision Provenance
Software-engineering and accountability literatures have long studied design decisions, rationale, knowledge capture/maintenance, and decision provenance. AHICP Human Decision Persistence must build on that lineage rather than claim to discover that decisions should be preserved.

AHICP adds project-governance semantics such as proposed / approved / rejected / deferred / authorized and propagates decision state through Working Memory -> Decision Log -> Long-Term Memory -> Artifact.

### 3.4 Provenance Standards
W3C PROV and related work provide general background for describing entities, activities, agents, and derivation. AHICP adopts the importance of traceability but does not claim to implement PROV or derive empirical validity from provenance standards.

### 3.5 Extended / Distributed Cognition
Clark & Chalmers and Hutchins provide theoretical background for external cognitive scaffolds and distributed cognition. The paper adopts a weak claim: a repository is a persistent cognitive/project-state scaffold; it need not treat AI or the repository as an independent cognitive subject.

### 3.6 Candidate Synthesis Contribution
The most defensible current novelty position is that AHICP organizes prior project memory, Agent memory, decision/rationale provenance, and human approval/authorization mechanisms into a **governed, model-substitutable Project Memory Architecture**.

That novelty still requires systematic literature review and peer review. The current framework must avoid unsupported priority claims such as “first” or “unique.”

---

## 4. Paper structure

### I. Introduction — From “can AI write?” to “how does a project remain continuous?”
Introduce generation–verification asymmetry as an analytical label and motivate project memory.

### II. Related work and boundary — prior Project Memory, Agent Memory, and Decision Provenance
Discuss organizational/project memory, design rationale / architecture knowledge management, decision provenance, Generative Agents, MemGPT, the agent-memory survey, LongMemEval, MemBench, RealMem, and provenance / distributed cognition.

### III. Design requirements for long-running project memory
Model independence, inspectability, versionability, provenance, decision persistence, resumability, selective retrieval, privacy boundaries, and human authority.

### IV. AHICP Project Memory Architecture
Three long-term layers + Working Memory + decision/evidence/form/authorization roles; repository-backed context.

### V. Working Memory as a cross-session continuity layer
Not psychological working memory / hidden state; Current Focus, Task Plan, Work Log, Clarification, Promotion.

### VI. Decision persistence and human authority
Proposed/confirmed/rejected/deferred/authorized states, Decision Log, authorization provenance, and durable human authority.

### VII. Agent / Model substitution — from principle to stress test
Zero-context onboarding, manifest, bootstrap, Onboarding Report, stale-cache invalidation, and handoff criterion.

### VIII. More memory is not always better — curation, conflict, staleness, privacy
Memory bloat, conflicting state, selective retrieval, archive, summary, privacy/publication boundaries.

### IX. Framework Approval, authorship responsibility, and public artifacts
Connect project memory to Framework Approval / Final Artifact Approval, framework vs derived defects, and reader-facing projection.

### X. Relationship to prior Project Memory, Agent Memory, and provenance research
Clarify the intersection and boundaries among the three traditions and constrain AHICP novelty to the candidate synthesis of a governed, model-substitutable Project Memory Architecture.

### XI. Evaluation framework and research agenda
Tasks, metrics, controls; no empirical results claimed.

### XII. Limitations and objections
Maintenance cost, rubber-stamp approval, error persistence, over-structuring, privacy, platform dependence, conflict resolution, domain variation.

### XIII. Conclusion
Core statement:

> **The durable memory of a long-running human–AI project should belong to the project, not to a particular model.**

---

## 5. Proposed evaluation framework

| Test | Intervention | Primary metrics |
|---|---|---|
| Zero-context handoff | Remove chat history; replacement Agent reads project entry only | state reconstruction accuracy, missing critical state, time-to-resume |
| Agent/model substitution | Switch model/vendor | decision retention, task continuity, policy adherence |
| Decision persistence | Seed confirmed/rejected/deferred decisions | reopening error rate, provenance accuracy |
| Semantic drift / fidelity | Multi-round AI revision | core-claim drift, framework-artifact consistency |
| Stale/conflict handling | Present conflicting current/old state | stale-use rate, conflict surfacing rate |
| Memory curation | Expand historical archive | retrieval precision/recall, context cost, resume quality |
| Review effort | Compare with chat-centric workflow | human review time, serious defect rate, correction latency |

These are research designs, not reported results.

---

## 6. Approval and provenance status

- T1–T10 and T12 are supported by AHICP-D030 and earlier human decisions such as HARC-D023/D024.
- T11 is literature-constrained; the cited work must not be represented as validation of AHICP.
- `semantic version control` and `generation–verification asymmetry` may be used as explanatory labels but are not claimed as established field-standard terms.
- `MA-FW-001` has received overall Framework Approval under `AHICP-D031`.
- The current Argument Map is aligned with `MA-FW-001` but may continue evolving as the working entrypoint toward a later `MA-FW-002`.
- Final Artifact Approval has not occurred.