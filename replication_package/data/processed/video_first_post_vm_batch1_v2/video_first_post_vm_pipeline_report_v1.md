# Video-First Post-VM Pipeline Report v1

## Inputs
- data/processed/vm_returns_batch1

## Discovery
- packages discovered: 37
- packages loaded: 37
- packages empty or skipped at load: 0

## Scoring
- classifier mode: axiswise
- unique text models: sentence-transformers/all-mpnet-base-v2
- scored segment rows: 492
- skipped rows after validation or scoring: 0

## Aggregation
- interview-level packages materialized: 37
- narrator-level rollups materialized: 31

## Outcome Distribution
- Guarded Vigilance: 25
- Diffuse Unease: 0
- Wounded Belonging: 368
- Stigmatized Discomposure: 69
- Oppositional Citizenship: 30
- Ambivalent Estrangement: 0

## Outputs
- segment scores: data/processed/video_first_post_vm_batch1_v2/multimodal_segment_scores_v1.csv
- interview shares: data/processed/video_first_post_vm_batch1_v2/interview_outcome_share_vectors_v1.csv
- narrator rollups: data/processed/video_first_post_vm_batch1_v2/narrator_outcome_rollups_v1.csv
- package inventory: data/processed/video_first_post_vm_batch1_v2/source_package_inventory_v1.csv
- skipped rows: data/processed/video_first_post_vm_batch1_v2/skipped_rows_v1.csv
- interview packages root: data/processed/video_first_post_vm_batch1_v2/interviews

## SQLite Load
- SQLite load was skipped for this run.
