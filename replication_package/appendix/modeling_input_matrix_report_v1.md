# Modeling Input Matrix Report v1

## Outputs
- Full merged matrix: `data\processed\modeling_inputs_v1\narrator_model_matrix_v1.csv`
- Main sample matrix: `data\processed\modeling_inputs_v1\narrator_model_matrix_main_v1.csv`
- Recovered complete-case matrix: `data\processed\modeling_inputs_v1\narrator_model_matrix_complete_case_v1.csv`
- Analysis-ready missing-outcome audit: `data\processed\modeling_inputs_v1\analysis_ready_missing_outcome_audit_v1.csv`

## Row Counts
- Outcome-defined merged rows: 642
- Main modeling rows (`analysis_ready_treatment_covariate_flag = 1`): 633
- Recovered complete-case rows: 564
- Analysis-ready rows missing canonical v2 outcomes: 37
- Treatment-observed rows missing canonical v2 outcomes: 46

## Weight Audit
- `ipw_weight_v1` vs `weight_ipw_norm_v1` mismatches: 0
- `rake_weight_v1` vs `weight_rake_norm_v1` mismatches: 0
- Transport-weight-ready rows inside main sample: 632

## Included Treatment Variables
- age_at_first_exposure
- adolescent_exposure_flag
- total_days_incarcerated
- severity_index_v1
- severity_index_v2
- family_separation_flag
- loyalty_conflict_flag
- segregation_flag
- parental_arrest_flag

## Included Core Covariates
- birth_year
- generation
- gender
- prewar_region
- interview_year
- derived age_at_interview

## Included Recovered Covariates
- family_ses_prewar_v1_final_v1
- education_prewar_v1_final_v1
- english_ability_prewar_v1_final_v1
- cultural_orientation_prewar_v1_final_v1
- born_in_japan_flag_prewar_v1_final_v1
- time_in_japan_flag_prewar_v1_final_v1
- kibei_flag_prewar_v1_final_v1
- japanese_language_school_flag_prewar_v1_final_v1

## Included Outcome Families
- Track 1 six-cell what-by-how shares (`share_joint_*`)
- Track 1 class and region shares (`share_class_*`, `share_region_*`)
- Track 2 continuous outcomes (`authority_stance`, `belonging_stance`, `how_multimodal_score_mean`)

## Sample Rule
- Base table is outcome-defined on canonical narrator-level v2 rows.
- Primary modeling sample is the subset with `analysis_ready_treatment_covariate_flag = 1`.
- Recovered complete-case robustness additionally requires no `unknown` in the four main recovered categorical covariates.
