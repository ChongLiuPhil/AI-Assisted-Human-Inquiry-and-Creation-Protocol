# Human–AI Research Collaboration Protocol
## A Human–AI Collaboration Architecture Using GitHub as Persistent Research State

**Working White Paper v0.1 (English mirror)**

**Language status:** Chinese `WHITEPAPER.zh-CN.md` is canonical; this English file is its synchronized mirror.  
**Historical status:** this white paper is retained as an early conceptual introduction. Newer normative rules are governed by Protocol Core / Specification, and newer scholarly argument is governed by the Methodology Article.

## Abstract

As AI begins to participate in long-term research, academic writing, book development, and sustained intellectual exploration, the difficult problem is no longer merely how to generate better prose. It is how a long-running project can preserve the human author's intellectual continuity, responsibility boundaries, and traceability across many conversations, multiple models, multiple agents, and long periods of time.

The Human–AI Research Collaboration Protocol (HARC) proposes a GitHub-centered solution. It does not treat the AI chat window as the project's long-term memory. Instead, it treats versioned repository documents as a persistent, explicit, and auditable shared research state. The protocol distinguishes the human author's substantive research intentions, the human author's presentation intentions, the AI's operational representation of argument structure, an evidence layer, historical decisions, and the final expanded artifact.

HARC further introduces three key mechanisms. First, important human feedback is classified as `CONTENT / FORM / PROTOCOL` and written into the corresponding foundational documents before it enters the final text. Second, an argument framework maintained by AI becomes a versioned Approved Framework only after explicit human reading and confirmation. Third, Framework Approval is separated from Final Artifact Approval, allowing human attention to focus primarily on intellectual and argumentative structure while preserving a distinct responsibility checkpoint before formal publication.

HARC's aim is not to make AI a hidden author. Its aim is to establish sustainable human–AI research infrastructure in which AI agents can be replaced without the research state disappearing with one agent or one chat window.

---

## 1. Why ordinary AI conversation is not adequate long-term research infrastructure

A short question can be answered in one conversation. A paper, a book, or a multi-year research project is different. It contains evolving theses, definitions, structures, evidence, objections, presentation preferences, and decision history.

If those elements primarily live inside AI-platform chat context, several structural problems arise.

### 1.1 Semantic drift

A human author may begin with a rough but important idea. The AI rewrites it to make the argument clearer or more defensible. The rewrite may be useful, but after many rounds, the AI's version can gradually be treated as though it were what the author meant all along.

The prose becomes more polished while it becomes less clear who actually determined the core meaning.

Traditional Git can show that a passage changed. It cannot by itself tell us whether the human changed position or the AI introduced an interpretation that the human has not yet confirmed.

Long-term human–AI research therefore requires not only textual version control, but a form of **semantic version control**.

### 1.2 Context-window dependence

No matter how large a context window becomes, a sustained research project can eventually exceed what one conversation can hold.

Even if a platform provides account-level memory, that memory may be opaque, incomplete, non-portable to other models or vendors, and unsuitable as a formal research audit record.

Long-term research should therefore not treat a particular AI platform as its only memory layer.

### 1.3 Structural opacity in long-form work

If a book contains hundreds of thousands of words, the human author should not need to reread the entire manuscript every time the argument structure is discussed.

A better approach is to maintain an operational text that is much shorter than the full manuscript while still showing its core structure:

- what the work is actually trying to establish;
- which chapter performs which argumentative step;
- which theses depend on which others;
- which problems remain unresolved;
- which ideas are merely AI suggestions.

This is HARC's Operational Argument Representation.

---

## 2. GitHub is not merely storage; it is externalized research memory

HARC treats GitHub as a form of **externalized research memory**.

Its central principle is:

> **Chat is a temporary interaction surface; the repository is the persistent shared research state.**

This does not mean that every sentence in a conversation should be saved.

The protocol uses a simple promotion rule:

> If a completely new AI agent took over tomorrow and losing one human instruction from the current conversation would change how that agent should continue the project, that instruction should be promoted into persistent GitHub state.

The repository is therefore not a warehouse of raw chat logs. It is a structured representation of project-relevant state.

---

## 3. HARC's foundational file layers

### 3.1 Content Core: what does the human actually intend to claim?

`CONTENT_CORE.md` stores only the currently active substantive research intentions of the human author.

It answers questions such as:

- What is the central problem?
- What does the human currently actually claim?
- Which theses are tentative?
- Which distinctions must be preserved?
- Which questions remain open?

AI may propose new arguments, but until the human accepts them, those arguments must not automatically be written as the author's position.

### 3.2 Form Core: how does the human want the work presented?

`FORM_CORE.md` is independent of research content.

It stores:

- artifact type;
- language and prose register;
- typeface and font size;
- page and paragraph systems;
- heading structure;
- citation and bibliography presentation;
- figure and table style;
- reusable cross-project author presentation preferences.

This prevents a common error: an AI chooses a font size or layout temporarily, and a later agent mistakenly infers that it is a stable personal preference of the author.

### 3.3 Decision Log: preserve the development history of thought and rules

Current state should remain concise, but research history must not disappear.

`DECISION_LOG.md` therefore records important human decisions: when a thesis was added, when an interpretation was rejected, when an AI suggestion was accepted, and when form requirements were changed.

The Content Core says “what governs now.” The Decision Log says “how we got here.”

### 3.4 Working Argument Map: the main interface for structural human–AI discussion

`argument-map.md` is an operational representation maintained primarily by AI.

It is not merely a table of contents. It should display:

- central theses;
- major premises;
- support and limitation relations among claims;
- the argumentative function of each chapter or section;
- strongest objections;
- evidence dependencies;
- questions awaiting human decision;
- AI proposals not yet accepted by the human.

For large projects, the main intellectual discussion between human and AI should occur as much as possible at this level, rather than requiring wholesale operations directly on a manuscript of tens or hundreds of thousands of words.

---

## 4. Three feedback routes: CONTENT, FORM, and PROTOCOL

HARC requires the AI to classify important human feedback before persisting it.

### CONTENT

Changes **what the work says**.

Examples include revising a thesis, adding a distinction, rejecting an interpretation, or changing argumentative scope.

Typical propagation:

`Human decision -> Decision Log -> Content Core -> Argument Map -> Final text`

### FORM

Changes **how the work is presented**.

Examples include typography, layout, chapter style, citation format, whether the artifact is a book or a paper, and visual presentation.

Typical propagation:

`Human decision -> Decision Log -> Form Core -> Typesetting/rendering -> Final artifact`

### PROTOCOL

Changes **how the human and AI collaborate**.

Examples include whether GitHub must be updated first, how framework confirmation works, how agents are replaced, and how versions are approved.

Typical propagation:

`Human decision -> Decision Log -> Protocol documents -> Agent behavior`

One item of feedback may carry multiple labels.

---

## 5. Why HARC needs a human-approved Framework Snapshot

The AI-maintained Working Argument Map must remain flexible, but it cannot automatically represent the human author.

HARC therefore distinguishes:

- **Working Framework** — AI-maintained, mutable, and used for discussion;
- **Approved Framework Snapshot** — explicitly read and confirmed by the human.

Once confirmed, the framework is frozen as:

`FW-001`

If the core argumentative structure later changes materially, the project should create:

`FW-002`

rather than silently overwriting the old version.

This allows a new agent or a future researcher to know:

- what the human author actually confirmed;
- when it was confirmed;
- what changed afterward;
- whether the current manuscript is still faithful to the approved framework.

This is what HARC calls a **semantic audit trail**.

---

## 6. Concentrating human attention on what matters most

A major feature of AI is that it can rapidly generate large amounts of expanded text while human reading speed does not increase proportionally.

If collaboration requires humans to reread hundreds of thousands of words line by line after every AI revision, then AI does not solve the structural problem of long-term research.

HARC therefore proposes that the most intensive human review should focus on the **intellectual architecture**.

The human should understand and confirm:

- core theses;
- the argument chain;
- major distinctions;
- logical relations among chapters;
- scope limitations;
- intentionally unresolved questions.

After confirmation, AI can perform extensive expansion within that framework.

HARC therefore distinguishes two gates.

### Gate A: Framework Approval

Confirms the work's core intellectual and argumentative architecture.

### Gate B: Final Artifact Approval

Before formal submission, publication, or public release, confirms the concrete release version to the degree required by the relevant discipline, journal, publisher, or institution.

In compressed form:

> **Framework approval defines the center of substantive intellectual authorship; final artifact approval defines the threshold of public scholarly accountability.**

---

## 7. The approved framework must be projected into the introduction or abstract

If the human-approved framework exists only inside GitHub while the reader cannot recover it from the final work, the framework is merely an internal management tool.

HARC goes further: the human-approved core structure should be faithfully expressed in a reader-visible overview.

Examples:

- academic paper: abstract + introduction;
- ordinary article: opening statement of the problem and argument route;
- book: introduction/general overview + chapter roadmap;
- report: executive summary + structural overview.

This creates an important check. If the introduction can no longer accurately represent `FW-001`, then either the introduction is wrong, the body has drifted, or the framework needs updating.

---

## 8. Not infinite context, but indefinitely growing external state

HARC does not claim that AI obtains an infinite context window.

More precisely, it allows the project to stop being bound to any single conversation window.

The project can accumulate a growing historical state without requiring a new agent to load everything at once.

HARC divides information into:

### Active state

- Content Core;
- Form Core;
- latest Framework;
- Argument Map;
- recent decisions.

### Growing historical state

- full decision history;
- evidence archives;
- older Frameworks;
- older drafts;
- research notes.

As history grows, the project can add indexes, summaries, and archives, retrieving detail selectively when needed.

The goal is therefore not infinite context, but **persistent and recoverable state**.

---

## 9. AI agents should be replaceable

HARC aims to transfer long-term continuity from the identity of an AI system to the research state itself.

A conventional picture is:

`Human <-> one persistent AI assistant`

HARC is closer to:

`Human <-> persistent research repository <-> interchangeable AI agents`

New models, new vendors, or specialized agents can take over so long as they can read the explicit GitHub state and follow the protocol.

The principle can be summarized as:

> **AI agents may be replaceable; research state must not disappear with the agent.**

---

## 10. Limitations and future work

HARC v0.1 still has clear limitations.

First, it cannot guarantee that the research content is true. The protocol can improve structural transparency but cannot replace evidence, expertise, and critical judgment.

Second, framework compression can itself lose detail. How to build a high-quality compressed representation of argument structure is therefore an important research problem.

Third, human confirmation can become ceremonial. If the author does not genuinely understand the Framework, the Approval Gate loses its meaning.

Fourth, maintaining these files introduces overhead. Future automation should reduce synchronization costs.

Future development may include:

- automatic repository initialization;
- machine-readable schemas;
- consistency checks between Framework and manuscript;
- visual argument graphs;
- claim-level provenance;
- multi-human and multi-agent governance;
- implementations beyond GitHub;
- empirical evaluation of whether semantic drift is actually reduced.

---

## Conclusion

The future of AI-assisted research requires more than better generation. It requires persistent collaboration architecture.

HARC's core idea is not that AI should do less work. It is that AI work should always remain traceable to explicit human intention, explicit structural confirmation, explicit evidence constraints, and explicit release responsibility.

It transforms long-term research from “an increasingly long chat transcript” into “an explicit research state that different agents can read, inspect, continue, and correct.”

In one sentence:

> **Externalize the research state, separate levels of authority, let humans confirm the core framework, and keep AI expansion traceable to what humans actually approved.**
