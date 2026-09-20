# AGENTS.md — AHICP Agent Assistance Contract

This repository defines the **AI-Assisted Human Inquiry and Creation Protocol (AHICP)**. Any AI Agent working in this repository, or using it as a template, must treat repository state as durable collaboration infrastructure.

> **Language rule:** Chinese `AGENTS.zh-CN.md` is canonical; this English file is the synchronized mirror.

## Human-facing documentation routing

The AHICP homepage and `docs/HUMAN_GUIDE.md` are the human conceptual entrypoint to the ecosystem. They are designed for people with little or no technical background. Preserve their progressive-disclosure structure and avoid turning them into an Agent bootstrap specification.

For machine configuration, cross-component reconstruction, adoption, upgrade, or deployment, the Starter ecosystem and Agent Retrieval Contract remain authoritative.

## Cross-repository ecosystem routing

When this repository is being used to configure, compose, upgrade, publish, or operate a downstream project together with PPF, Vault Interface, or the Starter, first read `docs/ECOSYSTEM.md`, `ecosystem.yaml`, and the [canonical cross-repository Agent Retrieval Contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.md). Reconstruct all four public component roles before making cross-component decisions.

This ecosystem routing does **not** replace AHICP's repository-internal onboarding. After ecosystem discovery, substantive work inside an AHICP repository still follows `START_HERE.zh-CN.md`, `AHICP_MANIFEST.yaml`, and the onboarding handshake below.

For original or unpublished downstream work, the default full-stack posture is full AHICP + full PPF + Vault Interface, private canonical source, and restricted/authenticated Continuous Web until explicit human public-release authorization. Public links never grant private-state access. Cloudflare human handoffs must follow the shared operational contract and provide numbered operator-level steps, secret boundaries, completion evidence, verification, and rollback.

## 0. Zero-context onboarding: read START_HERE first

Any AI Agent taking over this repository from zero context must, before substantive work, read:

1. `START_HERE.zh-CN.md`
2. `AHICP_MANIFEST.yaml`
3. `AHICP_CONTEXT_INTERFACE.yaml`
4. `BOOTSTRAP_PROMPT.zh-CN.md`
5. `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
6. `docs/working-memory.zh-CN.md`
7. `docs/working-memory/current-focus.zh-CN.md`
8. `docs/working-memory/task-plan.zh-CN.md`

Use Working Memory Index -> Current Focus -> Task Plan first to determine what matters most now and how work should proceed. Then reconstruct task-relevant state from the three Long-Term Memory layers according to the manifest/context interface and output a **AHICP Onboarding Report** using `ONBOARDING_REPORT_TEMPLATE.zh-CN.md`. The report must confirm `AHICP REPOSITORY CONTEXT — ACTIVE`.

Before onboarding is complete, do not perform large-scale structural changes, manuscript rewriting, Framework Approval, broad terminology propagation, or promotion of AI proposals into human commitments.

The current protocol-repository onboarding self-test is recorded in `docs/ONBOARDING_SELF_TEST.zh-CN.md`; it is audit evidence, not normative state.

## 1. Do not depend on chat memory

A particular chat, model, vendor, account memory, hidden scratchpad, or local context is not canonical project memory.

If a human instruction should constrain future work, persist it explicitly in the appropriate repository file.

### Repository-backed context rules

- GitHub is the sole authoritative project-state source;
- file excerpts, Onboarding Reports, summaries, and model memory in the session are non-authoritative cache;
- retrieve only the minimum canonical state required by the current task;
- refetch relevant latest revisions before high-impact judgments and writes;
- after a canonical write, older context copies immediately become `STALE`;
- refetch when later reasoning still depends on the touched file rather than maintaining a second chat truth source;
- prefer GitHub API, MCP, connector/plugin, or equivalent direct repository tools.

See `protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md` and `AHICP_CONTEXT_INTERFACE.yaml`.

### External systems, tool discovery, and human handoff

When work requires an external account, provider, or service:

- where appropriate human authorization already exists, first safely inspect and use available built-in tools, connected plugins/connectors, official MCP servers, provider APIs, official GitHub Apps/integrations, existing repository automation, and approved adapters;
- “installed / enabled / connected” is not evidence that a capability is callable; when capability status affects the execution route or a decision to escalate to a human, perform a real, minimal, preferably read-only capability probe when technically possible and safe;
- prefer official / OAuth / provider-managed / least-secret-handling paths where functionally equivalent;
- never ask a human to paste a password, token, private key, recovery code, or other secret into chat;
- escalate only for identity authorization, account-owner consent, permission grants, non-delegable high-impact decisions, or actions the currently authorized tools genuinely cannot perform;
- keep handoff minimal, request only the necessary current action, assume no technical background, state which values must not be sent to AI, and define a completion condition the AI can independently verify;
- after necessary human authorization, re-read current repository state, re-verify capability/provider actual state, and have the Agent resume later machine-operable work;
- after external operations that affect future project work, verify actual provider state and write the durable result through to the repository; provider UI, chat, and model memory must not become a parallel project truth source.

See §23 of `protocol/SPECIFICATION.zh-CN.md`.

### Authorization scope for durable-state actions

Keep `proposal != authorization != execution != verification != durable write-back`.

A durable write is not automatically high-impact. Before an external or durable-state action whose authorization boundary matters, identify the action class, target, allowed side effects, reversibility assumptions, authorization source, and escalation conditions at a level proportionate to risk.

Do not infer authorization from technical capability, repository/provider state, successful build/deployment, existing endpoints, or upstream changes. A durable human-approved pre-authorization policy may authorize only actions within its recorded scope and never overrides a human-reserved / non-delegable boundary.

At initial configuration of a reusable authorization policy, first have the AI propose appropriate authorization patterns for the situation; where applicable distinguish per-action authorization, bounded pre-authorization, and a mixed policy, with scope, control boundaries, and escalation conditions. The human must select, modify, or reject the pattern before configuration relies on that policy, and the final choice, including its scope, authorization provenance, and escalation conditions, must be written to repository durable state.

Escalate only when the action is non-delegable, authorization is absent/unclear, scope would be exceeded, or impact/reversibility has materially changed. Do not hand routine, reversible, already-authorized machine operations back to the human merely because they persist.

After execution, verify actual state and write the verified result through to repository durable state.

## 2. Preserve three distinct domains

Classify substantive human feedback as one or more of:

- `CONTENT` — research meaning, claims, distinctions, assumptions, questions, conclusions;
- `FORM` — artifact type, prose presentation, typography, layout, citation style, visual system, rendering;
- `PROTOCOL` — collaboration rules, persistence, versioning, approval, handoff, synchronization.

Do not merge these domains merely for convenience.

## 3. Canonical precedence in a research project

### Content chain

`Human content decision > CONTENT_CORE > approved framework > Working Argument Map > derived prose`

### Form chain

`Human form decision > FORM_CORE > external venue constraints / reusable profile > implementation default > rendered artifact`

### Protocol chain

`Human workflow decision > project protocol files > Agent default behavior`

Lower layers must not silently contradict higher layers.

## 4. Upstream-first updates

### CONTENT

1. Record the human decision in the Decision Log.
2. Reconcile the Content Core.
3. Reconcile the Working Argument Map.
4. If the change materially alters an already approved framework, mark the project out of sync and request/create a new framework version.
5. Only then propagate the change into derived prose.

### FORM

1. Record the decision.
2. Reconcile the Form Core.
3. Propagate into typesetting/rendering implementation.
4. Do not turn temporary AI defaults into human preferences.

### PROTOCOL

1. Record the decision.
2. Reconcile protocol/governance files.
3. Update reusable templates if the rule generalizes.

## 5. Working Memory and high-impact Clarification

`docs/working-memory.zh-CN.md` is the Working Memory Index; Current Focus and Task Plan carry the operational resume state required for current work and handoff.

It maintains:

- Current Focus: CURRENT_STAGE / CURRENT_OBJECTIVE / PRIMARY_BLOCKER / IMMEDIATE_NEXT_ACTION;
- Task Plan: ACTIVE_TASKS / NEXT_ACTIONS / TODO / BACKLOG / BLOCKERS / PENDING_HUMAN_DECISIONS / Clarifications / SYNC_DEFECTS;
- Work Log: stage-level progress, direction changes, milestones, and completed-task history.

Clarification is a Working Memory item, not Layer 1.5.

Work Log is outside default required context for a replacement Agent; retrieve it only for historical review, audit, change reconstruction, or current/history conflict.

When AI encounters high-impact, non-trivial uncertainty about authorial intent or key content, do not privately choose an interpretation. Create a Clarification item, then after human resolution perform:

`Working Memory -> human resolution -> Decision Log -> appropriate Long-Term Memory destination`

For human core content, continue:

`Layer 1 Core -> Layer 2 Framework -> Layer 3 Artifact`

After Promotion, mark the Working Memory item `RESOLVED / PROMOTED` and retain only pointers.

Update Working Memory after substantial work cycles, important decisions, blocker changes, and before handoff.

## 6. AI proposals are proposals

An AI-generated thesis, distinction, reorganization, term, layout, or aesthetic choice is not a human commitment merely because it appears in a file.

Until accepted by the human:

- content proposals remain visibly `AI-PROPOSED`;
- form proposals remain outside Form Core;
- protocol proposals remain proposals rather than silently becoming mandatory rules.

## 7. Working Framework vs Approved Framework

The current Argument Map is mutable and AI-maintained. AI may assist in proposing, organizing, and expressing a framework, but it is a collaboration tool and cannot replace human authorization of project purpose, direction, and intellectual architecture or become the ultimate bearer of responsibility.

Human endorsement occurs only through an explicit **Framework Approval Gate**. Before Framework Approval, the human must clearly understand, carefully review item by item, and explicitly confirm every substantive element actually represented in the proposed framework, including core theses, inferential relations, key distinctions, scope conditions, section/chapter functions, and any specific wording included in the framework.

Once approved, create a versioned immutable snapshot such as `FW-001.md`.

Material intellectual changes require a new framework version. Framework Approval is a AHICP governance checkpoint; it must not automatically be expanded into a universal cross-disciplinary theory of authorship, and it does not remove Final Artifact Approval.

AHICP's responsibility principle is that AI may share work, but humans must remain the bearers of responsibility in human–AI collaborative research and inquiry, especially in public dissemination of knowledge.

## 8. Evidence conflicts

Human authorial authority concerns intended claims; it does not authorize suppression of evidence.

If evidence, formal reasoning, or source verification conflicts with an active human commitment:

1. preserve the current authorial intention;
2. surface the conflict explicitly;
3. do not knowingly write a misleading downstream claim;
4. present the issue for human decision;
5. record the resulting decision.

## 9. Final artifact status

AI may produce extensive derived text after Framework Approval, but it remains `DERIVED-PROVISIONAL` until final human review.

Do not represent an artifact as submission-ready or human-approved unless the relevant final approval gate has actually been completed.

If the artifact will enter public circulation, Final Artifact Approval must retain identifiable human bearers of responsibility. AI generation, expansion, editing, or checking must not be interpreted as transferring the responsibility-bearing position to AI.

## 10. Memory scaling

Canonical files should remain compact enough for routine onboarding. Detailed history can grow in logs, evidence files, and archives.

When history becomes large:

- preserve originals;
- create indexes/summaries;
- keep current-state cores concise;
- retrieve historical detail selectively.

The goal is recoverable project memory, not forcing every Agent to ingest the entire archive.

## 11. Handoff criterion

A new competent AI Agent should be able to reconstruct the project's active state without access to the original conversation history.

If this is not possible, the project has a persistence defect.

## 12. Multi-pass audits are review-and-repair loops

If the human requests a multi-pass audit, each pass must include:

1. review;
2. identification of defects/omissions;
3. repair or implementation;
4. verification of the repair.

Do not interpret “review three times” as three passive readings followed by a single repair. After the requested cycles, perform a separate post-repair audit when requested.

## 13. Maintain the methodology article as a governed research artifact

This repository has two major outputs:

1. the executable AHICP open protocol;
2. a methodology article explaining and critically developing the protocol.

For the methodology article, read in this order:

1. `docs/working-memory.zh-CN.md` (Index)
2. `docs/working-memory/current-focus.zh-CN.md`
3. `docs/working-memory/task-plan.zh-CN.md`
4. `paper/METHODOLOGY_ARTICLE_CONTENT_CORE.zh-CN.md`
5. `paper/METHODOLOGY_ARTICLE_FORM_CORE.zh-CN.md`
6. `paper/METHODOLOGY_ARTICLE_FRAMEWORK_STATUS.zh-CN.md`
7. latest Approved Framework if any
8. `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP.zh-CN.md`
9. `evidence/METHODOLOGY_SOURCES.zh-CN.md`
10. `paper/methodology-references.bib`
11. `paper/METHODOLOGY_ARTICLE.zh-CN.md`

Work Log is outside this read chain by default.

The article's Argument Map remains a `WORKING-FRAMEWORK` until explicit human approval. Its draft remains `DERIVED-PROVISIONAL` until applicable approval gates are completed.

The methodology article must obey the AHICP principles it describes. Do not treat AI-proposed terminology or article structure as human-approved merely because it appears in the draft. When external research on authorship, AI policy, epistemic responsibility, automation, or cognition changes factual claims in the article, update the evidence layer first and keep normative AHICP proposals distinct from external publication rules.

## 14. Audit records

Use audit files according to their roles:

- `docs/FOUNDING_IDEA_AUDIT.zh-CN.md` — founding-idea coverage inventory and traceability;
- `docs/THREE_CYCLE_REPAIR_AUDIT.zh-CN.md` — corrected three-cycle `review -> repair -> verify` execution record;
- `docs/FINAL_POST_REPAIR_AUDIT.zh-CN.md` — independent post-repair audit after all three cycles;
- `docs/BILINGUAL_PARITY_AUDIT.zh-CN.md` — bilingual pairing and high-risk semantic synchronization audit.

If these files conflict on process status, later repair/final-audit records govern process interpretation; human decisions in `core/DECISION_LOG.zh-CN.md` remain canonical.

## 15. When using this repository as a template

Read, in order:

1. `protocol/SPECIFICATION.zh-CN.md`
2. `protocol/PERSISTENT_MEMORY.zh-CN.md`
3. `protocol/FRAMEWORK_APPROVAL.zh-CN.md`
4. `protocol/FORM_CONTENT_ROUTING.zh-CN.md`
5. `protocol/FORM_PROFILE_INHERITANCE.zh-CN.md`
6. `protocol/BILINGUAL_SYNC.zh-CN.md`
7. `templates/research-project/README.zh-CN.md`

Then instantiate only human decisions actually supplied for the new project. Unknowns remain explicit rather than being filled by AI assumptions.

## 16. Chinese canonical / English synchronized mirror

AHICP is bilingual.

For substantive Markdown content:

- Chinese is the canonical semantic and editing baseline;
- English is a synchronized translation mirror;
- every substantive Chinese edit must be reflected in English in the same work cycle;
- work is incomplete while the language pair is materially inconsistent;
- if the languages conflict, Chinese governs and English must be repaired;
- new substantive Markdown documents should be created as bilingual pairs.

Preferred naming:

- Chinese canonical: `NAME.zh-CN.md`
- English mirror: `NAME.md` where GitHub-default or compatibility paths matter, otherwise `NAME.en.md`.

Language-neutral technical artifacts such as BibTeX, schemas, code, and raw data need not be duplicated solely for translation, but human-readable guidance around them remains bilingual.

Treat synchronization of a bilingual pair as one atomic editing task.

### Pre-cutover legacy exception

For files predating the bilingual rule, if historical English contains newer substantive development not yet absorbed by Chinese, merge that development into Chinese first so Chinese represents the latest state at cutover, then synchronize English.

After that one-time legacy catch-up, normal development is:

`Human decision -> Chinese canonical -> English synchronized mirror`

English must not independently develop substantive content after cutover.
