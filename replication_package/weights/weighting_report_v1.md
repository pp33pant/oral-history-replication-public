# weighting_report_v1

## Design
- Target frame: Names Registry (WRA/FAR) rows standardized to common weighting covariates.
- Sample frame: Densho oral-history narrators from person_table.
- Linkage: narrator_id -> registry_id from `registry_matches_v1.csv`.
- Explicit postwar births (`birth_year > 1945`), narrator IDs flagged with `prebirth_exposure_excluded_v1`, and narrator IDs with conservative bio-based non-personal-incarceration evidence are excluded from the weighting sample.

## Coverage
- target rows: 108991
- sample rows: 805
- matched sample rows: 307
- match rate: 0.3814

## Weight Families
- `ipw_weight_v1`: overlap-aware post-stratified inverse-probability style weight with trimming and normalization.
- `rake_weight_v1`: iterative proportional fitting to target margins (birth cohort, sex, prewar region).

## Balance Diagnostics (max absolute SMD)
- pre-weight: 0.7233
- post-IPW: 0.1639
- post-raking: 0.1352

## Outputs
- weights/target_population_frame_v1.csv
- weights/combined_weight_design_v1.csv
- weights/ipw_weights_v1.csv
- weights/raking_weights_v1.csv
- weights/weighting_report_v1.md

## Person Table Migration
- Added/updated columns: `ipw_weight_v1`, `rake_weight_v1`, `registry_id_v1`, `linked_to_registry`
- Migration id: `weights_from_names_registry_v1`
