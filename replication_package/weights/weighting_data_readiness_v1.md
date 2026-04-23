# weighting_data_readiness_v1

## Summary
- Sample frame rows exported: 1011
- Narrators linked to registry: 391
- Narrators with observed treatment timing/dosage: 753
- Narrators with non-null `ipw_weight_v1` and `rake_weight_v1`: 889
- Final transport-weight artifacts are present for the plausibly incarcerated sample; this file now summarizes coverage rather than a blocked scaffold state.

## Current Availability
- Sample-side covariates exported from `person_table`
- `registry_matches_v1.csv` present: yes
- exposure-derived treatment variables present in `person_table`: yes
- final transport weights present: yes
- `facility_spells_v1.csv` present: no; the frozen release relies on the exposure-history engineering outputs instead of a separate facility-spells export

## Sample Missingness Snapshot
- missing `birth_year`: 65
- missing `generation`: 142
- missing `gender`: 54
- unknown `prewar_region_3cat`: 94
- missing `interview_year`: 8

## Archived Design Notes
1. Remaining core-covariate missingness is documented in this snapshot rather than reopened inside the frozen release.
2. The frozen estimand remains the plausibly incarcerated sample used by the released weighting artifacts.
3. The exported treatment/covariate frame and weight artifacts remain the authoritative basis for any post-release balance or positivity audit.