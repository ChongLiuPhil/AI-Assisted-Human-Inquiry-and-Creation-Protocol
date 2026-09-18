# From Conversation to Persistent Research State: Human–AI Research Collaboration, Cognitive Responsibility, and Auditable Authorship in the AI Era

**Chinese title:** 从对话到持久研究状态：AI时代的人机研究协作、认知责任与可审计作者性

**Status:** `DERIVED-PROVISIONAL`  
**Framework status:** `WORKING-FRAMEWORK — not yet formally approved by the human author`  
**Protocol:** Human–AI Research Collaboration Protocol (HARC) v0.2.0-draft  
**Upstream Content Core:** `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`  
**Form Core:** `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`  
**Framework Status:** `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`  
**Evidence verification:** `evidence/METHODOLOGY_SOURCES.zh-CN.md`

> **Language status:** this English document is the synchronized mirror of the canonical Chinese `METHODOLOGY_ARTICLE.zh-CN.md`. If the two versions conflict, the Chinese version governs.

## Abstract

Generative artificial intelligence is substantially changing the division of work in research. Literature search, idea organization, argument reconstruction, draft generation, language editing, format conversion, and even some formalization can now be performed or assisted by AI Agents used as tools at speeds far beyond traditional manual workflows. Yet researchers' reading speed, capacity for understanding, judgment, and ability to bear responsibility do not increase at the same rate. This creates a methodological problem more fundamental than whether “AI can write a paper”: when more and more concrete research work can be assisted or automated by AI tools, what must human researchers still understand, confirm, judge, and take responsibility for?

This article presents the Human–AI Research Collaboration Protocol (HARC) as a persistent, explicit, and auditable architecture for human–AI research collaboration, currently implemented primarily through GitHub. HARC does not treat a chat window or the private context of a particular model as the long-term memory of a research project. Instead, it treats version-controlled repository documents as the persistent state of an evolving research process. The protocol separates the human author's substantive research intentions, presentation intentions, the operational argument framework maintained by AI, evidence constraints, historical decisions, and final derived text. It uses structures such as the Content Core, Form Core, Decision Log, Working Argument Map, and Approved Framework Snapshot to create a governable research state.

The article further argues that the purpose, central problem, and direction of a research or creative project must originate with humans and remain under human navigation or approval; within HARC, an AI Agent is a collaboration tool that may perform or assist extensive work but is not characterized as a cognitive subject. For long-form work, human core intellectual responsibility is operationalized primarily through the Layer 2 Framework: AI may assist in proposing, organizing, and expressing the framework, but before Framework Approval the human author must clearly understand, carefully review, and explicitly confirm every substantive element actually represented in it. On this basis, the article distinguishes framework-level defects from derived-expansion defects and Framework Approval from Final Artifact Approval, while discussing the relation of this architecture to the extended mind, distributed cognition, epistemic dependence, automation reliance, and existing scholarly authorship norms.

**Keywords:** human–AI collaboration; generative AI; research methodology; epistemic responsibility; authorship; distributed cognition; version control; GitHub; AI agents; research integrity

---

## 1. The question is no longer merely “Can AI write?” but “Who governs the research state?”

Discussions of generative AI and research writing often revolve around a surface-level question: can AI produce a competent paper, report, or book manuscript? That question matters, but it does not reach the most difficult part of long-term human–AI collaboration.

The deeper structural change is that **generative capacity is beginning to outpace human review capacity**. An AI agent can quickly produce multiple versions of an argument, dozens of pages of elaboration, literature summaries, alternative formulations, and structural reorganizations. Humans, however, still need time to read, understand, compare, judge, and bear the consequences. This article provisionally calls this difference the **generation–verification asymmetry**.

If research collaboration continues to use the traditional pattern of “conversation → full-text generation → line-by-line human review,” then as projects scale, humans face two unattractive choices. Either they reinvest enormous amounts of time in word-by-word verification, eroding much of AI's efficiency advantage, or they reduce verification, gradually losing the ability to say clearly which claims in a work they genuinely understood and confirmed.

The problem, therefore, is not only textual productivity but **cognitive governance**. How does a project lasting months or years preserve its intellectual state? How are the contribution boundaries between human and AI made explicit? Which changes represent a genuine change in the author's position, and which are merely temporary AI interpretations? When a new agent takes over, how does it know which material has been human-confirmed and which is merely a previous agent's suggestion?

HARC is designed to address these questions.

---

## 2. Why a chat window is not adequate long-term research memory

### 2.1 Context is transient

AI conversations are well suited to immediate reasoning, but they are not stable research infrastructure. Different models have different context limits, platform memory systems can change, account-level memory may not be transparent, and such memory is difficult to use as a formal research audit trail. More importantly, the lifetime of a research project can exceed the lifetime of any particular conversation.

HARC therefore begins from a simple principle:

> **Chat is the interaction surface; the repository is the persistent research state.**

“Repository” here currently means primarily GitHub. GitHub is not chosen because it has any special philosophical status, but because it provides several properties useful for long-term research collaboration: explicit files, version history, diffs, branches, commit records, cross-device access, and relatively mature automation and agent interfaces.

### 2.2 Textual version control does not by itself solve semantic drift

Git can tell us when a passage changed, but it cannot automatically answer more important questions:

- Did the human author change their position?
- Or did the AI alter the wording to make it more fluent?
- Is this a newly accepted thesis?
- Or an AI proposal awaiting human decision?
- Was this revision required by evidence?
- Or is it merely a temporary formatting default?

When these states are not distinguished, **semantic drift** occurs: a more polished and fluent AI-generated version gradually replaces what the human originally intended, until neither party can easily trace when the substitution happened.

HARC therefore needs more than textual version control. It needs a form of **semantic version control**.

---

## 3. From a repository to externalized research state

Treating GitHub as research memory has clear affinities with ideas about the extended mind and distributed cognition, but HARC need not commit to any strong metaphysical thesis.

In “The Extended Mind,” Clark and Chalmers argue that some stable, reliable, and readily available external resources can play roles in cognition analogous to internal memory (Clark & Chalmers, 1998). Hutchins's study of navigation teams emphasizes that complex cognitive activity can be distributed across people, tools, representations, and social organization rather than understood solely within isolated individuals (Hutchins, 1995).

HARC can draw on this line of thought to understand long-term research collaboration. The “current cognitive state” of a paper or book need not be entirely stored in the author's brain or entirely inside an AI context. It can be externalized into a set of structured, mutually constraining files.

This article adopts a weaker claim, however: **the repository is at least a cognitive scaffold and a carrier of external research state.** Whether it should further be considered part of some “collective cognitive subject” is not necessary for HARC to function.

HARC's aim is operational: important project state should be readable, recoverable, comparable, and auditable.

---

## 4. HARC's core architecture: separating authorial intention, AI representation, and final text

HARC separates several things that are often collapsed in conventional writing workflows.

### 4.1 Content Core: what does the human actually intend to claim?

The Content Core stores the currently active human substantive intention: research questions, core theses, key distinctions, scope conditions, explicit reservations, and unresolved questions.

Its purpose is to establish an **upstream source of semantic authority**. AI may propose new ideas, but before those ideas are accepted by the human, they do not automatically become the author's position simply because they are well written.

### 4.2 Form Core: how should the work be presented?

Presentation preferences are different from research content. Typeface, font size, section style, footnotes, citation format, page layout, figure style, and overall visual conventions for a book or paper should be managed in an independent Form Core.

This separation prevents another form of drift: an AI may temporarily choose a font size simply to make a LaTeX build work, and a later agent may mistakenly treat that choice as a long-standing author preference.

HARC further allows form preferences to inherit across levels: reusable author preferences, artifact-type templates, current-project decisions, external journal or publisher constraints, and temporary AI defaults should remain distinguishable.

### 4.3 Decision Log: separating current state from historical state

The Content Core and Form Core should stay concise because a new agent must quickly understand “what governs now.” But concision should not require deleting history.

The Decision Log therefore records how the project changed: when a claim changed, when an AI proposal was accepted or rejected, when a form requirement changed, and when the collaboration protocol itself was revised.

The Core represents the current active state; the Log represents how the project arrived there.

### 4.4 Working Memory: a parallel operational layer for current work and high-impact uncertainty

HARC no longer treats Critical Clarification as a “Layer 1.5” between the Content/Form Core and the Working Argument Map.

A more accurate architecture treats all three primary content layers as Long-Term Research Memory.

Layer 1 is the **Human Authorial Core**: progressively expressed, corrected, confirmed, and refined human commitments.

Layer 2 is the **Current Framework**: current argument structure, core propositions, key concepts, inferential relations, and section functions. It is constrained by Layer 1 but may contain structural material not stated item-by-item there. It is more revisable while still remaining durable project memory.

Layer 3 is the **Derived Artifact**: the paper, book, or report expanded primarily from Layer 2 while remaining compatible with Layer 1 and evidence constraints.

Parallel to these three layers, HARC maintains **Working Memory**. Working Memory answers not “what does the project ultimately claim?” but “where is the project now, and where should work resume?” It records current stage, work objective, overall plan, active tasks, recently completed work, next actions, TODOs, blockers, pending human decisions, Clarifications, synchronization defects, and handoff notes.

High-impact uncertainty is now simply a Clarification item inside Working Memory. When multiple reasonable interpretations of a core claim, concept, scope condition, inferential relation, section function, or key term exist, the AI should not choose privately. It should place the issue in Working Memory for human resolution.

After human resolution, perform Promotion:

`Working Memory -> Decision Log -> appropriate Long-Term Memory destination`

For human core content:

`Layer 1 Core -> Layer 2 Framework -> Layer 3 Artifact`

Working Memory is therefore not a fourth content layer. It also need not be one monolithic document. HARC can separate it into three logical roles: **Current Focus** for the highest-priority immediate objective, **Task Plan** for dynamic tasks, TODOs, blockers, pending human decisions, and Clarifications, and **Work Log** for stage-level historical summaries primarily intended for later human review.

This separation answers two different needs. Current Focus + Task Plan support seamless continuation after interruption; Work Log supports later human review of how the project and intellectual path changed. A replacement Agent therefore reads Current Focus and Task Plan by default rather than loading the entire Work Log. Completed tasks leave active Task Plan and receive high-level summaries in Work Log, while stable normative results are still promoted into the three Long-Term Memory layers.

Work Log records auditable progress, expressed high-level reasons, and direction changes rather than hidden AI chain-of-thought or scratchpads. This preserves a readable long-term research history for the human while keeping AI operational context compact.

Resolved Clarifications leave active state; the authoritative answer is deposited into Long-Term Memory, while Working Memory retains only necessary status and pointers.

### 4.5 Working Argument Map: the intermediate layer best suited to human–AI discussion

A full paper or book may be too long to serve as the direct object of every structural discussion. HARC therefore maintains a Working Argument Map, primarily maintained by AI but constrained by the Content Core.

It should be far shorter than the full manuscript, while explicitly showing:

- central questions and theses;
- major concepts;
- support and limitation relations;
- the argumentative function of each section or chapter;
- crucial objections;
- evidence dependencies;
- issues awaiting human decision;
- AI suggestions not yet accepted.

This document is not automatically endorsed by the author. It is first and foremost an **operational representation**.

---

## 5. From Working Framework to Approved Framework: a semantic approval gate

A core mechanism of HARC is the distinction between:

1. **Working Framework** — a mutable structure that AI can continuously revise;
2. **Approved Framework Snapshot** — a structural version that the human has actually read and explicitly approved.

Once a framework version is confirmed, it should be frozen as a versioned snapshot such as `FW-001`. If the central argument later changes materially, the project should create `FW-002` rather than silently overwriting the earlier framework.

The value of this mechanism is that it answers a question that becomes crucial in long-form AI collaboration:

> What exactly did the human author approve?

For a large book, a human may not be able to reread every sentence after each AI revision. But the human may still be able to review a compressed intellectual architecture with high intensity. Such a framework should include at least the central theses, major inferential relations, key distinctions, chapter roles, scope conditions, and explicitly unresolved issues.

HARC therefore treats framework approval as a **primary substantive intellectual checkpoint**.

---

## 6. Human responsibility in the AI era: AI may perform work, while purpose and intellectual architecture remain human responsibilities

HARC first needs a clear description of the AI role. An AI Agent is a research-collaboration tool, not an actor that this article needs to treat as a cognitive subject. The article therefore does not use “AI performs cognitive labor” or “AI performs cognitive tasks” as its central conceptual language. More precisely, AI tools may perform or assist with extensive concrete work, including:

- searching and preliminarily filtering literature;
- summarizing debates;
- generating candidate structures;
- discovering possible counterexamples;
- drafting paragraphs;
- formalizing an argument;
- checking internal inconsistencies;
- converting formats;
- building citations and bibliographies;
- comparing versions.

But the fact that AI can perform these kinds of work does not imply that the purpose, central problem, direction, and ultimate core responsibility of a research or creative project transfer to AI. What the project is trying to investigate, why it proceeds in a given direction, and which core claims are ultimately accepted must remain matters that the human author actually understands, navigates, and approves.

For long-form work, HARC operationalizes this human responsibility primarily through the Layer 2 Framework. AI may assist in proposing, organizing, and expressing the framework, but the framework cannot be merely a summary that receives a blanket human sign-off. Framework Approval requires the human to form a clear and complete understanding of every substantive element actually represented in it and to review and confirm those elements item by item, including core theses, inferential relations and their logical dependencies, key distinctions, scope conditions, section/chapter functions, and any specific wording included in the framework.

Hardwig's discussion of epistemic dependence can help contextualize the fact that research practices already depend on external resources, other people's work, and mediated information (Hardwig, 1985). But HARC does not infer from this that AI should be treated as a cognitive subject structurally equivalent to a human expert. The more important question is how human understanding, judgment, authorization, and responsibility remain locatable, inspectable, and auditable when people use AI tools to generate, organize, or transform research material.

HARC's responsibility model is therefore neither “humans must personally produce the whole text line by line” nor “sufficiently capable AI reduces human responsibility to a ceremonial approval.” Humans remain responsible for project purpose and direction, while the Approved Framework serves as the primary structural anchor of core intellectual responsibility. The concrete public version still requires Final Artifact Approval and remains subject to factual-accuracy, research-integrity, and venue requirements.

---

## 7. Framework defects and expansion defects are not the same kind of error

Suppose `FW-001` explicitly contains an invalid central inference—for example, its conclusion does not follow from its principal premises. This is a **framework-level defect**, because the error lies in an intellectual architecture that the human explicitly approved.

By contrast, if the framework itself does not contain the error but a later AI expansion introduces an unsuitable example, a faulty transition, repetitive prose, or a local expression problem, this is first a **derived-expansion defect**.

This distinction matters in two ways.

First, it improves the precision of responsibility attribution. We should not infer from a local AI-generation error that the human previously approved that error. Conversely, a structural defect already present in an Approved Framework cannot simply be dismissed as “the AI wrote it badly.”

Second, it helps organize review resources. Framework-level problems must be returned upstream for renewed approval. Expansion-level problems can be repaired downstream so long as the repair does not change the core structure.

This distinction, however, must not be misread as meaning that humans “only need to review the framework and may ignore the final manuscript.” Influential current scholarly norms such as those of ICMJE and Nature Portfolio still connect publication under human authorship with human approval, judgment, and accountability. ICMJE's current authorship criteria explicitly include final approval of the version to be published and agreement to be accountable for all aspects of the work. Nature Portfolio's current AI policies likewise emphasize that authors remain responsible for originality, accuracy, and integrity, and that the associated judgment cannot simply be delegated to AI. HARC therefore distinguishes two approval gates: Framework Approval and Final Artifact Approval.

---

## 8. Two approval gates: intellectual architecture and public accountability

### Gate A: Framework Approval

This gate confirms:

- major theses;
- inferential structure;
- central distinctions;
- the argumentative roles of sections or chapters;
- important limitations;
- intentionally open questions.

It can be understood as the work's **intellectual-architecture responsibility anchor**.

### Gate B: Final Artifact Approval

This gate confirms the concrete release version. The required level of review must follow the actual requirements of the discipline, publisher, journal, school, or institution.

Under current ICMJE and Nature Portfolio rules, for example, AI tools cannot substitute for the approval, judgment, and accountability roles assigned to human authors. HARC does not attempt to universalize those specific rules into a single authorship law for every field, nor does it seek to circumvent the requirements of any target journal, publisher, or institution. Instead, it provides a process architecture in which statements such as “I approved this,” “I am responsible for this,” and “this is my core judgment” can correspond to explicit versions, approval nodes, and audit trails.

Within HARC, framework approval establishes an intellectual baseline genuinely understood and accepted by the human. Final approval reconnects a concrete public version to that baseline and to relevant external rules.

---

## 9. Why the Approved Framework must be projected into the abstract, introduction, or general overview

If a human-approved framework exists only inside GitHub and readers cannot recover it from the work itself, then it is merely a project-management device.

HARC requires a stronger correspondence: the core structure of the Approved Framework should be faithfully projected into a reader-facing overview.

For an academic paper, this normally means that the abstract and introduction should clearly state the main problem, core thesis, principal argumentative moves, and roadmap of the paper. For a book, this should appear in the introduction or general overview and in the chapter roadmap.

This produces a useful drift detector. If `FW-001` and the final introduction have become clearly inconsistent, then something is wrong: the framework is obsolete, the introduction is inaccurate, or the body has materially drifted during later expansion.

---

## 10. Replaceable agents and non-disposable research state

Another HARC design principle can be summarized as follows:

> **AI agents may be replaceable; research state must not disappear with the agent.**

A project should therefore not depend primarily on the fact that “a particular model knows me well.” A replacement agent should be able to reconstruct from the repository:

- the current human substantive position;
- current presentation preferences;
- recent important decisions;
- which framework has been approved;
- which AI suggestions remain unapproved;
- which evidence conflicts remain unresolved;
- the status of the current full artifact.

Merely having these files in the repository does not guarantee that a replacement agent will read them correctly. AI platforms differ in how they discover entry files, automatic context, and repository instructions. HARC therefore also requires a **zero-context bootstrap protocol**: a root `START_HERE`, a machine-readable manifest, an explicit mandatory read order, and an Onboarding Report produced before substantive work.

This handshake turns “the agent understood the project” from an assumption into an observable check. The Agent should first report current stage, objective, active tasks, recently completed work, next actions, blockers, and pending human decisions from Working Memory, then retrieve task-relevant long-term Core, Framework, and Artifact state. If these cannot be recovered from repository state, the project has a persistence/onboarding defect that should be repaired before large-scale expansion continues.

HARC goes further by avoiding a second dynamic project-state copy in chat. The more precise mechanism is a **Repository-Backed Context Interface**: GitHub serves as both authoritative external memory and working-state store, while model context retains only a minimal Repository Resolver and temporarily retrieves files needed by the current task.

Working Memory and all three Long-Term Research Memory layers therefore remain in GitHub. Working Memory provides the resume point; Layers 1/2/3 provide durable intellectual and artifact state. The Agent fetches relevant latest canonical revisions when needed, reconfirms revisions before high-impact judgments or writes, writes changes directly back to the repository, and treats older excerpts already present in model context as stale after a write. A `HARC CONTEXT REFRESH` no longer means copying the whole project back into chat; it means resolving current task dependencies and fresh-fetching those files.

This does not mean that a model can reason with literally no context. Relevant information still has to become temporarily available during an inference. HARC changes the authority and lifecycle: **GitHub is the truth source; model context is a short-lived projection of repository state for the current task.**

This does not create “infinite context.” As a project grows, historical materials may still far exceed any model's one-shot context window. HARC therefore keeps Current Focus + Task Plan short and current and keeps Layer 1 Cores and Layer 2 Frameworks compact. Work Log may grow as a human-oriented historical chronicle while remaining outside default AI context; detailed older versions, evidence, and archives remain available through selective retrieval.

The project thereby shifts from “depending on one enormous conversation” to “depending on recoverable explicit state.”

---

## 11. HARC and existing authorship norms: from abstract responsibility to operational responsibility

Existing scholarly norms provide important boundary cases for HARC rather than a single unified rule that HARC can simply copy.

ICMJE links authorship with substantial contribution, drafting or critical revision of important content, final approval, and accountability. Nature Portfolio's current AI policies emphasize that authors remain responsible for originality, accuracy, and integrity and require disclosure of relevant AI use according to applicable rules. CRediT offers another useful perspective: its 14 contribution roles increase transparency about research contributions, but a contribution taxonomy is not identical to the determination of authorship eligibility under a particular journal or institution.

These examples suggest that at least two different questions must be addressed in the AI era:

1. Who did what?
2. Who understood, approved, and is responsible for what?

HARC focuses primarily on the process infrastructure for the second question, while still allowing contribution records and AI-use disclosures to become part of project state.

From this perspective, HARC is not trying to redefine a journal's authorship policy. It is trying to provide an **engineering implementation of authorial responsibility**: making statements such as “I approved this,” “I take responsibility for this,” and “this is my core judgment” correspond to explicit versions, files, and audit trails.

---

## 12. Automation reliance: why human approval gates cannot become ceremonial clicks

Framework approval by itself cannot guarantee genuine responsibility. A person can click “approve” without seriously reading. One of HARC's largest risks, therefore, is that genuine epistemic judgment becomes another formal ritual.

This risk is related to the problem of over-reliance discussed in classic automation research. Parasuraman and Riley (1997), for example, describe one form of automation misuse as excessive reliance on automation and note its potential relation to monitoring failures and decision biases.

HARC therefore cannot prove good collaboration merely from the existence of files. Future conformance tests should also examine:

- whether humans can explain the Approved Framework in their own words;
- whether humans understand key premises and limitations;
- whether agents actively surface uncertainty and evidence conflicts;
- whether a framework is compressed enough to be usable without hiding decisive issues;
- whether the final text remains faithful to the human-approved structure.

In other words, HARC addresses how to build an inspectable responsibility architecture; it does not automatically guarantee that every participant exercised high-quality judgment.

---

## 13. As an open protocol, HARC should be empirically testable

If HARC were only an essay about “how people ought to work with AI,” it would remain a normative proposal. One value of making it an open-source project is that it can be tested.

At least the following types of experiment could be designed:

### 13.1 Agent handoff test

Give a new agent the repository but not the original chat and test whether it can accurately reconstruct the current project state.

### 13.2 Semantic drift test

Let multiple agents successively revise the same research project and compare drift in the human's core theses with and without HARC.

### 13.3 Framework fidelity test

Compare the Approved Framework with the final abstract, introduction, and body structure.

### 13.4 Review-effort test

Measure whether framework approval enables human review time to shift from low-leverage line-by-line checking toward high-leverage structural judgment without significantly increasing serious errors.

### 13.5 Cross-model portability test

Have agents from different vendors and capability levels take over the same project and observe whether the repository architecture actually reduces platform dependence.

HARC can therefore function both as a normative project and as an ongoing experimental platform for AI-assisted research methodology.

---

## 14. Limitations and objections

HARC faces at least the following limitations.

First, **framework compression may hide detail-level risk**. A correct-looking high-level structure does not guarantee that every empirical citation, mathematical derivation, or factual statement is correct. Evidence verification cannot be replaced by Framework Approval.

Second, **human judgment is itself limited**. If an author lacks sufficient competence in a field, a structured framework can become merely ceremonial confirmation. HARC cannot transform lack of expertise into genuine epistemic responsibility.

Third, **maintaining the repository has overhead**. Full HARC may be too heavy for very short projects, so the protocol needs lightweight profiles.

Fourth, **confidentiality and data-governance problems are not solved by GitHub structure itself**. Sensitive data, unpublished peer-review materials, and restricted files still require compliance with relevant institutional and platform policies.

Fifth, **authorship norms differ across fields**. HARC must be treated as a base collaboration architecture rather than a universal authorization mechanism that overrides journals, publishers, universities, or law.

Sixth, **AI capabilities continue to change**. The protocol must keep its logical layer stable while allowing the implementation layer to evolve with agent capabilities, retrieval tools, and automation systems.

---

## 15. Conclusion: from “AI writing for humans” to human governance of AI-expanded research capacity

Generative AI creates a new speed structure in research: AI tools can generate, combine, restate, organize, and explore far more material than humans can inspect line by line. If we continue to define a “real human author” as someone who personally typed every sentence, that concept no longer describes actual human–AI research practice. But if AI's ability to perform more work becomes a reason to transfer purpose, judgment, direction, and responsibility to the model as well, human authorship and research responsibility lose substantive content.

HARC proposes a different direction: **expand the executable and expressive capacity of research while making human purpose, authority, memory, evidence, framework confirmation, and ultimate responsibility explicit.**

Under this model, an AI Agent used as a tool may perform or assist with extensive work, but the purpose, central problem, and direction of the research or creative project must be given and navigated by humans. A Working Framework may be developed with AI assistance, but it can become an Approved Framework only after the human has formed a clear understanding of every substantive element actually represented in it, reviewed those elements item by item, and explicitly confirmed them. Full text may then be extensively AI-expanded under that structure, but the expansion must remain faithful to the framework and pass the appropriate Final Artifact Approval before public release.

The central methodological question in AI-era research therefore need not be framed as whether machines participated in thinking. It can be stated more directly:

> **Can a research community clearly explain who supplied the project's purpose and direction, who understood and confirmed its core intellectual structure, which concrete work was performed or assisted by AI tools, which evidence constrained what, and whether intellectual continuity and human responsibility remain traceable after the Agent is replaced?**

HARC turns this question into an open-protocol problem that can be implemented, audited, tested, and iteratively improved.

---

## References and policy sources

- Clark, A., & Chalmers, D. (1998). The Extended Mind. *Analysis*, 58(1), 7–19. https://doi.org/10.1093/analys/58.1.7
- Hardwig, J. (1985). Epistemic Dependence. *The Journal of Philosophy*, 82(7), 335–349. https://doi.org/10.2307/2026523
- Hutchins, E. (1995). *Cognition in the Wild*. MIT Press. https://doi.org/10.7551/mitpress/1881.001.0001
- Parasuraman, R., & Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. *Human Factors*, 39(2), 230–253. https://doi.org/10.1518/001872097778543886
- International Committee of Medical Journal Editors (ICMJE). Defining the Role of Authors and Contributors. https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html
- Nature Portfolio. Editorial Policies, including Artificial Intelligence (AI) policies. https://www.nature.com/nature-portfolio/editorial-policies
- *Nature Methods*. (2026). Using AI responsibly in scientific publishing. *Nature Methods*, 23, 271. https://doi.org/10.1038/s41592-026-03020-1
- NISO. CRediT — Contributor Role Taxonomy; ANSI/NISO Z39.104-2022. https://credit.niso.org/ ; https://doi.org/10.3789/ansi.niso.z39.104-2022
- UNESCO. (2023). Guidance for Generative AI in Education and Research. https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research

For complete source-verification notes, see `evidence/METHODOLOGY_SOURCES.md`. BibTeX metadata is in `paper/methodology-references.bib`.

## Current article-development note

This document is the first complete working draft of HARC's methodology article. It was expanded from `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`, but that framework has not yet passed formal human Framework Approval. The article must therefore be treated as `DERIVED-PROVISIONAL`, not as a final human-approved manuscript.

The Chinese `paper/METHODOLOGY_ARTICLE.zh-CN.md` is the canonical semantic and editing source. This English document must remain synchronized with it.
