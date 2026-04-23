# How-Dimension MNAR Sensitivity Report (v1)

## Delta-Adjusted Sensitivity

Outcome column: how_multimodal_score_mean

Interpretation: δ = 0 means unobservable narrators have the same mean how-score
as observable narrators. δ = 1 SD means they are shifted 1 standard deviation
toward greater discomposure in the current score orientation. Higher δ
represents stronger MNAR selection.

| δ (SD) | Imputed How (unobs) | ATE how | N obs | N imputed |
|--------|---------------------|---------|-------|-----------|
| 0.0 | 0.4765 | -0.0201 | 430 | 212 |
| 0.2 | 0.5023 | -0.0201 | 430 | 212 |
| 0.5 | 0.5411 | -0.0201 | 430 | 212 |
| 0.8 | 0.5799 | -0.0202 | 430 | 212 |
| 1.0 | 0.6057 | -0.0202 | 430 | 212 |
| 1.5 | 0.6704 | -0.0203 | 430 | 212 |

## Lee Bounds (Partial Identification)

- Lower bound: -0.030028
- Upper bound: -0.030028
- Trim fraction: 0.0013
- Trimmed group: treated

## Verdict

If the main ATE estimate remains inside the Lee bounds and the delta-adjusted
estimate stays stable up to δ ≈ 0.5 SD, the how-dimension result is moderately
robust. If estimates reverse sign by δ = 0.5, the how-dimension finding is fragile.