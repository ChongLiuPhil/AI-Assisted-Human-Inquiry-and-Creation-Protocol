# Ethics and Information Technology — Submission Derivative Package

**Status:** `VENUE-SPECIFIC DERIVATIVE — FINAL ARTIFACT APPROVAL PENDING`  
**Primary target:** *Ethics and Information Technology*  
**Approved Framework baseline:** `MA-FW-001`  
**Authorization:** `AHICP-D033`

This directory contains venue-specific derivatives and submission-preparation materials. It does **not** replace the canonical bilingual article.

## Files

- `MANUSCRIPT_BLINDED.md` — traceable blinded baseline: direct identity removed, public protocol name retained.
- `MANUSCRIPT_BLINDED_MASKED.md` — masked double-anonymous reviewer derivative with protocol name removed.
- `BLINDING_REVIEW.md` / `.zh-CN.md` — anonymization-risk analysis and reviewer-manuscript recommendation.
- `SUBMISSION_CHECKLIST.md` / `.zh-CN.md` — venue-specific compliance checklist.
- `AI_USE_DISCLOSURE.md` / `.zh-CN.md` — disclosure wording and governance notes.
- `TITLE_PAGE_METADATA_TEMPLATE.md` — author/title-page/submission-system metadata template; no identity is prefilled.
- `COVER_LETTER_DRAFT.md` — non-submission-authorized cover-letter draft with required human-confirmation placeholders.
- `CITATION_AUDIT.md` — publication-status / metadata / policy-source audit for the venue derivative.
- `tools/build_eit_docx.py` — reproducible DOCX builder used by EIT Submission CI; generated DOCX remains a build candidate until visual QA.

## Current machine-checked manuscript metrics

- abstract: 185 words;
- content: approximately 5,367 words under the repository validator's counting method;
- keywords: 6;
- maximum displayed heading level: 3;
- internal Decision / Framework / Working-Memory IDs in blinded manuscript: none;
- direct GitHub URL in blinded manuscript: none;
- empirical-results claim: none;
- AI-use disclosure: present;
- Data Availability Statement: present;
- citation / publication-status audit: completed for current reference set;
- citation ↔ reference-list bidirectional consistency: `VERIFIED — 18/18 MAPPINGS / EIT CI PASS`;
- masked manuscript: prepared; `AHICP`, full protocol name, direct GitHub URL, and internal IDs removed;
- traceable DOCX build candidate: generated / structural validation PASS / workflow artifact uploaded;
- masked DOCX build candidate: generated / structural validation PASS / workflow artifact uploaded;
- CI-generated DOCX files are not final until visual QA.

## Important anonymization risk

The distinctive protocol name `AHICP` remains scientifically necessary to identify the object under discussion, but it may permit search-based deanonymization because public project materials exist.

This risk is **not resolved by deleting author names alone**.

A masked reviewer derivative is now prepared. Before actual submission, the human author must still choose one of the following, ideally after checking the live submission interface or seeking editorial clarification:

1. use `MANUSCRIPT_BLINDED_MASKED.md` as the reviewer manuscript (current recommendation);
2. retain the protocol name only if the editorial office explicitly accepts the residual discoverability risk;
3. follow another masked supplementary/repository route requested by the editorial office.

Do not fabricate anonymity by misdescribing project provenance.

## Governance boundary

Creating or merging this package is not Final Artifact Approval and is not authorization to submit, publish, or release a manuscript through the journal system.
