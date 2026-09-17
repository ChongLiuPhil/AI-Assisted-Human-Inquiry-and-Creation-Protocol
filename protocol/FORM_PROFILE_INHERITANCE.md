# Form Profile Inheritance

## Purpose

HARC separates research content from presentation form. This document makes form reuse operational across multiple projects and artifact types.

The human-originated design goal is that an author may develop stable presentation preferences over time while still allowing books, academic papers, articles, reports, and individual projects to use different forms.

## 1. Form layers

A project may draw form constraints from five sources:

1. **Reusable Author Profile** — preferences the human explicitly intends to reuse across projects.
2. **Artifact-Type Profile** — conventions or author decisions specific to a type such as `BOOK`, `ACADEMIC_PAPER`, or `ARTICLE`.
3. **Project-Specific Form Core** — decisions that apply only to the current project.
4. **External Constraint** — requirements imposed by a journal, publisher, institution, style guide, or venue.
5. **Temporary Default** — provisional AI/tool choices made only because no human rule is available yet.

These sources must not be conflated.

## 2. Recommended resolution order

When rules conflict, first identify their source rather than silently choosing one.

A practical implementation order is:

`mandatory external constraint -> explicit project-specific human decision -> applicable artifact-type profile -> reusable author preference -> temporary default`

If a mandatory external constraint conflicts with a human preference, record the conflict explicitly rather than rewriting the preference as though the author changed their mind.

## 3. Reusable author profile

Use a reusable profile only for preferences the human has explicitly generalized beyond one project.

Examples:

- preferred density of headings;
- recurring typography choices;
- footnote philosophy;
- equation presentation;
- preferred visual restraint;
- bilingual terminology conventions.

Do not infer cross-project preference from one accidental or AI-generated implementation.

Template:

`templates/form-profiles/AUTHOR_PROFILE.md`

## 4. Artifact-type profiles

HARC provides separate template profiles for common artifact types.

Initial profiles:

- `templates/form-profiles/BOOK.md`
- `templates/form-profiles/ACADEMIC_PAPER.md`
- `templates/form-profiles/ARTICLE.md`

These files are intentionally mostly unresolved. Their purpose is to provide the correct decision fields without inventing the author's preferences.

A project may add profiles for `REPORT`, `THESIS`, `PRESENTATION`, or other types.

## 5. Project initialization

At initialization, the AI agent should:

1. identify the artifact type;
2. load any explicitly applicable reusable author profile;
3. load the corresponding artifact-type profile;
4. create the project's `core/FORM_CORE.md`;
5. record project-specific overrides and external constraints;
6. leave unspecified fields as `UNRESOLVED`;
7. mark any tool-created fallback as `TEMPORARY-DEFAULT`.

## 6. Persistence rule

A human form correction follows:

`Human decision -> Decision Log -> FORM_CORE -> reusable/type profile if explicitly generalized -> rendering implementation -> artifact`

Do not update a reusable profile merely because the current project changed. The human must indicate that the preference should generalize.

## 7. Portability

The form-profile system is topic-independent. It can be reused across research projects without carrying over any substantive research claims.
