# Descriptive Statistics (Treatment-Observed 688 Cases)

This file is regenerated from `data/processed/treatment_covariate_frame_v1.csv`, filtered to `treatment_observed_flag = 1`.

## Sample Overview
| Measure | n | Share |
| --- | --- | --- |
| Rows exported | 688 | 100.0% |
| Linked to registry | 307 | 44.6% |
| Plausibly incarcerated sample | 676 | 98.3% |
| Core covariates complete | 670 | 97.4% |
| Treatment observed | 688 | 100.0% |
| Weight eligible | 676 | 98.3% |
| Analysis ready | 670 | 97.4% |

## Variable Missingness
| Variable | Missing n | Missing share |
| --- | --- | --- |
| birth_year | 11 | 1.6% |
| generation | 5 | 0.7% |
| gender | 4 | 0.6% |
| prewar_state | 3 | 0.4% |
| interview_year | 2 | 0.3% |
| prewar_region | 3 | 0.4% |
| age_at_first_exposure | 11 | 1.6% |
| adolescent_exposure_flag | 11 | 1.6% |
| total_days_incarcerated | 0 | 0.0% |

## Generation Distribution
| Generation | n | Share |
| --- | --- | --- |
| Nisei | 580 | 84.3% |
| Sansei | 81 | 11.8% |
| Kibei | 13 | 1.9% |
| Issei | 9 | 1.3% |
| <MISSING> | 5 | 0.7% |

## Gender Distribution
| Gender | n | Share |
| --- | --- | --- |
| male | 361 | 52.5% |
| female | 323 | 46.9% |
| <MISSING> | 4 | 0.6% |

## Prewar Region Distribution
| Region | n | Share |
| --- | --- | --- |
| west_coast | 620 | 90.1% |
| inland | 51 | 7.4% |
| hawaii | 14 | 2.0% |
| <MISSING> | 3 | 0.4% |

## Timing Confidence
| Timing confidence | n | Share |
| --- | --- | --- |
| low | 688 | 100.0% |

## Numeric Summaries
| Variable | n | Missing | Mean | Median | P25 | P75 | Min | Max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| birth_year | 677 | 11 | 1926.20 | 1925 | 1921 | 1931 | 1901 | 1945 |
| interview_year | 686 | 2 | 2008.06 | 2009 | 2004 | 2012 | 1983 | 2024 |
| interview_count | 686 | 2 | 1.17 | 1 | 1 | 1 | 1 | 6 |
| interview_length_words | 686 | 2 | 534.33 | 193.50 | 138 | 887.75 | 34 | 5307 |
| age_at_first_exposure | 677 | 11 | 16.28 | 17.33 | 11.33 | 21.42 | 0.08 | 41.42 |
| total_days_incarcerated | 688 | 0 | 1596.10 | 1312 | 1275 | 1530 | 77 | 4611 |
| days_in_assembly_center | 688 | 0 | 82.68 | 77 | 0 | 137 | 0 | 382 |
| days_in_wra_camp | 688 | 0 | 1159.47 | 1175 | 1146 | 1269 | 0 | 2544 |
| days_in_segregation | 688 | 0 | 284.02 | 0 | 0 | 0 | 0 | 1393 |
| n_facilities | 688 | 0 | 1.86 | 2 | 1 | 2 | 1 | 5 |
| severity_index_v1 | 688 | 0 | 0.61 | 0 | 0 | 1 | 0 | 4 |
| severity_index_v2 | 688 | 0 | 0.15 | 0 | 0 | 0.25 | 0 | 1 |

## Treatment-Missing Reason Audit
| Reason | n | Share of full sample |
| --- | --- | --- |
| no_personal_incarceration_evidence_recovered | 0 | 0.0% |
| postwar_or_too_young_for_personal_incarceration | 0 | 0.0% |
| bio_evidence_non_japanese_ally_or_witness | 0 | 0.0% |
| bio_evidence_hawaii_military_family_nonincarceration | 0 | 0.0% |
| birth_year_missing_cannot_assess_personal_incarceration | 0 | 0.0% |
| bio_evidence_avoided_incarceration | 0 | 0.0% |
| bio_evidence_composite_couple_profile | 0 | 0.0% |
| bio_evidence_secondary_family_relation_nonpersonal | 0 | 0.0% |
| exposure_detected_but_timing_unresolved | 0 | 0.0% |

## Notes
- Source frame: `data\processed\treatment_covariate_frame_v1.csv`.
- Filter: `treatment_observed_flag = 1` (688 cases).
- Shares are computed against the filtered 688-case sample.
