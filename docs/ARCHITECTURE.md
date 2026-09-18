# HARC Architecture

> **Language:** Chinese canonical: `ARCHITECTURE.zh-CN.md`; this English file is the synchronized mirror.

## System model

```text
        Zero-context Bootstrap / Onboarding Handshake
             START_HERE + HARC_MANIFEST
                        |
                   Human Author
                        |
        +---------------+---------------+
        |               |               |
     CONTENT           FORM          PROTOCOL
        |               |               |
        v               v               v
  CONTENT_CORE      FORM_CORE      AGENTS / spec
        \               /               |
         \             /                |
          +---- DECISION_LOG <-----------+
                     |
                     v
            Working Argument Map
                     |
          Human Framework Approval
                     |
                     v
             Approved FW-xxx
                     |
        +------------+-------------+
        |                          |
        v                          v
     Evidence                 AI Expansion
        \                          /
         \                        /
          +------ Derived Artifact
                     |
               Final Review
                     |
                     v
               Final Approved
```

## Authority is not identical to chronology

Later text is not automatically more authoritative than earlier canonical state.

A polished manuscript paragraph does not override the Content Core merely because it was generated later.

A human-approved framework does not override a later explicit human content decision; instead the framework becomes out of sync and requires revision/reapproval.

## State vs history

HARC separates:

- **current state** — compact canonical files governing current work;
- **history** — decisions, old frameworks, evidence, archived drafts.

This permits long-lived memory without forcing every agent to ingest all historical detail.

## Three routing planes

### Content plane

```text
Human content feedback
  -> if high-impact ambiguity exists: Clarification Register
  -> human resolution
  -> Decision Log
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

A stable HARC project should allow a new competent agent to answer, from repository state alone:

1. What does the human currently mean to argue?
2. What presentation does the human currently want?
3. What argument framework has the human actually approved?
4. What has the AI proposed but the human not yet accepted?
5. What evidence constrains the current claims?
6. Which high-impact uncertainties are waiting for human resolution in the Clarification Register?
7. What remains unresolved?
8. Is the current artifact synchronized with the approved state?
9. Are the Chinese canonical and English mirror files semantically synchronized?

If these questions cannot be answered without the previous chat history, the project has a persistence defect.
