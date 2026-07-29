# ANOVA vs ANCOVA

**Prev:** [[03 - Frequentist vs Bayesian]] · **Next:** [[05 - Structure Learning]]

---

## In plain English

**ANOVA** compares average outcomes across **3+ groups**. **ANCOVA** does the same but **adjusts for a baseline variable** (covariate) like pre-test score or age.

---

| | ANOVA | ANCOVA |
|---|--------|--------|
| Controls confounders | No | Yes (covariates) |
| Power | Lower if noise unmodeled | Often higher |
| Example | 3 teaching methods | 3 methods, controlling pre-test |

→ Full ANOVA math: [[01 Statistics & Probability/05 - ANOVA]]

---

## Common traps

| Trap | Correct |
|------|---------|
| ANCOVA without randomization care | Assumptions on covariate relationship |
| ANOVA for only 2 groups | Use **t-test** |

---

**Next:** [[05 - Structure Learning]]
