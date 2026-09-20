#!/usr/bin/env python3
from pathlib import Path
import fnmatch
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "templates/template-manifest.yaml"

def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

def matches(root, pattern):
    if pattern.endswith("/"):
        prefix = pattern.rstrip("/") + "/"
        return any(p.is_file() and p.relative_to(root).as_posix().startswith(prefix) for p in root.rglob("*"))
    return any(fnmatch.fnmatch(p.relative_to(root).as_posix(), pattern) for p in root.rglob("*") if p.is_file())

def main():
    data = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))
    if data.get("schema") != "ahicp-template-manifest/v2":
        fail("template manifest schema must be ahicp-template-manifest/v2")
    if data.get("template_version") != "0.3.1-draft":
        fail("template version must be 0.3.1-draft")
    if data.get("template_root") != "templates/research-project":
        fail("unexpected template_root")

    template_root = ROOT / data["template_root"]
    profiles = data.get("profiles") or {}
    expected_profiles = {"research-lite", "research-standard", "research-full"}
    if set(profiles) != expected_profiles:
        fail(f"profile set mismatch: {sorted(profiles)}")

    bindings = data.get("role_bindings") or {}
    used_roles = set()
    for name, profile in profiles.items():
        roles = profile.get("required_roles")
        if not isinstance(roles, list) or not roles:
            fail(f"{name} must declare required_roles")
        used_roles.update(roles)
        missing = [role for role in roles if role not in bindings]
        if missing:
            fail(f"{name} has unbound roles: {missing}")

    for role in sorted(used_roles):
        path = bindings[role]
        if not isinstance(path, str) or not path:
            fail(f"invalid role binding for {role}")
        if not matches(template_root, path):
            fail(f"role binding target does not exist: {role} -> {path}")

    policy = data.get("upgrade_policy") or {}
    keys = ("project_owned", "merge_managed", "upstream_managed")
    for key in keys:
        if not isinstance(policy.get(key), list):
            fail(f"upgrade_policy.{key} must be a list")

    exact_seen = {}
    for key in keys:
        for entry in policy[key]:
            if entry in exact_seen:
                fail(f"ownership entry appears in both {exact_seen[entry]} and {key}: {entry}")
            exact_seen[entry] = key

    for key in ("merge_managed", "upstream_managed"):
        for pattern in policy[key]:
            if not matches(template_root, pattern):
                fail(f"{key} pattern matches no template file: {pattern}")

    rule = str(data.get("rule", "")).casefold()
    if "functionally mapped" not in rule:
        fail("functional-mapping rule is missing")

    print("AHICP template manifest contract passed.")

if __name__ == "__main__":
    main()
