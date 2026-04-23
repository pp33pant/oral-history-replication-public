# Cleaning Rules v1

## Scope

Deterministic first-pass rules for transcript, metadata, and variable cleaning.
Version: v1
Date: 2026-04-03

## Rule Set A: Text and Segment Cleaning

1. Encoding normalization
- Input text must be normalized to UTF-8.
- Replace malformed unicode characters with explicit replacement token and log count.

2. Whitespace normalization
- Collapse repeated spaces to single space.
- Normalize line breaks to `\n`.
- Trim leading/trailing whitespace.

3. Speaker filtering
- Keep narrator speech for analysis outputs.
- Preserve interviewer turns in raw archive only.

4. Segment boundaries
- Prefer existing topic-tag boundaries.
- Fallback: deterministic paragraph split.
- Reject segments with `< 30` words unless manually whitelisted.

5. Segment quality flags
- `segment_empty_flag`, `segment_short_flag`, `segment_malformed_flag`, `segment_low_confidence_flag`.

## Rule Set B: Metadata Normalization

1. Key mapping
- Map all raw keys to canonical dictionary keys.
- Unmapped keys must be listed in `metadata_unmapped_keys_v1.csv`.

2. Category normalization
- Normalize generation labels into {Issei, Nisei, Kibei, Sansei}.
- Normalize region into {west_coast, inland, hawaii, other}.

3. Date parsing
- Parse date fields to ISO `YYYY-MM-DD` when available.
- If partial date, store best available precision and set confidence flag.

4. ID hygiene
- Strip whitespace around IDs.
- Enforce lowercase for machine IDs where applicable.

## Rule Set C: Treatment Variable Cleaning

1. Logical consistency
- `adolescent_exposure_flag` and `adult_exposure_flag` cannot both be 1.
- `age_at_first_exposure >= 0`.

2. Day counts
- All `days_*` variables must be non-negative.
- `total_days_incarcerated >= max(days_in_assembly_center, days_in_wra_camp, days_in_segregation)`.

3. Severity indices
- `severity_index_v1` in [0,4].
- `severity_index_v2` in [0,1].

4. Conflict tracking
- If date/source conflict exists, set conflict flag and preserve both source values in audit file.

## Rule Set D: Outcome Variable Cleaning

1. Controlled label checks
- `what_type_rubric` and `what_type_embed` must come from the 3-class controlled set only.
- `how_composure_rubric` and `how_type_embed` must come from the 2-class composure set only.
- `outcome_type_3x2_rubric` and `outcome_type_3x2_embed` must come from the six-type controlled set only.

2. Continuous score checks
- `what_order_score_embed` and `how_composure_score_embed` must be finite numeric values.
- If a run applies score normalization, the normalization rule and valid range must be logged with the model version.

3. Cross-field consistency
- Each `outcome_type_3x2_*` label must match the observed combination of its underlying `what` and `how` labels.

4. Confidence handling
- Low-confidence reasoned-rubric rows must be preserved and routed to audit workflow, not dropped.

5. Aggregation rules
- Narrator-level aggregates require at least one valid segment-level code or score.
- `what_type_mode_rubric` uses plurality; ties must be logged as tie cases.
- `how_composure_mean_rubric` is interpreted as the share of composed coded segments.
- Do not compare legacy share-composed or `how_composure_*` quantities directionally to the active GPT text `composure_score` without reorientation; the active text score uses `0 = composed`, `1 = discomposed`.
- Dominant 3x2 types use plurality; ties must be logged as tie cases.

## Rule Set E: Missingness and Outlier Policy

1. Missingness thresholds
- Critical variable missingness > 10% triggers review.
- Critical = treatment core + outcome core + key covariates.

2. Outlier handling
- Do not winsorize silently.
- Outlier treatment must be explicit and versioned in robustness specs.

3. Exclusion policy
- Any row exclusion requires `exclusion_reason_code` and source skill stamp.

## Output Contracts

Required outputs per cleaning run:
- `data/processed/segments_clean_v1.json`
- `data/processed/metadata_normalized_v1.csv`
- `data/processed/variable_cleaning_log_v1.csv`
- `appendix/variable_cleaning_report_v1.md`

## Rollback Trigger

Rollback this run if any condition occurs:
- duplicate key rate > 0
- critical variable range violations > 1%
- silent column drop detected
- unresolved parser errors > 5% of records
