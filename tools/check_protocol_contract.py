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
    ("docs/working-memory/current-focus.zh-CN.md", "docs/working-memory/current-focus.md"),
    ("docs/working-memory/task-plan.zh-CN.md", "docs/working-memory/task-plan.md"),
    ("docs/working-memory/work-log.zh-CN.md", "docs/working-memory/work-log.md"),
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
    "docs/working-memory/current-focus.zh-CN.md": ["AHICP-D027", "AHICP-D028", "AHICP-D029", "2026-09-20"],
    "docs/working-memory/current-focus.md": ["AHICP-D027", "AHICP-D028", "AHICP-D029", "2026-09-20"],
    "docs/working-memory/task-plan.zh-CN.md": ["WM-T019", "WM-T020", "WM-T021", "COMPLETED / CI-GATED"],
    "docs/working-memory/task-plan.md": ["WM-T019", "WM-T020", "WM-T021", "COMPLETED / CI-GATED"],
    "docs/working-memory/work-log.zh-CN.md": ["# AHICP Working Memory — Work Log", "AHICP-D029", "section-local"],
    "docs/working-memory/work-log.md": ["# AHICP Working Memory — Work Log", "AHICP-D029", "section-local"],
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_section(path: str, start_marker: str, end_marker: str, markers: list[str]) -> None:
    body = (ROOT / path).read_text(encoding="utf-8")
    start = body.find(start_marker)
    if start < 0:
        fail(f"{path} is missing section start: {start_marker}")
    end = body.find(end_marker, start + len(start_marker))
    if end < 0:
        fail(f"{path} is missing section end: {end_marker}")
    section = body[start:end].casefold()
    for marker in markers:
        if marker.casefold() not in section:
            fail(f"{path} section {start_marker} is missing contract marker: {marker}")


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

require_section(
    "protocol/SPECIFICATION.zh-CN.md",
    "### 23.3 Human handoff",
    "### 23.4 Provider actual state 与 repository durable state",
    ["权限授予"],
)
require_section(
    "protocol/SPECIFICATION.md",
    "### 23.3 Human handoff",
    "### 23.4 Provider actual state and repository durable state",
    ["permission grants"],
)
require_section(
    "protocol/SPECIFICATION.zh-CN.md",
    "### 23.5.1 首次配置时的人类授权方式选择",
    "### 23.5.2 Provider-neutral 的高影响判断",
    ["scope", "authorization provenance", "escalation conditions", "repository durable state"],
)
require_section(
    "protocol/SPECIFICATION.md",
    "### 23.5.1 Human choice of authorization mode at initial configuration",
    "### 23.5.2 Provider-neutral high-impact test",
    ["scope", "authorization provenance", "escalation conditions", "repository durable state"],
)

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
