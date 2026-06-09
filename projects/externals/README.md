# External Projects

This directory documents external Lean 4 projects that xLaDe has
wrapped as git submodules and executed via `xlade run`.

---

## What "External" Means

An external project is a Lean 4 repository that:

- Was not written by the xLaDe team for xLaDe
- Has no code connection to xLaDe
- Has no knowledge of xLaDe's existence
- Was added as a git submodule and wrapped with an `experiment.toml`

The non-invasive claim — that xLaDe can study external Lean projects
without modifying them — is tested here.

---

## Current External Projects

| Experiment  | Project                  | Author  | Dependencies | First Run  | Status  |
|-------------|--------------------------|---------|--------------|------------|---------|
| EXP-004     | exp-004-project-proof-1  | Lakshit | none         | 2026-06-07 | success |
| EXP-005     | lean4-courses (BaDaaS)   | BaDaaS  | none         | 2026-06-08 | success |

EXP-004 was authored by myself but exists as a completely
independent repository with no xLaDe code. EXP-005 is the first
project with genuinely no connection to the xLaDe team.

---

## What Gets Documented Per Project

Each subdirectory contains:

- Project overview and repository link
- Why it was selected
- Integration method (submodule path, toml configuration)
- Toolchain findings (pinned version, version used, mismatch if any)
- First run results
- Open research questions raised by the integration
- Anything unexpected discovered during setup

---

## What This Is Not

This is not a curated list of good Lean 4 projects. It is a research
log of projects xLaDe has attempted to wrap, what worked, what
didn't, and what was learned. Failed attempts will be documented here
too when they occur.

---

## Relationship to Experiments

The execution artifacts live in `experiments/`. This directory is for
reflection and findings — what the integration revealed about the
project, the toolchain, and xLaDe's own capabilities.