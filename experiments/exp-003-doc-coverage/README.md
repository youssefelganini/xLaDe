# EXP-003: Documentation Coverage Check

## Research Question

Can xLaDe enforce documentation discipline across its own structure
without modifying Lean or relying on external tools?

---

## Hypothesis

A lightweight script can detect missing documentation in experiments,
modes, and policies — making doc gaps visible and enforceable via CI.

---

## Enforcement Mechanism

- Script-based: `scripts/check-doc-coverage.sh`
- Checks for README.md in every experiment directory
- Checks for README.md in every mode directory
- Checks for at least one .md file in policies/
- Exits non-zero if any required doc is missing

---

## Scope

- `experiments/` — every subdirectory must have README.md
- `modes/` — every subdirectory must have README.md
- `policies/` — must contain at least one .md file

---

## Non-Goals

- Does not check doc quality or content
- Does not validate Lean files
- Does not enforce doc length or structure

---

## Reversibility

Remove the experiment or the CI step. No state is modified.

---

## Success Criteria

- Missing READMEs are reliably detected
- Well-documented repos pass cleanly
- Output is human-readable and actionable

---

## Exit Criteria

- **Promoted** if integrated into CI as a standard repo check
- **Abandoned** if doc discipline is enforced another way

---

## Mode Integration

| Mode         | Status   |
|--------------|----------|
| Onboarding   | Disabled |
| Stable       | Disabled |
| Experimental | Enabled  |

---

## Status

Active