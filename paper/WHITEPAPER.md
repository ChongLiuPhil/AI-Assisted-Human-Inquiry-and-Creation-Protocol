# Human–AI Research Collaboration Protocol
## A Repository-Centered Architecture for Persistent, Auditable, Human-Governed Research

**Working white paper — v0.1**

## Abstract

AI systems can now participate in research processes that extend far beyond isolated question answering: they can search literature, reconstruct arguments, formalize ideas, draft sections, revise manuscripts, maintain bibliographies, and help develop books or research programs over long periods. Yet most human–AI collaboration still relies on a fragile substrate: the conversational context of a particular AI system. Important human decisions remain embedded in chat histories; AI-generated reformulations can gradually become indistinguishable from the author's own commitments; formatting defaults can become mistaken for stable preferences; and a new agent often cannot reconstruct what the project actually means without rereading an inaccessible conversation.

The **Human–AI Research Collaboration Protocol (HARC)** proposes a repository-centered alternative. HARC treats GitHub not merely as storage for finished text, but as the durable, version-controlled state of a human–AI research relationship. It separates the human author's substantive commitments, presentation intentions, AI-maintained operational representation of the argument, evidence, historical decisions, and derived manuscript. It introduces explicit routing rules for new human feedback, versioned human approval of argument frameworks, and a distinction between framework approval and final artifact approval. The aim is to make AI-assisted research persistent across context windows and interchangeable agents while preserving human intellectual agency, traceability, and corrigibility.

HARC is not a theory that AI should replace authorship. It is a protocol for making the boundary between human intention and AI transformation explicit enough that long-running collaboration can remain intellectually governed by humans even when AI performs extensive downstream work.

---

## 1. The problem: collaboration without persistent intellectual state

Contemporary AI interfaces are optimized around conversations. This is useful for local tasks, but a serious research project is not merely a sequence of prompts and replies. It is a changing system of claims, definitions, evidence, unresolved questions, stylistic decisions, and commitments that may evolve over months or years.

When such a project lives primarily inside chat history, several structural problems arise.

### 1.1 Semantic drift

A human may express an initially rough but philosophically important thesis. An AI then produces a cleaner, more defensible formulation. That reformulation may be useful, but after several rounds of revision it can quietly become treated as if it were what the human originally intended.

The text improves while authorship of the meaning becomes less clear.

This is not simply a version-control problem. Git can show that sentence A changed into sentence B, but ordinary textual history does not by itself encode whether:

- the human changed position;
- the AI proposed a reinterpretation;
- the human accepted the proposal;
- the change was merely stylistic;
- or a temporary drafting choice accidentally became authoritative.

HARC therefore treats semantic state as something that must be represented explicitly.

### 1.2 Context-window dependence

A long project can outgrow any single AI conversation. Even when a platform provides memory features, those memories may be incomplete, opaque, account-specific, unavailable to another model, or unsuitable as a scholarly audit trail.

The result is a paradox: AI makes long projects easier to generate but can make them harder to maintain coherently.

HARC addresses this by externalizing durable state into the repository.

### 1.3 Structural opacity

A long manuscript is not a good operational interface for every intellectual decision. If a book has 150,000 words, a human should not need to reread all 150,000 words every time they want to decide whether Chapter 6 still supports the central thesis.

Humans need a compressed representation of the intellectual architecture: what the work claims, why the parts are connected, what each chapter contributes, which objections remain open, and which claims are provisional.

HARC calls this the **Operational Argument Representation**.

### 1.4 Presentation drift

AI agents also make thousands of small presentational choices: heading levels, margins, citation styles, typography, tone, footnote conventions, visual density, and document structure.

Some are temporary implementation defaults. Some are venue requirements. Some reflect genuine author preferences. If these categories are not separated, accidental defaults become misremembered as intention.

HARC therefore separates substantive content from form and presentation.

### 1.5 Agent handoff failure

A durable research system should not require the same AI agent forever. Models change. Platforms change. Tools change. A project may also use different agents for research, statistics, editing, or typesetting.

If the project's meaning exists only in one agent's conversational history, the agent is effectively part of the storage layer.

HARC instead aims for a stronger invariant:

> **AI agents may be replaceable; the research state must not be.**

---

## 2. Repository-centered research memory

HARC treats the repository as **externalized epistemic memory**: a durable representation of what the project currently means, how it got there, what remains unresolved, and how it should be expressed.

This does not mean that every chat message belongs in GitHub. A repository full of raw conversation transcripts would simply recreate the context problem in another location.

The protocol therefore uses a **promotion rule**:

> If losing a human instruction would change how a new competent agent should continue the project, that instruction should be promoted into durable repository state.

This transforms ephemeral conversation into structured project memory.

The repository is therefore not merely an archive. It is the current coordination medium among human and AI participants.

---

## 3. The canonical layers

HARC separates several functions that ordinary AI-assisted writing often collapses.

### 3.1 Content Core: what the human means

The **Content Core** records the human author's active substantive commitments.

It contains the current answer to questions such as:

- What is the project trying to establish?
- Which distinctions matter?
- Which theses are active?
- Which positions are tentative?
- Which questions remain deliberately open?

Only human-originated commitments, or AI proposals explicitly accepted or modified by the human, belong here.

The Content Core is not supposed to become a full manuscript. Its value comes from compression and authority.

### 3.2 Form Core: how the human wants the work expressed

The **Form Core** records presentation intention independently of research content.

A project can therefore distinguish:

- a font chosen temporarily by an AI;
- a citation style imposed by a journal;
- a layout chosen specifically for one book;
- a genuine cross-project author preference.

This prevents technical defaults from becoming false memories of authorial taste.

### 3.3 Decision Log: how current state was reached

Current-state files should be concise. But concision creates another risk: rewriting the current state can erase the history of how a decision was reached.

The **Decision Log** solves this by preserving a chronological audit trail.

A current thesis may change; the old thesis can disappear from the active Content Core while remaining visible in the historical decision record.

This yields two different forms of memory:

- **active memory** — what governs work now;
- **historical memory** — how the project arrived there.

### 3.4 Operational Argument Representation: what the project structurally says

The **Working Argument Map** is an AI-maintained structural model of the current work.

It is not merely a table of contents. It should expose inferential structure:

- thesis A depends on premises B and C;
- Chapter 3 establishes B;
- Chapter 4 addresses objection D;
- Section 6 narrows the scope of A;
- claim E remains an AI proposal and is not yet human-approved.

This is the principal interface for structural human–AI discussion.

The human does not need to inspect every expanded paragraph in order to reason about the architecture of the work.

### 3.5 Evidence layer: what constrains responsible assertion

Human authorial authority concerns intended meaning; it does not make evidence optional.

Literature, data, formal derivations, calculations, and source checks belong in an **Evidence Layer**.

When evidence conflicts with the Content Core, the correct response is neither:

- silently rewriting the human's position; nor
- hiding contrary evidence to preserve consistency.

The conflict should become explicit project state and return to the human for decision.

### 3.6 Derived artifact: the expanded work

The manuscript, book, report, or article is the **Derived Artifact**.

It can be much larger than the upstream state. AI can help produce explanations, examples, literature discussions, transitions, tables, and stylistic development.

But the artifact is not independently authoritative over the human-governed layers that generated it.

---

## 4. Three kinds of human feedback

A core operational rule of HARC is that human instructions should be classified before persistence.

### CONTENT

Changes what the work means, argues, assumes, distinguishes, or concludes.

### FORM

Changes how the artifact is expressed: typography, layout, genre, citations, visuals, presentation conventions.

### PROTOCOL

Changes how collaboration operates: persistence, approval gates, handoff, versioning, agent responsibilities.

A single instruction may be multi-label.

The distinction matters because each class has a different propagation path. A change to a philosophical thesis should not be implemented only as a local edit in Chapter 8. A change to font size should not be recorded as if it were an intellectual commitment. A change to approval workflow should not rewrite the research argument.

This is the protocol's **upstream-first principle**: update the authoritative state before propagating the change into derived artifacts.

---

## 5. From AI-maintained structure to human-approved framework

The operational argument map is useful precisely because it is flexible. But flexibility creates an authorship problem: an AI can reorganize a paper in ways the human has never seen.

HARC therefore distinguishes a **Working Framework** from an **Approved Framework Snapshot**.

### 5.1 Working Framework

Mutable, AI-maintained, open to experimentation.

It may include proposed restructurings, unresolved tensions, and AI-generated suggestions.

### 5.2 Approved Framework Snapshot

A compact version of the intellectual architecture explicitly reviewed and confirmed by the human.

Once approved, it is frozen under an identifier such as:

`FW-001`

A material change creates a new version instead of silently rewriting the old one.

This creates a semantic audit trail not available from ordinary manuscript versioning alone.

A future reviewer of the repository can ask:

- Which framework did the human actually approve?
- When?
- What changed afterward?
- Does the current manuscript still implement it?

---

## 6. A different allocation of human attention

One motivation for HARC is practical. AI can produce long text much faster than humans can inspect it line by line.

If the only acceptable collaboration model requires the human to manually reread every provisional sentence after every AI revision, the human becomes the throughput bottleneck and many potential gains from AI disappear.

HARC proposes that human attention be concentrated at a higher-value level: **intellectual architecture**.

For a long work, the human should be able to review a compressed representation containing:

- the main thesis;
- argument dependencies;
- major distinctions;
- chapter/section functions;
- limitations;
- unresolved questions.

Once the human approves that framework, AI may perform extensive downstream elaboration subject to framework fidelity.

This does not imply that final publication responsibility disappears. It distinguishes two checkpoints.

### Gate A: Framework Approval

Confirms the intellectual architecture.

### Gate B: Final Artifact Approval

Confirms the concrete version intended for submission, publication, or public release to the degree required by relevant external standards.

Thus:

> **Framework approval defines the center of substantive intellectual authorship; final artifact approval defines the threshold of public scholarly accountability.**

---

## 7. Framework projection into the final work

A framework that exists only in repository metadata would be useful for collaboration but invisible to readers.

HARC therefore requires a **projection relation** between the approved framework and the reader-facing overview of the final work.

For an academic paper, the abstract and introduction should faithfully express the main problem, thesis, argumentative move, contribution, and roadmap.

For a book, the introduction or overview chapter should explain the governing framework and the role of major chapters.

The overview does not need to reproduce repository language verbatim. The requirement is structural fidelity.

This creates a useful validation test:

- if the overview cannot accurately represent the approved framework, the overview or manuscript is out of sync;
- if the manuscript contains a major conclusion absent from the approved framework, the manuscript may have drifted beyond human approval.

---

## 8. Semantic version control

Git provides textual version control. HARC adds a layer of **semantic version control**.

A commit can tell us which characters changed. HARC state attempts to tell us what kind of change occurred:

- human changed thesis;
- human accepted AI proposal;
- AI proposed structure but human has not accepted it;
- form changed while content did not;
- evidence created a conflict;
- approved framework became outdated.

This distinction is central for research because a project is not merely a text file. It is a changing network of commitments.

---

## 9. Scaling beyond the context window

HARC does not abolish context-window limits. It relocates long-term memory outside the model.

A repository can grow indefinitely in ordinary storage terms, while each agent reads only the subset needed for current work.

The protocol therefore separates:

### Compact active state

- Content Core;
- Form Core;
- latest framework;
- current argument map;
- recent decisions.

### Expanding historical state

- full decision history;
- evidence archives;
- older frameworks;
- historical drafts;
- research notes.

When historical state becomes large, the system should add indexes, summaries, and dated archives rather than bloating the active cores.

The design goal is not infinite context. It is **persistent, selectively retrievable state**.

---

## 10. Agent replaceability and platform independence

HARC initially uses GitHub because it provides version history, branching, review, structured files, and widespread tooling.

But the conceptual architecture does not depend on a specific model.

A project following HARC should remain intelligible when moving from:

- one AI model to another;
- one specialized agent to another;
- one vendor to another;
- one conversation to another.

This changes the human–AI relationship from:

`Human <-> One Persistent Assistant`

into:

`Human <-> Persistent Research State <-> Interchangeable Agents`

The continuity belongs to the research state, not to the AI identity.

---

## 11. Self-hosting and protocol evolution

HARC itself should be developed using HARC principles.

The repository therefore contains a Protocol Core and Decision Log distinguishing:

- human-originated design commitments;
- AI elaborations;
- later community proposals;
- accepted protocol changes.

This self-hosting property provides a practical test: if the protocol cannot manage its own evolution transparently, it is unlikely to manage more complex research projects well.

---

## 12. Limitations and open questions

HARC v0.1 is deliberately modest.

### 12.1 It does not guarantee truth

Explicit provenance does not make an argument correct. Evidence review, expertise, and critical reasoning remain necessary.

### 12.2 It does not solve every authorship question

Different disciplines, institutions, and publishers may impose different rules for disclosure, final approval, or acceptable AI use. HARC provides internal provenance and responsibility checkpoints; it does not replace external policy.

### 12.3 It introduces maintenance overhead

Canonical state must be updated. If agents fail to promote important decisions, the repository becomes stale.

The protocol therefore needs lightweight tooling and validation in future versions.

### 12.4 Framework compression can omit nuance

A compact framework is useful precisely because it compresses. But excessive compression may hide important qualifications.

Framework design therefore becomes an intellectual skill, not a clerical task.

### 12.5 Human confirmation can become ceremonial

An approval gate only matters if the human actually understands what is being approved. Future work should explore interfaces that make framework review efficient without reducing it to a checkbox.

---

## 13. Future development

Potential extensions include:

- automated repository initialization;
- schema validation for canonical files;
- synchronization checks between approved framework and manuscript;
- visual argument graphs;
- provenance annotations at claim or section level;
- integration with citation managers and research databases;
- pull-request workflows for framework approval;
- reusable author form profiles;
- local-first and non-GitHub backends;
- multi-human / multi-agent governance;
- empirical evaluation of whether HARC reduces semantic drift and onboarding cost.

---

## 14. Conclusion

AI-assisted research needs more than better generation. It needs a durable collaboration architecture.

The central proposal of HARC is that human intention, AI representation, evidence, presentation intention, historical decisions, and final expression should not be collapsed into one mutable manuscript or one disappearing chat history.

By externalizing those functions into explicit repository state, HARC attempts to make long-running human–AI research:

- persistent;
- auditable;
- transferable across agents;
- structurally inspectable;
- corrigible by evidence;
- and governed by human approval at the level that matters most: the intellectual architecture of the work.

The protocol can be summarized in one line:

> **Externalize the research state, separate its authorities, approve the framework, and let AI expansion remain traceable to what the human actually meant.**
