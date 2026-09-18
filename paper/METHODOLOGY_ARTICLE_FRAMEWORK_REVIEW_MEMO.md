# Methodology Article — AI Framework Review Memo

> Chinese `paper/METHODOLOGY_ARTICLE_FRAMEWORK_REVIEW_MEMO.zh-CN.md` is the canonical version of this review aid; this English file is its synchronized mirror. The memo remains AI-PROPOSED in both languages.

**Status:** `AI-PROPOSED REVIEW AID`  
**Authority:** non-canonical; this file does not modify the Article Content Core and does not constitute human approval.  
**Purpose:** help the human author review the `WORKING-FRAMEWORK — REVIEW READY` before any `MA-FW-001` snapshot is created.

---

## Working Memory / Clarification mapping

This memo is now only an **analytical attachment**. Formal operational state for high-impact unresolved issues has moved to `docs/clarification-register.md`:

- former D1 -> `CLR-001`
- former D2 -> `CLR-002`
- former D3 -> `CLR-003`, `CLR-004`, `CLR-005`
- former D4 -> `CLR-006`
- former D5 -> `CLR-007`
- former D6 -> `CLR-008`

If this memo conflicts with the Clarification Register about status, severity, or human resolution, the Clarification Register governs the current operational interface. Final human decisions must still be promoted into the Decision Log and appropriate Core.

# 1. Overall assessment

The current framework is coherent enough for human review, but it should not yet be approved without explicit decisions on six points. The largest conceptual risk is not internal inconsistency; it is **overclaiming**—turning a practical governance architecture developed for HARC into a universal theory of authorship or epistemic responsibility before the argument and evidence justify that move.

A defensible first methodology article can make a strong contribution without making that stronger universal claim.

The recommended overall posture is therefore:

> **Strong about the architecture; moderate about the universal philosophical conclusions.**

HARC can confidently propose a repository-centered method for persistent, auditable, human-governed research collaboration while treating broader claims about the essence of authorship, cognition, or responsibility as open philosophical questions.

---

# 2. D1 — Central responsibility terminology

## Option A — `epistemic responsibility` / 认识责任

### Advantages

- directly concerns what a researcher is justified in accepting, asserting, approving, and taking responsibility for;
- connects naturally to evidence, inference, testimony/dependence, and scholarly accountability;
- gives the methodology article a clear philosophical center.

### Risks

- narrower than all forms of cognitive agency;
- may sound as if the article already possesses a settled theory of epistemic responsibility.

## Option B — `cognitive responsibility` / 认知责任

### Advantages

- broader and easier to connect to task allocation, cognition, memory, planning, and AI assistance.

### Risks

- less standard and conceptually less precise;
- may blur performance of cognitive work with responsibility for claims.

## Option C — layered distinction

Use:

- **cognitive labor** for search, synthesis, drafting, checking, formalization, formatting, etc.;
- **epistemic responsibility** for understanding, accepting, rejecting, authorizing, and answering for important claims/inferences.

### AI recommendation

`AI-PROPOSED DEFAULT: Option C.`

This gives the article the cleanest distinction:

> **Cognitive labor can be extensively delegated; epistemic responsibility must remain explicitly governed.**

This formulation does not imply that every factual detail must be independently re-derived by the human. It instead creates the problem HARC is designed to govern: where and how responsibility is anchored when cognitive labor is distributed.

---

# 3. D2 — Strength of the Framework Responsibility Thesis

## Strong version

> Human approval of the framework is generally the center of substantive intellectual authorship in AI-assisted long-form work.

### Advantages

- philosophically bold;
- potentially distinctive.

### Risks

- claims too much too early;
- different disciplines and genres may distribute intellectual responsibility differently;
- a high-level framework can omit decisive factual, mathematical, methodological, or interpretive errors;
- the concept of authorship is institutionally and philosophically contested.

## Moderate version

> Within HARC, an explicitly human-approved framework functions as the primary substantive intellectual responsibility anchor for long-form AI-assisted collaboration.

### Advantages

- directly supported by the protocol architecture;
- preserves the founder's central insight about human responsibility for the compressed argument structure;
- does not pretend to settle the general metaphysics or ethics of authorship.

### AI recommendation

`AI-PROPOSED DEFAULT: Moderate version.`

The article can later ask whether the HARC model supports a more general theory of authorship, but it should not require that stronger conclusion for the protocol to succeed.

Suggested formulation:

> **HARC treats framework approval not as a complete theory of authorship, but as a primary responsibility anchor: a versioned point at which the human explicitly accepts the work's central claims, inferential architecture, distinctions, scope, and structural commitments.**

---

# 4. D3 — AI-proposed terminology

## A. `semantic version control`

### Assessment

This term is useful because ordinary Git records textual change, while HARC additionally records whether a change is a human decision, AI proposal, evidence constraint, temporary default, or approved framework revision.

### Risk

Readers may assume it is an established technical field or formal standard.

### AI recommendation

`ACCEPT AS HARC COINAGE / WORKING TERM`, with explicit definition and no claim that the term is established literature.

Suggested wording:

> HARC uses **semantic version control** as a project term for versioning not only text, but also the status and authority of meanings, decisions, proposals, and approvals.

---

## B. `generation–verification asymmetry`

### Assessment

Useful as an intuitive problem statement: AI-assisted generation can scale more quickly than human review.

### Risk

Without empirical measurement, calling it a general “asymmetry” may sound like an established quantitative law.

### AI recommendation

`KEEP AS A HEURISTIC LABEL`, not as a demonstrated empirical theorem.

Suggested wording:

> The article calls this practical pressure the **generation–verification asymmetry**: a working label for the fact that AI can make production and transformation of candidate research content much cheaper than careful human understanding and verification.

---

## C. `responsibility concentration`

### Assessment

Captures the founder's idea that human attention should focus on the compressed framework rather than repeatedly reviewing every intermediate expansion.

### Risk

“Concentration” may be misunderstood as permission to ignore downstream accuracy, and may conflict rhetorically with the separate Final Artifact Approval Gate.

### AI recommendation

`REPLACE OR DEMOTE.`

Preferred alternatives:

- **epistemic responsibility anchoring**;
- **responsibility architecture**;
- **high-leverage human review**.

The first is especially compatible with the Approved Framework concept.

---

# 5. D4 — Extended/distributed cognition connection

## Option A — central theoretical grounding

HARC is presented as an application or extension of extended/distributed cognition.

### Risk

This unnecessarily makes HARC depend on controversial theses in philosophy of mind and cognitive science.

## Option B — secondary conceptual comparison

The literature helps explain why cognition can be scaffolded by external artifacts and distributed across people/tools, while HARC remains methodologically independent of stronger metaphysical conclusions.

## Option C — minimal background

Mention only briefly.

### AI recommendation

`AI-PROPOSED DEFAULT: Option B.`

This provides theoretical depth without making HARC hostage to whether the extended-mind thesis is true.

Recommended position:

> HARC is compatible with externalist and distributed approaches to cognition, but requires only the weaker practical claim that explicit external representations can preserve and coordinate research state.

---

# 6. D5 — Empirical validation program

## Option A — core contribution

The article presents HARC together with a formal experimental research program.

### Advantage

Makes HARC unusually testable.

### Risk

The current project does not yet contain empirical results, so the article may promise more than it demonstrates.

## Option B — future research agenda

The main article is methodological/normative; empirical tests are proposed as falsifiable or operational follow-up work.

## Option C — omit

Keep the article purely conceptual.

### AI recommendation

`AI-PROPOSED DEFAULT: Option B.`

This preserves the important claim that HARC should be testable without pretending that its effectiveness is already established.

Recommended wording:

> HARC's practical claims generate an empirical research agenda rather than already established performance results.

---

# 7. D6 — Disciplinary positioning

## Philosophy of technology / epistemology

Best if the article focuses on responsibility, epistemic dependence, extended cognition, authorship, and delegation.

## Research methodology

Best if the article focuses on workflow architecture, validity, auditability, and reproducible research practice.

## Scholarly communication / research integrity

Best if the article focuses on authorship policies, provenance, contribution disclosure, accountability, and publication governance.

## Interdisciplinary AI governance

Broadest audience, but risks losing conceptual precision.

### AI recommendation

`AI-PROPOSED DEFAULT: interdisciplinary methodology with a philosophy-of-technology core.`

Practical implication for the first draft:

- lead with the methodological problem;
- make epistemic responsibility the conceptual center;
- use authorship/research-integrity rules as constraints rather than the article's sole subject;
- retain an operational protocol section substantial enough that the paper cannot be reduced to abstract ethics.

Target venue can be chosen later after the intellectual framework stabilizes.

---

# 8. Recommended approval candidate

If the human author accepts the above defaults, the first approved framework could be built around the following compressed thesis:

> **AI-assisted research should be organized around explicit, version-controlled research state that separates human commitments, AI representations, evidence constraints, approval states, and derived expression. Cognitive labor may be extensively delegated, but epistemic responsibility must remain human-governed through identifiable high-leverage decisions. In HARC, a human-approved intellectual framework functions as a primary responsibility anchor for long-form collaboration, while a separate final-artifact approval gate preserves public release accountability.**

`AI-PROPOSED SYNTHESIS — NOT HUMAN APPROVED.`

This synthesis is deliberately narrower than a general theory of authorship. It is strong enough to motivate the protocol while leaving room for later philosophical development.

---

# 9. Approval discipline

Human review may result in:

- acceptance of the entire framework;
- acceptance with revisions;
- rejection of individual theses/terms;
- promotion of an AI-proposed term into human-approved state;
- demotion of a thesis to future research;
- restructuring of the article.

Only an explicit whole-framework approval should trigger creation of `MA-FW-001`. Agreement with one or more recommendations in this memo is not automatically whole-framework approval.
