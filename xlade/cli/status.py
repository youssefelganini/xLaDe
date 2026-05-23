import os
import json


def run():
    print("xLaDe Status\n")

    home = os.path.expanduser("~")
    mode_file = os.path.join(home, ".xlade", "mode")

    mode = "unknown"
    if os.path.exists(mode_file):
        with open(mode_file) as f:
            mode = f.read().strip()

    print(f"Mode:     {mode}")

    if not os.path.isdir(".xlade"):
        print("\nxLaDe is not initialized in this directory.")
        return

    last_run_file = os.path.join(".xlade", "last-run")
    last_exp = "none"
    if os.path.exists(last_run_file):
        with open(last_run_file) as f:
            last_exp = f.read().strip()

    print(f"Last run: {last_exp}")

    metrics_path = os.path.join(".xlade", "metrics.json")

    if not os.path.isfile(metrics_path):
        print("\nNo experiment runs recorded yet.")
        return

    try:
        with open(metrics_path, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError):
        print("\nmetrics.json is unreadable or corrupted.")
        return

    if not data:
        print("\nNo experiment runs recorded yet.")
        return

    total = len(data)
    success = sum(1 for r in data if r.get("status") == "success")
    failed  = sum(1 for r in data if r.get("status") == "failed")
    other   = total - success - failed

    print(f"\nTotal runs: {total}")
    print(f"  ✅ success:   {success}")
    if failed:
        print(f"  ❌ failed:    {failed}")
    if other:
        print(f"  ⏸  other:     {other}")

    print("\nRecent runs:")
    for r in data[-5:]:
        status = r.get("status", "unknown")
        symbol = "✅" if status == "success" else "❌" if status == "failed" else "⏸"
        print(f"  {symbol} {r['experiment_id']:<20} {r.get('timestamp', '')}")