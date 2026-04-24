# Oral History State Violence Public Release

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19716589.svg)](https://doi.org/10.5281/zenodo.19716589)

This repository is the public release surface for the study:

> **How Does State Violence Experienced During Adolescence Shape State-Person Narratives?**  
> *Multimodal Causal Evidence from Japanese American Oral Histories*

It is designed to let an external reader do three things quickly:

1. read the paper and appendix;
2. inspect the released replication package;
3. understand how an agent-assisted workflow was used to structure cleaning, documentation, and release audit.

## Start Here

| If you want to... | Go to... | What you will find |
|---|---|---|
| Read the manuscript | `paper/full_paper.pdf` | Current public paper PDF |
| Read the appendix | `paper/appendix_tex.pdf` | Standalone appendix PDF |
| Reproduce released results | `replication_package/README.md` | Public rerun instructions, scripts, and released processed inputs |
| Understand the workflow architecture | `skills/SKILLS_INDEX.md` | Public-facing index of the cleaned agent-assisted workflow surface |

## What This Public Repo Contains

- `paper/`: reader-facing manuscript outputs.
- `replication_package/`: frozen public replication interface with shareable processed inputs, model outputs, weighting tables, robustness summaries, appendix audit notes, and rerun scripts.
- `skills/`: a selective public documentation layer showing how workflow skills fit into project management, deterministic cleaning, and provenance / audit writing.
- `LICENSE`: repository license.

## Why The `skills/` Folder Is Public

This public repo does not only release files. It also shows part of the workflow logic that produced those files.

The `skills/` folder is a cleaned publication layer that explains:

- what different workflow skills were responsible for in the research system;
- what remained under direct human researcher / orchestrator control;
- what structured outputs made the workflow reproducible and auditable.

It is intentionally selective. The public repo exposes workflow roles and audit logic, not the full private operational stack.

## Human Researcher / Orchestrator Role

The workflow in this project is agent-assisted, not researcher-replaced.

The human researcher remained responsible for:

- defining the research question, scope conditions, and admissible claims;
- deciding which steps could be automated and which required manual adjudication;
- freezing versions, release boundaries, and publication-ready outputs;
- approving what could be made public and what had to remain excluded;
- interpreting robustness, narrowing claims where necessary, and writing the final paper-facing conclusions.

## Citation And DOI

- Zenodo concept DOI for the public release series: https://doi.org/10.5281/zenodo.19716589
- Latest GitHub release: https://github.com/pp33pant/oral-history-replication-public/releases/latest
- Full release history: https://github.com/pp33pant/oral-history-replication-public/releases
- For an exact frozen version, use the version-specific DOI shown on the matching Zenodo version page for the tagged release you use.

Use the concept DOI when you want a stable pointer that resolves to the latest public release. Use the version-specific DOI attached to the matching Zenodo record when you need to cite one exact archived release.

Stable release-series citation:

```text
Pan, Guanghui. (2026). pp33pant/oral-history-replication-public. Zenodo. https://doi.org/10.5281/zenodo.19716589
```

## Data Sharing Boundary

This public release is intentionally narrower than the private working repository.

- Included: processed research variables, public metadata, frozen numeric outputs, codebook materials, robustness documentation, workflow-facing release notes, and replication scripts.
- Excluded: direct transcript payloads, raw archive-intake files, cookie-based/manual download artifacts, transcript-bearing review packages, and private orchestration assets tightly bound to restricted workflow surfaces.

If you need transcript text, obtain it from Densho under Densho's public-access terms and then rebuild that layer from the documented pipeline.

## Reproduction Interface

The main public rerun surface is `replication_package/README.md`.

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

- This repository is a public showcase and release surface, not the full development workspace.
- The replication package is the canonical audit trail for the released processed results.
- The `skills/` folder is a selective publication of cleaned workflow documentation, not a dump of the private internal skill library.
- The DOI-bearing archival snapshot is the Zenodo-backed GitHub release rather than the mutable default branch state.

## Contact

Questions about the released materials should first be checked against the appendix audit notes and codebook materials inside `replication_package/`. For further questions, contact `panguanghuipant@gmail.com`.