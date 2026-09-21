# Ethics and Information Technology — Double-Anonymous Blinding Review

**Status:** `MASKED DERIVATIVE PREPARED — HUMAN / EDITORIAL CONFIRMATION PENDING`  
**Authority:** AHICP-D033  
**Objects:**
- `MANUSCRIPT_BLINDED.md` — baseline blinded version with direct identity removed but protocol name retained;
- `MANUSCRIPT_BLINDED_MASKED.md` — masked derivative for double-anonymous review.

## 1. Risk source

The baseline blinded manuscript already removes:

- author names;
- affiliations / contact information;
- GitHub URLs;
- internal Decision IDs;
- Framework IDs;
- Working Memory IDs;
- development-status metadata.

However, it still contains many occurrences of `AHICP` / the protocol's full name. Because the protocol has public project materials, the distinctive name itself may allow an ordinary search to identify the project and author. Removing author names alone is therefore not a sufficient double-anonymous mitigation.

## 2. Current mitigation

`MANUSCRIPT_BLINDED_MASKED.md`:

- preserves the same title, argument structure, citations, references, AI-use disclosure, and Data Availability Statement;
- does not alter `MA-FW-001`;
- does not alter the canonical article;
- replaces the protocol name / `AHICP` with neutral formulations such as:
  - `the proposed protocol`
  - `the protocol`
  - `the proposed Project Memory Architecture`
- retains provider-neutral / repository-neutral implementation description;
- introduces no fabricated institution, author, or project provenance.

Machine checks:

- `AHICP`: 0;
- full protocol name: 0;
- direct GitHub URL: 0;
- internal Decision / Framework / Working-Memory IDs: 0.

## 3. Recommended submission route

Current recommendation:

> **Unless the editorial office instructs otherwise, use the masked derivative as the double-anonymous reviewer manuscript.**

Retain the unmasked blinded version as:

- the project-traceable baseline;
- an alternative if the editor explicitly permits the public protocol name;
- the source for restoring the proper name after deblinding / review.

## 4. Residual risk

The masked derivative materially reduces the direct “search the protocol name and find the author” risk, but it cannot guarantee perfect anonymity.

Residual discoverability may remain through:

- title or distinctive phrase similarity to public material;
- public chronology;
- pre-existing public repository / webpage;
- unusual combinations of concepts.

The project must therefore not claim that anonymity is complete.

## 5. Human gate before submission

Before actual submission, complete one of the following:

1. the human explicitly selects the masked derivative as the reviewer manuscript; or
2. the editorial office explicitly confirms that retaining the public protocol name is acceptable under double-anonymous review; or
3. another masked-material / supplementary-material route is adopted following editorial guidance.

Also verify that:

- reviewer-visible supplementary / repository material does not directly reveal identity;
- submission-system title-page / author metadata is not exposed in the reviewer manuscript;
- self-citation wording does not disclose identity.

## 6. Governance boundary

Creating the masked derivative:

- is not Final Artifact Approval;
- is not submission authorization;
- does not modify `MA-FW-001`;
- does not guarantee that the journal will consider the anonymization sufficient.

It is a venue-specific derivative prepared for double-anonymous review.