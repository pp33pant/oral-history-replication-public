# Data Archival And Causal Input Protection Plan v1

## Status

This memo defines the **local-only** data archival and protection policy for the current GPT-5.4 text-phase outputs.

- It is intentionally **not** a Git LFS plan.
- It assumes large local CSV artifacts remain on the workstation or VM-return workspace.
- It separates mutable execution roots from frozen causal-analysis inputs.

## Three-Tier Layout

### 1. Active execution root

`data/processed/video_first_post_vm_batch1_v2/`

Purpose:

- working root for machine-generated What + How(text phase 1) outputs
- generic filenames used by some legacy or downstream scripts
- can still be overwritten by future reruns unless explicitly protected

Current causal-analysis-relevant files:

- `segment_llm_fulltext_2d_outcomes_v1.csv`
- `interview_llm_fulltext_2d_outcomes_v1.csv`
- `narrator_llm_fulltext_2d_outcomes_v1.csv`

Canonicalization note (2026-04-17):

- the generic `*_v1.csv` files are the only canonical production inputs for downstream reclassification and causal work
- the canonical generic segment file is defined by the intersection of the canonical interview and canonical narrator production tables, not by the broader model-specific segment source
- model-specific `*_gpt-5.4_v1.csv` files are transitional execution artifacts and must be archived once the generic canonical files are materialized
- archived chi-1 rerun repair artifacts and superseded wrong-base v2 outputs now live under `data/processed/archive_baselines_v1/what_how_text_phase1/2026-04-17_canonical_realignment_v1/`

### 2. Local archive / baseline root

`data/processed/archive_baselines_v1/what_how_text_phase1/`

Purpose:

- remove old model outputs and stale checkpoints from the active root
- keep `gpt-4o`, `gpt-4o-mini`, `gpt-5.4-mini`, and `gpt-5.4-nano` comparison artifacts available for provenance
- keep old runtime checkpoints available without letting them masquerade as current production inputs

Rule:

- no retired baseline file should remain in `video_first_post_vm_batch1_v2/` once it has been superseded locally
- wrong-base or model-specific files that are replaced by canonical generic production files must be copied or moved into a dated archive subfolder with a lineage note before any overwrite

### 3. Protected causal-input snapshot root

`data/processed/protected_causal_inputs_v1/what_how_text_phase1/`

Purpose:

- hold a frozen local snapshot of the exact text-phase outputs that will feed the next causal-analysis cycle
- carry SHA-256 hashes, byte sizes, and source-path provenance in a machine-readable manifest
- keep snapshot files read-only to prevent accidental overwrite

Rule:

- once a causal-analysis cycle starts, downstream modeling should read from this protected snapshot, not from the mutable execution root

## Operational Policy

### Freeze step

Run:

`python scripts/protect_causal_inputs_v1.py snapshot`

This operation:

- copies the three active generic GPT-5.4 text-phase outputs into the protected snapshot root
- writes `protection_manifest_v1.json` and `protection_manifest_v1.md`
- marks both the protected copies and the active generic source files as read-only

### Verify step

Run:

`python scripts/protect_causal_inputs_v1.py verify`

This operation:

- re-hashes the protected snapshot files
- checks manifest consistency
- checks that the protected copies remain read-only
- checks that the active generic source files are still read-only and still match the protected snapshot hashes

## What Is Protected Now

This v1 protection layer is for the text-phase outputs already needed for upcoming causal analysis:

- segment-level GPT-5.4 What + How(text) outputs
- interview-level GPT-5.4 aggregates
- narrator-level GPT-5.4 aggregates

The large runtime checkpoint is not the primary causal-analysis input and is therefore not duplicated into the protected snapshot by default.

## Regeneration Rule

If text-phase outputs must be regenerated later:

1. do **not** overwrite the protected snapshot in place;
2. intentionally unprotect or replace the active root only after a documented rerun decision;
3. create a new protected snapshot generation rather than silently mutating `v1`.

## Why This Plan Avoids Version Errors

- current memos can describe one active root, one archive root, and one protected causal-input root without ambiguity
- current scripts can keep execution defaults while causal-analysis workflows point to a frozen local snapshot
- skills used for causal analysis can require the protection manifest before modeling begins
- no large binary/CSV promotion into Git or Git LFS is required