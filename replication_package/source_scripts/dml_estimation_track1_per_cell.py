#!/usr/bin/env python3
"""Run Track 1 per-cell share DML estimation and write auditable outputs."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from _causal_modeling_runtime_v1 import (
    DESIGN_BASE_COLUMNS,
    ROOT,
    TRACK1_CLASS_OUTCOMES,
    TRACK1_JOINT_OUTCOMES,
    TRACK1_MARGIN_OUTCOMES,
    TRACK1_REGION_OUTCOMES,
    build_primary_covariate_matrix,
    default_track1_specifications,
    ensure_dir,
    load_model_matrix,
    run_plr_track,
)


DEFAULT_OUTPUT_DIR = ROOT / "models" / "causal_estimates_v1" / "track1_per_cell_v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Track 1 per-cell DML estimation")
    parser.add_argument("--sample", choices=["main", "complete_case", "full"], default="main")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--folds", type=int, default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    frame = load_model_matrix(args.sample)
    outcomes = TRACK1_JOINT_OUTCOMES + TRACK1_CLASS_OUTCOMES + TRACK1_REGION_OUTCOMES + TRACK1_MARGIN_OUTCOMES
    encoded_x = build_primary_covariate_matrix(frame, include_auxiliary_flags=False)

    output_dir = Path(args.output_dir)
    ensure_dir(output_dir)
    design = pd.concat(
        [
            frame[DESIGN_BASE_COLUMNS + outcomes],
            encoded_x,
        ],
        axis=1,
    )
    paths = run_plr_track(
        track="track1_per_cell",
        sample=args.sample,
        frame=frame,
        x_matrix=encoded_x,
        design=design,
        outcomes=outcomes,
        specification_map=default_track1_specifications(),
        output_dir=output_dir,
        output_stem="track1_per_cell",
        report_title="Track 1 Per-Cell Report v1",
        script_name=Path(__file__).name,
        folds=args.folds,
    )

    print(f"rows={len(frame)}")
    print(f"design={paths['design']}")
    print(f"task_grid={paths['task_grid']}")
    print(f"estimates={paths['estimates']}")
    print(f"diagnostics={paths['diagnostics']}")
    print(f"report={paths['report']}")
    print(f"manifest={paths['manifest']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())