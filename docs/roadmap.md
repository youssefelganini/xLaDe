# xLaDe Roadmap: v1.5.0 → v2.0.0

This document outlines the planned development arc for xLaDe from its
current stable release through the 2.0.0 milestone.

xLaDe follows a research-first development philosophy: releases are
deliberate, documented, and honest about limitations. Not every release
will work perfectly — and that is by design.

---

## v1.5.0 — "The CLI Becomes Real"

**Expected Release - May 2026**

The release where xLaDe stopped being a research document with Python
files next to it and became working software.

- 50-test pytest suite covering all CLI modules
- `pip install -e .` works — xlade is a proper installable command
- EXP-002 executes `check-kernel.sh` for real via subprocess
- EXP-003 (doc coverage) added and executable
- `metrics.json` written on every run, read by `xlade metrics` and `xlade status`
- `xlade metrics` shows aligned run history table with status symbols
- `xlade status` shows run summary with success/fail counts
- `errors.py` duplication removed
- `CODE_OF_CONDUCT.md` contact filled in
- `pyproject.toml` — proper Python packaging

---

## v1.6.0 — "Lean Works Here"

**Expected Release - June 2026**

**Theme:** Make Lean installation understandable and integrate it properly
with the Python CLI.

**Goals:**

- Write proper installation documentation: `elan` → `lean4` → `lake`,
  step by step for Linux
- `xlade doctor` gives actionable guidance, not just "lake not found"
- `xlade/core/lean.py` — clean Python module wrapping subprocess calls
  to `lake` and `lean`, returning structured results
- EXP-001 (Enforced Proof Review) executes for real when Lake is present
- Lean output parsed and surfaced in `xlade run` output meaningfully
- `INSTALL.md` rewritten to reflect actual tested installation steps

**Expected outcome:** A new contributor can follow the docs, install
Lean, and run all three experiments successfully.

---

## v1.7.0 — "Real World Use Trial for serious projects"

**Expected Release - July 2026**

**Theme:** Map real Lean 4 ecosystem projects to experiments. Expect
and document failure honestly.

**Goals:**

- Research and document 2-3 real Lean 4 projects (e.g. PhysLean,
  CS Lean, community proof projects) as candidate experiments
- Write experiment READMEs framing each as a research question
  xLaDe can investigate
- Attempt basic integration, not full execution, but enough to
  understand where the boundaries are
- Document what breaks, why, and what would be needed to fix it
- This release is expected to partially fail and failures are the data

**Philosophy:** xLaDe is a research laboratory. Publishing honest
failure is a feature, not a bug. v1.7.0 exists to find the edges.

**Expected outcome:** 2-3 new experiments in draft/active state,
at least one partially working, with documented findings on the others.

---

## v1.8.0 — "Preservation and Compatibility"

**Expected Release - August 2026**

**Theme:** Metadata, compatibility matrices, and long-term preservation.

**Goals:**

- Expand `experiment.toml` schema with full compatibility metadata:
  validated Lean versions, known breakages, last-tested date
- Compatibility matrix document: which experiments work on which
  Lean versions
- `xlade check` reports compatibility warnings when current Lean
  version differs from experiment's validated version
- Address Lean 4's backward compatibility problem explicitly —
  `docs/REPRODUCIBILITY_AND_COMPATIBILITY.md` finally has tooling
  behind it
- Archive format defined for retired experiments — nothing deleted,
  everything traceable
- `lake-manifest.json` and `lean-toolchain` pinning formally
  documented as part of the reproducibility story

**Expected outcome:** Running an experiment on the wrong Lean version
produces a clear warning. Every experiment has a documented environment
it was validated against.

---

## v1.9.0 — "Production Documentation"

**Expected Release - September 2026**

**Theme:** Documentation rewritten to production standard, with the
personality of people who actually built and use this.

**Goals:**

- Full installation guide tested on clean machines across platforms
- Every CLI command documented with real examples and expected output
- Architecture documentation reflects the actual codebase, not the
  aspirational one
- `docs/` reorganized for clarity — onboarding path clearly marked
- Dev jokes permitted and encouraged in comments and inline notes
  (this is a research tool, not enterprise software)
- `HOW_TO_READ_THIS_REPO.md` updated to reflect v1.9.0 reality
- CHANGELOG for all releases cleaned up and consistent

**Philosophy:** Docs written after the software stabilizes are
accurate. Docs written before go stale. v1.9.0 is the right time.

**Expected outcome:** A new Lean researcher can read the docs,
understand what xLaDe is for, install it, and run their first
experiment without asking anyone for help.

---

## v2.0.0 — "Trust and Identity"

**Expected Release - October 2026**

**Theme:** Not a feature release. A trust, governance, and identity
release. xLaDe declares itself a serious long-term project.

**Two changes only:**

### 1. Signed Commits — Mandatory

- GPG signing required for all commits to main from v2.0.0 onward
- Each contributor and maintainer holds their own GPG key
- Public keys published and verifiable
- GitHub branch protection enforces signed commits
- `CONTRIBUTING.md` documents GPG setup for new contributors
- `security/KEY_MANAGEMENT.md` documents who holds what keys,
  what each controls, and recovery procedures

**Why:** The project has a trust model, a threat model, and a
security policy. Signed commits make those documents real instead
of aspirational. A commit claiming to be from a maintainer but
unsigned is detectable. That matters for a project studying
ecosystem governance.

### 2. Official Website — Primary Entry Point

- The Tor onion service becomes the true primary interface
- Website actively maintained: release notes published there first,
  documentation lives there, project status visible
- GitHub and all mirrors become secondary — development and
  contribution infrastructure, not the canonical public face
- Onion private key held by project lead and CEO, with documented
  offline backup and recovery procedure
- `OFFICIAL_SOURCES.md` updated to reflect the new hierarchy

**Why:** xLaDe already states in `OFFICIAL_SOURCES.md` that the
onion service is the official web presence. v2.0.0 makes that true
rather than aspirational. A project whose stated philosophy is
reducing reliance on centralized infrastructure should not have
GitHub as its real home.

---

## Contributing

If you are interested in contributing to any of these releases,
see `CONTRIBUTING.md` for guidelines.

Discussions about roadmap direction are welcome via GitHub Issues
on the primary repository.

The project is experimental. The roadmap is intentionally flexible.
Community feedback and experimental results guide prioritization.

---

*xLaDe is a living laboratory for Lean 4 ecosystem design.*
*The roadmap exists to be honest about where it is going,*
*not to promise it will arrive on schedule.*