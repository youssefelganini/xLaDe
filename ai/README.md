# xLaDe AI Module

This directory contains everything related to artificial intelligence
and large language models in the context of xLaDe.

It is not a polished integration. It is a research log - trials,
failures, successes, comparisons, criticisms, and ideas, all documented
honestly as they happen.

---

## What This Contains

**experiments/** — using AI models to assist with xLaDe experiments:
writing enforcement scripts, interpreting results, proposing new
experiment ideas.

**lean_proof_assistance/** — testing AI models on Lean 4 proof tasks
relevant to xLaDe: writing simple proofs, diagnosing elaboration errors,
translating proofs to human-readable form.

**code_review/** — submitting xLaDe source code to AI models and
documenting their feedback, criticisms, and suggestions.

**benchmarks/** — structured comparisons across models on defined tasks.
Same prompt, same context, different models. Results recorded verbatim,
analysis written separately.

**integrations/** — ideas and early experiments for integrating AI
assistance into the xLaDe CLI and experiment workflow.

---

## Models

See models.md for the full list of models tested, their versions,
quantization, hardware, and any relevant notes.

Current local models:
- DeepSeek R1 Distill Qwen 14B (Q4_K_M)
- Microsoft Phi-4 Reasoning Plus 14B (Q4_K_M)

---

## Principles

- Outputs are recorded verbatim before any editing or analysis
- Failures are documented as carefully as successes  
- Model, version, date, and prompt are always recorded with results
- AI suggestions are evaluated critically, not treated as authoritative
- No AI output is committed to xLaDe core without human review and understanding
- For use policy, see [docs/AI_USE.md](docs/AI_USE.md)

---