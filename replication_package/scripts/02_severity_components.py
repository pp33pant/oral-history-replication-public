#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = PACKAGE_ROOT / "source_scripts"
MODEL_ROOT = PACKAGE_ROOT / "models" / "causal_estimates_v1"


def run_step(script_name: str, *args: str) -> None:
    command = [sys.executable, str(SOURCE_ROOT / script_name), *args]
    print("Running:", " ".join(command), flush=True)
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Re-run packaged severity-component models")
    parser.add_argument("--sample", choices=["main", "complete_case", "full"], default="main")
    args = parser.parse_args()

    run_step(
        "dml_estimation_track1_per_cell_severity_components.py",
        "--sample",
        args.sample,
        "--output-dir",
        str(MODEL_ROOT / "track1_per_cell_severity_components_v1"),
    )
    run_step(
        "dml_estimation_track1_ilr_severity_components.py",
        "--sample",
        args.sample,
        "--output-dir",
        str(MODEL_ROOT / "track1_ilr_severity_components_v1"),
    )
    run_step(
        "dml_estimation_track2_severity_components.py",
        "--sample",
        args.sample,
        "--output-dir",
        str(MODEL_ROOT / "track2_severity_components_v1"),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())