# Pretreatment Covariate Descriptive Distribution v1

This note summarizes the completed pretreatment covariate recovery outputs pulled back from `oral-history-vm` after the full realtime Step 2 run finished successfully.

## Source Artifacts

- `data/processed/pretreatment_covariates_v1/pretreatment_covariate_step2_results_gpt-5.4_realtime_v1.csv`
- `data/processed/pretreatment_covariates_v1/pretreatment_covariate_final_frame_v1.csv`
- `appendix/pretreatment_covariate_extraction_report_v1.md`

## Cohort Coverage

- final frame rows: 1011
- treatment-observed rows: 688
- Step 2 status counts in final frame: `ok = 688`, `missing = 323`
- manual review recommended within treatment-observed cohort: `627 / 688` (91.1%)

## Final Covariate Distributions: Treatment-Observed Cohort

### `family_ses_prewar_v1_final_v1`

- `small_business`: 265 (38.5%)
- `farming_fishing`: 258 (37.5%)
- `professional_white_collar`: 60 (8.7%)
- `unknown`: 53 (7.7%)
- `wage_labor_service`: 52 (7.6%)
- source counts: `step2 = 624`, `step1 = 11`, `unknown = 53`
- conflict count: 188

### `education_prewar_v1_final_v1`

- `secondary`: 316 (45.9%)
- `primary_or_less`: 176 (25.6%)
- `schooling_unspecified`: 92 (13.4%)
- `college_plus`: 69 (10.0%)
- `unknown`: 35 (5.1%)
- source counts: `step2 = 635`, `step1 = 18`, `unknown = 35`
- conflict count: 258

### `english_ability_prewar_v1_final_v1`

- `bilingual_or_functional`: 469 (68.2%)
- `child_not_applicable`: 160 (23.3%)
- `limited_english`: 29 (4.2%)
- `unknown`: 24 (3.5%)
- `japanese_only_or_none`: 6 (0.9%)
- source counts: `step2 = 660`, `step1 = 4`, `unknown = 24`
- conflict count: 48

### `cultural_orientation_prewar_v1_final_v1`

- `mixed_japan_us`: 509 (74.0%)
- `us_embedded`: 163 (23.7%)
- `japan_embedded`: 15 (2.2%)
- `unknown`: 1 (0.1%)
- source counts: `step2 = 621`, `step1 = 66`, `unknown = 1`
- conflict count: 296

## Final Covariate Distributions: All Rows

### `family_ses_prewar_v1_final_v1`

- `farming_fishing`: 322 (31.8%)
- `small_business`: 320 (31.7%)
- `unknown`: 233 (23.0%)
- `professional_white_collar`: 78 (7.7%)
- `wage_labor_service`: 58 (5.7%)

### `education_prewar_v1_final_v1`

- `secondary`: 366 (36.2%)
- `primary_or_less`: 190 (18.8%)
- `schooling_unspecified`: 178 (17.6%)
- `unknown`: 145 (14.3%)
- `college_plus`: 132 (13.1%)

### `english_ability_prewar_v1_final_v1`

- `bilingual_or_functional`: 536 (53.0%)
- `unknown`: 267 (26.4%)
- `child_not_applicable`: 160 (15.8%)
- `limited_english`: 29 (2.9%)
- `japanese_only_or_none`: 19 (1.9%)

### `cultural_orientation_prewar_v1_final_v1`

- `mixed_japan_us`: 550 (54.4%)
- `us_embedded`: 407 (40.3%)
- `japan_embedded`: 37 (3.7%)
- `unknown`: 17 (1.7%)

## Auxiliary Flags: Treatment-Observed Cohort

- `born_in_japan_flag_prewar_v1_final_v1`: `1 = 18` (2.6%), `0 = 670` (97.4%)
- `time_in_japan_flag_prewar_v1_final_v1`: `1 = 347` (50.4%), `0 = 341` (49.6%)
- `kibei_flag_prewar_v1_final_v1`: `1 = 31` (4.5%), `0 = 657` (95.5%)
- `japanese_language_school_flag_prewar_v1_final_v1`: `1 = 254` (36.9%), `0 = 434` (63.1%)

## Short Readout

- The full realtime Step 2 run completed locally recoverable outputs for all 688 treatment-observed narrators with `status = ok` for every row.
- The treatment-observed cohort is dominated by `small_business` and `farming_fishing` family SES, `secondary` and `primary_or_less` schooling, `bilingual_or_functional` English ability, and `mixed_japan_us` cultural orientation.
- Unknown rates are now modest within the treatment-observed cohort for the four recovered covariates: 7.7%, 5.1%, 3.5%, and 0.1%, respectively.
- Conflict rates remain substantial for several fields, especially cultural orientation and education, so downstream causal work should continue to retain the manual-review and conflict indicators as provenance-sensitive diagnostics rather than silently discarding them.