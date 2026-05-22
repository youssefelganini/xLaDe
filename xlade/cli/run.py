import os
import time
import json
import subprocess
import tomllib
from xlade.core.errors import error


def run(exp_id):
    if not os.path.isdir(".xlade"):
        error(
            "Workspace not initialized",
            "No .xlade directory found.",
            "Run `xlade init` in this project."
        )
        return

    exp_path = os.path.join("experiments", exp_id)
    if not os.path.isdir(exp_path):
        print(f"Experiment not found: {exp_id}")
        return

    config_path = os.path.join(exp_path, "experiment.toml")
    if not os.path.exists(config_path):
        print(f"No experiment.toml found for {exp_id}")
        return

    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
    except Exception as e:
        print(f"Failed to parse experiment.toml: {e}")
        return

    home = os.path.expanduser("~")
    mode_file = os.path.join(home, ".xlade", "mode")

    current_mode = "unknown"
    if os.path.exists(mode_file):
        with open(mode_file) as f:
            current_mode = f.read().strip()

    allowed_modes = config.get("allowed_modes", [])
    if allowed_modes and current_mode not in allowed_modes:
        print(f"Experiment {exp_id} is not allowed in mode: {current_mode}")
        print(f"Allowed modes: {', '.join(allowed_modes)}")
        return

    lean_toolchain = config.get("lean_toolchain", "unspecified")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    exp_type = config.get("type", "unknown")
    entry = config.get("entry", None)

    print(f"Running experiment: {exp_id}")
    print(f"Mode: {current_mode}")
    print(f"Required Lean: {lean_toolchain}")
    print(f"Timestamp: {timestamp}")

    status = _execute(exp_type, entry)

    with open(".xlade/last-run", "w") as f:
        f.write(exp_id + "\n")

    _write_metrics(exp_id, current_mode, lean_toolchain, timestamp, config, status)

    print(f"Status: {status}")


def _execute(exp_type, entry):
    if exp_type == "script-policy" and entry:
        if not os.path.isfile(entry):
            print(f"Entry script not found: {entry}")
            return "error"

        if not os.access(entry, os.X_OK):
            os.chmod(entry, 0o755)

        result = subprocess.run(
            ["bash", entry],
            capture_output=False,
        )
        return "success" if result.returncode == 0 else "failed"

    print("Execution: simulated")
    return "simulated"


def _write_metrics(exp_id, mode, lean_toolchain, timestamp, config, status):
    metrics_path = os.path.join(".xlade", "metrics.json")

    existing = []
    if os.path.exists(metrics_path):
        try:
            with open(metrics_path, "r") as f:
                existing = json.load(f)
        except (json.JSONDecodeError, IOError):
            existing = []

    entry = {
        "experiment_id": exp_id,
        "experiment_name": config.get("name", exp_id),
        "type": config.get("type", "unknown"),
        "mode": mode,
        "lean_toolchain": lean_toolchain,
        "timestamp": timestamp,
        "status": status,
    }

    existing.append(entry)

    with open(metrics_path, "w") as f:
        json.dump(existing, f, indent=2)