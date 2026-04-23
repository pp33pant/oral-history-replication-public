#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "models" / "causal_estimates_v1"
MEMO_PATH = OUTPUT_DIR / "causal_estimates_readout_memo_v2.md"

MEMO_TITLE = "Causal Estimates Readout Memo v2"
MEMO_DATE = "2026-04-19"
STATUS_LINE = "Status: Release-facing v2 memo for the frozen 2026-04-20 causal-results archive."
SOURCE_SCRIPT_DISPLAY = "scripts/build_causal_readout_memo_v2.py"

MAIN_TREATMENT_SOURCES = {
	"ilr_joint6": OUTPUT_DIR / "track1_ilr_v1" / "track1_ilr_estimates_v1.csv",
	"plr_joint_shares": OUTPUT_DIR / "track1_per_cell_v1" / "track1_per_cell_estimates_v1.csv",
	"track2_continuous": OUTPUT_DIR / "track2_v1" / "track2_estimates_v1.csv",
}

COMPONENT_SOURCES = {
	"ilr_joint6_components": OUTPUT_DIR / "track1_ilr_severity_components_v1" / "track1_ilr_severity_components_estimates_v1.csv",
	"plr_joint_share_components": OUTPUT_DIR / "track1_per_cell_severity_components_v1" / "track1_per_cell_severity_components_estimates_v1.csv",
	"track2_continuous_components": OUTPUT_DIR / "track2_severity_components_v1" / "track2_severity_components_estimates_v1.csv",
}

WEIGHT_TITLES = {
	"unweighted": "Unweighted",
	"ipw": "IPW",
	"rake": "Rake",
}

MAIN_OUTCOMES = {
	"ilr_joint6": [f"ilr_joint6_{index}" for index in range(1, 6)],
	"plr_joint_shares": [
		"share_joint_Injury_composed",
		"share_joint_Injury_discomposed",
		"share_joint_Rupture_composed",
		"share_joint_Rupture_discomposed",
		"share_joint_Distrust_composed",
		"share_joint_Distrust_discomposed",
	],
	"track2_continuous": [
		"authority_stance",
		"belonging_stance",
		"how_multimodal_score_mean",
	],
}

SECTION_TITLES = {
	"ilr_joint6": "ILR Joint6",
	"plr_joint_shares": "PLR Joint Shares",
	"track2_continuous": "Track 2 Continuous",
	"ilr_joint6_components": "ILR Joint6 Components",
	"plr_joint_share_components": "PLR Joint Share Components",
	"track2_continuous_components": "Track 2 Continuous Components",
}

MAIN_ROW_SPECS = [
	("timing_dummy", "adolescent_exposure_flag", "Timing D: adolescent_exposure_flag"),
	("joint_continuous", "age_at_first_exposure", "Timing C: age_at_first_exposure"),
	("joint_continuous", "total_days_incarcerated", "Dosage: total_days_incarcerated"),
	("joint_continuous", "severity_index_v2", "Severity: severity_index_v2"),
]

COMPONENT_ROW_SPECS = [
	("severity_components", "age_at_first_exposure", "Timing C: age_at_first_exposure"),
	("severity_components", "total_days_incarcerated", "Dosage: total_days_incarcerated"),
	("severity_components", "family_separation_flag", "Component: family_separation_flag"),
	("severity_components", "parental_arrest_flag", "Component: parental_arrest_flag"),
	("severity_components", "loyalty_conflict_flag", "Component: loyalty_conflict_flag"),
	("severity_components", "segregation_flag", "Component: segregation_flag"),
]


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Build the causal readout memo with BH q-values.")
	parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
	return parser.parse_args()


def format_number(value: float) -> str:
	return f"{value:.4g}"


def format_p_value(value: float) -> str:
	if value < 0.001:
		return "<0.001"
	return f"{value:.3g}"


def format_q_value(value: float) -> str:
	if pd.isna(value):
		return "NA"
	if value < 0.001:
		return "<0.001"
	return f"{value:.3g}"


def star_label_q(q_value: float) -> str:
	if pd.isna(q_value):
		return ""
	if q_value < 0.001:
		return "***"
	if q_value < 0.01:
		return "**"
	if q_value < 0.05:
		return "*"
	return ""


def format_cell(row: pd.Series) -> str:
	q_value = float(row["p_value_adj_bh"])
	return (
		f"{format_number(float(row['estimate']))}{star_label_q(q_value)} "
		f"({format_number(float(row['std_error']))}); "
		f"p={format_p_value(float(row['p_value']))}; "
		f"q={format_q_value(q_value)}"
	)


def format_result_pair(row: pd.Series) -> str:
	return f"p={format_p_value(float(row['p_value']))}, q={format_q_value(float(row['p_value_adj_bh']))}"


def markdown_table(frame: pd.DataFrame) -> list[str]:
	columns = frame.columns.tolist()
	lines = [
		"| " + " | ".join(columns) + " |",
		"| " + " | ".join(["---"] * len(columns)) + " |",
	]
	for _, row in frame.iterrows():
		lines.append("| " + " | ".join(str(row[column]) for column in columns) + " |")
	return lines


def load_sources(source_map: dict[str, Path]) -> dict[str, pd.DataFrame]:
	return {key: pd.read_csv(path) for key, path in source_map.items()}


def select_row(frame: pd.DataFrame, weight_status: str, spec_id: str, treatment: str, outcome: str) -> pd.Series:
	match = frame[
		(frame["weight_status"] == weight_status)
		& (frame["spec_id"] == spec_id)
		& (frame["treatment"] == treatment)
		& (frame["outcome"] == outcome)
	]
	if match.empty:
		raise KeyError((weight_status, spec_id, treatment, outcome))
	return match.iloc[0]


def build_table(frame: pd.DataFrame, weight_status: str, outcomes: list[str], row_specs: list[tuple[str, str, str]]) -> pd.DataFrame:
	rows: list[dict[str, str]] = []
	for spec_id, treatment, label in row_specs:
		row = {"treatment": label}
		for outcome in outcomes:
			row[outcome] = format_cell(select_row(frame, weight_status, spec_id, treatment, outcome))
		rows.append(row)
	return pd.DataFrame(rows)


def build_results_narrative(main_frames: dict[str, pd.DataFrame], component_frames: dict[str, pd.DataFrame]) -> list[str]:
	timing_authority = select_row(main_frames["track2_continuous"], "unweighted", "timing_dummy", "adolescent_exposure_flag", "authority_stance")
	timing_distrust = select_row(main_frames["plr_joint_shares"], "unweighted", "timing_dummy", "adolescent_exposure_flag", "share_joint_Distrust_discomposed")

	severity_authority_rows = [
		select_row(main_frames["track2_continuous"], weight_status, "joint_continuous", "severity_index_v2", "authority_stance")
		for weight_status in ["unweighted", "ipw", "rake"]
	]
	severity_distrust_rows = [
		select_row(main_frames["plr_joint_shares"], weight_status, "joint_continuous", "severity_index_v2", "share_joint_Distrust_discomposed")
		for weight_status in ["unweighted", "ipw", "rake"]
	]

	loyalty_authority_rows = [
		select_row(component_frames["track2_continuous_components"], weight_status, "severity_components", "loyalty_conflict_flag", "authority_stance")
		for weight_status in ["unweighted", "ipw", "rake"]
	]
	loyalty_distrust_rows = [
		select_row(component_frames["plr_joint_share_components"], weight_status, "severity_components", "loyalty_conflict_flag", "share_joint_Distrust_discomposed")
		for weight_status in ["unweighted", "ipw", "rake"]
	]

	component_bh_counts = {
		treatment: int(component_frames["track2_continuous_components"].loc[
			(component_frames["track2_continuous_components"]["treatment"] == treatment)
			& (component_frames["track2_continuous_components"]["p_value_adj_bh"] < 0.05)
		].shape[0])
		for treatment in [
			"family_separation_flag",
			"parental_arrest_flag",
			"loyalty_conflict_flag",
			"segregation_flag",
		]
	}

	severity_authority_text = ", ".join(
		f"{WEIGHT_TITLES[row['weight_status']]} {format_number(float(row['estimate']))} ({format_result_pair(row)})"
		for row in severity_authority_rows
	)
	severity_distrust_text = ", ".join(
		f"{WEIGHT_TITLES[row['weight_status']]} {format_number(float(row['estimate']))} ({format_result_pair(row)})"
		for row in severity_distrust_rows
	)
	loyalty_authority_text = ", ".join(
		f"{WEIGHT_TITLES[row['weight_status']]} {format_number(float(row['estimate']))} ({format_result_pair(row)})"
		for row in loyalty_authority_rows
	)
	loyalty_distrust_text = ", ".join(
		f"{WEIGHT_TITLES[row['weight_status']]} {format_number(float(row['estimate']))} ({format_result_pair(row)})"
		for row in loyalty_distrust_rows
	)

	return [
		f"Across the main treatment block, broad binary timing remains weak under BH correction. In the unweighted specification, `authority_stance <- adolescent_exposure_flag` is {format_number(float(timing_authority['estimate']))} ({format_result_pair(timing_authority)}), while `share_joint_Distrust_discomposed <- adolescent_exposure_flag` is {format_number(float(timing_distrust['estimate']))} ({format_result_pair(timing_distrust)}). These rows do not provide corrected evidence for a stable adolescent-dummy effect.",
		f"The corrected signal is more concentrated in aggregate severity than in timing or dosage. For `authority_stance <- severity_index_v2`, the three weighting schemes are {severity_authority_text}. For `share_joint_Distrust_discomposed <- severity_index_v2`, the corresponding rows are {severity_distrust_text}. This keeps the main causal readout centered on severity rather than on a broad timing contrast.",
		f"Within the severity decomposition, `loyalty_conflict_flag` remains the dominant component once q-values are reported explicitly. For `authority_stance <- loyalty_conflict_flag`, the rows are {loyalty_authority_text}. For `share_joint_Distrust_discomposed <- loyalty_conflict_flag`, the rows are {loyalty_distrust_text}. By comparison, the Track 2 BH-retained row counts are {component_bh_counts['family_separation_flag']} for `family_separation_flag`, {component_bh_counts['parental_arrest_flag']} for `parental_arrest_flag`, {component_bh_counts['loyalty_conflict_flag']} for `loyalty_conflict_flag`, and {component_bh_counts['segregation_flag']} for `segregation_flag`, which keeps the decomposition story centered on the loyalty-conflict channel.",
	]


def build_memo(main_frames: dict[str, pd.DataFrame], component_frames: dict[str, pd.DataFrame]) -> str:
	main_sample_n = int(main_frames["track2_continuous"].loc[main_frames["track2_continuous"]["weight_status"] == "unweighted", "sample_n"].iloc[0])
	weighted_sample_n = int(main_frames["track2_continuous"].loc[main_frames["track2_continuous"]["weight_status"] == "ipw", "sample_n"].iloc[0])
	results_narrative = build_results_narrative(main_frames, component_frames)

	lines = [
		f"# {MEMO_TITLE}",
		"",
		f"Date: {MEMO_DATE}",
		"",
		STATUS_LINE,
		"",
		"## 1. What this memo reports",
		"",
		"This document is now the single causal-results memo for the project. It consolidates the main-sample narrator-level DML results in one place. It contains three parts:",
		"",
		"- The main model setup and estimation conventions.",
		"- Eighteen full result tables: 3 weighting schemes x 3 outcome families x 2 result blocks.",
		"- A narrative interpretation that can be adapted directly into the paper's results section.",
		"",
		"This version updates the reporting layer so the memo now surfaces BH-adjusted q-values directly in the tables while retaining raw p-values for transparency.",
		"",
		"## 2. Sample and estimation setup",
		"",
		f"- Main sample: `N = {main_sample_n}`; weighted estimation sample `N = {weighted_sample_n}`.",
		"- Estimator: 5-fold cross-fitted DML / PLR.",
		"- Nuisance learner: LightGBM regressor.",
		"- Inference: `unweighted` uses OLS + HC3; `ipw` and `rake` use WLS + HC3.",
		"- Main covariate block: `birth_year`, `generation`, `gender`, `prewar_region`, `interview_year`, `age_at_interview`, `family_ses_prewar_v1_final_v1`, `education_prewar_v1_final_v1`, `english_ability_prewar_v1_final_v1`, and `cultural_orientation_prewar_v1_final_v1`.",
		"",
		"## 3. Models",
		"",
		"The timing dummy corresponds to the timing-only DML specification:",
		"",
		"$$",
		"Y_{io} = \\tau_D D_i + X_i^\\top \\beta + u_{io}",
		"$$",
		"",
		"where `D_i` is `adolescent_exposure_flag`.",
		"",
		"Timing-continuous / dosage / severity correspond to the joint continuous DML specification:",
		"",
		"$$",
		"Y_{io} = \\tau_A A_i + \\tau_T T_i + \\tau_S S_i + X_i^\\top \\beta + u_{io}",
		"$$",
		"",
		"where `A_i` is `age_at_first_exposure`, `T_i` is `total_days_incarcerated`, and `S_i` is `severity_index_v2`.",
		"",
		"The severity-decomposition specification is:",
		"",
		"$$",
		"Y_{io} = \\tau_A A_i + \\tau_T T_i + \\delta_1 F_i + \\delta_2 P_i + \\delta_3 L_i + \\delta_4 G_i + X_i^\\top \\beta + u_{io}",
		"$$",
		"",
		"where the four components are `family_separation_flag`, `parental_arrest_flag`, `loyalty_conflict_flag`, and `segregation_flag`.",
		"",
		"## 4. What `Rake` Means and How to Read the Tables",
		"",
		"`Rake` refers to a calibration / raking weight. It is not an inverse-probability weight derived from each individual's treatment probability. Instead, it uses iterative proportional fitting to align the sample with a target population on selected margins. Intuitively, `rake` is meant to make the weighted sample look more like the target population on demographic or design benchmarks, whereas `ipw` reweights by the probability of entering the sample or receiving a treatment state. Both are weighting conventions only; neither turns an association into causal identification on its own.",
		"",
		"The ILR tables require a different reading rule from the PLR joint-share tables. The six-part joint composition is ordered as `share_joint_Injury_composed`, `share_joint_Injury_discomposed`, `share_joint_Rupture_composed`, `share_joint_Rupture_discomposed`, `share_joint_Distrust_composed`, and `share_joint_Distrust_discomposed`. The five reported ILR coordinates are balances rather than category-specific effects:",
		"",
		"- `ilr_joint6_1`: Injury-composed versus Injury-discomposed.",
		"- `ilr_joint6_2`: the geometric mean of the first two Injury cells versus Rupture-composed.",
		"- `ilr_joint6_3`: the geometric mean of the first three cells versus Rupture-discomposed.",
		"- `ilr_joint6_4`: the geometric mean of the first four cells versus Distrust-composed.",
		"- `ilr_joint6_5`: the geometric mean of the first five cells versus Distrust-discomposed.",
		"",
		"A positive coefficient shifts the composition toward the numerator side of that balance; a negative coefficient shifts it toward the denominator side. ILR coefficients should therefore be read as composition-level movement and then checked against the PLR joint-share tables for category-specific interpretation.",
		"",
		"Table cells now use the format `beta + stars (s.e.); p=...; q=...`. The stars follow BH-adjusted q-values: `* q<0.05`, `** q<0.01`, `*** q<0.001`. Raw `p` values are retained for transparency, but corrected interpretation should follow `BH q`.",
		"",
		"## 5. Main treatment results",
		"",
	]

	for index, weight_status in enumerate(["unweighted", "ipw", "rake"], start=1):
		lines.extend([f"### 5.{index} {WEIGHT_TITLES[weight_status]}", ""])
		for family_key in ["ilr_joint6", "plr_joint_shares", "track2_continuous"]:
			lines.extend([f"#### {SECTION_TITLES[family_key]}", ""])
			lines.extend(
				markdown_table(
					build_table(
						main_frames[family_key],
						weight_status,
						MAIN_OUTCOMES[family_key],
						MAIN_ROW_SPECS,
					)
				)
			)
			lines.append("")

	lines.extend(["## 6. Severity component decomposition", ""])
	for index, weight_status in enumerate(["unweighted", "ipw", "rake"], start=1):
		lines.extend([f"### 6.{index} {WEIGHT_TITLES[weight_status]}", ""])
		for family_key, outcome_key in [
			("ilr_joint6_components", "ilr_joint6"),
			("plr_joint_share_components", "plr_joint_shares"),
			("track2_continuous_components", "track2_continuous"),
		]:
			lines.extend([f"#### {SECTION_TITLES[family_key]}", ""])
			lines.extend(
				markdown_table(
					build_table(
						component_frames[family_key],
						weight_status,
						MAIN_OUTCOMES[outcome_key],
						COMPONENT_ROW_SPECS,
					)
				)
			)
			lines.append("")

	lines.extend(["## 7. Narrative interpretation", ""])
	for paragraph in results_narrative:
		lines.extend([paragraph, ""])

	lines.extend([
		"## 8. Source files",
		"",
		f"- `{SOURCE_SCRIPT_DISPLAY}`",
		f"- `{MAIN_TREATMENT_SOURCES['ilr_joint6'].relative_to(ROOT).as_posix()}`",
		f"- `{MAIN_TREATMENT_SOURCES['plr_joint_shares'].relative_to(ROOT).as_posix()}`",
		f"- `{MAIN_TREATMENT_SOURCES['track2_continuous'].relative_to(ROOT).as_posix()}`",
		f"- `{COMPONENT_SOURCES['ilr_joint6_components'].relative_to(ROOT).as_posix()}`",
		f"- `{COMPONENT_SOURCES['plr_joint_share_components'].relative_to(ROOT).as_posix()}`",
		f"- `{COMPONENT_SOURCES['track2_continuous_components'].relative_to(ROOT).as_posix()}`",
	])
	return "\n".join(lines) + "\n"


def main() -> int:
	_ = parse_args()
	main_frames = load_sources(MAIN_TREATMENT_SOURCES)
	component_frames = load_sources(COMPONENT_SOURCES)
	MEMO_PATH.write_text(build_memo(main_frames, component_frames), encoding="utf-8")
	print(f"Saved memo -> {MEMO_PATH}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())