# AGENTS.md — Project AHICP Contract

This project follows the AI-Assisted Human Inquiry and Creation Protocol.

> **Language:** Chinese `AGENTS.zh-CN.md` is canonical; this English file is the synchronized mirror. Projects initialized from this template use Chinese canonical + English synchronized mirror unless the human explicitly chooses different language governance.

## Zero-context onboarding

Before substantive work, any new AI Agent must read:

1. `START_HERE.zh-CN.md`
2. `AHICP_MANIFEST.yaml`
3. `AHICP_CONTEXT_INTERFACE.yaml`
4. `BOOTSTRAP_PROMPT.zh-CN.md`
5. `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
6. `docs/working-memory.zh-CN.md`
7. `docs/working-memory/current-focus.zh-CN.md`
8. `docs/working-memory/task-plan.zh-CN.md`

Use Working Memory Index -> Current Focus -> Task Plan first to identify the resume point. Then reconstruct task-relevant state from the three Long-Term Memory layers according to the manifest/context interface and output a AHICP Onboarding Report using `ONBOARDING_REPORT_TEMPLATE.zh-CN.md`. The report must confirm `AHICP REPOSITORY CONTEXT — ACTIVE`. Later dynamic state is always retrieved from the latest canonical GitHub revision on demand.

Before the onboarding handshake is complete, do not perform large-scale structural changes, Framework Approval, or promotion of AI proposals into human commitments.

## Working Memory

Working Memory Area consists of Index, Current Focus, Task Plan, and Work Log.

- Current Focus stores what matters most now;
- Task Plan stores dynamic tasks, TODOs, blockers, pending human decisions, Clarifications, and sync defects;
- Work Log stores stage history primarily for later human review.

**Work Log is outside default onboarding context for a replacement Agent.** Retrieve it only for human historical review, dedicated audit, reconstruction of direction changes, or current/history conflict.

Clarification is a Working Memory item, not Layer 1.5. After human resolution, perform Promotion into the appropriate Long-Term Memory destination and mark the item `RESOLVED / PROMOTED`.

Update Current Focus / Task Plan after substantial work cycles and before handoff. Update Work Log periodically at meaningful milestones rather than after every micro-action.

## Repository-backed context

- GitHub is the sole authoritative project-state source;
- session summaries/excerpts are non-authoritative cache;
- selectively retrieve according to the current CONTENT / FORM / PROTOCOL route;
- fresh-fetch before high-impact judgments and writes;
- invalidate affected cache after writes;
- do not maintain a second dynamic truth source inside chat.

## External systems, tool discovery, and human handoff

When a task requires an external system, account, or service:

- where appropriate human authorization already exists, first inspect currently available and authorized built-in tools, plugins/connectors, official MCP servers, provider APIs, official integrations, repository automation, and approved adapters;
- installed / enabled / connected does not mean actually callable; when technically possible and safe, perform a real minimal capability probe first;
- prefer official / OAuth / provider-managed / least-secret-handling paths;
- never ask a human to paste passwords, tokens, private keys, or other secrets into chat;
- hand off only identity authorization, account-owner consent, permission grants, non-delegable high-impact decisions, or actions the current tools genuinely cannot perform;
- keep handoff to the fewest steps, request only the necessary current action, assume no technical background, identify values that must not be sent to AI, and define a verifiable completion condition;
- after authorization, have the Agent fresh-read the repository, re-verify provider actual state, and resume later machine-operable work;
- external operations that affect future work must be verified and their durable result written back to the repository.

Provider UI, chat state, and model memory are not durable project authority.

## Authorization scope for durable-state actions

Keep `proposal != authorization != execution != verification != durable write-back`.

Durable state is not automatically high-impact. For an action whose authorization boundary matters, identify action class, target, allowed side effects, reversibility assumptions, authorization source, and escalation conditions at a level proportionate to risk.

Do not infer authorization from technical facts such as capability, repository/provider state, build/deployment success, an existing endpoint, or an upstream change. A durable human-approved pre-authorization policy applies only within its recorded scope and cannot override a human-reserved / non-delegable boundary.

Escalate only when authorization is genuinely missing, the action is non-delegable, scope would be exceeded, or impact/reversibility materially changes. Otherwise continue authorized machine-operable execution, verify actual state, and write the verified result back to durable repository state.

## Protocol source

At project initialization record:

- upstream repository: `ChongLiuPhil/AI-Assisted-Human-Inquiry-and-Creation-Protocol`
- AHICP version: `0.3.0-draft` (replace with actual adopted version/tag/commit)
- adopted commit/tag: `UNRESOLVED — record at initialization`

Future Agents must not silently assume later upstream AHICP rules have already been adopted by this project. Protocol upgrades require an explicit project decision.

## Task-relevant Long-Term Memory retrieval

After Working Memory Index -> Current Focus -> Task Plan, selectively retrieve according to task route:

1. `core/CONTENT_CORE.zh-CN.md` for CONTENT tasks;
2. `core/FORM_CORE.zh-CN.md` for FORM tasks;
3. recent relevant `core/DECISION_LOG.zh-CN.md` entries;
4. `docs/framework-status.zh-CN.md`;
5. latest Approved Framework if any;
6. `docs/argument-map.zh-CN.md`;
7. relevant artifact and evidence files;
8. English mirrors when needed for bilingual parity.

Legacy `docs/clarification-register.zh-CN.md` is only a compatibility pointer and is not part of the active-state required-read path.

## Repository state outranks chat memory

Do not treat an old Agent's chat context as canonical project state. Durable human decisions must be promoted into repository files.

## Route human feedback

Classify substantive instructions as:

- `CONTENT`
- `FORM`
- `PROTOCOL`
- or multi-tag.

Persist first, then propagate upstream-first.

## Content rules

Human content decisions outrank AI drafts. AI proposals remain visibly pending until accepted.

The AI Agent is a collaboration tool. Do not characterize AI as a cognitive subject or use “AI performs cognitive labor / cognitive tasks” as normative terminology; identify the concrete search, synthesis, drafting, restructuring, checking, and related work AI performs or assists.

The purpose, central problem, and direction of the research or creative project must originate with the human or be explicitly authorized by the human. More precisely, humans must remain the bearers of responsibility; AI may share work but cannot become the ultimate bearer of responsibility for project purpose, core judgment, framework authorization, or public dissemination of knowledge.

## Form rules

Human form decisions outrank rendering defaults. Do not infer durable author preferences from temporary tool choices.

Where appropriate, distinguish reusable author preference, artifact-type profile, project-specific rule, external constraint, and temporary default.

## Clarification rules

If there is high-impact uncertainty about core claims, key concepts, terminology/translation, scope, major inferential relations, or section functions, write it first into the Clarification area in `docs/working-memory/task-plan.zh-CN.md`; do not privately choose an interpretation and propagate it.

Mark the item `BLOCKING / NON-BLOCKING`. After human resolution perform:

`Task Plan / Clarification -> Decision Log -> appropriate Long-Term Memory`

Then update Argument Map and artifact as required.

Run a Working Memory / Clarification Scan before Framework Approval, formal translation, large-scale expansion, and Final Review.

## Framework rules

`docs/argument-map.zh-CN.md` is an AI-maintained working structure and is not automatically human-endorsed.

Create `docs/frameworks/FW-xxx.zh-CN.md` and its English mirror only after explicit human Framework Approval. Do not silently modify an approved snapshot.

The Approved Framework is the primary substantive intellectual baseline and the structural anchor of core intellectual responsibility borne by humans. Before Framework Approval, the human must clearly understand, carefully review, and explicitly confirm every substantive element actually represented in the proposed framework, including core theses, inferential relations, key distinctions, scope conditions, section/chapter functions, and any specific wording included in the framework. Distinguish framework-level defects from local defects introduced only in later AI expansion.

AI may help construct the framework, but it cannot become the ultimate bearer of intellectual responsibility for it.

## Evidence rules

If evidence conflicts with a current human commitment, surface the conflict explicitly. Do not suppress counterevidence or silently rewrite the human position.

## Artifact status

AI-expanded prose remains `DERIVED-PROVISIONAL` until the applicable final human approval is recorded.

If the artifact will enter public circulation, Final Artifact Approval must retain identifiable human bearers of responsibility. AI generation, expansion, editing, or checking must not be interpreted as transferring ultimate responsibility for public knowledge dissemination to AI.

## Bilingual synchronization

- Chinese canonical is the human editing/review baseline;
- English mirror must be synchronized in the same work cycle;
- if the languages conflict, Chinese governs;
- material bilingual mismatch is a synchronization defect;
- new substantive Markdown files should be paired at creation.

## Handoff criterion

A new competent Agent should be able to continue the project from repository state alone, without the original chat transcript.
