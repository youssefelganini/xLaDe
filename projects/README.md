# xLaDe Projects

This directory contains two types of project documentation:

- `demo/` — working demonstrations of xLaDe in action
- `externals/` — external Lean 4 projects that xLaDe has wrapped and studied

---

## demo/

Two documents showing xLaDe working in practice:

- `DEMO_SESSION.md` — a real terminal session with actual output, no
  editing, no cleanup. What xLaDe looks like when you run it.
- `GETTING_STARTED.md` — a guided walkthrough for someone running
  xLaDe for the first time, with explanation at each step.

## externals/

Documentation of external Lean 4 projects that xLaDe has integrated
as git submodules and executed via `xlade run`.

Each subdirectory corresponds to an experiment wrapping an external
project. It contains findings from the first run, toolchain notes,
open research questions, and anything unexpected that was discovered
during integration.

This is where xLaDe's non-invasive ecosystem layer claim is tested
against real code written by people who have never heard of xLaDe.

---

## Relationship to Experiments

The experiments themselves live in `experiments/`. This directory is
not for execution — it is for documentation and reflection. The
findings here inform the research direction and the roadmap.

- Execution → `experiments/`
- Findings → `projects/externals/`
- Demonstration → `projects/demo/`
