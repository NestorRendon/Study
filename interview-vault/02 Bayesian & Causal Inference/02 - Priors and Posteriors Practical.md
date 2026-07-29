# Priors & Posteriors (Practical)

**Prev:** [[01 - Bayesian Inference]] · **Next:** [[03 - Frequentist vs Bayesian]]

---

## In plain English

**Prior** = what you believe before seeing today's data. **Posterior** = what you believe after. More data → posterior depends less on prior.

---

## Types of priors

| Prior | When to use | Example |
|-------|-------------|---------|
| **Uninformative / weak** | Little prior knowledge; let data speak | Wide Normal on coefficient |
| **Informative** | Strong domain knowledge | Expert elicitation on conversion rate |
| **Conjugate** | Math convenience — prior + likelihood → same family posterior | Beta-Binomial, Normal-Normal |

---

## Conjugate examples (interview favorites)

### Beta–Binomial (proportion)

- Prior: $p \sim \text{Beta}(\alpha, \beta)$
- Data: $k$ successes in $n$ trials
- Posterior: $\text{Beta}(\alpha + k, \beta + n - k)$

**Use:** click-through rate, defect rate, A/B conversion.

### Normal–Normal (mean with known variance)

- Prior: $\mu \sim \mathcal{N}(\mu_0, \sigma_0^2)$
- Posterior mean is precision-weighted blend of prior and sample mean.

---

## Credible interval vs confidence interval

| | Frequentist CI | Bayesian credible interval |
|---|----------------|----------------------------|
| Meaning | Procedure covers true θ 95% of repeated samples | **95% probability** θ is in interval (given model & prior) |
| Interpretation | Tricky for non-statisticians | Natural for decision makers |

---

## Pragmatic workflow

1. Choose prior (weak if unsure).
2. Fit model (analytic, MCMC, Variational).
3. **Prior sensitivity:** do conclusions change with reasonable priors?
4. Report posterior mean + 95% credible interval.

---

## Common traps

| Trap | Correct |
|------|---------|
| Improper prior without checking | Ensure posterior is proper (integrates to 1) |
| Double-counting data in prior | Prior should exclude current experiment data |
| Only report posterior mean | Report **uncertainty** (intervals) |

---

**Next:** [[03 - Frequentist vs Bayesian]]
