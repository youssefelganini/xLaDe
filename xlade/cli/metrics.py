import os
import json


def run():
    _show_run_history()
    print()
    _show_research_artifacts()


def _show_run_history():
    metrics_path = os.path.join(".xlade", "metrics.json")

    if not os.path.isdir(".xlade"):
        print("xLaDe not initialized. Run `xlade init` first.")
        return

    if not os.path.isfile(metrics_path):
        print("No experiment runs recorded yet.")
        return

    try:
        with open(metrics_path, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError):
        print("metrics.json is unreadable or corrupted.")
        return

    if not data:
        print("No experiment runs recorded yet.")
        return

    print(f"Run history ({len(data)} total):\n")

    col_id    = max(len(r["experiment_id"])   for r in data)
    col_mode  = max(len(r.get("mode", ""))    for r in data)
    col_ts    = max(len(r.get("timestamp", "")) for r in data)
    col_st    = max(len(r.get("status", ""))  for r in data)

    col_id   = max(col_id,   13)
    col_mode = max(col_mode,  4)
    col_ts   = max(col_ts,   19)
    col_st   = max(col_st,    6)

    header = (
        f"{'Experiment':<{col_id}}  "
        f"{'Mode':<{col_mode}}  "
        f"{'Timestamp':<{col_ts}}  "
        f"{'Status':<{col_st}}"
    )
    divider = "-" * len(header)

    print(header)
    print(divider)

    for r in data:
        status = r.get("status", "unknown")
        symbol = "✅" if status == "success" else "❌" if status == "failed" else "⏸"
        print(
            f"{r['experiment_id']:<{col_id}}  "
            f"{r.get('mode', ''):<{col_mode}}  "
            f"{r.get('timestamp', ''):<{col_ts}}  "
            f"{symbol} {status}"
        )


def _show_research_artifacts():
    research_dir = "metrics"

    if not os.path.isdir(research_dir):
        return

    files = [f for f in os.listdir(research_dir) if f.endswith(".md")]
    if not files:
        return

    print("Research artifacts:")
    for f in sorted(files):
        print(f"  - {f}")