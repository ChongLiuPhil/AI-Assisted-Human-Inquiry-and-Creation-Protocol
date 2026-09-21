# Citation and Policy-Source Audit — Ethics and Information Technology Submission Derivative

**Status:** `AUDITED — FINAL LIVE-POLICY RECHECK STILL REQUIRED`  
**Audit date:** 2026-09-22  
**Object:** `MANUSCRIPT_BLINDED.md`  
**Scope:** bibliographic metadata, publication status, DOI / canonical source, and distinction between scholarly references and dynamic policy sources.

This audit applies only to the venue-specific submission derivative. It does not replace the project's canonical evidence layer.

## Status meanings

- `VERIFIED-PUBLISHED` — publication status and core bibliographic metadata were confirmed from an authoritative publisher / society / proceedings source.
- `VERIFIED-STANDARD` — formal standard status and date were confirmed from the standards body.
- `VERIFIED-BIBLIOGRAPHIC` — book or legacy bibliographic metadata were confirmed from a reliable bibliographic record; final formatting may still be normalized.
- `CURRENT-POLICY-SOURCE` — live institutional/publisher policy page checked on 2026-09-22; must be checked again immediately before submission because policy text can change.

## Scholarly / standards references

| Reference | Audit status | Verification note |
|---|---|---|
| Bian et al. (2026), *RealMem* | `VERIFIED-PUBLISHED` | ACL Anthology confirms Findings of ACL 2026, pp. 14349–14365, DOI 10.18653/v1/2026.findings-acl.703. |
| Clark & Chalmers (1998), “The Extended Mind” | `VERIFIED-PUBLISHED` | Oxford Academic confirms *Analysis* 58(1), pp. 7–19, DOI 10.1093/analys/58.1.7. |
| Hardwig (1985), “Epistemic Dependence” | `VERIFIED-PUBLISHED` | JSTOR issue record confirms *The Journal of Philosophy* 82(7), pp. 335–349, DOI 10.2307/2026523. |
| Hutchins (1995), *Cognition in the Wild* | `VERIFIED-BIBLIOGRAPHIC` | MIT Press / bibliographic records confirm Edwin Hutchins, MIT Press, 1995; current project DOI retained. |
| Lee (1992), “Design Rationale Management Research” | `VERIFIED-PUBLISHED` | Cambridge Core confirms *The Knowledge Engineering Review* 7(4), pp. 363–366, DOI 10.1017/S0269888900006470. |
| Mariano & Awazu (2024), “Managing large-scale projects…” | `VERIFIED-PUBLISHED` | Elsevier / ScienceDirect confirms *International Journal of Project Management* 42(2), article 102573, DOI 10.1016/j.ijproman.2024.102573. |
| Parasuraman & Riley (1997), “Humans and Automation…” | `VERIFIED-PUBLISHED` | SAGE / *Human Factors* confirms 39(2), pp. 230–253, DOI 10.1518/001872097778543886. |
| Park et al. (2023), “Generative Agents…” | `VERIFIED-PUBLISHED` | ACM Digital Library confirms UIST 2023, Article 2, pp. 1–22, DOI 10.1145/3586183.3606763. |
| Singh, Cobbe & Norval (2019), “Decision Provenance…” | `VERIFIED-PUBLISHED` | Cambridge repository metadata identifies *IEEE Access* 7 and publisher DOI 10.1109/ACCESS.2018.2887201; current page range retained from publisher metadata used by the project. |
| Tan et al. (2025), *MemBench* | `VERIFIED-PUBLISHED` | ACL Anthology confirms Findings of ACL 2025, pp. 19336–19352, DOI 10.18653/v1/2025.findings-acl.989. |
| W3C (2013), *PROV-DM* | `VERIFIED-STANDARD` | W3C confirms Recommendation status dated 30 April 2013; manuscript reference normalized accordingly. |
| Walsh & Ungson (1991), “Organizational Memory” | `VERIFIED-PUBLISHED` | Academy of Management confirms *Academy of Management Review* 16(1), pp. 57–91, DOI 10.5465/amr.1991.4278992. |
| Weinreich & Groher (2016), SAKM systematic review | `VERIFIED-PUBLISHED` | Elsevier / ScienceDirect confirms *Information and Software Technology* 80, pp. 265–286, DOI 10.1016/j.infsof.2016.09.007. |
| Weiser & Morrison (1998), “Project Memory…” | `VERIFIED-PUBLISHED` | Taylor & Francis confirms *Journal of Management Information Systems* 14(4), pp. 149–166, DOI 10.1080/07421222.1998.11518189. |
| Wu et al. (2025), *LongMemEval* | `VERIFIED-PUBLISHED` | ICLR proceedings confirm publication as a conference paper at ICLR 2025; manuscript now cites the proceedings page. |
| Zhang et al. (2025), Agent-memory survey | `VERIFIED-PUBLISHED` | ACM Digital Library confirms *ACM Transactions on Information Systems* 43(6), Article 155, DOI 10.1145/3748302, published 10 September 2025. |

## Dynamic policy / responsibility sources

| Source | Audit status | Submission rule |
|---|---|---|
| International Committee of Medical Journal Editors (ICMJE), “Defining the Role of Authors and Contributors” | `CURRENT-POLICY-SOURCE` | Current page checked 2026-09-22. It continues to link authorship to approval/accountability and explicitly addresses AI-assisted technology; current guidance also emphasizes transparent disclosure of AI use. Recheck immediately before submission. |
| Nature Portfolio, editorial / AI policies | `CURRENT-POLICY-SOURCE` | Current policy page checked 2026-09-22. Used only as a comparative boundary case, not as the target journal's governing policy; human accountability and transparent AI-use expectations remain consistent with the manuscript's bounded claim. Recheck if retained at submission. |

## Submission-derivative cleanup decisions

- `MemGPT` was removed from the venue derivative because the cited version remained a preprint and the target-journal guideline asks the reference list to contain works cited in the text that are published or accepted. It remains in the canonical evidence infrastructure.
- Uncited evidence-only references (including CRediT / UNESCO / the previously uncited Nature Methods item) were removed from the venue derivative.
- W3C PROV-DM was normalized to its formal Recommendation status and date.
- LongMemEval was normalized to its ICLR 2025 proceedings page.
- ICMJE and Nature Portfolio entries were expanded with canonical live URLs and are explicitly treated as dynamic policy sources.

## Remaining citation tasks before Final Artifact Approval

- [x] Core scholarly references checked for publication status and core metadata.
- [x] Major DOI / proceedings identifiers checked.
- [x] Preprint-only MemGPT removed from venue derivative.
- [x] Dynamic policy sources separated from scholarly evidence.
- [x] Automated/manual reference consistency completed for the submission derivative; latest-head EIT CI verifies the explicit 18-entry citation ↔ reference mapping and rejects unmapped year-bearing citation material.
- [x] ICMJE / Nature policy pages rechecked on 2026-09-22; the manuscript's comparative policy claim remains supported.
- [x] Final traceable / masked Word/docx candidates re-rendered and reviewed page-by-page after the latest reference/table-formatting changes (20 pages + 20 pages).
- [ ] Live EIT submission interface plus dynamic policy pages rechecked immediately before actual submission.

**Conclusion:** no known citation or policy-source blocker currently requires changing `MA-FW-001` or the EIT manuscript. The remaining policy task is the at-submission live-interface / dynamic-policy recheck.
