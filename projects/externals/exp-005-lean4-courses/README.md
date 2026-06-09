# External Project: lean4-courses (BaDaaS)

## Overview

| Field            | Value                                              |
|------------------|----------------------------------------------------|
| Repository       | https://github.com/BaDaaS/lean4-courses            |
| Author           | BaDaaS                                             |
| xLaDe experiment | EXP-005                                            |
| Submodule path   | `experiments/exp-005-lean4-courses/lean4-courses/` |
| First run        | 2026-06-08                                         |
| Result           | success                                            |

---

## Why This Project

This is the first external project in xLaDe with genuinely no
connection to the xLaDe team by code or collaboration. It was
selected for three reasons:

**No Mathlib.** Every real-world Lean 4 project attempted before
this one pulled Mathlib transitively. PFR (Polynomial Freiman-Ruzsa
conjecture proof by Tao et al.) was attempted first but requires
gigabytes of dependency downloads — impractical on a slow connection.
lean4-courses has zero external dependencies.

**Real code.** 32 course modules covering Lean 4 from startup to
type theory foundations. Not toy examples — structured educational
content with examples, exercises, and solutions.

**Personal connection.** This repository was independently starred
by the xLaDe lead as a personal Lean 4 learning resource before
this experiment was conceived. It was not created for xLaDe.

---

## Project Structure
lean4-courses/
├── lakefile.lean           33 lean_lib targets, no require blocks
├── lake-manifest.json
├── lean-toolchain          leanprover/lean4:v4.29.0
├── 0000-startup/
│   ├── Examples.lean
│   ├── Exercises.lean
│   ├── README.md
│   └── Solutions.lean
├── ... (32 modules total)
└── Solutions/
├── S0010.lean
├── S0011.lean
└── S0014.lean

**Modules:** 0000-startup through 0031-type-theory-foundations  
**Targets:** 33 lean_lib targets  
**Dependencies:** none — stdlib only, no Mathlib, no external packages

---

## Selection Process

Before settling on lean4-courses, two other projects were attempted:

**PFR (teorth/pfr)** — Polynomial Freiman-Ruzsa conjecture proof.
Rejected: pulls Mathlib transitively via AddCombi. Download
estimated at 18+ minutes on available connection (454 KB/s).
Toolchain: v4.29.0.

**lean4-courses (BaDaaS)** — selected. Zero dependencies confirmed
from lakefile inspection before attempting build.

The Mathlib problem is real: even projects that appear to have only
2 dependencies can hide Mathlib one layer down. Checking the full
transitive dependency chain before attempting a build is now a
standard step in xLaDe's external project integration process.

---

## Toolchain Findings

| Field                 | Value                                 |
|-----------------------|---------------------------------------|
| Pinned toolchain      | leanprover/lean4:v4.29.0              |
| Toolchain used        | leanprover/lean4:v4.30.0              |
| Mismatch              | yes — minor version bump              |
| Override method       | lean-toolchain overwritten in script  |
| Dependencies          | none (stdlib only)                    |
| Mathlib               | absent (direct and transitive)        |

v4.29.0 was not locally available at the time of first run. Download
estimated at 18+ minutes. v4.30.0 was substituted. The build passed
cleanly, indicating the minor version bump is backward compatible
for stdlib-only Lean 4 code — at least for this project.

This is a finding, not just a workaround. It suggests that
stdlib-only Lean 4 projects are more resilient to minor toolchain
version bumps than Mathlib-dependent projects. Further testing
required to confirm.

---

## First Run Results

| Field       | Value                                    |
|-------------|------------------------------------------|
| Date        | 2026-06-08 16:51:50                      |
| Status      | success                                  |
| Build time  | ~650ms (Solutions 321ms, Examples 324ms) |
| Build jobs  | 4                                        |
| Command     | xlade run exp-005-lean4-courses          |

Second run showed `Replayed Solutions` and `Replayed Examples` —
lake used cached `.olean` files. Expected behaviour.

---

## Open Questions

1. Does lean4-courses build on `v4.29.0` as originally pinned?
2. Does it build on `leanprover/lean4:stable`?
3. At what future version does it first break, if any?
4. Do the `Exercises.lean` files (with `sorry`) compile cleanly?
5. Can xLaDe detect toolchain breakage automatically when it occurs?

Systematic toolchain compatibility testing is planned for v1.8.0.

---

## Lessons for xLaDe

**Check transitive dependencies before attempting a build.** A
two-dependency project can still require gigabytes of downloads if
either dependency pulls Mathlib.

**Minor toolchain version bumps are survivable for stdlib-only code.**
v4.29.0 → v4.30.0 worked here. This may not hold for all projects.

**Document the selection process, not just the result.** The PFR
attempt produced useful data even though it was abandoned. Failed
attempts belong in the research log.