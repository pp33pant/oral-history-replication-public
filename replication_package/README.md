# Replication Package

This directory is the frozen replication interface for the manuscript. It packages the shareable processed inputs, codebook materials, model outputs, robustness summaries, and wrapper scripts needed to reproduce the paper-facing tables from the released research frame.

## Archive And Citation

- Public repository: https://github.com/pp33pant/oral-history-replication-public
- Zenodo record: https://zenodo.org/records/19716590
- Version DOI for this frozen public release (`v1.0.0`): https://doi.org/10.5281/zenodo.19716590
- Concept DOI for the release series: https://doi.org/10.5281/zenodo.19716589

Use the version DOI when citing the exact archived public release. Use the concept DOI when citing the evolving public release series.

## Contents

- `codebook/`: schema, measurement, and coding references.
- `data/processed/`: shareable processed inputs used by the released estimation scripts.
- `models/`: frozen causal estimate tables and readout memo.
- `weights/`: weighting tables and balance diagnostics.
- `robustness/`: frozen robustness summaries and supporting tables.
- `appendix/`: release-facing appendix notes, including the data-sharing audit and data-availability statement.
- `source_scripts/`: versioned source scripts copied from the repository snapshot.
- `scripts/`: one-command wrappers for the packaged reruns and archive checks.

## Software Requirements

- Python 3.12
- Packages pinned in `requirements.txt`

Install with:

```bash
pip install -r requirements.txt
```

## Data Access Boundary

This package redistributes processed research variables and public metadata only. It does not redistribute direct transcript payloads. If you need transcript text, obtain it from Densho and rebuild that layer separately using the documented pipeline.

## Reproduction Steps

Run the scripts from inside `replication_package/`.

1. `python scripts/01_causal_models.py`
   Re-runs the main Track 1 per-cell, Track 1 ILR, and Track 2 causal models using the packaged model matrix.

2. `python scripts/02_severity_components.py`
   Re-runs the severity-component decomposition models.

3. `python scripts/03_robustness.py --full`
   Re-runs the paper-facing robustness battery, excluding the appendix-how raw-source rerun that depends on governed archive-intake assets outside this package.

4. `python scripts/04_causal_readout.py`
   Rebuilds the causal readout memo from the packaged estimate tables.

5. `python scripts/05_replication_checks.py`
   Verifies the package inventory and refreshes `replication_check_log_v1.md`.

## Expected Runtime

- Main causal models: several minutes on a modern laptop.
- Severity-component models: several minutes on a modern laptop.
- Full paper-facing robustness rerun: materially longer than the main models.
- Inventory and checksum checks: under one minute.

## Package Policy

- The package is designed to reproduce the released paper-facing results from the frozen processed frame.
- Direct transcript text is intentionally excluded and should be accessed from Densho.
- The difficult-cases panel remains part of the released appendix evidence, but transcript-bearing review payloads are not redistributed here.

## Contact

Questions about the package should be resolved by consulting the appendix documents and the codebook materials first; those files are the canonical audit trail for the released archive. Any further questions contact panguanghuipant@gmail.com. 