# Ethics and Information Technology — Submission Derivative Package

**Status:** `FINAL ARTIFACT APPROVED — SUBMISSION AUTHORIZATION PENDING`  
**Primary target:** *Ethics and Information Technology*  
**Approved Framework baseline:** `MA-FW-001`  
**Final Artifact Approval:** `AHICP-D034`  
**Preparation authorization:** `AHICP-D033`

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
- citation ↔ reference-list consistency: `VERIFIED — 18/18 MAPPINGS + UNMAPPED-YEAR GUARD / EIT CI PASS`;
- masked manuscript: prepared; `AHICP`, full protocol name, direct GitHub URL, and internal IDs removed;
- traceable DOCX candidate: generated / structural validation PASS / 20-page visual QA PASS;
- masked DOCX candidate: generated / structural validation PASS / 20-page visual QA PASS;
- automatic PAGE field, non-splitting table rows, table-caption pagination, and anonymous metadata gates: PASS.

## Important anonymization risk

The distinctive protocol name `AHICP` remains scientifically necessary to identify the object under discussion, but it may permit search-based deanonymization because public project materials exist.

This risk is **not resolved by deleting author names alone**.

AHICP-D034 records the human route choice:

1. use `MANUSCRIPT_BLINDED_MASKED.md` as the reviewer manuscript;
2. do not proactively provide the public GitHub repository to reviewers;
3. if the editorial process requires reviewer-visible repository / supplementary material, provide it only through an appropriate masked / anonymized route.

Residual discoverability risk remains acknowledged and must not be represented as eliminated.

Do not fabricate anonymity by misdescribing project provenance.

## Governance boundary

Final Artifact Approval is complete under AHICP-D034. This package is still **not submission-authorized**: formal submission, publication, or release requires separate explicit human authorization, and submission-time factual metadata plus the live-interface / dynamic-policy final recheck remain pending.
