# Central Limit Theorem

**Prev:** [[02 - Probability Distributions]] · **Next:** [[04 - Hypothesis Testing]]

---

## Interview one-liner

Sample means from large enough samples are **approximately Normal**, even if the original data are not — this justifies t-tests, confidence intervals, and many ML assumptions.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*

## Law of Large Numbers (LLN)

$$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{n \to \infty} \mu$$

Sample average converges to the true mean.

---

## Central Limit Theorem (CLT)

For i.i.d. $X_i$ with mean $\mu$ and finite variance $\sigma^2$:

$$\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

| Symbol | Meaning |
|--------|---------|
| $\bar{X}_n$ | Sample mean |
| $\mu$ | Population mean |
| $\sigma$ | Population std dev |
| $n$ | Sample size |

**Intuition:** sums/averages of many random pieces → bell curve.

---

## Why it matters in DS

- Justify **Normal-based** confidence intervals on metrics.
- Understand **standard error** shrinks as $1/\sqrt{n}$.
- Foundation for **hypothesis tests** on means (next note).

---

**Next:** [[04 - Hypothesis Testing]]
