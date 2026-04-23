#!/usr/bin/env python3
"""Run Track 2 DML with decomposed severity-component treatments."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from _causal_modeling_runtime_v1 import (
    DESIGN_BASE_COLUMNS,
    ROOT,
    SEVERITY_COMPONENT_TREATMENTS,
    TRACK2_OUTCOMES,
    build_primary_covariate_matrix,
    ensure_dir,
    load_model_matrix,
    run_plr_track,
    severity_component_specifications,
)


DEFAULT_OUTPUT_DIR = ROOT / "models" / "causal_estimates_v1" / "track2_severity_components_v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Track 2 severity-component DML estimation")
    parser.add_argument("--sample", choices=["main", "complete_case", "full"], default="main")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--folds", type=int, default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    frame = load_model_matrix(args.sample)
    encoded_x = build_primary_covariate_matrix(frame, include_auxiliary_flags=False)

    output_dir = Path(args.output_dir)
    ensure_dir(output_dir)
    design = pd.concat(
        [
            frame[DESIGN_BASE_COLUMNS + SEVERITY_COMPONENT_TREATMENTS + TRACK2_OUTCOMES],
            encoded_x,
        ],
        axis=1,
    )
    paths = run_plr_track(
        track="track2_severity_components",
        sample=args.sample,
        frame=frame,
        x_matrix=encoded_x,
        design=design,
        outcomes=TRACK2_OUTCOMES,
        specification_map=severity_component_specifications(),
        output_dir=output_dir,
        output_stem="track2_severity_components",
        report_title="Track 2 Severity Components Report v1",
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