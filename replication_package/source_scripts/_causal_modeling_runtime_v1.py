from __future__ import annotations

import importlib.util
import json
import os
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LassoCV
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler

try:
    from lightgbm import LGBMRegressor
except ImportError:
    LGBMRegressor = None

try:
    import statsmodels.api as sm
    from statsmodels.stats.multitest import multipletests
except ImportError:
    sm = None
    multipletests = None


ROOT = Path(__file__).resolve().parents[1]
MODELING_INPUT_DIR = ROOT / "data" / "processed" / "modeling_inputs_v1"
MAIN_MATRIX_PATH = MODELING_INPUT_DIR / "narrator_model_matrix_main_v1.csv"
COMPLETE_CASE_MATRIX_PATH = MODELING_INPUT_DIR / "narrator_model_matrix_complete_case_v1.csv"
FULL_MATRIX_PATH = MODELING_INPUT_DIR / "narrator_model_matrix_v1.csv"
CAUSAL_MODEL_SPEC_PATH = ROOT / "data" / "processed" / "causal_model_spec_v1.md"
MEANING_SENSITIVITY_PATH = ROOT / "models" / "causal_estimates_v1" / "measurement_sensitivity_v1.csv"
MEANING_SENSITIVITY_REPORT_PATH = ROOT / "models" / "causal_estimates_v1" / "measurement_sensitivity_v1.md"

PROTECTION_MANIFEST_CANDIDATES = [
    ROOT / "data" / "processed" / "protected_causal_inputs_v1" / "what_how_text_phase1_canonical_realignment_2026-04-17" / "protection_manifest_v1.json",
    ROOT / "data" / "processed" / "protected_causal_inputs_v1" / "what_how_text_phase1" / "protection_manifest_v1.json",
]

TRACK1_JOINT_OUTCOMES = [
    "share_joint_Injury_composed",
    "share_joint_Injury_discomposed",
    "share_joint_Rupture_composed",
    "share_joint_Rupture_discomposed",
    "share_joint_Distrust_composed",
    "share_joint_Distrust_discomposed",
]

TRACK1_CLASS_OUTCOMES = [
    "share_class_Injury",
    "share_class_Rupture",
    "share_class_Distrust",
]

TRACK1_REGION_OUTCOMES = [
    "share_region_injury",
    "share_region_injury_disrupted",
    "share_region_adaptive_rupture",
    "share_region_default_rupture",
    "share_region_politicizing_rupture",
    "share_region_distrust",
]

TRACK1_MARGIN_OUTCOMES = [
    "share_composed",
    "share_discomposed",
    "share_composed_text",
    "share_discomposed_text",
]

TRACK2_OUTCOMES = [
    "authority_stance",
    "belonging_stance",
    "how_multimodal_score_mean",
]

PRIMARY_TREATMENTS = [
    "age_at_first_exposure",
    "total_days_incarcerated",
    "severity_index_v2",
]

SEVERITY_COMPONENT_TREATMENTS = [
    "family_separation_flag",
    "parental_arrest_flag",
    "loyalty_conflict_flag",
    "segregation_flag",
]

SEVERITY_DECOMPOSITION_TREATMENTS = [
    "age_at_first_exposure",
    "total_days_incarcerated",
    *SEVERITY_COMPONENT_TREATMENTS,
]

SECONDARY_TREATMENTS = [
    "adolescent_exposure_flag",
    "severity_index_v1",
]

CORE_COVARIATES = [
    "birth_year",
    "generation",
    "gender",
    "prewar_region",
    "interview_year",
    "age_at_interview",
]

RECOVERED_CATEGORICAL = [
    "family_ses_prewar_v1_final_v1",
    "education_prewar_v1_final_v1",
    "english_ability_prewar_v1_final_v1",
    "cultural_orientation_prewar_v1_final_v1",
]

RECOVERED_FACTUAL = [
    "born_in_japan_flag_prewar_v1_final_v1",
    "time_in_japan_flag_prewar_v1_final_v1",
    "kibei_flag_prewar_v1_final_v1",
    "japanese_language_school_flag_prewar_v1_final_v1",
]

PRIMARY_X_BLOCK = CORE_COVARIATES + RECOVERED_CATEGORICAL
EXTENDED_X_BLOCK = PRIMARY_X_BLOCK + RECOVERED_FACTUAL

WEIGHT_OPTIONS = [
    ("unweighted", None),
    ("ipw", "ipw_weight_v1"),
    ("rake", "rake_weight_v1"),
]

DEPENDENCY_MODULES = ["doubleml", "sklearn", "lightgbm", "statsmodels"]
PACKAGE_VERSION_MAP = {
    "numpy": "numpy",
    "pandas": "pandas",
    "sklearn": "scikit-learn",
    "doubleml": "doubleml",
    "statsmodels": "statsmodels",
    "lightgbm": "lightgbm",
}
DESIGN_BASE_COLUMNS = [
    "narrator_id",
    "name_full",
    "age_at_first_exposure",
    "adolescent_exposure_flag",
    "total_days_incarcerated",
    "severity_index_v1",
    "severity_index_v2",
    "interview_year_centered_v1",
    "adolescent_x_dosage_v1",
    "adolescent_x_severity_v1",
    "adolescent_x_interview_year_centered_v1",
    "ipw_weight_v1",
    "rake_weight_v1",
    "transport_weight_ready_flag_v1",
]
DEFAULT_RANDOM_STATE = 1729
DEFAULT_MAIN_FOLDS = 5
DEFAULT_COMPLETE_CASE_FOLDS = 10
ESTIMATION_ENGINE_IMPL = "crossfit_plr_residual_ols_hc3_v1"
VERBOSE_PROGRESS = os.environ.get("CAUSAL_VERBOSE_PROGRESS", "").strip().lower() in {"1", "true", "yes", "on"}


def progress(message: str) -> None:
    if VERBOSE_PROGRESS:
        print(message, flush=True)


class StandardizedLassoCVRegressor:
    def __init__(self, random_state: int, cv: int = 5) -> None:
        self.scaler = StandardScaler()
        self.model = LassoCV(
            cv=cv,
            alphas=100,
            max_iter=10000,
            n_jobs=-1,
            random_state=random_state,
            selection="random",
        )

    def fit(self, x_matrix: pd.DataFrame | np.ndarray, target: np.ndarray, sample_weight: np.ndarray | None = None):
        x_scaled = self.scaler.fit_transform(np.asarray(x_matrix, dtype=float))
        fit_kwargs: dict[str, Any] = {}
        if sample_weight is not None:
            fit_kwargs["sample_weight"] = sample_weight
        try:
            self.model.fit(x_scaled, target, **fit_kwargs)
        except TypeError:
            self.model.fit(x_scaled, target)
        return self

    def predict(self, x_matrix: pd.DataFrame | np.ndarray) -> np.ndarray:
        x_scaled = self.scaler.transform(np.asarray(x_matrix, dtype=float))
        return self.model.predict(x_scaled)


def dependency_flags() -> dict[str, bool]:
    return {module: bool(importlib.util.find_spec(module)) for module in DEPENDENCY_MODULES}


def installed_package_versions() -> dict[str, str]:
    versions: dict[str, str] = {}
    for module_name, dist_name in PACKAGE_VERSION_MAP.items():
        try:
            versions[module_name] = metadata.version(dist_name)
        except metadata.PackageNotFoundError:
            continue
    return versions


def resolve_protection_manifest() -> Path | None:
    for candidate in PROTECTION_MANIFEST_CANDIDATES:
        if candidate.exists():
            return candidate
    return None


def load_model_matrix(sample: str = "main") -> pd.DataFrame:
    path_map = {
        "main": MAIN_MATRIX_PATH,
        "complete_case": COMPLETE_CASE_MATRIX_PATH,
        "full": FULL_MATRIX_PATH,
    }
    if sample not in path_map:
        raise ValueError(f"Unsupported sample: {sample}")
    path = path_map[sample]
    if not path.exists():
        raise FileNotFoundError(f"Missing modeling input: {path}")
    frame = pd.read_csv(path)
    frame["narrator_id"] = frame["narrator_id"].astype("string").str.strip()
    return add_scaffold_features(frame)


def add_scaffold_features(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    out["age_at_interview"] = out["interview_year"] - out["birth_year"]
    interview_year_mean = float(out["interview_year"].dropna().mean())
    out["interview_year_centered_v1"] = out["interview_year"] - interview_year_mean
    out["adolescent_x_dosage_v1"] = out["adolescent_exposure_flag"] * out["total_days_incarcerated"]
    out["adolescent_x_severity_v1"] = out["adolescent_exposure_flag"] * out["severity_index_v2"]
    out["adolescent_x_interview_year_centered_v1"] = out["adolescent_exposure_flag"] * out["interview_year_centered_v1"]
    return out


def _helmert_basis(parts: int) -> np.ndarray:
    basis = np.zeros((parts, parts - 1), dtype=float)
    for column in range(parts - 1):
        scale = np.sqrt((column + 1) * (column + 2))
        basis[: column + 1, column] = 1.0 / scale
        basis[column + 1, column] = -(column + 1) / scale
    return basis


def composition_to_ilr(frame: pd.DataFrame, columns: list[str], prefix: str, eps: float = 1e-6) -> pd.DataFrame:
    composition = frame[columns].astype(float).clip(lower=0.0)
    composition = composition + eps
    composition = composition.div(composition.sum(axis=1), axis=0)
    log_comp = np.log(composition.to_numpy())
    ilr = log_comp @ _helmert_basis(len(columns))
    ilr_columns = [f"{prefix}_{index + 1}" for index in range(ilr.shape[1])]
    return pd.DataFrame(ilr, columns=ilr_columns, index=frame.index)


def build_primary_covariate_matrix(frame: pd.DataFrame, include_auxiliary_flags: bool = False) -> pd.DataFrame:
    x_block = EXTENDED_X_BLOCK if include_auxiliary_flags else PRIMARY_X_BLOCK
    covariates = frame[x_block].copy()
    categorical_columns = [
        "generation",
        "gender",
        "prewar_region",
        *RECOVERED_CATEGORICAL,
    ]
    encoded = pd.get_dummies(covariates, columns=categorical_columns, prefix_sep="__", dtype=int)
    encoded = encoded.astype(float)
    if encoded.isna().any().any():
        encoded = encoded.fillna(encoded.median(numeric_only=True)).fillna(0.0)
    return encoded


def build_task_grid(
    frame: pd.DataFrame,
    track: str,
    outcomes: list[str],
    specification_map: dict[str, dict[str, Any]],
    weight_options: list[tuple[str, str | None]] | None = None,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    active_weight_options = weight_options or WEIGHT_OPTIONS
    for outcome in outcomes:
        for spec_id, spec in specification_map.items():
            treatment_columns = list(spec["treatment_columns"])
            x_exclude_columns = list(spec.get("x_exclude_columns", []))
            for weight_status, weight_var in active_weight_options:
                if weight_var is None:
                    sample_n = int(len(frame))
                else:
                    sample_n = int(frame[weight_var].notna().sum())
                rows.append(
                    {
                        "track": track,
                        "outcome": outcome,
                        "spec_id": spec_id,
                        "spec_label": spec["label"],
                        "hypothesis_family": spec["hypothesis_family"],
                        "treatment_columns": ";".join(treatment_columns),
                        "n_treatments": len(treatment_columns),
                        "weight_status": weight_status,
                        "weight_column": weight_var or "",
                        "sample_n": sample_n,
                        "engine_target": spec["engine_target"],
                        "x_block_id": spec.get("x_block_id", "primary"),
                        "x_exclude_columns": ";".join(x_exclude_columns),
                        "status": "pending_estimation",
                        "notes": spec["notes"],
                    }
                )
    return pd.DataFrame(rows)


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def choose_fold_count(sample: str, override: int | None = None) -> int:
    if override is not None:
        return max(2, int(override))
    if sample == "complete_case":
        return DEFAULT_COMPLETE_CASE_FOLDS
    return DEFAULT_MAIN_FOLDS


def build_crossfit_splits(
    n_samples: int,
    n_folds: int,
    random_state: int,
    group_ids: pd.Series | np.ndarray | None = None,
) -> list[tuple[np.ndarray, np.ndarray]]:
    if group_ids is not None:
        groups = pd.Series(group_ids).reset_index(drop=True)
        unique_groups = groups.drop_duplicates().tolist()
        if 1 < len(unique_groups) < n_samples:
            folds = max(2, min(int(n_folds), len(unique_groups)))
            rng = np.random.default_rng(random_state)
            shuffled_groups = np.asarray(unique_groups, dtype=object)
            rng.shuffle(shuffled_groups)
            group_partitions = np.array_split(shuffled_groups, folds)
            group_array = groups.to_numpy(dtype=object)
            splits: list[tuple[np.ndarray, np.ndarray]] = []
            for fold_groups in group_partitions:
                test_mask = np.isin(group_array, fold_groups)
                test_index = np.flatnonzero(test_mask)
                train_index = np.flatnonzero(~test_mask)
                if len(test_index) == 0 or len(train_index) == 0:
                    continue
                splits.append((train_index, test_index))
            if len(splits) >= 2:
                return splits

    folds = max(2, min(int(n_folds), int(n_samples)))
    if folds >= n_samples:
        folds = max(2, n_samples // 2)
    splitter = KFold(n_splits=folds, shuffle=True, random_state=random_state)
    index = np.arange(n_samples)
    return list(splitter.split(index))


def default_nuisance_learner_name(preferred: str | None = None) -> str:
    allowed = {
        "lightgbm_regressor",
        "random_forest_regressor",
        "lasso_cv_regressor",
    }
    if preferred is not None:
        if preferred not in allowed:
            raise ValueError(f"Unsupported nuisance learner: {preferred}")
        return preferred
    if LGBMRegressor is not None:
        return "lightgbm_regressor"
    return "random_forest_regressor"


def build_nuisance_model(random_state: int, learner_name: str | None = None):
    chosen = default_nuisance_learner_name(learner_name)
    if chosen == "lightgbm_regressor":
        if LGBMRegressor is None:
            raise ImportError("lightgbm is required for nuisance_learner=lightgbm_regressor")
        return LGBMRegressor(
            objective="regression",
            n_estimators=200,
            learning_rate=0.05,
            num_leaves=31,
            min_child_samples=10,
            subsample=0.85,
            colsample_bytree=0.85,
            reg_lambda=0.5,
            random_state=random_state,
            n_jobs=-1,
            verbosity=-1,
        )
    if chosen == "lasso_cv_regressor":
        return StandardizedLassoCVRegressor(random_state=random_state)
    return RandomForestRegressor(
        n_estimators=400,
        min_samples_leaf=5,
        random_state=random_state,
        n_jobs=-1,
    )


def fit_nuisance_model(
    model: Any,
    x_matrix: pd.DataFrame,
    target: np.ndarray,
    sample_weight: np.ndarray | None,
) -> Any:
    if sample_weight is None:
        model.fit(x_matrix, target)
        return model
    try:
        model.fit(x_matrix, target, sample_weight=sample_weight)
    except TypeError:
        model.fit(x_matrix, target)
    return model


def weighted_r2(y_true: np.ndarray, y_pred: np.ndarray, sample_weight: np.ndarray | None = None) -> float:
    if sample_weight is None:
        centered = y_true - float(np.mean(y_true))
        denominator = float(np.sum(centered**2))
        numerator = float(np.sum((y_true - y_pred) ** 2))
    else:
        mean_value = float(np.average(y_true, weights=sample_weight))
        denominator = float(np.sum(sample_weight * (y_true - mean_value) ** 2))
        numerator = float(np.sum(sample_weight * (y_true - y_pred) ** 2))
    if denominator <= 0:
        return float("nan")
    return 1.0 - numerator / denominator


def crossfit_residualize(
    target: pd.Series,
    x_matrix: pd.DataFrame,
    sample_weight: np.ndarray | None,
    splits: list[tuple[np.ndarray, np.ndarray]],
    random_state: int,
    nuisance_learner: str | None = None,
) -> dict[str, Any]:
    target_array = target.astype(float).to_numpy()
    feature_matrix = x_matrix.astype(float).reset_index(drop=True)
    predictions = np.zeros(len(target_array), dtype=float)
    fold_assignments = np.full(len(target_array), -1, dtype=int)

    for fold_number, (train_index, test_index) in enumerate(splits, start=1):
        progress(f"[crossfit] fold={fold_number}/{len(splits)} train={len(train_index)} test={len(test_index)}")
        model = build_nuisance_model(random_state + fold_number, nuisance_learner)
        fit_nuisance_model(
            model,
            feature_matrix.iloc[train_index],
            target_array[train_index],
            sample_weight[train_index] if sample_weight is not None else None,
        )
        predictions[test_index] = model.predict(feature_matrix.iloc[test_index])
        fold_assignments[test_index] = fold_number

    residuals = target_array - predictions
    return {
        "predictions": predictions,
        "residuals": residuals,
        "fold_assignments": fold_assignments,
        "oof_r2": weighted_r2(target_array, predictions, sample_weight),
    }


def fit_partial_linear_regression(
    outcome_residuals: np.ndarray,
    treatment_residuals: pd.DataFrame,
    sample_weight: np.ndarray | None,
    cluster_ids: pd.Series | np.ndarray | None = None,
) -> dict[str, Any]:
    if sm is None:
        raise ImportError("statsmodels is required for the residual-on-residual regression step.")

    near_zero_treatments = [
        column
        for column in treatment_residuals.columns
        if float(np.std(treatment_residuals[column].to_numpy(dtype=float))) < 1e-8
    ]
    if near_zero_treatments:
        joined = ", ".join(near_zero_treatments)
        raise ValueError(f"Residualized treatment variance is effectively zero for: {joined}")

    design_matrix = sm.add_constant(treatment_residuals.astype(float), has_constant="add")
    if sample_weight is None:
        model = sm.OLS(outcome_residuals, design_matrix)
    else:
        model = sm.WLS(outcome_residuals, design_matrix, weights=sample_weight)

    if cluster_ids is None or pd.Series(cluster_ids).nunique(dropna=False) < 2:
        fitted = model.fit(cov_type="HC3")
    else:
        fitted = model.fit(cov_type="cluster", cov_kwds={"groups": np.asarray(cluster_ids)})
    confidence_intervals = fitted.conf_int()
    coefficient_rows: list[dict[str, float]] = []
    for treatment in treatment_residuals.columns:
        coefficient_rows.append(
            {
                "treatment": treatment,
                "estimate": float(fitted.params[treatment]),
                "std_error": float(fitted.bse[treatment]),
                "p_value": float(fitted.pvalues[treatment]),
                "ci_low": float(confidence_intervals.loc[treatment, 0]),
                "ci_high": float(confidence_intervals.loc[treatment, 1]),
            }
        )

    return {
        "coefficients": coefficient_rows,
        "model_r2": float(getattr(fitted, "rsquared", np.nan)),
        "condition_number": float(np.linalg.cond(design_matrix.to_numpy(dtype=float))),
    }


def resolve_x_columns(x_matrix: pd.DataFrame, x_exclude_columns: list[str]) -> list[str]:
    excluded = set(x_exclude_columns)
    return [column for column in x_matrix.columns if column not in excluded]


def estimate_task_grid(
    *,
    frame: pd.DataFrame,
    x_matrix: pd.DataFrame,
    task_grid: pd.DataFrame,
    track: str,
    sample: str,
    folds: int,
    random_state: int,
    nuisance_learner: str | None = None,
    group_ids: pd.Series | np.ndarray | None = None,
    cluster_ids: pd.Series | np.ndarray | None = None,
    weight_options: list[tuple[str, str | None]] | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if sm is None:
        raise ImportError("statsmodels is required for estimation. Install requirements-causal-modeling-v1.txt first.")

    results_rows: list[dict[str, Any]] = []
    diagnostics_rows: list[dict[str, Any]] = []
    updated_tasks: list[dict[str, Any]] = []
    chosen_nuisance_learner = default_nuisance_learner_name(nuisance_learner)
    active_weight_options = weight_options or WEIGHT_OPTIONS
    x_matrix = x_matrix.copy()

    for weight_status, weight_column in active_weight_options:
        progress(f"[estimate] weight_status={weight_status} weight_column={weight_column or 'none'}")
        current_tasks = task_grid[task_grid["weight_status"] == weight_status].copy()
        if current_tasks.empty:
            continue

        if weight_column is None:
            subset_mask = pd.Series(True, index=frame.index)
        else:
            subset_mask = frame[weight_column].notna()

        subset_frame = frame.loc[subset_mask].reset_index(drop=True)
        sample_weight = None
        if weight_column is not None:
            sample_weight = subset_frame[weight_column].astype(float).to_numpy()
        subset_group_ids = None
        if group_ids is not None:
            subset_group_ids = pd.Series(group_ids, index=frame.index).loc[subset_mask].reset_index(drop=True)
        subset_cluster_ids = None
        if cluster_ids is not None:
            subset_cluster_ids = pd.Series(cluster_ids, index=frame.index).loc[subset_mask].reset_index(drop=True)

        x_key_to_columns: dict[str, list[str]] = {}
        residual_cache: dict[tuple[str, str, str], dict[str, Any]] = {}

        for _, task in current_tasks.iterrows():
            x_key = str(task["x_block_id"])
            if x_key not in x_key_to_columns:
                excluded = [value for value in str(task["x_exclude_columns"]).split(";") if value]
                x_key_to_columns[x_key] = resolve_x_columns(x_matrix, excluded)

        for x_key, x_columns in x_key_to_columns.items():
            x_subset = x_matrix.loc[subset_mask, x_columns].reset_index(drop=True)
            if x_subset.isna().any().any():
                raise ValueError(f"Missing values remain in the encoded covariate matrix for x_block_id={x_key}")

            splits = build_crossfit_splits(len(x_subset), folds, random_state, group_ids=subset_group_ids)
            x_key_tasks = current_tasks[current_tasks["x_block_id"] == x_key]
            progress(
                f"[estimate] x_block={x_key} rows={len(x_subset)} folds={len(splits)} outcomes={x_key_tasks['outcome'].nunique()} treatments="
                f"{len(sorted({treatment for treatment_columns in x_key_tasks['treatment_columns'] for treatment in str(treatment_columns).split(';') if treatment}))}"
            )

            unique_outcomes = sorted(x_key_tasks["outcome"].unique())
            for outcome in unique_outcomes:
                if subset_frame[outcome].isna().any():
                    raise ValueError(f"Missing outcome values detected for outcome={outcome} in sample={sample}")
                progress(f"[estimate] residualizing outcome={outcome}")
                residual_cache[(x_key, "outcome", outcome)] = crossfit_residualize(
                    subset_frame[outcome],
                    x_subset,
                    sample_weight,
                    splits,
                    random_state,
                    chosen_nuisance_learner,
                )

            unique_treatments = sorted(
                {
                    treatment
                    for treatment_columns in x_key_tasks["treatment_columns"]
                    for treatment in str(treatment_columns).split(";")
                    if treatment
                }
            )
            for treatment in unique_treatments:
                if subset_frame[treatment].isna().any():
                    raise ValueError(f"Missing treatment values detected for treatment={treatment} in sample={sample}")
                progress(f"[estimate] residualizing treatment={treatment}")
                residual_cache[(x_key, "treatment", treatment)] = crossfit_residualize(
                    subset_frame[treatment],
                    x_subset,
                    sample_weight,
                    splits,
                    random_state + 1000,
                    chosen_nuisance_learner,
                )

        for _, task in current_tasks.iterrows():
            treatment_columns = [value for value in str(task["treatment_columns"]).split(";") if value]
            x_key = str(task["x_block_id"])
            x_columns = x_key_to_columns[x_key]
            progress(
                f"[estimate] fitting track={track} outcome={task['outcome']} spec={task['spec_id']} weight={task['weight_status']} treatments={','.join(treatment_columns)}"
            )
            task_record = task.to_dict()
            task_record.update(
                {
                    "folds": folds,
                    "nuisance_learner": nuisance_learner,
                    "x_feature_count": len(x_columns),
                    "engine_impl": ESTIMATION_ENGINE_IMPL,
                }
            )

            try:
                outcome_cache = residual_cache[(x_key, "outcome", str(task["outcome"]))]
                treatment_residuals = pd.DataFrame(
                    {
                        treatment: residual_cache[(x_key, "treatment", treatment)]["residuals"]
                        for treatment in treatment_columns
                    }
                )
                fitted = fit_partial_linear_regression(
                    outcome_cache["residuals"],
                    treatment_residuals,
                    sample_weight,
                    subset_cluster_ids,
                )
                treatment_r2 = {
                    treatment: float(residual_cache[(x_key, "treatment", treatment)]["oof_r2"])
                    for treatment in treatment_columns
                }
                mean_treatment_r2 = float(np.nanmean(list(treatment_r2.values())))

                diagnostics_rows.append(
                    {
                        "track": track,
                        "sample": sample,
                        "outcome": task["outcome"],
                        "spec_id": task["spec_id"],
                        "spec_label": task["spec_label"],
                        "weight_status": task["weight_status"],
                        "weight_column": task["weight_column"],
                        "sample_n": int(task["sample_n"]),
                        "folds": folds,
                        "nuisance_learner": chosen_nuisance_learner,
                        "x_block_id": x_key,
                        "x_exclude_columns": task["x_exclude_columns"],
                        "x_feature_count": len(x_columns),
                        "outcome_oof_r2": float(outcome_cache["oof_r2"]),
                        "mean_treatment_oof_r2": mean_treatment_r2,
                        "min_treatment_oof_r2": float(np.nanmin(list(treatment_r2.values()))),
                        "max_treatment_oof_r2": float(np.nanmax(list(treatment_r2.values()))),
                        "final_model_r2": fitted["model_r2"],
                        "condition_number": fitted["condition_number"],
                        "status": "estimated",
                        "error_message": "",
                    }
                )

                for coefficient in fitted["coefficients"]:
                    results_rows.append(
                        {
                            "track": track,
                            "sample": sample,
                            "outcome": task["outcome"],
                            "spec_id": task["spec_id"],
                            "spec_label": task["spec_label"],
                            "hypothesis_family": task["hypothesis_family"],
                            "weight_status": task["weight_status"],
                            "weight_column": task["weight_column"],
                            "sample_n": int(task["sample_n"]),
                            "folds": folds,
                            "nuisance_learner": chosen_nuisance_learner,
                            "engine_impl": ESTIMATION_ENGINE_IMPL,
                            "x_block_id": x_key,
                            "x_exclude_columns": task["x_exclude_columns"],
                            "x_feature_count": len(x_columns),
                            "treatment": coefficient["treatment"],
                            "estimate": coefficient["estimate"],
                            "std_error": coefficient["std_error"],
                            "ci_low": coefficient["ci_low"],
                            "ci_high": coefficient["ci_high"],
                            "p_value": coefficient["p_value"],
                            "outcome_oof_r2": float(outcome_cache["oof_r2"]),
                            "treatment_oof_r2": treatment_r2[coefficient["treatment"]],
                            "mean_treatment_oof_r2": mean_treatment_r2,
                            "final_model_r2": fitted["model_r2"],
                            "condition_number": fitted["condition_number"],
                        }
                    )

                task_record.update(
                    {
                        "status": "estimated",
                        "coefficient_rows": len(fitted["coefficients"]),
                        "outcome_oof_r2": float(outcome_cache["oof_r2"]),
                        "mean_treatment_oof_r2": mean_treatment_r2,
                        "final_model_r2": fitted["model_r2"],
                        "condition_number": fitted["condition_number"],
                        "error_message": "",
                    }
                )
            except Exception as exc:
                diagnostics_rows.append(
                    {
                        "track": track,
                        "sample": sample,
                        "outcome": task["outcome"],
                        "spec_id": task["spec_id"],
                        "spec_label": task["spec_label"],
                        "weight_status": task["weight_status"],
                        "weight_column": task["weight_column"],
                        "sample_n": int(task["sample_n"]),
                        "folds": folds,
                        "nuisance_learner": chosen_nuisance_learner,
                        "x_block_id": x_key,
                        "x_exclude_columns": task["x_exclude_columns"],
                        "x_feature_count": len(x_columns),
                        "outcome_oof_r2": float("nan"),
                        "mean_treatment_oof_r2": float("nan"),
                        "min_treatment_oof_r2": float("nan"),
                        "max_treatment_oof_r2": float("nan"),
                        "final_model_r2": float("nan"),
                        "condition_number": float("nan"),
                        "status": "failed",
                        "error_message": str(exc),
                    }
                )
                task_record.update(
                    {
                        "status": "failed",
                        "coefficient_rows": 0,
                        "outcome_oof_r2": float("nan"),
                        "mean_treatment_oof_r2": float("nan"),
                        "final_model_r2": float("nan"),
                        "condition_number": float("nan"),
                        "error_message": str(exc),
                    }
                )

            updated_tasks.append(task_record)

    results = pd.DataFrame(results_rows)
    if not results.empty and multipletests is not None:
        filled_p_values = results["p_value"].fillna(1.0).to_numpy()
        reject_bh, p_value_adj_bh, _, _ = multipletests(filled_p_values, method="fdr_bh")
        reject_holm, p_value_adj_holm, _, _ = multipletests(filled_p_values, method="holm")
        results["p_value_adj_bh"] = p_value_adj_bh
        results["p_value_adj_holm"] = p_value_adj_holm
        results["significant_bh_0_05"] = reject_bh.astype(int)
        results["significant_holm_0_05"] = reject_holm.astype(int)

    diagnostics = pd.DataFrame(diagnostics_rows)
    task_grid_completed = pd.DataFrame(updated_tasks)
    return results, diagnostics, task_grid_completed


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_plr_track(
    *,
    track: str,
    sample: str,
    frame: pd.DataFrame,
    x_matrix: pd.DataFrame,
    design: pd.DataFrame,
    outcomes: list[str],
    specification_map: dict[str, dict[str, Any]],
    output_dir: Path,
    output_stem: str,
    report_title: str,
    script_name: str,
    folds: int | None = None,
    random_state: int = DEFAULT_RANDOM_STATE,
    nuisance_learner: str | None = None,
    group_ids: pd.Series | np.ndarray | None = None,
    cluster_ids: pd.Series | np.ndarray | None = None,
    weight_options: list[tuple[str, str | None]] | None = None,
) -> dict[str, Path]:
    ensure_dir(output_dir)
    chosen_folds = choose_fold_count(sample, folds)
    active_weight_options = weight_options or WEIGHT_OPTIONS
    chosen_nuisance_learner = default_nuisance_learner_name(nuisance_learner)
    task_grid = build_task_grid(frame, track, outcomes, specification_map, active_weight_options)
    estimates, diagnostics, task_grid_completed = estimate_task_grid(
        frame=frame,
        x_matrix=x_matrix,
        task_grid=task_grid,
        track=track,
        sample=sample,
        folds=chosen_folds,
        random_state=random_state,
        nuisance_learner=chosen_nuisance_learner,
        group_ids=group_ids,
        cluster_ids=cluster_ids,
        weight_options=active_weight_options,
    )

    design_path = output_dir / f"{output_stem}_design_v1.csv"
    task_path = output_dir / f"{output_stem}_task_grid_v1.csv"
    estimates_path = output_dir / f"{output_stem}_estimates_v1.csv"
    diagnostics_path = output_dir / f"{output_stem}_diagnostics_v1.csv"
    report_path = output_dir / f"{output_stem}_report_v1.md"
    manifest_path = output_dir / f"{output_stem}_run_manifest_v1.json"

    design.to_csv(design_path, index=False)
    task_grid_completed.to_csv(task_path, index=False)
    estimates.to_csv(estimates_path, index=False)
    diagnostics.to_csv(diagnostics_path, index=False)

    dependency_state = dependency_flags()
    protection_manifest = resolve_protection_manifest()
    manifest_payload = {
        "track": track,
        "sample": sample,
        "rows": int(len(frame)),
        "outcomes": outcomes,
        "crossfit_folds": chosen_folds,
        "random_state": random_state,
        "nuisance_learner": chosen_nuisance_learner,
        "engine_impl": ESTIMATION_ENGINE_IMPL,
        "script_name": script_name,
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "protection_manifest": protection_manifest.relative_to(ROOT).as_posix() if protection_manifest else None,
        "dependency_flags": dependency_state,
        "package_versions": installed_package_versions(),
        "weight_status_row_counts": {
            row["weight_status"]: int(row["sample_n"])
            for _, row in task_grid_completed[["weight_status", "sample_n"]].drop_duplicates().iterrows()
        },
        "output_files": {
            "design": design_path.relative_to(ROOT).as_posix(),
            "task_grid": task_path.relative_to(ROOT).as_posix(),
            "estimates": estimates_path.relative_to(ROOT).as_posix(),
            "diagnostics": diagnostics_path.relative_to(ROOT).as_posix(),
            "report": report_path.relative_to(ROOT).as_posix(),
        },
    }
    write_json(manifest_path, manifest_payload)

    estimated_tasks = int((task_grid_completed["status"] == "estimated").sum()) if not task_grid_completed.empty else 0
    failed_tasks = int((task_grid_completed["status"] == "failed").sum()) if not task_grid_completed.empty else 0
    lines = [
        f"# {report_title}",
        "",
        f"- sample: {sample}",
        f"- rows: {len(frame)}",
        f"- outcomes: {len(outcomes)}",
        f"- task rows: {len(task_grid_completed)}",
        f"- estimated tasks: {estimated_tasks}",
        f"- failed tasks: {failed_tasks}",
        f"- coefficient rows: {len(estimates)}",
        f"- nuisance learner: {chosen_nuisance_learner}",
        f"- estimation engine: {ESTIMATION_ENGINE_IMPL}",
        f"- cross-fit folds: {chosen_folds}",
        f"- design file: `{design_path.relative_to(ROOT).as_posix()}`",
        f"- task grid: `{task_path.relative_to(ROOT).as_posix()}`",
        f"- estimates file: `{estimates_path.relative_to(ROOT).as_posix()}`",
        f"- diagnostics file: `{diagnostics_path.relative_to(ROOT).as_posix()}`",
        f"- run manifest: `{manifest_path.relative_to(ROOT).as_posix()}`",
        f"- doubleml available: {dependency_state['doubleml']}",
        f"- sklearn available: {dependency_state['sklearn']}",
        f"- lightgbm available: {dependency_state['lightgbm']}",
        f"- statsmodels available: {dependency_state['statsmodels']}",
        "- status: estimation completed.",
    ]
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    write_causal_model_spec()

    return {
        "design": design_path,
        "task_grid": task_path,
        "estimates": estimates_path,
        "diagnostics": diagnostics_path,
        "report": report_path,
        "manifest": manifest_path,
    }


def write_causal_model_spec() -> None:
    full_frame = load_model_matrix("full")
    main_frame = load_model_matrix("main")
    complete_case = load_model_matrix("complete_case")
    manifest_path = resolve_protection_manifest()
    deps = dependency_flags()

    lines = [
        "# Causal Model Spec v1",
        "",
        "## Inputs",
        f"- Full outcome-defined matrix: `{FULL_MATRIX_PATH.relative_to(ROOT).as_posix()}`",
        f"- Main modeling matrix: `{MAIN_MATRIX_PATH.relative_to(ROOT).as_posix()}`",
        f"- Recovered complete-case matrix: `{COMPLETE_CASE_MATRIX_PATH.relative_to(ROOT).as_posix()}`",
        f"- Protected manifest: `{manifest_path.relative_to(ROOT).as_posix()}`" if manifest_path else "- Protected manifest: not found",
        "",
        "## Sample Counts",
        f"- Outcome-defined rows: {len(full_frame)}",
        f"- Main rows: {len(main_frame)}",
        f"- Recovered complete-case rows: {len(complete_case)}",
        f"- Weighted-ready main rows: {int(main_frame['transport_weight_ready_flag_v1'].sum())}",
        "",
        "## Primary Treatments",
        "- age_at_first_exposure",
        "- total_days_incarcerated",
        "- severity_index_v2",
        "",
        "## Secondary Timing / Robustness Terms",
        "- adolescent_exposure_flag",
        "- severity_index_v1",
        "- adolescent_x_dosage_v1",
        "- adolescent_x_severity_v1",
        "- adolescent_x_interview_year_centered_v1",
        "",
        "## Primary Covariate Block",
    ]
    lines.extend([f"- {column}" for column in PRIMARY_X_BLOCK])
    lines.extend([
        "",
        "## Auxiliary Factual Flags",
    ])
    lines.extend([f"- {column}" for column in RECOVERED_FACTUAL])
    lines.extend([
        "",
        "## Output Roots",
        "- `models/causal_estimates_v1/track1_ilr_v1/`",
        "- `models/causal_estimates_v1/track1_per_cell_v1/`",
        "- `models/causal_estimates_v1/track2_v1/`",
        "- `models/causal_estimates_v1/measurement_sensitivity_v1.csv`",
        "",
        "## Outcome Families",
        "- Track 1 ILR on six-cell and three-class share outcomes",
        "- Track 1 per-cell share PLR estimates",
        "- Track 2 continuous authority/belonging/multimodal How estimates",
        "",
        "## Dependency Snapshot",
    ])
    lines.extend([f"- {name}: {'available' if available else 'missing'}" for name, available in deps.items()])

    CAUSAL_MODEL_SPEC_PATH.parent.mkdir(parents=True, exist_ok=True)
    CAUSAL_MODEL_SPEC_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def default_track1_specifications() -> dict[str, dict[str, Any]]:
    return {
        "joint_continuous": {
            "label": "Joint continuous treatments",
            "hypothesis_family": "H3",
            "treatment_columns": PRIMARY_TREATMENTS,
            "engine_target": "dml_plr",
            "x_block_id": "primary",
            "x_exclude_columns": [],
            "notes": "Primary joint timing/dosage/severity comparison.",
        },
        "timing_dummy": {
            "label": "Adolescent timing contrast",
            "hypothesis_family": "H1",
            "treatment_columns": ["adolescent_exposure_flag"],
            "engine_target": "dml_plr",
            "x_block_id": "primary",
            "x_exclude_columns": [],
            "notes": "Sensitive-period timing contrast.",
        },
        "amplification": {
            "label": "Timing amplification interactions",
            "hypothesis_family": "H4",
            "treatment_columns": [
                "adolescent_exposure_flag",
                "total_days_incarcerated",
                "severity_index_v2",
                "adolescent_x_dosage_v1",
                "adolescent_x_severity_v1",
            ],
            "engine_target": "dml_plr",
            "x_block_id": "primary",
            "x_exclude_columns": [],
            "notes": "Interaction model for timing-by-dosage and timing-by-severity.",
        },
        "expressive_environment": {
            "label": "Interview-year moderation",
            "hypothesis_family": "H5",
            "treatment_columns": [
                "adolescent_exposure_flag",
                "interview_year_centered_v1",
                "adolescent_x_interview_year_centered_v1",
            ],
            "engine_target": "dml_plr",
            "x_block_id": "h5_no_interview_year_controls",
            "x_exclude_columns": ["interview_year", "age_at_interview"],
            "notes": "Interview-year moderation with direct interview-year controls removed from X to avoid exact collinearity.",
        },
    }


def default_track2_specifications() -> dict[str, dict[str, Any]]:
    return {
        "joint_continuous": {
            "label": "Joint continuous treatments",
            "hypothesis_family": "H3",
            "treatment_columns": PRIMARY_TREATMENTS,
            "engine_target": "dml_plr",
            "x_block_id": "primary",
            "x_exclude_columns": [],
            "notes": "Primary Track 2 joint mechanism comparison.",
        },
        "timing_dummy": {
            "label": "Adolescent timing contrast",
            "hypothesis_family": "H1_H2",
            "treatment_columns": ["adolescent_exposure_flag"],
            "engine_target": "dml_plr",
            "x_block_id": "primary",
            "x_exclude_columns": [],
            "notes": "Timing-only contrast for Track 2 continuous outcomes.",
        },
        "amplification": {
            "label": "Timing amplification interactions",
            "hypothesis_family": "H4",
            "treatment_columns": [
                "adolescent_exposure_flag",
                "total_days_incarcerated",
                "severity_index_v2",
                "adolescent_x_dosage_v1",
                "adolescent_x_severity_v1",
            ],
            "engine_target": "dml_plr",
            "x_block_id": "primary",
            "x_exclude_columns": [],
            "notes": "Interaction model for Track 2.",
        },
        "expressive_environment": {
            "label": "Interview-year moderation",
            "hypothesis_family": "H5",
            "treatment_columns": [
                "adolescent_exposure_flag",
                "interview_year_centered_v1",
                "adolescent_x_interview_year_centered_v1",
            ],
            "engine_target": "dml_plr",
            "x_block_id": "h5_no_interview_year_controls",
            "x_exclude_columns": ["interview_year", "age_at_interview"],
            "notes": "Interview-year moderation with direct interview-year controls removed from X to avoid exact collinearity.",
        },
    }


def severity_component_specifications() -> dict[str, dict[str, Any]]:
    return {
        "severity_components": {
            "label": "Severity component decomposition",
            "hypothesis_family": "R11_component_decomposition",
            "treatment_columns": SEVERITY_DECOMPOSITION_TREATMENTS,
            "engine_target": "dml_plr",
            "x_block_id": "primary",
            "x_exclude_columns": [],
            "notes": "Timing and dosage retained while the main severity index is decomposed into four component flags.",
        },
    }