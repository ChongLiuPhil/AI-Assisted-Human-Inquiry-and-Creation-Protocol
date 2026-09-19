# AHICP v0.3 Migration Validation Record

**Date:** 2026-09-19  
**Branch:** `ahicp-semantic-migration-v0.3`  
**Status:** STRUCTURAL CHECKS PASSED / SEMANTIC REVIEW CONTINUES

## 1. Manifest path consistency

Repository-path references parsed from `AHICP_MANIFEST.yaml` were checked:

- path candidates checked: 33
- missing files: 0

The manifest currently points only to existing live control/state files.

## 2. Bilingual file pairing

All `*.zh-CN.md` files on the migration branch were checked for an English mirror:

- Chinese files: 62
- missing English mirrors: 0

This establishes physical pairing, but does **not** by itself prove paragraph-level semantic equivalence. Semantic parity remains a separate review task.

## 3. Zero-context control-chain check

The following Chinese canonical entry points were checked:

- `START_HERE.zh-CN.md`
- `BOOTSTRAP_PROMPT.zh-CN.md`
- `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
- `AGENTS.zh-CN.md`
- `protocol/ONBOARDING_HANDSHAKE.zh-CN.md`
- `AHICP_MANIFEST.yaml`
- `AHICP_CONTEXT_INTERFACE.yaml`

Results:

- all point to the new `AHICP_MANIFEST.yaml` / `AHICP_CONTEXT_INTERFACE.yaml`;
- no live onboarding/control entry above references `HARC_MANIFEST.yaml` or `HARC_CONTEXT_INTERFACE.yaml`;
- legacy `HARC_*` files remain only as compatibility pointers.

## 4. Historical identifiers

The migration does not rewrite historical `HARC-D001`–`HARC-D025` IDs.

The new naming/scope decision is recorded as:

- `AHICP-D026`

This preserves the audit distinction between historical events and the current protocol identity.

## 5. Research specialization template

`templates/research-project/` remains a research-specific specialization rather than being generalized into the only inquiry/creation structure.

It now has:
- `AHICP_MANIFEST.yaml`;
- `AHICP_CONTEXT_INTERFACE.yaml`;
- legacy `HARC_*` control files reduced to compatibility pointers;
- principal onboarding/agent files migrated to AHICP identifiers.

## 6. Methodology article / evidence migration result

Completed:
- the methodology Content Core now describes the **methodological significance of AHICP in research settings** rather than treating the protocol itself as research-only;
- the Working Argument Map, article text, evidence layer, Form Core, and Framework Status now use AHICP as the current protocol identity;
- historical `HARC-Dxxx` identifiers remain unchanged;
- the human-approved research-specific article title remains unchanged because it describes the article's subject rather than the protocol's formal name.

Remaining:
1. **semantic** bilingual parity on key normative files;
2. independent post-migration repair audit.

## 7. Current conclusion

The control plane and project entry points are structurally viable under AHICP v0.3.

This record does not equate structural validation with complete semantic migration. The PR should remain open until the remaining semantic audit is complete.
