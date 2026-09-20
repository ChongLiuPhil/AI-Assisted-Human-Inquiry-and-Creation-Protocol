from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
CORE_REPOSITORIES = [
    "https://github.com/ChongLiuPhil/AI-Assisted-Human-Inquiry-and-Creation-Protocol",
    "https://github.com/ChongLiuPhil/Personal-Publishing-Framework",
    "https://github.com/ChongLiuPhil/Vault-interface",
    "https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter",
]
HUMAN_ENTRY = "https://chongliuphil.github.io/AI-Assisted-Human-Inquiry-and-Creation-Protocol/"
MACHINE_ENTRY = "https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/agent/"


def main() -> int:
    manifest = yaml.safe_load((ROOT / "ecosystem.yaml").read_text())
    if not isinstance(manifest, dict):
        raise SystemExit("ecosystem.yaml must contain a mapping")

    has_entrypoint = any(
        key in manifest for key in ("agent_entrypoint", "ecosystem_entrypoint", "canonical_entrypoint")
    ) or "ecosystem" in manifest
    if not has_entrypoint:
        raise SystemExit("ecosystem.yaml is missing an agent/ecosystem entrypoint")

    human = manifest.get("human_entrypoint")
    machine = manifest.get("machine_entrypoint")
    if not isinstance(human, dict) or human.get("role") != "human-conceptual-entry":
        raise SystemExit("ecosystem.yaml is missing the human conceptual entry")
    if human.get("current_public_landing") != HUMAN_ENTRY:
        raise SystemExit("human entry does not point to the AHICP public landing")
    if not human.get("provider_may_change"):
        raise SystemExit("human entry must remain delivery-provider independent")
    if not isinstance(machine, dict) or machine.get("public_landing") != MACHINE_ENTRY:
        raise SystemExit("machine entry does not point to the Starter /agent/ landing")

    manifest_text = (ROOT / "ecosystem.yaml").read_text()
    for repository in CORE_REPOSITORIES:
        if repository not in manifest_text:
            raise SystemExit(f"ecosystem.yaml is missing {repository}")

    for relative in ("README.md", "README.zh-CN.md"):
        text = (ROOT / relative).read_text()
        if "ecosystem.yaml" not in text and "docs/ECOSYSTEM" not in text:
            raise SystemExit(f"{relative} does not point to the ecosystem entrypoint")

    for relative in ("docs/HUMAN_GUIDE.zh-CN.md", "docs/HUMAN_GUIDE.md"):
        path = ROOT / relative
        if not path.exists() or len(path.read_text(encoding="utf-8")) < 5000:
            raise SystemExit(f"{relative} is missing or unexpectedly short")

    page = (ROOT / "docs/index.html").read_text(encoding="utf-8")
    required_page_markers = [
        "HUMAN_GUIDE.zh-CN.md",
        "HUMAN_GUIDE.md",
        MACHINE_ENTRY,
        'id="guideContentZh"',
        'id="guideContentEn"',
        'data-copy="newProjectPromptZh"',
        "function renderMd",
    ]
    for marker in required_page_markers:
        if marker not in page:
            raise SystemExit(f"AHICP public homepage is missing {marker}")

    print("ecosystem + human-entry validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
