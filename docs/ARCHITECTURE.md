# AHICP Architecture

> **Language:** Chinese canonical: `ARCHITECTURE.zh-CN.md`; this English file is the synchronized mirror.

## System model

```text
        Zero-context Bootstrap / Onboarding Handshake
      START_HERE + MANIFEST + CONTEXT_INTERFACE
                       |
               Repository Resolver
                       |
              Working Memory Area
       +-----------------------------+
       | Current Focus               |
       | Task Plan                   |
       | Work Log (human history)    |
       +-----------------------------+
              /           |           \
             v            v            v
     +-----------+   +-----------+   +-----------+
     |  Layer 1  |-->|  Layer 2  |-->|  Layer 3  |
     | Authorial |   |  Current  |   |  Derived  |
     |   Core    |   | Framework |   | Artifact  |
     +-----------+   +-----------+   +-----------+
          ^               ^               ^
          |               |               |
          +------ Promotion from ----------+
                 resolved Working Memory
```

All three layers are Long-Term Project Memory. Working Memory Area is parallel: Current Focus + Task Plan provide resumable operational state, while Work Log preserves human-oriented stage history outside default AI takeover context.

## Repository-backed context

AHICP defines GitHub as the sole authoritative project-state source:

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

The Agent session retains only a minimal Repository Resolver. Dynamic Blocking Clarifications, Framework, Artifact, Core, and Decision Log state are retrieved on demand from latest canonical GitHub revisions. After writes, older context cache becomes stale.

## Authority is not identical to chronology

Later text is not automatically more authoritative than earlier canonical state.

A polished manuscript paragraph does not override the Content Core merely because it was generated later.

A human-approved framework does not override a later explicit human content decision; instead the framework becomes out of sync and requires revision/reapproval.

## Long-term memory, Working Memory, and history

AHICP separates:

- **Long-Term Memory Layer 1** — Human Authorial Core;
- **Long-Term Memory Layer 2** — Current Framework;
- **Long-Term Memory Layer 3** — Derived Artifact;
- **Working Memory / Current Focus** — highest-priority current objective and immediate next action;
- **Working Memory / Task Plan** — current tasks, blockers, Clarifications, TODOs, and plan;
- **Working Memory / Work Log** — human-retrospective stage history and direction changes;
- **history** — decisions, older frameworks, evidence, archived drafts, and Git history.

Working Memory supports resumption but does not replace the long-term layers. Stable results are promoted into the appropriate long-term destination.

## Three routing planes

### Content plane

```text
Human content feedback
  -> if high-impact ambiguity exists: Working Memory / Clarification
  -> human resolution
  -> Promotion -> Decision Log
  -> Content Core
  -> Working Argument Map
  -> Framework approval if material
  -> Derived Artifact
```

### Form plane

```text
Human form feedback
  -> Decision Log
  -> Form Core
  -> Typesetting / Rendering
  -> Derived Artifact
```

### Protocol plane

```text
Human workflow feedback
  -> Decision Log
  -> Protocol / AGENTS
  -> Agent behavior / templates
```

## Two approval gates

```text
Working intellectual structure
  -> FRAMEWORK_APPROVAL
  -> AI-assisted large-scale expansion
  -> FINAL_ARTIFACT_APPROVAL
  -> release/submission
```

The first gate governs intellectual architecture. The second governs the concrete release version.

## Core invariant

A stable AHICP project should allow a new competent agent to answer, from repository state alone:

1. What does the human currently mean to argue?
2. What presentation does the human currently want?
3. What argument framework has the human actually approved?
4. What has the AI proposed but the human not yet accepted?
5. What evidence constrains the current claims?
6. What is the highest-priority Current Focus, and which blockers, pending human decisions, and Clarifications are active in Task Plan?
7. What remains unresolved?
8. Is the current artifact synchronized with the approved state?
9. Are the Chinese canonical and English mirror files semantically synchronized?

If these questions cannot be answered without the previous chat history, the project has a persistence defect.
