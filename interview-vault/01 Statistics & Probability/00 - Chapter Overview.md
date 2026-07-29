# Chapter 1 — Statistics & Probability

**Overview = story only.** Detail notes hold formulas, traps, and interview lines.

---

## The story

1. **Describe the data** — mean, spread, shape ([[01 - Descriptive Statistics]])
2. **Know the distributions** — what to expect from randomness ([[02 - Probability Distributions]])
3. **CLT** — why averages look normal ([[03 - Central Limit Theorem]])
4. **Test hypotheses** — p-values, significance ([[04 - Hypothesis Testing]])
5. **Compare groups** — ANOVA ([[05 - ANOVA]])
6. **Score classifiers** — precision, recall, F1 ([[06 - Classification Metrics]])
7. **Score regressors** — RMSE, R² ([[07 - Regression Metrics]])
8. **Validate honestly** — CV, no leakage ([[08 - Cross Validation]])
9. **Reduce dimensions** — PCA ([[09 - PCA and Factor Analysis]])

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | Descriptive statistics | [[01 - Descriptive Statistics]] |
| 2 | Common distributions | [[02 - Probability Distributions]] |
| 3 | Central Limit Theorem | [[03 - Central Limit Theorem]] |
| 4 | Hypothesis testing & p-values | [[04 - Hypothesis Testing]] |
| 5 | ANOVA | [[05 - ANOVA]] |
| 6 | Classification metrics | [[06 - Classification Metrics]] |
| 7 | Regression metrics | [[07 - Regression Metrics]] |
| 8 | Cross-validation & leakage | [[08 - Cross Validation]] |
| 9 | PCA & factor analysis | [[09 - PCA and Factor Analysis]] |

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Causal inference** | Moving beyond p-values to effect sizes |
| **Bayesian A/B** | Startups use posterior for decisions |
| **Robust stats** | Heavy-tailed metrics in tech/finance |

---

## Common traps (chapter)

| Trap (wrong) | Correct |
|--------------|---------|
| "p-value = probability H₀ is true" | p-value = P(data this extreme **given** H₀) |
| "Significant = important" | Check **effect size** |
| "Always use mean" | Use **median** with skew / outliers |
| "High accuracy on imbalanced data" | Use **precision/recall/F1** |
| "Fit scaler on all data before split" | **Split first**, fit on train |
| "ANOVA for 2 groups only" | Use **t-test** for 2 groups |

---

## Next chapter

→ **[[02 Bayesian & Causal Inference/00 - Chapter Overview]]** (probability updating — natural follow-up to stats)

[[Home|← Home]]
