# weighting_spec_v1

## Target
- Target population: Japanese Americans in the adolescent-exposure cohorts (approx. birth years 1924-1935).
- Primary estimand remains archive-internal (unweighted); weights are for transport-oriented checks.

## Available Variables in the Frozen v1 Design
- `generation` (person_table)
- `gender` (person_table)
- `prewar_region_3cat` derived from `prewar_state` (west_coast / inland_or_other / hawaii)
- `birth_year` and `adolescent_cohort_1924_1935`
- `age_at_first_exposure`, `total_days_incarcerated`, `severity_index_v1`, `severity_index_v2`
- `linked_to_registry`, `registry_id_v1`, `ipw_weight_v1`, `rake_weight_v1`

## Variables Not Included in the Frozen v1 Design
- `age_at_incarceration_quintile` was not needed for the frozen balance diagnostics
- `total_days_incarcerated_quintile` was not needed for the frozen balance diagnostics

## Artifacts Produced
- `weights/sample_weight_frame_v1.csv`
- `weights/target_population_frame_v1.template.csv`
- `weights/weighting_data_readiness_v1.md`
- `weights/target_population_frame_v1.csv`
- `weights/combined_weight_design_v1.csv`
- `weights/ipw_weights_v1.csv`
- `weights/raking_weights_v1.csv`