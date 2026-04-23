# Variable Dictionary v1

## Scope

This dictionary defines the first-pass analysis variables for oral history causal estimation.
Version: v1
Date: 2026-04-17

## Naming Convention

- Use snake_case.
- Use `_flag` suffix for binary indicators.
- Use `_score` for continuous scale outputs.
- Use `_v{N}` for versioned derived variables.

## 1) Keys and IDs

| variable | type | level | source | definition | allowed values |
|---|---|---|---|---|---|
| narrator_id | string | narrator | archive-intake | unique narrator identifier | non-empty string |
| interview_id | string | interview/segment | archive-intake | unique Densho interview identifier | non-empty string |
| segment_id | string | segment | data-cleaning-pipeline | unique segment identifier | non-empty string |
| spell_id | string | spell | timeline-builder | unique incarceration spell identifier | non-empty string |
| registry_id | string | narrator | narrator-linker | matched Names Registry identifier | nullable string |
| embedding_config_id | string | segment/narrator/run | embedding-scaler | versioned multimodal embedding configuration identifier | nullable string |

## 2) Treatment Variables

| variable | type | level | source | definition | allowed values |
|---|---|---|---|---|---|
| spell_sequence | int | spell | timeline-builder | within-narrator ordering of exposure spells | >= 1 |
| age_at_first_exposure | float | narrator | timeline-builder | age in years at first incarceration entry | >= 0 |
| adolescent_exposure_flag | int | narrator | timeline-builder | first exposure happened during adolescence | 0/1 |
| early_adolescence_flag | int | narrator | timeline-builder | first exposure in early adolescence | 0/1 |
| mid_adolescence_flag | int | narrator | timeline-builder | first exposure in middle adolescence | 0/1 |
| late_adolescence_flag | int | narrator | timeline-builder | first exposure in late adolescence | 0/1 |
| adult_exposure_flag | int | narrator | timeline-builder | first exposure at age >= 19 | 0/1 |
| timing_confidence | string | narrator | timeline-builder | confidence level for person-level timing variables | high / low / missing |
| total_days_incarcerated | int | narrator | timeline-builder | cumulative incarceration days across spells | >= 0 |
| days_in_assembly_center | int | narrator | timeline-builder | cumulative days in assembly centers | >= 0 |
| days_in_wra_camp | int | narrator | timeline-builder | cumulative days in WRA camps | >= 0 |
| days_in_segregation | int | narrator | timeline-builder | cumulative days in segregation settings | >= 0 |
| n_facilities | int | narrator | timeline-builder | distinct incarceration facilities count | >= 0 |
| family_separation_flag | int | narrator | timeline-builder | family separation occurred | 0/1 |
| loyalty_conflict_flag | int | narrator | timeline-builder | loyalty conflict signal present | 0/1 |
| segregation_flag | int | narrator | timeline-builder | ever assigned to segregation camp | 0/1 |
| parental_arrest_flag | int | narrator | timeline-builder | parent-level arrest/incarceration indicator | 0/1 |
| severity_index_v1 | int | narrator | timeline-builder | additive severity index | 0-4 |
| severity_index_v2 | float | narrator | timeline-builder | weighted/normalized severity index | 0-1 |
| source_priority | int | spell | timeline-builder | source hierarchy for exposure spell rows | 1=registry, 2=interview description, 3+=lower confidence |
| source_record_id | string | spell | timeline-builder | registry id or interview id used to derive the spell | nullable string |
| source_conflict_flag | int | spell | timeline-builder | source disagreement flag for spell construction | 0/1 |

## 2b) Outcome Variables (Active Multimodal Arm)

| variable | type | level | source | definition | allowed values |
|---|---|---|---|---|---|
| authority_stance | float | segment | GPT-5.4 text scorer | segment-level authority stance score on the protector-to-enemy axis | 0-1 |
| belonging_stance | float | segment | GPT-5.4 text scorer | segment-level belonging stance score on the retained-membership to alienation axis | 0-1 |
| composure_score | float | segment | GPT-5.4 text scorer | transcript-only How subscore; retains a historical name but is discomposure-oriented | 0-1 |
| how_text_discomposed | int | segment | GPT-5.4 text scorer / downstream aggregator | binary text-only provenance flag derived from `composure_score >= 0.50` | 0/1 |
| audio_discomposure_score | float | segment | frozen A/V scorer / downstream aggregator | threshold-centered audio discomposure score derived from `z_audio_composite` | 0-1 |
| video_discomposure_score | float | segment | frozen A/V scorer / downstream aggregator | threshold-centered video discomposure score derived from `z_video_composite` | 0-1 |
| how_av_score | float | segment | frozen A/V scorer / downstream aggregator | fused audio/video discomposure score: `max(audio_discomposure_score, video_discomposure_score)` | 0-1 |
| how_multimodal_score | float | segment/interview/narrator | multimodal downstream aggregator | active final How score: `max(composure_score, audio_discomposure_score, video_discomposure_score)` | 0-1 |
| how_discomposed | int | segment/interview/narrator | multimodal downstream aggregator | active final multimodal How flag: `how_multimodal_score >= 0.50` | 0/1 |
| region_6 | string | segment/interview/narrator | GPT-5.4 text scorer / downstream aggregator | six-region `what` map derived from authority and belonging scores | injury / injury_disrupted / adaptive_rupture / default_rupture / politicizing_rupture / distrust |
| outcome_3class | string | segment/interview/narrator | GPT-5.4 text scorer / downstream aggregator | merged three-class `what` outcome | Injury / Rupture / Distrust |
| n_discomposed | int | interview/narrator | multimodal downstream aggregator | count of scored segments with `how_discomposed = 1` | >= 0 |
| share_discomposed | float | interview/narrator | multimodal downstream aggregator | share of scored segments with `how_discomposed = 1` | 0-1 |
| share_composed | float | interview/narrator | multimodal downstream aggregator | share of scored segments with `how_discomposed = 0` | 0-1 |
| how_any_discomposed | int | interview/narrator | multimodal downstream aggregator | indicator that at least one scored segment is multimodally discomposed | 0/1 |
| n_discomposed_text | int | interview/narrator | GPT-5.4 text scorer / downstream aggregator | provenance count of scored segments with `how_text_discomposed = 1` | >= 0 |
| share_discomposed_text | float | interview/narrator | GPT-5.4 text scorer / downstream aggregator | provenance share of scored segments with `how_text_discomposed = 1` | 0-1 |
| share_composed_text | float | interview/narrator | GPT-5.4 text scorer / downstream aggregator | provenance share of scored segments with `how_text_discomposed = 0` | 0-1 |
| how_text_any_discomposed | int | interview/narrator | GPT-5.4 text scorer / downstream aggregator | provenance indicator that at least one scored segment crosses the text-only threshold | 0/1 |
| composure_score_mean | float | interview/narrator | GPT-5.4 text scorer / downstream aggregator | mean text-only How subscore across scored segments | 0-1 |
| how_multimodal_score_mean | float | interview/narrator | multimodal downstream aggregator | mean active multimodal How score across scored segments | 0-1 |

Interpretation note:

- In the active multimodal arm, `how_multimodal_score` is the paper's final continuous How outcome and `how_discomposed` is the paper's final binary How outcome.
- `composure_score` remains the transcript-only provenance subscore, with `how_text_discomposed = 1` iff `composure_score >= 0.50`.
- The active main-analysis A/V thresholds were refrozen on 2026-04-17 from the full archived z-composite marginals: `audio = 0.587275`, `video = 0.372174`.
- The archived calibration thresholds `audio = 0.3747` and `video = 0.2850` remain provenance-only baselines rather than the active downstream merge rule.
- The primary A/V threshold robustness pair is `audio = 0.490034`, `video = 0.533734`; it is used only for the archived-union-rate sensitivity check and does not alter the text threshold `0.50`.
- Do not compare the direction of `composure_score` directly to legacy share-composed or `how_composure_*` archive variables without reorientation.

## 3) Outcome Variables (Rubric Arm)

| variable | type | level | source | definition | allowed values |
|---|---|---|---|---|---|
| what_type_rubric | string | segment | rubric-coder / reasoned-rubric pass | segment-level substantive injury class from the rubric reasoning pass | authority_schema_injury / shame_mediated_identity_rupture / explicit_political_distrust |
| how_composure_rubric | string | segment | rubric-coder / reasoned-rubric pass | segment-level narrative composure label from the rubric reasoning pass | composed / discomposed |
| outcome_type_3x2_rubric | string | segment | rubric-coder / reasoned-rubric pass | six-cell 3x2 outcome label from rubric reasoning or coding | Guarded Vigilance / Diffuse Unease / Wounded Belonging / Stigmatized Discomposure / Oppositional Citizenship / Ambivalent Estrangement |
| justification_excerpt | string | segment | rubric-coder / reasoned-rubric pass | short excerpt supporting the rubric assignment | non-empty text when coded |
| coder_confidence | string | segment | rubric-coder / reasoned-rubric pass | rubric confidence label | high / medium / low |
| what_type_mode_rubric | string | narrator | rubric-coder / reasoned-rubric pass | narrator-level modal `what` class across candidate segments | 3-class controlled set |
| how_composure_mean_rubric | float | narrator | rubric-coder / reasoned-rubric pass | narrator-level share composed across coded candidate segments | 0-1 |
| dominant_type_3x2_rubric | string | narrator | rubric-coder / reasoned-rubric pass | dominant rubric 3x2 type at narrator level | six-type controlled set |
| rubric_confidence_mean | float | narrator | rubric-coder / reasoned-rubric pass | mean rubric confidence transformed to a numeric summary | 0-1 or documented run-specific scale |

Interpretation note:

- In v1, rubric labels are reasoning-backed categorical outcomes. They may enter downstream causal models before manual review; reviewed subsets form an audit and validation layer rather than the only admissible rubric sample.

## 4) Outcome Variables (Embedding Arm)

Current frozen operational definition:

- represent each segment or interview with a high-dimensional text/audio/video or multimodal vector
- compute cosine similarity against theory-defined `what` prototypes and `how` prototypes separately
- assign the nearest axis label on each dimension and combine them into the segment-level `outcome_type_3x2_embed`
- reserve direct six-type prototype scoring for later robustness checks rather than the current production rule

| variable | type | level | source | definition | allowed values |
|---|---|---|---|---|---|
| what_order_score_embed | float | segment | embedding-scaler | axis-level `what` score derived from cosine similarities between the observation embedding and the frozen `what` prototypes | numeric model output |
| how_composure_score_embed | float | segment | embedding-scaler | axis-level `how` score derived from cosine similarities between the observation embedding and the frozen `how` prototypes | numeric model output |
| what_type_embed | string | segment | embedding-scaler | nearest or highest-similarity 3-class `what` prototype assignment under the frozen rule | 3-class controlled set |
| how_type_embed | string | segment | embedding-scaler | nearest or highest-similarity 2-class `how` prototype assignment under the frozen rule | composed / discomposed |
| outcome_type_3x2_embed | string | segment | embedding-scaler | six-cell outcome label formed by combining the frozen `what_type_embed` and `how_type_embed` assignments; direct six-prototype comparison is reserved for robustness checks | six-type controlled set |
| type3x2_probability_vector_embed | string(JSON) | segment | embedding-scaler | six-cell probability vector induced by the frozen axis-level similarity probabilities | JSON array / object |
| what_order_mean_embed | float | narrator | embedding-scaler | narrator-level mean of the similarity-derived `what` score | numeric model output |
| how_composure_mean_embed | float | narrator | embedding-scaler | narrator-level mean of the similarity-derived `how` score | numeric model output |
| dominant_type_3x2_embed | string | narrator | embedding-scaler | dominant narrator-level 3x2 type after segment-level prototype assignment and aggregation | six-type controlled set |
| dominant_type_probability_embed | float | narrator | embedding-scaler | probability assigned to narrator-level dominant 3x2 type under the frozen prototype rule | 0-1 |
| n_multimodal_segments | int | narrator | embedding-scaler | count of narrator segments eligible for multimodal measurement | >= 0 |
| n_scored_segments_embed | int | narrator | embedding-scaler | count of narrator segments with completed embedding scores | >= 0 |
| multimodal_coverage | float | narrator | embedding-scaler | share of narrator segments with multimodal availability | 0-1 |
| measurement_status | string | narrator | embedding-scaler | narrator-level measurement pipeline status | unavailable / pending / scored / audited |

## 4b) Multimodal / Config Variables

| variable | type | level | source | definition | allowed values |
|---|---|---|---|---|---|
| has_audio | int | narrator/segment | archive-intake | audio modality available from the interview asset | 0/1 |
| has_video | int | narrator/segment | archive-intake | video modality available from the interview asset | 0/1 |
| multimodal_ready | int | narrator/segment | data-cleaning-pipeline | cleaned segment text plus linked interview audio and video are available for the configured multimodal pipeline | 0/1 |
| media_duration_seconds | int | narrator/segment | archive-intake | interview duration in seconds from archive metadata | >= 0 |
| primary_interview_id | string | narrator | archive-intake | primary interview chosen for narrator-level multimodal metadata linkage | nullable string |
| primary_interview_format | string | narrator | archive-intake | archive format code for primary interview | archive-controlled string |
| language_flag | string | segment | data-cleaning-pipeline | cleaned segment language flag | en / ja / mixed / unknown |
| char_count | int | segment | data-cleaning-pipeline | cleaned segment character count | >= 0 |

## 5) Covariates (Frozen Core + Pretreatment Recovery)

### 5a) Core narrator covariates

| variable | type | level | source | definition | allowed values |
|---|---|---|---|---|---|
| birth_year | int | narrator | archive-intake | narrator birth year | plausible historical range |
| generation | string | narrator | archive-intake | generation category | Issei / Nisei / Kibei / Sansei |
| gender | binary | narrator | archive-intake | gender category as recorded | male / female |
| prewar_state | string | narrator | archive-intake | prewar state | normalized state string |
| prewar_region | string | narrator | metadata-normalizer | prewar region bucket | west_coast / inland / hawaii / other (note: `other` is currently unused in the final main modeling sample) |
| interview_year | int | narrator | archive-intake | interview year | plausible range |
| age_at_interview | derived (int) | narrator | computed | interview_year − birth_year; not stored in CSV, computed at estimation time | plausible range |
| interview_length_words | int | narrator | data-cleaning-pipeline | transcript length in words; descriptive only, not used as covariate in DML | >= 0 |

### 5b) Recovered pre-treatment covariates (merged final analysis fields)

These fields are produced by the frozen Step 1 + Step 2 pipeline under `appendix/pretreatment_covariate_extraction_contract_v1.md`. They are narrator-level baseline controls and should be interpreted as the merged final values, not as raw Step 1 or raw Step 2 intermediate outputs.

| variable | type | level | source | definition | allowed values |
|---|---|---|---|---|---|
| family_ses_prewar_v1_final_v1 | string | narrator | pretreatment-covariate-recovery | merged final coarse family socioeconomic position before incarceration | farming_fishing / small_business / wage_labor_service / professional_white_collar / unknown |
| education_prewar_v1_final_v1 | string | narrator | pretreatment-covariate-recovery | merged final highest clearly supported prewar schooling level | primary_or_less / secondary / college_plus / schooling_unspecified / unknown |
| english_ability_prewar_v1_final_v1 | string | narrator | pretreatment-covariate-recovery | merged final prewar English ability or exposure category | japanese_only_or_none / limited_english / bilingual_or_functional / child_not_applicable / unknown |
| cultural_orientation_prewar_v1_final_v1 | string | narrator | pretreatment-covariate-recovery | merged final coarse prewar Japan-linkage orientation based on factual linkage signals rather than inferred psychology | japan_embedded / mixed_japan_us / us_embedded / unknown |
| born_in_japan_flag_prewar_v1_final_v1 | string | narrator | pretreatment-covariate-recovery | merged final factual flag for narrator born in Japan | 0 / 1 / missing when unresolved |
| time_in_japan_flag_prewar_v1_final_v1 | string | narrator | pretreatment-covariate-recovery | merged final factual flag for any supported prewar time spent in Japan | 0 / 1 / missing when unresolved |
| kibei_flag_prewar_v1_final_v1 | string | narrator | pretreatment-covariate-recovery | merged final factual flag for Kibei status or equivalent Japan-schooling return pattern | 0 / 1 / missing when unresolved |
| japanese_language_school_flag_prewar_v1_final_v1 | string | narrator | pretreatment-covariate-recovery | merged final factual flag for prewar Japanese language school attendance | 0 / 1 / missing when unresolved |

### 5c) Pretreatment recovery provenance and audit fields

| variable | type | level | source | definition | allowed values |
|---|---|---|---|---|---|
| step2_status_v1 | string | narrator | pretreatment-covariate-recovery | status of the Step 2 LLM extraction pass for that narrator row | ok / missing / parse_error:* / request_failed / no_choices |
| manual_review_recommended_flag_v1 | int | narrator | pretreatment-covariate-recovery | row-level flag indicating that Step 1 / Step 2 disagreement or ambiguity should be manually reviewed | 0/1 |
| family_ses_prewar_v1_final_source_v1 | string | narrator | pretreatment-covariate-recovery | source selected for the merged family SES final value | step1 / step2 / unknown |
| education_prewar_v1_final_source_v1 | string | narrator | pretreatment-covariate-recovery | source selected for the merged education final value | step1 / step2 / unknown |
| english_ability_prewar_v1_final_source_v1 | string | narrator | pretreatment-covariate-recovery | source selected for the merged English-ability final value | step1 / step2 / unknown |
| cultural_orientation_prewar_v1_final_source_v1 | string | narrator | pretreatment-covariate-recovery | source selected for the merged cultural-orientation final value | step1 / step2 / unknown |
| family_ses_prewar_v1_conflict_flag_v1 | int | narrator | pretreatment-covariate-recovery | disagreement between non-unknown Step 1 and Step 2 family SES values | 0/1 |
| education_prewar_v1_conflict_flag_v1 | int | narrator | pretreatment-covariate-recovery | disagreement between non-unknown Step 1 and Step 2 education values | 0/1 |
| english_ability_prewar_v1_conflict_flag_v1 | int | narrator | pretreatment-covariate-recovery | disagreement between non-unknown Step 1 and Step 2 English-ability values | 0/1 |
| cultural_orientation_prewar_v1_conflict_flag_v1 | int | narrator | pretreatment-covariate-recovery | disagreement between non-unknown Step 1 and Step 2 cultural-orientation values | 0/1 |
| english_generation_proxy_step1_v1 | string | narrator | pretreatment-covariate-recovery | Step 1 generation-based English proxy retained as recovery context only; not a final adjustment variable by itself | generation_proxy_issei / generation_proxy_kibei / generation_proxy_nisei / generation_proxy_sansei / empty |

## 6) Weighting Variables

| variable | type | level | source | definition |
|---|---|---|---|---|
| ipw_weight_v1 | float | narrator | weight-builder | inverse-probability weight for transport to WRA Names Registry population |
| rake_weight_v1 | float | narrator | weight-builder | raking weight calibrated to WRA marginals (birth year, sex, prewar region) |
| weight_eligible_flag | int | narrator | weight-builder | flag indicating whether narrator is eligible for weight estimation | 

## 7) Mandatory QA Checks

- Key uniqueness: `narrator_id`, `segment_id`, `spell_id` must be unique in their level tables.
- Binary validity: all `_flag` variables must be in {0,1}.
- Range validity: all axis scores must be in [1,5].
- Non-negativity: all day-count variables must be >= 0.
- Missingness report required for all treatment, outcome, and covariate variables.

## 8) Change Management

Any variable definition change requires:
1. codebook-governor change request
2. version bump (`v2`, `v3`, ...)
3. migration note listing impacted skills and output files
