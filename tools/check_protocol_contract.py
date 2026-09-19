#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

PAIRS = [
    ("protocol/SPECIFICATION.zh-CN.md", "protocol/SPECIFICATION.md"),
    ("core/PROTOCOL_CORE.zh-CN.md", "core/PROTOCOL_CORE.md"),
    ("AGENTS.zh-CN.md", "AGENTS.md"),
    ("templates/research-project/AGENTS.zh-CN.md", "templates/research-project/AGENTS.md"),
    ("core/DECISION_LOG.zh-CN.md", "core/DECISION_LOG.md"),
]

REQUIRED = {
    "protocol/SPECIFICATION.zh-CN.md": [
        "## 23. 外部系统、工具发现、授权与人类交接",
        "平台内建工具",
        "官方 MCP",
        "MUST",
        "MUST NOT",
        "provider actual state",
        "write-through",
    ],
    "protocol/SPECIFICATION.md": [
        "## 23. External Systems, Tool Discovery, Authorization, and Human Handoff",
        "built-in tools",
        "official MCP",
        "MUST",
        "MUST NOT",
        "provider actual state",
        "write",
    ],
    "core/PROTOCOL_CORE.zh-CN.md": ["## P25.", "machine-operable-first", "provider actual state"],
    "core/PROTOCOL_CORE.md": ["## P25.", "machine-operable-first", "provider actual state"],
    "AGENTS.zh-CN.md": ["capability probe", "secret", "provider actual state"],
    "AGENTS.md": ["capability probe", "secret", "provider actual state"],
    "templates/research-project/AGENTS.zh-CN.md": ["capability probe", "0.3.0-draft"],
    "templates/research-project/AGENTS.md": ["capability probe", "0.3.0-draft"],
    "core/DECISION_LOG.zh-CN.md": ["AHICP-D027"],
    "core/DECISION_LOG.md": ["AHICP-D027"],
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


for zh, en in PAIRS:
    if not (ROOT / zh).is_file():
        fail(f"missing canonical file: {zh}")
    if not (ROOT / en).is_file():
        fail(f"missing English mirror: {en}")

for path, markers in REQUIRED.items():
    body = (ROOT / path).read_text(encoding="utf-8")
    folded = body.casefold()
    for marker in markers:
        if marker.casefold() not in folded:
            fail(f"{path} is missing contract marker: {marker}")

for path in (
    "protocol/SPECIFICATION.zh-CN.md",
    "protocol/SPECIFICATION.md",
    "core/PROTOCOL_CORE.zh-CN.md",
    "core/PROTOCOL_CORE.md",
):
    if "Cloudflare" in (ROOT / path).read_text(encoding="utf-8"):
        fail(f"provider-specific Cloudflare detail leaked into normative core: {path}")

for path in (
    "templates/research-project/AGENTS.zh-CN.md",
    "templates/research-project/AGENTS.md",
):
    if "0.2.0-draft" in (ROOT / path).read_text(encoding="utf-8"):
        fail(f"stale AHICP template version remains: {path}")

print("AHICP protocol contract validation passed.")
