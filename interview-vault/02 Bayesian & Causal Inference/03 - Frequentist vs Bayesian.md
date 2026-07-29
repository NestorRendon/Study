# Frequentist vs Bayesian

**Prev:** [[02 - Priors and Posteriors Practical]] · **Next:** [[04 - ANOVA vs ANCOVA]]

---

## In plain English

**Frequentist:** parameters are fixed unknown constants; probability describes **repeated experiments**.  
**Bayesian:** parameters are random variables; probability describes **your uncertainty**.

---

## Comparison

| | Frequentist | Bayesian |
|---|-------------|----------|
| Parameters | Fixed | Distributions |
| Output | Point estimate + p-value | Posterior distribution |
| Uncertainty | Confidence interval | Credible interval |
| Prior knowledge | Not in standard tests | Explicit prior |
| Small $n$ | Wide CI, may be unstable | Prior can regularize |

---

## When each shines (pragmatic)

| Use frequentist | Use Bayesian |
|-----------------|--------------|
| Large RCT, standard reporting | Small data, hierarchical models |
| Regulatory templates expect p-values | Need probability "treatment beats control" |
| Simple t-test / chi-square | Sequential monitoring, multi-arm bandits |

---

## Common traps

| Trap | Correct |
|------|---------|
| "p = 0.04 → 96% chance H₁ true" | p-value is NOT P(H₁ \| data) |
| "Bayes is only for subjective priors" | Weak priors ≈ data-driven |
| "Never use p-values" | Context matters — communicate clearly |

---

**Next:** [[04 - ANOVA vs ANCOVA]]
