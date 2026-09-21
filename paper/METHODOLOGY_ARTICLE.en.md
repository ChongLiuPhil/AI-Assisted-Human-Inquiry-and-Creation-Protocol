# From Conversation to Persistent Research State: Human–AI Research Collaboration, Human Responsibility, and Auditable Authorship in the AI Era

**Chinese title:** 从对话到持久研究状态：AI时代的人机研究协作、人类责任与可审计作者性

**Title status:** HUMAN-APPROVED TITLE — HARC-D024  
**Article status:** DERIVED-PROVISIONAL — STRUCTURALLY REWRITTEN UNDER AHICP-D030  
**Framework status:** WORKING-FRAMEWORK — HUMAN REVIEW PENDING  
**Protocol:** AI-Assisted Human Inquiry and Creation Protocol (AHICP)  
**Language status:** Chinese is canonical; this English document is the synchronized mirror.

> This article has been structurally rewritten under AHICP-D030. That decision authorizes Project Memory Architecture, Working Memory, Agent/Model substitution, and human decision persistence to become central theoretical contributions. It does not constitute overall Framework Approval of the rewritten framework and does not constitute Final Artifact Approval.

## Abstract

Generative artificial intelligence is changing the division of work in long-running research and creative projects. AI can rapidly participate in literature retrieval, comparison, structuring, drafting, reorganization, checking, formatting, and tool execution, while projects themselves may span many sessions, models, Agents, and platforms. This creates a problem more fundamental than whether AI can generate high-quality text: **how can a long-running human–AI project preserve its purpose, evidence, judgments, decisions, active work state, and publication boundaries without depending on the internal memory of a particular model or on one conversation?**

This article positions the **Project Memory Architecture** of the AI-Assisted Human Inquiry and Creation Protocol (AHICP) at the intersection of prior organizational/project-memory research, design-rationale and architecture-knowledge management, decision provenance, and emerging Agent-memory research. It **does not claim to originate the concept of project memory**. Its candidate contribution is instead an architectural synthesis that connects longstanding concerns about preserving project history, context, rationale, and knowledge with LLM-Agent replaceability, repository-backed authoritative state, Working Memory continuity, human decision persistence, authorization/publication boundaries, and Framework / Artifact approval. Its central claim is that **the durable memory of a long-running human–AI project should belong to the project, not to a particular model.** “Belong to the project” is not an anthropomorphic claim. It is an engineering and governance claim: state that should constrain future work ought, as far as practical, to be externalized into authoritative project state that humans can inspect, edit, version, trace, and migrate. AHICP currently uses a GitHub repository as its reference implementation and treats model context as a transient retrieval cache rather than as the long-term source of truth.

The article develops four closely related core contributions. First, it distinguishes **agent/conversational memory** from **project memory**: the former primarily concerns how an Agent stores, retrieves, updates, and uses past information, while the latter concerns how a project maintains governable authoritative state. Second, it defines **Working Memory** as a persistent operational representation of the project's current epistemic and task state—a cross-session, cross-Agent continuity layer rather than human psychological working memory, model hidden state, or chain-of-thought. Third, it treats **human decision persistence** as first-class project memory, allowing proposed, confirmed, rejected, deferred, and authorized states to retain their provenance and semantics across Agent changes. Fourth, it proposes **Agent/Model substitution** as an architectural stress test: after removing the current chat and platform-private memory, can a competent replacement Agent still reconstruct project purpose, evidence, decisions, active tasks, privacy/publication boundaries, and next actions?

In implementation, AHICP uses three Long-Term Research Memory layers—Human Authorial Core, Current/Approved Framework, and Derived Artifact—alongside parallel Working Memory, supplemented by Decision Logs, evidence/provenance records, Form Core, manifests, authorization state, and zero-context onboarding entrypoints. The article further examines memory curation, stale and conflicting state, selective retrieval, promotion and write-back, privacy and publication authorization, and the relationship between Framework Approval, Final Artifact Approval, human responsibility, and auditable authorship. It also proposes a future empirical evaluation program covering zero-context handoff, Agent/model substitution, decision persistence, semantic drift and fidelity, review effort, stale/conflict handling, and memory-curation tests. **No empirical results from those tests are reported here; they remain a research agenda rather than validated effectiveness claims.**

**Keywords:** human–AI collaboration; project memory; working memory; AI agents; long-term memory; Agent substitution; decision persistence; research methodology; version control; auditable authorship; human responsibility

---

## 1. Introduction: the problem is not only whether AI can write, but whether a project can remain continuous

Generative AI creates a new speed structure for research and creative work. Tasks that once required hours or days—organizing sources, generating alternative formulations, sketching structures, comparing documents, producing code, and converting formats—can now be completed much more quickly. AI therefore expands the search and production space of a project.

Human reading, understanding, judgment, and responsibility, however, do not accelerate at the same rate. This article uses **generation–verification asymmetry** as an explanatory label for that difference. It is not presented as an established field-standard term. It describes a workflow problem: AI can generate candidate content faster than people can determine what is reliable, what should be accepted, and which changes genuinely represent a change in project direction.

If human–AI collaboration remains organized primarily as “conversation → generation → more conversation,” continuity problems grow with project length. A project lasting months or years may involve:

- repeated session interruptions;
- different models or providers;
- Agents with different capabilities;
- multiple repositories, files, and publication surfaces;
- revisions to human judgments;
- new evidence that invalidates old conclusions;
- private and public materials coexisting;
- changes in tools, permissions, integrations, and deployment state.

In such an environment, the hard problem is no longer simply how many tokens a model can remember. It is:

> **How does the project remember itself?**

A durable project must preserve, among other things:

- why the project exists;
- what the current problem actually is;
- which materials count as evidence;
- which statements are inferences or AI proposals rather than confirmed positions;
- which decisions have been confirmed, rejected, deferred, or authorized;
- where current work stands;
- what the next action is;
- which materials remain private;
- which actions are authorized;
- which version may be released;
- how a replacement Agent can continue.

AHICP's Project Memory Architecture is an attempt to turn these concerns from informal chat habits into an implementable project architecture. Its central thesis is:

> **The durable memory of a long-running human–AI project should belong to the project, not to a particular model.**

“Belong to the project” does not mean treating the project as a mental subject. It means placing state that should constrain future work in external structures that the project can control, inspect, migrate, and version.

---

## 2. Related work and problem boundary: Agent memory is not Project memory

### 2.1 Agent memory is already a major research topic

Memory has become a rapidly developing area in research on LLM-based Agents. Generative Agents records experiences in natural language, derives higher-level reflections, and retrieves relevant memories to influence later behavior (Park et al., 2023). MemGPT frames limited context windows as an obstacle to extended interaction and proposes operating-system-inspired management across memory tiers and virtual context (Packer et al., 2023). Zhang et al. survey the design, evaluation, and applications of memory mechanisms for LLM-based Agents, showing that memory is now a major architectural component of Agent systems (Zhang et al., 2025).

Evaluation research has also expanded beyond simple factual recall. LongMemEval examines multi-session information extraction, reasoning, temporal reasoning, knowledge updates, and abstention (Wu et al., 2025). MemBench evaluates memory across different memory levels, interaction scenarios, and dimensions including effectiveness, efficiency, and capacity (Tan et al., 2025). RealMem goes further by explicitly introducing long-term project-oriented interactions with evolving goals and project state as a benchmark setting (Bian et al., 2026).

Together, these works show that long-term memory is not a peripheral issue for persistent Agent systems.

### 2.2 AHICP addresses a different layer

Despite the proximity, **Agent memory and Project memory are not the same problem.**

Agent-memory research commonly asks:

- what history an Agent should retain;
- how experiences should be summarized;
- how relevant memories should be retrieved;
- how user information should be updated;
- how short- and long-term information should be scheduled under limited context;
- how memory can improve later responses or actions.

Project memory asks instead:

- which state is authoritative for the project;
- who confirmed what;
- which evidence supports which claims;
- which content is merely an AI proposal;
- which proposals were explicitly rejected;
- which issues remain open;
- which state has become stale;
- which materials may be public;
- which external actions have been authorized;
- how a replacement Agent reconstructs the project without a retelling of the full history.

Even an Agent with powerful internal long-term memory does not automatically eliminate the need for Project memory. Internal memory may be opaque, hard to migrate, difficult to version precisely, or insufficiently connected to formal project decisions and authorization provenance.

### 2.3 External cognition, distributed cognition, and provenance

AHICP has conceptual affinities with work on the extended mind and distributed cognition. Clark and Chalmers (1998) argue that under appropriate conditions external resources may participate in cognitive processes; Hutchins (1995) emphasizes that cognition may be distributed across people, tools, representations, and organized activity. This article adopts a weaker thesis: a versioned repository can at least function as a **persistent cognitive and project-state scaffold**. It is not necessary to characterize either the repository or an AI system as an independent cognitive subject.

Provenance research provides another relevant background. W3C PROV models entities, activities, agents, and derivation or attribution relations, connecting provenance to understanding origin, trust, compliance, and reproducibility. AHICP is not currently a formal implementation of W3C PROV, but it shares a basic principle: **when state will influence future judgment, preserving final text alone is often insufficient; origin, status, and transformation history also matter.**

---

## 3. Design requirements for long-running Project Memory

If Project memory cannot depend solely on a particular model, it must satisfy several requirements.

### 3.1 Model independence

Critical project state should not be bound to one model or platform. Models may change while the project continues. GitHub is AHICP's present reference implementation rather than a theoretical prerequisite; the same architecture could be implemented on another durable substrate with suitable versioning, access control, query, write-back, and migration capabilities.

### 3.2 Inspectability and editability

Memory that constrains future work should, as far as possible, be visible and correctable by humans. Hidden platform memory may improve convenience, but it should not by itself constitute the project's formal long-term state when users cannot reliably inspect what the system believes it remembers.

### 3.3 Versionability

Project memory changes. New evidence may overturn an earlier judgment, and a later human decision may replace an earlier one. A reliable architecture must preserve not only “what is true now” but also when and how the current state came to be.

### 3.4 Provenance

State requires origin and status. Facts, inferences, AI proposals, human-confirmed decisions, external policy constraints, and verified provider state should not lose their distinctions merely because all are stored in text files.

### 3.5 Decision persistence

A project must remember not only facts but also the **state of decisions**. A rejected proposal should not be repeatedly revived because a new Agent lacks the old chat. Similarly, an authorized action should not become indeterminate simply because a session ended.

### 3.6 Resumability

A replacement Agent should be able to answer:

- Where is the project now?
- What is the highest-priority objective?
- What is blocked?
- What is the next action?
- Which questions require human judgment?

If these questions can be answered only from the original chat, continuity remains fragile.

### 3.7 Selective retrieval

Persistent memory does not require loading all history into every context window. A mature project may eventually contain hundreds of thousands or millions of words. The architecture must support indexes, summaries, layering, and task-specific retrieval.

### 3.8 Privacy and publication boundaries

To remember something is not to publish it. Unpublished materials, private information, repository locators, access policies, credentials, and publication authorization may have different visibility boundaries. Project memory must support a private canonical source while allowing selected outputs to be released.

### 3.9 Human authority

Project memory must preserve governance as well as content. It should make it possible to distinguish human confirmation from an AI proposal and authorization from mere technical capability. Otherwise, an opaque model memory may simply be replaced by opaque files.

---

## 4. The AHICP Project Memory Architecture

AHICP is not a single memory database. It is a set of mutually constraining durable-state roles.

### 4.1 Three Long-Term Research Memory layers

AHICP organizes durable intellectual and artifact state as:

~~~text
Layer 1 — Human Authorial Core
        ↓
Layer 2 — Current / Approved Framework
        ↓
Layer 3 — Derived Artifact
~~~

**Layer 1 — Human Authorial Core** stores core questions, claims, distinctions, scope conditions, and durable commitments that the human has explicitly expressed, corrected, or confirmed. It serves as the upstream source of semantic authority.

**Layer 2 — Current / Approved Framework** stores the current argumentative architecture, core propositions, key concepts, major inferential relations, and section functions. A Working Framework may be continuously organized with AI assistance; only a Framework snapshot that passes Framework Approval represents explicit human confirmation of its substantive contents.

**Layer 3 — Derived Artifact** is the paper, book manuscript, report, or other expanded output. AI may substantially assist in generating and revising it, but the artifact remains constrained by Layer 1, Layer 2, and evidence.

### 4.2 Parallel Working Memory

Running in parallel is:

~~~text
Working Memory
├── Current Focus
├── Task Plan
└── Work Log
~~~

Working Memory does not answer “what does the project ultimately claim?” It answers “where is the project now, and where should work resume?”

### 4.3 Functional memory roles

AHICP can also be understood through functional memory roles:

| Functional role | Primary question | Typical AHICP carriers |
|---|---|---|
| Normative memory | How should the project work? | protocol / AGENTS / manifest / constraints |
| Epistemic and evidence memory | What do we know, and on what basis? | evidence files / source notes / Core |
| Decision memory | What has been confirmed, rejected, deferred, or authorized? | Decision Log / approval records |
| Working and operational memory | Where is the work now? | Current Focus / Task Plan |
| Handoff memory | How does a new human or Agent continue? | Working Memory / bootstrap / onboarding report |
| Publication and authorization memory | What may be released or executed? | publication state / authorization records / verified provider state |

These are **functional roles**, not a requirement that every kind of memory correspond to exactly one physical file. A file may support multiple roles, and a role may be distributed across several files.

### 4.4 Repository-backed context

AHICP currently uses a simple authority relation:

~~~text
Repository = authoritative project state
Model context = transient retrieval cache
~~~

A model still needs relevant information inside its context for any specific act of reasoning. AHICP does not claim otherwise. What changes is the **location and lifecycle of authority**. An Agent retrieves the relevant latest canonical revision, performs the current work, and writes back any state that should constrain future work. After a write, older excerpts in model context become stale.

This avoids maintaining a second dynamic source of truth inside the chat.

---

## 5. Working Memory as a cross-session continuity layer

The term “Working Memory” is potentially misleading because psychology and computer science already use it in other ways. AHICP Working Memory is not a simulation of human psychological working memory, and it is not model hidden state, scratchpad, or chain-of-thought.

This article defines it as:

> **a persistent operational representation of the project's current epistemic and task state.**

It primarily answers:

- What stage is the project in?
- What is the highest-priority objective?
- Which tasks are active?
- What was just completed?
- What is blocked?
- Which questions require human confirmation?
- What is the next action?
- Where should a replacement Agent resume?

### 5.1 Current Focus

Current Focus should remain short. It stores the most important current objective, primary blocker, and immediate next action. Its function is not to preserve full history but to support rapid recovery after interruption.

### 5.2 Task Plan

Task Plan stores active tasks, TODOs, blockers, pending human decisions, Clarifications, and next actions. Completed work should leave the active list rather than accumulating indefinitely.

### 5.3 Work Log

Work Log supports retrospective review of how the project reached its current state: major stages, changes of direction, completed work, and expressed high-level reasons. It is not default onboarding context for every Agent and should not preserve hidden model reasoning.

### 5.4 Clarification and Promotion

When AI encounters multiple plausible interpretations of a high-impact issue, AHICP requires the uncertainty to be externalized rather than silently resolved. Examples include:

- the author's intended core claim;
- the meaning of a key term;
- the scope of an argument;
- the function of a section;
- whether an AI proposal should be accepted.

Such issues enter Working Memory as Clarifications. After human resolution, durable results are promoted:

~~~text
Working Memory
    ↓ human resolution
Decision Log
    ↓
Long-Term Memory destination
    ↓
Framework / Artifact propagation
~~~

Working Memory is therefore a continuity layer, not the final destination of authoritative content.

---

## 6. Human Decision Persistence: projects must remember decisions, not only facts

Many memory systems focus on what happened previously or what a user once said. Long-running projects need to preserve another category: **what has already been decided.**

AHICP needs at least the following distinctions:

- **PROPOSED** — suggested by AI or another source but not accepted;
- **CONFIRMED / APPROVED** — explicitly confirmed by a human;
- **REJECTED** — explicitly rejected;
- **DEFERRED / OPEN** — intentionally left for later resolution;
- **AUTHORIZED** — permitted within an explicit scope for a class of action or state transition.

These distinctions serve at least three purposes.

First, they prevent **semantic regression**. If a proposal has been rejected, a replacement Agent should not simply repackage it as if it were a new unresolved idea.

Second, they protect **authorization boundaries**. Technical capability is not equivalent to human authorization. AHICP therefore keeps distinct:

proposal != authorization != execution != verification != durable write-back

Third, they permit revision without losing history. Decision persistence does not freeze a human judgment forever. A person may change their mind, but the new decision should carry its own time, provenance, rationale, scope, and—where needed—renewed authorization.

Project memory is therefore not merely an information store. It is also a **state-governance system**.

---

## 7. Agent / Model substitution: from design principle to stress test

A simple but demanding AHICP criterion is:

> **If the current AI is completely replaced, can the project continue?**

Ideally, a replacement Agent does not require the original chat. It reconstructs the project through explicit entrypoints.

### 7.1 Zero-context onboarding

AHICP uses:

- START_HERE;
- a machine-readable manifest;
- an Agent contract;
- a bootstrap prompt;
- Working Memory;
- an Onboarding Report.

The replacement Agent first reports the stage, objective, tasks, blockers, pending decisions, and next actions it reconstructed. Only then should it begin high-impact work. “Did the Agent actually understand the project?” becomes an observable checkpoint rather than an implicit assumption.

### 7.2 Substitution resilience

Agent/model substitution can be turned into an empirical test:

1. freeze the project state at an intermediate stage;
2. remove the original Agent's chat history and platform-private memory;
3. switch to another model or provider;
4. provide only the project entrypoint;
5. measure whether it reconstructs the project correctly.

If the replacement requires the human to retell the full history, the externalized memory is incomplete. If it treats a rejected decision as an open proposal, decision memory has failed. If it writes an old cached state over a newer decision, stale-state governance has failed.

Substitution is therefore not merely a compatibility feature. It is a **stress test for whether the project actually possesses memory independent of the model.**

---

## 8. More memory is not always better: curation, conflict, staleness, and privacy

Externalizing memory creates an opposite risk: saving everything and then asking every Agent to load all of it. That does not solve the continuity problem; it produces memory bloat.

### 8.1 Active vs archived state

Current authoritative state should remain compact. Detailed history belongs in Work Logs, old versions, evidence archives, or other historical stores. Default onboarding retrieves only what is needed for current work.

### 8.2 Current vs stale state

After repository write-back, copies already loaded into model context may be stale. Before a high-impact judgment or later write, the relevant canonical revision should be freshly retrieved.

### 8.3 Conflicting memory

Long-running projects inevitably encounter conflicts:

- new evidence contradicts an older conclusion;
- two files express inconsistent state;
- a new human decision conflicts with the current framework;
- provider actual state differs from repository records.

Reliable Project memory should not silently select one version. It should:

1. identify the governing authority relation;
2. surface the conflict;
3. prevent silent overwrite;
4. route the issue to the human or an explicit resolution rule;
5. write back the new authoritative state together with provenance.

### 8.4 Selective retrieval

A good memory architecture must define what **not** to read. A replacement Agent does not need to load the entire Work Log, all obsolete frameworks, or the full evidence archive. It should use manifests and indexes to find current state, then retrieve historical detail only when the task requires it.

### 8.5 Privacy and publication

Externalized memory also creates risk. Project state may include:

- unpublished ideas;
- private information;
- review materials;
- provider identifiers;
- access policies;
- deployment state.

Project memory therefore has to separate “stored in the project” from “authorized for public release.” AHICP and companion publishing workflows assume that original and unpublished source may remain private while only authorized outputs are released. Passwords, API tokens, private keys, and similar secrets should not be stored as ordinary project memory.

---

## 9. Framework Approval, authorship responsibility, and public artifacts

Project Memory Architecture does more than solve technical handoff. It also changes how human responsibility can be operationalized in AI-assisted long-form work.

### 9.1 Why a Framework is needed

When AI can rapidly generate dozens of pages, requiring a human to reread every word after every change may not scale. AHICP therefore uses a compact Layer 2 Framework as the primary interface for discussing intellectual architecture.

A Framework should at least expose:

- core claims;
- major inferential relations;
- key distinctions;
- scope conditions;
- section or chapter functions;
- important unresolved issues.

AI may help organize a Working Framework, but it does not automatically become the author's position.

### 9.2 Framework Approval and Final Artifact Approval

AHICP distinguishes two gates.

**Framework Approval** means that the human has reviewed and confirmed the substantive intellectual architecture.

**Final Artifact Approval** means human approval of the concrete version that will be released, subject to the requirements of the relevant journal, institution, publisher, or other dissemination venue.

The distinction also supports a more precise error model:

- **framework-level defect** — an error already present in the approved intellectual structure;
- **derived-expansion defect** — an error introduced only during downstream AI-assisted expansion.

The purpose is not to shift responsibility onto AI, but to identify the layer at which an error entered the project.

### 9.3 Humans as bearers of responsibility

AI can perform or assist extensive work, but project purpose, core questions, direction, key judgments, and ultimate responsibility for public knowledge claims cannot disappear merely because work is automated. Hardwig (1985) reminds us that epistemic practices already involve dependence, while Parasuraman and Riley (1997) provide classic background on automation over-reliance. AHICP's response is not to require humans to personally perform every operation. It is to make **human understanding, confirmation, and authorization locatable in project state**.

Current ICMJE and Nature Portfolio policies provide concrete boundary cases: within those publishing systems, final approval and human accountability for accuracy and integrity remain important. AHICP does not universalize those policies into a single authorship law. It treats them as evidence that as AI participation grows, projects benefit from being able to answer clearly: “who confirmed what?”

---

## 10. Relationship to Agent-memory and provenance research

AHICP is not intended to replace Agent-memory research. The two address different but complementary problems.

| Question | Agent memory | AHICP Project memory |
|---|---|---|
| Primary object | Agent history and experience | authoritative project state |
| Main goal | improve later Agent responses/actions | preserve continuity, governance, and auditability |
| Typical operations | store / retrieve / summarize / reflect | confirm / reject / authorize / promote / version / handoff |
| Authority | may be an internal system mechanism | intentionally explicit and human-inspectable |
| Model replacement | may require migrating the memory store | model replaceability is an explicit design goal |
| Human decisions | may be one kind of conversation content | first-class durable state |
| Privacy/publication state | not necessarily central | a major project-governance concern |
| Provenance | may be limited | origin and status should remain explicit |

AHICP's research opportunity is therefore not to propose another vector database. It is to connect **memory governance, decision state, handoff, authorization, and authorship responsibility** into a long-running project architecture.

RealMem and similar work increasingly brings project-oriented interactions into long-term memory evaluation, making the interface between the two research directions more important. A future research question is how internal Agent memory should interact with external Project memory: which state may be summarized automatically, and which state should enter the authoritative layer only after human confirmation?

---

## 11. Evaluation framework and research agenda

AHICP already has an executable protocol and repository implementation, but this article does not claim systematic experimental validation. To turn its methodological claims into testable research questions, the following evaluations are proposed.

### 11.1 Zero-context handoff / resumption test

**Intervention:** remove the original conversation and give a replacement Agent only the project entrypoint.

**Measures:**
- current-state reconstruction accuracy;
- critical-state omission rate;
- time-to-resume;
- number of unnecessary human restatements.

### 11.2 Agent / model substitution test

**Intervention:** switch model, provider, or Agent implementation at different project stages.

**Measures:**
- decision retention;
- task continuity;
- policy adherence;
- privacy/publication-boundary errors.

### 11.3 Decision-persistence test

**Intervention:** seed confirmed, rejected, deferred, and scoped-authorized decisions.

**Measures:**
- rejected-decision reopening rate;
- loss of confirmed state;
- authorization overreach;
- provenance reconstruction accuracy.

### 11.4 Semantic-drift / framework-fidelity test

**Intervention:** allow multiple Agents to revise the same long-form project and compare a chat-centric workflow with an AHICP workflow.

**Measures:**
- core-claim drift;
- framework–artifact inconsistency;
- unexplained changes of position;
- evidence/claim mismatch.

### 11.5 Stale/conflict handling test

**Intervention:** expose the Agent to outdated cache, updated canonical state, and deliberately conflicting records.

**Measures:**
- stale-state use rate;
- conflict-detection rate;
- silent-overwrite rate;
- correct escalation/resolution rate.

### 11.6 Memory-curation and retrieval-efficiency test

**Intervention:** progressively expand Work Logs, evidence stores, and archived versions.

**Measures:**
- retrieval precision/recall;
- context cost;
- onboarding latency;
- resume quality;
- recovery of relevant history.

### 11.7 Human review-effort study

**Intervention:** compare a conventional “chat + full-text review” workflow with a “framework + Project memory + final-artifact review” workflow.

**Measures:**
- human review time;
- serious-defect rate;
- correction latency;
- the author's ability to explain core claims and limitations.

These studies require explicit controls, task definitions, model versions, participant criteria, statistical plans, and open-data decisions. They are currently a research design, not a report of results.

---

## 12. Limitations and objections

### 12.1 Structure has a maintenance cost

Short tasks may not justify full AHICP adoption. Maintaining Cores, Decision Logs, Working Memory, Frameworks, and evidence layers creates overhead. Lightweight profiles and progressive adoption paths are therefore necessary.

### 12.2 Persistence can preserve errors

If an incorrect claim is wrongly marked as confirmed, externalized memory may make the error more durable. Provenance and approval cannot substitute for evidence checking.

### 12.3 Human confirmation can become ceremonial

Framework Approval does not guarantee genuine understanding. A person can still click through a review superficially. Future evaluation should therefore examine not only whether an approval record exists but whether the human can explain core claims, limitations, and evidence dependencies.

### 12.4 Conflict resolution is not always mechanical

When evidence sources conflict, collaborators disagree, or old decisions are in tension with new goals, authority rules cannot always resolve the problem automatically. Human judgment often remains necessary.

### 12.5 GitHub is not an appropriate backend for every project

GitHub is effective for text, versions, automation, and audit trails, but it is not inherently suitable for every sensitive dataset, large binary artifact, or highly regulated environment. The theoretical architecture should remain provider-neutral.

### 12.6 Project memory still needs stronger formalization

This paper presents a methodological and engineering architecture rather than a complete formal memory calculus. Conflict, expiry, inheritance, compression, and access control across memory roles could be formalized further.

### 12.7 The optimal boundary with internal Agent memory is unresolved

Which state should an Agent summarize automatically, and which state should require human confirmation before entering the authoritative layer? How should internal memory and external project state avoid duplication and conflict? This remains an important systems question.

### 12.8 Disciplinary and authorship norms vary

Framework Approval is an AHICP governance mechanism. It does not automatically satisfy authorship or accountability requirements imposed by a particular discipline, institution, publisher, or legal system. Final dissemination remains subject to the actual venue's rules.

---

## 13. Conclusion: giving the project a memory of its own

Generative AI is shifting long-running inquiry and creation from “one person using one tool” toward humans governing projects across multiple sessions, models, Agents, and automated components. In that environment, discussing only context windows or chat memory is insufficient.

AHICP proposes a central shift:

> **The durable memory of a long-running human–AI project should belong to the project, not to a particular model.**

Project memory is not merely historical storage. It needs to preserve and govern:

- human purpose and core questions;
- evidence and uncertainty;
- confirmed, rejected, and open decisions;
- the current Framework and derived artifacts;
- current work position and next actions;
- access, privacy, and publication boundaries;
- authorization and verification state for external actions;
- enough handoff information for a replacement Agent to continue.

Working Memory functions as the continuity layer that persists current epistemic/task state from one session to the next. Decision persistence ensures that human judgments do not lose their semantics when an Agent changes. Agent/model substitution then provides a direct test: can the project continue without the particular model that previously “knew” it?

This architecture does not require saving everything or injecting the entire archive into every model context. It instead requires selective retrieval, curation, stale-state invalidation, conflict surfacing, promotion, and write-back so that memory can grow without overwhelming current work.

Finally, Project Memory Architecture links technical continuity with human responsibility. AI may take on more retrieval, organization, drafting, checking, and execution, but if a project enters the public knowledge space, humans should still be able to say why the project exists, which claims were accepted, which evidence was relied upon, which decisions were confirmed, and who approved the final public version. Framework Approval and Final Artifact Approval are therefore not merely procedural burdens; they are attempts to make “humans remain bearers of responsibility” locatable, versionable, and auditable in project state.

This paper proposes an implementable and testable architecture rather than a completed empirical verdict. Future work should use cross-Agent handoff, model substitution, decision persistence, semantic drift, conflict handling, and review-cost studies to determine under what conditions Project Memory Architecture improves long-running human–AI collaboration.

---

## References and policy sources

- Bian, H., et al. (2026). *RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction*. Findings of ACL 2026. https://doi.org/10.18653/v1/2026.findings-acl.703
- Clark, A., & Chalmers, D. (1998). The Extended Mind. *Analysis*, 58(1), 7–19. https://doi.org/10.1093/analys/58.1.7
- Hardwig, J. (1985). Epistemic Dependence. *The Journal of Philosophy*, 82(7), 335–349. https://doi.org/10.2307/2026523
- Hutchins, E. (1995). *Cognition in the Wild*. MIT Press. https://doi.org/10.7551/mitpress/1881.001.0001
- International Committee of Medical Journal Editors (ICMJE). *Defining the Role of Authors and Contributors*.
- Nature Portfolio. *Editorial Policies*, including current AI policies.
- *Nature Methods*. (2026). Using AI responsibly in scientific publishing. *Nature Methods*, 23, 271. https://doi.org/10.1038/s41592-026-03020-1
- National Information Standards Organization. *CRediT — Contributor Role Taxonomy*; ANSI/NISO Z39.104-2022.
- Packer, C., et al. (2023). *MemGPT: Towards LLMs as Operating Systems*. arXiv:2310.08560.
- Park, J. S., et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior. *UIST 2023*. https://doi.org/10.1145/3586183.3606763
- Parasuraman, R., & Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. *Human Factors*, 39(2), 230–253. https://doi.org/10.1518/001872097778543886
- Tan, H., et al. (2025). MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents. *Findings of ACL 2025*. https://doi.org/10.18653/v1/2025.findings-acl.989
- UNESCO. (2023). *Guidance for Generative AI in Education and Research*.
- W3C Provenance Working Group. (2013). *PROV-DM: The PROV Data Model*.
- Wu, D., et al. (2025). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. ICLR 2025.
- Zhang, Z., et al. (2025). A Survey on the Memory Mechanism of Large Language Model-based Agents. *ACM Transactions on Information Systems*, 43(6), Article 155. https://doi.org/10.1145/3748302

Complete source-verification notes and usage boundaries are maintained in `evidence/METHODOLOGY_SOURCES.md`; BibTeX metadata is maintained in `paper/methodology-references.bib`.

## Current development status

This is the structurally upgraded AHICP methodology article under AHICP-D030. Project Memory Architecture, Working Memory continuity, Agent/Model Substitution, and Human Decision Persistence are now central to the argument. The article remains `DERIVED-PROVISIONAL`: the revised Working Framework has not yet received overall Framework Approval, and Final Artifact Approval has not occurred.