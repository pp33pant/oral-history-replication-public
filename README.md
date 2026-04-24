# Oral History State Violence Public Release

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19716589.svg)](https://doi.org/10.5281/zenodo.19716589)

This public repository contains the shareable manuscript outputs and frozen replication archive for the study:

> **How Does State Violence Experienced During Adolescence Shape State-Person Narratives?**  
> *Multimodal Causal Evidence from Japanese American Oral Histories*

## What Is Included

- `paper/full_paper.pdf`: current compiled manuscript.
- `paper/appendix_tex.pdf`: standalone appendix.
- `replication_package/`: frozen replication interface with shareable processed inputs, model outputs, weighting tables, robustness summaries, appendix audit notes, and rerun scripts.
- `LICENSE`: repository license.

## Citation And DOI

- Zenodo concept DOI for the public release series: https://doi.org/10.5281/zenodo.19716589
- Latest GitHub release: https://github.com/pp33pant/oral-history-replication-public/releases/latest
- Full release history: https://github.com/pp33pant/oral-history-replication-public/releases
- For an exact frozen version, use the version-specific DOI shown on the matching Zenodo version page for the tagged release you use.

Use the concept DOI when you want a stable pointer that always resolves to the latest public release. Use the version-specific DOI attached to the tagged Zenodo record when you need to cite one exact archived release.

Stable release-series citation:

```text
Guanghui/Panda. (2026). pp33pant/oral-history-replication-public. Zenodo. https://doi.org/10.5281/zenodo.19716589
```

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
- The DOI-bearing archival snapshot is the Zenodo-backed GitHub release rather than the mutable default branch state.

## Contact

Questions about the released materials should first be checked against the appendix audit notes and codebook materials inside `replication_package/`. For further questions, contact `panguanghuipant@gmail.com`.