from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "paper/submission/ethics-information-technology"

MANUSCRIPT = BASE / "MANUSCRIPT_BLINDED.md"
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


def main() -> int:
    manuscript = read(MANUSCRIPT)
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
        f"(abstract={abstract_words}, content={content_words}, keywords={keyword_count}, refs={len(ref_lines)})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
