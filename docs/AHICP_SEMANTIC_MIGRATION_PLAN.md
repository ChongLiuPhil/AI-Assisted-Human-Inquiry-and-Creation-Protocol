# HARC → AHICP Semantic Migration Plan

**Status:** Working migration plan  
**Target version:** v0.3.0-draft  
**Normative direction:** Human-led, AI-assisted, repository-grounded.

## 1. Purpose

This migration is not a simple rename.

The former **Human–AI Research Collaboration Protocol (HARC)** was developed primarily around sustained research collaboration. The new formal name is:

> **AI-Assisted Human Inquiry and Creation Protocol (AHICP)**

with the fixed subtitle:

> **A protocol for human-led inquiry, research, reasoning, writing, and creation with AI assistance.**

The migration aligns the name, scope, and existing governance architecture while avoiding language that could imply that AI is a cognitive subject, an intellectual-labor subject, or a bearer of ultimate responsibility parallel to the human.

## 2. Core architecture retained

The following mature design elements remain:

- repository-backed persistent project state;
- chat is not the durable source of truth;
- Content / Form / Protocol routing;
- Content Core / Form Core / Decision Log;
- Working Memory;
- Working vs. Approved Framework;
- Framework Approval and Final Artifact Approval;
- AI proposal ≠ human commitment;
- evidence constraints;
- zero-context onboarding;
- cross-agent handoff;
- audit discipline;
- Chinese-canonical / English-mirror bilingual governance;
- humans remain bearers of purpose, judgment, approval, and ultimate responsibility.

## 3. Scope generalization

Research-specific wording that currently carries a general protocol function should be reviewed and generalized where appropriate:

- `research project` → `inquiry or creation project` / `project`;
- `research state` → `project state`;
- `research memory` → `project memory` or `inquiry-and-creation memory`;
- `research content` → `substantive content`, `project content`, or remain research-specific depending on context;
- `research collaboration` no longer serves as the protocol's top-level category.

Text that genuinely concerns research, evidence, scholarly articles, academic policy, or research integrity should remain research-specific.

## 4. Normative status of AI

AHICP uses this model:

```text
Human
  ├─ purpose
  ├─ inquiry
  ├─ reasoning
  ├─ judgment
  ├─ creation
  ├─ approval
  └─ responsibility
          ▲
          │
     AI assistance
          │
  ├─ retrieve
  ├─ compare
  ├─ structure
  ├─ propose
  ├─ draft
  ├─ verify
  ├─ transform
  └─ maintain project state
```

Normative text must not use ordinary collaboration language in a way that makes AI appear to be a symmetric cognitive subject, authorial responsibility bearer, or ultimate bearer of knowledge responsibility.

## 5. Generalized three-layer model

The former logic:

`Human Authorial Core -> Current Framework -> Derived Artifact`

is retained but generalized for multiple project types:

- Layer 1 — **Human Intentional / Authorial Core**
- Layer 2 — **Operational Framework**
- Layer 3 — **Derived Artifact**

Research projects may continue to use an Argument Map; creative projects may use an appropriate structural representation.

## 6. Migration phases

### Phase A — semantic entry points
- bilingual README;
- bilingual Specification;
- bilingual AGENTS contract;
- protocol core / decision state;
- methodology article naming and scope statements.

### Phase B — control plane
- `HARC_MANIFEST.yaml` → `AHICP_MANIFEST.yaml`;
- `HARC_CONTEXT_INTERFACE.yaml` → `AHICP_CONTEXT_INTERFACE.yaml`;
- bootstrap and onboarding references;
- downstream template references.

Legacy filenames may temporarily remain as compatibility pointers but must not become a second normative truth source.

### Phase C — repository-wide semantic audit
Classify each occurrence as:
- generalize;
- retain as research-specific;
- preserve as historical record;
- update as a legacy identifier.

### Phase D — parity and takeover validation
Run:
- bilingual parity audit;
- zero-context onboarding test;
- semantic migration audit;
- post-migration repair audit.

## 7. Versioning

The recommended transition is:

> **HARC v0.2.x → AHICP v0.3.0-draft**

The core governance architecture remains, while scope and normative language are materially expanded.

## 8. Boundary with PPF

AHICP governs AI assistance in human inquiry and creation. It does not define publishing infrastructure.

The **Personal Publishing Framework (PPF)** governs source / build / publish / release / archive.

Projects may adopt:

```text
AHICP only
PPF only
AHICP + PPF
```

The two projects should reference rather than duplicate each other's rules.
