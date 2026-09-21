from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "paper/submission/ethics-information-technology"

MANUSCRIPT = BASE / "MANUSCRIPT_BLINDED.md"
MASKED_MANUSCRIPT = BASE / "MANUSCRIPT_BLINDED_MASKED.md"
BLINDING_EN = BASE / "BLINDING_REVIEW.md"
BLINDING_ZH = BASE / "BLINDING_REVIEW.zh-CN.md"
README = BASE / "README.md"
CHECK_EN = BASE / "SUBMISSION_CHECKLIST.md"
CHECK_ZH = BASE / "SUBMISSION_CHECKLIST.zh-CN.md"
AI_EN = BASE / "AI_USE_DISCLOSURE.md"
AI_ZH = BASE / "AI_USE_DISCLOSURE.zh-CN.md"
CITATION_AUDIT = BASE / "CITATION_AUDIT.md"
TITLE_META = BASE / "TITLE_PAGE_METADATA_TEMPLATE.md"
COVER = BASE / "COVER_LETTER_DRAFT.md"

FORM_EN = ROOT / "paper/METHODOLOGY_ARTICLE_FORM_CORE.md"
FORM_ZH = ROOT / "paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md"
DEC_EN = ROOT / "core/DECISION_LOG.md"
DEC_ZH = ROOT / "core/DECISION_LOG.zh-CN.md"
FOCUS_EN = ROOT / "docs/working-memory/current-focus.md"
FOCUS_ZH = ROOT / "docs/working-memory/current-focus.zh-CN.md"
TASK_EN = ROOT / "docs/working-memory/task-plan.md"
TASK_ZH = ROOT / "docs/working-memory/task-plan.zh-CN.md"


def fail(message: str) -> None:
    raise SystemExit(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing EIT submission artifact: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def words(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE))


def section(text: str, start: str, end: str | None = None) -> str:
    a = text.find(start)
    if a < 0:
        fail(f"missing section marker: {start}")
    if end is None:
        return text[a:]
    b = text.find(end, a + len(start))
    if b < 0:
        fail(f"missing section end marker: {end}")
    return text[a:b]


def require(text: str, marker: str, source: str) -> None:
    if marker not in text:
        fail(f"{source} missing required marker: {marker}")


def reference_sort_key(line: str) -> str:
    raw = line[2:].strip().lstrip("*")
    if raw.startswith("International Committee"):
        return "international committee"
    if raw.startswith("Nature Portfolio"):
        return "nature portfolio"
    if raw.startswith("W3C"):
        return "w3c"
    return raw.split(",", 1)[0].replace("*", "").strip().lower()


def build_masked_derivative(source: str) -> str:
    """Derive the reviewer-masked manuscript from the traceable submission derivative."""
    replacements = (
        ("the Project Memory Architecture of the AI-Assisted Human Inquiry and Creation Protocol (AHICP)", "the proposed Project Memory Architecture"),
        ("AHICP's Project Memory Architecture", "The proposed Project Memory Architecture"),
        ("The AHICP Project Memory Architecture", "The proposed Project Memory Architecture"),
        ("AHICP Project Memory", "the protocol's Project Memory"),
        ("AHICP governed Project Memory", "Proposed governed Project Memory"),
        ("AHICP Working Memory", "The protocol's Working Memory"),
        ("an AHICP workflow", "a protocol-governed workflow"),
        ("full AHICP adoption", "full adoption of the protocol"),
        ("an AHICP governance mechanism", "a governance mechanism of the protocol"),
        ("demanding AHICP criterion", "demanding protocol criterion"),
        ("Typical AHICP carriers", "Typical protocol carriers"),
        ("AHICP asks", "The protocol asks"),
        ("AHICP has conceptual", "The protocol has conceptual"),
        ("AHICP is not currently", "The protocol is not currently"),
        ("AHICP is not a single", "The protocol is not a single"),
        ("AHICP organizes", "The protocol organizes"),
        ("AHICP can also", "The protocol can also"),
        ("AHICP currently", "The protocol currently"),
        ("AHICP does not", "The protocol does not"),
        ("AHICP needs", "The protocol needs"),
        ("AHICP therefore", "The protocol therefore"),
        ("AHICP uses", "The protocol uses"),
        ("AHICP distinguishes", "The protocol distinguishes"),
        ("AHICP is not intended", "The protocol is not intended"),
        ("AHICP already", "The protocol already"),
        ("AHICP proposes", "The protocol proposes"),
        ("AHICP's", "the protocol's"),
        ("AHICP", "the protocol"),
    )
    masked = source
    for old, new in replacements:
        masked = masked.replace(old, new)
    post_replacements = (
        ("recorded.** the protocol's candidate contribution", "recorded.** The protocol's candidate contribution"),
        ("over-reliance. the protocol's response", "over-reliance. The protocol's response"),
        ("the protocol's Project Memory asks instead:", "The protocol's Project Memory asks instead:"),
        ("the protocol's research opportunity is therefore", "The protocol's research opportunity is therefore"),
        ("as a new concept. the protocol's scholarly value", "as a new concept. The protocol's scholarly value"),
        ("public release.” the protocol and companion", "public release.” The protocol and companion"),
    )
    for old, new in post_replacements:
        masked = masked.replace(old, new)
    return masked


def find_unmapped_years(
    body: str, citation_pairs: tuple[tuple[str, str], ...]
) -> list[str]:
    residual = body
    for citation_marker, _reference_prefix in citation_pairs:
        residual = residual.replace(citation_marker, "")
    return sorted(set(re.findall(r"(?<!\d)(?:19|20)\d{2}(?!\d)", residual)))


def require_no_unmapped_years(
    body: str, citation_pairs: tuple[tuple[str, str], ...], source: str
) -> None:
    years = find_unmapped_years(body, citation_pairs)
    if years:
        fail(
            f"{source} contains year-bearing text not covered by citation audit mapping: "
            + ", ".join(years)
        )


def main() -> int:
    if find_unmapped_years("Synthetic unmapped citation (2099).", ()) != ["2099"]:
        fail("citation consistency guard self-test failed")

    manuscript = read(MANUSCRIPT)
    masked_manuscript = read(MASKED_MANUSCRIPT)
    blinding_en = read(BLINDING_EN)
    blinding_zh = read(BLINDING_ZH)
    package_readme = read(README)
    check_en = read(CHECK_EN)
    check_zh = read(CHECK_ZH)
    ai_en = read(AI_EN)
    ai_zh = read(AI_ZH)
    citation_audit = read(CITATION_AUDIT)
    title_meta = read(TITLE_META)
    cover = read(COVER)
    form_en = read(FORM_EN)
    form_zh = read(FORM_ZH)
    dec_en = read(DEC_EN)
    dec_zh = read(DEC_ZH)
    focus_en = read(FOCUS_EN)
    focus_zh = read(FOCUS_ZH)
    task_en = read(TASK_EN)
    task_zh = read(TASK_ZH)

    abstract_block = section(manuscript, "## Abstract", "**Keywords:**")
    abstract_text = abstract_block.replace("## Abstract", "").strip()
    abstract_words = words(abstract_text)
    if not 150 <= abstract_words <= 250:
        fail(f"EIT abstract must be 150-250 words; found {abstract_words}")

    m = re.search(r"^\*\*Keywords:\*\*\s*(.+)$", manuscript, re.MULTILINE)
    if not m:
        fail("blinded manuscript is missing Keywords")
    keyword_count = len([x for x in m.group(1).split(";") if x.strip()])
    if not 4 <= keyword_count <= 6:
        fail(f"EIT keywords must contain 4-6 items; found {keyword_count}")

    content = section(manuscript, "## 1. Introduction:", "## References")
    content_words = words(content)
    if not 5000 <= content_words <= 8000:
        fail(f"EIT manuscript content must be 5000-8000 words; found {content_words}")

    heading_levels = [len(m.group(1)) for m in re.finditer(r"^(#+)\s", manuscript, re.MULTILINE)]
    if not heading_levels or max(heading_levels) > 3:
        fail("EIT manuscript must use no more than three displayed heading levels")

    table_headers = re.findall(
        r"^\|.+\|\n\|(?:\s*:?-+:?\s*\|)+$",
        manuscript,
        re.MULTILINE,
    )
    table_captions = re.findall(
        r"^\*\*Table\s+(\d+)\..+\*\*$",
        manuscript,
        re.MULTILINE,
    )
    if len(table_headers) != 2:
        fail(f"EIT manuscript must contain exactly 2 Markdown tables; found {len(table_headers)}")
    if table_captions != ["1", "2"]:
        fail(
            "EIT manuscript tables must have sequential bold captions "
            f"Table 1 and Table 2; found {table_captions}"
        )
    for table_number in (1, 2):
        if len(re.findall(rf"\bTable\s+{table_number}\b", manuscript)) < 2:
            fail(
                f"EIT manuscript Table {table_number} must be cited in text "
                "in addition to its caption"
            )

    required_manuscript = (
        "## Methodological and AI-use disclosure",
        "iterative drafting",
        "structural reorganization",
        "literature organization",
        "bilingual synchronization",
        "No AI system is listed as an author",
        "## Data availability statement",
        "No original empirical dataset was generated or analyzed",
        "No effectiveness results are reported",
    )
    for marker in required_manuscript:
        require(manuscript, marker, "blinded manuscript")

    forbidden_patterns = {
        r"(?:AHICP|HARC)-D\d+": "internal Decision ID",
        r"MA-FW-\d+": "internal Framework ID",
        r"WM-T\d+": "Working Memory task ID",
        r"FINAL ARTIFACT APPROVAL PENDING": "development-status metadata",
        r"CURRENT-FRAMEWORK": "framework-status metadata",
        r"APPROVED-FRAMEWORK": "framework-status metadata",
        r"github\.com": "direct GitHub URL",
        r"ChongLiuPhil": "repository owner identifier",
        r"\*\*Chinese title:\*\*": "internal bilingual metadata",
        r"\*\*Article status:\*\*": "internal development metadata",
    }
    for pattern, description in forbidden_patterns.items():
        if re.search(pattern, manuscript, re.IGNORECASE):
            fail(f"blinded manuscript contains prohibited {description}: {pattern}")

    if "MemGPT" in manuscript or "Packer, C." in manuscript:
        fail("blinded manuscript still cites MemGPT preprint; venue derivative should use published/accepted references")
    if "*Nature Methods*. (2026)" in manuscript:
        fail("blinded manuscript contains an uncited Nature Methods reference")

    refs = section(manuscript, "## References")
    ref_lines = [line for line in refs.splitlines() if line.startswith("- ")]
    if len(ref_lines) < 10:
        fail(f"unexpectedly small reference list: {len(ref_lines)} entries")
    keys = [reference_sort_key(line) for line in ref_lines]
    if keys != sorted(keys):
        fail("EIT reference list is not alphabetized by first author / institutional author")

    body_without_refs = manuscript[:manuscript.find("## References")]
    citation_reference_pairs = (
        ("Bian et al., 2026", "- Bian, H., et al. (2026)."),
        ("Clark and Chalmers (1998)", "- Clark, A., & Chalmers, D. (1998)."),
        ("Hardwig (1985)", "- Hardwig, J. (1985)."),
        ("Hutchins (1995)", "- Hutchins, E. (1995)."),
        ("ICMJE", "- International Committee of Medical Journal Editors (ICMJE)."),
        ("Lee, 1992", "- Lee, J. (1992)."),
        ("Mariano and Awazu (2024)", "- Mariano, S., & Awazu, Y. (2024)."),
        ("Nature Portfolio", "- Nature Portfolio. (n.d.)."),
        ("Parasuraman and Riley (1997)", "- Parasuraman, R., & Riley, V. (1997)."),
        ("Park et al., 2023", "- Park, J. S., et al. (2023)."),
        ("Singh, Cobbe, & Norval, 2019", "- Singh, J., Cobbe, J., & Norval, C. (2019)."),
        ("Tan et al., 2025", "- Tan, H., et al. (2025)."),
        ("Walsh & Ungson, 1991", "- Walsh, J. P., & Ungson, G. R. (1991)."),
        ("Weinreich & Groher, 2016", "- Weinreich, R., & Groher, I. (2016)."),
        ("Weiser and Morrison's (1998)", "- Weiser, M., & Morrison, J. (1998)."),
        ("W3C PROV", "- World Wide Web Consortium (W3C). (2013)."),
        ("Wu et al., 2025", "- Wu, D., et al. (2025)."),
        ("Zhang et al., 2025", "- Zhang, Z., et al. (2025)."),
    )
    if len(citation_reference_pairs) != len(ref_lines):
        fail(
            "citation/reference audit mapping must cover every reference-list entry "
            f"(mapped={len(citation_reference_pairs)}, refs={len(ref_lines)})"
        )
    for citation_marker, reference_prefix in citation_reference_pairs:
        require(body_without_refs, citation_marker, "blinded manuscript body")
        if not any(line.startswith(reference_prefix) for line in ref_lines):
            fail(f"reference list is missing mapped entry for citation: {citation_marker}")

    require_no_unmapped_years(body_without_refs, citation_reference_pairs, "blinded manuscript body")

    masked_abstract = section(masked_manuscript, "## Abstract", "**Keywords:**")
    masked_abstract_words = words(masked_abstract.replace("## Abstract", "").strip())
    if not 150 <= masked_abstract_words <= 250:
        fail(f"masked EIT abstract must be 150-250 words; found {masked_abstract_words}")

    masked_kw = re.search(r"^\*\*Keywords:\*\*\s*(.+)$", masked_manuscript, re.MULTILINE)
    if not masked_kw:
        fail("masked blinded manuscript is missing Keywords")
    masked_keyword_count = len([x for x in masked_kw.group(1).split(";") if x.strip()])
    if not 4 <= masked_keyword_count <= 6:
        fail(f"masked EIT keywords must contain 4-6 items; found {masked_keyword_count}")

    masked_content = section(masked_manuscript, "## 1. Introduction:", "## References")
    masked_content_words = words(masked_content)
    if not 5000 <= masked_content_words <= 8000:
        fail(f"masked EIT manuscript content must be 5000-8000 words; found {masked_content_words}")

    masked_heading_levels = [
        len(m.group(1)) for m in re.finditer(r"^(#+)\s", masked_manuscript, re.MULTILINE)
    ]
    if not masked_heading_levels or max(masked_heading_levels) > 3:
        fail("masked EIT manuscript must use no more than three displayed heading levels")

    for marker in required_manuscript:
        require(masked_manuscript, marker, "masked blinded manuscript")

    for pattern, description in forbidden_patterns.items():
        if re.search(pattern, masked_manuscript, re.IGNORECASE):
            fail(f"masked blinded manuscript contains prohibited {description}: {pattern}")

    for pattern, description in (
        (r"\bAHICP\b", "protocol acronym"),
        (r"AI-Assisted Human Inquiry and Creation Protocol", "full protocol name"),
        (r"\bthe the\b", "duplicated article from masking"),
        (r"\ban the protocol\b", "broken article from masking"),
        (r"\bfull the protocol\b", "broken masking phrase"),
        (r"Typical the protocol", "broken masking table label"),
        (r"demanding the protocol", "broken masking phrase"),
    ):
        if re.search(pattern, masked_manuscript, re.IGNORECASE):
            fail(f"masked blinded manuscript contains prohibited {description}: {pattern}")

    require(masked_manuscript, "proposed Project Memory Architecture", "masked blinded manuscript")
    require(masked_manuscript, "the protocol", "masked blinded manuscript")

    masked_refs = section(masked_manuscript, "## References")
    if masked_refs != refs:
        fail("masked and unmasked blinded manuscripts must have identical reference sections")

    masked_body_without_refs = masked_manuscript[:masked_manuscript.find("## References")]
    for citation_marker, _reference_prefix in citation_reference_pairs:
        require(masked_body_without_refs, citation_marker, "masked blinded manuscript body")

    require_no_unmapped_years(
        masked_body_without_refs, citation_reference_pairs, "masked blinded manuscript body"
    )

    expected_masked = build_masked_derivative(manuscript)
    if masked_manuscript != expected_masked:
        fail(
            "masked manuscript diverges from deterministic identity-masking transform "
            "of traceable manuscript"
        )

    require(blinding_en, "MASKED DERIVATIVE PREPARED", "English Blinding Review")
    require(blinding_zh, "MASKED DERIVATIVE PREPARED", "Chinese Blinding Review")
    require(blinding_en, "MANUSCRIPT_BLINDED_MASKED.md", "English Blinding Review")
    require(blinding_zh, "MANUSCRIPT_BLINDED_MASKED.md", "Chinese Blinding Review")

    for marker in (
        "AHICP-D033",
        "Ethics and Information Technology",
        "does not constitute Final Artifact Approval",
        "does not authorize submission / publication / release",
    ):
        require(dec_en, marker, "English Decision Log")
    for marker in (
        "AHICP-D033",
        "Ethics and Information Technology",
        "不构成 Final Artifact Approval",
        "不构成 submission / publication / release authorization",
    ):
        require(dec_zh, marker, "Chinese Decision Log")

    for text, language in ((form_en, "English Form Core"), (form_zh, "Chinese Form Core")):
        require(text, "ETHICS AND INFORMATION TECHNOLOGY", language)
        require(text, "AHICP-D033", language)
        require(text, "150", language)
        require(text, "250", language)
        require(text, "4", language)
        require(text, "6", language)
        require(text, "double-anonymous", language)

    require(package_readme, "Final Artifact Approval", "package README")
    require(check_en, "Final Artifact Approval", "English checklist")
    require(check_zh, "Final Artifact Approval", "Chinese checklist")
    require(ai_en, "FINAL HUMAN REVIEW PENDING", "English AI disclosure")
    require(ai_zh, "FINAL HUMAN REVIEW PENDING", "Chinese AI disclosure")
    require(citation_audit, "AUDITED — FINAL LIVE-POLICY RECHECK STILL REQUIRED", "Citation Audit")
    require(citation_audit, "VERIFIED-PUBLISHED", "Citation Audit")
    require(citation_audit, "CURRENT-POLICY-SOURCE", "Citation Audit")
    require(citation_audit, "MemGPT", "Citation Audit")
    require(citation_audit, "PROV-DM", "Citation Audit")

    require(title_meta, "[HUMAN TO COMPLETE]", "title-page metadata template")
    require(cover, "[CONFIRM: the manuscript is not under consideration elsewhere]", "cover-letter draft")

    require(focus_en, "Ethics and Information Technology", "English Current Focus")
    require(focus_zh, "Ethics and Information Technology", "Chinese Current Focus")
    require(task_en, "WM-T026", "English Task Plan")
    require(task_zh, "WM-T026", "Chinese Task Plan")

    print(
        "EIT submission validation passed "
        f"(abstract={abstract_words}, content={content_words}, keywords={keyword_count}, "
        f"masked_abstract={masked_abstract_words}, masked_content={masked_content_words}, "
        f"masked_keywords={masked_keyword_count}, refs={len(ref_lines)})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
