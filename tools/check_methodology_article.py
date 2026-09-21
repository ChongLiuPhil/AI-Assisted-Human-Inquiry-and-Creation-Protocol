from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

ZH_ARTICLE = ROOT / "paper/METHODOLOGY_ARTICLE.zh-CN.md"
EN_ARTICLE = ROOT / "paper/METHODOLOGY_ARTICLE.en.md"
ZH_MAP = ROOT / "paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md"
EN_MAP = ROOT / "paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.md"
ZH_CORE = ROOT / "paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md"
EN_CORE = ROOT / "paper/METHODOLOGY_ARTICLE_CONTENT_CORE.md"
ZH_STATUS = ROOT / "paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md"
EN_STATUS = ROOT / "paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.md"
ZH_DECISIONS = ROOT / "core/DECISION_LOG.zh-CN.md"
EN_DECISIONS = ROOT / "core/DECISION_LOG.md"
ZH_EVIDENCE = ROOT / "evidence/METHODOLOGY_SOURCES.zh-CN.md"
EN_EVIDENCE = ROOT / "evidence/METHODOLOGY_SOURCES.md"
BIB = ROOT / "paper/methodology-references.bib"
ZH_FOCUS = ROOT / "docs/working-memory/current-focus.zh-CN.md"
EN_FOCUS = ROOT / "docs/working-memory/current-focus.md"
ZH_TASK = ROOT / "docs/working-memory/task-plan.zh-CN.md"
EN_TASK = ROOT / "docs/working-memory/task-plan.md"
ZH_APPROVED = ROOT / "paper/frameworks/MA-FW-001.zh-CN.md"
EN_APPROVED = ROOT / "paper/frameworks/MA-FW-001.md"
ZH_REVIEW = ROOT / "paper/METHODOLOGY_ARTICLE_FRAMEWORK_REVIEW_MEMO.zh-CN.md"
EN_REVIEW = ROOT / "paper/METHODOLOGY_ARTICLE_FRAMEWORK_REVIEW_MEMO.md"

CORE_THESIS_ZH = "一个长期人机项目的持久记忆，应当属于项目，而不是属于某一个模型"
CORE_THESIS_EN = "The durable memory of a long-running human–AI project should belong to the project, not to a particular model"

REQUIRED_REFS = (
    "park2023generativeagents",
    "packer2023memgpt",
    "zhang2025agentsmemorysurvey",
    "wu2025longmemeval",
    "tan2025membench",
    "bian2026realmem",
    "w3c2013prov",
    "walsh1991organizationalmemory",
    "weiser1998projectmemory",
    "mariano2024projectmemory",
    "weinreich2016sakm",
    "singh2019decisionprovenance",
    "lee1992designrationale",
)

REQUIRED_EVIDENCE = (
    "Generative Agents",
    "MemGPT",
    "LongMemEval",
    "MemBench",
    "RealMem",
    "W3C PROV",
    "Organizational Memory",
    "Project Memory: Information Management for Project Teams",
    "Managing large-scale projects: Unpacking the role of project memory",
    "Software Architecture Knowledge Management",
    "Decision Provenance",
)

STALE_MARKERS = (
    "full structural rewrite remains deferred",
    "Do not perform the major structural rewrite",
    "在整体 Framework Approval 前，不进行大规模结构性重写",
    "current draft retains the earlier 15-part structure",
    "正文仍保留较早的 15 部分结构",
    "WORKING-FRAMEWORK — REVISED UNDER AHICP-D030 / HUMAN REVIEW PENDING",
    "Framework Approval：`NOT COMPLETED`",
    "Framework Approval: `NOT COMPLETED`",
)


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"missing methodology artifact: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require(text: str, marker: str, source: str) -> None:
    if marker not in text:
        raise SystemExit(f"{source} is missing required marker: {marker}")


def main() -> int:
    zh_article = read(ZH_ARTICLE)
    en_article = read(EN_ARTICLE)
    zh_map = read(ZH_MAP)
    en_map = read(EN_MAP)
    zh_core = read(ZH_CORE)
    en_core = read(EN_CORE)
    zh_status = read(ZH_STATUS)
    en_status = read(EN_STATUS)
    zh_decisions = read(ZH_DECISIONS)
    en_decisions = read(EN_DECISIONS)
    zh_evidence = read(ZH_EVIDENCE)
    en_evidence = read(EN_EVIDENCE)
    bib = read(BIB)
    zh_focus = read(ZH_FOCUS)
    en_focus = read(EN_FOCUS)
    zh_task = read(ZH_TASK)
    en_task = read(EN_TASK)
    zh_approved = read(ZH_APPROVED)
    en_approved = read(EN_APPROVED)
    zh_review = read(ZH_REVIEW)
    en_review = read(EN_REVIEW)

    zh_sections = re.findall(r"^## (?:一|二|三|四|五|六|七|八|九|十|十一|十二|十三)、", zh_article, re.MULTILINE)
    en_sections = re.findall(r"^## (?:[1-9]|1[0-3])\. ", en_article, re.MULTILINE)
    if len(zh_sections) != 13:
        raise SystemExit(f"Chinese methodology article must have 13 main sections; found {len(zh_sections)}")
    if len(en_sections) != 13:
        raise SystemExit(f"English methodology article must have 13 main sections; found {len(en_sections)}")

    require(zh_article, CORE_THESIS_ZH, "Chinese article")
    require(en_article, CORE_THESIS_EN, "English article")
    require(zh_article, "本文不报告这些测试的实证结果", "Chinese article")
    require(en_article, "No empirical results from those tests are reported here", "English article")
    require(zh_article, "DERIVED-FROM-MA-FW-001 — FINAL ARTIFACT APPROVAL PENDING", "Chinese article")
    require(en_article, "DERIVED-FROM-MA-FW-001 — FINAL ARTIFACT APPROVAL PENDING", "English article")
    require(zh_article, "不主张首创“project memory”概念", "Chinese article")
    require(en_article, "does not claim to originate the concept of project memory", "English article")
    require(zh_article, "design research question", "Chinese article")
    require(en_article, "design research question", "English article")

    for marker in ("AHICP-D030", "AHICP-D031", "一篇统一论文", "Project Memory Architecture", "MA-FW-001"):
        require(zh_decisions, marker, "Chinese Decision Log")
    for marker in ("AHICP-D030", "AHICP-D031", "one unified paper", "Project Memory Architecture", "MA-FW-001"):
        require(en_decisions, marker, "English Decision Log")

    for number in range(17, 23):
        require(zh_core, f"## C{number}.", "Chinese Article Content Core")
        require(en_core, f"## C{number}.", "English Article Content Core")

    for number in range(1, 14):
        require(zh_map, f"### T{number} —", "Chinese Working Argument Map")
        require(en_map, f"### T{number} —", "English Working Argument Map")
    require(zh_map, "CURRENT-FRAMEWORK — ALIGNED WITH APPROVED MA-FW-001", "Chinese Working Argument Map")
    require(en_map, "CURRENT-FRAMEWORK — ALIGNED WITH APPROVED MA-FW-001", "English Working Argument Map")
    require(zh_map, "Framework Approval as a Structured Human-Review Gate and Responsibility Anchor", "Chinese Working Argument Map")
    require(en_map, "Framework Approval as a Structured Human-Review Gate and Responsibility Anchor", "English Working Argument Map")

    for status_text, language in ((zh_status, "Chinese"), (en_status, "English")):
        require(status_text, "MA-FW-001", f"{language} Framework Status")
        require(status_text, "Framework Approval", f"{language} Framework Status")
        require(status_text, "COMPLETED", f"{language} Framework Status")
        require(status_text, "Final Artifact Approval", f"{language} Framework Status")
        require(status_text, "NOT COMPLETED", f"{language} Framework Status")

    for approved_text, language in ((zh_approved, "Chinese"), (en_approved, "English")):
        require(approved_text, "APPROVED-FRAMEWORK — MA-FW-001", f"{language} MA-FW-001 snapshot")
        require(approved_text, "AHICP-D031", f"{language} MA-FW-001 snapshot")
        require(approved_text, "Framework Approval as a Structured Human-Review Gate and Responsibility Anchor", f"{language} MA-FW-001 snapshot")
        for number in range(1, 14):
            require(approved_text, f"### T{number} —", f"{language} MA-FW-001 snapshot")

    require(zh_review, "SCHOLARLY REVIEW COMPLETED — MA-FW-001 APPROVED", "Chinese Framework Review Memo")
    require(en_review, "SCHOLARLY REVIEW COMPLETED — MA-FW-001 APPROVED", "English Framework Review Memo")

    for marker in REQUIRED_REFS:
        require(bib, marker, "methodology-references.bib")
    if "\n---\n" in bib:
        raise SystemExit("methodology-references.bib contains a Markdown separator and is not clean BibTeX")
    for marker in REQUIRED_EVIDENCE:
        require(zh_evidence, marker, "Chinese evidence layer")
        require(en_evidence, marker, "English evidence layer")

    require(zh_focus, "WM-OBJ-005", "Chinese Current Focus")
    require(en_focus, "WM-OBJ-005", "English Current Focus")
    require(zh_focus, "MA-FW-001", "Chinese Current Focus")
    require(en_focus, "MA-FW-001", "English Current Focus")
    for marker in ("WM-T022", "WM-T023", "WM-T024", "WM-T025", "WM-T026"):
        require(zh_task, marker, "Chinese Task Plan")
        require(en_task, marker, "English Task Plan")

    combined = "\n".join((
        zh_article, en_article, zh_map, en_map, zh_status, en_status,
        zh_focus, en_focus, zh_task, en_task, zh_approved, en_approved, zh_review, en_review,
    ))
    for marker in STALE_MARKERS:
        if marker in combined:
            raise SystemExit(f"stale pre-D030 methodology status remains: {marker}")

    effectiveness_phrases = (
        "AHICP has been proven",
        "AHICP 已被证明",
        "AHICP proves that",
        "实验证明 AHICP",
        "AHICP is the first project memory",
        "AHICP first introduced project memory",
        "AHICP 首创 project memory",
        "AHICP 首次提出 project memory",
    )
    require(zh_decisions, "不构成 Final Artifact Approval", "Chinese Decision Log")
    require(en_decisions, "does not constitute Final Artifact Approval", "English Decision Log")
    require(zh_decisions, "不自动授权 PR merge", "Chinese Decision Log")
    require(en_decisions, "does not automatically authorize PR merge", "English Decision Log")

    for marker in effectiveness_phrases:
        if marker in zh_article or marker in en_article:
            raise SystemExit(f"unsupported effectiveness wording detected: {marker}")

    print("methodology article consistency validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
