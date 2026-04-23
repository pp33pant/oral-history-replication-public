# Online Appendix: Robustness Checks

This appendix reports the broader robustness checks for the baseline narrator-level specifications. Two patterns survive the largest share of the battery. First, the severity index remains positively associated with authority stance and with the joint distrust-discomposure outcome. Second, the broad binary timing indicator remains weaker and more specification-sensitive. For readability, the discussion below uses paper labels rather than machine-readable variable labels.

## 1. Alternative Estimators, Weighting, and Support Restrictions

The first set of checks asks whether the baseline results depend on nuisance learner choice, cross-fitting splits, treatment coding, overlap enforcement, or weighting. Across these checks, the authority-side and distrust-side severity results are stable in sign and generally stable in magnitude. What changes more often are timing contrasts and several secondary outcomes, especially on the belonging side.

Learner sensitivity and cross-fitting are the cleanest checks in this group. Across learners, the main severity rows remain positive and close in magnitude to the baseline, while timing estimates are more likely to weaken or flip sign. Changing the number of folds produces even less movement. Together, these results indicate that the main severity pattern is not an artifact of one nuisance-model configuration or one cross-fitting partition.

The remaining checks are more substantively informative. Disaggregating the severity bundle shows that no single component reproduces the full composite pattern by itself, although loyalty conflict is a recurring contributor on both authority stance and the joint distrust-discomposure outcome. Overlap trimming changes some magnitudes, but the main severity rows remain positive across weighting schemes. Likewise, moving between inverse-probability weighting, raking, and unweighted estimation does not alter the central authority-side and distrust-side severity pattern, even though secondary belonging and rupture outcomes are less uniform.

### Table A1. Estimation and specification checks

| Check | Alternative specification | Headline evidence | Interpretation |
| --- | --- | --- | --- |
| R1 | Learner sensitivity | Same-sign rate 83.7%; median absolute drift $2.339 \times 10^{-5}$; severity on authority stance moves from 0.0409 in the baseline to 0.0547 under lasso and 0.0499 under random forest; severity on joint distrust-discomposure moves from 0.1393 to 0.1549 and 0.1316 | The main severity pattern is not driven by one learner choice; timing is less stable |
| R2 | Cross-fit folds | Same-sign rate 90.1%; median absolute drift $8.143 \times 10^{-6}$; severity rows remain within very narrow ranges across 3-, 5-, and 10-fold estimation | The main severity pattern is not driven by one fold partition |
| R3 | Treatment discretization | Loyalty conflict remains positive on authority stance and on the joint distrust-discomposure outcome across all three weight schemes; other severity components are weaker and less systematic | The composite severity index captures cumulative burden rather than a single isolated component |
| R4 | Overlap trimming | Sample falls to 561-562 observations; same-sign rate 76.5%; median absolute drift 0.008948; the main severity rows remain positive across weights | Support restriction changes magnitudes, but not the core authority/distrust conclusion |
| R5 | Weight specification | Across IPW, rake, and unweighted estimation, severity remains positive on authority stance and on the joint distrust-discomposure outcome | The main severity result is weighting-robust; secondary outcomes are less uniform |

## 2. Outcome Definition, Measurement, and Cross-Track Agreement

The second group of checks asks whether the main conclusions depend on classification boundaries, aggregation rules, minority-signal cells, dimensionality choices, or the relation between Track 1 and Track 2. The general pattern is that the measurement system is not arbitrary, but some margins are more stable than others. Authority/distrust and discomposure are better identified than the finer distinction between rupture and distrust, and they are also more stable than the belonging-side contrasts.

The boundary-sensitivity exercise is the clearest example. Around the baseline cutpoint, small changes in one boundary parameter leave the class shares unchanged, while moving the high-side cutpoint shifts observations between rupture and distrust. This suggests that the baseline classification is not perched on an unstable knife-edge, but it also shows why the fine rupture-versus-distrust split should remain an appendix-level result rather than a heavily emphasized headline claim.

The remaining checks reinforce this pattern. Alternative aggregation is a hard stress test because it sharply reduces the effective sample and changes the analysis unit; its mixed performance therefore speaks more to estimand and sample changes than to a routine robustness failure. By contrast, the minority-signal and ILR dimensionality checks do not overturn the main interpretation. The Track 1 / Track 2 audit is strongest for authority/distrust and discomposure-linked constructs, and noticeably weaker for belonging-side contrasts. That is the right way to summarize measurement robustness in this setting: strong on the principal authority and distrust dimensions, weaker on finer compositional and belonging-side margins.

### Table A2. Outcome-definition and measurement checks

| Check | Alternative specification | Headline evidence | Interpretation |
| --- | --- | --- | --- |
| R6 | Boundary sensitivity | Baseline upper and lower cutpoints are 0.54 and 0.43; baseline shares are 36.8% Injury, 50.0% Rupture, and 13.2% Distrust; lowering the upper cutpoint to 0.53 moves 7 percentage points from Rupture to Distrust | The baseline boundary is locally stable, but fine rupture-versus-distrust allocation is threshold-sensitive |
| R7 | Alternative aggregation | Effective analysis falls to 31 narrators; same-sign rate 54.0%; median absolute drift 0.01106 | This is a demanding stress test, but too disruptive to replace the preferred narrator-level design |
| R8 | Minority-signal outcomes | Same-sign rate 100%; zero coefficient drift on the highlighted baseline rows | The main severity pattern does not depend on dropping low-frequency outcome cells |
| R9 | ILR dimensionality | 63 rows; 7 raw $p<0.05$ rows; no headline contradiction identified in the review | The dimensionality choice does not force a revised interpretation |
| Track 1 / Track 2 audit | Meaning-consistency comparison | 216 rows total; 130 same-sign and 86 opposite-sign rows overall; strongest agreement for authority/distrust and discomposure constructs | Cross-track support is strongest for authority/distrust and discomposure, and weaker for belonging-side contrasts |

## 3. Identification, Placebo, and Leverage Checks

The third set of checks asks whether the main severity result survives omitted-confounding diagnostics, component decomposition, an interview-level reformulation, sequential orthogonalization, placebo assignments, and leave-one-camp-out re-estimation. These checks do not overturn the main conclusion, but they do narrow the language that can be used to describe it.

The omitted-confounding analysis is the most important caution. The main severity rows are not trivial, but they are not immune to omitted-variable concerns. The appropriate conclusion is not that the design is invulnerable, but that the strongest severity rows have non-negligible robustness values and remain economically meaningful under several other stress tests.

The rest of the battery is more reassuring. The exogenous-severity exercise shows that the distrust-side pattern does not disappear when the severity bundle is decomposed, although no single component reproduces the full composite result. Sequential DML leaves the coefficient surface almost unchanged. Leave-one-camp-out changes some magnitudes, but does not reduce the main authority-side or distrust-side severity result to a single-site artifact. By contrast, the interview-level long-format specification is too small and too unstable to serve as a preferred alternative, and the placebo exercise is supportive but mixed rather than uniformly dispositive.

### Table A3. Identification and leverage checks

| Check | Alternative specification | Headline evidence | Interpretation |
| --- | --- | --- | --- |
| R10 | Omitted-confounding sensitivity | Median $RV_{q=1}$ across the panel is 3.2%; the authority-stance severity row has $RV_{q=1}=0.1199$; the joint distrust-discomposure severity row has $RV_{q=1}=0.1176$ | The main severity rows are non-trivial, but not invulnerable to omitted confounding |
| R11 | Exogenous severity components | Total days incarcerated remains positive on authority stance with $p \approx 0.007$ to 0.008 across weights; family separation remains positive on the joint distrust-discomposure outcome and reaches significance in the unweighted fit | The main severity index is not reducible to one component, but the distrust-side pattern is not purely a compositional artifact |
| R12 | Interview-level long format | 37 interview observations representing 31 narrators; same-sign rate 52.4% | The interview-level reformulation is too unstable and low-power to replace the narrator-level design |
| R13 | Sequential DML | 27 rows; same-sign rate 96.3%; median absolute drift about 0.00075 | The main coefficient surface is essentially unchanged under sequential orthogonalization |
| R14 | Placebo permutations | 45 rows; 21 rows with empirical $p<0.05$ | The placebo exercise is supportive but mixed, not a universal pass/fail test |
| R15 | Leave-one-camp-out | 243 rows; same-sign rate 74.9%; median absolute drift 0.006656 | Magnitudes are leverage-sensitive, but the main severity result is not a single-site artifact |

## 4. Selection, Observability, and Scope

Selection checks matter most for two reasons. First, the baseline results should not be an artifact of recovered missingness handling. Second, the How dimension is more vulnerable than the What outcomes to archiveability and narratability concerns. The evidence in this section supports the first point clearly and the second point only partially.

The complete-case rerun preserves the main severity pattern. In the reduced sample, severity remains positive on authority stance and on the joint distrust-discomposure outcome across all three weighting schemes, while timing remains weak. This is strong evidence that the main severity result does not depend on recovered-unknown handling.

The frozen How diagnostics are more informative than the earlier archived note, but they remain mixed rather than exculpatory. Adolescent exposure predicts a lower gap rate ($p=0.015$), and dosage predicts shorter mean segment length ($p=0.0037$), so some treatment variation co-moves with technical proxies. The trauma-versus-casual segment contrast is also not in the direction of a trauma-only discomposure story: trauma segments score about 0.008 lower on the multimodal How measure ($p=0.0147$). At the same time, the base adolescent-exposure-to-How coefficient is small, and the interview-id residualization check strengthens rather than erases the negative association. The observability and MNAR modules are now frozen as companion outputs: 430 of 642 narrators satisfy the current observability rule; mean observed $\hat p(R_{how}=1)$ is 0.712; stabilized IPO weights trim at 1.548; the delta-adjusted simple How ATE stays near $-0.020$ through $\delta=1.5$; and the Lee bound is about $-0.030$. A companion difficult-cases appendix panel is also frozen as an export layer rather than a human-verdict summary, with 69 narrators split into 25 high-discomposure, 25 boundary-uncertain, and 19 technically poor but flagged cases. The right scope condition is therefore explicit rather than deferred: the How findings remain interpretable for the observed archiveable narrator population, but they should not be overstated as if the negative-control and observability layers had fully closed narratability concerns.

### Table A4. Selection and observability checks

| Check | Alternative specification | Headline evidence | Interpretation |
| --- | --- | --- | --- |
| R16 | Recovered complete-case rerun | $N=564$; severity on authority stance equals 0.049, 0.048, and 0.042 across IPW, rake, and unweighted estimation, all with $p<0.001$; severity on the joint distrust-discomposure outcome equals 0.103, 0.106, and 0.090 | The main severity result is not driven by recovered-missingness handling |
| Frozen How negative controls | Treatment-to-noise, non-trauma contrast, and interview-id absorption | Adolescent exposure predicts a lower gap rate ($p=0.015$); dosage predicts shorter mean segment length ($p=0.0037$); trauma-minus-casual multimodal How equals about $-0.008$ ($p=0.0147$); interview-id residualization leaves the coefficient negative at $-0.018$ ($p=0.0024$) | Negative controls do not support a pure interviewer-artifact account, but they are not clean nulls |
| Difficult-cases appendix panel | Frozen panel export | 69 narrators exported: 25 high-discomposure, 25 boundary-uncertain, and 19 technically poor but flagged, each with a segment package | Frozen as a diagnostic appendix panel without relying on a human-verdict summary |
| Scope condition | Observed archiveable sample plus observability/MNAR sensitivity | 430 of 642 narrators satisfy the current observability rule; mean observed $\hat p(R_{how}=1)$ is 0.712; stabilized IPO weights trim at 1.548; the delta-adjusted simple How ATE stays near $-0.020$ through $\delta=1.5$; the Lee bound is about $-0.030$ | The How findings should remain scoped to the observed archiveable narrator population |

## 5. Extensions and Heterogeneity

The frozen robustness archive does not report a separate demographic subgroup battery. In this appendix, the extension layer is instead represented by the older embedding arm, interview-year interaction checks, and the composure-only specification. None of these checks displaces the baseline interpretation.

The embedding arm is explicitly exploratory. It is based on a much smaller sample, it does not align closely with the baseline coefficients, and it should not be treated as a competing measurement system. Interview-year moderation is also weak: it does not convert the timing result into a robust moderated pattern. By contrast, isolating composure leaves the main How interpretation unchanged, which is reassuring because it shows that the How pattern is not mechanically generated by bundling composure together with the broader What-by-How structure.

### Table A5. Extensions and related checks

| Check | Alternative specification | Headline evidence | Interpretation |
| --- | --- | --- | --- |
| R17 | Embedding arm versus baseline language-model arm | 31 observations; same-sign rate 46.7%; median absolute drift about 0.02048 | The embedding arm is exploratory and too unstable to adjudicate the main results |
| R18 | Interview-year interaction | Headline adolescent-by-interview-year rows remain weak or non-significant across the displayed baseline outcomes | Expressive-environment moderation does not rescue the weak timing result |
| R19 | Composure-separate model | 72 rows; same-sign rate 100%; zero median drift on the highlighted How rows | The How interpretation survives a cleaner composure-only specification |

## 6. Overall Interpretation

Taken together, the robustness battery supports a bounded conclusion. Severity is the most stable treatment dimension in the current design, especially for authority stance and for the joint distrust-discomposure outcome. Timing remains weaker and more specification-sensitive. Belonging-side interpretation is more fragile than authority-side interpretation, particularly once the analysis turns to alternative aggregation and cross-track comparison. The How dimension remains directionally supportive, but it continues to require narrower scope language because selection and narratability concerns are not fully resolved by the currently available diagnostics.

That is the most defensible summary of the appendix evidence. The battery does not overturn the paper's central result, but it does discipline how strongly each part of the argument can be stated.

## 7. Check-by-Check Direct-Evidence Inventory

Because the online appendix is not page-constrained, this final section reports the robustness battery again in itemized form. Tables A6-A8 are deliberately selective rather than exhaustive. For each robustness check, they report only the most informative within-check statistics, such as same-sign rates, median drift, or sample changes when those quantities are available, together with one focal row or row contrast that anchors the interpretation. The full coefficient inventory remains in the source result table listed in the second column.

### Table A6. Selected key rows and within-check statistics for R1-R6

| Check | Full result table | Key rows and within-check statistics | Reading |
| --- | --- | --- | --- |
| R1 | `robustness/causal_robustness_probe_v1/r1/r1_learner_sensitivity_v1.csv` | Same-sign rate 83.7%; median absolute drift $2.339 \times 10^{-5}$; focal row: IPW authority-stance severity = 0.0409 in the baseline, 0.0547 under lasso, and 0.0499 under random forest | Learner choice does not overturn the main severity pattern |
| R2 | `robustness/causal_robustness_v2/r2/r2_crossfit_folds_v1.csv` | Same-sign rate 90.1%; median absolute drift $8.143 \times 10^{-6}$; focal row: IPW authority-stance severity = 0.0409 in the 5-fold baseline, 0.0387 in the 3-fold fit, and 0.0411 in the 10-fold fit | Cross-fitting partitions have negligible effects on the principal severity rows |
| R3 | `robustness/causal_robustness_v2/r3/r3_treatment_discretization_v1.csv` | Focal rows: loyalty conflict on authority stance = 0.0155 (`p=0.016`), 0.0162 (`p=0.012`), and 0.0185 (`p<0.001`) across IPW, rake, and unweighted fits; on joint distrust-discomposure = 0.0507 (`p=0.003`), 0.0559 (`p=0.001`), and 0.0297 (`p=0.029`) | Loyalty conflict is a recurrent contributor, but no single severity component reproduces the full composite pattern |
| R4 | `robustness/causal_robustness_v2/r4/r4_overlap_trimming_v1.csv` | Same-sign rate 76.5%; median absolute drift 0.008948; trimmed sample falls to 561-562 observations; focal result: the highlighted severity rows remain positive after overlap trimming | Support restriction moves magnitudes, but does not reverse the core authority/distrust result |
| R5 | `robustness/causal_robustness_v2/r5/r5_weight_specification_v1.csv` | Focal rows: authority-stance severity = 0.0409 under IPW, 0.0381 under rake, and 0.0215 unweighted; joint distrust-discomposure severity = 0.1393, 0.1287, and 0.0788 | The authority-side and distrust-side severity pattern survives reweighting; belonging remains less robust |
| R6 | `robustness/causal_robustness_v2/r6/r6_boundary_sensitivity_v1.csv` | Focal threshold contrast: baseline cutpoints 0.54 and 0.43 imply 36.8% Injury, 50.0% Rupture, and 13.2% Distrust; lowering the upper cutpoint to 0.53 moves Rupture to 43.0% and Distrust to 20.2% | The baseline boundary is locally stable, but the fine Rupture-versus-Distrust split is threshold-sensitive |

### Table A7. Selected key rows and within-check statistics for R7-R12

| Check | Full result table | Key rows and within-check statistics | Reading |
| --- | --- | --- | --- |
| R7 | `robustness/causal_robustness_v2/r7/r7_alternative_aggregation_v1.csv` | Same-sign rate 54.0%; median absolute drift 0.01106; focal contrast: authority-stance severity stays positive at 0.0469, 0.0680, and 0.0494 across weights, while How severity turns negative under rake and unweighted aggregation | Alternative aggregation is a severe estimand-and-sample change rather than a routine replacement for the preferred narrator-level design |
| R8 | `robustness/causal_robustness_v2/r8/r8_minority_signal_v1.csv` | Same-sign rate 100.0%; median absolute drift 0; focal row: joint distrust-discomposure severity remains 0.1393 under IPW, 0.1287 under rake, and 0.0788 unweighted, with zero drift relative to the reference rows | The headline severity pattern does not depend on dropping minority-signal outcome cells |
| R9 | `robustness/causal_robustness_v2/r9/r9_ilr_dimensionality_v1.csv` | 7 raw `p<0.05` rows; focal rows fall on latent basis coordinates rather than paper-facing outcomes, for example rake `ilr_joint6_5` severity = -3.611 (`p=0.013`) and IPW `ilr_joint6_4` severity = 2.843 (`p=0.043`) | Changing ILR dimensionality redistributes signal across latent coordinates, but does not generate a paper-facing contradiction on the main authority/distrust margins |
| R10 | `robustness/causal_robustness_v2/r10/r10_unobserved_confounding_sensitivity_v1.csv` | Median $RV_{q=1}$ across the panel is 3.2%; focal rows: IPW authority-stance severity has $RV_{q=1}=0.1199$ and $RV_{q=1,\alpha=0.05}=0.0482$, while the joint distrust-discomposure severity row has 0.1176 and 0.0458 | The strongest severity rows are non-trivial, but they are not immune to omitted confounding |
| R11 | `robustness/causal_robustness_probe_v1/r11/r11_exogenous_severity_only_v1.csv` | Focal rows: total days incarcerated on authority stance = 0.000014 (`p=0.0075`), 0.000014 (`p=0.0073`), and 0.000010 (`p=0.0082`); family separation on joint distrust-discomposure = 0.0570 (`p=0.133`), 0.0655 (`p=0.0589`), and 0.0662 (`p=0.0459`) | The distrust-side result does not disappear when severity is decomposed, but no single component fully substitutes for the composite severity index |
| R12 | `robustness/causal_robustness_v2/r12/r12_interview_long_format_v1.csv` | Same-sign rate 52.4%; sample is only 37 interviews representing 31 narrators; focal contrast: IPW authority-stance severity = 0.0724 (`p=0.015`), while rake How severity = -0.2120 (`p=0.010`) | The interview-level reformulation is too small and too unstable to replace the narrator-level analysis |

### Table A8. Selected key rows and within-check statistics for R13-R19

| Check | Full result table | Key rows and within-check statistics | Reading |
| --- | --- | --- | --- |
| R13 | `robustness/causal_robustness_v2/r13/r13_sequential_dml_v1.csv` | Same-sign rate 96.3%; median absolute drift 0.0007495; focal row: authority-stance timing = 0.0052 under sequential DML versus 0.0064 in the baseline unweighted fit | Sequential orthogonalization leaves the timing surface essentially unchanged |
| R14 | `robustness/causal_robustness_v2/r14/r14_placebo_permutation_summary_v1.csv` | 21 empirical `p<0.05` rows; focal contrast: authority-stance placebo `p`-values are 0, 0, and 0 across weights for age at first exposure, whereas How severity placebo `p`-values are 0.3125, 0.375, and 0.625 | The placebo exercise is supportive for the strongest authority-side rows, but mixed elsewhere |
| R15 | `robustness/causal_robustness_v2/r15/r15_leave_one_camp_out_v1.csv` | Same-sign rate 74.9%; median absolute drift 0.006656; focal row: IPW authority-stance severity = 0.0362 without Minidoka, 0.0363 without Manzanar, and 0.0628 without Tule Lake | Facility leverage changes magnitudes, but the main severity result is not a single-site artifact |
| R16 | `robustness/causal_robustness_probe_v1/r16/r16_complete_case_v1.csv` | `N=564`; focal rows: authority-stance severity = 0.0492, 0.0484, and 0.0424 across IPW, rake, and unweighted estimation, all with `p<0.001`; joint distrust-discomposure severity = 0.1026 (`p=0.0167`), 0.1059 (`p=0.0114`), and 0.0895 (`p=0.0089`) | The main severity result is not driven by recovered-missingness handling |
| R17 | `robustness/causal_robustness_probe_v1/r17/r17_embedding_arm_v1.csv` | Same-sign rate 46.7%; median absolute drift 0.02048; focal rows sit on embedding-specific outcomes, including IPW `embed_share_Injury` severity = 0.0268 (`p=0.0012`) and rake `embed_ilr_what_1` severity = 0.0831 (`p=0.0034`) | The embedding arm carries its own signal, but aligns too weakly with the baseline arm to adjudicate the main results |
| R18 | `robustness/causal_robustness_v2/r18/r18_interview_year_interaction_v1.csv` | 74 raw `p<0.05` rows overall; focal interaction rows on paper-facing outcomes are weak, with IPW authority stance = 0.0231 (`p=0.790`), unweighted How = 0.1074 (`p=0.666`), and unweighted joint distrust-discomposure = 0.1240 (`p=0.188`) | Interview-year moderation does not rescue the weak timing result |
| R19 | `robustness/causal_robustness_probe_v1/r19/r19_composure_separate_v1.csv` | Same-sign rate 100.0%; median absolute drift 0; focal result: the displayed How coefficients have zero delta relative to the reference rows across IPW, rake, and unweighted estimation | The composure-only re-estimation leaves the How results unchanged |