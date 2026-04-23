# Replication Check Log v1

Generated: 2026-04-23 23:13:46 UTC

## Required Inventory

- README.md: present
- requirements.txt: present
- scripts/01_causal_models.py: present
- scripts/02_severity_components.py: present
- scripts/03_robustness.py: present
- scripts/04_causal_readout.py: present
- scripts/05_replication_checks.py: present
- source_scripts/_causal_modeling_runtime_v1.py: present
- source_scripts/dml_estimation_track1_per_cell.py: present
- data/processed/modeling_inputs_v1/narrator_model_matrix_main_v1.csv: present
- data/processed/video_first_post_vm_batch1_v2/narrator_llm_fulltext_2d_outcomes_v2.csv: present
- models/causal_estimates_v1/track1_per_cell_v1/track1_per_cell_estimates_v1.csv: present
- models/causal_estimates_v1/track2_v1/track2_estimates_v1.csv: present
- models/causal_estimates_v1/causal_estimates_readout_memo_v2.md: present
- weights/combined_weight_design_v1.csv: present
- robustness/causal_robustness_v1/robustness_summary_v1.md: present
- appendix/data_sharing_audit_v1.md: present
- appendix/data_availability_statement_v1.md: present
- appendix/replication_archive_manifest.md: present

## Exclusion Checks

- data/processed/transcripts: not present
- data/processed/video_first_post_vm_batch1_v2/segment_llm_fulltext_2d_outcomes_v2.csv: not present

## Hash Inventory

- data/processed/modeling_inputs_v1/narrator_model_matrix_main_v1.csv: `eb03b77a99033648704937bea9c3f0e1346c9ff5c3f50112b35ee3bef58fd293`
- data/processed/video_first_post_vm_batch1_v2/narrator_llm_fulltext_2d_outcomes_v2.csv: `e7cb850e5ebf0d031237d322a2b0a89c01fa5c3b2a5caa93f9f6f21160ecd6d9`
- models/causal_estimates_v1/track1_per_cell_v1/track1_per_cell_estimates_v1.csv: `7999d0070be5262495882d2a256be4e27d73c10e21179442fd8a22102448bc10`
- models/causal_estimates_v1/track2_v1/track2_estimates_v1.csv: `0cfce0486751e3ea77e37b33e3fd4da14e02f8f6dccec1c2c7fbfe2c208c5e79`
- weights/combined_weight_design_v1.csv: `48782eb4b0e20bab88d27229c313b013732cedb6e0a8b685c8a8d8220a3e7029`
- robustness/causal_robustness_v1/robustness_summary_v1.md: `1bf0e50470e7af9a1f5349bae90ef956ceb57a9afcc7f0aaf1dbc59665d18d98`

## Verdict

- required inventory missing: 0
- forbidden payloads present: 0
- overall verdict: pass
