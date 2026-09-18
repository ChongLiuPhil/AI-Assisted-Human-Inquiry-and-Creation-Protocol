# HARC Bilingual Synchronization Policy

**Status: normative project rule**  
**Chinese: canonical source**  
**English: synchronized mirror**

## 1. Core rule

HARC substantive documentation is maintained in both Chinese and English.

- Chinese is the authoritative semantic, editing, and human-review baseline.
- English is a synchronized translation mirror of the Chinese version.
- Every substantive change must update both languages in the same work cycle.
- If the Chinese and English versions materially conflict, Chinese governs and the English version must be repaired.
- Updating only one language does not constitute a complete edit.

## 2. File naming

Recommended:

- Chinese canonical version: `NAME.zh-CN.md`
- English mirror: retain `NAME.md` where GitHub default/backward compatibility is useful; otherwise use `NAME.en.md`.

The root `README.md` may remain the default English GitHub entry point, while `README.zh-CN.md` is its canonical Chinese source.

## 3. Documents that must be bilingual

All substantive human-readable Markdown should have Chinese and English counterparts, including:

- protocol specifications and governance;
- Content / Form / Protocol Cores;
- Decision Logs;
- Argument Maps and Framework Status;
- audits;
- evidence/source notes;
- methodology articles, white papers, and explanatory documents;
- reusable project and form-profile templates;
- CONTRIBUTING, ROADMAP, licensing-decision, and similar governance files.

## 4. Language-neutral technical files

The following may remain single-copy where their contents are language-neutral:

- BibTeX;
- JSON/YAML schemas;
- source code;
- raw data;
- machine-generated hashes or state manifests.

Human-facing documentation around those files remains bilingual.

## 5. Completion condition

A bilingual edit is complete only when:

1. the Chinese canonical file is updated;
2. the English mirror is synchronized;
3. claims, requirements, states, unresolved issues, and link relationships are semantically equivalent;
4. neither version contains a substantive section absent from the other;
5. any affected Decision Log, Framework Status, or upstream state is synchronized in both languages.

## 6. Agent behavior

An AI Agent should edit the Chinese canonical version first, then generate or update the English mirror.

A legacy single-language document is a synchronization defect and should be paired.

An Agent must not use a more polished English wording to silently change the Chinese meaning. If the Chinese meaning should change, return upstream and revise the Chinese canonical source first.

## 7. New-project inheritance

A new HARC project may explicitly adopt the bilingual profile. When it does, Chinese canonical and English mirror files should be created at initialization rather than added later.


## 8. Pre-cutover legacy catch-up

The Chinese-canonical / English-synchronized-mirror rule became formal HARC governance on 2026-09-18.

For bilingual files that existed before that rule, if the **English version had in fact developed substantive content newer than the Chinese version**, that newer content must not be discarded merely to impose Chinese canonical status immediately.

Perform a one-time legacy catch-up:

`pre-cutover English development -> Chinese catch-up -> bilingual parity -> Chinese canonical cutover`

Requirements:

1. identify substantive pre-rule English developments not yet present in Chinese;
2. incorporate them into Chinese so that Chinese represents the genuinely latest semantic state at cutover;
3. then synchronize English to that updated Chinese version;
4. complete a parity check before declaring canonical cutover complete;
5. after cutover, English must no longer develop independently.

This catch-up is a migration exception and does not alter the long-term direction of governance.

## 9. Normal editing direction after cutover

After canonical cutover, all normal substantive edits must follow:

`Human decision -> Chinese canonical -> English synchronized mirror`

English wording may be improved as translation, but the English mirror must not independently add, remove, strengthen, or weaken substantive content.

If English drafting reveals that the Chinese content itself should change, revise the Chinese canonical source first and then resynchronize English. English must not become an independent substantive source after cutover.
