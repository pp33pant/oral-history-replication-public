#!/usr/bin/env python3
"""Run Track 1 ILR DML with decomposed severity-component treatments."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from _causal_modeling_runtime_v1 import (
    DESIGN_BASE_COLUMNS,
    ROOT,
    SEVERITY_COMPONENT_TREATMENTS,
    TRACK1_CLASS_OUTCOMES,
    TRACK1_JOINT_OUTCOMES,
    build_primary_covariate_matrix,
    composition_to_ilr,
    ensure_dir,
    load_model_matrix,
    run_plr_track,
    severity_component_specifications,
)


DEFAULT_OUTPUT_DIR = ROOT / "models" / "causal_estimates_v1" / "track1_ilr_severity_components_v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Track 1 ILR severity-component DML estimation")
    parser.add_argument("--sample", choices=["main", "complete_case", "full"], default="main")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--folds", type=int, default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    frame = load_model_matrix(args.sample)
    six_part_ilr = composition_to_ilr(frame, TRACK1_JOINT_OUTCOMES, "ilr_joint6")
    what3_ilr = composition_to_ilr(frame, TRACK1_CLASS_OUTCOMES, "ilr_what3")
    estimation_frame = pd.concat([frame, six_part_ilr, what3_ilr], axis=1)
    encoded_x = build_primary_covariate_matrix(frame, include_auxiliary_flags=False)
    outcomes = list(six_part_ilr.columns) + list(what3_ilr.columns)

    output_dir = Path(args.output_dir)
    ensure_dir(output_dir)
    design = pd.concat(
        [
            frame[DESIGN_BASE_COLUMNS + SEVERITY_COMPONENT_TREATMENTS],
            six_part_ilr,
            what3_ilr,
            encoded_x,
        ],
        axis=1,
    )
    paths = run_plr_track(
        track="track1_ilr_severity_components",
        sample=args.sample,
        frame=estimation_frame,
        x_matrix=encoded_x,
        design=design,
        outcomes=outcomes,
        specification_map=severity_component_specifications(),
        output_dir=output_dir,
        output_stem="track1_ilr_severity_components",
        report_title="Track 1 ILR Severity Components Report v1",
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