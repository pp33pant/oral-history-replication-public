# names_registry_weight_plan_v1

## Goal
Build final transport weights in one pass from Names Registry (target population) to Densho oral-history sample (analytic sample), then write normalized weights back to `person_table`.

## Required Inputs
- `data/raw/manual_import/names_registry_v1.csv`
- `data/raw/manual_import/registry_matches_v1.csv`
- `data/oral_history.db` (`person_table` must be populated)

## One-Pass Commands
1. Download Names Registry CSV with authenticated session cookie:
   - Set `DENSHO_COOKIE`
   - Set `DENSHO_NAMES_CSV_URL` to the direct CSV download URL from the Names Registry page
   - Run: `python scripts/fetch_names_registry_csv_with_cookie.py`
2. Build final weights and write back to SQLite:
   - Run: `python scripts/build_final_weights_from_names_registry_v1.py`

## Output Artifacts
- `weights/target_population_frame_v1.csv`
- `weights/combined_weight_design_v1.csv`
- `weights/ipw_weights_v1.csv`
- `weights/raking_weights_v1.csv`
- `weights/weighting_report_v1.md`

## SQLite Columns Written
- `person_table.ipw_weight_v1`
- `person_table.rake_weight_v1`
- `person_table.registry_id_v1`
- `person_table.linked_to_registry`

## Balance Targets
- Max absolute SMD after weighting <= 0.10 on key weighting covariates
- Inspect ESS and weight concentration in `weighting_report_v1.md`
