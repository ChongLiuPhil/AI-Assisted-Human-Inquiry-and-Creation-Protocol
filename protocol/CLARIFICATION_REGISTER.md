# Critical Clarification Register Protocol

> **Language:** Chinese canonical: `CLARIFICATION_REGISTER.zh-CN.md`; this English file is the synchronized mirror.

## 1. Purpose

HARC adds an explicit **Critical Clarification Layer** between human-authoritative state and the AI-maintained operational argument structure.

It handles cases where:

- the AI has important uncertainty about the human author's intended meaning;
- two or more plausible interpretations would materially change a core thesis or argument structure;
- a key concept, term, translation, or bilingual correspondence remains unconfirmed;
- scope, qualification, causal/logical relation, or section function is ambiguous;
- an implementation choice could harden an unconfirmed interpretation into the Argument Map or artifact;
- getting the issue wrong would cause substantial downstream work to rest on a mistaken understanding.

The purpose is not to collect every minor question, but to promote **high-impact uncertainty** from chat into an explicit object for human review.

## 2. Architectural position

The Clarification Register is a **Layer 1.5 bridge**:

```text
Layer 1 — Human-authoritative state
  Content Core / Form Core / Protocol Core / Decision Log
                    ^
                    |
            human resolution
                    |
Layer 1.5 — Critical Clarification Register
                    ^
                    |
       AI detects high-impact ambiguity
                    |
Layer 2 — Working Argument Map / operational structure
                    |
Layer 3 — Derived Artifact
```

Open clarification entries are **not human-approved claims**.

Their role is to prevent the AI from silently selecting one interpretation and allowing it to propagate into Layers 2 or 3.

## 3. When an entry is required

An AI Agent **MUST** create or update a clarification entry when both conditions hold:

1. the uncertainty is non-trivial: at least two reasonable interpretations, terminology choices, translations, scope readings, or structural readings exist; and
2. the impact is high: different choices could materially change a core thesis, major inferential relation, key concept, framework structure, reader understanding, approval state, or long-term project continuity.

Typical triggers include ambiguous meanings, multiple technical/philosophical senses, non-equivalent bilingual terminology, strong-vs-weak readings of a claim, unclear scope conditions, unclear section functions, possible tension between new human feedback and older state, or any interpretive choice that would affect the whole work.

## 4. The AI must surface uncertainty proactively

The Agent should not wait for the human to notice ambiguity.

A **Clarification Scan** SHOULD occur before:

- a new major research phase;
- large-scale Argument Map restructuring;
- Framework Approval;
- propagating a new concept or term across the work;
- producing a formal translation from the author's primary language;
- large chapter expansion;
- incorporating evidence that may change a central interpretation;
- Final Artifact Review.

High-impact uncertainty should be registered and raised with the human before silent propagation.

## 5. Blocking vs non-blocking

Each entry should be marked:

- `BLOCKING` — related structural propagation or large-scale expansion should pause until resolved;
- `NON-BLOCKING` — unrelated work may continue, but no candidate answer may be represented as the human's position.

## 6. Recommended entry schema

Each entry should include:

- **ID:** `CLR-001`
- **Status:** `OPEN / HUMAN-CONFIRMED / HUMAN-CORRECTED / DEFERRED / SUPERSEDED`
- **Severity:** `BLOCKING / NON-BLOCKING`
- **Category:** `CONCEPT / CLAIM / INFERENCE / SCOPE / STRUCTURE / TERMINOLOGY / TRANSLATION / FORM / PROTOCOL / EVIDENCE`
- **Trigger/source**
- **Uncertain point**
- **Candidate interpretations**
- **Why it matters**
- **Affected files/claims/sections**
- **AI recommendation** (optional, explicitly `AI-PROPOSED`)
- **Question for the human**
- **Human resolution**
- **Propagation targets**
- **Resolution date / decision ID**

## 7. Key concepts and bilingual terminology

The Register is especially appropriate for key definitions, primary-language/English mappings, overly strong or weak translations, whether to retain source-language terms, cross-section terminology consistency, and translations that may alter philosophical, legal, statistical, technical, or methodological meaning.

After human confirmation:

- research-semantic concept/term decisions go to Content Core;
- primarily presentational/translation conventions go to Form Core;
- durable project-level decisions go to Decision Log;
- the Working Argument Map and derived artifact are then synchronized.

## 8. Resolution Promotion Rule

A resolved clarification is not complete merely because its status changes.

The required propagation is:

`Human resolution -> Decision Log -> appropriate Core -> Argument Map -> Derived Artifact`

The Clarification Register is a decision interface and audit trace, not the final normative truth source.

Resolved entries may remain to record what was uncertain and how it was resolved, while the authoritative answer lives in the appropriate Core.

## 9. Difference from the Decision Log

- **Clarification Register:** what high-impact questions currently require human judgment and how they are resolved.
- **Decision Log:** what durable human decisions were ultimately made.

The former governs uncertainty; the latter preserves decision history.

## 10. Difference from the Working Argument Map

The Argument Map may mention unresolved issues but should not carry the full clarification-governance burden.

The Clarification Register adds severity, provenance, candidate interpretations, human resolution state, propagation targets, bilingual/terminology decisions, and an audit trail. The Argument Map may simply reference relevant `CLR-xxx` entries.

## 11. Completion condition

A high-impact clarification closes only when:

1. the human explicitly confirms, corrects, defers, or rejects;
2. the resolution is recorded in the Register;
3. the durable decision is recorded in the Decision Log;
4. the appropriate Core is updated;
5. the Working Argument Map is synchronized;
6. affected derived artifacts are synchronized or explicitly marked pending;
7. Chinese/English parity is complete.

## 12. Principle

> **When uncertainty may change meaning, the AI's job is not to guess more confidently; it is to promote the uncertainty into an explicit object of human governance.**
