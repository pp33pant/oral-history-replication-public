# Causal Estimates Readout Memo v1

Date: 2026-04-19

Status: Frozen baseline retained for archive; the release-facing memo is `causal_estimates_readout_memo_v2.md`.

## 1. What this memo reports

This document is now the single causal-results memo for the project. It consolidates the main-sample narrator-level DML results in one place. It contains three parts:

- The main model setup and estimation conventions.
- Eighteen full result tables: 3 weighting schemes x 3 outcome families x 2 result blocks.
- A narrative interpretation that can be adapted directly into the paper's results section.

This version makes three explicit adjustments:

- ILR results report only `ilr_joint6_1` through `ilr_joint6_5`; the what-3 ILR dimensions are no longer reported here.
- Statistical significance is marked with stars using raw p-values: `* p<0.05`, `** p<0.01`, `*** p<0.001`; BH-adjusted `q` values are handled in the v2 working memo for multiple-testing-aware interpretation.
- The memo now clarifies what `rake` means and how it differs from `ipw`.

## 2. Sample and estimation setup

- Main sample: `N = 633`; weighted estimation sample `N = 632`.
- Estimator: 5-fold cross-fitted DML / PLR.
- Nuisance learner: LightGBM regressor.
- Inference: `unweighted` uses OLS + HC3; `ipw` and `rake` use WLS + HC3.
- Main covariate block: `birth_year`, `generation`, `gender`, `prewar_region`, `interview_year`, `age_at_interview`, `family_ses_prewar_v1_final_v1`, `education_prewar_v1_final_v1`, `english_ability_prewar_v1_final_v1`, and `cultural_orientation_prewar_v1_final_v1`.

## 3. Models

The timing dummy corresponds to the timing-only DML specification:

$$
Y_{io} = \tau_D D_i + X_i^\top \beta + u_{io}
$$

where $D_i$ is `adolescent_exposure_flag`.

Timing-continuous / dosage / severity correspond to the joint continuous DML specification:

$$
Y_{io} = \tau_A A_i + \tau_T T_i + \tau_S S_i + X_i^\top \beta + u_{io}
$$

where $A_i$ is `age_at_first_exposure`, $T_i$ is `total_days_incarcerated`, and $S_i$ is `severity_index_v2`.

The severity-decomposition specification is:

$$
Y_{io} = \tau_A A_i + \tau_T T_i + \delta_1 F_i + \delta_2 P_i + \delta_3 L_i + \delta_4 G_i + X_i^\top \beta + u_{io}
$$

where the four components are `family_separation_flag`, `parental_arrest_flag`, `loyalty_conflict_flag`, and `segregation_flag`.

## 4. What `Rake` Means and How to Read the Tables

`Rake` refers to a calibration / raking weight. It is not an inverse-probability weight derived from each individual's treatment probability. Instead, it uses iterative proportional fitting to align the sample with a target population on selected margins. Intuitively, `rake` is meant to make the weighted sample look more like the target population on demographic or design benchmarks, whereas `ipw` reweights by the probability of entering the sample or receiving a treatment state. Both are weighting conventions only; neither turns an association into causal identification on its own.

The ILR tables require a different reading rule from the PLR joint-share tables. The six-part joint composition is ordered as `share_joint_Injury_composed`, `share_joint_Injury_discomposed`, `share_joint_Rupture_composed`, `share_joint_Rupture_discomposed`, `share_joint_Distrust_composed`, and `share_joint_Distrust_discomposed`. The five reported ILR coordinates are balances rather than category-specific effects:

- `ilr_joint6_1`: Injury-composed versus Injury-discomposed.
- `ilr_joint6_2`: the geometric mean of the first two Injury cells versus Rupture-composed.
- `ilr_joint6_3`: the geometric mean of the first three cells versus Rupture-discomposed.
- `ilr_joint6_4`: the geometric mean of the first four cells versus Distrust-composed.
- `ilr_joint6_5`: the geometric mean of the first five cells versus Distrust-discomposed.

A positive coefficient shifts the composition toward the numerator side of that balance; a negative coefficient shifts it toward the denominator side. ILR coefficients should therefore be read as composition-level movement and then checked against the PLR joint-share tables for category-specific interpretation.

Table cells use the common format `beta + stars (s.e.); p=...`. In this frozen v1 baseline, the stars are attached to the raw p-value: `* p<0.05`, `** p<0.01`, `*** p<0.001`. BH-adjusted `q` values are not printed here; multiple-testing-aware interpretation should therefore be taken from the v2 working memo, which retains the same raw-p stars while also displaying `q`. Because `total_days_incarcerated` is measured in days, its coefficients will look mechanically smaller in magnitude.

## 5. Main treatment results

### 5.1 Unweighted

#### ILR Joint6

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | 3.972 (8.069); p=0.622 | 2.109 (2.705); p=0.436 | -5.936 (6.035); p=0.325 | 4.739 (5.234); p=0.365 | -1.352 (8.320); p=0.871 |
| Timing C: age_at_first_exposure | -0.200 (0.897); p=0.824 | -0.0095 (0.435); p=0.983 | 0.012 (0.400); p=0.977 | 0.039 (0.532); p=0.942 | -0.380 (0.866); p=0.661 |
| Dosage: total_days_incarcerated | 0.00051 (0.00042); p=0.226 | -0.00026 (0.00034); p=0.447 | -0.00029 (0.00039); p=0.460 | -0.00045 (0.00034); p=0.187 | -0.00030 (0.00036); p=0.410 |
| Severity: severity_index_v2 | -0.878 (1.328); p=0.508 | -0.046 (0.842); p=0.957 | 0.334 (1.120); p=0.766 | 0.348 (1.030); p=0.735 | -2.222 (1.155); p=0.054 |

#### PLR Joint Shares

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | 0.058 (0.120); p=0.630 | -0.027 (0.088); p=0.756 | -0.205 (0.238); p=0.389 | 0.215 (0.124); p=0.082 | -0.076 (0.129); p=0.559 | -0.047 (0.191); p=0.805 |
| Timing C: age_at_first_exposure | 0.016 (0.018); p=0.377 | -0.024 (0.022); p=0.266 | -0.0079 (0.023); p=0.726 | 0.043 (0.025); p=0.086 | -0.0031 (0.020); p=0.874 | -0.0031 (0.020); p=0.878 |
| Dosage: total_days_incarcerated | -8.15e-06 (9.67e-06); p=0.399 | -4.77e-06 (9.02e-06); p=0.597 | -1.40e-06 (1.75e-05); p=0.936 | 8.29e-06 (1.57e-05); p=0.598 | 8.18e-06 (1.39e-05); p=0.555 | -2.75e-06 (8.30e-06); p=0.740 |
| Severity: severity_index_v2 | -0.0038 (0.030); p=0.897 | -0.022 (0.023); p=0.332 | -0.095 (0.049); p=0.052 | -0.0071 (0.049); p=0.885 | 0.050 (0.037); p=0.172 | 0.079** (0.029); p=0.006 |

#### Track 2 Continuous

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | -0.037 (0.083); p=0.655 | -0.0078 (0.039); p=0.842 | 0.088 (0.106); p=0.409 |
| Timing C: age_at_first_exposure | 0.0064 (0.010); p=0.538 | 0.0097 (0.0075); p=0.193 | 0.0086 (0.014); p=0.536 |
| Dosage: total_days_incarcerated | 6.52e-06 (3.74e-06); p=0.081 | 4.86e-06 (4.62e-06); p=0.292 | -4.51e-06 (9.56e-06); p=0.637 |
| Severity: severity_index_v2 | 0.021* (0.010); p=0.037 | 0.020 (0.014); p=0.144 | 0.023 (0.028); p=0.420 |

### 5.2 IPW

#### ILR Joint6

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | 2.722 (11.731); p=0.817 | 3.727 (9.418); p=0.692 | -4.005 (11.049); p=0.717 | 6.738 (9.357); p=0.472 | -2.475 (10.707); p=0.817 |
| Timing C: age_at_first_exposure | -0.384 (1.019); p=0.706 | 0.150 (0.518); p=0.773 | 0.145 (0.487); p=0.766 | -0.084 (0.580); p=0.885 | 0.099 (0.833); p=0.905 |
| Dosage: total_days_incarcerated | 0.0014** (0.00055); p=0.008 | -0.00057 (0.00048); p=0.232 | -0.00018 (0.00044); p=0.678 | -0.0011* (0.00047); p=0.021 | -0.00016 (0.00046); p=0.732 |
| Severity: severity_index_v2 | -3.118 (1.798); p=0.083 | 0.253 (1.168); p=0.828 | -0.630 (1.231); p=0.609 | 2.843* (1.407); p=0.043 | -3.035* (1.394); p=0.029 |

#### PLR Joint Shares

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | 0.496 (0.328); p=0.130 | 0.400 (0.316); p=0.206 | -0.337 (0.425); p=0.428 | -0.061 (0.403); p=0.880 | -0.357 (0.497); p=0.472 | -0.091 (0.247); p=0.714 |
| Timing C: age_at_first_exposure | -0.0046 (0.019); p=0.806 | -0.011 (0.017); p=0.506 | -0.052 (0.029); p=0.069 | 0.052 (0.030); p=0.080 | 0.0016 (0.022); p=0.941 | 0.011 (0.027); p=0.685 |
| Dosage: total_days_incarcerated | 4.46e-06 (1.16e-05); p=0.701 | -1.45e-05 (1.07e-05); p=0.176 | 1.90e-05 (2.42e-05); p=0.431 | -2.39e-06 (2.14e-05); p=0.911 | 1.85e-05 (2.33e-05); p=0.427 | -1.28e-05 (1.10e-05); p=0.242 |
| Severity: severity_index_v2 | -0.044 (0.032); p=0.160 | -0.013 (0.036); p=0.711 | -0.154* (0.068); p=0.023 | 0.042 (0.070); p=0.547 | 0.030 (0.047); p=0.524 | 0.139** (0.044); p=0.002 |

#### Track 2 Continuous

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | -0.196 (0.148); p=0.185 | 0.046 (0.183); p=0.801 | 0.035 (0.289); p=0.902 |
| Timing C: age_at_first_exposure | 0.0036 (0.0093); p=0.700 | 0.018 (0.0093); p=0.055 | 0.018 (0.017); p=0.309 |
| Dosage: total_days_incarcerated | 8.26e-06 (5.13e-06); p=0.107 | 4.93e-06 (5.91e-06); p=0.404 | -5.57e-06 (1.24e-05); p=0.654 |
| Severity: severity_index_v2 | 0.041** (0.013); p=0.001 | -0.00013 (0.018); p=0.995 | 0.043 (0.038); p=0.262 |

### 5.3 Rake

#### ILR Joint6

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | -2.300 (12.803); p=0.857 | 6.577 (8.484); p=0.438 | -10.634 (9.421); p=0.259 | 6.983 (8.016); p=0.384 | -0.059 (8.626); p=0.995 |
| Timing C: age_at_first_exposure | 0.472 (1.251); p=0.706 | -0.126 (0.459); p=0.784 | 0.163 (0.485); p=0.737 | 0.250 (0.422); p=0.553 | 0.963 (0.980); p=0.326 |
| Dosage: total_days_incarcerated | 0.0012* (0.00056); p=0.035 | -0.00045 (0.00050); p=0.368 | -0.00015 (0.00045); p=0.735 | -0.0012** (0.00048); p=0.009 | 0.00012 (0.00045); p=0.797 |
| Severity: severity_index_v2 | -2.697 (1.736); p=0.120 | -0.197 (1.350); p=0.884 | -1.511 (1.263); p=0.232 | 2.451 (1.340); p=0.067 | -3.611* (1.449); p=0.013 |

#### PLR Joint Shares

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | 0.310 (0.313); p=0.322 | 0.347 (0.361); p=0.335 | -0.305 (0.360); p=0.397 | 0.039 (0.337); p=0.909 | -0.233 (0.358); p=0.515 | -0.069 (0.199); p=0.730 |
| Timing C: age_at_first_exposure | 0.0038 (0.023); p=0.871 | -0.00071 (0.0094); p=0.940 | -0.0098 (0.041); p=0.810 | 0.030 (0.029); p=0.289 | -0.0094 (0.013); p=0.477 | -0.016 (0.033); p=0.631 |
| Dosage: total_days_incarcerated | 1.60e-06 (1.25e-05); p=0.898 | -4.30e-06 (9.33e-06); p=0.645 | 1.15e-05 (2.51e-05); p=0.646 | -8.29e-06 (2.31e-05); p=0.719 | 2.77e-05 (2.49e-05); p=0.265 | -1.11e-05 (1.11e-05); p=0.318 |
| Severity: severity_index_v2 | -0.039 (0.034); p=0.241 | -0.033 (0.034); p=0.325 | -0.129 (0.068); p=0.056 | 0.076 (0.073); p=0.294 | 0.015 (0.047); p=0.752 | 0.129*** (0.039); p<0.001 |

#### Track 2 Continuous

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | -0.125 (0.138); p=0.365 | 0.091 (0.163); p=0.576 | 0.239 (0.274); p=0.382 |
| Timing C: age_at_first_exposure | -0.0011 (0.0058); p=0.849 | 0.018 (0.011); p=0.107 | 0.0028 (0.018); p=0.874 |
| Dosage: total_days_incarcerated | 9.13e-06 (5.00e-06); p=0.068 | 1.80e-07 (6.33e-06); p=0.977 | -1.19e-05 (1.24e-05); p=0.336 |
| Severity: severity_index_v2 | 0.038** (0.014); p=0.007 | 0.032 (0.019); p=0.094 | 0.055 (0.039); p=0.152 |

## 6. Severity component decomposition

### 6.1 Unweighted

#### ILR Joint6 Components

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | -0.174 (0.883); p=0.844 | -0.035 (0.437); p=0.936 | 0.0072 (0.403); p=0.986 | -0.016 (0.524); p=0.976 | -0.388 (0.869); p=0.655 |
| Dosage: total_days_incarcerated | 0.00055 (0.00043); p=0.208 | -0.00019 (0.00036); p=0.603 | -0.00019 (0.00040); p=0.629 | -0.00047 (0.00036); p=0.189 | -0.00027 (0.00038); p=0.479 |
| Component: family_separation_flag | -0.414 (1.215); p=0.733 | -1.314 (1.030); p=0.202 | -0.040 (1.167); p=0.972 | -0.308 (0.923); p=0.739 | -0.950 (1.180); p=0.421 |
| Component: parental_arrest_flag | -0.466 (0.653); p=0.475 | 0.838 (0.438); p=0.056 | 0.227 (0.599); p=0.705 | 1.030* (0.495); p=0.038 | -0.176 (0.609); p=0.773 |
| Component: loyalty_conflict_flag | 1.187 (0.627); p=0.058 | -0.223 (0.481); p=0.644 | 0.892 (0.536); p=0.096 | -1.183* (0.491); p=0.016 | -0.421 (0.537); p=0.434 |
| Component: segregation_flag | -0.952 (0.682); p=0.163 | -0.178 (0.558); p=0.750 | -0.570 (0.564); p=0.312 | 0.618 (0.534); p=0.247 | -0.838 (0.603); p=0.164 |

#### PLR Joint Share Components

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | 0.015 (0.018); p=0.394 | -0.024 (0.022); p=0.264 | -0.0073 (0.023); p=0.746 | 0.041 (0.024); p=0.094 | -0.0021 (0.020); p=0.915 | -0.0028 (0.020); p=0.891 |
| Dosage: total_days_incarcerated | -3.14e-06 (1.01e-05); p=0.755 | -7.10e-06 (9.75e-06); p=0.466 | -7.44e-07 (1.81e-05); p=0.967 | 5.81e-06 (1.59e-05); p=0.714 | 1.09e-05 (1.42e-05); p=0.442 | -3.24e-06 (8.38e-06); p=0.699 |
| Component: family_separation_flag | 0.023 (0.045); p=0.610 | -0.016 (0.020); p=0.413 | 0.041 (0.044); p=0.352 | -0.043 (0.050); p=0.386 | -0.027 (0.032); p=0.388 | 0.062 (0.033); p=0.061 |
| Component: parental_arrest_flag | 0.0021 (0.016); p=0.895 | -0.0014 (0.012); p=0.909 | -0.049 (0.025); p=0.050 | 0.042 (0.024); p=0.082 | 0.0091 (0.017); p=0.600 | -0.0036 (0.014); p=0.804 |
| Component: loyalty_conflict_flag | 0.015 (0.015); p=0.324 | -0.024* (0.012); p=0.043 | -0.0056 (0.023); p=0.803 | -0.065** (0.022); p=0.002 | 0.054** (0.019); p=0.004 | 0.029* (0.013); p=0.032 |
| Component: segregation_flag | -0.025 (0.017); p=0.140 | 0.0088 (0.013); p=0.489 | -0.039 (0.027); p=0.144 | 0.030 (0.024); p=0.216 | -0.0091 (0.018); p=0.607 | 0.021 (0.014); p=0.119 |

#### Track 2 Continuous Components

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing C: age_at_first_exposure | 0.0065 (0.010); p=0.535 | 0.0098 (0.0075); p=0.193 | 0.0080 (0.014); p=0.555 |
| Dosage: total_days_incarcerated | 7.07e-06 (3.96e-06); p=0.074 | 3.31e-06 (4.87e-06); p=0.497 | -7.65e-06 (9.59e-06); p=0.425 |
| Component: family_separation_flag | 0.00086 (0.014); p=0.952 | -0.011 (0.021); p=0.606 | -0.020 (0.027); p=0.449 |
| Component: parental_arrest_flag | 0.0045 (0.0048); p=0.348 | 0.0066 (0.0060); p=0.277 | 0.021 (0.015); p=0.166 |
| Component: loyalty_conflict_flag | 0.018*** (0.0054); p<0.001 | -0.0086 (0.0066); p=0.194 | -0.022 (0.013); p=0.100 |
| Component: segregation_flag | -0.00078 (0.0061); p=0.899 | 0.018* (0.0070); p=0.013 | 0.028* (0.014); p=0.046 |

### 6.2 IPW

#### ILR Joint6 Components

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | -0.367 (1.018); p=0.719 | 0.128 (0.510); p=0.802 | 0.155 (0.490); p=0.752 | -0.090 (0.590); p=0.879 | 0.055 (0.844); p=0.948 |
| Dosage: total_days_incarcerated | 0.0013* (0.00057); p=0.021 | -0.00039 (0.00047); p=0.403 | -0.00018 (0.00044); p=0.686 | -0.0011* (0.00048); p=0.026 | -0.00013 (0.00047); p=0.774 |
| Component: family_separation_flag | -1.838 (1.250); p=0.141 | -1.740 (1.428); p=0.223 | -1.312 (1.374); p=0.340 | 2.695 (1.439); p=0.061 | -1.571 (2.141); p=0.463 |
| Component: parental_arrest_flag | -1.126 (0.871); p=0.196 | 1.179 (0.705); p=0.094 | 0.248 (0.968); p=0.798 | 0.700 (0.667); p=0.294 | -0.490 (0.876); p=0.576 |
| Component: loyalty_conflict_flag | 0.127 (0.902); p=0.888 | 0.807 (0.619); p=0.192 | 1.051 (0.697); p=0.131 | 0.275 (0.604); p=0.649 | -0.910 (0.711); p=0.201 |
| Component: segregation_flag | -0.842 (0.894); p=0.346 | -0.925 (0.599); p=0.122 | -0.872 (0.587); p=0.137 | 0.800 (0.701); p=0.254 | -0.775 (0.748); p=0.300 |

#### PLR Joint Share Components

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | -0.0059 (0.019); p=0.752 | -0.012 (0.017); p=0.482 | -0.054 (0.029); p=0.063 | 0.051 (0.029); p=0.082 | 0.0029 (0.023); p=0.897 | 0.015 (0.028); p=0.604 |
| Dosage: total_days_incarcerated | 6.34e-06 (1.10e-05); p=0.563 | -1.39e-05 (1.13e-05); p=0.221 | 1.74e-05 (2.38e-05); p=0.465 | -3.45e-06 (2.17e-05); p=0.874 | 2.36e-05 (2.24e-05); p=0.293 | -1.57e-05 (1.11e-05); p=0.155 |
| Component: family_separation_flag | -0.023 (0.034); p=0.511 | 0.022 (0.032); p=0.499 | 0.020 (0.040); p=0.619 | 0.044 (0.060); p=0.463 | -0.112* (0.045); p=0.013 | 0.063 (0.037); p=0.093 |
| Component: parental_arrest_flag | 0.012 (0.022); p=0.581 | -0.00074 (0.013); p=0.954 | -0.066 (0.034); p=0.054 | 0.032 (0.033); p=0.328 | 0.038 (0.029); p=0.188 | 0.0021 (0.019); p=0.914 |
| Component: loyalty_conflict_flag | 0.021 (0.018); p=0.245 | -0.0017 (0.014); p=0.900 | -0.071* (0.032); p=0.028 | -0.050 (0.027); p=0.062 | 0.042 (0.023); p=0.064 | 0.053** (0.018); p=0.003 |
| Component: segregation_flag | -0.039* (0.016); p=0.016 | -0.0090 (0.017); p=0.587 | -0.019 (0.034); p=0.583 | 0.044 (0.032); p=0.175 | -0.022 (0.020); p=0.254 | 0.039* (0.017); p=0.023 |

#### Track 2 Continuous Components

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing C: age_at_first_exposure | 0.0045 (0.0095); p=0.637 | 0.018 (0.0093); p=0.058 | 0.018 (0.018); p=0.306 |
| Dosage: total_days_incarcerated | 8.39e-06 (5.27e-06); p=0.111 | 3.98e-06 (5.80e-06); p=0.493 | -6.81e-06 (1.26e-05); p=0.590 |
| Component: family_separation_flag | -0.00019 (0.012); p=0.988 | -0.0065 (0.024); p=0.790 | 0.025 (0.029); p=0.389 |
| Component: parental_arrest_flag | 0.0093 (0.0078); p=0.235 | 0.0012 (0.0090); p=0.899 | 0.012 (0.023); p=0.611 |
| Component: loyalty_conflict_flag | 0.017** (0.0065); p=0.009 | -0.028** (0.0098); p=0.004 | -0.0081 (0.016); p=0.623 |
| Component: segregation_flag | 0.0079 (0.0058); p=0.178 | 0.020* (0.0083); p=0.016 | 0.025 (0.019); p=0.174 |

### 6.3 Rake

#### ILR Joint6 Components

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | 0.513 (1.252); p=0.682 | -0.102 (0.411); p=0.803 | 0.186 (0.458); p=0.685 | 0.232 (0.426); p=0.587 | 0.952 (0.982); p=0.332 |
| Dosage: total_days_incarcerated | 0.0010 (0.00057); p=0.081 | -0.00023 (0.00048); p=0.638 | -0.00011 (0.00046); p=0.817 | -0.0012* (0.00048); p=0.013 | 8.59e-05 (0.00046); p=0.852 |
| Component: family_separation_flag | -2.333* (1.153); p=0.043 | -3.380* (1.353); p=0.012 | -2.155 (1.122); p=0.055 | 1.853 (1.308); p=0.157 | -2.489 (1.681); p=0.139 |
| Component: parental_arrest_flag | -1.152 (0.828); p=0.164 | 1.059 (0.733); p=0.148 | -0.068 (0.926); p=0.942 | 0.951 (0.654); p=0.146 | -0.694 (0.860); p=0.420 |
| Component: loyalty_conflict_flag | -0.480 (0.803); p=0.551 | 1.034 (0.664); p=0.119 | 0.662 (0.631); p=0.294 | 0.321 (0.612); p=0.600 | -1.147 (0.648); p=0.077 |
| Component: segregation_flag | -0.050 (0.882); p=0.955 | -1.254 (0.673); p=0.062 | -1.029 (0.608); p=0.091 | 0.546 (0.677); p=0.420 | -0.656 (0.775); p=0.397 |

#### PLR Joint Share Components

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | 0.0039 (0.022); p=0.859 | -0.00052 (0.0095); p=0.957 | -0.011 (0.041); p=0.793 | 0.027 (0.028); p=0.331 | -0.0077 (0.014); p=0.579 | -0.014 (0.034); p=0.674 |
| Dosage: total_days_incarcerated | 4.84e-06 (1.24e-05); p=0.697 | -4.53e-06 (1.00e-05); p=0.651 | 2.59e-06 (2.45e-05); p=0.916 | -4.30e-06 (2.32e-05); p=0.853 | 2.96e-05 (2.44e-05); p=0.225 | -1.04e-05 (1.06e-05); p=0.327 |
| Component: family_separation_flag | -0.034 (0.040); p=0.394 | -0.032 (0.036); p=0.373 | 0.028 (0.041); p=0.492 | 0.094 (0.069); p=0.170 | -0.098* (0.039); p=0.012 | 0.071* (0.034); p=0.034 |
| Component: parental_arrest_flag | -0.0031 (0.021); p=0.883 | -0.0045 (0.016); p=0.775 | -0.060 (0.035); p=0.087 | 0.058 (0.034); p=0.087 | 0.026 (0.028); p=0.345 | -0.00077 (0.019); p=0.967 |
| Component: loyalty_conflict_flag | 0.023 (0.017); p=0.174 | 0.00015 (0.015); p=0.992 | -0.058 (0.030); p=0.055 | -0.049 (0.028); p=0.078 | 0.035 (0.020); p=0.089 | 0.057** (0.018); p=0.001 |
| Component: segregation_flag | -0.038* (0.018); p=0.030 | -0.012 (0.016); p=0.472 | 0.0067 (0.036); p=0.852 | 0.032 (0.034); p=0.335 | -0.014 (0.019); p=0.482 | 0.022 (0.018); p=0.232 |

#### Track 2 Continuous Components

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing C: age_at_first_exposure | -0.00064 (0.0060); p=0.914 | 0.017 (0.012); p=0.134 | 0.0027 (0.018); p=0.881 |
| Dosage: total_days_incarcerated | 9.52e-06 (5.11e-06); p=0.062 | -7.25e-07 (6.25e-06); p=0.908 | -1.07e-05 (1.24e-05); p=0.389 |
| Component: family_separation_flag | 0.0048 (0.014); p=0.734 | 0.0085 (0.026); p=0.749 | 0.027 (0.027); p=0.331 |
| Component: parental_arrest_flag | 0.011 (0.0074); p=0.141 | 0.013 (0.0097); p=0.184 | 0.018 (0.022); p=0.409 |
| Component: loyalty_conflict_flag | 0.016** (0.0063); p=0.009 | -0.023* (0.0091); p=0.010 | 0.0028 (0.017); p=0.869 |
| Component: segregation_flag | 0.0055 (0.0064); p=0.384 | 0.028** (0.0094); p=0.003 | 0.016 (0.019); p=0.409 |

## 7. Narrative interpretation

Across the main treatment block, the most stable nonzero signal still comes from `severity_index_v2`, not `adolescent_exposure_flag`. Across `unweighted`, `ipw`, and `rake`, severity remains positive on Track 2 `authority_stance`; within the Track 1 per-cell joint shares, it most consistently shifts expression toward `share_joint_Distrust_discomposed` while loading negatively on several injury- and rupture-related cells. By contrast, the timing dummy is usually weak, and continuous timing `age_at_first_exposure` leaves only scattered and not fully consistent local results.

The ILR Joint6 tables show that under weighted specifications, `severity_index_v2` is most likely to appear on `ilr_joint6_4` and `ilr_joint6_5`, which indicates composition-level movement with treatment intensity. But ILR coordinates should not be read as changes in any single share. The substantive interpretation should therefore remain anchored in the PLR joint-share tables. For dosage, the coefficients on `total_days_incarcerated` are numerically small mainly because the unit is a single day, so dosage should be judged by direction and significance rather than absolute magnitude.

Within the severity decomposition, `loyalty_conflict_flag` is the dominant component. It repeatedly appears across weighting schemes in distrust-related and rupture-related outcomes, and on Track 2 it is also associated with higher `authority_stance`. `parental_arrest_flag` has a narrower signal, mostly limited to a smaller set of composure/text rows or a few PLR outcomes. `family_separation_flag` and `segregation_flag` are not null across the board, but they are materially less stable than `loyalty_conflict_flag`. The safest decomposition narrative at this stage is therefore that the aggregate severity signal is driven primarily by the loyalty-conflict channel.

## 8. Source files

- `models/causal_estimates_v1/track1_ilr_v1/track1_ilr_estimates_v1.csv`
- `models/causal_estimates_v1/track1_per_cell_v1/track1_per_cell_estimates_v1.csv`
- `models/causal_estimates_v1/track2_v1/track2_estimates_v1.csv`
- `models/causal_estimates_v1/track1_ilr_severity_components_v1/track1_ilr_severity_components_estimates_v1.csv`
- `models/causal_estimates_v1/track1_per_cell_severity_components_v1/track1_per_cell_severity_components_estimates_v1.csv`
- `models/causal_estimates_v1/track2_severity_components_v1/track2_severity_components_estimates_v1.csv`
