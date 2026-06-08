# Metrics — EXP-004: Project Proof 1

## Enforcement Strength
- Script-based via `lake build`
- Pass/fail determined by exit code
- No semantic analysis beyond Lean type checking

## Scope
- External project only (`exp-004-project-proof-1/` submodule)
- No impact on xLaDe core or Lean kernel

## Friction Introduced
- Requires Lake installed (`elan toolchain install leanprover/lean4:stable`)
- Submodule must be populated (`git submodule update --init --recursive`)
- No friction on xLaDe core workflows

## Reversibility
- Fully reversible — remove experiment directory and submodule reference
- No persistent state introduced outside `.xlade/metrics.json`

## Observed Outcome

First run: 2026-06-07. Status: success.

`lake build` completed with 0 jobs (all proofs already compiled and cached
on first attempt). All 5 theorems in `Proofs/Basic.lean` checked by Lean's
type checker without errors.

One issue encountered during setup: `lake` was not on PATH inside the bash
subprocess spawned by Python. Fixed by sourcing `~/.elan/env` at the top of
the run script. This is expected on macOS and should be treated as standard
practice for all future experiment scripts.

Architecture validated: external Lean 4 project as git submodule inside an
xLaDe experiment directory works as intended. Full metadata recorded in
`.xlade/metrics.json`.

## Limitations
- Only tests compilation, not proof strategy or tactic quality
- Submodule pinned to a specific commit — upstream changes require manual update
- Requires full Lean toolchain — skips cleanly without Lake