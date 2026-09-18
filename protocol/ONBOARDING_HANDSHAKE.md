# Zero-Context Onboarding Handshake Protocol

> **Language:** Chinese canonical: `ONBOARDING_HANDSHAKE.zh-CN.md`; this English file is the synchronized mirror.

## 1. Purpose

Durable repository state supports cross-Agent continuity only if a replacement AI Agent can correctly discover, read, distinguish authority levels, and act from that state.

Repository access alone does not count as successful takeover.

Successful takeover must be verified through an explicit **Onboarding Handshake**.

## 2. When it is required

Run a full handshake when:

- a new AI Agent first takes over;
- the primary model/platform/Agent changes;
- the Agent cannot access prior chat;
- work resumes after a long interruption and state may have changed;
- the human explicitly requests re-onboarding;
- the Agent detects obvious inconsistency among manifest, Core, Framework, Current Focus, Task Plan, or Clarification state.

Short-term continuous work by the same Agent need not repeat the full handshake every turn, but relevant upstream state should be reread after major changes.

## 3. Prohibited actions before handshake

Before a successful handshake, do not:

- create or approve a Framework;
- promote AI proposals into human commitments;
- resolve or close a Clarification without human confirmation;
- perform large-scale Argument Map restructuring;
- perform large-scale Artifact rewriting;
- change reusable author Form preferences;
- make release/submission judgments;
- overwrite Chinese canonical state from English mirrors.

Permitted actions are limited to reading, state reconstruction, path/version/parity checks, defect reporting, and repair of obvious onboarding-infrastructure defects that do not alter substantive research content.

## 4. Required state to read

The root manifest determines exact paths. At minimum:

1. START_HERE;
2. HARC_MANIFEST;
3. HARC_CONTEXT_INTERFACE;
4. AGENTS / Session Context Bootstrap;
5. Working Memory Index;
6. Current Focus;
7. Task Plan;
8. Onboarding Handshake / Protocol governance;
9. task-relevant Layer 1 Core / Decision Log;
10. task-relevant Layer 2 Framework Status / Working or Approved Framework;
11. task-relevant Layer 3 Artifact;
12. task-relevant Evidence;
13. English-mirror parity.

## 4.5 Working Memory resume check

Before broad Long-Term Memory retrieval, read Working Memory Index, Current Focus, and Task Plan and confirm:

- CURRENT_STAGE;
- CURRENT_OBJECTIVE;
- PRIMARY_BLOCKER;
- IMMEDIATE_NEXT_ACTION;
- ACTIVE_TASKS;
- NEXT_ACTIONS;
- TODO / BACKLOG;
- BLOCKERS;
- PENDING_HUMAN_DECISIONS / Clarifications.

Work Log is skipped by default; retrieve it only for historical review, audit, change reconstruction, or current/history conflict.

If Working Memory clearly conflicts with canonical Long-Term Memory, report `WORKING-MEMORY-STALE` and repair Working Memory first rather than continuing from its stale summary.

## 5. Required Onboarding Report

The report must cover at least:

- protocol version and canonical language;
- human-confirmed content;
- Form state;
- Current Focus: CURRENT_STAGE / CURRENT_OBJECTIVE / PRIMARY_BLOCKER / IMMEDIATE_NEXT_ACTION;
- Task Plan: ACTIVE_TASKS / NEXT_ACTIONS / TODO / BACKLOG;
- BLOCKERS / PENDING_HUMAN_DECISIONS / Clarifications;
- Working / Approved Framework;
- Artifact state;
- Evidence conflict;
- bilingual synchronization state;
- permitted and blocked next actions;
- propagation path for the current request.

Recommended format:

`ONBOARDING_REPORT_TEMPLATE.zh-CN.md`

## 5.5 Repository Context Activation

After the Onboarding Report, the Agent must read `HARC_CONTEXT_INTERFACE.yaml` and `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md` and confirm:

`HARC REPOSITORY CONTEXT — ACTIVE`

This confirmation loads only the minimal Repository Resolver:

- GitHub source of truth;
- manifest / context-interface paths;
- task route;
- latest-revision / write-through / cache-invalidation rules.

It must not keep long-lived copies of Working Memory, Framework, Artifact, Core, or other dynamic state.

Onboarding can be `PASS` only when:

- the Onboarding Report is complete;
- Repository Context is active;
- the Agent can read current blockers / pending decisions from latest Working Memory and verify affected gates against corresponding canonical Long-Term Memory;
- the Agent understands that report summaries and session excerpts are non-authoritative cache.

## 6. PASS / PARTIAL / FAIL

### PASS

The Agent can accurately answer the core state questions using repository state alone, with no onboarding defect blocking the current work.

### PARTIAL

The Agent can reconstruct most state, but work is constrained by missing files, unresolved Clarifications, unclear adopted protocol version, evidence gaps, or synchronization defects.

Only unaffected work may proceed.

### FAIL

Onboarding fails if the Agent cannot reliably determine:

- which content is a human commitment;
- which content is AI-proposed;
- which Clarifications are blocking;
- current Framework / Artifact state;
- canonical-language / mirror relation;
- the currently permitted next action.

Large-scale substantive work must not proceed in FAIL state.

## 7. Human verification

The Onboarding Report is a compressed verification interface, not a request for the human to reread the entire repository.

The human can confirm understanding, correct a misreading, identify missing state, resolve a new high-impact uncertainty, or decide whether the next phase may begin.

## 8. Machine manifest and human-readable state

`HARC_MANIFEST.yaml` is a machine-readable index of paths, state entry points, and invariants.

It does not replace:

- Protocol Core;
- Decision Log;
- Content/Form Core;
- Task Plan / Clarification state;
- Framework.

If the manifest conflicts with Chinese canonical human-readable rules, Chinese canonical governs and the manifest must be repaired.

## 9. Real limits of platform independence

HARC cannot guarantee that every third-party AI platform will automatically read `START_HERE`, `AGENTS`, or the manifest.

It therefore uses multiple discovery mechanisms:

- conspicuous root-level files;
- README navigation;
- AGENTS contract;
- standalone Bootstrap Prompt;
- machine manifest;
- a startup instruction the human can copy directly;
- Onboarding Report verification.

The objective is not “automatic platform obedience.” It is:

> **If an Agent can read the repository and follows explicit project instructions, it can reconstruct the same governance state from zero context, and the human can verify that reconstruction.**

## 10. Principle

> **Persistent state solves “the memory was not lost”; the Onboarding Handshake solves “the new Agent actually understood and used the memory under the correct authority structure.”**
