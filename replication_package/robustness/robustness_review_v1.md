# Robustness Review v1

This review prioritizes the paper-facing outcome panel: the six joint-share outcomes plus the three Track 2 outcomes.

Scanned output roots:
- `robustness/causal_robustness_v2`
- `robustness/causal_robustness_probe_v1`
- `robustness/causal_robustness_appendix_probe_v1`

## R1

### R1

- Source: `robustness/causal_robustness_probe_v1/r1/r1_learner_sensitivity_v1.csv`
- Rows: 783
- sample_n range: 632-633
- Same-sign rate vs reference: 83.7%
- Median absolute delta vs reference: 2.339e-05
- Raw p < 0.05 rows: 118

Headline rows:

| check_id | check_variant | weight_status | outcome | treatment | estimate | std_error | p_value | estimate_delta_vs_reference | same_sign_as_reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | baseline_default | ipw | authority_stance | age_at_first_exposure | 0.003564 | 0.009259 | 0.7003 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | authority_stance | age_at_first_exposure | -0.0293 | 0.01355 | 0.03059 | -0.03287 | 0 |
| R1 | random_forest_regressor | ipw | authority_stance | age_at_first_exposure | -0.003306 | 0.005827 | 0.5705 | -0.006869 | 0 |
| R1 | baseline_default | ipw | authority_stance | severity_index_v2 | 0.04091 | 0.01276 | 0.001343 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | authority_stance | severity_index_v2 | 0.05472 | 0.01127 | 1.204e-06 | 0.01381 | 1 |
| R1 | random_forest_regressor | ipw | authority_stance | severity_index_v2 | 0.04994 | 0.01267 | 8.081e-05 | 0.009036 | 1 |
| R1 | baseline_default | ipw | authority_stance | total_days_incarcerated | 8.26e-06 | 5.127e-06 | 0.1071 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | authority_stance | total_days_incarcerated | 5.64e-06 | 5.425e-06 | 0.2985 | -2.62e-06 | 1 |
| R1 | random_forest_regressor | ipw | authority_stance | total_days_incarcerated | 3.941e-06 | 4.642e-06 | 0.3959 | -4.319e-06 | 1 |
| R1 | baseline_default | ipw | belonging_stance | age_at_first_exposure | 0.01777 | 0.009266 | 0.05521 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | belonging_stance | age_at_first_exposure | -0.01556 | 0.01792 | 0.3852 | -0.03332 | 0 |
| R1 | random_forest_regressor | ipw | belonging_stance | age_at_first_exposure | -0.001247 | 0.007798 | 0.873 | -0.01901 | 0 |
| R1 | baseline_default | ipw | belonging_stance | severity_index_v2 | -0.0001257 | 0.01827 | 0.9945 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | belonging_stance | severity_index_v2 | 0.05358 | 0.0213 | 0.0119 | 0.0537 | 0 |
| R1 | random_forest_regressor | ipw | belonging_stance | severity_index_v2 | 0.0175 | 0.0188 | 0.3519 | 0.01763 | 0 |
| R1 | baseline_default | ipw | belonging_stance | total_days_incarcerated | 4.933e-06 | 5.913e-06 | 0.4042 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | belonging_stance | total_days_incarcerated | 8.486e-06 | 7.358e-06 | 0.2488 | 3.553e-06 | 1 |
| R1 | random_forest_regressor | ipw | belonging_stance | total_days_incarcerated | 5.674e-06 | 5.87e-06 | 0.3338 | 7.411e-07 | 1 |
| R1 | baseline_default | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01771 | 0.01741 | 0.3089 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01296 | 0.03148 | 0.6807 | -0.004759 | 1 |
| R1 | random_forest_regressor | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01677 | 0.0163 | 0.3033 | -0.0009399 | 1 |
| R1 | baseline_default | ipw | how_multimodal_score_mean | severity_index_v2 | 0.04294 | 0.03828 | 0.2619 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | how_multimodal_score_mean | severity_index_v2 | 0.06345 | 0.04348 | 0.1445 | 0.0205 | 1 |
| R1 | random_forest_regressor | ipw | how_multimodal_score_mean | severity_index_v2 | 0.0474 | 0.04057 | 0.2426 | 0.004456 | 1 |
| R1 | baseline_default | ipw | how_multimodal_score_mean | total_days_incarcerated | -5.568e-06 | 1.242e-05 | 0.654 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | how_multimodal_score_mean | total_days_incarcerated | -2.646e-05 | 1.331e-05 | 0.04678 | -2.089e-05 | 1 |
| R1 | random_forest_regressor | ipw | how_multimodal_score_mean | total_days_incarcerated | -2.045e-05 | 1.24e-05 | 0.09919 | -1.488e-05 | 1 |
| R1 | baseline_default | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.01111 | 0.02742 | 0.6854 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | -0.01445 | 0.02189 | 0.5093 | -0.02556 | 0 |
| R1 | random_forest_regressor | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.004583 | 0.01968 | 0.8159 | -0.006527 | 1 |
| R1 | baseline_default | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1393 | 0.04433 | 0.001683 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1549 | 0.04729 | 0.001053 | 0.01565 | 1 |
| R1 | random_forest_regressor | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1316 | 0.04716 | 0.005258 | -0.007662 | 1 |
| R1 | baseline_default | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -1.282e-05 | 1.096e-05 | 0.2421 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -2.044e-05 | 1.22e-05 | 0.0939 | -7.627e-06 | 1 |
| R1 | random_forest_regressor | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -1.34e-05 | 1.14e-05 | 0.2401 | -5.8e-07 | 1 |
| R1 | baseline_default | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.05239 | 0.02993 | 0.08 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.05265 | 0.05188 | 0.3101 | 0.0002609 | 1 |
| R1 | random_forest_regressor | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.02086 | 0.03768 | 0.5799 | -0.03154 | 1 |
| R1 | baseline_default | ipw | share_joint_Rupture_discomposed | severity_index_v2 | 0.04191 | 0.06952 | 0.5466 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | share_joint_Rupture_discomposed | severity_index_v2 | 0.06394 | 0.07157 | 0.3717 | 0.02203 | 1 |
| R1 | random_forest_regressor | ipw | share_joint_Rupture_discomposed | severity_index_v2 | 0.02211 | 0.0682 | 0.7457 | -0.0198 | 1 |
| R1 | baseline_default | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -2.394e-06 | 2.14e-05 | 0.9109 | 0 | 1 |
| R1 | lasso_cv_regressor | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -2.123e-05 | 2.231e-05 | 0.3411 | -1.884e-05 | 1 |
| R1 | random_forest_regressor | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -1.224e-05 | 2.053e-05 | 0.5511 | -9.845e-06 | 1 |
| R1 | baseline_default | rake | authority_stance | age_at_first_exposure | -0.00111 | 0.00583 | 0.849 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | authority_stance | age_at_first_exposure | -0.01708 | 0.01258 | 0.1746 | -0.01597 | 1 |
| R1 | random_forest_regressor | rake | authority_stance | age_at_first_exposure | -0.003317 | 0.003179 | 0.2968 | -0.002207 | 1 |
| R1 | baseline_default | rake | authority_stance | severity_index_v2 | 0.03815 | 0.01417 | 0.007087 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | authority_stance | severity_index_v2 | 0.05408 | 0.01174 | 4.088e-06 | 0.01593 | 1 |
| R1 | random_forest_regressor | rake | authority_stance | severity_index_v2 | 0.04669 | 0.01358 | 0.0005867 | 0.008542 | 1 |
| R1 | baseline_default | rake | authority_stance | total_days_incarcerated | 9.132e-06 | 5e-06 | 0.06777 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | authority_stance | total_days_incarcerated | 6.115e-06 | 5.064e-06 | 0.2272 | -3.017e-06 | 1 |
| R1 | random_forest_regressor | rake | authority_stance | total_days_incarcerated | 5.32e-06 | 4.761e-06 | 0.2638 | -3.812e-06 | 1 |
| R1 | baseline_default | rake | belonging_stance | age_at_first_exposure | 0.01763 | 0.01093 | 0.1067 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | belonging_stance | age_at_first_exposure | -0.008237 | 0.01859 | 0.6576 | -0.02587 | 0 |
| R1 | random_forest_regressor | rake | belonging_stance | age_at_first_exposure | -0.001889 | 0.01309 | 0.8852 | -0.01952 | 0 |
| R1 | baseline_default | rake | belonging_stance | severity_index_v2 | 0.03153 | 0.01885 | 0.09449 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | belonging_stance | severity_index_v2 | 0.06574 | 0.02023 | 0.001154 | 0.03422 | 1 |
| R1 | random_forest_regressor | rake | belonging_stance | severity_index_v2 | 0.02752 | 0.01909 | 0.1493 | -0.004003 | 1 |
| R1 | baseline_default | rake | belonging_stance | total_days_incarcerated | 1.802e-07 | 6.332e-06 | 0.9773 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | belonging_stance | total_days_incarcerated | 6.782e-06 | 6.176e-06 | 0.2721 | 6.602e-06 | 1 |
| R1 | random_forest_regressor | rake | belonging_stance | total_days_incarcerated | 5.795e-06 | 5.58e-06 | 0.299 | 5.615e-06 | 1 |
| R1 | baseline_default | rake | how_multimodal_score_mean | age_at_first_exposure | 0.002821 | 0.01786 | 0.8745 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | how_multimodal_score_mean | age_at_first_exposure | 0.01823 | 0.03601 | 0.6127 | 0.01541 | 1 |
| R1 | random_forest_regressor | rake | how_multimodal_score_mean | age_at_first_exposure | 0.01463 | 0.02323 | 0.5287 | 0.01181 | 1 |
| R1 | baseline_default | rake | how_multimodal_score_mean | severity_index_v2 | 0.05545 | 0.03866 | 0.1515 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | how_multimodal_score_mean | severity_index_v2 | 0.06429 | 0.04034 | 0.1109 | 0.008848 | 1 |
| R1 | random_forest_regressor | rake | how_multimodal_score_mean | severity_index_v2 | 0.04247 | 0.0398 | 0.286 | -0.01298 | 1 |
| R1 | baseline_default | rake | how_multimodal_score_mean | total_days_incarcerated | -1.189e-05 | 1.236e-05 | 0.3359 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | how_multimodal_score_mean | total_days_incarcerated | -2.147e-05 | 1.205e-05 | 0.07473 | -9.584e-06 | 1 |
| R1 | random_forest_regressor | rake | how_multimodal_score_mean | total_days_incarcerated | -1.583e-05 | 1.184e-05 | 0.1815 | -3.937e-06 | 1 |
| R1 | baseline_default | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.01598 | 0.03331 | 0.6315 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.008697 | 0.0252 | 0.73 | 0.007282 | 1 |
| R1 | random_forest_regressor | rake | share_joint_Distrust_discomposed | age_at_first_exposure | 0.002537 | 0.03578 | 0.9435 | 0.01852 | 0 |
| R1 | baseline_default | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1287 | 0.03901 | 0.0009705 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1499 | 0.04308 | 0.0005029 | 0.0212 | 1 |
| R1 | random_forest_regressor | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1235 | 0.04243 | 0.003599 | -0.005168 | 1 |
| R1 | baseline_default | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -1.109e-05 | 1.111e-05 | 0.318 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -1.748e-05 | 1.129e-05 | 0.1216 | -6.389e-06 | 1 |
| R1 | random_forest_regressor | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -8.656e-06 | 1.189e-05 | 0.4666 | 2.437e-06 | 1 |
| R1 | baseline_default | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.03023 | 0.0285 | 0.2889 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.04848 | 0.0599 | 0.4183 | 0.01825 | 1 |
| R1 | random_forest_regressor | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.01515 | 0.0358 | 0.6722 | -0.01508 | 1 |
| R1 | baseline_default | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.07638 | 0.07279 | 0.294 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.07994 | 0.07026 | 0.2553 | 0.00356 | 1 |
| R1 | random_forest_regressor | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.04837 | 0.06931 | 0.4853 | -0.028 | 1 |
| R1 | baseline_default | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -8.291e-06 | 2.307e-05 | 0.7194 | 0 | 1 |
| R1 | lasso_cv_regressor | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -2.203e-05 | 2.23e-05 | 0.3232 | -1.374e-05 | 1 |
| R1 | random_forest_regressor | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -9.067e-06 | 2.043e-05 | 0.6572 | -7.765e-07 | 1 |
| R1 | baseline_default | unweighted | authority_stance | age_at_first_exposure | 0.006366 | 0.01032 | 0.5375 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | authority_stance | age_at_first_exposure | -0.02355 | 0.01289 | 0.06766 | -0.02992 | 0 |
| R1 | random_forest_regressor | unweighted | authority_stance | age_at_first_exposure | -0.006108 | 0.003999 | 0.1267 | -0.01247 | 0 |
| R1 | baseline_default | unweighted | authority_stance | severity_index_v2 | 0.02147 | 0.01031 | 0.03726 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | authority_stance | severity_index_v2 | 0.05436 | 0.01254 | 1.464e-05 | 0.03289 | 1 |
| R1 | random_forest_regressor | unweighted | authority_stance | severity_index_v2 | 0.03839 | 0.0116 | 0.0009359 | 0.01692 | 1 |
| R1 | baseline_default | unweighted | authority_stance | total_days_incarcerated | 6.52e-06 | 3.736e-06 | 0.08096 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | authority_stance | total_days_incarcerated | 3.008e-07 | 3.409e-06 | 0.9297 | -6.219e-06 | 1 |
| R1 | random_forest_regressor | unweighted | authority_stance | total_days_incarcerated | 1.602e-06 | 3.345e-06 | 0.6319 | -4.918e-06 | 1 |
| R1 | baseline_default | unweighted | belonging_stance | age_at_first_exposure | 0.009699 | 0.00745 | 0.193 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | belonging_stance | age_at_first_exposure | -0.01573 | 0.01566 | 0.3151 | -0.02543 | 0 |
| R1 | random_forest_regressor | unweighted | belonging_stance | age_at_first_exposure | 0.00168 | 0.008549 | 0.8442 | -0.008019 | 1 |
| R1 | baseline_default | unweighted | belonging_stance | severity_index_v2 | 0.01983 | 0.01356 | 0.1436 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | belonging_stance | severity_index_v2 | 0.04891 | 0.01614 | 0.002435 | 0.02908 | 1 |
| R1 | random_forest_regressor | unweighted | belonging_stance | severity_index_v2 | 0.02367 | 0.01383 | 0.08686 | 0.003843 | 1 |
| R1 | baseline_default | unweighted | belonging_stance | total_days_incarcerated | 4.864e-06 | 4.616e-06 | 0.292 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | belonging_stance | total_days_incarcerated | 8.871e-06 | 4.977e-06 | 0.07465 | 4.007e-06 | 1 |
| R1 | random_forest_regressor | unweighted | belonging_stance | total_days_incarcerated | 7.819e-06 | 4.187e-06 | 0.0618 | 2.955e-06 | 1 |
| R1 | baseline_default | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.008564 | 0.01385 | 0.5363 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | how_multimodal_score_mean | age_at_first_exposure | -0.01222 | 0.02688 | 0.6493 | -0.02079 | 0 |
| R1 | random_forest_regressor | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.01893 | 0.02564 | 0.4604 | 0.01037 | 1 |
| R1 | baseline_default | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.02265 | 0.02809 | 0.42 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.05701 | 0.03019 | 0.05895 | 0.03436 | 1 |
| R1 | random_forest_regressor | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.03856 | 0.02938 | 0.1894 | 0.01591 | 1 |
| R1 | baseline_default | unweighted | how_multimodal_score_mean | total_days_incarcerated | -4.514e-06 | 9.565e-06 | 0.637 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | how_multimodal_score_mean | total_days_incarcerated | -1.493e-05 | 1.035e-05 | 0.1493 | -1.042e-05 | 1 |
| R1 | random_forest_regressor | unweighted | how_multimodal_score_mean | total_days_incarcerated | -9.055e-06 | 9.436e-06 | 0.3372 | -4.542e-06 | 1 |
| R1 | baseline_default | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.003116 | 0.02023 | 0.8776 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | 0.005358 | 0.01861 | 0.7733 | 0.008475 | 0 |
| R1 | random_forest_regressor | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.003358 | 0.02505 | 0.8933 | -0.0002421 | 1 |
| R1 | baseline_default | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.07878 | 0.02869 | 0.006039 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.1267 | 0.03422 | 0.0002127 | 0.04793 | 1 |
| R1 | random_forest_regressor | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.1032 | 0.03274 | 0.001628 | 0.02437 | 1 |
| R1 | baseline_default | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -2.754e-06 | 8.299e-06 | 0.74 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -8.756e-06 | 8.485e-06 | 0.3021 | -6.002e-06 | 1 |
| R1 | random_forest_regressor | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -9.536e-06 | 7.93e-06 | 0.2292 | -6.782e-06 | 1 |
| R1 | baseline_default | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.04301 | 0.02509 | 0.08649 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | -0.0103 | 0.04532 | 0.8202 | -0.05331 | 0 |
| R1 | random_forest_regressor | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.02513 | 0.0429 | 0.558 | -0.01788 | 1 |
| R1 | baseline_default | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | -0.007079 | 0.04878 | 0.8846 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | 0.05414 | 0.05048 | 0.2835 | 0.06122 | 0 |
| R1 | random_forest_regressor | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | 0.01682 | 0.05157 | 0.7443 | 0.0239 | 0 |
| R1 | baseline_default | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | 8.286e-06 | 1.569e-05 | 0.5975 | 0 | 1 |
| R1 | lasso_cv_regressor | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | -1.514e-05 | 1.763e-05 | 0.3906 | -2.342e-05 | 0 |
| R1 | random_forest_regressor | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | -3.915e-06 | 1.676e-05 | 0.8153 | -1.22e-05 | 0 |

## R2

### R2

- Source: `robustness/causal_robustness_v2/r2/r2_crossfit_folds_v1.csv`
- Rows: 243
- sample_n range: 632-633
- Same-sign rate vs reference: 90.1%
- Median absolute delta vs reference: 8.143e-06
- Raw p < 0.05 rows: 28

Headline rows:

| check_id | check_variant | weight_status | outcome | treatment | estimate | std_error | p_value | estimate_delta_vs_reference | same_sign_as_reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R2 | folds_10 | ipw | authority_stance | age_at_first_exposure | 0.0001262 | 0.01056 | 0.9905 | -0.003437 | 1 |
| R2 | folds_3 | ipw | authority_stance | age_at_first_exposure | 0.006603 | 0.01336 | 0.6211 | 0.00304 | 1 |
| R2 | folds_5_baseline | ipw | authority_stance | age_at_first_exposure | 0.003564 | 0.009259 | 0.7003 | 0 | 1 |
| R2 | folds_10 | ipw | authority_stance | severity_index_v2 | 0.04109 | 0.01331 | 0.002021 | 0.0001843 | 1 |
| R2 | folds_3 | ipw | authority_stance | severity_index_v2 | 0.03869 | 0.01319 | 0.003356 | -0.002222 | 1 |
| R2 | folds_5_baseline | ipw | authority_stance | severity_index_v2 | 0.04091 | 0.01276 | 0.001343 | 0 | 1 |
| R2 | folds_10 | ipw | authority_stance | total_days_incarcerated | 7.169e-06 | 5.306e-06 | 0.1767 | -1.091e-06 | 1 |
| R2 | folds_3 | ipw | authority_stance | total_days_incarcerated | 5.518e-06 | 4.654e-06 | 0.2357 | -2.742e-06 | 1 |
| R2 | folds_5_baseline | ipw | authority_stance | total_days_incarcerated | 8.26e-06 | 5.127e-06 | 0.1071 | 0 | 1 |
| R2 | folds_10 | ipw | belonging_stance | age_at_first_exposure | 0.01368 | 0.009944 | 0.1689 | -0.004086 | 1 |
| R2 | folds_3 | ipw | belonging_stance | age_at_first_exposure | 0.02602 | 0.01538 | 0.09069 | 0.00825 | 1 |
| R2 | folds_5_baseline | ipw | belonging_stance | age_at_first_exposure | 0.01777 | 0.009266 | 0.05521 | 0 | 1 |
| R2 | folds_10 | ipw | belonging_stance | severity_index_v2 | 0.0004109 | 0.01977 | 0.9834 | 0.0005366 | 0 |
| R2 | folds_3 | ipw | belonging_stance | severity_index_v2 | 0.00994 | 0.01893 | 0.5995 | 0.01007 | 0 |
| R2 | folds_5_baseline | ipw | belonging_stance | severity_index_v2 | -0.0001257 | 0.01827 | 0.9945 | 0 | 1 |
| R2 | folds_10 | ipw | belonging_stance | total_days_incarcerated | 3.647e-06 | 6.119e-06 | 0.5511 | -1.285e-06 | 1 |
| R2 | folds_3 | ipw | belonging_stance | total_days_incarcerated | 8.115e-06 | 5.863e-06 | 0.1664 | 3.183e-06 | 1 |
| R2 | folds_5_baseline | ipw | belonging_stance | total_days_incarcerated | 4.933e-06 | 5.913e-06 | 0.4042 | 0 | 1 |
| R2 | folds_10 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.02411 | 0.01901 | 0.2047 | 0.006398 | 1 |
| R2 | folds_3 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.0141 | 0.02948 | 0.6325 | -0.003618 | 1 |
| R2 | folds_5_baseline | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01771 | 0.01741 | 0.3089 | 0 | 1 |
| R2 | folds_10 | ipw | how_multimodal_score_mean | severity_index_v2 | 0.03986 | 0.03842 | 0.2995 | -0.003088 | 1 |
| R2 | folds_3 | ipw | how_multimodal_score_mean | severity_index_v2 | 0.0171 | 0.03388 | 0.6138 | -0.02585 | 1 |
| R2 | folds_5_baseline | ipw | how_multimodal_score_mean | severity_index_v2 | 0.04294 | 0.03828 | 0.2619 | 0 | 1 |
| R2 | folds_10 | ipw | how_multimodal_score_mean | total_days_incarcerated | -1.003e-05 | 1.228e-05 | 0.4142 | -4.462e-06 | 1 |
| R2 | folds_3 | ipw | how_multimodal_score_mean | total_days_incarcerated | -3.748e-06 | 1.295e-05 | 0.7722 | 1.82e-06 | 1 |
| R2 | folds_5_baseline | ipw | how_multimodal_score_mean | total_days_incarcerated | -5.568e-06 | 1.242e-05 | 0.654 | 0 | 1 |
| R2 | folds_10 | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.007258 | 0.02402 | 0.7625 | -0.003852 | 1 |
| R2 | folds_3 | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | -0.00288 | 0.0321 | 0.9285 | -0.01399 | 0 |
| R2 | folds_5_baseline | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.01111 | 0.02742 | 0.6854 | 0 | 1 |
| R2 | folds_10 | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1513 | 0.04673 | 0.001208 | 0.01202 | 1 |
| R2 | folds_3 | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.134 | 0.04426 | 0.002469 | -0.00529 | 1 |
| R2 | folds_5_baseline | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1393 | 0.04433 | 0.001683 | 0 | 1 |
| R2 | folds_10 | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -1.519e-05 | 1.107e-05 | 0.1701 | -2.372e-06 | 1 |
| R2 | folds_3 | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -9.515e-06 | 1.183e-05 | 0.421 | 3.3e-06 | 1 |
| R2 | folds_5_baseline | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -1.282e-05 | 1.096e-05 | 0.2421 | 0 | 1 |
| R2 | folds_10 | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.03204 | 0.03232 | 0.3215 | -0.02035 | 1 |
| R2 | folds_3 | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.0706 | 0.03388 | 0.03716 | 0.01821 | 1 |
| R2 | folds_5_baseline | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.05239 | 0.02993 | 0.08 | 0 | 1 |
| R2 | folds_10 | ipw | share_joint_Rupture_discomposed | severity_index_v2 | 0.02417 | 0.07115 | 0.7341 | -0.01774 | 1 |
| R2 | folds_3 | ipw | share_joint_Rupture_discomposed | severity_index_v2 | -0.02284 | 0.06524 | 0.7263 | -0.06475 | 0 |
| R2 | folds_5_baseline | ipw | share_joint_Rupture_discomposed | severity_index_v2 | 0.04191 | 0.06952 | 0.5466 | 0 | 1 |
| R2 | folds_10 | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -1.729e-05 | 2.311e-05 | 0.4543 | -1.49e-05 | 1 |
| R2 | folds_3 | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | 4.337e-06 | 2.101e-05 | 0.8364 | 6.731e-06 | 0 |
| R2 | folds_5_baseline | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -2.394e-06 | 2.14e-05 | 0.9109 | 0 | 1 |
| R2 | folds_10 | rake | authority_stance | age_at_first_exposure | -0.007941 | 0.005511 | 0.1496 | -0.006831 | 1 |
| R2 | folds_3 | rake | authority_stance | age_at_first_exposure | -0.004762 | 0.003982 | 0.2318 | -0.003652 | 1 |
| R2 | folds_5_baseline | rake | authority_stance | age_at_first_exposure | -0.00111 | 0.00583 | 0.849 | 0 | 1 |
| R2 | folds_10 | rake | authority_stance | severity_index_v2 | 0.04329 | 0.01456 | 0.002949 | 0.00514 | 1 |
| R2 | folds_3 | rake | authority_stance | severity_index_v2 | 0.03266 | 0.01271 | 0.01019 | -0.005491 | 1 |
| R2 | folds_5_baseline | rake | authority_stance | severity_index_v2 | 0.03815 | 0.01417 | 0.007087 | 0 | 1 |
| R2 | folds_10 | rake | authority_stance | total_days_incarcerated | 6.456e-06 | 5.469e-06 | 0.2377 | -2.676e-06 | 1 |
| R2 | folds_3 | rake | authority_stance | total_days_incarcerated | 1.024e-05 | 4.61e-06 | 0.02636 | 1.107e-06 | 1 |
| R2 | folds_5_baseline | rake | authority_stance | total_days_incarcerated | 9.132e-06 | 5e-06 | 0.06777 | 0 | 1 |
| R2 | folds_10 | rake | belonging_stance | age_at_first_exposure | 0.02 | 0.008895 | 0.02452 | 0.002375 | 1 |
| R2 | folds_3 | rake | belonging_stance | age_at_first_exposure | 0.03028 | 0.0161 | 0.06003 | 0.01265 | 1 |
| R2 | folds_5_baseline | rake | belonging_stance | age_at_first_exposure | 0.01763 | 0.01093 | 0.1067 | 0 | 1 |
| R2 | folds_10 | rake | belonging_stance | severity_index_v2 | 0.01546 | 0.0196 | 0.4303 | -0.01607 | 1 |
| R2 | folds_3 | rake | belonging_stance | severity_index_v2 | 0.01637 | 0.01792 | 0.3608 | -0.01515 | 1 |
| R2 | folds_5_baseline | rake | belonging_stance | severity_index_v2 | 0.03153 | 0.01885 | 0.09449 | 0 | 1 |
| R2 | folds_10 | rake | belonging_stance | total_days_incarcerated | 5.919e-06 | 6.308e-06 | 0.3481 | 5.738e-06 | 1 |
| R2 | folds_3 | rake | belonging_stance | total_days_incarcerated | 6.322e-06 | 6.166e-06 | 0.3052 | 6.142e-06 | 1 |
| R2 | folds_5_baseline | rake | belonging_stance | total_days_incarcerated | 1.802e-07 | 6.332e-06 | 0.9773 | 0 | 1 |
| R2 | folds_10 | rake | how_multimodal_score_mean | age_at_first_exposure | 0.001188 | 0.0193 | 0.9509 | -0.001634 | 1 |
| R2 | folds_3 | rake | how_multimodal_score_mean | age_at_first_exposure | -0.00634 | 0.02188 | 0.772 | -0.009161 | 0 |
| R2 | folds_5_baseline | rake | how_multimodal_score_mean | age_at_first_exposure | 0.002821 | 0.01786 | 0.8745 | 0 | 1 |
| R2 | folds_10 | rake | how_multimodal_score_mean | severity_index_v2 | 0.05109 | 0.03721 | 0.1697 | -0.00436 | 1 |
| R2 | folds_3 | rake | how_multimodal_score_mean | severity_index_v2 | 0.03461 | 0.03296 | 0.2938 | -0.02084 | 1 |
| R2 | folds_5_baseline | rake | how_multimodal_score_mean | severity_index_v2 | 0.05545 | 0.03866 | 0.1515 | 0 | 1 |
| R2 | folds_10 | rake | how_multimodal_score_mean | total_days_incarcerated | -1.316e-05 | 1.131e-05 | 0.2445 | -1.275e-06 | 1 |
| R2 | folds_3 | rake | how_multimodal_score_mean | total_days_incarcerated | -1.736e-05 | 1.165e-05 | 0.1363 | -5.468e-06 | 1 |
| R2 | folds_5_baseline | rake | how_multimodal_score_mean | total_days_incarcerated | -1.189e-05 | 1.236e-05 | 0.3359 | 0 | 1 |
| R2 | folds_10 | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.02423 | 0.03265 | 0.4581 | -0.008247 | 1 |
| R2 | folds_3 | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.04488 | 0.03455 | 0.194 | -0.0289 | 1 |
| R2 | folds_5_baseline | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.01598 | 0.03331 | 0.6315 | 0 | 1 |
| R2 | folds_10 | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1441 | 0.03916 | 0.000233 | 0.01545 | 1 |
| R2 | folds_3 | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1272 | 0.03706 | 0.0005982 | -0.001469 | 1 |
| R2 | folds_5_baseline | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1287 | 0.03901 | 0.0009705 | 0 | 1 |
| R2 | folds_10 | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -2.015e-05 | 1.137e-05 | 0.07641 | -9.057e-06 | 1 |
| R2 | folds_3 | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -1.331e-05 | 1.172e-05 | 0.2562 | -2.216e-06 | 1 |
| R2 | folds_5_baseline | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -1.109e-05 | 1.111e-05 | 0.318 | 0 | 1 |
| R2 | folds_10 | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.009024 | 0.02414 | 0.7086 | -0.02121 | 1 |
| R2 | folds_3 | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.02002 | 0.03239 | 0.5364 | -0.01021 | 1 |
| R2 | folds_5_baseline | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.03023 | 0.0285 | 0.2889 | 0 | 1 |
| R2 | folds_10 | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.08059 | 0.07225 | 0.2647 | 0.004212 | 1 |
| R2 | folds_3 | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.03706 | 0.06337 | 0.5586 | -0.03931 | 1 |
| R2 | folds_5_baseline | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.07638 | 0.07279 | 0.294 | 0 | 1 |
| R2 | folds_10 | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -2.18e-05 | 2.166e-05 | 0.3141 | -1.351e-05 | 1 |
| R2 | folds_3 | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -9.111e-06 | 2.004e-05 | 0.6494 | -8.204e-07 | 1 |
| R2 | folds_5_baseline | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -8.291e-06 | 2.307e-05 | 0.7194 | 0 | 1 |
| R2 | folds_10 | unweighted | authority_stance | age_at_first_exposure | -0.0005617 | 0.009969 | 0.9551 | -0.006928 | 0 |
| R2 | folds_3 | unweighted | authority_stance | age_at_first_exposure | 0.006142 | 0.0077 | 0.4251 | -0.0002237 | 1 |
| R2 | folds_5_baseline | unweighted | authority_stance | age_at_first_exposure | 0.006366 | 0.01032 | 0.5375 | 0 | 1 |
| R2 | folds_10 | unweighted | authority_stance | severity_index_v2 | 0.03627 | 0.01107 | 0.00105 | 0.0148 | 1 |
| R2 | folds_3 | unweighted | authority_stance | severity_index_v2 | 0.03538 | 0.01235 | 0.004171 | 0.01391 | 1 |
| R2 | folds_5_baseline | unweighted | authority_stance | severity_index_v2 | 0.02147 | 0.01031 | 0.03726 | 0 | 1 |
| R2 | folds_10 | unweighted | authority_stance | total_days_incarcerated | 2.496e-06 | 3.16e-06 | 0.4296 | -4.024e-06 | 1 |
| R2 | folds_3 | unweighted | authority_stance | total_days_incarcerated | 2.359e-06 | 3.449e-06 | 0.494 | -4.161e-06 | 1 |
| R2 | folds_5_baseline | unweighted | authority_stance | total_days_incarcerated | 6.52e-06 | 3.736e-06 | 0.08096 | 0 | 1 |
| R2 | folds_10 | unweighted | belonging_stance | age_at_first_exposure | 0.004728 | 0.00778 | 0.5434 | -0.004971 | 1 |
| R2 | folds_3 | unweighted | belonging_stance | age_at_first_exposure | 0.01315 | 0.007314 | 0.07214 | 0.003454 | 1 |
| R2 | folds_5_baseline | unweighted | belonging_stance | age_at_first_exposure | 0.009699 | 0.00745 | 0.193 | 0 | 1 |
| R2 | folds_10 | unweighted | belonging_stance | severity_index_v2 | 0.03302 | 0.01326 | 0.01279 | 0.01319 | 1 |
| R2 | folds_3 | unweighted | belonging_stance | severity_index_v2 | 0.03655 | 0.01411 | 0.009584 | 0.01672 | 1 |
| R2 | folds_5_baseline | unweighted | belonging_stance | severity_index_v2 | 0.01983 | 0.01356 | 0.1436 | 0 | 1 |
| R2 | folds_10 | unweighted | belonging_stance | total_days_incarcerated | -3.19e-07 | 4.344e-06 | 0.9415 | -5.183e-06 | 0 |
| R2 | folds_3 | unweighted | belonging_stance | total_days_incarcerated | 4.041e-06 | 4.402e-06 | 0.3586 | -8.227e-07 | 1 |
| R2 | folds_5_baseline | unweighted | belonging_stance | total_days_incarcerated | 4.864e-06 | 4.616e-06 | 0.292 | 0 | 1 |
| R2 | folds_10 | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.005908 | 0.01367 | 0.6657 | -0.002656 | 1 |
| R2 | folds_3 | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.01176 | 0.01241 | 0.3436 | 0.003192 | 1 |
| R2 | folds_5_baseline | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.008564 | 0.01385 | 0.5363 | 0 | 1 |
| R2 | folds_10 | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.0399 | 0.02768 | 0.1494 | 0.01725 | 1 |
| R2 | folds_3 | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.0403 | 0.02944 | 0.171 | 0.01765 | 1 |
| R2 | folds_5_baseline | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.02265 | 0.02809 | 0.42 | 0 | 1 |
| R2 | folds_10 | unweighted | how_multimodal_score_mean | total_days_incarcerated | -1.127e-05 | 9.23e-06 | 0.2221 | -6.756e-06 | 1 |
| R2 | folds_3 | unweighted | how_multimodal_score_mean | total_days_incarcerated | -1.248e-05 | 1.004e-05 | 0.214 | -7.964e-06 | 1 |
| R2 | folds_5_baseline | unweighted | how_multimodal_score_mean | total_days_incarcerated | -4.514e-06 | 9.565e-06 | 0.637 | 0 | 1 |
| R2 | folds_10 | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.009473 | 0.02152 | 0.6599 | -0.006356 | 1 |
| R2 | folds_3 | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | 0.003022 | 0.01929 | 0.8755 | 0.006138 | 0 |
| R2 | folds_5_baseline | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.003116 | 0.02023 | 0.8776 | 0 | 1 |
| R2 | folds_10 | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.09558 | 0.02957 | 0.001229 | 0.01679 | 1 |
| R2 | folds_3 | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.09747 | 0.03312 | 0.003254 | 0.01869 | 1 |
| R2 | folds_5_baseline | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.07878 | 0.02869 | 0.006039 | 0 | 1 |
| R2 | folds_10 | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -8.715e-06 | 8.208e-06 | 0.2883 | -5.962e-06 | 1 |
| R2 | folds_3 | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -8.147e-06 | 8.626e-06 | 0.3449 | -5.394e-06 | 1 |
| R2 | folds_5_baseline | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -2.754e-06 | 8.299e-06 | 0.74 | 0 | 1 |
| R2 | folds_10 | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.01833 | 0.02422 | 0.4492 | -0.02468 | 1 |
| R2 | folds_3 | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.03001 | 0.01867 | 0.108 | -0.01299 | 1 |
| R2 | folds_5_baseline | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.04301 | 0.02509 | 0.08649 | 0 | 1 |
| R2 | folds_10 | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | 0.02355 | 0.04922 | 0.6323 | 0.03063 | 0 |
| R2 | folds_3 | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | 0.03468 | 0.0499 | 0.4871 | 0.04175 | 0 |
| R2 | folds_5_baseline | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | -0.007079 | 0.04878 | 0.8846 | 0 | 1 |
| R2 | folds_10 | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | -1.197e-05 | 1.613e-05 | 0.458 | -2.025e-05 | 0 |
| R2 | folds_3 | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | -1.419e-05 | 1.662e-05 | 0.3932 | -2.247e-05 | 0 |
| R2 | folds_5_baseline | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | 8.286e-06 | 1.569e-05 | 0.5975 | 0 | 1 |

## R3

### R3

- Source: `robustness/causal_robustness_v2/r3/r3_treatment_discretization_v1.csv`
- Rows: 243
- sample_n range: 632-633
- Raw p < 0.05 rows: 24

Headline rows:

| check_id | weight_status | outcome | treatment | estimate | std_error | p_value |
| --- | --- | --- | --- | --- | --- | --- |
| R3 | ipw | authority_stance | family_separation_flag | 0.002743 | 0.01208 | 0.8204 |
| R3 | ipw | authority_stance | loyalty_conflict_flag | 0.01545 | 0.006422 | 0.0161 |
| R3 | ipw | authority_stance | parental_arrest_flag | 0.01007 | 0.008485 | 0.2353 |
| R3 | ipw | authority_stance | segregation_flag | 0.01162 | 0.006667 | 0.08126 |
| R3 | ipw | belonging_stance | family_separation_flag | -0.004548 | 0.0268 | 0.8652 |
| R3 | ipw | belonging_stance | loyalty_conflict_flag | -0.02768 | 0.009641 | 0.004086 |
| R3 | ipw | belonging_stance | parental_arrest_flag | 0.003124 | 0.00931 | 0.7372 |
| R3 | ipw | belonging_stance | segregation_flag | 0.01394 | 0.008835 | 0.1145 |
| R3 | ipw | how_multimodal_score_mean | family_separation_flag | 0.02257 | 0.02963 | 0.4463 |
| R3 | ipw | how_multimodal_score_mean | loyalty_conflict_flag | -0.008334 | 0.01647 | 0.6128 |
| R3 | ipw | how_multimodal_score_mean | parental_arrest_flag | 0.0128 | 0.02421 | 0.5971 |
| R3 | ipw | how_multimodal_score_mean | segregation_flag | 0.01352 | 0.01914 | 0.4802 |
| R3 | ipw | share_joint_Distrust_discomposed | family_separation_flag | 0.06421 | 0.03731 | 0.08528 |
| R3 | ipw | share_joint_Distrust_discomposed | loyalty_conflict_flag | 0.05074 | 0.01726 | 0.003288 |
| R3 | ipw | share_joint_Distrust_discomposed | parental_arrest_flag | 0.002906 | 0.01971 | 0.8828 |
| R3 | ipw | share_joint_Distrust_discomposed | segregation_flag | 0.02379 | 0.01704 | 0.1627 |
| R3 | ipw | share_joint_Rupture_discomposed | family_separation_flag | 0.04302 | 0.06259 | 0.4919 |
| R3 | ipw | share_joint_Rupture_discomposed | loyalty_conflict_flag | -0.05811 | 0.02661 | 0.02899 |
| R3 | ipw | share_joint_Rupture_discomposed | parental_arrest_flag | 0.02978 | 0.03241 | 0.3581 |
| R3 | ipw | share_joint_Rupture_discomposed | segregation_flag | 0.03899 | 0.03131 | 0.2131 |
| R3 | rake | authority_stance | family_separation_flag | 0.005882 | 0.01395 | 0.6733 |
| R3 | rake | authority_stance | loyalty_conflict_flag | 0.01624 | 0.006467 | 0.01205 |
| R3 | rake | authority_stance | parental_arrest_flag | 0.01164 | 0.008097 | 0.1506 |
| R3 | rake | authority_stance | segregation_flag | 0.008437 | 0.007621 | 0.2683 |
| R3 | rake | belonging_stance | family_separation_flag | 0.0116 | 0.02911 | 0.6904 |
| R3 | rake | belonging_stance | loyalty_conflict_flag | -0.02502 | 0.009033 | 0.005613 |
| R3 | rake | belonging_stance | parental_arrest_flag | 0.01421 | 0.009897 | 0.151 |
| R3 | rake | belonging_stance | segregation_flag | 0.02052 | 0.01057 | 0.05221 |
| R3 | rake | how_multimodal_score_mean | family_separation_flag | 0.02701 | 0.02788 | 0.3326 |
| R3 | rake | how_multimodal_score_mean | loyalty_conflict_flag | 0.002063 | 0.01695 | 0.9031 |
| R3 | rake | how_multimodal_score_mean | parental_arrest_flag | 0.01652 | 0.02226 | 0.458 |
| R3 | rake | how_multimodal_score_mean | segregation_flag | 0.004855 | 0.02017 | 0.8097 |
| R3 | rake | share_joint_Distrust_discomposed | family_separation_flag | 0.07056 | 0.03296 | 0.03229 |
| R3 | rake | share_joint_Distrust_discomposed | loyalty_conflict_flag | 0.05591 | 0.01707 | 0.001057 |
| R3 | rake | share_joint_Distrust_discomposed | parental_arrest_flag | -0.002682 | 0.01969 | 0.8916 |
| R3 | rake | share_joint_Distrust_discomposed | segregation_flag | 0.01241 | 0.01931 | 0.5202 |
| R3 | rake | share_joint_Rupture_discomposed | family_separation_flag | 0.09085 | 0.0705 | 0.1975 |
| R3 | rake | share_joint_Rupture_discomposed | loyalty_conflict_flag | -0.05408 | 0.02796 | 0.0531 |
| R3 | rake | share_joint_Rupture_discomposed | parental_arrest_flag | 0.05481 | 0.03298 | 0.09649 |
| R3 | rake | share_joint_Rupture_discomposed | segregation_flag | 0.02668 | 0.03269 | 0.4145 |
| R3 | unweighted | authority_stance | family_separation_flag | 0.002168 | 0.01422 | 0.8788 |
| R3 | unweighted | authority_stance | loyalty_conflict_flag | 0.01849 | 0.005485 | 0.0007481 |
| R3 | unweighted | authority_stance | parental_arrest_flag | 0.0051 | 0.004933 | 0.3012 |
| R3 | unweighted | authority_stance | segregation_flag | 0.001868 | 0.006861 | 0.7854 |
| R3 | unweighted | belonging_stance | family_separation_flag | -0.009787 | 0.02082 | 0.6384 |
| R3 | unweighted | belonging_stance | loyalty_conflict_flag | -0.008523 | 0.006744 | 0.2063 |
| R3 | unweighted | belonging_stance | parental_arrest_flag | 0.007732 | 0.006054 | 0.2016 |
| R3 | unweighted | belonging_stance | segregation_flag | 0.01763 | 0.007806 | 0.0239 |
| R3 | unweighted | how_multimodal_score_mean | family_separation_flag | -0.02176 | 0.02694 | 0.4192 |
| R3 | unweighted | how_multimodal_score_mean | loyalty_conflict_flag | -0.02148 | 0.01349 | 0.1113 |
| R3 | unweighted | how_multimodal_score_mean | parental_arrest_flag | 0.02221 | 0.01471 | 0.1311 |
| R3 | unweighted | how_multimodal_score_mean | segregation_flag | 0.02104 | 0.01459 | 0.1494 |
| R3 | unweighted | share_joint_Distrust_discomposed | family_separation_flag | 0.0606 | 0.03357 | 0.071 |
| R3 | unweighted | share_joint_Distrust_discomposed | loyalty_conflict_flag | 0.02971 | 0.01358 | 0.02872 |
| R3 | unweighted | share_joint_Distrust_discomposed | parental_arrest_flag | -0.002901 | 0.01453 | 0.8418 |
| R3 | unweighted | share_joint_Distrust_discomposed | segregation_flag | 0.01423 | 0.01423 | 0.3172 |
| R3 | unweighted | share_joint_Rupture_discomposed | family_separation_flag | -0.03956 | 0.04987 | 0.4276 |
| R3 | unweighted | share_joint_Rupture_discomposed | loyalty_conflict_flag | -0.06426 | 0.02159 | 0.002915 |
| R3 | unweighted | share_joint_Rupture_discomposed | parental_arrest_flag | 0.04692 | 0.02394 | 0.05 |
| R3 | unweighted | share_joint_Rupture_discomposed | segregation_flag | 0.02775 | 0.02501 | 0.2671 |

## R4

### R4

- Source: `robustness/causal_robustness_v2/r4/r4_overlap_trimming_v1.csv`
- Rows: 81
- sample_n range: 561-562
- Same-sign rate vs reference: 76.5%
- Median absolute delta vs reference: 0.008948
- Raw p < 0.05 rows: 22

Headline rows:

| check_id | weight_status | outcome | treatment | estimate | std_error | p_value | estimate_delta_vs_reference | same_sign_as_reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4 | ipw | authority_stance | age_at_first_exposure | 0.01729 | 0.0166 | 0.2975 | 0.01373 | 1 |
| R4 | ipw | authority_stance | severity_index_v2 | 0.03253 | 0.01499 | 0.02998 | -0.008379 | 1 |
| R4 | ipw | authority_stance | total_days_incarcerated | 5.181e-06 | 6.23e-06 | 0.4056 | -3.079e-06 | 1 |
| R4 | ipw | belonging_stance | age_at_first_exposure | 0.01621 | 0.01562 | 0.2992 | -0.00155 | 1 |
| R4 | ipw | belonging_stance | severity_index_v2 | 0.06559 | 0.0192 | 0.0006349 | 0.06572 | 0 |
| R4 | ipw | belonging_stance | total_days_incarcerated | -1.029e-06 | 5.607e-06 | 0.8543 | -5.962e-06 | 0 |
| R4 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.001345 | 0.02889 | 0.9629 | -0.01637 | 1 |
| R4 | ipw | how_multimodal_score_mean | severity_index_v2 | 0.05519 | 0.04014 | 0.1691 | 0.01224 | 1 |
| R4 | ipw | how_multimodal_score_mean | total_days_incarcerated | -3.303e-05 | 1.431e-05 | 0.02095 | -2.746e-05 | 1 |
| R4 | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.003992 | 0.02298 | 0.8621 | -0.007118 | 1 |
| R4 | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.118 | 0.03668 | 0.001303 | -0.02131 | 1 |
| R4 | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -3.228e-05 | 1.017e-05 | 0.001504 | -1.947e-05 | 1 |
| R4 | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | -0.003803 | 0.04134 | 0.9267 | -0.0562 | 0 |
| R4 | ipw | share_joint_Rupture_discomposed | severity_index_v2 | 0.08441 | 0.07842 | 0.2817 | 0.0425 | 1 |
| R4 | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -4.196e-05 | 2.507e-05 | 0.0942 | -3.956e-05 | 1 |
| R4 | rake | authority_stance | age_at_first_exposure | 0.01757 | 0.01691 | 0.2986 | 0.01868 | 0 |
| R4 | rake | authority_stance | severity_index_v2 | 0.04149 | 0.015 | 0.005681 | 0.003344 | 1 |
| R4 | rake | authority_stance | total_days_incarcerated | 4.926e-06 | 6.463e-06 | 0.446 | -4.206e-06 | 1 |
| R4 | rake | belonging_stance | age_at_first_exposure | 0.01415 | 0.01457 | 0.3317 | -0.003484 | 1 |
| R4 | rake | belonging_stance | severity_index_v2 | 0.06016 | 0.02246 | 0.007397 | 0.02863 | 1 |
| R4 | rake | belonging_stance | total_days_incarcerated | 3.019e-06 | 6.033e-06 | 0.6168 | 2.838e-06 | 1 |
| R4 | rake | how_multimodal_score_mean | age_at_first_exposure | -0.0102 | 0.0276 | 0.7118 | -0.01302 | 0 |
| R4 | rake | how_multimodal_score_mean | severity_index_v2 | 0.0644 | 0.0408 | 0.1145 | 0.008948 | 1 |
| R4 | rake | how_multimodal_score_mean | total_days_incarcerated | -2.751e-05 | 1.274e-05 | 0.03091 | -1.562e-05 | 1 |
| R4 | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.009168 | 0.02144 | 0.669 | 0.00681 | 1 |
| R4 | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1382 | 0.03693 | 0.0001823 | 0.009535 | 1 |
| R4 | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -3.503e-05 | 9.763e-06 | 0.000333 | -2.394e-05 | 1 |
| R4 | rake | share_joint_Rupture_discomposed | age_at_first_exposure | -0.01644 | 0.03653 | 0.6526 | -0.04667 | 0 |
| R4 | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.118 | 0.08108 | 0.1454 | 0.04167 | 1 |
| R4 | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -4.929e-05 | 2.515e-05 | 0.05002 | -4.1e-05 | 1 |
| R4 | unweighted | authority_stance | age_at_first_exposure | 0.01632 | 0.009741 | 0.0938 | 0.009957 | 1 |
| R4 | unweighted | authority_stance | severity_index_v2 | 0.03205 | 0.01349 | 0.01749 | 0.01058 | 1 |
| R4 | unweighted | authority_stance | total_days_incarcerated | 4.275e-06 | 4.011e-06 | 0.2865 | -2.245e-06 | 1 |
| R4 | unweighted | belonging_stance | age_at_first_exposure | 0.01212 | 0.009048 | 0.1805 | 0.00242 | 1 |
| R4 | unweighted | belonging_stance | severity_index_v2 | 0.02961 | 0.01498 | 0.04807 | 0.009779 | 1 |
| R4 | unweighted | belonging_stance | total_days_incarcerated | 4.238e-06 | 4.755e-06 | 0.3728 | -6.263e-07 | 1 |
| R4 | unweighted | how_multimodal_score_mean | age_at_first_exposure | -0.02622 | 0.01623 | 0.1062 | -0.03478 | 0 |
| R4 | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.06755 | 0.02926 | 0.02095 | 0.04489 | 1 |
| R4 | unweighted | how_multimodal_score_mean | total_days_incarcerated | -2.473e-05 | 9.819e-06 | 0.01178 | -2.022e-05 | 1 |
| R4 | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.003695 | 0.01515 | 0.8073 | -0.0005787 | 1 |
| R4 | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.1035 | 0.03315 | 0.001788 | 0.02474 | 1 |
| R4 | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -2.202e-05 | 8.939e-06 | 0.01377 | -1.926e-05 | 1 |
| R4 | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | -0.04001 | 0.0267 | 0.134 | -0.08302 | 0 |
| R4 | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | 0.07119 | 0.05345 | 0.1829 | 0.07827 | 0 |
| R4 | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | -2.972e-05 | 1.716e-05 | 0.08335 | -3.8e-05 | 0 |

## R5

### R5

- Source: `robustness/causal_robustness_v2/r5/r5_weight_specification_v1.csv`
- Rows: 81
- sample_n range: 632-633
- Raw p < 0.05 rows: 7

Headline rows:

| check_id | weight_status | outcome | treatment | estimate | std_error | p_value |
| --- | --- | --- | --- | --- | --- | --- |
| R5 | ipw | authority_stance | age_at_first_exposure | 0.003564 | 0.009259 | 0.7003 |
| R5 | ipw | authority_stance | severity_index_v2 | 0.04091 | 0.01276 | 0.001343 |
| R5 | ipw | authority_stance | total_days_incarcerated | 8.26e-06 | 5.127e-06 | 0.1071 |
| R5 | ipw | belonging_stance | age_at_first_exposure | 0.01777 | 0.009266 | 0.05521 |
| R5 | ipw | belonging_stance | severity_index_v2 | -0.0001257 | 0.01827 | 0.9945 |
| R5 | ipw | belonging_stance | total_days_incarcerated | 4.933e-06 | 5.913e-06 | 0.4042 |
| R5 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01771 | 0.01741 | 0.3089 |
| R5 | ipw | how_multimodal_score_mean | severity_index_v2 | 0.04294 | 0.03828 | 0.2619 |
| R5 | ipw | how_multimodal_score_mean | total_days_incarcerated | -5.568e-06 | 1.242e-05 | 0.654 |
| R5 | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.01111 | 0.02742 | 0.6854 |
| R5 | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1393 | 0.04433 | 0.001683 |
| R5 | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -1.282e-05 | 1.096e-05 | 0.2421 |
| R5 | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.05239 | 0.02993 | 0.08 |
| R5 | ipw | share_joint_Rupture_discomposed | severity_index_v2 | 0.04191 | 0.06952 | 0.5466 |
| R5 | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -2.394e-06 | 2.14e-05 | 0.9109 |
| R5 | rake | authority_stance | age_at_first_exposure | -0.00111 | 0.00583 | 0.849 |
| R5 | rake | authority_stance | severity_index_v2 | 0.03815 | 0.01417 | 0.007087 |
| R5 | rake | authority_stance | total_days_incarcerated | 9.132e-06 | 5e-06 | 0.06777 |
| R5 | rake | belonging_stance | age_at_first_exposure | 0.01763 | 0.01093 | 0.1067 |
| R5 | rake | belonging_stance | severity_index_v2 | 0.03153 | 0.01885 | 0.09449 |
| R5 | rake | belonging_stance | total_days_incarcerated | 1.802e-07 | 6.332e-06 | 0.9773 |
| R5 | rake | how_multimodal_score_mean | age_at_first_exposure | 0.002821 | 0.01786 | 0.8745 |
| R5 | rake | how_multimodal_score_mean | severity_index_v2 | 0.05545 | 0.03866 | 0.1515 |
| R5 | rake | how_multimodal_score_mean | total_days_incarcerated | -1.189e-05 | 1.236e-05 | 0.3359 |
| R5 | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.01598 | 0.03331 | 0.6315 |
| R5 | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1287 | 0.03901 | 0.0009705 |
| R5 | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -1.109e-05 | 1.111e-05 | 0.318 |
| R5 | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.03023 | 0.0285 | 0.2889 |
| R5 | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.07638 | 0.07279 | 0.294 |
| R5 | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -8.291e-06 | 2.307e-05 | 0.7194 |
| R5 | unweighted | authority_stance | age_at_first_exposure | 0.006366 | 0.01032 | 0.5375 |
| R5 | unweighted | authority_stance | severity_index_v2 | 0.02147 | 0.01031 | 0.03726 |
| R5 | unweighted | authority_stance | total_days_incarcerated | 6.52e-06 | 3.736e-06 | 0.08096 |
| R5 | unweighted | belonging_stance | age_at_first_exposure | 0.009699 | 0.00745 | 0.193 |
| R5 | unweighted | belonging_stance | severity_index_v2 | 0.01983 | 0.01356 | 0.1436 |
| R5 | unweighted | belonging_stance | total_days_incarcerated | 4.864e-06 | 4.616e-06 | 0.292 |
| R5 | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.008564 | 0.01385 | 0.5363 |
| R5 | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.02265 | 0.02809 | 0.42 |
| R5 | unweighted | how_multimodal_score_mean | total_days_incarcerated | -4.514e-06 | 9.565e-06 | 0.637 |
| R5 | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.003116 | 0.02023 | 0.8776 |
| R5 | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.07878 | 0.02869 | 0.006039 |
| R5 | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -2.754e-06 | 8.299e-06 | 0.74 |
| R5 | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.04301 | 0.02509 | 0.08649 |
| R5 | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | -0.007079 | 0.04878 | 0.8846 |
| R5 | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | 8.286e-06 | 1.569e-05 | 0.5975 |

## R6

### R6

- Source: `robustness/causal_robustness_v2/r6/r6_boundary_sensitivity_v1.csv`
- Rows: 9

No headline rows found for this check.

## R7

### R7

- Source: `robustness/causal_robustness_v2/r7/r7_alternative_aggregation_v1.csv`
- Rows: 63
- sample_n: 31
- Analysis rows: 31
- Analysis narrators: 31
- Same-sign rate vs reference: 54.0%
- Median absolute delta vs reference: 0.01106
- Raw p < 0.05 rows: 2
- Unsupported outcomes dropped: share_joint_Injury_discomposed, share_joint_Distrust_discomposed

Headline rows:

| check_id | aggregation_variant | weight_status | outcome | treatment | estimate | std_error | p_value | estimate_delta_vs_reference | same_sign_as_reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7 | interview_equal_mean | ipw | authority_stance | age_at_first_exposure | -0.0009985 | 0.001766 | 0.5719 | -0.004562 | 0 |
| R7 | interview_equal_mean | ipw | authority_stance | severity_index_v2 | 0.04688 | 0.03666 | 0.201 | 0.005971 | 1 |
| R7 | interview_equal_mean | ipw | authority_stance | total_days_incarcerated | 2.843e-05 | 1.954e-05 | 0.1458 | 2.017e-05 | 1 |
| R7 | interview_equal_mean | ipw | belonging_stance | age_at_first_exposure | 0.004195 | 0.005719 | 0.4633 | -0.01357 | 1 |
| R7 | interview_equal_mean | ipw | belonging_stance | severity_index_v2 | 0.09565 | 0.08709 | 0.2721 | 0.09578 | 0 |
| R7 | interview_equal_mean | ipw | belonging_stance | total_days_incarcerated | -1.679e-05 | 1.676e-05 | 0.3166 | -2.172e-05 | 0 |
| R7 | interview_equal_mean | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.001126 | 0.00829 | 0.892 | -0.01659 | 1 |
| R7 | interview_equal_mean | ipw | how_multimodal_score_mean | severity_index_v2 | 0.02738 | 0.1528 | 0.8578 | -0.01557 | 1 |
| R7 | interview_equal_mean | ipw | how_multimodal_score_mean | total_days_incarcerated | -4.791e-05 | 2.94e-05 | 0.1032 | -4.235e-05 | 1 |
| R7 | interview_equal_mean | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | -0.002871 | 0.01087 | 0.7916 | -0.05527 | 0 |
| R7 | interview_equal_mean | ipw | share_joint_Rupture_discomposed | severity_index_v2 | -0.07372 | 0.1734 | 0.6708 | -0.1156 | 0 |
| R7 | interview_equal_mean | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -3.816e-05 | 3.771e-05 | 0.3115 | -3.577e-05 | 1 |
| R7 | interview_equal_mean | rake | authority_stance | age_at_first_exposure | -0.001998 | 0.001255 | 0.1113 | -0.000888 | 1 |
| R7 | interview_equal_mean | rake | authority_stance | severity_index_v2 | 0.06803 | 0.03554 | 0.05559 | 0.02988 | 1 |
| R7 | interview_equal_mean | rake | authority_stance | total_days_incarcerated | 2.158e-05 | 1.325e-05 | 0.1032 | 1.245e-05 | 1 |
| R7 | interview_equal_mean | rake | belonging_stance | age_at_first_exposure | 0.003073 | 0.004218 | 0.4664 | -0.01456 | 1 |
| R7 | interview_equal_mean | rake | belonging_stance | severity_index_v2 | 0.03621 | 0.07924 | 0.6477 | 0.004682 | 1 |
| R7 | interview_equal_mean | rake | belonging_stance | total_days_incarcerated | 3.412e-06 | 2.056e-05 | 0.8682 | 3.232e-06 | 1 |
| R7 | interview_equal_mean | rake | how_multimodal_score_mean | age_at_first_exposure | -0.003368 | 0.005662 | 0.5519 | -0.00619 | 0 |
| R7 | interview_equal_mean | rake | how_multimodal_score_mean | severity_index_v2 | -0.09601 | 0.1016 | 0.3446 | -0.1515 | 0 |
| R7 | interview_equal_mean | rake | how_multimodal_score_mean | total_days_incarcerated | -2.055e-05 | 2.328e-05 | 0.3773 | -8.664e-06 | 1 |
| R7 | interview_equal_mean | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.002303 | 0.008201 | 0.7788 | -0.02793 | 1 |
| R7 | interview_equal_mean | rake | share_joint_Rupture_discomposed | severity_index_v2 | -0.04684 | 0.1277 | 0.7137 | -0.1232 | 0 |
| R7 | interview_equal_mean | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -2.195e-05 | 3.241e-05 | 0.4983 | -1.366e-05 | 1 |
| R7 | interview_equal_mean | unweighted | authority_stance | age_at_first_exposure | -0.0001266 | 0.001391 | 0.9275 | -0.006493 | 0 |
| R7 | interview_equal_mean | unweighted | authority_stance | severity_index_v2 | 0.04938 | 0.04245 | 0.2447 | 0.02791 | 1 |
| R7 | interview_equal_mean | unweighted | authority_stance | total_days_incarcerated | 1.678e-05 | 1.523e-05 | 0.2705 | 1.026e-05 | 1 |
| R7 | interview_equal_mean | unweighted | belonging_stance | age_at_first_exposure | -0.002579 | 0.004569 | 0.5725 | -0.01228 | 0 |
| R7 | interview_equal_mean | unweighted | belonging_stance | severity_index_v2 | 0.04319 | 0.07505 | 0.565 | 0.02336 | 1 |
| R7 | interview_equal_mean | unweighted | belonging_stance | total_days_incarcerated | 1.629e-05 | 2.464e-05 | 0.5084 | 1.143e-05 | 1 |
| R7 | interview_equal_mean | unweighted | how_multimodal_score_mean | age_at_first_exposure | -0.004056 | 0.006987 | 0.5616 | -0.01262 | 0 |
| R7 | interview_equal_mean | unweighted | how_multimodal_score_mean | severity_index_v2 | -0.07586 | 0.1376 | 0.5815 | -0.09852 | 0 |
| R7 | interview_equal_mean | unweighted | how_multimodal_score_mean | total_days_incarcerated | -2.042e-05 | 3.131e-05 | 0.5144 | -1.59e-05 | 1 |
| R7 | interview_equal_mean | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | -0.008812 | 0.006315 | 0.1629 | -0.05182 | 0 |
| R7 | interview_equal_mean | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | -0.05163 | 0.1196 | 0.666 | -0.04455 | 1 |
| R7 | interview_equal_mean | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | -1.428e-05 | 2.56e-05 | 0.5769 | -2.257e-05 | 0 |

## R8

### R8

- Source: `robustness/causal_robustness_v2/r8/r8_minority_signal_v1.csv`
- Rows: 63
- sample_n range: 632-633
- Same-sign rate vs reference: 100.0%
- Median absolute delta vs reference: 0
- Raw p < 0.05 rows: 10

Headline rows:

| check_id | weight_status | outcome | treatment | estimate | std_error | p_value | estimate_delta_vs_reference | same_sign_as_reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01771 | 0.01741 | 0.3089 | 0 | 1 |
| R8 | ipw | how_multimodal_score_mean | severity_index_v2 | 0.04294 | 0.03828 | 0.2619 | 0 | 1 |
| R8 | ipw | how_multimodal_score_mean | total_days_incarcerated | -5.568e-06 | 1.242e-05 | 0.654 | 0 | 1 |
| R8 | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.01111 | 0.02742 | 0.6854 | 0 | 1 |
| R8 | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1393 | 0.04433 | 0.001683 | 0 | 1 |
| R8 | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -1.282e-05 | 1.096e-05 | 0.2421 | 0 | 1 |
| R8 | rake | how_multimodal_score_mean | age_at_first_exposure | 0.002821 | 0.01786 | 0.8745 | 0 | 1 |
| R8 | rake | how_multimodal_score_mean | severity_index_v2 | 0.05545 | 0.03866 | 0.1515 | 0 | 1 |
| R8 | rake | how_multimodal_score_mean | total_days_incarcerated | -1.189e-05 | 1.236e-05 | 0.3359 | 0 | 1 |
| R8 | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.01598 | 0.03331 | 0.6315 | 0 | 1 |
| R8 | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1287 | 0.03901 | 0.0009705 | 0 | 1 |
| R8 | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -1.109e-05 | 1.111e-05 | 0.318 | 0 | 1 |
| R8 | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.008564 | 0.01385 | 0.5363 | 0 | 1 |
| R8 | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.02265 | 0.02809 | 0.42 | 0 | 1 |
| R8 | unweighted | how_multimodal_score_mean | total_days_incarcerated | -4.514e-06 | 9.565e-06 | 0.637 | 0 | 1 |
| R8 | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.003116 | 0.02023 | 0.8776 | 0 | 1 |
| R8 | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.07878 | 0.02869 | 0.006039 | 0 | 1 |
| R8 | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -2.754e-06 | 8.299e-06 | 0.74 | 0 | 1 |

## R9

### R9

- Source: `robustness/causal_robustness_v2/r9/r9_ilr_dimensionality_v1.csv`
- Rows: 63
- sample_n range: 632-633
- Raw p < 0.05 rows: 7

No headline rows found for this check.

## R10

### R10

- Source: `robustness/causal_robustness_v2/r10/r10_unobserved_confounding_sensitivity_v1.csv`
- Rows: 81
- sample_n range: 632-633
- Raw p < 0.05 rows: 7
- Median RV q=1: 3.2%
- Median RV q=1, alpha=0.05: 0.0%

Headline rows:

| check_id | weight_status | outcome | treatment | estimate | std_error | p_value | t_statistic | partial_r2 | rv_q | rv_qa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10 | ipw | authority_stance | age_at_first_exposure | 0.003564 | 0.009259 | 0.7003 | 0.3849 | 0.0002351 | 0.01522 | 0 |
| R10 | ipw | authority_stance | severity_index_v2 | 0.04091 | 0.01276 | 0.001343 | 3.207 | 0.01606 | 0.1199 | 0.04825 |
| R10 | ipw | authority_stance | total_days_incarcerated | 8.26e-06 | 5.127e-06 | 0.1071 | 1.611 | 0.004104 | 0.06217 | 0 |
| R10 | ipw | belonging_stance | age_at_first_exposure | 0.01777 | 0.009266 | 0.05521 | 1.917 | 0.005801 | 0.07352 | 0 |
| R10 | ipw | belonging_stance | severity_index_v2 | -0.0001257 | 0.01827 | 0.9945 | -0.006877 | 7.507e-08 | 0.0002739 | 0 |
| R10 | ipw | belonging_stance | total_days_incarcerated | 4.933e-06 | 5.913e-06 | 0.4042 | 0.8342 | 0.001103 | 0.03269 | 0 |
| R10 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01771 | 0.01741 | 0.3089 | 1.017 | 0.001641 | 0.03972 | 0 |
| R10 | ipw | how_multimodal_score_mean | severity_index_v2 | 0.04294 | 0.03828 | 0.2619 | 1.122 | 0.001994 | 0.04371 | 0 |
| R10 | ipw | how_multimodal_score_mean | total_days_incarcerated | -5.568e-06 | 1.242e-05 | 0.654 | -0.4483 | 0.0003188 | 0.0177 | 0 |
| R10 | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.01111 | 0.02742 | 0.6854 | 0.4051 | 0.0002605 | 0.01601 | 0 |
| R10 | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1393 | 0.04433 | 0.001683 | 3.141 | 0.01542 | 0.1176 | 0.04576 |
| R10 | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -1.282e-05 | 1.096e-05 | 0.2421 | -1.17 | 0.002167 | 0.04553 | 0 |
| R10 | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.05239 | 0.02993 | 0.08 | 1.751 | 0.004841 | 0.06736 | 0 |
| R10 | ipw | share_joint_Rupture_discomposed | severity_index_v2 | 0.04191 | 0.06952 | 0.5466 | 0.6028 | 0.0005765 | 0.02373 | 0 |
| R10 | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -2.394e-06 | 2.14e-05 | 0.9109 | -0.1119 | 1.987e-05 | 0.004448 | 0 |
| R10 | rake | authority_stance | age_at_first_exposure | -0.00111 | 0.00583 | 0.849 | -0.1904 | 5.755e-05 | 0.007557 | 0 |
| R10 | rake | authority_stance | severity_index_v2 | 0.03815 | 0.01417 | 0.007087 | 2.693 | 0.01138 | 0.1017 | 0.02856 |
| R10 | rake | authority_stance | total_days_incarcerated | 9.132e-06 | 5e-06 | 0.06777 | 1.827 | 0.005268 | 0.07017 | 0 |
| R10 | rake | belonging_stance | age_at_first_exposure | 0.01763 | 0.01093 | 0.1067 | 1.613 | 0.004114 | 0.06224 | 0 |
| R10 | rake | belonging_stance | severity_index_v2 | 0.03153 | 0.01885 | 0.09449 | 1.672 | 0.004419 | 0.06444 | 0 |
| R10 | rake | belonging_stance | total_days_incarcerated | 1.802e-07 | 6.332e-06 | 0.9773 | 0.02845 | 1.285e-06 | 0.001133 | 0 |
| R10 | rake | how_multimodal_score_mean | age_at_first_exposure | 0.002821 | 0.01786 | 0.8745 | 0.158 | 3.961e-05 | 0.006274 | 0 |
| R10 | rake | how_multimodal_score_mean | severity_index_v2 | 0.05545 | 0.03866 | 0.1515 | 1.434 | 0.003254 | 0.05553 | 0 |
| R10 | rake | how_multimodal_score_mean | total_days_incarcerated | -1.189e-05 | 1.236e-05 | 0.3359 | -0.9623 | 0.001468 | 0.03761 | 0 |
| R10 | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.01598 | 0.03331 | 0.6315 | -0.4796 | 0.000365 | 0.01893 | 0 |
| R10 | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1287 | 0.03901 | 0.0009705 | 3.299 | 0.01698 | 0.1231 | 0.05174 |
| R10 | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -1.109e-05 | 1.111e-05 | 0.318 | -0.9985 | 0.00158 | 0.039 | 0 |
| R10 | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.03023 | 0.0285 | 0.2889 | 1.061 | 0.001782 | 0.04137 | 0 |
| R10 | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.07638 | 0.07279 | 0.294 | 1.049 | 0.001745 | 0.04094 | 0 |
| R10 | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -8.291e-06 | 2.307e-05 | 0.7194 | -0.3593 | 0.0002049 | 0.01421 | 0 |
| R10 | unweighted | authority_stance | age_at_first_exposure | 0.006366 | 0.01032 | 0.5375 | 0.6166 | 0.0006022 | 0.02425 | 0 |
| R10 | unweighted | authority_stance | severity_index_v2 | 0.02147 | 0.01031 | 0.03726 | 2.083 | 0.006828 | 0.07955 | 0.004669 |
| R10 | unweighted | authority_stance | total_days_incarcerated | 6.52e-06 | 3.736e-06 | 0.08096 | 1.745 | 0.004803 | 0.0671 | 0 |
| R10 | unweighted | belonging_stance | age_at_first_exposure | 0.009699 | 0.00745 | 0.193 | 1.302 | 0.002679 | 0.0505 | 0 |
| R10 | unweighted | belonging_stance | severity_index_v2 | 0.01983 | 0.01356 | 0.1436 | 1.463 | 0.003379 | 0.05655 | 0 |
| R10 | unweighted | belonging_stance | total_days_incarcerated | 4.864e-06 | 4.616e-06 | 0.292 | 1.054 | 0.001757 | 0.04108 | 0 |
| R10 | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.008564 | 0.01385 | 0.5363 | 0.6184 | 0.0006056 | 0.02432 | 0 |
| R10 | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.02265 | 0.02809 | 0.42 | 0.8064 | 0.001029 | 0.03159 | 0 |
| R10 | unweighted | how_multimodal_score_mean | total_days_incarcerated | -4.514e-06 | 9.565e-06 | 0.637 | -0.4719 | 0.0003528 | 0.01861 | 0 |
| R10 | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.003116 | 0.02023 | 0.8776 | -0.154 | 3.759e-05 | 0.006113 | 0 |
| R10 | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.07878 | 0.02869 | 0.006039 | 2.746 | 0.01181 | 0.1035 | 0.03059 |
| R10 | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -2.754e-06 | 8.299e-06 | 0.74 | -0.3318 | 0.0001744 | 0.01312 | 0 |
| R10 | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.04301 | 0.02509 | 0.08649 | 1.714 | 0.004635 | 0.06595 | 0 |
| R10 | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | -0.007079 | 0.04878 | 0.8846 | -0.1451 | 3.337e-05 | 0.00576 | 0 |
| R10 | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | 8.286e-06 | 1.569e-05 | 0.5975 | 0.528 | 0.0004415 | 0.0208 | 0 |

## R11

### R11

- Source: `robustness/causal_robustness_probe_v1/r11/r11_exogenous_severity_only_v1.csv`
- Rows: 348
- sample_n range: 632-633
- Raw p < 0.05 rows: 35

Headline rows:

| check_id | weight_status | outcome | treatment | estimate | std_error | p_value |
| --- | --- | --- | --- | --- | --- | --- |
| R11 | ipw | authority_stance | age_at_first_exposure | 0.003481 | 0.009518 | 0.7145 |
| R11 | ipw | authority_stance | family_separation_flag | -0.002355 | 0.01246 | 0.8501 |
| R11 | ipw | authority_stance | parental_arrest_flag | 0.008781 | 0.008408 | 0.2963 |
| R11 | ipw | authority_stance | total_days_incarcerated | 1.434e-05 | 5.362e-06 | 0.007488 |
| R11 | ipw | belonging_stance | age_at_first_exposure | 0.01782 | 0.009268 | 0.05448 |
| R11 | ipw | belonging_stance | family_separation_flag | -0.0002438 | 0.02465 | 0.9921 |
| R11 | ipw | belonging_stance | parental_arrest_flag | -0.001676 | 0.008549 | 0.8446 |
| R11 | ipw | belonging_stance | total_days_incarcerated | 5.006e-06 | 5.355e-06 | 0.3499 |
| R11 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01713 | 0.0174 | 0.3248 |
| R11 | ipw | how_multimodal_score_mean | family_separation_flag | 0.02811 | 0.02813 | 0.3177 |
| R11 | ipw | how_multimodal_score_mean | parental_arrest_flag | 0.008965 | 0.02311 | 0.698 |
| R11 | ipw | how_multimodal_score_mean | total_days_incarcerated | -5.254e-08 | 1.116e-05 | 0.9962 |
| R11 | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.01076 | 0.02726 | 0.6932 |
| R11 | ipw | share_joint_Distrust_discomposed | family_separation_flag | 0.05698 | 0.03791 | 0.1329 |
| R11 | ipw | share_joint_Distrust_discomposed | parental_arrest_flag | -0.001134 | 0.02051 | 0.9559 |
| R11 | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | 7.608e-06 | 9.035e-06 | 0.3997 |
| R11 | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.0508 | 0.02992 | 0.08957 |
| R11 | ipw | share_joint_Rupture_discomposed | family_separation_flag | 0.05547 | 0.05857 | 0.3436 |
| R11 | ipw | share_joint_Rupture_discomposed | parental_arrest_flag | 0.02642 | 0.03225 | 0.4126 |
| R11 | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | 1.272e-06 | 1.894e-05 | 0.9464 |
| R11 | rake | authority_stance | age_at_first_exposure | -0.001354 | 0.005897 | 0.8184 |
| R11 | rake | authority_stance | family_separation_flag | 0.003112 | 0.01404 | 0.8245 |
| R11 | rake | authority_stance | parental_arrest_flag | 0.01133 | 0.007827 | 0.1478 |
| R11 | rake | authority_stance | total_days_incarcerated | 1.423e-05 | 5.3e-06 | 0.007266 |
| R11 | rake | belonging_stance | age_at_first_exposure | 0.01723 | 0.01111 | 0.1211 |
| R11 | rake | belonging_stance | family_separation_flag | 0.0145 | 0.02669 | 0.587 |
| R11 | rake | belonging_stance | parental_arrest_flag | 0.01004 | 0.009557 | 0.2935 |
| R11 | rake | belonging_stance | total_days_incarcerated | 4.03e-06 | 6.221e-06 | 0.5172 |
| R11 | rake | how_multimodal_score_mean | age_at_first_exposure | 0.002095 | 0.01766 | 0.9056 |
| R11 | rake | how_multimodal_score_mean | family_separation_flag | 0.02786 | 0.02706 | 0.3032 |
| R11 | rake | how_multimodal_score_mean | parental_arrest_flag | 0.01687 | 0.02131 | 0.4286 |
| R11 | rake | how_multimodal_score_mean | total_days_incarcerated | -5.141e-06 | 1.127e-05 | 0.6484 |
| R11 | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.01676 | 0.03248 | 0.6058 |
| R11 | rake | share_joint_Distrust_discomposed | family_separation_flag | 0.06545 | 0.03465 | 0.05893 |
| R11 | rake | share_joint_Distrust_discomposed | parental_arrest_flag | 0.0002846 | 0.01928 | 0.9882 |
| R11 | rake | share_joint_Distrust_discomposed | total_days_incarcerated | 6.714e-06 | 9.745e-06 | 0.4909 |
| R11 | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.0275 | 0.02847 | 0.3342 |
| R11 | rake | share_joint_Rupture_discomposed | family_separation_flag | 0.1044 | 0.06816 | 0.1258 |
| R11 | rake | share_joint_Rupture_discomposed | parental_arrest_flag | 0.05341 | 0.03316 | 0.1073 |
| R11 | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -2.471e-06 | 2.027e-05 | 0.903 |
| R11 | unweighted | authority_stance | age_at_first_exposure | 0.006396 | 0.0104 | 0.5385 |
| R11 | unweighted | authority_stance | family_separation_flag | 0.0008359 | 0.01377 | 0.9516 |
| R11 | unweighted | authority_stance | parental_arrest_flag | 0.005691 | 0.004886 | 0.2442 |
| R11 | unweighted | authority_stance | total_days_incarcerated | 9.708e-06 | 3.674e-06 | 0.008238 |
| R11 | unweighted | belonging_stance | age_at_first_exposure | 0.009858 | 0.007572 | 0.1929 |
| R11 | unweighted | belonging_stance | family_separation_flag | -0.007603 | 0.02048 | 0.7105 |
| R11 | unweighted | belonging_stance | parental_arrest_flag | 0.005921 | 0.005982 | 0.3223 |
| R11 | unweighted | belonging_stance | total_days_incarcerated | 7.984e-06 | 4.288e-06 | 0.06259 |
| R11 | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.008112 | 0.01377 | 0.5558 |
| R11 | unweighted | how_multimodal_score_mean | family_separation_flag | -0.01513 | 0.02652 | 0.5682 |
| R11 | unweighted | how_multimodal_score_mean | parental_arrest_flag | 0.01898 | 0.01487 | 0.2018 |
| R11 | unweighted | how_multimodal_score_mean | total_days_incarcerated | -1.528e-06 | 8.425e-06 | 0.8561 |
| R11 | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.002886 | 0.02003 | 0.8854 |
| R11 | unweighted | share_joint_Distrust_discomposed | family_separation_flag | 0.06625 | 0.03319 | 0.04592 |
| R11 | unweighted | share_joint_Distrust_discomposed | parental_arrest_flag | -0.001866 | 0.01451 | 0.8977 |
| R11 | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | 8.705e-06 | 7.448e-06 | 0.2425 |
| R11 | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.0413 | 0.02507 | 0.09954 |
| R11 | unweighted | share_joint_Rupture_discomposed | family_separation_flag | -0.03794 | 0.0492 | 0.4407 |
| R11 | unweighted | share_joint_Rupture_discomposed | parental_arrest_flag | 0.03755 | 0.02424 | 0.1214 |
| R11 | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | 5.803e-06 | 1.399e-05 | 0.6783 |

## R12

### R12

- Source: `robustness/causal_robustness_v2/r12/r12_interview_long_format_v1.csv`
- Rows: 63
- sample_n: 37
- Analysis rows: 37
- Analysis narrators: 31
- Estimation unit: interview
- Same-sign rate vs reference: 52.4%
- Median absolute delta vs reference: 0.006428
- Raw p < 0.05 rows: 20
- Unsupported outcomes dropped: share_joint_Injury_discomposed, share_joint_Distrust_discomposed

Headline rows:

| check_id | weight_status | outcome | treatment | estimate | std_error | p_value | estimate_delta_vs_reference | same_sign_as_reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R12 | ipw | authority_stance | age_at_first_exposure | -0.003822 | 0.001462 | 0.008921 | -0.007386 | 0 |
| R12 | ipw | authority_stance | severity_index_v2 | 0.07237 | 0.02987 | 0.0154 | 0.03146 | 1 |
| R12 | ipw | authority_stance | total_days_incarcerated | 3.422e-05 | 8.778e-06 | 9.658e-05 | 2.596e-05 | 1 |
| R12 | ipw | belonging_stance | age_at_first_exposure | 0.01473 | 0.005162 | 0.004323 | -0.003035 | 1 |
| R12 | ipw | belonging_stance | severity_index_v2 | 0.09765 | 0.07741 | 0.2072 | 0.09777 | 0 |
| R12 | ipw | belonging_stance | total_days_incarcerated | -3.836e-05 | 2.405e-05 | 0.1108 | -4.329e-05 | 0 |
| R12 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01601 | 0.006478 | 0.01344 | -0.0017 | 1 |
| R12 | ipw | how_multimodal_score_mean | severity_index_v2 | -0.06717 | 0.1245 | 0.5896 | -0.1101 | 0 |
| R12 | ipw | how_multimodal_score_mean | total_days_incarcerated | -2.564e-05 | 3.504e-05 | 0.4643 | -2.007e-05 | 1 |
| R12 | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | -0.00953 | 0.005787 | 0.09959 | -0.06192 | 0 |
| R12 | ipw | share_joint_Rupture_discomposed | severity_index_v2 | -0.02235 | 0.1368 | 0.8703 | -0.06426 | 0 |
| R12 | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -8.945e-05 | 3.25e-05 | 0.005921 | -8.706e-05 | 1 |
| R12 | rake | authority_stance | age_at_first_exposure | -0.002819 | 0.001587 | 0.07569 | -0.001708 | 1 |
| R12 | rake | authority_stance | severity_index_v2 | 0.07505 | 0.02654 | 0.004688 | 0.03691 | 1 |
| R12 | rake | authority_stance | total_days_incarcerated | 3.174e-05 | 6.654e-06 | 1.846e-06 | 2.26e-05 | 1 |
| R12 | rake | belonging_stance | age_at_first_exposure | 0.007275 | 0.005522 | 0.1877 | -0.01035 | 1 |
| R12 | rake | belonging_stance | severity_index_v2 | -0.01825 | 0.0618 | 0.7678 | -0.04978 | 0 |
| R12 | rake | belonging_stance | total_days_incarcerated | 4.457e-06 | 1.473e-05 | 0.7623 | 4.277e-06 | 1 |
| R12 | rake | how_multimodal_score_mean | age_at_first_exposure | 0.003424 | 0.00773 | 0.6578 | 0.0006025 | 1 |
| R12 | rake | how_multimodal_score_mean | severity_index_v2 | -0.212 | 0.08242 | 0.0101 | -0.2675 | 0 |
| R12 | rake | how_multimodal_score_mean | total_days_incarcerated | 2.48e-05 | 1.81e-05 | 0.1706 | 3.669e-05 | 0 |
| R12 | rake | share_joint_Rupture_discomposed | age_at_first_exposure | -0.01016 | 0.004345 | 0.01941 | -0.04039 | 0 |
| R12 | rake | share_joint_Rupture_discomposed | severity_index_v2 | -0.1141 | 0.1127 | 0.3117 | -0.1904 | 0 |
| R12 | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -4.388e-05 | 2.871e-05 | 0.1264 | -3.559e-05 | 1 |
| R12 | unweighted | authority_stance | age_at_first_exposure | 0.0007199 | 0.001694 | 0.6708 | -0.005646 | 1 |
| R12 | unweighted | authority_stance | severity_index_v2 | 0.04536 | 0.04226 | 0.2831 | 0.02389 | 1 |
| R12 | unweighted | authority_stance | total_days_incarcerated | 2.515e-05 | 1.079e-05 | 0.01981 | 1.863e-05 | 1 |
| R12 | unweighted | belonging_stance | age_at_first_exposure | 0.008363 | 0.005013 | 0.09525 | -0.001336 | 1 |
| R12 | unweighted | belonging_stance | severity_index_v2 | -0.01263 | 0.06244 | 0.8397 | -0.03246 | 0 |
| R12 | unweighted | belonging_stance | total_days_incarcerated | 2.468e-05 | 1.404e-05 | 0.07874 | 1.981e-05 | 1 |
| R12 | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.006408 | 0.007167 | 0.3713 | -0.002156 | 1 |
| R12 | unweighted | how_multimodal_score_mean | severity_index_v2 | -0.1549 | 0.09743 | 0.1119 | -0.1775 | 0 |
| R12 | unweighted | how_multimodal_score_mean | total_days_incarcerated | 2.441e-05 | 2.58e-05 | 0.3441 | 2.893e-05 | 0 |
| R12 | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | -0.01153 | 0.006303 | 0.06729 | -0.05454 | 0 |
| R12 | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | -0.1145 | 0.08938 | 0.2003 | -0.1074 | 1 |
| R12 | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | -6.599e-06 | 1.935e-05 | 0.7331 | -1.488e-05 | 0 |

## R13

### R13

- Source: `robustness/causal_robustness_v2/r13/r13_sequential_dml_v1.csv`
- Rows: 27
- sample_n range: 632-633
- Same-sign rate vs reference: 96.3%
- Median absolute delta vs reference: 0.0007495
- Raw p < 0.05 rows: 0

Headline rows:

| check_id | weight_status | outcome | treatment | estimate | std_error | p_value | estimate_delta_vs_reference | same_sign_as_reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13 | ipw | authority_stance | age_at_first_exposure | 0.001479 | 0.009266 | 0.8732 | -0.002085 | 1 |
| R13 | ipw | belonging_stance | age_at_first_exposure | 0.01702 | 0.008895 | 0.05577 | -0.0007495 | 1 |
| R13 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.0177 | 0.01697 | 0.297 | -1.719e-05 | 1 |
| R13 | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.01025 | 0.02696 | 0.7037 | -0.0008549 | 1 |
| R13 | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.05191 | 0.02944 | 0.07784 | -0.0004802 | 1 |
| R13 | rake | authority_stance | age_at_first_exposure | -0.002072 | 0.00588 | 0.7246 | -0.0009615 | 1 |
| R13 | rake | belonging_stance | age_at_first_exposure | 0.01734 | 0.01081 | 0.1087 | -0.0002855 | 1 |
| R13 | rake | how_multimodal_score_mean | age_at_first_exposure | 0.003163 | 0.01703 | 0.8526 | 0.0003416 | 1 |
| R13 | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.01633 | 0.03238 | 0.6141 | -0.0003476 | 1 |
| R13 | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.03014 | 0.02748 | 0.2727 | -8.835e-05 | 1 |
| R13 | unweighted | authority_stance | age_at_first_exposure | 0.0052 | 0.01032 | 0.6142 | -0.001166 | 1 |
| R13 | unweighted | belonging_stance | age_at_first_exposure | 0.008802 | 0.007394 | 0.2339 | -0.0008964 | 1 |
| R13 | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.00911 | 0.01366 | 0.5048 | 0.0005458 | 1 |
| R13 | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.003236 | 0.0205 | 0.8746 | -0.0001197 | 1 |
| R13 | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.04177 | 0.02519 | 0.09735 | -0.001242 | 1 |

## R14

### R14

- Source: `robustness/causal_robustness_v2/r14/r14_placebo_permutation_summary_v1.csv`
- Rows: 45
- Empirical p < 0.05 rows: 21

Headline rows:

| check_id | weight_status | outcome | treatment | empirical_p_value |
| --- | --- | --- | --- | --- |
| R14 | ipw | authority_stance | age_at_first_exposure | 0 |
| R14 | ipw | authority_stance | severity_index_v2 | 0 |
| R14 | ipw | authority_stance | total_days_incarcerated | 0 |
| R14 | ipw | belonging_stance | age_at_first_exposure | 0 |
| R14 | ipw | belonging_stance | severity_index_v2 | 1 |
| R14 | ipw | belonging_stance | total_days_incarcerated | 0.375 |
| R14 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0 |
| R14 | ipw | how_multimodal_score_mean | severity_index_v2 | 0.3125 |
| R14 | ipw | how_multimodal_score_mean | total_days_incarcerated | 0.875 |
| R14 | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0 |
| R14 | ipw | share_joint_Rupture_discomposed | severity_index_v2 | 0.4375 |
| R14 | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | 0.9375 |
| R14 | rake | authority_stance | age_at_first_exposure | 0 |
| R14 | rake | authority_stance | severity_index_v2 | 0 |
| R14 | rake | authority_stance | total_days_incarcerated | 0 |
| R14 | rake | belonging_stance | age_at_first_exposure | 0 |
| R14 | rake | belonging_stance | severity_index_v2 | 0.375 |
| R14 | rake | belonging_stance | total_days_incarcerated | 1 |
| R14 | rake | how_multimodal_score_mean | age_at_first_exposure | 0 |
| R14 | rake | how_multimodal_score_mean | severity_index_v2 | 0.375 |
| R14 | rake | how_multimodal_score_mean | total_days_incarcerated | 0.5625 |
| R14 | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0 |
| R14 | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.375 |
| R14 | rake | share_joint_Rupture_discomposed | total_days_incarcerated | 0.5 |
| R14 | unweighted | authority_stance | age_at_first_exposure | 0 |
| R14 | unweighted | authority_stance | severity_index_v2 | 0.125 |
| R14 | unweighted | authority_stance | total_days_incarcerated | 0.3125 |
| R14 | unweighted | belonging_stance | age_at_first_exposure | 0 |
| R14 | unweighted | belonging_stance | severity_index_v2 | 0.25 |
| R14 | unweighted | belonging_stance | total_days_incarcerated | 0.75 |
| R14 | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0 |
| R14 | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.625 |
| R14 | unweighted | how_multimodal_score_mean | total_days_incarcerated | 0.875 |
| R14 | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0 |
| R14 | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | 0.9375 |
| R14 | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | 0.3125 |

## R15

### R15

- Source: `robustness/causal_robustness_v2/r15/r15_leave_one_camp_out_v1.csv`
- Rows: 243
- sample_n range: 568-589
- Same-sign rate vs reference: 74.9%
- Median absolute delta vs reference: 0.006656
- Raw p < 0.05 rows: 35

Headline rows:

| check_id | excluded_facility | weight_status | outcome | treatment | estimate | std_error | p_value | estimate_delta_vs_reference | same_sign_as_reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R15 | minidoka | ipw | authority_stance | age_at_first_exposure | 0.004346 | 0.008478 | 0.6083 | 0.000782 | 1 |
| R15 | manzanar | ipw | authority_stance | age_at_first_exposure | -0.003952 | 0.003536 | 0.2637 | -0.007516 | 0 |
| R15 | tule_lake | ipw | authority_stance | age_at_first_exposure | -0.007076 | 0.007798 | 0.3642 | -0.01064 | 0 |
| R15 | minidoka | ipw | authority_stance | severity_index_v2 | 0.03622 | 0.01365 | 0.007939 | -0.004684 | 1 |
| R15 | manzanar | ipw | authority_stance | severity_index_v2 | 0.03628 | 0.01399 | 0.009518 | -0.004625 | 1 |
| R15 | tule_lake | ipw | authority_stance | severity_index_v2 | 0.06284 | 0.01719 | 0.0002568 | 0.02193 | 1 |
| R15 | minidoka | ipw | authority_stance | total_days_incarcerated | 9.256e-06 | 4.929e-06 | 0.0604 | 9.956e-07 | 1 |
| R15 | manzanar | ipw | authority_stance | total_days_incarcerated | 5.329e-06 | 5.041e-06 | 0.2904 | -2.931e-06 | 1 |
| R15 | tule_lake | ipw | authority_stance | total_days_incarcerated | 7.822e-06 | 4.951e-06 | 0.1142 | -4.381e-07 | 1 |
| R15 | minidoka | ipw | belonging_stance | age_at_first_exposure | 0.01005 | 0.007724 | 0.1931 | -0.007712 | 1 |
| R15 | manzanar | ipw | belonging_stance | age_at_first_exposure | 0.01189 | 0.0114 | 0.297 | -0.005878 | 1 |
| R15 | tule_lake | ipw | belonging_stance | age_at_first_exposure | 0.008288 | 0.008797 | 0.3461 | -0.009477 | 1 |
| R15 | minidoka | ipw | belonging_stance | severity_index_v2 | 0.02516 | 0.02034 | 0.2161 | 0.02528 | 0 |
| R15 | manzanar | ipw | belonging_stance | severity_index_v2 | 0.02506 | 0.01803 | 0.1647 | 0.02518 | 0 |
| R15 | tule_lake | ipw | belonging_stance | severity_index_v2 | 0.04023 | 0.01875 | 0.03186 | 0.04036 | 0 |
| R15 | minidoka | ipw | belonging_stance | total_days_incarcerated | -2.626e-07 | 6.106e-06 | 0.9657 | -5.195e-06 | 0 |
| R15 | manzanar | ipw | belonging_stance | total_days_incarcerated | -1.382e-06 | 6.233e-06 | 0.8246 | -6.314e-06 | 0 |
| R15 | tule_lake | ipw | belonging_stance | total_days_incarcerated | -1.543e-06 | 6.274e-06 | 0.8057 | -6.476e-06 | 0 |
| R15 | minidoka | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.02611 | 0.01437 | 0.06924 | 0.008398 | 1 |
| R15 | manzanar | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01142 | 0.0278 | 0.6814 | -0.006299 | 1 |
| R15 | tule_lake | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.002986 | 0.01511 | 0.8433 | -0.01473 | 1 |
| R15 | minidoka | ipw | how_multimodal_score_mean | severity_index_v2 | 0.01195 | 0.03867 | 0.7572 | -0.03099 | 1 |
| R15 | manzanar | ipw | how_multimodal_score_mean | severity_index_v2 | 0.05811 | 0.03667 | 0.113 | 0.01517 | 1 |
| R15 | tule_lake | ipw | how_multimodal_score_mean | severity_index_v2 | -0.07027 | 0.03865 | 0.06903 | -0.1132 | 0 |
| R15 | minidoka | ipw | how_multimodal_score_mean | total_days_incarcerated | -4.103e-06 | 1.163e-05 | 0.7243 | 1.465e-06 | 1 |
| R15 | manzanar | ipw | how_multimodal_score_mean | total_days_incarcerated | -2.551e-05 | 1.337e-05 | 0.05639 | -1.994e-05 | 1 |
| R15 | tule_lake | ipw | how_multimodal_score_mean | total_days_incarcerated | 2.091e-05 | 1.236e-05 | 0.09078 | 2.647e-05 | 0 |
| R15 | minidoka | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | 0.004454 | 0.01511 | 0.7682 | -0.006656 | 1 |
| R15 | manzanar | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | -0.01031 | 0.01194 | 0.3878 | -0.02142 | 0 |
| R15 | tule_lake | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | -0.02643 | 0.02172 | 0.2236 | -0.03754 | 0 |
| R15 | minidoka | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1257 | 0.04946 | 0.01102 | -0.01353 | 1 |
| R15 | manzanar | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1641 | 0.04804 | 0.0006354 | 0.02485 | 1 |
| R15 | tule_lake | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.05489 | 0.03314 | 0.09767 | -0.08437 | 1 |
| R15 | minidoka | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -1.484e-05 | 1.121e-05 | 0.1856 | -2.025e-06 | 1 |
| R15 | manzanar | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -3.011e-05 | 1.176e-05 | 0.01049 | -1.729e-05 | 1 |
| R15 | tule_lake | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | 2.341e-06 | 1.08e-05 | 0.8285 | 1.516e-05 | 0 |
| R15 | minidoka | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.06436 | 0.0192 | 0.0008014 | 0.01197 | 1 |
| R15 | manzanar | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.02684 | 0.02957 | 0.364 | -0.02555 | 1 |
| R15 | tule_lake | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.03233 | 0.02847 | 0.2561 | -0.02006 | 1 |
| R15 | minidoka | ipw | share_joint_Rupture_discomposed | severity_index_v2 | -0.005605 | 0.06579 | 0.9321 | -0.04752 | 0 |
| R15 | manzanar | ipw | share_joint_Rupture_discomposed | severity_index_v2 | 0.07257 | 0.08131 | 0.3721 | 0.03066 | 1 |
| R15 | tule_lake | ipw | share_joint_Rupture_discomposed | severity_index_v2 | -0.04078 | 0.06784 | 0.5478 | -0.08269 | 0 |
| R15 | minidoka | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -2.162e-05 | 2.176e-05 | 0.3204 | -1.922e-05 | 1 |
| R15 | manzanar | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | -2.65e-05 | 2.364e-05 | 0.2622 | -2.41e-05 | 1 |
| R15 | tule_lake | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | 3.444e-05 | 2.329e-05 | 0.1391 | 3.684e-05 | 0 |
| R15 | minidoka | rake | authority_stance | age_at_first_exposure | 0.003555 | 0.008061 | 0.6592 | 0.004665 | 0 |
| R15 | manzanar | rake | authority_stance | age_at_first_exposure | -0.006727 | 0.004771 | 0.1586 | -0.005617 | 1 |
| R15 | tule_lake | rake | authority_stance | age_at_first_exposure | -0.007212 | 0.006199 | 0.2446 | -0.006102 | 1 |
| R15 | minidoka | rake | authority_stance | severity_index_v2 | 0.02953 | 0.01461 | 0.04319 | -0.008615 | 1 |
| R15 | manzanar | rake | authority_stance | severity_index_v2 | 0.04026 | 0.015 | 0.007263 | 0.002111 | 1 |
| R15 | tule_lake | rake | authority_stance | severity_index_v2 | 0.05801 | 0.01634 | 0.0003834 | 0.01987 | 1 |
| R15 | minidoka | rake | authority_stance | total_days_incarcerated | 1.005e-05 | 5.316e-06 | 0.05875 | 9.15e-07 | 1 |
| R15 | manzanar | rake | authority_stance | total_days_incarcerated | 5.835e-06 | 5.13e-06 | 0.2554 | -3.297e-06 | 1 |
| R15 | tule_lake | rake | authority_stance | total_days_incarcerated | 9.894e-06 | 4.877e-06 | 0.0425 | 7.623e-07 | 1 |
| R15 | minidoka | rake | belonging_stance | age_at_first_exposure | 0.009871 | 0.009619 | 0.3048 | -0.007758 | 1 |
| R15 | manzanar | rake | belonging_stance | age_at_first_exposure | 0.03136 | 0.01215 | 0.009876 | 0.01373 | 1 |
| R15 | tule_lake | rake | belonging_stance | age_at_first_exposure | 0.01522 | 0.01169 | 0.1929 | -0.002412 | 1 |
| R15 | minidoka | rake | belonging_stance | severity_index_v2 | 0.02522 | 0.02163 | 0.2435 | -0.006304 | 1 |
| R15 | manzanar | rake | belonging_stance | severity_index_v2 | 0.03473 | 0.01991 | 0.08105 | 0.003198 | 1 |
| R15 | tule_lake | rake | belonging_stance | severity_index_v2 | 0.04602 | 0.0192 | 0.01651 | 0.01449 | 1 |
| R15 | minidoka | rake | belonging_stance | total_days_incarcerated | 2.032e-06 | 6.619e-06 | 0.7588 | 1.852e-06 | 1 |
| R15 | manzanar | rake | belonging_stance | total_days_incarcerated | -6.223e-07 | 6.55e-06 | 0.9243 | -8.025e-07 | 0 |
| R15 | tule_lake | rake | belonging_stance | total_days_incarcerated | 3.402e-06 | 6.226e-06 | 0.5848 | 3.221e-06 | 1 |
| R15 | minidoka | rake | how_multimodal_score_mean | age_at_first_exposure | 0.01726 | 0.02095 | 0.4102 | 0.01443 | 1 |
| R15 | manzanar | rake | how_multimodal_score_mean | age_at_first_exposure | -0.009696 | 0.01947 | 0.6184 | -0.01252 | 0 |
| R15 | tule_lake | rake | how_multimodal_score_mean | age_at_first_exposure | -0.005793 | 0.01349 | 0.6677 | -0.008614 | 0 |
| R15 | minidoka | rake | how_multimodal_score_mean | severity_index_v2 | 0.033 | 0.04065 | 0.417 | -0.02245 | 1 |
| R15 | manzanar | rake | how_multimodal_score_mean | severity_index_v2 | 0.05706 | 0.03557 | 0.1087 | 0.001611 | 1 |
| R15 | tule_lake | rake | how_multimodal_score_mean | severity_index_v2 | -0.03112 | 0.03842 | 0.4179 | -0.08657 | 0 |
| R15 | minidoka | rake | how_multimodal_score_mean | total_days_incarcerated | -8.112e-06 | 1.165e-05 | 0.4863 | 3.778e-06 | 1 |
| R15 | manzanar | rake | how_multimodal_score_mean | total_days_incarcerated | -2.228e-05 | 1.247e-05 | 0.0739 | -1.039e-05 | 1 |
| R15 | tule_lake | rake | how_multimodal_score_mean | total_days_incarcerated | 1.549e-05 | 1.169e-05 | 0.1852 | 2.738e-05 | 0 |
| R15 | minidoka | rake | share_joint_Distrust_discomposed | age_at_first_exposure | 0.0139 | 0.01569 | 0.3757 | 0.02988 | 0 |
| R15 | manzanar | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.05103 | 0.02438 | 0.03633 | -0.03505 | 1 |
| R15 | tule_lake | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.04116 | 0.0236 | 0.08114 | -0.02518 | 1 |
| R15 | minidoka | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1214 | 0.04301 | 0.004765 | -0.007299 | 1 |
| R15 | manzanar | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1399 | 0.0426 | 0.001019 | 0.01125 | 1 |
| R15 | tule_lake | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.07197 | 0.03308 | 0.02958 | -0.05671 | 1 |
| R15 | minidoka | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -1.961e-05 | 1.057e-05 | 0.06352 | -8.519e-06 | 1 |
| R15 | manzanar | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -2.127e-05 | 1.154e-05 | 0.06538 | -1.017e-05 | 1 |
| R15 | tule_lake | rake | share_joint_Distrust_discomposed | total_days_incarcerated | 2.566e-06 | 1.062e-05 | 0.8091 | 1.366e-05 | 0 |
| R15 | minidoka | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.04057 | 0.04142 | 0.3274 | 0.01034 | 1 |
| R15 | manzanar | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.01603 | 0.02365 | 0.498 | -0.0142 | 1 |
| R15 | tule_lake | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.03134 | 0.02113 | 0.138 | 0.001106 | 1 |
| R15 | minidoka | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.02149 | 0.07509 | 0.7747 | -0.05488 | 1 |
| R15 | manzanar | rake | share_joint_Rupture_discomposed | severity_index_v2 | 0.05823 | 0.07845 | 0.4579 | -0.01815 | 1 |
| R15 | tule_lake | rake | share_joint_Rupture_discomposed | severity_index_v2 | -0.009354 | 0.07109 | 0.8953 | -0.08573 | 0 |
| R15 | minidoka | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -3.339e-05 | 2.37e-05 | 0.159 | -2.51e-05 | 1 |
| R15 | manzanar | rake | share_joint_Rupture_discomposed | total_days_incarcerated | -2.895e-05 | 2.456e-05 | 0.2385 | -2.066e-05 | 1 |
| R15 | tule_lake | rake | share_joint_Rupture_discomposed | total_days_incarcerated | 3.028e-05 | 2.206e-05 | 0.17 | 3.857e-05 | 0 |
| R15 | minidoka | unweighted | authority_stance | age_at_first_exposure | -0.002042 | 0.007327 | 0.7804 | -0.008408 | 0 |
| R15 | manzanar | unweighted | authority_stance | age_at_first_exposure | 0.001475 | 0.005744 | 0.7973 | -0.004891 | 1 |
| R15 | tule_lake | unweighted | authority_stance | age_at_first_exposure | -0.002946 | 0.004273 | 0.4906 | -0.009312 | 0 |
| R15 | minidoka | unweighted | authority_stance | severity_index_v2 | 0.039 | 0.01191 | 0.001057 | 0.01753 | 1 |
| R15 | manzanar | unweighted | authority_stance | severity_index_v2 | 0.04854 | 0.01213 | 6.26e-05 | 0.02707 | 1 |
| R15 | tule_lake | unweighted | authority_stance | severity_index_v2 | 0.04018 | 0.01513 | 0.007922 | 0.01871 | 1 |
| R15 | minidoka | unweighted | authority_stance | total_days_incarcerated | 4.749e-06 | 3.512e-06 | 0.1764 | -1.771e-06 | 1 |
| R15 | manzanar | unweighted | authority_stance | total_days_incarcerated | 1.306e-06 | 3.115e-06 | 0.6751 | -5.214e-06 | 1 |
| R15 | tule_lake | unweighted | authority_stance | total_days_incarcerated | 3.379e-06 | 3.398e-06 | 0.32 | -3.141e-06 | 1 |
| R15 | minidoka | unweighted | belonging_stance | age_at_first_exposure | 0.008386 | 0.007164 | 0.2418 | -0.001312 | 1 |
| R15 | manzanar | unweighted | belonging_stance | age_at_first_exposure | 0.001149 | 0.006898 | 0.8678 | -0.00855 | 1 |
| R15 | tule_lake | unweighted | belonging_stance | age_at_first_exposure | 0.01057 | 0.006343 | 0.09566 | 0.0008703 | 1 |
| R15 | minidoka | unweighted | belonging_stance | severity_index_v2 | 0.0439 | 0.01546 | 0.004524 | 0.02407 | 1 |
| R15 | manzanar | unweighted | belonging_stance | severity_index_v2 | 0.03125 | 0.0151 | 0.03848 | 0.01141 | 1 |
| R15 | tule_lake | unweighted | belonging_stance | severity_index_v2 | 0.05038 | 0.0165 | 0.002268 | 0.03055 | 1 |
| R15 | minidoka | unweighted | belonging_stance | total_days_incarcerated | 1.23e-06 | 4.577e-06 | 0.7881 | -3.634e-06 | 1 |
| R15 | manzanar | unweighted | belonging_stance | total_days_incarcerated | 4.389e-06 | 4.403e-06 | 0.3189 | -4.752e-07 | 1 |
| R15 | tule_lake | unweighted | belonging_stance | total_days_incarcerated | -2.378e-06 | 4.404e-06 | 0.5893 | -7.242e-06 | 0 |
| R15 | minidoka | unweighted | how_multimodal_score_mean | age_at_first_exposure | -0.000642 | 0.01495 | 0.9657 | -0.009206 | 0 |
| R15 | manzanar | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.001524 | 0.01207 | 0.8995 | -0.00704 | 1 |
| R15 | tule_lake | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.006494 | 0.01066 | 0.5424 | -0.00207 | 1 |
| R15 | minidoka | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.05635 | 0.032 | 0.0783 | 0.03369 | 1 |
| R15 | manzanar | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.01042 | 0.0294 | 0.7229 | -0.01223 | 1 |
| R15 | tule_lake | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.04748 | 0.03123 | 0.1284 | 0.02483 | 1 |
| R15 | minidoka | unweighted | how_multimodal_score_mean | total_days_incarcerated | -1.274e-05 | 9.942e-06 | 0.2002 | -8.222e-06 | 1 |
| R15 | manzanar | unweighted | how_multimodal_score_mean | total_days_incarcerated | -1.119e-05 | 9.87e-06 | 0.2569 | -6.677e-06 | 1 |
| R15 | tule_lake | unweighted | how_multimodal_score_mean | total_days_incarcerated | -2.308e-06 | 9.271e-06 | 0.8034 | 2.206e-06 | 1 |
| R15 | minidoka | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | 0.002929 | 0.01191 | 0.8057 | 0.006045 | 0 |
| R15 | manzanar | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.01303 | 0.01299 | 0.3161 | -0.009909 | 1 |
| R15 | tule_lake | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.00565 | 0.01675 | 0.7359 | -0.002534 | 1 |
| R15 | minidoka | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.1102 | 0.03214 | 0.0006046 | 0.03144 | 1 |
| R15 | manzanar | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.1033 | 0.03359 | 0.002112 | 0.02448 | 1 |
| R15 | tule_lake | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.08316 | 0.02896 | 0.004085 | 0.00438 | 1 |
| R15 | minidoka | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -1.039e-05 | 8.611e-06 | 0.2276 | -7.637e-06 | 1 |
| R15 | manzanar | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -1.227e-05 | 8.222e-06 | 0.1356 | -9.516e-06 | 1 |
| R15 | tule_lake | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -1.039e-05 | 8.341e-06 | 0.2127 | -7.641e-06 | 1 |
| R15 | minidoka | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.0118 | 0.02552 | 0.6438 | -0.03121 | 1 |
| R15 | manzanar | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.01381 | 0.02518 | 0.5835 | -0.0292 | 1 |
| R15 | tule_lake | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.01775 | 0.0209 | 0.3958 | -0.02526 | 1 |
| R15 | minidoka | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | 0.03376 | 0.05631 | 0.5488 | 0.04084 | 0 |
| R15 | manzanar | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | -0.003786 | 0.0528 | 0.9428 | 0.003292 | 1 |
| R15 | tule_lake | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | 0.08655 | 0.05501 | 0.1156 | 0.09363 | 0 |
| R15 | minidoka | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | -1.244e-05 | 1.703e-05 | 0.4651 | -2.073e-05 | 0 |
| R15 | manzanar | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | -9.454e-06 | 1.7e-05 | 0.5782 | -1.774e-05 | 0 |
| R15 | tule_lake | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | -9.038e-06 | 1.642e-05 | 0.5819 | -1.732e-05 | 0 |

## R16

### R16

- Source: `robustness/causal_robustness_probe_v1/r16/r16_complete_case_v1.csv`
- Rows: 261
- sample_n: 564
- Same-sign rate vs reference: 67.0%
- Median absolute delta vs reference: 0.01248
- Raw p < 0.05 rows: 41

Headline rows:

| check_id | sample_variant | weight_status | outcome | treatment | estimate | std_error | p_value | estimate_delta_vs_reference | same_sign_as_reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R16 | complete_case | ipw | authority_stance | age_at_first_exposure | -0.002079 | 0.007619 | 0.7849 | -0.005643 | 0 |
| R16 | complete_case | ipw | authority_stance | severity_index_v2 | 0.04923 | 0.01142 | 1.615e-05 | 0.008324 | 1 |
| R16 | complete_case | ipw | authority_stance | total_days_incarcerated | 1.765e-06 | 4.95e-06 | 0.7214 | -6.495e-06 | 1 |
| R16 | complete_case | ipw | belonging_stance | age_at_first_exposure | 0.01017 | 0.01049 | 0.3322 | -0.00759 | 1 |
| R16 | complete_case | ipw | belonging_stance | severity_index_v2 | 0.004296 | 0.01863 | 0.8176 | 0.004421 | 0 |
| R16 | complete_case | ipw | belonging_stance | total_days_incarcerated | 9.496e-07 | 5.605e-06 | 0.8655 | -3.983e-06 | 1 |
| R16 | complete_case | ipw | how_multimodal_score_mean | age_at_first_exposure | -0.001146 | 0.02008 | 0.9545 | -0.01886 | 0 |
| R16 | complete_case | ipw | how_multimodal_score_mean | severity_index_v2 | -0.03265 | 0.03587 | 0.3628 | -0.07559 | 0 |
| R16 | complete_case | ipw | how_multimodal_score_mean | total_days_incarcerated | 9.011e-06 | 1.291e-05 | 0.4851 | 1.458e-05 | 0 |
| R16 | complete_case | ipw | share_joint_Distrust_discomposed | age_at_first_exposure | -0.004616 | 0.01781 | 0.7955 | -0.01573 | 0 |
| R16 | complete_case | ipw | share_joint_Distrust_discomposed | severity_index_v2 | 0.1026 | 0.04286 | 0.0167 | -0.03668 | 1 |
| R16 | complete_case | ipw | share_joint_Distrust_discomposed | total_days_incarcerated | -6.577e-06 | 1.198e-05 | 0.5829 | 6.238e-06 | 1 |
| R16 | complete_case | ipw | share_joint_Rupture_discomposed | age_at_first_exposure | 0.03192 | 0.03773 | 0.3976 | -0.02048 | 1 |
| R16 | complete_case | ipw | share_joint_Rupture_discomposed | severity_index_v2 | -0.1184 | 0.07726 | 0.1255 | -0.1603 | 0 |
| R16 | complete_case | ipw | share_joint_Rupture_discomposed | total_days_incarcerated | 1.658e-05 | 2.415e-05 | 0.4925 | 1.897e-05 | 0 |
| R16 | complete_case | rake | authority_stance | age_at_first_exposure | -0.008496 | 0.004355 | 0.05109 | -0.007385 | 1 |
| R16 | complete_case | rake | authority_stance | severity_index_v2 | 0.04841 | 0.01256 | 0.0001165 | 0.01026 | 1 |
| R16 | complete_case | rake | authority_stance | total_days_incarcerated | 1.481e-06 | 5.282e-06 | 0.7792 | -7.651e-06 | 1 |
| R16 | complete_case | rake | belonging_stance | age_at_first_exposure | 0.02321 | 0.01237 | 0.06066 | 0.005581 | 1 |
| R16 | complete_case | rake | belonging_stance | severity_index_v2 | -0.0003291 | 0.02113 | 0.9876 | -0.03186 | 0 |
| R16 | complete_case | rake | belonging_stance | total_days_incarcerated | 4.366e-06 | 6.767e-06 | 0.5188 | 4.186e-06 | 1 |
| R16 | complete_case | rake | how_multimodal_score_mean | age_at_first_exposure | -0.009904 | 0.01196 | 0.4075 | -0.01273 | 0 |
| R16 | complete_case | rake | how_multimodal_score_mean | severity_index_v2 | -0.01571 | 0.03644 | 0.6663 | -0.07116 | 0 |
| R16 | complete_case | rake | how_multimodal_score_mean | total_days_incarcerated | 5.179e-06 | 1.271e-05 | 0.6837 | 1.707e-05 | 0 |
| R16 | complete_case | rake | share_joint_Distrust_discomposed | age_at_first_exposure | -0.04382 | 0.02447 | 0.07334 | -0.02784 | 1 |
| R16 | complete_case | rake | share_joint_Distrust_discomposed | severity_index_v2 | 0.1059 | 0.04188 | 0.01141 | -0.02274 | 1 |
| R16 | complete_case | rake | share_joint_Distrust_discomposed | total_days_incarcerated | -1.071e-05 | 1.222e-05 | 0.3808 | 3.804e-07 | 1 |
| R16 | complete_case | rake | share_joint_Rupture_discomposed | age_at_first_exposure | 0.0199 | 0.02376 | 0.4024 | -0.01033 | 1 |
| R16 | complete_case | rake | share_joint_Rupture_discomposed | severity_index_v2 | -0.1155 | 0.07632 | 0.1302 | -0.1919 | 0 |
| R16 | complete_case | rake | share_joint_Rupture_discomposed | total_days_incarcerated | 1.813e-05 | 2.55e-05 | 0.4769 | 2.642e-05 | 0 |
| R16 | complete_case | unweighted | authority_stance | age_at_first_exposure | -0.002561 | 0.006877 | 0.7096 | -0.008927 | 0 |
| R16 | complete_case | unweighted | authority_stance | severity_index_v2 | 0.04236 | 0.01151 | 0.000233 | 0.0209 | 1 |
| R16 | complete_case | unweighted | authority_stance | total_days_incarcerated | 1.868e-06 | 3.348e-06 | 0.5769 | -4.652e-06 | 1 |
| R16 | complete_case | unweighted | belonging_stance | age_at_first_exposure | 0.009424 | 0.008084 | 0.2437 | -0.0002745 | 1 |
| R16 | complete_case | unweighted | belonging_stance | severity_index_v2 | 0.02511 | 0.0147 | 0.08764 | 0.005275 | 1 |
| R16 | complete_case | unweighted | belonging_stance | total_days_incarcerated | 2.97e-06 | 4.726e-06 | 0.5297 | -1.894e-06 | 1 |
| R16 | complete_case | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.0005797 | 0.01348 | 0.9657 | -0.007984 | 1 |
| R16 | complete_case | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.009505 | 0.0294 | 0.7465 | -0.01315 | 1 |
| R16 | complete_case | unweighted | how_multimodal_score_mean | total_days_incarcerated | 1.342e-06 | 9.82e-06 | 0.8913 | 5.856e-06 | 0 |
| R16 | complete_case | unweighted | share_joint_Distrust_discomposed | age_at_first_exposure | -0.0156 | 0.01947 | 0.4231 | -0.01248 | 1 |
| R16 | complete_case | unweighted | share_joint_Distrust_discomposed | severity_index_v2 | 0.0895 | 0.03419 | 0.008855 | 0.01072 | 1 |
| R16 | complete_case | unweighted | share_joint_Distrust_discomposed | total_days_incarcerated | -6.361e-06 | 9.043e-06 | 0.4818 | -3.608e-06 | 1 |
| R16 | complete_case | unweighted | share_joint_Rupture_discomposed | age_at_first_exposure | 0.02527 | 0.03227 | 0.4336 | -0.01774 | 1 |
| R16 | complete_case | unweighted | share_joint_Rupture_discomposed | severity_index_v2 | -0.02573 | 0.05286 | 0.6264 | -0.01866 | 1 |
| R16 | complete_case | unweighted | share_joint_Rupture_discomposed | total_days_incarcerated | 6.073e-06 | 1.693e-05 | 0.7198 | -2.213e-06 | 1 |

## R17

### R17

- Source: `robustness/causal_robustness_probe_v1/r17/r17_embedding_arm_v1.csv`
- Rows: 45
- sample_n: 31
- Same-sign rate vs reference: 46.7%
- Median absolute delta vs reference: 0.02048
- Raw p < 0.05 rows: 9

No headline rows found for this check.

## R18

### R18

- Source: `robustness/causal_robustness_v2/r18/r18_interview_year_interaction_v1.csv`
- Rows: 261
- sample_n range: 632-633
- Raw p < 0.05 rows: 74

Headline rows:

| check_id | weight_status | outcome | treatment | estimate | std_error | p_value |
| --- | --- | --- | --- | --- | --- | --- |
| R18 | ipw | authority_stance | adolescent_exposure_flag | 0.0231 | 0.08684 | 0.7902 |
| R18 | ipw | belonging_stance | adolescent_exposure_flag | 0.06492 | 0.2541 | 0.7983 |
| R18 | ipw | how_multimodal_score_mean | adolescent_exposure_flag | -0.05183 | 0.5345 | 0.9228 |
| R18 | ipw | share_joint_Distrust_discomposed | adolescent_exposure_flag | 0.2688 | 0.4532 | 0.5531 |
| R18 | ipw | share_joint_Rupture_discomposed | adolescent_exposure_flag | 0.415 | 0.7227 | 0.5658 |
| R18 | rake | authority_stance | adolescent_exposure_flag | 0.006128 | 0.06756 | 0.9277 |
| R18 | rake | belonging_stance | adolescent_exposure_flag | 0.05219 | 0.3905 | 0.8937 |
| R18 | rake | how_multimodal_score_mean | adolescent_exposure_flag | -0.07925 | 0.7654 | 0.9175 |
| R18 | rake | share_joint_Distrust_discomposed | adolescent_exposure_flag | 0.09242 | 0.1662 | 0.578 |
| R18 | rake | share_joint_Rupture_discomposed | adolescent_exposure_flag | 0.2521 | 0.3334 | 0.4497 |
| R18 | unweighted | authority_stance | adolescent_exposure_flag | 0.0007895 | 0.07564 | 0.9917 |
| R18 | unweighted | belonging_stance | adolescent_exposure_flag | 0.01061 | 0.219 | 0.9614 |
| R18 | unweighted | how_multimodal_score_mean | adolescent_exposure_flag | 0.1074 | 0.2488 | 0.6661 |
| R18 | unweighted | share_joint_Distrust_discomposed | adolescent_exposure_flag | 0.124 | 0.09419 | 0.1882 |
| R18 | unweighted | share_joint_Rupture_discomposed | adolescent_exposure_flag | 0.3177 | 0.3404 | 0.3507 |

## R19

### R19

- Source: `robustness/causal_robustness_probe_v1/r19/r19_composure_separate_v1.csv`
- Rows: 72
- sample_n range: 632-633
- Same-sign rate vs reference: 100.0%
- Median absolute delta vs reference: 0
- Raw p < 0.05 rows: 6

Headline rows:

| check_id | weight_status | outcome | treatment | estimate | std_error | p_value | estimate_delta_vs_reference | same_sign_as_reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R19 | ipw | how_multimodal_score_mean | age_at_first_exposure | 0.01771 | 0.01741 | 0.3089 | 0 | 1 |
| R19 | ipw | how_multimodal_score_mean | severity_index_v2 | 0.04294 | 0.03828 | 0.2619 | 0 | 1 |
| R19 | ipw | how_multimodal_score_mean | total_days_incarcerated | -5.568e-06 | 1.242e-05 | 0.654 | 0 | 1 |
| R19 | rake | how_multimodal_score_mean | age_at_first_exposure | 0.002821 | 0.01786 | 0.8745 | 0 | 1 |
| R19 | rake | how_multimodal_score_mean | severity_index_v2 | 0.05545 | 0.03866 | 0.1515 | 0 | 1 |
| R19 | rake | how_multimodal_score_mean | total_days_incarcerated | -1.189e-05 | 1.236e-05 | 0.3359 | 0 | 1 |
| R19 | unweighted | how_multimodal_score_mean | age_at_first_exposure | 0.008564 | 0.01385 | 0.5363 | 0 | 1 |
| R19 | unweighted | how_multimodal_score_mean | severity_index_v2 | 0.02265 | 0.02809 | 0.42 | 0 | 1 |
| R19 | unweighted | how_multimodal_score_mean | total_days_incarcerated | -4.514e-06 | 9.565e-06 | 0.637 | 0 | 1 |

## MEASUREMENT_AUDIT

### MEASUREMENT_AUDIT

- Source: `robustness/causal_robustness_v2/measurement_audit/measurement_sensitivity_audit_v1.csv`
- Rows: 216

No headline rows found for this check.

## APPENDIX_HOW

### APPENDIX_HOW

- Source: `scripts/robustness/how_negative_controls_v1.csv`
- Rows: 6

No headline rows found for this check.
