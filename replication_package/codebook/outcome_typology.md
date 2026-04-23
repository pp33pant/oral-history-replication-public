# Outcome Typology: Refinement Discussion and Design Decisions

> **Date**: 2026-04-14 (v2 boundary revision)
> **Status**: Working reference for the current GPT-5.4 text-stage outcome system
> **Relates to**: README.md § Outcome Framework, `appendix/what_dimension_pipeline_freeze_v2.md`, `data/processed/video_first_post_vm_batch1_v2/`
> **Change log**: v2 (2026-04-14) revised x1 high cut 0.65→0.54, x2 cut 0.45→0.43, and merge map. See §2.4 for rationale. v1 boundaries archived in §2.5.

---

## 1. Clarification of the What-Axis: Two Latent Dimensions

The three what-axis categories — `authority_schema_injury`, `shame_mediated_identity_rupture`, and `explicit_political_distrust` — are not defined by surface-level narrative topic (e.g., "talks about government" vs "talks about discrimination" vs "talks about activism"). They are defined by the narrator's **position on two underlying latent dimensions**: authority-stance and belonging-stance. These two dimensions draw on the distinction between specific and diffuse political support (Easton 1965, 1975) and on layered political-trust architectures (van der Meer and Zmerli 2017; Norris 2011).

### 1.1 The Two Latent Dimensions

| Category | Reader label | Authority-stance | Belonging-stance |
|---|---|---|---|
| `authority_schema_injury` | Injury | Authority = **protector** (still trusted normatively; betrayal precisely because protection was expected) | **Still belonging** (narrator identifies as member of the polity) |
| `shame_mediated_identity_rupture` | Rupture | **Indifferent** toward authority (authority is no longer the central reference point) | **Partial or no belonging** (damaged membership, outsider status) |
| `explicit_political_distrust` | Distrust | Authority = **enemy** (explicitly adversarial political object) | **Opposite belonging** (oppositional, alienated, or claim-making against the state) |

### 1.2 Why This Matters for Classification

The category names — injury, rupture, distrust — emphasize the *form of relational damage*, not the narrative topic. The most important classification discriminant is therefore:

- **Injury**: specific distrust coexisting with retained belonging (cf. Easton 1975 on specific versus diffuse support). The narrator still operates within a frame where authority *should have* protected. The betrayal is intelligible precisely because the protection expectation remains intact.
- **Rupture**: indifference toward authority combined with partial or absent belonging. The narrator is no longer centrally engaged with whether the state failed or succeeded as protector. The injury has migrated to the identity and membership layer.
- **Distrust**: authority as enemy, with general (not specific) distrust and oppositional or alienated belonging (Bertsou 2019; Hooghe 2011). The narrator has moved to an explicitly political stance toward the state as an adversarial object.

This three-way distinction cannot be reduced to a severity scale. A narrator in the injury category may be extremely angry but still locate the state within a protection frame. A narrator in the rupture category may appear less politically articulate but carry a deeper wound to membership and selfhood. A narrator in the distrust category may be highly composed and engaged but has fundamentally repositioned the state as an adversary.

### 1.3 Relationship Between Latent Dimensions and the Three Categories

The three classes occupy distinct but connected regions in the two-dimensional (authority-stance × belonging-stance) space:

```
                    Belonging
            still ←————————————→ opposite/alienated
Authority     |                       |
protector     |   INJURY              |
              |     (specific trust   |
              |      + belonging)     |
              |                       |
indifferent   |          RUPTURE      |
              |     (indifference     |
              |      + partial/no     |
              |        belonging)     |
              |                       |
enemy         |               DISTRUST|
              |          (enemy +     |
              |           opposite    |
              |           belonging)  |
```

The three categories are positioned roughly along a diagonal in this space: from (protector, belonging) through (indifferent, partial) to (enemy, opposite). This diagonal structure is what makes the ordered-continuum hypothesis plausible — but the two dimensions need not always co-vary, which is what the parallel-dimensions alternative model tests.

---

## 2. The Rupture Absorption Problem

### 2.1 Why Rupture Dominates Empirically

In the current 37-interview, 492-segment dataset (see `appendix/descriptive_stats.md`), all classification methods (cosine-prototype, LLM, supervised probe) assign 70-95% of segments to the rupture/shame category at the segment level, and 85-97% at the interview level (argmax-dominant).

This is not solely a classifier failure. It reflects a structural property of the corpus:

1. **Narrative default mode**: Most Densho oral history testimony describes the experience of incarceration in concrete, experiential terms — childhood memories, camp daily life, community disruption, post-war return. This language, by its nature, sits in the rupture zone: the narrator is neither explicitly framing the state as a failed protector (injury) nor making an explicitly political argument (distrust). The default is indifference toward authority combined with partial belonging disruption.

2. **Content distribution**: Segments covering childhood, family background, school life, community activities, and daily camp routines constitute 60-70% of a typical interview. These segments do not clearly signal either the "state should have protected us" frame (injury) or the "state is an adversary" frame (distrust). They default to rupture.

3. **Residual category function**: In operational terms, rupture functions as the residual category — anything not clearly injury or distrust falls here. This is theoretically defensible (the middle register is defined by what it lacks: neither a protection frame nor an adversarial political frame) but empirically problematic (it absorbs too much variance).

### 2.2 Is Rupture a Valid Single Category?

The theoretical definition of rupture is clear: indifference toward authority + partial/no belonging. But the empirical content classified as rupture is heterogeneous. Under the current 160-character summary text regime, the following all get classified as rupture:

- A narrator describing deep shame about hiding Japanese identity for decades (deep identity wound)
- A narrator matter-of-factly describing camp school and recreational activities (adaptive coping within disruption)
- A narrator describing post-war community rebuilding (partial belonging restoration)
- A narrator describing family dynamics and childhood memories (pre-incarceration context)

These represent very different positions within the rupture space.

### 2.3 Potential Subdivision of Rupture

If rupture is to be subdivided, the most theoretically grounded cut follows the belonging-stance dimension:

| Subcategory | Belonging position | Typical expression |
|---|---|---|
| **Adaptive rupture** | Partial belonging — community bonds maintained, life rebuilt within the disruption | Camp community life, post-war rebuilding, "we made the best of it," new friendships and institutions within confinement |
| **Deep rupture** | Minimal or no belonging — lasting damage to membership and selfhood | Hiding identity, lasting shame, feeling like an outsider in both Japanese and American communities, inability to discuss the experience |

This subdivision has clear theoretical warrant: the two sub-positions predict different downstream trajectories and should respond differently to treatment channels (dosage is expected to push adaptive → deep; severity is expected to push toward deep directly). Developmental stigma research (Goffman 1963; Link and Phelan 2001; Thoits 2011) supports the expectation that deeper rupture is associated with lasting identity damage rather than adaptive accommodation.

Under the old 160-character summary regime, operationalizing this distinction required richer text input than the summaries could provide. Under the current GPT-5.4 full-transcript run, the adaptive/deep rupture distinction is approximated through the v2 6-region boundary grid (§2.4) using narrator-level continuous scores.

**Current decision**: Retain the three-class what-axis (injury, rupture, distrust) as the active taxonomy. The adaptive/deep rupture distinction is operationalised through the v2 6-region boundary grid (§2.4) using GPT-5.4 fulltext continuous scores.

### 2.4 v2 Boundary Placement (2026-04-14): Fixing the Rupture Absorption Problem

The v1 boundary scheme (x1 cuts at 0.50/0.65, x2 cut at 0.45) produced a severely imbalanced 3-class distribution: Injury=506 (78.8%), Rupture=125 (19.5%), Distrust=11 (1.7%). The Distrust class was too small to model; the Rupture class was dominated by a single region (`default_rupture`); and `adaptive_rupture` was merged into Injury, collapsing meaningful between-narrator variation.

**Root cause**: The v1 x1 high cut at 0.65 was too aggressive. Fine-grained histogram analysis (0.01 bins) of the full N=642 narrator corpus revealed:

- **x1 density peak** at [0.50, 0.51) with 126 narrators (19.6%), and 47.8% of all narrators in x1∈[0.49, 0.52).
- **Natural density break at x1≈0.54**: 43 narrators in [0.53, 0.54) drops to 15 in [0.54, 0.55), a −65% decline. This is the largest proportional drop in the entire x1 range and corresponds to the transition from "mid-range ambiguity" to "clear enemy-leaning stance."
- **x2 density plateau** from [0.37, 0.47) with no sharp natural break; the x2=0.43 cut sits at the lower edge of this plateau and produces balanced 6-region cells within the Rupture band.

**v2 boundary constants**:

| Parameter | v1 | v2 | Rationale |
|---|---|---|---|
| `X1_CUT_LOW` | 0.50 | 0.50 | Theoretical midpoint of protector–enemy scale; retained |
| `X1_CUT_HIGH` | 0.65 | **0.54** | Natural density break (−65% drop); separates ambiguous mid-range from clear enemy-leaning |
| `X2_CUT` | 0.45 | **0.43** | Balances 6-region cells; lower edge of x2 plateau |

**v2 6-region distribution** (N=642 narrators; current production file):

| | x2 < 0.43 | x2 ≥ 0.43 | Total |
|---|---|---|---|
| x1 < 0.50 | injury: 199 | injury_disrupted: 37 | 236 |
| x1 ∈ [0.50, 0.54) | adaptive_rupture: 167 | default_rupture: 154 | 321 |
| x1 ≥ 0.54 | politicizing_rupture: 46 | distrust: 39 | 85 |

**v2 3-class merge map** (critical change from v1):

| 3-class | v1 composition | v2 composition |
|---|---|---|
| **Injury** | injury + injury_disrupted + adaptive_rupture | injury + injury_disrupted |
| **Rupture** | default_rupture | adaptive_rupture + default_rupture |
| **Distrust** | politicizing_rupture + distrust | politicizing_rupture + distrust |

**v2 3-class distribution** (N=642; current production file):

| 3-class | n | % |
|---|---|---|
| Injury | 236 | 36.8% |
| Rupture | 321 | 50.0% |
| Distrust | 85 | 13.2% |

The v2 scheme resolves the Rupture Absorption Problem: Injury drops from 78.8%→36.8%, Rupture increases from 19.5%→50.0% (now the proper residual/middle category), and Distrust increases from 1.7%→13.2% (fully modelable).

The current production outputs are stored in `data/processed/video_first_post_vm_batch1_v2/narrator_llm_fulltext_2d_outcomes_v2.csv` and aligned interview / segment tables in the same directory.

**Executed sensitivity-grid result**: the 3×3 boundary grid (`x1_high ∈ {0.53, 0.54, 0.55}`, `x2_cut ∈ {0.41, 0.43, 0.45}`) has already been run. The maximum single-class shift is 7.0 percentage points, which is below the 10 pp working tolerance; `x2_cut` has no effect on the 3-class totals in the current narrator distribution; nearly all 3-class sensitivity comes from the `x1_high` placement. See `data/processed/video_first_post_vm_batch1_v2/boundary_sensitivity_grid_v2.csv`.

### 2.5 Archived v1 Boundary Scheme

For reproducibility, the v1 boundary scheme is preserved here:

- v1 constants: `X1_CUT_LOW=0.50`, `X1_CUT_HIGH=0.65`, `X2_CUT=0.45`
- v1 merge: `{injury, injury_disrupted, adaptive_rupture}→Injury; {default_rupture}→Rupture; {politicizing_rupture, distrust}→Distrust`
- v1 distribution (N=642): Injury=506 (78.8%), Rupture=125 (19.5%), Distrust=11 (1.7%)
- v1 output files: `narrator_llm_fulltext_2d_outcomes_v1.csv`, `interview_llm_fulltext_2d_outcomes_v1.csv`

---

## 3. Aggregation: From Segments to Interviews and Narrators

### 3.1 The Majority-Vote Problem

Argmax aggregation (majority-vote) from segment to interview level systematically destroys minority-class signal. Because rupture dominates at the segment level (70-80%), taking the modal category per interview produces 85-97% rupture dominance at the interview level — even when individual interviews contain meaningful segments of injury or distrust.

### 3.2 Why This Matters for Causal Modeling

The causal hypotheses are defined at the narrator level. If the outcome has been reduced to a near-constant (97% rupture) by the time it reaches the causal model, there is no variation left for treatment channels to explain. The entire research design depends on measurable outcome heterogeneity at the narrator level.

### 3.3 Recommended Aggregation Approach

The recommended aggregation rule for the current text experiment and later causal-modeling prep should preserve within-interview heterogeneity rather than collapsing to a single label:

1. **Share vectors**: For each interview, compute the proportion of scored segments in each what-axis category: $(s_\text{inj}, s_\text{rup}, s_\text{dis})$. This is a point on the 3-simplex.

2. **Continuous ILR transform**: Apply the Isometric Log-Ratio (ILR) transform (Aitchison 1982; Egozcue et al. 2003) to map the 3-simplex to $\mathbb{R}^2$:
   - $\text{ilr}_1 = \sqrt{1/2} \cdot \ln(s_\text{inj} / s_\text{rup})$  — injury vs rupture contrast
   - $\text{ilr}_2 = \sqrt{2/3} \cdot \ln(\sqrt{s_\text{inj} \cdot s_\text{rup}} / s_\text{dis})$  — {injury, rupture} vs distrust contrast

3. **Minority-signal metrics**: In addition to the share vector, compute per-interview metrics that specifically capture the heterogeneity the causal model needs:
   - Entropy of the segment-level what distribution
   - Presence/absence of any injury or distrust segment (binary flags)
   - Maximum probability assigned to injury or distrust across segments (continuous)

4. **No argmax at interview level**: The dominant-type label may be retained as a summary field for descriptive tables, but it should not be the primary causal outcome. The primary outcome should be the share vector or its ILR transform.

### 3.4 Capturing Minority Heterogeneity

The user noted that the aggregation should "capture the heterogeneous minority parts" rather than averaging them away. This points toward a specific design choice: the causal model should be able to detect whether a treatment channel causes even a small number of segments to shift from rupture to injury or distrust, even if the interview-level majority remains rupture.

Approaches to operationalize this:
- Use the minority-class share ($s_\text{inj}$ or $s_\text{dis}$) as the outcome rather than the overall share vector
- Use the maximum segment-level probability of injury or distrust (capturing the single strongest deviation from rupture)
- Use the count or fraction of segments exceeding a threshold probability for injury or distrust

The exact methodological implementation is a causal-modeling design decision that remains open.

---

## 4. Continuous Scores and Causal Hypothesis Expression

All causal equations in this section are target-parameter specifications within the project's DML-first framework (Chernozhukov et al. 2018; Bodory, Huber, and Laffers 2022). In each equation, nuisance functions $g_0(\cdot)$ are estimated by flexible learners (e.g., random forest, lasso) via cross-fitting with Neyman-orthogonal scores, so that the low-dimensional target parameters ($\theta$, $\gamma$) retain $\sqrt{n}$-consistent inference even though the covariate adjustment is high-dimensional. "Estimation" throughout this section therefore refers to the DML partial-linear-model estimator, not to OLS.

### 4.1 The Problem with a Single Ordered Score

If the what-axis is treated as a single ordered variable ($Y \in \mathbb{R}$, from injury through rupture to distrust), the DML partial linear model (Chernozhukov et al. 2018) targets:

$$Y_i = \theta_1 \cdot \text{timing}_i + \theta_2 \cdot \text{dosage}_i + \theta_3 \cdot \text{severity}_i + g_0(X_i) + \varepsilon_i$$

where $g_0(X_i)$ is a nuisance function estimated by flexible learners over the covariate vector $X_i$ (gender, birth cohort, camp, interview year, etc.) and $\theta$ is the low-dimensional target parameter identified via cross-fitting.

This is parsimonious but imposes a strong assumption: that injury, rupture, and distrust are equidistant points on a single latent dimension. The compositional-data literature (Aitchison 1982) shows this is problematic when outcomes live on a simplex. The two-latent-dimension structure (§1) confirms that rupture is not the midpoint between injury and distrust in a simple sense — it sits at (indifferent, partial belonging), not at (half-protector, half-belonging).

Moreover, a single ordered score cannot distinguish whether a treatment channel shifts the injury type (moving along the authority-stance dimension) versus the belonging position (moving along the belonging-stance dimension). Those are mechanistically different effects that the causal design should be able to separate.

### 4.2 Two-Dimensional Latent Variable Scores

The most theory-consistent approach is to model the what-axis outcome as two continuous scores corresponding to the two latent dimensions. Within the DML partial linear model, the target parameters are:

$$x_{1i} = \gamma_{11} \cdot \text{timing}_i + \gamma_{12} \cdot \text{dosage}_i + \gamma_{13} \cdot \text{severity}_i + g_{01}(X_i) + \varepsilon_{1i}$$
$$x_{2i} = \gamma_{21} \cdot \text{timing}_i + \gamma_{22} \cdot \text{dosage}_i + \gamma_{23} \cdot \text{severity}_i + g_{02}(X_i) + \varepsilon_{2i}$$

where $x_1$ is authority-stance (protector → indifferent → enemy), $x_2$ is belonging-stance (belonging → partial → opposite/alienated), and $g_{01}(\cdot)$, $g_{02}(\cdot)$ are nuisance functions flexibly estimated via cross-fitting. Each equation is estimated separately under the DML cross-fitting protocol; $\gamma$ parameters retain valid inference under high-dimensional covariate adjustment.

This allows the three treatment channels to have differential effects on each dimension:

| Treatment channel | Predicted effect on $x_1$ (authority) | Predicted effect on $x_2$ (belonging) |
|---|---|---|
| **Timing** (exposure age ↑) | Protector → enemy ($\gamma_{11} > 0$) | Still → opposite ($\gamma_{21} > 0$) |
| **Dosage** (confinement duration ↑) | Uncertain — may push toward indifference | Belonging → no belonging ($\gamma_{22} > 0$) |
| **Severity** (betrayal intensity ↑) | Protector → enemy ($\gamma_{13} > 0$) | May or may not affect belonging |

This structure supports a key theoretical test: severity may primarily shift authority-stance (making the government into an enemy) without necessarily destroying belonging (some narrators become oppositional citizens rather than estranged; cf. Bertsou 2019 on critical distrust coexisting with engagement). Dosage may primarily erode belonging (long confinement damages membership) without necessarily politicizing the narrator's stance toward authority.

Within the project's two-track estimate matrix (see README § Causal Modeling Strategy), each $\gamma$ parameter is reported under both unweighted DML (archive-internal estimand) and weighted DML (transport-oriented estimand, following Bodory, Huber, and Laffers 2022), across Track 1 (6-cell categorical share) and Track 2 (continuous scores / ILR).

### 4.3 Retaining Typology Names with Continuous Scores

The 2D continuous scores do not replace the three category names. The categories remain as interpretive anchors in the 2D space:

- **Injury** = region where authority-stance ≈ protector and belonging-stance ≈ still belonging
- **Rupture** = region where authority-stance ≈ indifferent and belonging-stance ≈ partial
- **Distrust** = region where authority-stance ≈ enemy and belonging-stance ≈ opposite/alienated

The current names (injury, rupture, distrust) are retained because they correctly name the dominant form of relational damage in each region. Alternative naming was considered:

| Current name | Alternative considered | Reason for keeping current |
|---|---|---|
| Injury | Betrayal, failed-protection syndrome | "Injury" is broader and does not presuppose the specific mechanism |
| Rupture | Identity fracture, belonging collapse | "Rupture" captures both the belonging and authority-indifference aspects |
| Distrust | Political opposition, adversarial citizenship | "Distrust" is more parsimonious and connects directly to the political-trust literature |

The shorthand labels (failed protector, stigmatizing excluder, political enemy) describe the narrated role of authority. The formal category names (injury, rupture, distrust) describe the form of relational damage. Both are needed.

### 4.4 ILR as a Practical Bridge

The ILR transform (Aitchison 1982; Egozcue et al. 2003), now retained only as an archived robustness implementation in `scripts/archived_embed_v1/run_outcome_ilr_transform_v1.py`, provides a workable approximation to the 2D structure:
- $\text{ilr}_1$ (injury vs rupture contrast) ≈ partial proxy for authority-stance
- $\text{ilr}_2$ ({injury, rupture} vs distrust contrast) ≈ partial proxy for belonging-stance politicization

The ILR coordinates enter the DML partial linear model as continuous outcomes; each ILR component is estimated in a separate DML equation with cross-fitting. The ILR approach is immediately implementable with existing probability vectors. With the GPT-5.4 text classifier now producing direct 2D scores (authority-stance, belonging-stance), the ILR transform serves as a complementary text-stage Track 2 specification alongside the raw continuous scores. SUR or multivariate DML on the raw $(x_1, x_2, c)$ triple remains the intended Track 2 estimator, while ILR-DML on share vectors is a practical alternative that respects the simplex geometry.

---

## 5. Active What × How Contract

The repository's final What × How contract is now genuinely multimodal on the
How side.  The GPT-5.4 transcript scorer still supplies the authoritative What
axes and the text-side composure subscore, but final composed/discomposed status
is determined jointly by text, audio, and video.

Current implication for this memo:

- **Active categorical outcome**: the What-side 3-class / 6-region GPT-5.4 outputs described in §2.4, crossed with the active multimodal How binary.
- **Active continuous outcome set**: `(authority_stance, belonging_stance, how_multimodal_score)`.
- **Text-side provenance retained**: `composure_score` remains in the schema as the transcript-only How subscore.
- **Archived only**: rubric and embed validation layers remain inactive; older standalone feature-era notes remain historical, but the frozen audio/video outputs now belong to the active How definition.

This memo should therefore be read as authorizing the current multimodal What × How workflow rather than a text-only substitute.

---

## 6. Summary of Design Decisions

| Decision | Status | Rationale |
|---|---|---|
| Retain three what-axis categories (injury, rupture, distrust) | **Confirmed** | Names correctly identify the form of relational damage; theory-grounded in two latent dimensions |
| Flag rupture subdivision (adaptive vs deep) as future refinement | **Deferred** | Requires richer text input than current 160-char summaries |
| Use share vectors / ILR for segment-to-interview aggregation, not argmax | **Adopted** | Preserves minority-class heterogeneity needed for causal modeling |
| Support 2D continuous scores (authority-stance, belonging-stance) | **✅ Operational in production** | GPT-5.4 text classification produces the What axes directly; these remain the active Track 2 substantive dimensions |
| Use ILR as complementary Track 2 specification | **Active** | Respects simplex geometry; alternative to raw-score SUR within Track 2 |
| Multimodal How fusion | **Active** | Final How uses text-side composure plus frozen audio/video scores, with binary status induced by the max-fused multimodal score |

---

*This document records design discussions and decisions about the outcome typology. In its current form it should be read as the working memo for the GPT-5.4 What scorer plus multimodal How outcome system. Legacy rubric and embed materials are archived, while the frozen audio/video How outputs are now part of the active repository workflow.*

---

## References

Citations below include works referenced inline in this document. For the full project bibliography, see README.md § References.

### Compositional Data Analysis

Aitchison, John. 1982. "The Statistical Analysis of Compositional Data." *Journal of the Royal Statistical Society, Series B* 44(2):139-177.

Egozcue, Juan José, Vera Pawlowsky-Glahn, Glòria Mateu-Figueras, and Carles Barceló-Vidal. 2003. "Isometric Logratio Transformations for Compositional Data Analysis." *Mathematical Geology* 35(3):279-300.

### Double/Debiased Machine Learning and Dynamic Treatment

Bodory, Hugo, Martin Huber, and Lukas Laffers. 2022. "Evaluating (Weighted) Dynamic Treatment Effects by Double Machine Learning." *Econometrics Journal* 25(3):628-648. https://doi.org/10.1093/ectj/utac018.

Chernozhukov, Victor, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian Hansen, Whitney Newey, and James Robins. 2018. "Double/Debiased Machine Learning for Treatment and Structural Parameters." *Econometrics Journal* 21(1):C1-C68. https://doi.org/10.1111/ectj.12097.

Heckman, James J., John Eric Humphries, and Gregory Veramendi. 2016. "Dynamic Treatment Effects." *Journal of Econometrics* 191(2):276-292.

### State Support, Political Trust, and Distrust

Bertsou, Eri. 2019. "Rethinking Political Distrust." *European Political Science Review* 11(2):213-230.

Easton, David. 1965. *A Systems Analysis of Political Life*. New York: Wiley.

Easton, David. 1975. "A Re-Assessment of the Concept of Political Support." *British Journal of Political Science* 5(4):435-457.

Hooghe, Marc. 2011. "Why There Is Basically Only One Form of Political Trust." *British Journal of Politics and International Relations* 13(2):269-275.

Norris, Pippa, ed. 2011. *Democratic Deficit: Critical Citizens Revisited*. Cambridge: Cambridge University Press.

van der Meer, Tom W. G., and Sonja Zmerli. 2017. "The Deeply Rooted Concern with Political Trust." In *Handbook on Political Trust*, edited by Sonja Zmerli and Tom W. G. van der Meer. Cheltenham: Edward Elgar.

### Development, Identity Formation, and Stigma

Flanagan, Constance A. 2013. *Teenage Citizens: The Political Theories of the Young*. Cambridge, MA: Harvard University Press.

Goffman, Erving. 1963. *Stigma: Notes on the Management of Spoiled Identity*. Englewood Cliffs, NJ: Prentice-Hall.

Link, Bruce G., and Jo C. Phelan. 2001. "Conceptualizing Stigma." *Annual Review of Sociology* 27:363-385.

Pfeifer, Jennifer H., and Elliot T. Berkman. 2018. "The Development of Self and Identity in Adolescence: Neural Evidence and Implications for a Value-Based Choice Perspective on Motivated Behavior." *Child Development Perspectives* 12(3):158-164.

Thoits, Peggy A. 2011. "Resisting the Stigma of Mental Illness." *Social Psychology Quarterly* 74(1):6-28.

### Oral History, Narrative, and Composure

Portelli, Alessandro. 1991. *The Death of Luigi Trastulli and Other Stories: Form and Meaning in Oral History*. Albany: SUNY Press.

Summerfield, Penny. 2004. "Culture and Composure: Creating Narratives of the Gendered Self in Oral History Interviews." *Cultural and Social History* 1(1):65-93.

Thomson, Alistair. 1994. *Anzac Memories: Living with the Legend*. Oxford: Oxford University Press.
