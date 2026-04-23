#!/usr/bin/env python3
"""Run the narrator-level robustness battery and consolidate auditable outputs."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy.stats import t as student_t
from sklearn.linear_model import LogisticRegression

from _causal_modeling_runtime_v1 import (
    DESIGN_BASE_COLUMNS,
    PRIMARY_TREATMENTS,
    ROOT,
    SEVERITY_COMPONENT_TREATMENTS,
    TRACK1_CLASS_OUTCOMES,
    TRACK1_JOINT_OUTCOMES,
    TRACK1_MARGIN_OUTCOMES,
    TRACK1_REGION_OUTCOMES,
    TRACK2_OUTCOMES,
    build_primary_covariate_matrix,
    composition_to_ilr,
    default_track1_specifications,
    default_track2_specifications,
    ensure_dir,
    load_model_matrix,
    run_plr_track,
)


DEFAULT_OUTPUT_DIR = ROOT / "robustness" / "causal_robustness_v1"
BASELINE_DIR = ROOT / "models" / "causal_estimates_v1"
OUTCOME_DIR = ROOT / "data" / "processed" / "video_first_post_vm_batch1_v2"
INTERVIEW_SHARE_PATH = OUTCOME_DIR / "interview_outcome_share_vectors_v1.csv"
INTERVIEW_OUTCOME_PATH = OUTCOME_DIR / "interview_llm_fulltext_2d_outcomes_v2.csv"
EMBED_SHARE_PATH = OUTCOME_DIR / "narrator_1d_outcomes_v1.csv"
EMBED_ILR_PATH = OUTCOME_DIR / "narrator_ilr_outcomes_v1.csv"
BOUNDARY_SENSITIVITY_PATH = OUTCOME_DIR / "boundary_sensitivity_grid_v2.csv"
MEASUREMENT_SENSITIVITY_PATH = BASELINE_DIR / "measurement_sensitivity_v1.csv"
ARCHIVED_HOW_SCRIPTS = [
    {
        "step_id": "archiveability_audit",
        "label": "Archiveability audit",
        "script": ROOT / "scripts" / "archived_how_v1" / "audit_how_dimension_archiveability_v1.py",
        "args": [],
        "outputs": [
            ROOT / "data" / "processed" / "how_selection_audit_v1.csv",
            ROOT / "robustness" / "how_archiveability_treatment_assoc_v1.csv",
        ],
    },
    {
        "step_id": "observability_model",
        "label": "Observability model",
        "script": ROOT / "scripts" / "archived_how_v1" / "model_how_observability_v1.py",
        "args": ["--min-words", "150", "--min-candidate-segments", "0"],
        "outputs": [
            ROOT / "data" / "processed" / "how_observability_model_v1.csv",
            ROOT / "robustness" / "how_observability_model_report_v1.md",
        ],
    },
    {
        "step_id": "mnar_sensitivity",
        "label": "MNAR sensitivity",
        "script": ROOT / "scripts" / "archived_how_v1" / "run_mnar_sensitivity_how_v1.py",
        "args": [],
        "outputs": [
            ROOT / "data" / "processed" / "how_mnar_sensitivity_v1.csv",
            ROOT / "data" / "processed" / "how_lee_bounds_v1.csv",
            ROOT / "robustness" / "how_mnar_sensitivity_report_v1.md",
        ],
    },
    {
        "step_id": "negative_controls",
        "label": "Negative controls",
        "script": ROOT / "scripts" / "archived_how_v1" / "run_how_negative_controls_v1.py",
        "args": [],
        "outputs": [
            ROOT / "robustness" / "how_negative_controls_v1.csv",
            ROOT / "robustness" / "how_negative_controls_report_v1.md",
        ],
    },
    {
        "step_id": "difficult_cases_panel",
        "label": "Difficult-cases panel",
        "script": ROOT / "scripts" / "archived_how_v1" / "build_how_difficult_cases_panel_v1.py",
        "args": ["--n-per-stratum", "25"],
        "outputs": [
            ROOT / "data" / "processed" / "how_difficult_cases_panel_v1.csv",
            ROOT / "data" / "processed" / "how_difficult_cases_review_package_v1",
        ],
    },
]
ARCHIVE_DB_PATH = ROOT / "data" / "oral_history.db"
REGISTRY_PATH = DEFAULT_OUTPUT_DIR / "robustness_registry_v1.csv"
SUMMARY_PATH = DEFAULT_OUTPUT_DIR / "robustness_summary_v1.md"

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
    "appendix_how",
]

CATEGORY_TO_JOINT = {
    "Guarded Vigilance": "share_joint_Injury_composed",
    "Diffuse Unease": "share_joint_Injury_discomposed",
    "Wounded Belonging": "share_joint_Rupture_composed",
    "Stigmatized Discomposure": "share_joint_Rupture_discomposed",
    "Oppositional Citizenship": "share_joint_Distrust_composed",
    "Ambivalent Estrangement": "share_joint_Distrust_discomposed",
}

REFERENCE_KEYS = ["track", "outcome", "spec_id", "treatment", "weight_status"]
PAPER_FACING_TRACK1_OUTCOMES = TRACK1_JOINT_OUTCOMES
PAPER_FACING_TRACK2_OUTCOMES = TRACK2_OUTCOMES


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the causal robustness battery")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--checks", default="all", help="Comma-separated list, or 'all'.")
    parser.add_argument("--placebo-permutations", type=int, default=16)
    parser.add_argument("--logo-min-count", type=int, default=30)
    parser.add_argument("--logo-max-groups", type=int, default=8)
    return parser.parse_args()


def normalize_id(series: pd.Series) -> pd.Series:
    return series.astype(str).str.replace(r"\.0$", "", regex=True).str.strip()


def select_outcomes(frame: pd.DataFrame, candidates: list[str]) -> list[str]:
    return [column for column in candidates if column in frame.columns]


def build_outcome_support_audit(frame: pd.DataFrame, candidates: list[str]) -> pd.DataFrame:
    records: list[dict[str, Any]] = []
    for outcome in candidates:
        if outcome not in frame.columns:
            records.append(
                {
                    "outcome": outcome,
                    "present": 0,
                    "nonmissing_n": 0,
                    "unique_n": 0,
                    "status": "missing",
                }
            )
            continue
        series = frame[outcome]
        nonmissing_n = int(series.notna().sum())
        unique_n = int(series.dropna().nunique())
        if nonmissing_n == 0:
            status = "all_missing"
        elif unique_n <= 1:
            status = "constant"
        else:
            status = "supported"
        records.append(
            {
                "outcome": outcome,
                "present": 1,
                "nonmissing_n": nonmissing_n,
                "unique_n": unique_n,
                "status": status,
            }
        )
    return pd.DataFrame.from_records(records)


def supported_outcomes_from_audit(audit: pd.DataFrame) -> list[str]:
    return audit.loc[audit["status"] == "supported", "outcome"].tolist()


def build_design(frame: pd.DataFrame, x_matrix: pd.DataFrame, outcomes: list[str], extra_columns: list[str] | None = None) -> pd.DataFrame:
    design_columns = [column for column in DESIGN_BASE_COLUMNS if column in frame.columns]
    if extra_columns:
        for column in extra_columns:
            if column in frame.columns and column not in design_columns:
                design_columns.append(column)
    blocks = [frame[design_columns].reset_index(drop=True)]
    if outcomes:
        blocks.append(frame[outcomes].reset_index(drop=True))
    blocks.append(x_matrix.reset_index(drop=True))
    return pd.concat(blocks, axis=1)


def baseline_estimate_paths() -> dict[str, Path]:
    return {
        "track1_per_cell": BASELINE_DIR / "track1_per_cell_v1" / "track1_per_cell_estimates_v1.csv",
        "track1_ilr": BASELINE_DIR / "track1_ilr_v1" / "track1_ilr_estimates_v1.csv",
        "track2": BASELINE_DIR / "track2_v1" / "track2_estimates_v1.csv",
    }


@lru_cache(maxsize=1)
def load_baseline_estimates() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for track, path in baseline_estimate_paths().items():
        table = pd.read_csv(path)
        if "track" not in table.columns:
            table["track"] = track
        table["source_path"] = path.relative_to(ROOT).as_posix()
        frames.append(table)
    return pd.concat(frames, ignore_index=True)


def load_joint_reference() -> pd.DataFrame:
    return load_baseline_estimates().loc[lambda df: df["spec_id"] == "joint_continuous"].copy()


def load_expressive_reference() -> pd.DataFrame:
    return load_baseline_estimates().loc[lambda df: df["spec_id"] == "expressive_environment"].copy()


def partial_r2_numeric(t_statistic: float, dof: float) -> float:
    return float((t_statistic**2) / (t_statistic**2 + dof))


def partial_f2_numeric(t_statistic: float, dof: float) -> float:
    return float((t_statistic**2) / dof)


def extreme_robustness_value_numeric(
    t_statistic: float,
    dof: float,
    q: float = 1.0,
    alpha: float = 0.05,
    invert: bool = False,
) -> float:
    fq = q * abs(t_statistic / np.sqrt(dof))
    fq2 = fq**2
    t_crit = abs(student_t.ppf(alpha / 2, df=max(dof - 1, 1)))
    f_crit2 = (t_crit / np.sqrt(max(dof - 1, 1))) ** 2
    if invert:
        f1, f2 = f_crit2, fq2
    else:
        f1, f2 = fq2, f_crit2
    if f1 <= f2:
        return 0.0
    return float((f1 - f2) / (1 + f1))


def robustness_value_numeric(
    t_statistic: float,
    dof: float,
    q: float = 1.0,
    alpha: float = 0.05,
    invert: bool = False,
) -> float:
    fq = q * abs(t_statistic / np.sqrt(dof))
    f_crit = abs(student_t.ppf(alpha / 2, df=max(dof - 1, 1))) / np.sqrt(max(dof - 1, 1))
    if invert:
        f1, f2 = f_crit, fq
    else:
        f1, f2 = fq, f_crit
    fqa = f1 - f2
    if fqa <= 0:
        return 0.0
    binding_rv = float(2 / (1 + np.sqrt(1 + 4 / (fqa**2))))
    if f2 > 0 and f1 > (1 / f2):
        return extreme_robustness_value_numeric(t_statistic, dof=dof, q=q, alpha=alpha, invert=invert)
    return binding_rv


def build_sensitivity_stats_table(reference: pd.DataFrame) -> pd.DataFrame:
    working = reference.copy()
    working["dof_assumed"] = pd.to_numeric(working["sample_n"], errors="coerce") - 2.0
    working["t_statistic"] = np.where(
        working["std_error"].fillna(0).ne(0),
        working["estimate"] / working["std_error"],
        np.nan,
    )

    valid = working["t_statistic"].notna() & working["dof_assumed"].notna() & working["dof_assumed"].gt(1)
    working["partial_r2"] = np.nan
    working["partial_f2"] = np.nan
    working["rv_q"] = np.nan
    working["rv_qa"] = np.nan
    working["rv_q_pct"] = np.nan
    working["rv_qa_pct"] = np.nan

    for index, row in working.loc[valid].iterrows():
        t_statistic = float(row["t_statistic"])
        dof = float(row["dof_assumed"])
        partial_r2 = partial_r2_numeric(t_statistic, dof)
        partial_f2 = partial_f2_numeric(t_statistic, dof)
        rv_q = robustness_value_numeric(t_statistic, dof=dof, q=1.0, alpha=1.0)
        rv_qa = robustness_value_numeric(t_statistic, dof=dof, q=1.0, alpha=0.05)
        working.at[index, "partial_r2"] = partial_r2
        working.at[index, "partial_f2"] = partial_f2
        working.at[index, "rv_q"] = rv_q
        working.at[index, "rv_qa"] = rv_qa
        working.at[index, "rv_q_pct"] = rv_q * 100.0
        working.at[index, "rv_qa_pct"] = rv_qa * 100.0

    working["sensitivity_method"] = "cinelli_hazlett_numeric_minimal_reporting_v1"
    working["sensitivity_notes"] = (
        "Computed from estimate, standard error, and assumed final-stage dof = sample_n - 2 using the sensemakr numeric formulas."
    )
    return working


@lru_cache(maxsize=1)
def load_interview_sources() -> tuple[pd.DataFrame, pd.DataFrame]:
    share_frame = pd.read_csv(INTERVIEW_SHARE_PATH)
    outcome_frame = pd.read_csv(INTERVIEW_OUTCOME_PATH)
    share_frame["narrator_id"] = normalize_id(share_frame["narrator_id"])
    outcome_frame["narrator_id"] = normalize_id(outcome_frame["narrator_id"])
    return share_frame, outcome_frame


def joint_track1_spec() -> dict[str, dict[str, Any]]:
    return {"joint_continuous": default_track1_specifications()["joint_continuous"]}


def joint_track2_spec() -> dict[str, dict[str, Any]]:
    return {"joint_continuous": default_track2_specifications()["joint_continuous"]}


def annotate_vs_reference(
    estimates: pd.DataFrame,
    reference: pd.DataFrame,
    on_keys: list[str] | None = None,
    outcome_mapping: dict[str, str] | None = None,
) -> pd.DataFrame:
    if estimates.empty:
        return estimates
    merge_keys = on_keys or REFERENCE_KEYS
    working = estimates.copy()
    reference_subset = reference.copy()
    if outcome_mapping:
        working["reference_outcome"] = working["outcome"].map(outcome_mapping).fillna(working["outcome"])
        reference_subset = reference_subset.rename(columns={"outcome": "reference_outcome"})
        merge_keys = ["reference_outcome" if key == "outcome" else key for key in merge_keys]
    reference_subset = reference_subset[merge_keys + ["estimate", "std_error", "p_value"]].rename(
        columns={
            "estimate": "estimate_reference",
            "std_error": "std_error_reference",
            "p_value": "p_value_reference",
        }
    )
    merged = working.merge(reference_subset, on=merge_keys, how="left")
    merged["estimate_delta_vs_reference"] = merged["estimate"] - merged["estimate_reference"]
    merged["std_error_ratio_vs_reference"] = merged["std_error"] / merged["std_error_reference"]
    merged["same_sign_as_reference"] = np.where(
        merged["estimate_reference"].notna(),
        np.sign(merged["estimate"]) == np.sign(merged["estimate_reference"]),
        np.nan,
    )
    if "reference_outcome" in merged.columns:
        merged = merged.drop(columns=["reference_outcome"])
    return merged


def save_table(table: pd.DataFrame, path: Path) -> Path:
    ensure_dir(path.parent)
    table.to_csv(path, index=False)
    return path


def load_existing_track_pair(root: Path) -> pd.DataFrame | None:
    table_paths = [
        root / "track1_per_cell" / "track1_per_cell_estimates_v1.csv",
        root / "track2" / "track2_estimates_v1.csv",
    ]
    if not all(path.exists() for path in table_paths):
        return None
    return pd.concat([pd.read_csv(path) for path in table_paths], ignore_index=True)


def load_existing_r14_permutation(output_root: Path, permutation_id: int) -> pd.DataFrame | None:
    return load_existing_track_pair(output_root / f"perm_{permutation_id:02d}")


def run_configs(
    configs: list[dict[str, Any]],
    *,
    sample: str,
    output_root: Path,
    report_prefix: str,
    nuisance_learner: str | None = None,
    folds: int | None = None,
    group_ids: pd.Series | np.ndarray | None = None,
    cluster_ids: pd.Series | np.ndarray | None = None,
    weight_options: list[tuple[str, str | None]] | None = None,
) -> pd.DataFrame:
    results: list[pd.DataFrame] = []
    for config in configs:
        track_output = output_root / config["stem"]
        ensure_dir(track_output)
        paths = run_plr_track(
            track=config["track"],
            sample=sample,
            frame=config["frame"],
            x_matrix=config["x_matrix"],
            design=config["design"],
            outcomes=config["outcomes"],
            specification_map=config["specification_map"],
            output_dir=track_output,
            output_stem=config["stem"],
            report_title=f"{report_prefix}: {config['track']}",
            script_name=Path(__file__).name,
            folds=folds,
            nuisance_learner=nuisance_learner,
            group_ids=group_ids,
            cluster_ids=cluster_ids,
            weight_options=weight_options,
        )
        estimates = pd.read_csv(paths["estimates"])
        estimates["source_path"] = paths["estimates"].relative_to(ROOT).as_posix()
        results.append(estimates)
    if not results:
        return pd.DataFrame()
    return pd.concat(results, ignore_index=True)


def build_default_joint_configs(
    frame: pd.DataFrame,
    *,
    track1_outcomes: list[str] | None = None,
    track2_outcomes: list[str] | None = None,
    include_ilr: bool = True,
) -> list[dict[str, Any]]:
    frame = frame.reset_index(drop=True).copy()
    x_matrix = build_primary_covariate_matrix(frame, include_auxiliary_flags=False)
    configs: list[dict[str, Any]] = []

    per_cell_outcomes = track1_outcomes or select_outcomes(
        frame,
        TRACK1_JOINT_OUTCOMES + TRACK1_CLASS_OUTCOMES + TRACK1_REGION_OUTCOMES + TRACK1_MARGIN_OUTCOMES,
    )
    if per_cell_outcomes:
        configs.append(
            {
                "track": "track1_per_cell",
                "stem": "track1_per_cell",
                "frame": frame,
                "x_matrix": x_matrix,
                "outcomes": per_cell_outcomes,
                "specification_map": joint_track1_spec(),
                "design": build_design(frame, x_matrix, per_cell_outcomes),
            }
        )

    if include_ilr:
        joint_inputs = select_outcomes(frame, TRACK1_JOINT_OUTCOMES)
        class_inputs = select_outcomes(frame, TRACK1_CLASS_OUTCOMES)
        if len(joint_inputs) == len(TRACK1_JOINT_OUTCOMES) and len(class_inputs) == len(TRACK1_CLASS_OUTCOMES):
            six_part_ilr = composition_to_ilr(frame, TRACK1_JOINT_OUTCOMES, "ilr_joint6")
            class_ilr = composition_to_ilr(frame, TRACK1_CLASS_OUTCOMES, "ilr_what3")
            ilr_frame = pd.concat([frame, six_part_ilr, class_ilr], axis=1)
            ilr_outcomes = list(six_part_ilr.columns) + list(class_ilr.columns)
            configs.append(
                {
                    "track": "track1_ilr",
                    "stem": "track1_ilr",
                    "frame": ilr_frame,
                    "x_matrix": x_matrix,
                    "outcomes": ilr_outcomes,
                    "specification_map": joint_track1_spec(),
                    "design": build_design(ilr_frame, x_matrix, ilr_outcomes),
                }
            )

    continuous_outcomes = track2_outcomes or select_outcomes(frame, TRACK2_OUTCOMES)
    if continuous_outcomes:
        configs.append(
            {
                "track": "track2",
                "stem": "track2",
                "frame": frame,
                "x_matrix": x_matrix,
                "outcomes": continuous_outcomes,
                "specification_map": joint_track2_spec(),
                "design": build_design(frame, x_matrix, continuous_outcomes),
            }
        )

    return configs


def build_paper_facing_joint_configs(frame: pd.DataFrame) -> list[dict[str, Any]]:
    return build_default_joint_configs(
        frame,
        track1_outcomes=select_outcomes(frame, PAPER_FACING_TRACK1_OUTCOMES),
        track2_outcomes=select_outcomes(frame, PAPER_FACING_TRACK2_OUTCOMES),
        include_ilr=False,
    )


def record(registry: list[dict[str, Any]], check_id: str, label: str, status: str, table_path: Path | None, notes: str, rows: int | None = None) -> None:
    registry.append(
        {
            "check_id": check_id,
            "label": label,
            "status": status,
            "rows": rows,
            "table_path": table_path.relative_to(ROOT).as_posix() if table_path is not None else "",
            "notes": notes,
        }
    )


def parse_check_selection(raw_value: str) -> list[str]:
    if raw_value.strip().lower() == "all":
        return DEFAULT_CHECKS
    requested = [token.strip().lower() for token in raw_value.split(",") if token.strip()]
    return requested


def run_r1(main_frame: pd.DataFrame, output_root: Path) -> Path:
    reference = load_joint_reference().loc[
        lambda df: ((df["track"] == "track1_per_cell") & (df["outcome"].isin(PAPER_FACING_TRACK1_OUTCOMES)))
        | ((df["track"] == "track2") & (df["outcome"].isin(PAPER_FACING_TRACK2_OUTCOMES)))
    ].copy()
    tables = [annotate_vs_reference(reference, reference)]
    tables[0]["check_variant"] = "baseline_default"
    for learner in ["random_forest_regressor", "lasso_cv_regressor"]:
        learner_output = output_root / learner
        estimates = run_configs(
            build_paper_facing_joint_configs(main_frame),
            sample="main",
            output_root=learner_output,
            report_prefix=f"R1 learner sensitivity ({learner})",
            nuisance_learner=learner,
        )
        estimates = annotate_vs_reference(estimates, reference)
        estimates["check_variant"] = learner
        tables.append(estimates)
    table = pd.concat(tables, ignore_index=True)
    return save_table(table, output_root / "r1_learner_sensitivity_v1.csv")


def run_r2(main_frame: pd.DataFrame, output_root: Path) -> Path:
    reference_source = load_joint_reference().loc[
        lambda df: ((df["track"] == "track1_per_cell") & (df["outcome"].isin(PAPER_FACING_TRACK1_OUTCOMES)))
        | ((df["track"] == "track2") & (df["outcome"].isin(PAPER_FACING_TRACK2_OUTCOMES)))
    ].copy()
    reference = annotate_vs_reference(reference_source.copy(), reference_source.copy())
    reference["check_variant"] = "folds_5_baseline"
    tables = [reference]
    for fold_count in [3, 10]:
        print(f"[R2] starting folds={fold_count}", flush=True)
        fold_output = output_root / f"folds_{fold_count}"
        estimates = run_configs(
            build_paper_facing_joint_configs(main_frame),
            sample="main",
            output_root=fold_output,
            report_prefix=f"R2 fold sensitivity ({fold_count})",
            folds=fold_count,
        )
        estimates = annotate_vs_reference(estimates, reference_source)
        estimates["check_variant"] = f"folds_{fold_count}"
        tables.append(estimates)
        print(f"[R2] completed folds={fold_count}", flush=True)
    table = pd.concat(tables, ignore_index=True)
    return save_table(table, output_root / "r2_crossfit_folds_v1.csv")


def build_discretized_frame(frame: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    working = frame.copy()
    age_series = working["age_at_first_exposure"].astype(float)
    working["timing_childhood_flag_v1"] = (age_series < 13).astype(int)
    working["timing_adolescence_flag_v1"] = ((age_series >= 13) & (age_series < 18)).astype(int)
    dosage_bins = pd.qcut(
        working["total_days_incarcerated"].rank(method="first"),
        q=4,
        labels=False,
        duplicates="drop",
    )
    dosage_columns: list[str] = []
    if dosage_bins.nunique() > 1:
        for bin_value in sorted(int(value) for value in pd.Series(dosage_bins).dropna().unique()):
            if bin_value == 0:
                continue
            column = f"dosage_q{bin_value + 1}_flag_v1"
            working[column] = (dosage_bins == bin_value).astype(int)
            dosage_columns.append(column)
    grouped_treatments = ["timing_childhood_flag_v1", "timing_adolescence_flag_v1", *dosage_columns, *SEVERITY_COMPONENT_TREATMENTS]
    return working, grouped_treatments


def run_r3(main_frame: pd.DataFrame, output_root: Path) -> Path:
    working, grouped_treatments = build_discretized_frame(main_frame)
    spec = {
        "grouped_treatments": {
            "label": "Grouped treatment robustness",
            "hypothesis_family": "R3",
            "treatment_columns": grouped_treatments,
            "engine_target": "dml_plr",
            "x_block_id": "primary",
            "x_exclude_columns": [],
            "notes": "Timing bands, dosage quartiles, and severity component flags replace the continuous primary treatment bundle.",
        }
    }
    configs = build_paper_facing_joint_configs(working)
    for config in configs:
        config["specification_map"] = spec
    estimates = run_configs(
        configs,
        sample="main",
        output_root=output_root,
        report_prefix="R3 treatment discretization",
    )
    estimates["grouped_treatments"] = ";".join(grouped_treatments)
    return save_table(estimates, output_root / "r3_treatment_discretization_v1.csv")


def build_trimmed_frame(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    working = frame.reset_index(drop=True).copy()
    x_matrix = build_primary_covariate_matrix(working, include_auxiliary_flags=False)
    treatment = working["adolescent_exposure_flag"].astype(int)
    model = LogisticRegression(max_iter=5000)
    model.fit(x_matrix, treatment)
    propensity = model.predict_proba(x_matrix)[:, 1]
    working["timing_propensity_v1"] = propensity
    kept = working.loc[(propensity >= 0.05) & (propensity <= 0.95)].reset_index(drop=True)
    audit = pd.DataFrame(
        {
            "rows_before": [len(working)],
            "rows_after": [len(kept)],
            "trim_share": [1.0 - (len(kept) / len(working))],
            "propensity_min": [float(np.min(propensity))],
            "propensity_max": [float(np.max(propensity))],
        }
    )
    return kept, audit


def run_r4(main_frame: pd.DataFrame, output_root: Path) -> Path:
    trimmed, audit = build_trimmed_frame(main_frame)
    save_table(audit, output_root / "r4_overlap_trimming_audit_v1.csv")
    estimates = run_configs(
        build_paper_facing_joint_configs(trimmed),
        sample="main",
        output_root=output_root,
        report_prefix="R4 overlap trimming",
    )
    estimates = annotate_vs_reference(estimates, load_joint_reference())
    estimates["rows_before_trim"] = int(audit.loc[0, "rows_before"])
    estimates["rows_after_trim"] = int(audit.loc[0, "rows_after"])
    return save_table(estimates, output_root / "r4_overlap_trimming_v1.csv")


def run_r5(output_root: Path) -> Path:
    reference = load_joint_reference().loc[
        lambda df: ((df["track"] == "track1_per_cell") & (df["outcome"].isin(PAPER_FACING_TRACK1_OUTCOMES)))
        | ((df["track"] == "track2") & (df["outcome"].isin(PAPER_FACING_TRACK2_OUTCOMES)))
    ].copy()
    return save_table(reference, output_root / "r5_weight_specification_v1.csv")


def run_r6(output_root: Path) -> Path:
    table = pd.read_csv(BOUNDARY_SENSITIVITY_PATH)
    table["source_path"] = BOUNDARY_SENSITIVITY_PATH.relative_to(ROOT).as_posix()
    return save_table(table, output_root / "r6_boundary_sensitivity_v1.csv")


def build_interview_equal_frame(main_frame: pd.DataFrame) -> pd.DataFrame:
    share_frame, outcome_frame = load_interview_sources()
    share_records = share_frame[["narrator_id", "interview_id", "n_scored_segments", "interview_level_share_vector_3x2"]].copy()
    share_payload = share_records["interview_level_share_vector_3x2"].map(json.loads)
    for label, column in CATEGORY_TO_JOINT.items():
        share_records[column] = share_payload.map(lambda payload, key=label: float(payload.get(key, 0.0)))

    joint_columns = list(CATEGORY_TO_JOINT.values())
    aggregated_shares = share_records.groupby("narrator_id")[joint_columns].mean()
    aggregated_shares["share_class_Injury"] = aggregated_shares["share_joint_Injury_composed"] + aggregated_shares["share_joint_Injury_discomposed"]
    aggregated_shares["share_class_Rupture"] = aggregated_shares["share_joint_Rupture_composed"] + aggregated_shares["share_joint_Rupture_discomposed"]
    aggregated_shares["share_class_Distrust"] = aggregated_shares["share_joint_Distrust_composed"] + aggregated_shares["share_joint_Distrust_discomposed"]
    aggregated_shares["share_composed"] = aggregated_shares[["share_joint_Injury_composed", "share_joint_Rupture_composed", "share_joint_Distrust_composed"]].sum(axis=1)
    aggregated_shares["share_discomposed"] = aggregated_shares[["share_joint_Injury_discomposed", "share_joint_Rupture_discomposed", "share_joint_Distrust_discomposed"]].sum(axis=1)

    continuous = outcome_frame.groupby("narrator_id").agg(
        authority_stance=("authority_stance_mean", "mean"),
        belonging_stance=("belonging_stance_mean", "mean"),
        composure_score_mean=("composure_score_mean", "mean"),
        composure_score_max=("composure_score_max", "max"),
        how_multimodal_score_mean=("how_multimodal_score_mean", "mean"),
        how_multimodal_score_max=("how_multimodal_score_max", "max"),
        share_discomposed_text=("share_discomposed_text", "mean"),
        share_composed_text=("share_composed_text", "mean"),
        n_interviews_alt_v1=("interview_id", "nunique"),
    )

    region_dummies = pd.get_dummies(outcome_frame["region_6"], prefix="share_region").astype(float)
    region_table = pd.concat([outcome_frame[["narrator_id"]], region_dummies], axis=1).groupby("narrator_id").mean()
    for column in TRACK1_REGION_OUTCOMES:
        if column not in region_table.columns:
            region_table[column] = 0.0
    region_table = region_table[TRACK1_REGION_OUTCOMES]

    working = main_frame.copy()
    working["narrator_id"] = normalize_id(working["narrator_id"])
    outcome_updates = aggregated_shares.join(continuous, how="inner").join(region_table, how="left")
    update_columns = list(outcome_updates.columns)
    keyed = outcome_updates.reset_index()
    outcome_lookup = keyed.set_index("narrator_id")
    for column in update_columns:
        working[column] = working["narrator_id"].map(outcome_lookup[column])
    return working.loc[working[update_columns].notna().all(axis=1)].reset_index(drop=True)


def run_r7(main_frame: pd.DataFrame, output_root: Path) -> Path:
    alternative_frame = build_interview_equal_frame(main_frame)
    track1_audit = build_outcome_support_audit(alternative_frame, PAPER_FACING_TRACK1_OUTCOMES)
    track1_audit["track"] = "track1_per_cell"
    track2_audit = build_outcome_support_audit(alternative_frame, PAPER_FACING_TRACK2_OUTCOMES)
    track2_audit["track"] = "track2"
    support_audit = pd.concat([track1_audit, track2_audit], ignore_index=True)
    save_table(support_audit, output_root / "r7_outcome_support_audit_v1.csv")

    track1_outcomes = supported_outcomes_from_audit(track1_audit)
    track2_outcomes = supported_outcomes_from_audit(track2_audit)
    estimates = run_configs(
        build_default_joint_configs(
            alternative_frame,
            track1_outcomes=track1_outcomes,
            track2_outcomes=track2_outcomes,
            include_ilr=False,
        ),
        sample="main",
        output_root=output_root,
        report_prefix="R7 alternative aggregation",
    )
    estimates = annotate_vs_reference(estimates, load_joint_reference())
    estimates["aggregation_variant"] = "interview_equal_mean"
    estimates["analysis_rows"] = len(alternative_frame)
    estimates["analysis_narrators"] = alternative_frame["narrator_id"].nunique()
    return save_table(estimates, output_root / "r7_alternative_aggregation_v1.csv")


def run_r8(main_frame: pd.DataFrame, output_root: Path) -> Path:
    configs = build_default_joint_configs(
        main_frame,
        track1_outcomes=select_outcomes(main_frame, ["share_class_Distrust", "share_joint_Distrust_discomposed", "share_discomposed", "share_discomposed_text"]),
        track2_outcomes=select_outcomes(main_frame, ["how_multimodal_score_mean", "how_multimodal_score_max", "composure_score_max"]),
        include_ilr=False,
    )
    estimates = run_configs(
        configs,
        sample="main",
        output_root=output_root,
        report_prefix="R8 minority-signal outcomes",
    )
    estimates = annotate_vs_reference(estimates, load_joint_reference())
    return save_table(estimates, output_root / "r8_minority_signal_v1.csv")


def run_r9(output_root: Path) -> Path:
    reference = load_joint_reference().copy()
    table = reference.loc[
        (reference["track"] == "track1_ilr")
        & (reference["outcome"].str.startswith("ilr_joint6_") | reference["outcome"].str.startswith("ilr_what3_"))
    ].copy()
    return save_table(table, output_root / "r9_ilr_dimensionality_v1.csv")


def run_r10(output_root: Path) -> Path:
    reference = load_joint_reference().loc[
        lambda df: ((df["track"] == "track1_per_cell") & (df["outcome"].isin(PAPER_FACING_TRACK1_OUTCOMES)))
        | ((df["track"] == "track2") & (df["outcome"].isin(PAPER_FACING_TRACK2_OUTCOMES)))
    ].copy()
    table = build_sensitivity_stats_table(reference)
    return save_table(table, output_root / "r10_unobserved_confounding_sensitivity_v1.csv")


def run_r11(main_frame: pd.DataFrame, output_root: Path) -> Path:
    spec = {
        "exogenous_severity": {
            "label": "Exogenous severity only",
            "hypothesis_family": "R11",
            "treatment_columns": ["age_at_first_exposure", "total_days_incarcerated", "family_separation_flag", "parental_arrest_flag"],
            "engine_target": "dml_plr",
            "x_block_id": "primary",
            "x_exclude_columns": [],
            "notes": "Retain timing and dosage while restricting severity to the more exogenous genealogical components.",
        }
    }
    configs = build_paper_facing_joint_configs(main_frame)
    for config in configs:
        config["specification_map"] = spec
    estimates = run_configs(
        configs,
        sample="main",
        output_root=output_root,
        report_prefix="R11 exogenous severity only",
    )
    return save_table(estimates, output_root / "r11_exogenous_severity_only_v1.csv")


def build_interview_long_frame(main_frame: pd.DataFrame) -> tuple[pd.DataFrame, list[tuple[str, str | None]]]:
    share_frame, outcome_frame = load_interview_sources()
    working_share = share_frame[["narrator_id", "interview_id", "n_scored_segments", "interview_level_share_vector_3x2"]].copy()
    share_payload = working_share["interview_level_share_vector_3x2"].map(json.loads)
    for label, column in CATEGORY_TO_JOINT.items():
        working_share[column] = share_payload.map(lambda payload, key=label: float(payload.get(key, 0.0)))

    working = working_share.merge(
        outcome_frame[
            [
                "narrator_id",
                "interview_id",
                "n_segments",
                "authority_stance_mean",
                "belonging_stance_mean",
                "composure_score_mean",
                "composure_score_max",
                "how_multimodal_score_mean",
                "how_multimodal_score_max",
                "share_discomposed_text",
                "share_composed_text",
                "share_discomposed",
                "share_composed",
                "region_6",
                "outcome_3class",
            ]
        ],
        on=["narrator_id", "interview_id"],
        how="inner",
    )
    working = working.rename(
        columns={
            "authority_stance_mean": "authority_stance",
            "belonging_stance_mean": "belonging_stance",
        }
    )
    region_dummies = pd.get_dummies(working["region_6"], prefix="share_region").astype(float)
    working = pd.concat([working, region_dummies], axis=1)
    for column in TRACK1_REGION_OUTCOMES:
        if column not in working.columns:
            working[column] = 0.0
    working["share_class_Injury"] = working["share_joint_Injury_composed"] + working["share_joint_Injury_discomposed"]
    working["share_class_Rupture"] = working["share_joint_Rupture_composed"] + working["share_joint_Rupture_discomposed"]
    working["share_class_Distrust"] = working["share_joint_Distrust_composed"] + working["share_joint_Distrust_discomposed"]

    covariate_columns = ["narrator_id", *[column for column in main_frame.columns if column != "narrator_id" and column not in working.columns]]
    base = main_frame.copy()
    base["narrator_id"] = normalize_id(base["narrator_id"])
    base = base.drop_duplicates(subset=["narrator_id"])
    working = working.merge(base[covariate_columns], on="narrator_id", how="inner")
    total_segments = working.groupby("narrator_id")["n_segments"].transform("sum")
    segment_share = working["n_segments"] / total_segments
    working["ipw_weight_interview_v1"] = working["ipw_weight_v1"] * segment_share
    working["rake_weight_interview_v1"] = working["rake_weight_v1"] * segment_share
    weight_options = [("unweighted", None), ("ipw", "ipw_weight_interview_v1"), ("rake", "rake_weight_interview_v1")]
    return working.reset_index(drop=True), weight_options


def run_r12(main_frame: pd.DataFrame, output_root: Path) -> Path:
    long_frame, weight_options = build_interview_long_frame(main_frame)
    track1_audit = build_outcome_support_audit(long_frame, PAPER_FACING_TRACK1_OUTCOMES)
    track1_audit["track"] = "track1_per_cell"
    track2_audit = build_outcome_support_audit(long_frame, PAPER_FACING_TRACK2_OUTCOMES)
    track2_audit["track"] = "track2"
    support_audit = pd.concat([track1_audit, track2_audit], ignore_index=True)
    save_table(support_audit, output_root / "r12_outcome_support_audit_v1.csv")

    track1_outcomes = supported_outcomes_from_audit(track1_audit)
    track2_outcomes = supported_outcomes_from_audit(track2_audit)
    group_ids = long_frame["narrator_id"]
    estimates = run_configs(
        build_default_joint_configs(
            long_frame,
            track1_outcomes=track1_outcomes,
            track2_outcomes=track2_outcomes,
            include_ilr=False,
        ),
        sample="main",
        output_root=output_root,
        report_prefix="R12 interview-level long format",
        group_ids=group_ids,
        cluster_ids=group_ids,
        weight_options=weight_options,
    )
    estimates = annotate_vs_reference(estimates, load_joint_reference())
    estimates["estimation_unit"] = "interview"
    estimates["analysis_rows"] = len(long_frame)
    estimates["analysis_narrators"] = long_frame["narrator_id"].nunique()
    return save_table(estimates, output_root / "r12_interview_long_format_v1.csv")


def run_r13(main_frame: pd.DataFrame, output_root: Path) -> Path:
    spec = {
        "timing_total": {
            "label": "Timing total effect",
            "hypothesis_family": "R13",
            "treatment_columns": ["age_at_first_exposure"],
            "engine_target": "dml_plr",
            "x_block_id": "primary",
            "x_exclude_columns": [],
            "notes": "Sequential DML Layer 1 total timing effect without conditioning on dosage or severity.",
        }
    }
    configs = build_paper_facing_joint_configs(main_frame)
    for config in configs:
        config["specification_map"] = spec
    estimates = run_configs(
        configs,
        sample="main",
        output_root=output_root,
        report_prefix="R13 sequential DML",
    )
    estimates = annotate_vs_reference(
        estimates,
        load_joint_reference().loc[lambda df: df["treatment"] == "age_at_first_exposure"].copy(),
        on_keys=["track", "outcome", "treatment", "weight_status"],
    )
    return save_table(estimates, output_root / "r13_sequential_dml_v1.csv")


def run_r14(main_frame: pd.DataFrame, output_root: Path, permutations: int) -> Path:
    rng = np.random.default_rng(1729)
    headline_track1 = select_outcomes(main_frame, ["share_class_Distrust", "share_joint_Rupture_discomposed"])
    headline_track2 = select_outcomes(main_frame, ["authority_stance", "belonging_stance", "how_multimodal_score_mean"])
    placebo_rows: list[pd.DataFrame] = []
    for permutation_id in range(1, permutations + 1):
        existing = load_existing_r14_permutation(output_root, permutation_id)
        if existing is not None:
            existing = existing.copy()
            existing["permutation_id"] = permutation_id
            placebo_rows.append(existing)
            print(f"[r14] permutation {permutation_id}/{permutations} reuse existing outputs", flush=True)
            continue
        print(f"[r14] permutation {permutation_id}/{permutations} start", flush=True)
        permuted = main_frame.copy()
        shuffled_index = rng.permutation(len(permuted))
        for column in PRIMARY_TREATMENTS:
            permuted[column] = permuted.iloc[shuffled_index][column].to_numpy()
        estimates = run_configs(
            build_default_joint_configs(
                permuted,
                track1_outcomes=headline_track1,
                track2_outcomes=headline_track2,
                include_ilr=False,
            ),
            sample="main",
            output_root=output_root / f"perm_{permutation_id:02d}",
            report_prefix=f"R14 placebo permutation {permutation_id}",
        )
        estimates["permutation_id"] = permutation_id
        placebo_rows.append(estimates)
        print(f"[r14] permutation {permutation_id}/{permutations} complete", flush=True)
    placebo = pd.concat(placebo_rows, ignore_index=True)
    reference = load_joint_reference().copy()
    summary = (
        placebo.groupby(["track", "outcome", "spec_id", "treatment", "weight_status"], as_index=False)
        .agg(
            null_mean_estimate=("estimate", "mean"),
            null_sd_estimate=("estimate", "std"),
            null_q025=("estimate", lambda values: float(np.quantile(values, 0.025))),
            null_q975=("estimate", lambda values: float(np.quantile(values, 0.975))),
        )
    )
    summary = summary.merge(
        reference[["track", "outcome", "spec_id", "treatment", "weight_status", "estimate"]].rename(columns={"estimate": "estimate_reference"}),
        on=["track", "outcome", "spec_id", "treatment", "weight_status"],
        how="left",
    )
    empirical_p = (
        placebo.merge(
            reference[["track", "outcome", "spec_id", "treatment", "weight_status", "estimate"]].rename(columns={"estimate": "estimate_reference"}),
            on=["track", "outcome", "spec_id", "treatment", "weight_status"],
            how="left",
        )
        .assign(extreme=lambda df: np.abs(df["estimate"]) >= np.abs(df["estimate_reference"]))
        .groupby(["track", "outcome", "spec_id", "treatment", "weight_status"], as_index=False)["extreme"]
        .mean()
        .rename(columns={"extreme": "empirical_p_value"})
    )
    summary = summary.merge(empirical_p, on=["track", "outcome", "spec_id", "treatment", "weight_status"], how="left")
    save_table(placebo, output_root / "r14_placebo_permutation_draws_v1.csv")
    return save_table(summary, output_root / "r14_placebo_permutation_summary_v1.csv")


def run_r15(main_frame: pd.DataFrame, output_root: Path, min_count: int, max_groups: int) -> Path:
    facility_counts = main_frame["weight_primary_facility_v1"].fillna("unknown").value_counts()
    groups = [group for group, count in facility_counts.items() if group != "unknown" and int(count) >= min_count][:max_groups]
    tables: list[pd.DataFrame] = []
    reference = load_joint_reference()
    for facility in groups:
        facility_root = output_root / facility
        existing = load_existing_track_pair(facility_root)
        if existing is not None:
            print(f"[r15] exclude {facility} reuse existing outputs", flush=True)
            estimates = annotate_vs_reference(existing, reference)
            estimates["excluded_facility"] = facility
            estimates["remaining_rows"] = int(estimates["sample_n"].dropna().iloc[0]) if "sample_n" in estimates.columns and not estimates["sample_n"].dropna().empty else np.nan
            tables.append(estimates)
            continue
        print(f"[r15] exclude {facility} start", flush=True)
        subset = main_frame.loc[main_frame["weight_primary_facility_v1"].fillna("unknown") != facility].reset_index(drop=True)
        estimates = run_configs(
            build_paper_facing_joint_configs(subset),
            sample="main",
            output_root=facility_root,
            report_prefix=f"R15 leave-one-camp-out ({facility})",
        )
        estimates = annotate_vs_reference(estimates, reference)
        estimates["excluded_facility"] = facility
        estimates["remaining_rows"] = len(subset)
        tables.append(estimates)
        print(f"[r15] exclude {facility} complete", flush=True)
    combined = pd.concat(tables, ignore_index=True) if tables else pd.DataFrame()
    return save_table(combined, output_root / "r15_leave_one_camp_out_v1.csv")


def run_r16(output_root: Path) -> Path:
    complete_case = load_model_matrix("complete_case")
    estimates = run_configs(
        build_paper_facing_joint_configs(complete_case),
        sample="complete_case",
        output_root=output_root,
        report_prefix="R16 recovered unknown handling",
    )
    estimates = annotate_vs_reference(estimates, load_joint_reference())
    estimates["sample_variant"] = "complete_case"
    return save_table(estimates, output_root / "r16_complete_case_v1.csv")


def run_r17(main_frame: pd.DataFrame, output_root: Path) -> Path:
    embed_share = pd.read_csv(EMBED_SHARE_PATH)
    embed_ilr = pd.read_csv(EMBED_ILR_PATH)
    embed_share["narrator_id"] = normalize_id(embed_share["narrator_id"])
    embed_ilr["narrator_id"] = normalize_id(embed_ilr["narrator_id"])

    base = main_frame.copy()
    base["narrator_id"] = normalize_id(base["narrator_id"])
    share_lookup = embed_share.set_index("narrator_id")
    ilr_lookup = embed_ilr.set_index("narrator_id")
    base["embed_share_Injury"] = base["narrator_id"].map(share_lookup["prob_share_inj"])
    base["embed_share_Rupture"] = base["narrator_id"].map(share_lookup["prob_share_rup"])
    base["embed_share_Distrust"] = base["narrator_id"].map(share_lookup["prob_share_dis"])
    base["embed_ilr_what_1"] = base["narrator_id"].map(ilr_lookup["ilr_what_1"])
    base["embed_ilr_what_2"] = base["narrator_id"].map(ilr_lookup["ilr_what_2"])
    base = base.loc[base[["embed_share_Injury", "embed_share_Rupture", "embed_share_Distrust", "embed_ilr_what_1", "embed_ilr_what_2"]].notna().all(axis=1)].reset_index(drop=True)
    x_matrix = build_primary_covariate_matrix(base, include_auxiliary_flags=False)
    configs = [
        {
            "track": "track1_per_cell",
            "stem": "embedding_share",
            "frame": base,
            "x_matrix": x_matrix,
            "outcomes": ["embed_share_Injury", "embed_share_Rupture", "embed_share_Distrust"],
            "specification_map": joint_track1_spec(),
            "design": build_design(base, x_matrix, ["embed_share_Injury", "embed_share_Rupture", "embed_share_Distrust"]),
        },
        {
            "track": "track1_ilr",
            "stem": "embedding_ilr",
            "frame": base,
            "x_matrix": x_matrix,
            "outcomes": ["embed_ilr_what_1", "embed_ilr_what_2"],
            "specification_map": joint_track1_spec(),
            "design": build_design(base, x_matrix, ["embed_ilr_what_1", "embed_ilr_what_2"]),
        },
    ]
    estimates = run_configs(
        configs,
        sample="main",
        output_root=output_root,
        report_prefix="R17 embedding arm",
    )
    outcome_mapping = {
        "embed_share_Injury": "share_class_Injury",
        "embed_share_Rupture": "share_class_Rupture",
        "embed_share_Distrust": "share_class_Distrust",
        "embed_ilr_what_1": "ilr_what3_1",
        "embed_ilr_what_2": "ilr_what3_2",
    }
    estimates = annotate_vs_reference(
        estimates,
        load_joint_reference(),
        on_keys=["track", "outcome", "treatment", "weight_status"],
        outcome_mapping=outcome_mapping,
    )
    return save_table(estimates, output_root / "r17_embedding_arm_v1.csv")


def run_r18(output_root: Path) -> Path:
    table = load_expressive_reference().copy()
    return save_table(table, output_root / "r18_interview_year_interaction_v1.csv")


def run_r19(main_frame: pd.DataFrame, output_root: Path) -> Path:
    configs = build_default_joint_configs(
        main_frame,
        track1_outcomes=select_outcomes(main_frame, ["share_discomposed", "share_discomposed_text", "share_composed", "share_composed_text"]),
        track2_outcomes=select_outcomes(main_frame, ["how_multimodal_score_mean", "how_multimodal_score_max", "composure_score_mean", "composure_score_max"]),
        include_ilr=False,
    )
    estimates = run_configs(
        configs,
        sample="main",
        output_root=output_root,
        report_prefix="R19 composure separate model",
    )
    estimates = annotate_vs_reference(estimates, load_joint_reference())
    return save_table(estimates, output_root / "r19_composure_separate_v1.csv")


def run_measurement_audit(output_root: Path) -> Path:
    table = pd.read_csv(MEASUREMENT_SENSITIVITY_PATH)
    table["source_path"] = MEASUREMENT_SENSITIVITY_PATH.relative_to(ROOT).as_posix()
    return save_table(table, output_root / "measurement_sensitivity_audit_v1.csv")


def run_appendix_how(output_root: Path) -> tuple[str, Path | None, str]:
    if not ARCHIVE_DB_PATH.exists():
        return "skipped", None, "Archive database is unavailable for the archived how appendix rerun."

    missing_scripts = [step["script"] for step in ARCHIVED_HOW_SCRIPTS if not step["script"].exists()]
    if missing_scripts:
        missing_text = ", ".join(path.relative_to(ROOT).as_posix() for path in missing_scripts)
        return "skipped", None, f"Archived how appendix scripts are unavailable: {missing_text}."

    manifest_rows: list[dict[str, Any]] = []
    manifest_path = output_root / "appendix_how_run_manifest_v1.csv"

    for step in ARCHIVED_HOW_SCRIPTS:
        cmd = [sys.executable, str(step["script"]), "--db", str(ARCHIVE_DB_PATH), *step["args"]]
        result = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        log_path = output_root / f"appendix_how_{step['step_id']}_run_log_v1.txt"
        log_path.write_text((result.stdout or "") + "\n" + (result.stderr or ""), encoding="utf-8")

        emitted_outputs: list[str] = []
        missing_outputs: list[str] = []
        for candidate in step["outputs"]:
            relative_path = candidate.relative_to(ROOT).as_posix()
            if candidate.exists():
                emitted_outputs.append(relative_path)
            else:
                missing_outputs.append(relative_path)

        step_status = "completed" if result.returncode == 0 and not missing_outputs else "failed"
        manifest_rows.append(
            {
                "step_id": step["step_id"],
                "label": step["label"],
                "status": step_status,
                "returncode": result.returncode,
                "script_path": step["script"].relative_to(ROOT).as_posix(),
                "log_path": log_path.relative_to(ROOT).as_posix(),
                "emitted_outputs": "; ".join(emitted_outputs),
                "missing_outputs": "; ".join(missing_outputs),
            }
        )

        if step_status != "completed":
            pd.DataFrame.from_records(manifest_rows).to_csv(manifest_path, index=False)
            if result.returncode != 0:
                return "failed", manifest_path, f"Archived how step '{step['step_id']}' exited with code {result.returncode}."
            return "failed", manifest_path, f"Archived how step '{step['step_id']}' finished without all expected outputs."

    pd.DataFrame.from_records(manifest_rows).to_csv(manifest_path, index=False)
    return "completed", manifest_path, "Archived how appendix rerun completed for archiveability, observability, MNAR, negative controls, and difficult-cases outputs."


def write_summary(registry: list[dict[str, Any]], output_path: Path) -> None:
    lines = [
        "# Robustness Battery Summary v1",
        "",
        "| Check | Label | Status | Rows | Table | Notes |",
        "|---|---|---|---:|---|---|",
    ]
    for row in registry:
        table_path = row["table_path"] or ""
        lines.append(
            f"| {row['check_id']} | {row['label']} | {row['status']} | {'' if row['rows'] is None else row['rows']} | {table_path} | {row['notes']} |"
        )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    ensure_dir(output_dir)
    requested_checks = parse_check_selection(args.checks)
    main_frame = load_model_matrix("main")
    registry: list[dict[str, Any]] = []

    for check in requested_checks:
        check_output = output_dir / check
        ensure_dir(check_output)
        try:
            print(f"[battery] starting {check}", flush=True)
            if check == "r1":
                path = run_r1(main_frame, check_output)
                record(registry, "R1", "Learner sensitivity", "completed", path, "Baseline vs RF vs Lasso under the joint continuous specification.", int(pd.read_csv(path).shape[0]))
            elif check == "r2":
                path = run_r2(main_frame, check_output)
                record(registry, "R2", "Cross-fitting folds", "completed", path, "Compared K=3, K=5, and K=10 under the joint continuous specification.", int(pd.read_csv(path).shape[0]))
            elif check == "r3":
                path = run_r3(main_frame, check_output)
                record(registry, "R3", "Treatment discretization", "completed", path, "Timing bands, dosage quartiles, and severity components replace the continuous treatment bundle.", int(pd.read_csv(path).shape[0]))
            elif check == "r4":
                path = run_r4(main_frame, check_output)
                record(registry, "R4", "Overlap trimming", "completed", path, "Trim based on adolescent-exposure propensity outside [0.05, 0.95], then re-estimate the joint model.", int(pd.read_csv(path).shape[0]))
            elif check == "r5":
                path = run_r5(check_output)
                record(registry, "R5", "Weight specification", "completed", path, "Existing baseline joint-continuous estimates grouped by unweighted, IPW, and rake runs.", int(pd.read_csv(path).shape[0]))
            elif check == "r6":
                path = run_r6(check_output)
                record(registry, "R6", "Boundary sensitivity", "completed", path, "Existing 3x3 what-axis boundary grid already generated in the outcome pipeline.", int(pd.read_csv(path).shape[0]))
            elif check == "r7":
                path = run_r7(main_frame, check_output)
                record(registry, "R7", "Alternative aggregation", "completed", path, "Alternative operationalization uses equal interview weighting before narrator aggregation.", int(pd.read_csv(path).shape[0]))
            elif check == "r8":
                path = run_r8(main_frame, check_output)
                record(registry, "R8", "Minority-signal outcomes", "completed", path, "Joint model on distrust/discomposure-heavy outcome variants.", int(pd.read_csv(path).shape[0]))
            elif check == "r9":
                path = run_r9(check_output)
                record(registry, "R9", "6-cell vs 3-class ILR", "completed", path, "Existing joint-continuous ILR estimates split into 6-cell and 3-class representations.", int(pd.read_csv(path).shape[0]))
            elif check == "r10":
                path = run_r10(check_output)
                record(registry, "R10", "Sensitivity to unobserved confounding", "completed", path, "Cinelli-Hazlett minimal sensitivity statistics computed from the baseline joint-model estimates via the sensemakr numeric formulas.", int(pd.read_csv(path).shape[0]))
            elif check == "r11":
                path = run_r11(main_frame, check_output)
                record(registry, "R11", "Exogenous severity only", "completed", path, "Restricts severity to family separation and parental arrest while retaining timing and dosage.", int(pd.read_csv(path).shape[0]))
            elif check == "r12":
                path = run_r12(main_frame, check_output)
                record(registry, "R12", "Interview-level long format", "completed", path, "Narrator-grouped cross-fitting, narrator-clustered SEs, and redistributed interview weights.", int(pd.read_csv(path).shape[0]))
            elif check == "r13":
                path = run_r13(main_frame, check_output)
                record(registry, "R13", "Sequential DML", "completed", path, "Layer-1 timing-total estimates compared to the baseline partial timing effect embedded in the joint model.", int(pd.read_csv(path).shape[0]))
            elif check == "r14":
                path = run_r14(main_frame, check_output, args.placebo_permutations)
                record(registry, "R14", "Placebo treatment", "completed", path, f"Permutation null built from {args.placebo_permutations} joint-model placebo draws.", int(pd.read_csv(path).shape[0]))
            elif check == "r15":
                path = run_r15(main_frame, check_output, args.logo_min_count, args.logo_max_groups)
                record(registry, "R15", "Leave-one-camp-out", "completed", path, "Major facilities re-estimated one at a time using the joint model.", int(pd.read_csv(path).shape[0]))
            elif check == "r16":
                path = run_r16(check_output)
                record(registry, "R16", "Recovered unknown handling", "completed", path, "Complete-case rerun using the recovered covariate matrix.", int(pd.read_csv(path).shape[0]))
            elif check == "r17":
                path = run_r17(main_frame, check_output)
                record(registry, "R17", "Embedding arm vs LLM arm", "completed", path, "Embedding-derived class-share and class-ILR outcomes re-estimated under the joint model.", int(pd.read_csv(path).shape[0]))
            elif check == "r18":
                path = run_r18(check_output)
                record(registry, "R18", "Interview-year interaction", "completed", path, "Existing expressive-environment estimates from the baseline run.", int(pd.read_csv(path).shape[0]))
            elif check == "r19":
                path = run_r19(main_frame, check_output)
                record(registry, "R19", "Composure-separate model", "completed", path, "How-only outcomes re-estimated under the joint treatment bundle.", int(pd.read_csv(path).shape[0]))
            elif check == "measurement_audit":
                path = run_measurement_audit(check_output)
                record(registry, "A1", "Track meaning audit", "completed", path, "Existing cross-track measurement-sensitivity audit.", int(pd.read_csv(path).shape[0]))
            elif check == "appendix_how":
                status, path, notes = run_appendix_how(check_output)
                row_count = None
                if path is not None and path.suffix.lower() == ".csv" and path.exists():
                    row_count = int(pd.read_csv(path).shape[0])
                record(registry, "A2", "Archived how negative controls", status, path, notes, row_count)
            else:
                record(registry, check.upper(), "Unknown request", "skipped", None, "Requested check name was not recognized.")
            print(f"[battery] completed {check}", flush=True)
        except Exception as exc:
            record(registry, check.upper(), f"{check} failed", "failed", None, str(exc))
            print(f"[battery] failed {check}: {exc}", flush=True)

    registry_table = pd.DataFrame(registry)
    save_table(registry_table, REGISTRY_PATH if output_dir == DEFAULT_OUTPUT_DIR else output_dir / REGISTRY_PATH.name)
    write_summary(registry, SUMMARY_PATH if output_dir == DEFAULT_OUTPUT_DIR else output_dir / SUMMARY_PATH.name)
    print(f"registry={REGISTRY_PATH if output_dir == DEFAULT_OUTPUT_DIR else output_dir / REGISTRY_PATH.name}")
    print(f"summary={SUMMARY_PATH if output_dir == DEFAULT_OUTPUT_DIR else output_dir / SUMMARY_PATH.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())