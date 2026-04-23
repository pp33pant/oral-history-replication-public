# Causal Model Spec v1

## Inputs
- Full outcome-defined matrix: `data/processed/modeling_inputs_v1/narrator_model_matrix_v1.csv`
- Main modeling matrix: `data/processed/modeling_inputs_v1/narrator_model_matrix_main_v1.csv`
- Recovered complete-case matrix: `data/processed/modeling_inputs_v1/narrator_model_matrix_complete_case_v1.csv`
- Protected manifest: `data/processed/protected_causal_inputs_v1/what_how_text_phase1_canonical_realignment_2026-04-17/protection_manifest_v1.json`

## Sample Counts
- Outcome-defined rows: 642
- Main rows: 633
- Recovered complete-case rows: 564
- Weighted-ready main rows: 632

## Primary Treatments
- age_at_first_exposure
- total_days_incarcerated
- severity_index_v2

## Secondary Timing / Robustness Terms
- adolescent_exposure_flag
- severity_index_v1
- adolescent_x_dosage_v1
- adolescent_x_severity_v1
- adolescent_x_interview_year_centered_v1

## Primary Covariate Block
- birth_year
- generation
- gender
- prewar_region
- interview_year
- age_at_interview
- family_ses_prewar_v1_final_v1
- education_prewar_v1_final_v1
- english_ability_prewar_v1_final_v1
- cultural_orientation_prewar_v1_final_v1

## Auxiliary Factual Flags
- born_in_japan_flag_prewar_v1_final_v1
- time_in_japan_flag_prewar_v1_final_v1
- kibei_flag_prewar_v1_final_v1
- japanese_language_school_flag_prewar_v1_final_v1

## Output Roots
- `models/causal_estimates_v1/track1_ilr_v1/`
- `models/causal_estimates_v1/track1_per_cell_v1/`
- `models/causal_estimates_v1/track2_v1/`
- `models/causal_estimates_v1/measurement_sensitivity_v1.csv`

## Outcome Families
- Track 1 ILR on six-cell and three-class share outcomes
- Track 1 per-cell share PLR estimates
- Track 2 continuous authority/belonging/multimodal How estimates

## Dependency Snapshot
- doubleml: available
- sklearn: available
- lightgbm: available
- statsmodels: available
