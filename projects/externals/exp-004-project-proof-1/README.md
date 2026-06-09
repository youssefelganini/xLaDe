# External Project: exp-004-project-proof-1

## Overview

| Field            | Value                                                            |
|------------------|------------------------------------------------------------------|
| Repository       | https://github.com/LakshitSinghBishtTM/exp-004-project-proof-1   |
| Author           | Lakshit Singh Bisht (independent of xLaDe)                       |
| xLaDe experiment | EXP-004                                                          |
| Submodule path   | `experiments/exp-004-project-proof-1/exp-004-project-proof-1/`   |
| First run        | 2026-06-07                                                       |
| Result           | success                                                          |

---

## Why This Project

EXP-004 was designed to validate the submodule integration pattern
before attempting genuinely external projects. The repository is
independent — it has its own git history, its own lakefile, its own
lean-toolchain — but was authored by the xLaDe lead as a known-good
test case.

The distinction from EXP-005 is important: EXP-004 proves the
mechanism works. EXP-005 proves the mechanism works on code written
by someone else.

---

## Project Structure
exp-004-project-proof-1/
├── lakefile.lean
├── lake-manifest.json
├── lean-toolchain          leanprover/lean4:stable
├── LICENSE
└── Proofs/
└── Basic.lean          5 theorems

**Proofs included:**
- `add_comm_test` — commutativity of addition
- `add_assoc_test` — associativity of addition
- `zero_add_test` — zero as left identity
- `imp_trans_test` — transitivity of implication
- `and_comm_test` — commutativity of conjunction

---

## Toolchain Findings

| Field                 | Value                       |
|-----------------------|-----------------------------|
| Pinned toolchain      | leanprover/lean4:stable     |
| Toolchain used        | leanprover/lean4:stable     |
| Mismatch              | none                        |
| Dependencies          | none (stdlib only)          |
| Mathlib               | absent                      |

No toolchain override required. Clean match with xLaDe's own pin.

---

## Integration Notes

One issue encountered during setup: `lake` was not on PATH inside
the bash subprocess spawned by Python. Fixed by sourcing
`~/.elan/env` at the top of the run script. This became standard
practice for all subsequent experiment scripts.

Second run showed `Build completed successfully (0 jobs)` — lake
used cached `.olean` files. Expected behaviour.

---

## First Run Results

| Field       | Value                             |
|-------------|-----------------------------------|
| Date        | 2026-06-07                        |
| Status      | success                           |
| Build jobs  | 0 (cached)                        |
| Command     | xlade run exp-004-project-proof-1 |

---

## Open Questions

- Does the proof set remain compilable as Lean stable advances?
- At what future toolchain version does it first require changes?
- Can xLaDe detect the breakage automatically when it occurs?

---

## Lessons for xLaDe

The elan PATH fix (`source ~/.elan/env`) is essential for any
experiment script invoking lake or lean. Without it, scripts fail
even when elan is correctly installed. This is now documented in
`scripts/README.md` and applied to all experiment scripts.