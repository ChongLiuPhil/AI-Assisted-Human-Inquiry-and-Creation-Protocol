# HARC Session Context Bootstrap

> **Language:** Chinese canonical: `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`; this English file is the synchronized mirror.

## 0. Purpose

This file creates a second layer of protection:

1. the **GitHub repository** stores durable, auditable project state;
2. the **current AI conversation context** contains a compressed operating contract regenerated from repository state.

After repository onboarding, a replacement AI Agent should explicitly write a **HARC Active Session Contract** into its own current reply so that the key rules re-enter the active conversation context.

This is not a true platform-level `system prompt` and must not be represented as overriding platform system, developer, or safety instructions.

Correct precedence:

`Platform system/developer rules > HARC Session Contract > ordinary task-level AI defaults`

The HARC Session Contract is a **project-level session operating contract**.

## 1. When to load

Load or reload the Session Contract when:

- a new AI Agent first takes over;
- a new conversation begins;
- prior conversation context is unavailable;
- the Onboarding Handshake completes;
- a major human decision changes Core / Clarification / Framework state;
- before Framework Approval;
- before Final Artifact Review;
- the Agent suspects important HARC state has fallen out of active context.

## 2. Loading action

After required reading, the Agent must include in its first Onboarding Report a block headed:

`HARC ACTIVE SESSION CONTRACT — LOADED`

The Agent should compress the following current state into its own reply.

### A. Authority

- repository state outranks prior chat memory;
- Chinese canonical outranks English mirror;
- human-confirmed Core outranks AI proposals;
- Approved Framework outranks Working Argument Map;
- platform system/developer instructions remain higher priority than HARC.

### B. Current project status

- current human research purpose;
- key human Content / Form / Protocol commitments;
- current Blocking Clarifications;
- Working Framework status;
- latest Approved Framework if any;
- current Artifact status;
- current Final Approval status.

### C. Required behavior

- high-impact uncertainty -> Clarification Register;
- explicit human decision -> Decision Log -> appropriate Core -> downstream propagation;
- no silent promotion of AI proposals;
- no Framework Approval while blocking clarification remains unresolved unless explicitly deferred by the human;
- substantive Chinese edits -> English mirror in the same work cycle;
- derived artifacts remain provisional until the required approval gate.

### D. Current task constraint

State for the current request:

- CONTENT / FORM / PROTOCOL classification;
- whether clarification is triggered;
- which files require upstream-first updates;
- which actions are currently blocked.

## 3. Recommended echo format

```text
HARC ACTIVE SESSION CONTRACT — LOADED

Authority:
- Repository state > prior chat memory
- Chinese canonical > English mirror
- Human-confirmed Core > AI proposals
- Approved Framework > Working Argument Map
- Platform system/developer instructions > HARC project contract

Blocking Clarifications:
- CLR-...

Framework:
- Working: ...
- Approved: ...

Artifact:
- Status: ...

Current task:
- Classification: CONTENT / FORM / PROTOCOL
- Upstream files: ...
- Blocked actions: ...

Operational invariants:
- High-impact ambiguity -> Clarification Register
- Human decision -> Decision Log -> Core -> Argument Map -> Artifact
- Chinese edit -> English mirror
```

Keep this compact; do not copy the entire repository.

## 4. Why echoing matters

Reading a file does not guarantee that its most important rules remain salient throughout a long conversation.

Having the Agent rewrite a compressed Session Contract into its own reply:

1. places the rules into the active conversation context;
2. lets the human verify the reconstruction;
3. creates an explicit reference against which later Agent actions can be checked.

## 5. Context Refresh

The Session Contract should not appear only once.

Trigger a short `HARC CONTEXT REFRESH` after:

- resolution of a Blocking Clarification;
- substantive Core changes;
- creation of a new Approved Framework;
- transition from framework work to large-scale Artifact expansion;
- transition from Chinese canonical to formal English release preparation;
- Final Artifact Review;
- any long conversation where the Agent is unsure whether the earlier contract remains in active context.

A refresh need only update changed fields.

## 6. Do not fabricate hidden memory

The Agent must not claim that it:

- installed HARC into the platform's true system prompt;
- permanently changed model weights;
- changed platform-level memory;
- will automatically remember HARC in a new conversation.

If a platform exposes user-controlled custom instructions, project instructions, or pinned context, those may be used additionally, but that is a platform capability rather than something HARC can guarantee.

HARC can guarantee only:

> **The repository provides recoverable durable state; the Agent explicitly echoes key state back into the visible session context.**

## 7. If session context is lost

If the Agent suspects the conversation has been compressed, truncated, migrated, or lost:

1. stop relying on remembered state;
2. reread `HARC_MANIFEST.yaml`;
3. reread relevant canonical state;
4. output `HARC CONTEXT REFRESH`;
5. resume substantive work.

## 8. Principle

> **Repository memory provides persistence; Session Context Bootstrap restores salience.**
