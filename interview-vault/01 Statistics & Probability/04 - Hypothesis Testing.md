# Hypothesis Testing

**Prev:** [[03 - Central Limit Theorem]] · **Next:** [[05 - ANOVA]]

---

## In plain English

You have a default belief ("nothing special happened"). You collect data. You ask: *if the default were true, how weird would this data be?* If very weird (small p-value), you reject the default.

---

## Interview one-liner

$p$-value = probability of seeing data **at least this extreme**, assuming $H_0$ is true. It is **not** the probability that $H_0$ is true.

---

## Setup

| Term | Meaning |
|------|---------|
| $H_0$ | Null — no effect / no difference |
| $H_1$ | Alternative — effect exists |
| $\alpha$ | Max false-positive rate (often 0.05) |
| **p-value** | Evidence against $H_0$ (smaller = stronger) |
| **Power** | $1 - \beta$ = chance to detect real effect |

**Decision:** reject $H_0$ if p-value $< \alpha$.

---

## Tests (when to use)

| Test                   | Use when                                        |
| ---------------------- | ----------------------------------------------- |
| **t-test** (2 samples) | Compare **means** of 2 groups                   |
| **z-test**             | Large $n$, proportions                          |
| **$\chi^2$**           | Category counts, independence                   |
| **ANOVA**              | Compare means of **3+** groups → [[05 - ANOVA]] |
![[Pasted image 20260728210027.png]]
---



## Pragmatic workflow (A/B test)

1. Define $H_0$ (no lift) and metric (conversion rate).
2. Fix $\alpha$ and **minimum detectable effect** before peeking.
3. Run until planned sample size (avoid p-hacking).
4. Report p-value **and** confidence interval / effect size.

---

## Common traps

| Trap | Correct |
|------|---------|
| "p = 0.04 → 96% chance H₁ true" | p-value ≠ P(H₀\|data) |
| "Not significant = no effect" | May lack **power** (small $n$) |
| "Significant = important" | Check **practical** effect size |
| Peek at results daily and stop early | Inflates false positives |
| Multiple metrics without correction | Use Bonferroni / FDR |

---

## 30-second interview answer

> "I set H₀ and α upfront, choose the right test for the data type, and report both p-values and effect sizes. I treat p-values as evidence against H₀, not as the probability H₀ is true, and I'm careful with multiple comparisons and optional stopping."

---

**Next:** [[05 - ANOVA]]
