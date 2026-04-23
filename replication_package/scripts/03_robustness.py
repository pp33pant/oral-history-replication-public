#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = PACKAGE_ROOT / "source_scripts"
ROBUSTNESS_ROOT = PACKAGE_ROOT / "robustness"
DEFAULT_CHECKS = [
    "r1",
    "r2",
    "r3",
    "r4",
    "r5",
    "r6",
    "r7",
    "r8",
    "r9",
    "r10",
    "r11",
    "r12",
    "r13",
    "r14",
    "r15",
    "r16",
    "r17",
    "r18",
    "r19",
    "measurement_audit",
]
FROZEN_SNAPSHOTS = [
    ROBUSTNESS_ROOT / "causal_robustness_v1" / "robustness_registry_v1.csv",
    ROBUSTNESS_ROOT / "causal_robustness_v1" / "robustness_summary_v1.md",
    ROBUSTNESS_ROOT / "robustness_review_v1.md",
    ROBUSTNESS_ROOT / "robustness_review_key_rows_v1.csv",
    ROBUSTNESS_ROOT / "how_negative_controls_v1.csv",
    ROBUSTNESS_ROOT / "how_negative_controls_report_v1.md",
    ROBUSTNESS_ROOT / "how_observability_model_report_v1.md",
    ROBUSTNESS_ROOT / "how_mnar_sensitivity_report_v1.md",
    ROBUSTNESS_ROOT / "how_archiveability_treatment_assoc_v1.csv",
]


def copy_frozen_snapshot(target_dir: Path) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    for path in FROZEN_SNAPSHOTS:
        if not path.exists():
            continue
        shutil.copy2(path, target_dir / path.name)


def run_full(checks: str) -> None:
    command = [
        sys.executable,
        str(SOURCE_ROOT / "dml_robustness_battery.py"),
        "--output-dir",
        str(ROBUSTNESS_ROOT / "causal_robustness_v1"),
        "--checks",
        checks,
    ]
    print("Running:", " ".join(command), flush=True)
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh packaged robustness artifacts")
    parser.add_argument("--full", action="store_true", help="Re-run the packaged robustness battery")
    parser.add_argument("--checks", default=",".join(DEFAULT_CHECKS))
    args = parser.parse_args()

    copy_frozen_snapshot(ROBUSTNESS_ROOT / "frozen_snapshot")
    if args.full:
        run_full(args.checks)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())