# ANOVA (Analysis of Variance)

**Prev:** [[04 - Hypothesis Testing]] · **Next:** [[06 - Classification Metrics]]

---

## Interview one-liner

ANOVA tests whether **means of 3 or more groups** differ, by comparing **variance between groups** vs **variance within groups**.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## One-way ANOVA

**Model:** $Y_{ij} = \mu + \alpha_i + \varepsilon_{ij}$

| Index | Meaning |
|-------|---------|
| $i$ | Group ($1 \ldots k$) |
| $j$ | Observation within group |
| $\mu$ | Grand mean |
| $\alpha_i$ | Effect of group $i$ |
| $\varepsilon_{ij}$ | Residual noise |

**Null:** $\alpha_1 = \alpha_2 = \cdots = \alpha_k = 0$ (all group means equal).

---

## F-statistic

$$F = \frac{\text{MS}_{\text{between}}}{\text{MS}_{\text{within}}}$$

| Term | Meaning |
|------|---------|
| MS$_{\text{between}}$ | Mean square between groups |
| MS$_{\text{within}}$ | Mean square within groups |

Large $F$ → between-group spread dominates → reject equal means.

---

## ANCOVA (brief)

Adds **covariates** (e.g. baseline score) to reduce error variance and increase power.

| | ANOVA | ANCOVA |
|---|--------|--------|
| Controls confounders | No | Yes (continuous covariates) |
| Use | Simple group comparison | Adjusted comparison |

→ More detail: [[02 Bayesian & Causal Inference/04 - ANOVA vs ANCOVA|ANCOVA vs ANCOVA in Bayesian chapter]]

---

## Post-hoc

If ANOVA is significant, use **Tukey HSD** or similar to see **which pairs** differ (avoid pairwise t-tests without correction).

---

**Next:** [[06 - Classification Metrics]]
