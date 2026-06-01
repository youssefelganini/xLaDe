# End-to-End Trace

This document is a **narrative execution trace** of a complete xLaDe session
from a fresh clone to running all three active experiments and reviewing results.

This is not a tutorial. It shows exactly what happens at each step — commands,
output, and state changes — so you know what to expect before you run anything.

For installation help, see [`INSTALL.md`](../INSTALL.md).  
For a command reference, see [`CLI_DEMO.md`](CLI_DEMO.md).

---

## Scenario

A researcher wants to evaluate xLaDe's three active experiments:

- **EXP-001** — Enforced Proof Review (requires Lake)
- **EXP-002** — Kernel Boundary Violation Detection
- **EXP-003** — Documentation Coverage Check

The goal is to run all three, understand what each does, and inspect the
results. The machine has Python 3.12 and git, but Lean is not yet installed.

---

## Step 1 — Clone the Repository

```sh
git clone --recurse-submodules https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
```

The `--recurse-submodules` flag initialises `lean-core/` automatically.
Without it, `lean-core/` will be an empty directory and `xlade doctor`
will report it as missing.

---

## Step 2 — Install the CLI

```sh
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

After this, `xlade` is available as a command directly — no need to use
`./bin/xlade`.

---

## Step 3 — Check the Environment

```sh
xlade doctor
```

Output on a machine without Lean installed:

```
xLaDe Doctor Report
===================

❌ elan not found
   elan is the Lean version manager and is required to install
   lake and lean. To install it, run:

     curl https://elan.lean-lang.org/elan-init.sh -sSf | sh

   Then restart your shell and run `xlade doctor` again.
lake not found
   lake is the Lean build tool and is needed to run lean-policy
   experiments (e.g. EXP-001). It is installed automatically
   by elan once a lean-toolchain file is present. Steps:

     1. Install elan (see above if not installed)
     2. cd into your xLaDe directory
     3. Run: elan toolchain install leanprover/lean4:stable
     4. lake should now be available on your PATH
✅ lean-core submodule present
✅ lean-toolchain present  (leanprover/lean4:stable)
⚠️  workspace not initialised
   Run `xlade init` to set up the project workspace.

=========================

❌ 2 issues found. Fix the items above and re-run `xlade doctor`.
```

The researcher notes that EXP-001 will be skipped without Lake, but
EXP-002 and EXP-003 are script-based and will run fine. They proceed.

---

## Step 4 — Initialise the Workspace

```sh
xlade init
```

```
Initialized xLaDe workspace.
```

This creates `.xlade/` in the current directory with `experiments.lock`
and `last-run`. No Lean files are touched.

Running it again is safe:

```sh
xlade init
```

```
xLaDe already initialized in this directory.
```

---

## Step 5 — Set the Mode

```sh
xlade mode experimental
```

```
xLaDe mode set to: experimental
```

This writes `experimental` to `~/.xlade/mode`. Experiments with
`allowed_modes = ["experimental"]` will now be eligible to run.

---

## Step 6 — Discover Experiments

```sh
xlade list experiments
```

```
Available experiments:

EXP-001  active   [experimental]
EXP-002  active   [experimental]
EXP-003  active   [experimental]
```

All three are active and allowed in experimental mode.

---

## Step 7 — Run EXP-002 (Kernel Boundary Violation Detection)

Starting with EXP-002 since it has no Lean dependency.

```sh
xlade run EXP-002
```

```
Running experiment: EXP-002
Mode: experimental
Required Lean: leanprover/lean4:stable
Timestamp: 2026-06-01 14:10:03
✅ Kernel untouched.
Status: success
```

EXP-002 runs `scripts/check-kernel.sh`, which checks whether any files
under `lean-core/` have been modified relative to `origin/main`. On a
clean clone, nothing is modified, so it passes.

---

## Step 8 — Run EXP-003 (Documentation Coverage Check)

```sh
xlade run EXP-003
```

```
Running experiment: EXP-003
Mode: experimental
Required Lean: leanprover/lean4:stable
Timestamp: 2026-06-01 14:10:41
xLaDe Doc Coverage Check
=========================
✅ experiment: experiments/exp-001-proof-review/
✅ experiment: experiments/exp-002-kernel-boundary/
✅ experiment: experiments/exp-003-doc-coverage/
✅ mode: modes/experimental/
✅ mode: modes/onboarding/
✅ mode: modes/stable/
✅ policies/ has 4 documentation file(s)
=========================
✅ All documentation checks passed.
Status: success
```

EXP-003 runs `scripts/check-doc-coverage.sh`, which verifies that every
experiment and mode directory has a `README.md`, and that `policies/`
contains at least one `.md` file.

---

## Step 9 — Run EXP-001 (Enforced Proof Review)

EXP-001 requires Lake. On this machine it is not installed.

```sh
xlade run EXP-001
```

```
Running experiment: EXP-001
Mode: experimental
Required Lean: leanprover/lean4:stable
Timestamp: 2026-06-01 14:11:15
Execution: lake not found — cannot run lean-policy experiment.
Install Lean 4 and Lake via elan to enable full execution.
  curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
Status: skipped
```

The experiment is recorded as `skipped` — not failed. The distinction
matters: `skipped` means the environment prevented execution, not that
the experiment logic failed. Once Lake is installed, re-running EXP-001
will execute the proof review policy for real.

---

## Step 10 — Review Status

```sh
xlade status
```

```
xLaDe Status

Mode:     experimental
Last run: EXP-001

Total runs: 3
  ✅ success:   2
  ⏸  other:     1

Recent runs:
  ⏸  EXP-001               2026-06-01 14:11:15
  ✅ EXP-003               2026-06-01 14:10:41
  ✅ EXP-002               2026-06-01 14:10:03
```

---

## Step 11 — Review Metrics

```sh
xlade metrics
```

```
Run history (3 total):

Experiment       Mode          Timestamp            Status
---------------------------------------------------------------
EXP-002          experimental  2026-06-01 14:10:03  ✅ success
EXP-003          experimental  2026-06-01 14:10:41  ✅ success
EXP-001          experimental  2026-06-01 14:11:15  ⏸ skipped

Research artifacts:
  - summary.md
```

The full run history is stored in `.xlade/metrics.json` and survives
across sessions.

---

## Step 12 — Install Lean and Re-run EXP-001

The researcher installs elan and the Lean toolchain:

```sh
curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
source ~/.elan/env
elan toolchain install leanprover/lean4:stable
```

Verify Lake is now available:

```sh
xlade doctor
```

```
xLaDe Doctor Report
===================

✅ elan found
✅ lake found
✅ lean-core submodule present
✅ lean-toolchain present  (leanprover/lean4:stable)
✅ workspace initialised (.xlade present)

✅ All checks passed. xLaDe environment looks good.
```

Re-run EXP-001:

```sh
xlade run EXP-001
```

```
Running experiment: EXP-001
Mode: experimental
Required Lean: leanprover/lean4:stable
Timestamp: 2026-06-01 15:30:22
Executing Lake script: enforceReview
xLaDe: enforcing proof review policy
✔ Proofs/Reviewed.lean is reviewed
Status: success
```

EXP-001 runs `lake script run enforceReview` inside the experiment
directory. It reads `Proofs/Reviewed.lean`, confirms the `@reviewed`
marker is present, and passes.

---

## Step 13 — Reset the Workspace

To reset all xLaDe project-local state:

```sh
rm -rf .xlade
```

This removes the workspace directory, run history, and metrics. It does
not touch Lean source files, the kernel, or any experiment code.

To reinitialise from scratch:

```sh
xlade init
```

> **Note:** `rm -rf .xlade` only removes the xLaDe state directory.
> Do not confuse it with `rm -rf /` — that removes the entire filesystem,
> the OS, and everything else. One is a cleanup step. The other is a
> disaster. They look similar. They are not.

---

## Summary

This trace covered a complete xLaDe session:

| Step                | Command                          | Outcome                                        |
|---------------------|----------------------------------|------------------------------------------------|
| Environment check   | `xlade doctor`                   | 2 issues identified, actionable guidance given |
| Workspace setup     | `xlade init`                     | `.xlade/` created                              |
| Mode selection      | `xlade mode experimental`        | Experiments enabled                            |
| Discovery           | `xlade list experiments`         | 3 experiments found                            |
| EXP-002             | `xlade run EXP-002`              | ✅ success — kernel boundary intact            |
| EXP-003             | `xlade run EXP-003`              | ✅ success — all docs present                  |
| EXP-001 (no Lake)   | `xlade run EXP-001`              | ⏸ skipped — lake not found                     |
| EXP-001 (with Lake) | `xlade run EXP-001`              | ✅ success — proof review enforced             |
| Results             | `xlade status` / `xlade metrics` | Full run history visible                       |
| Cleanup             | `rm -rf .xlade`                  | State reset, Lean untouched                    |

xLaDe orchestrates experiments, records state explicitly, and remains
fully reversible at every step. 