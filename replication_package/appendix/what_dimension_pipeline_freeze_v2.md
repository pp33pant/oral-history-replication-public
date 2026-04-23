# What+How(multimodal) Dimension Pipeline Freeze v2

**Freeze date**: 2026-04-09 (model upgraded 2026-04-11; boundary revision v2 2026-04-14; multimodal How activation 2026-04-17; A/V threshold refreeze 2026-04-17)  
**Supersedes**: Embed-cosine prototype pipeline (archived to `appendix/archived_embed_v1/`)
**Boundary change log**: v2 boundaries (2026-04-14) revised x1 high cut 0.65→0.54, x2 cut 0.45→0.43, and merge map. See `outcome_typology.md` §2.4 for rationale.

## Production Configuration

| Parameter | Value |
|-----------|-------|
| Model | `gpt-5.4` (via OpenAI Chat Completions API; Batch API or Flex processing recommended for 50% cost savings) |
| Prompt version | `v1` (`SYSTEM_PROMPT_V1` in `scripts/run_outcome_llm_fulltext_2d_v1.py`) |
| Temperature | 0.0 |
| Max tokens | 120 (`max_completion_tokens` for gpt-5.x) |
| Input | Full transcript text per segment (fetched from Densho HTML) |
| Text scorer output | JSON: `{"authority_stance": float, "belonging_stance": float, "composure_score": float, "confidence": float}` |
| A/V companion input | `data/processed/how_av_scores_v1/how_av_scores.csv` (frozen z-composite archive consumed downstream) |
| Main A/V thresholds | full-corpus marginal `Q0.80`: audio `0.587275`, video `0.372174` |
| A/V robustness thresholds | union-target pair: audio `0.490034`, video `0.533734` |
| Final How fusion | `how_multimodal_score = max(text, audio, video)` over available modality scores |

## Continuous Output Space

The classifier returns three continuous scores per segment:

- `authority_stance ∈ [0, 1]` — degree of rights-based institutional framing
- `belonging_stance ∈ [0, 1]` — degree of communal/relational framing
- `composure_score ∈ [0, 1]` — text-side How subscore, with `0.0 = fully composed` and `1.0 = fully discomposed`
- `how_multimodal_score ∈ [0, 1]` — active final How score after threshold-centered audio/video fusion
- `confidence ∈ [0, 1]` — model confidence scalar

## 6-Region Boundary Map

Boundary cuts applied to the 2D continuous space:

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| `x1_low` (authority low) | 0.50 | Theoretical midpoint of protector–enemy scale |
| `x1_high` (authority high) | **0.54** | Natural density break (−65% drop at 0.54 in x1 histogram) |
| `x2_cut` (belonging) | **0.43** | Balanced 6-region cells; lower edge of x2 density plateau |

> **Archived v1 values**: x1_high=0.65, x2_cut=0.45

The six regions:

| Region | Authority range | Belonging range | Interpretation |
|--------|----------------|-----------------|----------------|
| `injury` | < 0.50 | < 0.43 | Low on both axes — raw injury without framing |
| `injury_disrupted` | < 0.50 | ≥ 0.43 | Low authority but belonging present — communal injury |
| `adaptive_rupture` | [0.50, 0.54) | < 0.43 | Moderate authority, low belonging — adaptive break |
| `default_rupture` | [0.50, 0.54) | ≥ 0.43 | Moderate authority + belonging — default interpretive break |
| `politicizing_rupture` | ≥ 0.54 | < 0.43 | Strong authority, low belonging — political framing |
| `distrust` | ≥ 0.54 | ≥ 0.43 | High on both axes — structured institutional critique |

## 3-Class Merge

The active v2 reclassification base is the chi-1-corrected canonical production cohort, not the earlier broader model-specific segment source. Superseded wrong-base v2 outputs and legacy model-specific v1 outputs are archived under `data/processed/archive_baselines_v1/what_how_text_phase1/2026-04-17_canonical_realignment_v1/`.

| Production class | Merged from | Share (v2, N=642 canonical narrators) |
|-----------------|-------------|----------------------|
| **Injury** | `injury` + `injury_disrupted` | 36.8% |
| **Rupture** | `adaptive_rupture` + `default_rupture` | 50.6% |
| **Distrust** | `politicizing_rupture` + `distrust` | 12.6% |

> **Archived v1 merge**: Injury ← injury+injury_disrupted+adaptive_rupture (78.8%); Rupture ← default_rupture (19.5%); Distrust ← politicizing_rupture+distrust (1.7%)

## Column Naming Convention

### Production columns (active multimodal contract)

| Column | Type | Description |
|--------|------|-------------|
| `authority_stance` | float [0,1] | Raw authority stance score |
| `belonging_stance` | float [0,1] | Raw belonging stance score |
| `confidence` | float [0,1] | Model confidence scalar |
| `composure_score` | float [0,1] | Text-side How subscore; higher values mean more discomposed narration |
| `how_text_discomposed` | int 0/1 | Text-only provenance flag derived from `composure_score >= 0.5` |
| `audio_discomposure_score` | float [0,1] | Threshold-centered audio discomposure score derived from `z_audio_composite` |
| `video_discomposure_score` | float [0,1] | Threshold-centered video discomposure score derived from `z_video_composite` |
| `how_av_score` | float [0,1] | A/V discomposure score (`max(audio, video)`) |
| `how_multimodal_score` | float [0,1] | Active final How score (`max(text, audio, video)`) |
| `how_discomposed` | int 0/1 | Active final multimodal How flag: `how_multimodal_score >= 0.5` |
| `n_discomposed` | int | Interview/narrator count of segments with `how_discomposed = 1` |
| `share_discomposed` | float [0,1] | Interview/narrator share of segments with `how_discomposed = 1` |
| `share_composed` | float [0,1] | Interview/narrator share of segments with `how_discomposed = 0` |
| `how_any_discomposed` | int 0/1 | Interview/narrator indicator that at least one segment is multimodally discomposed |
| `region_6` | str | 6-region label |
| `outcome_3class` | str | 3-class merged label (Injury/Rupture/Distrust) |

### Archived legacy columns (`*_embed`, `*_rubric`)

| Column | Type | Status |
|--------|------|--------|
| `what_type_embed` | str | Robustness audit only — not production |
| `how_type_embed` | str | Robustness audit only — not production |
| `outcome_type_3x2_embed` | str | Robustness audit only — not production |
| `what_type_rubric` | str | Historical annotation only — not part of the active production contract |
| `how_composure_rubric` | str | Historical annotation only — not part of the active production contract |

## How Dimension

The active How contract is multimodal.

- **Text-side subscore**: `composure_score` from `SYSTEM_PROMPT_V1`, with `0.0 = fully composed`, `1.0 = fully discomposed`, and threshold `0.5 -> how_text_discomposed`.
- **Audio branch**: use `z_audio_composite` from `how_av_scores.csv`, center the active main-analysis threshold `0.587275`, and map to `[0,1]` with the standard normal CDF.
- **Video branch**: use `z_video_composite` from `how_av_scores.csv`, center the active main-analysis threshold `0.372174`, and map to `[0,1]` with the standard normal CDF.
- **A/V score**: `how_av_score = max(audio_discomposure_score, video_discomposure_score)`.
- **Final active score**: `how_multimodal_score = max(composure_score, audio_discomposure_score, video_discomposure_score)`.
- **Final active binary**: `how_discomposed = 1` iff `how_multimodal_score >= 0.5`; equivalently, if any of the text/audio/video modality branches crosses its frozen threshold.
- **Naming note**: the variable name `composure_score` is retained for the text-side subscore only; it is no longer the paper's final How measure.

## A/V Threshold Governance

The current main-analysis thresholds are derived downstream from the frozen z-composite archive rather than by rerunning the archived feature generator.

- **Main analysis**: keep the text threshold fixed at `0.50` and refreeze the audio/video branches at the full-corpus marginal `Q0.80` of their archived z-composite distributions.
- **Current main thresholds**: `audio = 0.587275`, `video = 0.372174`.
- **Current main marginal rates**: audio `20.0%`, video `19.5%`; the resulting A/V OR-rate on the full corpus is `34.72%`.
- **Archived calibration baseline**: the earlier calibration thresholds `0.3747` / `0.2850` are provenance-only baselines and no longer define the active downstream merge.
- **Primary robustness check**: retain the text threshold at `0.50` and instead retune only the A/V thresholds by full-corpus grid search to recover the archived A/V union rate target `0.323`.
- **Current robustness pair**: `audio = 0.490034`, `video = 0.533734`, yielding full-corpus A/V marginal rates `24.00%` and `12.19%` with union `32.28%`.
- **Interpretation rule**: text is not quantile-calibrated. The `0.50` text cutoff remains the semantic midpoint of the LLM discomposure scale in both the main analysis and the robustness specification.

## Two-Track Estimation Architecture

```
Track 1: narrator-level what-by-how six-cell shares derived from active multimodal outputs
Track 2: continuous SUR / ILR-DML from active multimodal outputs (authority, belonging, multimodal How)
```

## Full-Scale Execution Parameters

| Parameter | Value |
|-----------|-------|
| Target population | 688 narrators with `treatment_observed_flag = 1` |
| Total segments | ~15,269 |
| Total interviews | ~900+ |
| Estimated API cost | ~$43 |
| Estimated VM cost | ~$5 |
| Script | `scripts/run_outcome_llm_fulltext_2d_v1.py` |
| VM orchestrator | `scripts/azure/run_video_first_target_corpus_pipeline_v1.sh` (updated) |

## Zero-Share Replacement

For ILR/ALR log-ratio transforms on share vectors:
- ε = 1 / (2 × n_segments) per interview
- Applied before log-ratio to avoid log(0)

## Selection History

Originally chosen from 2x2 factorial experiment: {gpt-4o-mini, gpt-4o} x {v1, v2_forced}. Upgraded to gpt-5.4 after WS-3 model comparison (2026-04-11).

| Config | Injury% | Rupture% | Distrust% | Decision |
|--------|---------|----------|-----------|----------|
| mini_v1 | 16 | 69 | 15 | Over-concentrates in rupture |
| mini_v2_forced | 15 | 75 | 10 | Worse — forced prompt backfires |
| **4o_v1** | **23** | **56** | **21** | **Selected — best spread** |
| 4o_v2_forced | 17 | 66 | 17 | Forced prompt narrows spread |
