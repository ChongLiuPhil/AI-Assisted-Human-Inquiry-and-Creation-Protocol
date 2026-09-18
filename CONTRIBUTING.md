# Contributing to HARC Protocol

> **Language:** Chinese canonical: `CONTRIBUTING.zh-CN.md`; this English file is the synchronized mirror.

HARC is intended to be an open, inspectable protocol for durable human–AI research collaboration.

## What contributions are welcome?

Examples include:

- critiques of the conceptual model;
- improvements to protocol clarity;
- alternative repository layouts that preserve the same semantic roles;
- examples for books, papers, reports, and interdisciplinary projects;
- machine-readable schemas;
- validation/linting tools;
- agent onboarding tools;
- studies of semantic drift, handoff quality, or human approval interfaces;
- documentation and translations.

## Preserve provenance

Please distinguish among:

- a change to the protocol's core design;
- an implementation suggestion;
- an optional extension;
- a concrete example;
- empirical evidence about whether the protocol works.

Do not present a contributor proposal as an already accepted founder principle.

## Suggested workflow

1. Open an issue describing the problem or proposal.
2. For major protocol changes, explain which invariant is being changed and why.
3. Keep normative changes separate from examples where practical.
4. Use a focused branch and pull request.
5. Update documentation and templates together when behavior changes.

## Compatibility principle

A proposed implementation is HARC-compatible when it preserves the functional distinctions among:

- human content intention;
- human form intention;
- AI operational representation;
- approval state;
- evidence;
- historical decisions;
- derived expression;
- cross-agent persistence.

Exact filenames and platforms may evolve.

## Licensing note

Contribution licensing terms will be finalized together with the repository's explicit open-license decision. See `LICENSE-DECISION.md` before submitting substantial contributions.
