#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
manifest=ROOT/"templates/template-manifest.yaml"
body=manifest.read_text(encoding="utf-8")
required=[
    "template_version: 0.3.0-draft",
    "research-lite:",
    "research-standard:",
    "research-full:",
    "project_owned:",
    "merge_managed:",
    "upstream_managed:",
    "functionally mapped",
]
for marker in required:
    if marker.casefold() not in body.casefold():
        print(f"ERROR: template manifest missing {marker}",file=sys.stderr)
        raise SystemExit(1)

for path in (
    "templates/research-project/START_HERE.zh-CN.md",
    "templates/research-project/AGENTS.zh-CN.md",
    "templates/research-project/AHICP_MANIFEST.yaml",
    "templates/research-project/AHICP_CONTEXT_INTERFACE.yaml",
    "templates/research-project/docs/working-memory.zh-CN.md",
):
    if not (ROOT/path).is_file():
        raise SystemExit(f"ERROR: installable template missing {path}")
print("AHICP template profile contract passed.")
