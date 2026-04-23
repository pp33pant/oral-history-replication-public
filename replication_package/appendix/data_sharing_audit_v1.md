# Data Sharing Audit v1

## Purpose

This audit records which artifacts are distributed in the replication package and which artifacts are excluded from redistribution. The governing rule is simple: the package includes public metadata and derived research variables needed to reproduce the paper-facing tables, while excluding direct transcript payloads and other governed source materials that should be accessed from Densho rather than republished here.

## Included in the Replication Package

| Category | Included artifacts | Reason for inclusion |
| --- | --- | --- |
| Codebook | variable dictionary, cleaning rules, outcome typology, scoring and weighting notes | These documents define the measurement contract and analysis schema. |
| Processed data | narrator-level model matrices, narrator/interview-level outcome aggregates, treatment and weighting frames, boundary-sensitivity grid, how observability and MNAR summary tables | These files are sufficient to reproduce the paper-facing causal and appendix-side summary results without redistributing transcript text. |
| Model outputs | frozen causal estimate tables, readout memo, robustness summaries, weighting tables | These are the direct numerical artifacts reported in the manuscript and appendix. |
| Appendix documents | robustness appendix, measurement freeze note, descriptive and weighting reports, data-availability statement | These provide the provenance and interpretive audit trail for the released artifacts. |
| Replication scripts | package wrapper scripts plus the versioned source scripts they call | These scripts provide one-command reruns for the released processed inputs. |

## Excluded from the Replication Package

| Category | Excluded artifacts | Reason for exclusion |
| --- | --- | --- |
| Direct transcript payloads | files containing `full_text`, transcript dumps, and transcript-segment exports | Transcript text should be obtained from Densho under its public-access terms rather than redistributed here. |
| Raw harvest payloads | cookie-based download artifacts, manual raw pulls, and other intake-stage source payloads | These are governed source materials and are not needed to reproduce the frozen paper tables from the released processed inputs. |
| Review-package transcript extracts | difficult-cases packages that embed transcript snippets or transcript segment exports | The paper keeps the difficult-cases panel as a frozen appendix device, but the direct transcript payloads remain outside the shareable archive. |
| Transient execution state | VM checkpoints, temporary manifests, and intermediate operational caches | These are operational artifacts rather than part of the frozen replication interface. |

## Package Boundary Decision

- Public narrator metadata and derived numeric research variables are included.
- Transcript text and other direct source payloads are excluded.
- The package therefore supports reproduction of the paper's frozen estimation layer while directing users back to Densho for direct source-text access.

## Included Processed Inputs

- `data/processed/modeling_inputs_v1/`
- `data/processed/video_first_post_vm_batch1_v2/` narrator- and interview-level aggregate outputs only
- `data/processed/treatment_covariate_frame_v1.csv`
- `data/processed/treatment_missing_audit_v1.csv`
- `data/processed/how_selection_audit_v1.csv`
- `data/processed/how_observability_model_v1.csv`
- `data/processed/how_mnar_sensitivity_v1.csv`
- `data/processed/how_lee_bounds_v1.csv`
- `data/processed/how_difficult_cases_panel_v1.csv`

## Exclusion Flags Enforced in the Package Copy

- No `segment_llm_fulltext_*` files are copied into the package.
- No `transcripts/` directory is copied into the package.
- No `transcript_segments.txt` files are copied into the package.

## Audit Verdict

The released package is a shareable processed-results archive rather than a raw-source mirror. That boundary preserves the paper's reproducibility for the frozen estimation layer while respecting Densho-based access governance for direct transcript materials.