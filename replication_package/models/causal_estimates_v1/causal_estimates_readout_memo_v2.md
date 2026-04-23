# Causal Estimates Readout Memo v2

Date: 2026-04-19

Status: Release-facing v2 memo for the frozen 2026-04-20 causal-results archive.

## 1. What this memo reports

This document is now the single causal-results memo for the project. It consolidates the main-sample narrator-level DML results in one place. It contains three parts:

- The main model setup and estimation conventions.
- Eighteen full result tables: 3 weighting schemes x 3 outcome families x 2 result blocks.
- A narrative interpretation that can be adapted directly into the paper's results section.

This version updates the reporting layer so the memo now surfaces BH-adjusted q-values directly in the tables while retaining raw p-values for transparency.

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

where `D_i` is `adolescent_exposure_flag`.

Timing-continuous / dosage / severity correspond to the joint continuous DML specification:

$$
Y_{io} = \tau_A A_i + \tau_T T_i + \tau_S S_i + X_i^\top \beta + u_{io}
$$

where `A_i` is `age_at_first_exposure`, `T_i` is `total_days_incarcerated`, and `S_i` is `severity_index_v2`.

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

Table cells now use the format `beta + stars (s.e.); p=...; q=...`. The stars follow raw p-values: `* p<0.05`, `** p<0.01`, `*** p<0.001`. BH-adjusted `q` values are retained for multiple-testing-aware interpretation, and corrected interpretation should still follow `BH q`.

## 5. Main treatment results

### 5.1 Unweighted

#### ILR Joint6

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | 3.972 (8.069); p=0.622; q=0.956 | 2.109 (2.705); p=0.436; q=0.934 | -5.936 (6.035); p=0.325; q=0.912 | 4.739 (5.234); p=0.365; q=0.934 | -1.352 (8.32); p=0.871; q=0.976 |
| Timing C: age_at_first_exposure | -0.1997 (0.8967); p=0.824; q=0.966 | -0.009494 (0.4349); p=0.983; q=0.994 | 0.01153 (0.4); p=0.977; q=0.993 | 0.03889 (0.5318); p=0.942; q=0.984 | -0.3802 (0.8665); p=0.661; q=0.956 |
| Dosage: total_days_incarcerated | 0.0005139 (0.000424); p=0.226; q=0.789 | -0.0002601 (0.0003421); p=0.447; q=0.934 | -0.0002864 (0.0003877); p=0.46; q=0.942 | -0.0004541 (0.0003442); p=0.187; q=0.693 | -0.0002973 (0.0003606); p=0.41; q=0.934 |
| Severity: severity_index_v2 | -0.8783 (1.328); p=0.508; q=0.956 | -0.04587 (0.8417); p=0.957; q=0.984 | 0.3337 (1.12); p=0.766; q=0.961 | 0.3485 (1.03); p=0.735; q=0.961 | -2.222 (1.155); p=0.0545; q=0.375 |

#### PLR Joint Shares

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | 0.0577 (0.1198); p=0.63; q=0.976 | -0.02738 (0.088); p=0.756; q=0.981 | -0.2047 (0.2376); p=0.389; q=0.887 | 0.2152 (0.1237); p=0.0818; q=0.523 | -0.07561 (0.1293); p=0.559; q=0.949 | -0.04708 (0.1906); p=0.805; q=0.981 |
| Timing C: age_at_first_exposure | 0.01568 (0.01774); p=0.377; q=0.887 | -0.02407 (0.02166); p=0.266; q=0.856 | -0.00794 (0.02263); p=0.726; q=0.981 | 0.04301 (0.02509); p=0.0865; q=0.543 | -0.003128 (0.01979); p=0.874; q=0.981 | -0.003116 (0.02023); p=0.878; q=0.981 |
| Dosage: total_days_incarcerated | -8.148e-06 (9.669e-06); p=0.399; q=0.887 | -4.771e-06 (9.024e-06); p=0.597; q=0.964 | -1.405e-06 (1.755e-05); p=0.936; q=0.981 | 8.286e-06 (1.569e-05); p=0.598; q=0.964 | 8.182e-06 (1.386e-05); p=0.555; q=0.949 | -2.754e-06 (8.299e-06); p=0.74; q=0.981 |
| Severity: severity_index_v2 | -0.003832 (0.02973); p=0.897; q=0.981 | -0.0221 (0.02277); p=0.332; q=0.887 | -0.09536 (0.04909); p=0.0521; q=0.396 | -0.007079 (0.04878); p=0.885; q=0.981 | 0.04995 (0.03654); p=0.172; q=0.707 | 0.07878** (0.02869); p=0.00604; q=0.0984 |

#### Track 2 Continuous

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | -0.03692 (0.0827); p=0.655; q=0.956 | -0.007827 (0.03936); p=0.842; q=0.995 | 0.08754 (0.1061); p=0.409; q=0.737 |
| Timing C: age_at_first_exposure | 0.006366 (0.01032); p=0.538; q=0.854 | 0.009699 (0.00745); p=0.193; q=0.548 | 0.008564 (0.01385); p=0.536; q=0.854 |
| Dosage: total_days_incarcerated | 6.52e-06 (3.736e-06); p=0.081; q=0.358 | 4.864e-06 (4.616e-06); p=0.292; q=0.631 | -4.514e-06 (9.565e-06); p=0.637; q=0.956 |
| Severity: severity_index_v2 | 0.02147* (0.01031); p=0.0373; q=0.201 | 0.01983 (0.01356); p=0.144; q=0.456 | 0.02265 (0.02809); p=0.42; q=0.744 |

### 5.2 IPW

#### ILR Joint6

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | 2.722 (11.73); p=0.817; q=0.966 | 3.727 (9.418); p=0.692; q=0.956 | -4.005 (11.05); p=0.717; q=0.961 | 6.738 (9.357); p=0.472; q=0.942 | -2.475 (10.71); p=0.817; q=0.966 |
| Timing C: age_at_first_exposure | -0.3844 (1.019); p=0.706; q=0.956 | 0.1496 (0.5178); p=0.773; q=0.961 | 0.1449 (0.4866); p=0.766; q=0.961 | -0.08424 (0.5804); p=0.885; q=0.976 | 0.09911 (0.8332); p=0.905; q=0.977 |
| Dosage: total_days_incarcerated | 0.001447** (0.0005453); p=0.00799; q=0.142 | -0.0005684 (0.0004753); p=0.232; q=0.789 | -0.0001834 (0.000441); p=0.678; q=0.956 | -0.001083* (0.00047); p=0.0212; q=0.246 | -0.0001573 (0.0004589); p=0.732; q=0.961 |
| Severity: severity_index_v2 | -3.118 (1.798); p=0.083; q=0.475 | 0.2534 (1.168); p=0.828; q=0.966 | -0.63 (1.231); p=0.609; q=0.956 | 2.843* (1.407); p=0.0433; q=0.352 | -3.035* (1.394); p=0.0294; q=0.275 |

#### PLR Joint Shares

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | 0.4959 (0.328); p=0.13; q=0.637 | 0.4004 (0.3164); p=0.206; q=0.78 | -0.3367 (0.4247); p=0.428; q=0.894 | -0.06079 (0.4029); p=0.88; q=0.981 | -0.3569 (0.4968); p=0.472; q=0.926 | -0.09053 (0.2469); p=0.714; q=0.981 |
| Timing C: age_at_first_exposure | -0.004592 (0.01867); p=0.806; q=0.981 | -0.01139 (0.01714); p=0.506; q=0.944 | -0.05183 (0.02854); p=0.0693; q=0.466 | 0.05239 (0.02993); p=0.08; q=0.516 | 0.001631 (0.02219); p=0.941; q=0.981 | 0.01111 (0.02742); p=0.685; q=0.981 |
| Dosage: total_days_incarcerated | 4.463e-06 (1.161e-05); p=0.701; q=0.981 | -1.45e-05 (1.071e-05); p=0.176; q=0.72 | 1.902e-05 (2.416e-05); p=0.431; q=0.894 | -2.394e-06 (2.14e-05); p=0.911; q=0.981 | 1.85e-05 (2.33e-05); p=0.427; q=0.894 | -1.282e-05 (1.096e-05); p=0.242; q=0.825 |
| Severity: severity_index_v2 | -0.04444 (0.03163); p=0.16; q=0.694 | -0.01337 (0.03607); p=0.711; q=0.981 | -0.1544* (0.06791); p=0.023; q=0.23 | 0.04191 (0.06952); p=0.547; q=0.949 | 0.02986 (0.04689); p=0.524; q=0.949 | 0.1393** (0.04433); p=0.00168; q=0.0446 |

#### Track 2 Continuous

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | -0.196 (0.148); p=0.185; q=0.541 | 0.04627 (0.1835); p=0.801; q=0.995 | 0.03548 (0.289); p=0.902; q=0.995 |
| Timing C: age_at_first_exposure | 0.003564 (0.009259); p=0.7; q=0.977 | 0.01777 (0.009266); p=0.0552; q=0.271 | 0.01771 (0.01741); p=0.309; q=0.654 |
| Dosage: total_days_incarcerated | 8.26e-06 (5.127e-06); p=0.107; q=0.393 | 4.933e-06 (5.913e-06); p=0.404; q=0.737 | -5.568e-06 (1.242e-05); p=0.654; q=0.956 |
| Severity: severity_index_v2 | 0.04091** (0.01276); p=0.00134; q=0.029 | -0.0001257 (0.01827); p=0.995; q=0.995 | 0.04294 (0.03828); p=0.262; q=0.59 |

### 5.3 Rake

#### ILR Joint6

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | -2.3 (12.8); p=0.857; q=0.976 | 6.577 (8.484); p=0.438; q=0.934 | -10.63 (9.421); p=0.259; q=0.842 | 6.983 (8.016); p=0.384; q=0.934 | -0.0592 (8.626); p=0.995; q=0.997 |
| Timing C: age_at_first_exposure | 0.4724 (1.251); p=0.706; q=0.956 | -0.1256 (0.4589); p=0.784; q=0.961 | 0.163 (0.4853); p=0.737; q=0.961 | 0.2505 (0.4223); p=0.553; q=0.956 | 0.9633 (0.9803); p=0.326; q=0.912 |
| Dosage: total_days_incarcerated | 0.001183* (0.0005596); p=0.0345; q=0.311 | -0.0004534 (0.0005033); p=0.368; q=0.934 | -0.000153 (0.0004514); p=0.735; q=0.961 | -0.001239** (0.0004763); p=0.00932; q=0.142 | 0.0001165 (0.0004523); p=0.797; q=0.961 |
| Severity: severity_index_v2 | -2.697 (1.736); p=0.12; q=0.586 | -0.1967 (1.35); p=0.884; q=0.976 | -1.511 (1.263); p=0.232; q=0.789 | 2.451 (1.34); p=0.0674; q=0.435 | -3.611* (1.449); p=0.0127; q=0.178 |

#### PLR Joint Shares

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | 0.3097 (0.313); p=0.322; q=0.887 | 0.3473 (0.3606); p=0.335; q=0.887 | -0.3046 (0.3596); p=0.397; q=0.887 | 0.03851 (0.3365); p=0.909; q=0.981 | -0.2333 (0.3582); p=0.515; q=0.944 | -0.06875 (0.1994); p=0.73; q=0.981 |
| Timing C: age_at_first_exposure | 0.003757 (0.02305); p=0.871; q=0.981 | -0.0007063 (0.009438); p=0.94; q=0.981 | -0.00976 (0.04051); p=0.81; q=0.981 | 0.03023 (0.0285); p=0.289; q=0.881 | -0.00937 (0.01318); p=0.477; q=0.932 | -0.01598 (0.03331); p=0.631; q=0.976 |
| Dosage: total_days_incarcerated | 1.604e-06 (1.251e-05); p=0.898; q=0.981 | -4.297e-06 (9.328e-06); p=0.645; q=0.976 | 1.154e-05 (2.51e-05); p=0.646; q=0.976 | -8.291e-06 (2.307e-05); p=0.719; q=0.981 | 2.774e-05 (2.489e-05); p=0.265; q=0.855 | -1.109e-05 (1.111e-05); p=0.318; q=0.887 |
| Severity: severity_index_v2 | -0.03934 (0.03352); p=0.241; q=0.825 | -0.03337 (0.03389); p=0.325; q=0.887 | -0.1289 (0.06752); p=0.0563; q=0.41 | 0.07638 (0.07279); p=0.294; q=0.881 | 0.01498 (0.04744); p=0.752; q=0.981 | 0.1287*** (0.03901); p=<0.001; q=0.0332 |

#### Track 2 Continuous

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing D: adolescent_exposure_flag | -0.1252 (0.1383); p=0.365; q=0.717 | 0.09088 (0.1626); p=0.576; q=0.899 | 0.2393 (0.2737); p=0.382; q=0.731 |
| Timing C: age_at_first_exposure | -0.00111 (0.00583); p=0.849; q=0.995 | 0.01763 (0.01093); p=0.107; q=0.393 | 0.002821 (0.01786); p=0.874; q=0.995 |
| Dosage: total_days_incarcerated | 9.132e-06 (5e-06); p=0.0678; q=0.318 | 1.802e-07 (6.332e-06); p=0.977; q=0.995 | -1.189e-05 (1.236e-05); p=0.336; q=0.698 |
| Severity: severity_index_v2 | 0.03815** (0.01417); p=0.00709; q=0.085 | 0.03153 (0.01885); p=0.0945; q=0.378 | 0.05545 (0.03866); p=0.152; q=0.468 |

## 6. Severity component decomposition

### 6.1 Unweighted

#### ILR Joint6 Components

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | -0.1738 (0.8827); p=0.844; q=0.958 | -0.03513 (0.4372); p=0.936; q=0.978 | 0.007225 (0.4027); p=0.986; q=0.986 | -0.01603 (0.5243); p=0.976; q=0.983 | -0.3878 (0.8687); p=0.655; q=0.928 |
| Dosage: total_days_incarcerated | 0.0005451 (0.0004326); p=0.208; q=0.557 | -0.0001865 (0.0003581); p=0.603; q=0.928 | -0.0001912 (0.0003955); p=0.629; q=0.928 | -0.000473 (0.0003599); p=0.189; q=0.554 | -0.0002687 (0.0003799); p=0.479; q=0.837 |
| Component: family_separation_flag | -0.4137 (1.215); p=0.733; q=0.943 | -1.314 (1.03); p=0.202; q=0.554 | -0.04034 (1.167); p=0.972; q=0.983 | -0.3079 (0.9226); p=0.739; q=0.943 | -0.9499 (1.18); p=0.421; q=0.791 |
| Component: parental_arrest_flag | -0.4661 (0.6529); p=0.475; q=0.837 | 0.8381 (0.4382); p=0.0558; q=0.414 | 0.2268 (0.5987); p=0.705; q=0.935 | 1.03* (0.4951); p=0.0376; q=0.414 | -0.1761 (0.6094); p=0.773; q=0.943 |
| Component: loyalty_conflict_flag | 1.187 (0.6269); p=0.0583; q=0.414 | -0.2226 (0.4813); p=0.644; q=0.928 | 0.8922 (0.5357); p=0.0958; q=0.473 | -1.183* (0.4911); p=0.016; q=0.414 | -0.4207 (0.5374); p=0.434; q=0.804 |
| Component: segregation_flag | -0.9519 (0.6817); p=0.163; q=0.517 | -0.1777 (0.5577); p=0.75; q=0.943 | -0.5699 (0.5636); p=0.312; q=0.702 | 0.6183 (0.5342); p=0.247; q=0.623 | -0.8382 (0.6026); p=0.164; q=0.517 |

#### PLR Joint Share Components

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | 0.01512 (0.01773); p=0.394; q=0.8 | -0.02412 (0.0216); p=0.264; q=0.707 | -0.007315 (0.02254); p=0.746; q=0.959 | 0.04097 (0.02445); p=0.0938; q=0.411 | -0.002131 (0.02005); p=0.915; q=0.996 | -0.002775 (0.02023); p=0.891; q=0.996 |
| Dosage: total_days_incarcerated | -3.144e-06 (1.006e-05); p=0.755; q=0.959 | -7.1e-06 (9.748e-06); p=0.466; q=0.822 | -7.442e-07 (1.815e-05); p=0.967; q=0.996 | 5.811e-06 (1.585e-05); p=0.714; q=0.95 | 1.09e-05 (1.418e-05); p=0.442; q=0.813 | -3.243e-06 (8.381e-06); p=0.699; q=0.937 |
| Component: family_separation_flag | 0.02279 (0.04467); p=0.61; q=0.888 | -0.01601 (0.01956); p=0.413; q=0.803 | 0.04106 (0.04415); p=0.352; q=0.783 | -0.04302 (0.04957); p=0.386; q=0.8 | -0.02738 (0.03171); p=0.388; q=0.8 | 0.06219 (0.03325); p=0.0614; q=0.34 |
| Component: parental_arrest_flag | 0.002142 (0.01628); p=0.895; q=0.996 | -0.001356 (0.0119); p=0.909; q=0.996 | -0.04942 (0.02526); p=0.0505; q=0.31 | 0.04191 (0.02406); p=0.0815; q=0.402 | 0.009095 (0.01737); p=0.6; q=0.888 | -0.0036 (0.01449); p=0.804; q=0.985 |
| Component: loyalty_conflict_flag | 0.01485 (0.01506); p=0.324; q=0.762 | -0.02381* (0.01174); p=0.0426; q=0.275 | -0.005635 (0.02258); p=0.803; q=0.985 | -0.06541** (0.02152); p=0.00237; q=0.0499 | 0.05418** (0.01859); p=0.00357; q=0.0565 | 0.02888* (0.01349); p=0.0323; q=0.251 |
| Component: segregation_flag | -0.02519 (0.01705); p=0.14; q=0.53 | 0.008781 (0.01269); p=0.489; q=0.831 | -0.03892 (0.02666); p=0.144; q=0.542 | 0.0303 (0.02447); p=0.216; q=0.652 | -0.009075 (0.01766); p=0.607; q=0.888 | 0.02128 (0.01365); p=0.119; q=0.49 |

#### Track 2 Continuous Components

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing C: age_at_first_exposure | 0.006479 (0.01043); p=0.535; q=0.78 | 0.009802 (0.007534); p=0.193; q=0.477 | 0.007985 (0.01351); p=0.555; q=0.788 |
| Dosage: total_days_incarcerated | 7.073e-06 (3.96e-06); p=0.0741; q=0.333 | 3.31e-06 (4.872e-06); p=0.497; q=0.745 | -7.653e-06 (9.586e-06); p=0.425; q=0.695 |
| Component: family_separation_flag | 0.0008587 (0.01437); p=0.952; q=0.97 | -0.01074 (0.02081); p=0.606; q=0.8 | -0.02008 (0.0265); p=0.449; q=0.713 |
| Component: parental_arrest_flag | 0.004522 (0.00482); p=0.348; q=0.691 | 0.006569 (0.006037); p=0.277; q=0.622 | 0.02055 (0.01483); p=0.166; q=0.477 |
| Component: loyalty_conflict_flag | 0.01818*** (0.005377); p=<0.001; q=0.0391 | -0.008609 (0.00663); p=0.194; q=0.477 | -0.02208 (0.01342); p=0.1; q=0.416 |
| Component: segregation_flag | -0.0007821 (0.006139); p=0.899; q=0.949 | 0.01755* (0.007039); p=0.0126; q=0.0974 | 0.02801* (0.01401); p=0.0455; q=0.273 |

### 6.2 IPW

#### ILR Joint6 Components

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | -0.3667 (1.018); p=0.719; q=0.943 | 0.1277 (0.51); p=0.802; q=0.943 | 0.1546 (0.4897); p=0.752; q=0.943 | -0.08982 (0.5901); p=0.879; q=0.975 | 0.05507 (0.8442); p=0.948; q=0.978 |
| Dosage: total_days_incarcerated | 0.001317* (0.0005719); p=0.0213; q=0.414 | -0.0003921 (0.0004693); p=0.403; q=0.791 | -0.0001758 (0.0004352); p=0.686; q=0.93 | -0.001064* (0.0004789); p=0.0263; q=0.414 | -0.0001345 (0.0004695); p=0.774; q=0.943 |
| Component: family_separation_flag | -1.838 (1.25); p=0.141; q=0.517 | -1.74 (1.428); p=0.223; q=0.585 | -1.312 (1.374); p=0.34; q=0.738 | 2.695 (1.439); p=0.0611; q=0.414 | -1.571 (2.141); p=0.463; q=0.837 |
| Component: parental_arrest_flag | -1.126 (0.8706); p=0.196; q=0.554 | 1.179 (0.7053); p=0.0945; q=0.473 | 0.2481 (0.9683); p=0.798; q=0.943 | 0.6996 (0.6669); p=0.294; q=0.686 | -0.4897 (0.8761); p=0.576; q=0.928 |
| Component: loyalty_conflict_flag | 0.1266 (0.9017); p=0.888; q=0.975 | 0.8072 (0.6187); p=0.192; q=0.554 | 1.051 (0.697); p=0.131; q=0.517 | 0.275 (0.6036); p=0.649; q=0.928 | -0.9095 (0.7113); p=0.201; q=0.554 |
| Component: segregation_flag | -0.8423 (0.8941); p=0.346; q=0.739 | -0.9249 (0.5988); p=0.122; q=0.517 | -0.8724 (0.5874); p=0.137; q=0.517 | 0.7998 (0.7012); p=0.254; q=0.628 | -0.7747 (0.748); p=0.3; q=0.688 |

#### PLR Joint Share Components

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | -0.005898 (0.01869); p=0.752; q=0.959 | -0.01228 (0.01746); p=0.482; q=0.827 | -0.05433 (0.02926); p=0.0633; q=0.34 | 0.051 (0.02936); p=0.0824; q=0.402 | 0.002928 (0.02264); p=0.897; q=0.996 | 0.01453 (0.02801); p=0.604; q=0.888 |
| Dosage: total_days_incarcerated | 6.341e-06 (1.096e-05); p=0.563; q=0.879 | -1.39e-05 (1.135e-05); p=0.221; q=0.659 | 1.74e-05 (2.384e-05); p=0.465; q=0.822 | -3.449e-06 (2.168e-05); p=0.874; q=0.996 | 2.363e-05 (2.245e-05); p=0.293; q=0.754 | -1.573e-05 (1.105e-05); p=0.155; q=0.56 |
| Component: family_separation_flag | -0.02255 (0.03428); p=0.511; q=0.848 | 0.02157 (0.03193); p=0.499; q=0.833 | 0.02004 (0.04035); p=0.619; q=0.888 | 0.04383 (0.05974); p=0.463; q=0.822 | -0.1119* (0.04509); p=0.0131; q=0.155 | 0.06263 (0.03724); p=0.0926; q=0.411 |
| Component: parental_arrest_flag | 0.01226 (0.02223); p=0.581; q=0.888 | -0.00074 (0.01293); p=0.954; q=0.996 | -0.0664 (0.0345); p=0.0542; q=0.32 | 0.03236 (0.03306); p=0.328; q=0.762 | 0.03804 (0.02887); p=0.188; q=0.617 | 0.002053 (0.01907); p=0.914; q=0.996 |
| Component: loyalty_conflict_flag | 0.02089 (0.01797); p=0.245; q=0.681 | -0.001702 (0.01357); p=0.9; q=0.996 | -0.07108* (0.03237); p=0.0281; q=0.229 | -0.04972 (0.02662); p=0.0618; q=0.34 | 0.04229 (0.0228); p=0.0636; q=0.34 | 0.05262** (0.01754); p=0.0027; q=0.0499 |
| Component: segregation_flag | -0.03938* (0.01635); p=0.016; q=0.161 | -0.009 (0.01658); p=0.587; q=0.888 | -0.01852 (0.03372); p=0.583; q=0.888 | 0.0439 (0.03235); p=0.175; q=0.598 | -0.02245 (0.01969); p=0.254; q=0.701 | 0.03882* (0.0171); p=0.0232; q=0.209 |

#### Track 2 Continuous Components

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing C: age_at_first_exposure | 0.004475 (0.009479); p=0.637; q=0.8 | 0.0177 (0.009329); p=0.0577; q=0.306 | 0.01801 (0.0176); p=0.306; q=0.661 |
| Dosage: total_days_incarcerated | 8.385e-06 (5.267e-06); p=0.111; q=0.43 | 3.979e-06 (5.802e-06); p=0.493; q=0.745 | -6.812e-06 (1.263e-05); p=0.59; q=0.8 |
| Component: family_separation_flag | -0.0001921 (0.01243); p=0.988; q=0.988 | -0.006493 (0.02438); p=0.79; q=0.927 | 0.02481 (0.02879); p=0.389; q=0.691 |
| Component: parental_arrest_flag | 0.009296 (0.00783); p=0.235; q=0.552 | 0.001151 (0.009038); p=0.899; q=0.949 | 0.01193 (0.02344); p=0.611; q=0.8 |
| Component: loyalty_conflict_flag | 0.01682** (0.006462); p=0.00923; q=0.0921 | -0.02835** (0.009767); p=0.0037; q=0.0667 | -0.008066 (0.01639); p=0.623; q=0.8 |
| Component: segregation_flag | 0.007873 (0.00584); p=0.178; q=0.477 | 0.02002* (0.008274); p=0.0156; q=0.105 | 0.02516 (0.01852); p=0.174; q=0.477 |

### 6.3 Rake

#### ILR Joint6 Components

| treatment | ilr_joint6_1 | ilr_joint6_2 | ilr_joint6_3 | ilr_joint6_4 | ilr_joint6_5 |
| --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | 0.5129 (1.252); p=0.682; q=0.93 | -0.1023 (0.4109); p=0.803; q=0.943 | 0.1858 (0.4583); p=0.685; q=0.93 | 0.2317 (0.4263); p=0.587; q=0.928 | 0.9523 (0.9818); p=0.332; q=0.734 |
| Dosage: total_days_incarcerated | 0.001 (0.0005727); p=0.0807; q=0.467 | -0.0002278 (0.0004845); p=0.638; q=0.928 | -0.0001052 (0.000456); p=0.817; q=0.945 | -0.001201* (0.0004809); p=0.0125; q=0.414 | 8.588e-05 (0.000459); p=0.852; q=0.958 |
| Component: family_separation_flag | -2.333* (1.153); p=0.0431; q=0.414 | -3.38* (1.353); p=0.0125; q=0.414 | -2.155 (1.122); p=0.0548; q=0.414 | 1.853 (1.308); p=0.157; q=0.517 | -2.489 (1.681); p=0.139; q=0.517 |
| Component: parental_arrest_flag | -1.152 (0.8277); p=0.164; q=0.517 | 1.059 (0.7326); p=0.148; q=0.517 | -0.06791 (0.926); p=0.942; q=0.978 | 0.9506 (0.6544); p=0.146; q=0.517 | -0.6941 (0.8602); p=0.42; q=0.791 |
| Component: loyalty_conflict_flag | -0.4796 (0.8035); p=0.551; q=0.925 | 1.034 (0.6639); p=0.119; q=0.517 | 0.6622 (0.631); p=0.294; q=0.686 | 0.3208 (0.6124); p=0.6; q=0.928 | -1.147 (0.6485); p=0.0768; q=0.467 |
| Component: segregation_flag | -0.05004 (0.8825); p=0.955; q=0.978 | -1.254 (0.6727); p=0.0624; q=0.414 | -1.029 (0.6082); p=0.0906; q=0.473 | 0.5457 (0.6773); p=0.42; q=0.791 | -0.6562 (0.7754); p=0.397; q=0.791 |

#### PLR Joint Share Components

| treatment | share_joint_Injury_composed | share_joint_Injury_discomposed | share_joint_Rupture_composed | share_joint_Rupture_discomposed | share_joint_Distrust_composed | share_joint_Distrust_discomposed |
| --- | --- | --- | --- | --- | --- | --- |
| Timing C: age_at_first_exposure | 0.003909 (0.02201); p=0.859; q=0.996 | -0.0005155 (0.009462); p=0.957; q=0.996 | -0.01079 (0.04115); p=0.793; q=0.985 | 0.0269 (0.02766); p=0.331; q=0.762 | -0.007694 (0.01387); p=0.579; q=0.888 | -0.01422 (0.03381); p=0.674; q=0.937 |
| Dosage: total_days_incarcerated | 4.841e-06 (1.241e-05); p=0.697; q=0.937 | -4.525e-06 (1.001e-05); p=0.651; q=0.924 | 2.59e-06 (2.452e-05); p=0.916; q=0.996 | -4.303e-06 (2.318e-05); p=0.853; q=0.996 | 2.958e-05 (2.44e-05); p=0.225; q=0.659 | -1.04e-05 (1.061e-05); p=0.327; q=0.762 |
| Component: family_separation_flag | -0.03431 (0.04028); p=0.394; q=0.8 | -0.03241 (0.03641); p=0.373; q=0.8 | 0.02821 (0.04104); p=0.492; q=0.831 | 0.09431 (0.06866); p=0.17; q=0.592 | -0.09777* (0.03893); p=0.012; q=0.152 | 0.07116* (0.03358); p=0.0341; q=0.256 |
| Component: parental_arrest_flag | -0.00309 (0.02108); p=0.883; q=0.996 | -0.004472 (0.01564); p=0.775; q=0.978 | -0.06017 (0.03517); p=0.0871; q=0.402 | 0.0576 (0.03365); p=0.0869; q=0.402 | 0.02605 (0.02757); p=0.345; q=0.776 | -0.0007747 (0.01883); p=0.967; q=0.996 |
| Component: loyalty_conflict_flag | 0.02348 (0.01727); p=0.174; q=0.598 | 0.0001515 (0.01493); p=0.992; q=0.996 | -0.05836 (0.03045); p=0.0553; q=0.32 | -0.04874 (0.02763); p=0.0777; q=0.402 | 0.03455 (0.02031); p=0.089; q=0.406 | 0.05683** (0.01783); p=0.00144; q=0.0328 |
| Component: segregation_flag | -0.038* (0.01755); p=0.0304; q=0.242 | -0.01164 (0.01617); p=0.472; q=0.823 | 0.006683 (0.03575); p=0.852; q=0.996 | 0.03237 (0.03357); p=0.335; q=0.763 | -0.01369 (0.01945); p=0.482; q=0.827 | 0.02184 (0.01828); p=0.232; q=0.666 |

#### Track 2 Continuous Components

| treatment | authority_stance | belonging_stance | how_multimodal_score_mean |
| --- | --- | --- | --- |
| Timing C: age_at_first_exposure | -0.0006428 (0.005968); p=0.914; q=0.949 | 0.01731 (0.01155); p=0.134; q=0.475 | 0.00267 (0.01778); p=0.881; q=0.949 |
| Dosage: total_days_incarcerated | 9.52e-06 (5.106e-06); p=0.0623; q=0.306 | -7.249e-07 (6.248e-06); p=0.908; q=0.949 | -1.068e-05 (1.241e-05); p=0.389; q=0.691 |
| Component: family_separation_flag | 0.004849 (0.01427); p=0.734; q=0.899 | 0.008471 (0.0265); p=0.749; q=0.899 | 0.02667 (0.02744); p=0.331; q=0.687 |
| Component: parental_arrest_flag | 0.01097 (0.007445); p=0.141; q=0.475 | 0.01283 (0.009653); p=0.184; q=0.477 | 0.01776 (0.02151); p=0.409; q=0.691 |
| Component: loyalty_conflict_flag | 0.01649** (0.006345); p=0.00934; q=0.0921 | -0.02339* (0.009109); p=0.0102; q=0.0921 | 0.002766 (0.01673); p=0.869; q=0.949 |
| Component: segregation_flag | 0.005534 (0.006356); p=0.384; q=0.691 | 0.02753** (0.009384); p=0.00335; q=0.0667 | 0.01563 (0.01895); p=0.409; q=0.691 |

## 7. Narrative interpretation

Across the main treatment block, broad binary timing remains weak under BH correction. In the unweighted specification, `authority_stance <- adolescent_exposure_flag` is -0.03692 (p=0.655, q=0.956), while `share_joint_Distrust_discomposed <- adolescent_exposure_flag` is -0.04708 (p=0.805, q=0.981). These rows do not provide corrected evidence for a stable adolescent-dummy effect.

The corrected signal is more concentrated in aggregate severity than in timing or dosage. For `authority_stance <- severity_index_v2`, the three weighting schemes are Unweighted 0.02147 (p=0.0373, q=0.201), IPW 0.04091 (p=0.00134, q=0.029), Rake 0.03815 (p=0.00709, q=0.085). For `share_joint_Distrust_discomposed <- severity_index_v2`, the corresponding rows are Unweighted 0.07878 (p=0.00604, q=0.0984), IPW 0.1393 (p=0.00168, q=0.0446), Rake 0.1287 (p=<0.001, q=0.0332). This keeps the main causal readout centered on severity rather than on a broad timing contrast.

Within the severity decomposition, `loyalty_conflict_flag` remains the dominant component once q-values are reported explicitly. For `authority_stance <- loyalty_conflict_flag`, the rows are Unweighted 0.01818 (p=<0.001, q=0.0391), IPW 0.01682 (p=0.00923, q=0.0921), Rake 0.01649 (p=0.00934, q=0.0921). For `share_joint_Distrust_discomposed <- loyalty_conflict_flag`, the rows are Unweighted 0.02888 (p=0.0323, q=0.251), IPW 0.05262 (p=0.0027, q=0.0499), Rake 0.05683 (p=0.00144, q=0.0328). By comparison, the Track 2 BH-retained row counts are 0 for `family_separation_flag`, 0 for `parental_arrest_flag`, 1 for `loyalty_conflict_flag`, and 0 for `segregation_flag`, which keeps the decomposition story centered on the loyalty-conflict channel.

## 8. Source files

- `scripts/build_causal_readout_memo_v2.py`
- `models/causal_estimates_v1/track1_ilr_v1/track1_ilr_estimates_v1.csv`
- `models/causal_estimates_v1/track1_per_cell_v1/track1_per_cell_estimates_v1.csv`
- `models/causal_estimates_v1/track2_v1/track2_estimates_v1.csv`
- `models/causal_estimates_v1/track1_ilr_severity_components_v1/track1_ilr_severity_components_estimates_v1.csv`
- `models/causal_estimates_v1/track1_per_cell_severity_components_v1/track1_per_cell_severity_components_estimates_v1.csv`
- `models/causal_estimates_v1/track2_severity_components_v1/track2_severity_components_estimates_v1.csv`
