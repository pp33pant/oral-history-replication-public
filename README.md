# Oral History State Violence Public Release

This public repository contains the shareable manuscript outputs and frozen replication archive for the study:

> **How Does State Violence Experienced During Adolescence Shape State-Person Narratives?**  
> *Multimodal Causal Evidence from Japanese American Oral Histories*

## What Is Included

- `paper/full_paper.pdf`: current compiled manuscript.
- `paper/appendix_tex.pdf`: standalone appendix.
- `replication_package/`: frozen replication interface with shareable processed inputs, model outputs, weighting tables, robustness summaries, appendix audit notes, and rerun scripts.
- `LICENSE`: repository license.

## Data Sharing Boundary

This public release is intentionally narrower than the private working repository.

- Included: processed research variables, public metadata, frozen numeric outputs, codebook materials, robustness documentation, and replication scripts.
- Excluded: direct transcript payloads, raw archive-intake files, cookie-based/manual download artifacts, and transcript-bearing review packages.

If you need transcript text, obtain it from Densho under Densho's public-access terms and then rebuild that layer from the documented pipeline.

## How To Use This Repository

The main reproduction interface is `replication_package/README.md`.

Typical workflow:

```bash
cd replication_package
pip install -r requirements.txt
python scripts/01_causal_models.py
python scripts/02_severity_components.py
python scripts/03_robustness.py --full
python scripts/04_causal_readout.py
python scripts/05_replication_checks.py
```

## Notes

- The public repo is a release surface, not the full development workspace.
- The replication package is the canonical audit trail for released processed results.
- The paper and appendix PDFs are included for direct reading without entering the rerun workflow.

## Contact

Questions about the released materials should first be checked against the appendix audit notes and codebook materials inside `replication_package/`. For further questions, contact `panguanghuipant@gmail.com`.