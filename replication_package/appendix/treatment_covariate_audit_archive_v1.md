# treatment_covariate_audit_archive_v1

## Scope
- audit target: narrator-level treatment and core covariate construction after the latest deterministic cleanup pass
- unit of audit: `data/processed/treatment_covariate_frame_v1.csv`
- excluded from this archive: downstream outcome coding and embedding work

## Archived Cleaning Steps
1. Rebuilt staged person metadata from the current manual-import files and cached narrator pages.
2. Applied conservative backfill for `birth_year`, `generation`, `gender`, `prewar_state`, and `interview_year` only when stronger source evidence existed and staged values were blank or implausible.
3. Added context-aware treatment-universe filtering so nonpersonal facility mentions, spouse-only composite profiles, and clear ally/witness biographies do not count as narrator-level incarceration exposure.
4. Validated registry links before using them for treatment scaffolds or weights; implausible narrator-registry matches are now rejected upstream of weighting.
5. Refreshed facility-window timing, including explicit Crystal City, Honouliuli, and Tashme handling, then reran person-level timing and duration engineering.
6. Re-exported the treatment/covariate frame, row-level treatment-missing audit, descriptive statistics, and Names Registry weights from the cleaned staging tables.

## Audited Outcome Snapshot
- exported narrator rows: 1011
- linked to registry: 307
- plausibly incarcerated sample: 805
- core covariates complete: 854
- treatment observed: 688
- weight eligible: 805
- analysis ready: 670

## Treatment-Missing Audit
- rows with treatment_observed_flag = 0: 323
- structural or conservative non-treatment categories dominate the missing-treatment set:
  - no_personal_incarceration_evidence_recovered: 128
  - postwar_or_too_young_for_personal_incarceration: 83
  - bio_evidence_non_japanese_ally_or_witness: 65
  - bio_evidence_hawaii_military_family_nonincarceration: 18
  - birth_year_missing_cannot_assess_personal_incarceration: 15
  - bio_evidence_avoided_incarceration: 6
  - bio_evidence_composite_couple_profile: 6
  - bio_evidence_secondary_family_relation_nonpersonal: 1
  - exposure_detected_but_timing_unresolved: 1

## Residual Treatment-Observed Tail
- treatment_observed_flag = 1 but core_covariate_complete_flag != 1: 18
- These are no longer broad cleaning failures; they are narrow metadata tail cases.
- Under the current cleaning rule, all 18 are retained as missing rather than imputed, because deterministic source recovery is exhausted and ad hoc fill-in would introduce more bias than leaving the fields missing.

| narrator_id | name_full | missing fields |
| --- | --- | --- |
| 157 | Grace Kubota Ybarra | birth_year; prewar_state |
| 697 | Amy Tsugawa | birth_year |
| 705 | Mika Hiuga | birth_year |
| 714 | Chico Uyeda | birth_year |
| 716 | Gus J. Solomon | generation; gender |
| 724 | Chizuko Iyama | birth_year |
| 737 | Mary Takayanagi | birth_year |
| 752 | George H. Morishita | birth_year |
| 805 | Ann Fujikawa | birth_year |
| 838 | Hana Shepard | birth_year |
| 839 | Mae Matsuzaki | birth_year |
| 885 | Lillian Horita | interview_year |
| 927 | Jimmy Naganuma | generation; gender |
| 928 | George Kazuharu Naganuma | generation; gender; prewar_state |
| 929 | Kazumu Naganuma | generation; gender; prewar_state |
| 1064 | Lily M. Inazu | birth_year |
| 1083 | Ron Kenmotsu | generation |
| 1086 | Patricia Kiwa Koyamatsu | interview_year |

## Timing And Facility Edge Cases
- recoverable timing-only case still open: narrator 223 (`Henry Shimizu`), where `hastings_park` remains an unresolved facility window and therefore treatment timing is still not observed
- unresolved facility windows remaining in the facility catalog: `ellis_island`, `hastings_park`, `mcneil_island`, `missoula`
- facility-window coverage after the latest pass: 26 ready, 4 unresolved
- Under the current cleaning rule, this timing case is also retained as missing rather than imputed from an undated facility reference.

## Weighting Audit
- weighting sample rows: 805
- matched sample rows: 307
- match rate: 0.3814
- max absolute SMD before weighting: 0.7233
- max absolute SMD after IPW: 0.1639
- max absolute SMD after raking: 0.1352

## Release Decision
- The deterministic, low-risk cleanup path is exhausted for this version.
- Current treatment and covariate files are fit for downstream causal work when the documented sample gates are respected.
- The 18 residual treatment-observed rows and the single unresolved timing case are recorded as missing by design; no statistical or hand-tuned imputation is applied in v1.
- Further reduction of the residual tail should be handled through manual archival lookup or a curated overrides file rather than new heuristic backfills.

## Authoritative Files
- frame export: `data/processed/treatment_covariate_frame_v1.csv`
- treatment-missing rows: `data/processed/treatment_missing_audit_v1.csv`
- descriptive snapshot: `appendix/descriptive_stats.md`
- cleaning report: `appendix/treatment_covariate_cleaning_report_v1.md`
- treatment-missing report: `appendix/treatment_missing_audit_report_v1.md`
- treatment engineering report: `appendix/treatment_engineering_report_v1.md`
- facility window report: `appendix/facility_windows_report_v1.md`
- weighting report: `weights/weighting_report_v1.md`
- change log: `codebook/change_requests_v1.md`