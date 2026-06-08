# EXP-005: Lean4 Courses

## Research Question

Can xLaDe wrap and execute a real external Lean 4 project with zero
code connection to xLaDe, and record full environment metadata in a
reproducible way?

---

## Hypothesis

An external Lean 4 repository with no knowledge of xLaDe can be
integrated as a submodule, executed via `lake build`, and produce
reproducible results with full metadata recorded — without modifying
the project source or the Lean kernel.

---

## Project

**Repository:** https://github.com/BaDaaS/lean4-courses  
**Author:** BaDaaS  
**Submodule path:** `experiments/exp-005-lean4-courses/lean4-courses/`

A hands-on Lean 4 crash course covering 32 topics from basic types
to advanced metaprogramming and type theory foundations. Designed for
mathematicians and computer scientists learning Lean 4 from scratch.

**Modules included:**
- 0000-startup through 0031-type-theory-foundations
- Each module contains Examples.lean and Solutions.lean
- StandaloneSolutions for selected modules (S0010, S0011, S0014)

**Total targets:** 33 lean_lib targets  
**Dependencies:** none — stdlib only, no Mathlib, no external packages

---

## Personal Note

This repository was independently discovered and starred by the xLaDe
lead before this experiment was conceived. It was being studied as a
personal Lean 4 learning resource. It has no code connection to xLaDe
by design or collaboration. It was selected as EXP-005 because it was
already known to be useful Lean 4 material and because it met the
criteria: external, zero dependencies, real code.

---

## Enforcement Mechanism

- Script-based: `scripts/experiments/run-exp-005.sh`
- Runs `lake build` inside the project submodule directory
- Exit code determines pass/fail
- Toolchain overridden to locally available version (see Toolchain Note)

---

## Toolchain Note

This experiment was first run against `leanprover/lean4:v4.30.0`.

The repository pins `leanprover/lean4:v4.29.0`. At the time of the
first run, v4.29.0 was not locally available and downloading it was
impractical on the available connection (~454 KB/s, estimated 18+ min).

v4.30.0 was used as a substitute. The build passed cleanly.

This is an honest limitation of the first run, not a flaw in the
experiment design. It raises open research questions documented in
METRICS.md.

---

## Success Criteria

`compilation` — `lake build` exits 0 with all targets checked.

Failure is any non-zero exit from `lake build`.

---

## Scope

- `experiments/exp-005-lean4-courses/lean4-courses/` — the external project
- No modifications to xLaDe core, Lean kernel, or project source
- Toolchain file overridden in script only, not committed upstream

---

## Non-Goals

- Does not test proof correctness beyond Lean's type checker
- Does not test individual exercise files (only Solutions and Examples)
- Does not modify the external project in any way
- Does not test all toolchain versions

---

## Reversibility

Remove the experiment directory and submodule entry from `.gitmodules`.
No xLaDe core files are affected.

---

## Exit Criteria

- **Promoted** if xLaDe can reliably build and record metadata for
  external projects with zero dependencies, informing the v1.8.0
  compatibility framework
- **Abandoned** if the submodule approach proves unworkable or the
  project becomes unmaintained

---

## Mode Integration

| Mode         | Status   |
|--------------|----------|
| Onboarding   | Disabled |
| Stable       | Disabled |
| Experimental | Enabled  |

---

## Relationship to EXP-004

EXP-004 was the first external project integrated as a submodule, but
it was authored by the xLaDe lead. EXP-005 is the first experiment
wrapping a project with genuinely no connection to xLaDe by code or
collaboration. The non-invasive claim is stronger here.

---

## Status

Active
