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
        "### 23.5 授权作用域与持久状态行动生命周期",
        "proposal",
        "authorization provenance",
        "non-delegable",
        "### 23.5.1 首次配置时的人类授权方式选择",
        "bounded pre-authorization",
        "mixed policy",
    ],
    "protocol/SPECIFICATION.md": [
        "## 23. External Systems, Tool Discovery, Authorization, and Human Handoff",
        "built-in tools",
        "official MCP",
        "MUST",
        "MUST NOT",
        "provider actual state",
        "write",
        "### 23.5 Authorization scope and durable-state action lifecycle",
        "proposal",
        "authorization provenance",
        "non-delegable",
        "### 23.5.1 Human choice of authorization mode at initial configuration",
        "bounded pre-authorization",
        "mixed policy",
    ],
    "core/PROTOCOL_CORE.zh-CN.md": [
        "## P25.",
        "machine-operable-first",
        "provider actual state",
        "## P26.",
        "授权必须具有作用域",
        "non-delegable",
        "第一次配置",
        "mixed policy",
    ],
    "core/PROTOCOL_CORE.md": [
        "## P25.",
        "machine-operable-first",
        "provider actual state",
        "## P26.",
        "Authorization is scoped",
        "non-delegable",
        "When first configuring",
        "mixed policy",
    ],
    "AGENTS.zh-CN.md": [
        "capability probe",
        "secret",
        "provider actual state",
        "持久状态行动的授权作用域",
        "durable write-back",
        "第一次配置",
        "mixed policy",
    ],
    "AGENTS.md": [
        "capability probe",
        "secret",
        "provider actual state",
        "Authorization scope for durable-state actions",
        "durable write-back",
        "initial configuration",
        "mixed policy",
    ],
    "templates/research-project/AGENTS.zh-CN.md": [
        "capability probe",
        "0.3.0-draft",
        "持久状态行动的授权作用域",
        "non-delegable",
        "第一次配置",
        "mixed policy",
    ],
    "templates/research-project/AGENTS.md": [
        "capability probe",
        "0.3.0-draft",
        "Authorization scope for durable-state actions",
        "non-delegable",
        "initial configuration",
        "mixed policy",
    ],
    "core/DECISION_LOG.zh-CN.md": ["AHICP-D027", "AHICP-D028", "AHICP-D029", "per-action authorization", "bounded pre-authorization", "CI green"],
    "core/DECISION_LOG.md": ["AHICP-D027", "AHICP-D028", "AHICP-D029", "per-action authorization", "bounded pre-authorization", "green CI"],
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
