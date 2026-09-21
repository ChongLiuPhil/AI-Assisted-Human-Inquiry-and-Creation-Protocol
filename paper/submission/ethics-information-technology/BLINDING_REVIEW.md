# Ethics and Information Technology — Double-Anonymous Blinding Review

**Status:** `MASKED REVIEWER ROUTE HUMAN-CONFIRMED — SUBMISSION AUTHORIZATION PENDING`  
**Authority:** AHICP-D033 + AHICP-D034  
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
  - `the protocol`
  - `the proposed Project Memory Architecture`
  - `the protocol's Project Memory`
- retains provider-neutral / repository-neutral implementation description;
- introduces no fabricated institution, author, or project provenance.

Machine checks:

- `AHICP`: 0;
- full protocol name: 0;
- direct GitHub URL: 0;
- internal Decision / Framework / Working-Memory IDs: 0.

Latest-head CI also requires:

- the masked manuscript to differ from the traceable manuscript only through a deterministic identity-masking transform, preventing a second substantive manuscript from emerging;
- identical reference sections across the two derivatives;
- absence of common mechanical masking grammar defects;
- DOCX core metadata to exclude project-owner / author identity markers.

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

Current EIT / Springer double-anonymous guidance places anonymization responsibility on authors and warns that public online material can make reverse identification easier. The masked derivative is therefore the conservative reviewer-facing route, but technical checks cannot eliminate residual discoverability created by a public project. The live guidelines / submission interface must still be rechecked immediately before actual submission.

## 5. Human route selection

AHICP-D034 completes the human route-selection gate:

1. use the masked derivative as the reviewer manuscript;
2. do not proactively supply the public GitHub repository to reviewers;
3. if the editorial process requires reviewer-visible repository / supplementary material, provide it only through an appropriate masked / anonymized route.

Already verified for the current artifact:

- reviewer-facing manuscript files omit direct author identity and internal project identifiers;
- self-citation wording does not disclose identity;
- DOCX core metadata excludes prohibited identity markers.

The live submission interface must still be checked so title-page / author metadata is not accidentally exposed to reviewers.

## 6. Governance boundary

The masked derivative and the route-selection decision:

- do not themselves authorize submission;
- do not modify `MA-FW-001`;
- do not guarantee that the journal will consider the anonymization sufficient.

Final Artifact Approval was completed separately under AHICP-D034. Formal submission remains subject to separate explicit human authorization.