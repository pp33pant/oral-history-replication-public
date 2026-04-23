# How-Dimension Negative Controls Report (v1)

## Purpose

Three negative-control tests check whether how-composure is driven by
genuine trauma-related narratability or by technical artefacts.

## Results Summary

### treatment_to_noise

| Predictor | Outcome | coef | SE | t | p | N |
|-----------|---------|------|----|---|---|---|
| adolescent_exposure_flag | gap_rate | -0.02833 | 0.011616 | -2.4389 | 0.015006 | 637 |
| adolescent_exposure_flag | mean_seg_wordcount | -408.287175 | 338.610723 | -1.2058 | 0.228355 | 637 |
| total_days_incarcerated | gap_rate | -1e-05 | 9e-06 | -1.0922 | 0.275162 | 642 |
| total_days_incarcerated | mean_seg_wordcount | -0.757543 | 0.260287 | -2.9104 | 0.003735 | 642 |

### nontrauma_discomposure

| Predictor | Outcome | coef | SE | t | p | N |
|-----------|---------|------|----|---|---|---|
| segment_type (trauma vs casual) | how_multimodal_score | -0.008144 | nan | -2.4398 | 0.014723 | 11791 |

### fe_absorption_base

| Predictor | Outcome | coef | SE | t | p | N |
|-----------|---------|------|----|---|---|---|
| adolescent_exposure_flag | how_multimodal_score (no FE) | -0.012459 | 0.011675 | -1.0671 | 0.286337 | 637 |

### fe_absorption_interview_id

| Predictor | Outcome | coef | SE | t | p | N |
|-----------|---------|------|----|---|---|---|
| adolescent_exposure_flag (residualized on interview_id) | how_multimodal_score (residualized on interview_id) | -0.018341 | 0.006018 | -3.0479 | 0.0024 | 637 |

## Interpretation

- **Test 1 (treatment → noise)**: if treatment significantly predicts technical
  noise indicators, the how measurement may conflate technical quality with composure.
  Ideal result: no significant association.

- **Test 2 (non-trauma discomposure)**: if discomposure is similar in trauma and
  non-trauma segments, it may reflect general verbal style rather than trauma-specific
  narratability difficulty. Ideal result: significant difference (higher discomposure
  in trauma segments).

- **Test 3 (FE absorption)**: if adding interviewer or collection FE fully absorbs
  the treatment→how coefficient, measured discomposure may be interviewer-driven.
  Ideal result: coefficient remains stable after FE residualization.