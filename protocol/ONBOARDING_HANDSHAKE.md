# Zero-Context Onboarding Handshake Protocol

> **Language:** Chinese canonical: `ONBOARDING_HANDSHAKE.zh-CN.md`; this English file is the synchronized mirror.

## 1. Purpose

Durable repository state supports cross-agent continuity only if a replacement AI Agent can correctly discover, read, distinguish authority levels, and act from that state.

Repository access alone does not count as successful takeover.

Successful takeover must be verified through an explicit **Onboarding Handshake**.

## 2. When it is required

Run a full handshake when:

- a new AI Agent first takes over;
- the primary model/platform/agent changes;
- the Agent cannot access prior chat;
- work resumes after a long interruption and state may have changed;
- the human explicitly requests re-onboarding;
- the Agent detects material inconsistency among manifest, Cores, Framework, or Clarification state.

Short-term continuous work by the same Agent need not repeat the full handshake every turn, but relevant upstream state should be reread after major changes.

## 3. Prohibited actions before handshake

Before a successful handshake, do not:

- create or approve a Framework;
- promote AI proposals into human commitments;
- resolve or close Clarifications;
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

Before broad long-term-state retrieval, the Agent should read Working Memory Index, Current Focus, and Task Plan and confirm current stage, objective, primary blocker, immediate next action, active tasks, next actions, TODO/backlog, blockers, and pending human decisions/clarifications.

Work Log is skipped by default and retrieved only for historical review, audit, change reconstruction, or current/history conflict.

If Working Memory clearly conflicts with durable repository state, report `WORKING-MEMORY-STALE` and repair Working Memory rather than treating its old summary as authoritative.

## 5. Required Onboarding Report

The report covers at least:

- protocol version and canonical language;
- human-confirmed content;
- Form state;
- Current Focus CURRENT_STAGE / CURRENT_OBJECTIVE / PRIMARY_BLOCKER / IMMEDIATE_NEXT_ACTION;
- Task Plan ACTIVE_TASKS / NEXT_ACTIONS / TODO / BACKLOG;
- BLOCKERS / PENDING_HUMAN_DECISIONS / Clarifications;
- Working / Approved Framework;
- Artifact state;
- Evidence conflicts;
- bilingual synchronization;
- permitted and blocked next actions;
- the propagation path for the current request.

Recommended format:

`ONBOARDING_REPORT_TEMPLATE.zh-CN.md`

## 5.5 Repository Context Activation

After the Onboarding Report, the Agent MUST read `HARC_CONTEXT_INTERFACE.yaml` and `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`, then confirm:

`HARC REPOSITORY CONTEXT — ACTIVE`

This loads only the minimal Repository Resolver:

- GitHub source of truth;
- manifest / context-interface paths;
- task route;
- latest-revision / write-through / cache-invalidation rules.

It must not maintain long-lived copies of Working Memory, Framework, Artifact, Core, or other dynamic project state.

Onboarding may be marked `PASS` only when:

- the Onboarding Report is complete;
- Repository Context is active;
- the Agent can retrieve current blockers / pending decisions from latest Working Memory and verify related gates against the relevant long-term canonical files;
- the Agent understands that report summaries and session excerpts are non-authoritative cache.

## 6. PASS / PARTIAL / FAIL

### PASS

The Agent can accurately reconstruct core project state from the repository and no onboarding defect blocks the current work.

### PARTIAL

Most state can be reconstructed, but some work is constrained by missing files, unresolved clarification, unknown adopted protocol version, evidence gaps, or synchronization defects.

Only unaffected work may proceed.

### FAIL

Onboarding fails if the Agent cannot reliably determine:

- what is human commitment;
- what remains AI-proposed;
- which clarifications are blocking;
- current Framework / Artifact state;
- canonical-language / mirror relationship;
- permitted next action.

Large-scale substantive work must not continue under FAIL.

## 7. Human verification

The Onboarding Report is a compressed verification interface, not a demand that the human reread the entire repository.

The human may confirm the reconstruction, correct misunderstandings, identify missing state, resolve high-impact uncertainty, or decide whether the next phase may begin.

## 8. Machine manifest vs human-readable state

`HARC_MANIFEST.yaml` is a machine-readable index of paths, entry points, and invariants.

It does not replace Protocol Core, Decision Log, Content/Form Core, Clarification Register, or Framework state.

If the manifest conflicts with Chinese canonical human-readable governance, Chinese canonical governs and the manifest must be repaired.

## 9. Practical platform-independence limit

HARC cannot guarantee that every third-party AI platform automatically reads `START_HERE`, `AGENTS`, or the manifest.

It therefore uses multiple discovery mechanisms:

- visible root files;
- README navigation;
- AGENTS contract;
- standalone Bootstrap Prompt;
- machine manifest;
- human-copyable startup instruction;
- Onboarding Report verification.

The target is:

> **Any repository-capable Agent that follows explicit project instructions can reconstruct the same governance state from zero context, and the human can verify that reconstruction.**

## 10. Principle

> **Persistent state solves “the memory was not lost”; the Onboarding Handshake solves “the new Agent actually understood and used that memory according to the correct authority structure.”**
