# Regularization (L1 & L2)

**Prev:** [[03 - Loss Functions]] · **Next:** [[05 - Dropout]]

---

## In plain English

Your model is memorizing noise. **Regularization** punishes complicated weights so the model stays simpler and generalizes better. **L2** gently shrinks all weights; **L1** can zero out useless features entirely.

---

## Interview one-liner

After **high variance** ([[01 - Bias-Variance Tradeoff]]), add a weight penalty. Use **L2** by default in neural nets; use **L1** when you need sparse features or interpretability.

---

## Equations

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{data}} + \lambda \Omega(\mathbf{w})$$

| Symbol | Meaning |
|--------|---------|
| $\mathcal{L}_{\text{data}}$ | MSE, cross-entropy, etc. |
| $\lambda$ | Regularization strength (↑ = more penalty) |
| $\Omega$ | L1 or L2 norm of weights |

**L2 (Ridge / weight decay):**

$$\Omega(\mathbf{w}) = \|\mathbf{w}\|_2^2 = \sum_j w_j^2$$

**L1 (Lasso):**

$$\Omega(\mathbf{w}) = \|\mathbf{w}\|_1 = \sum_j |w_j|$$

---

## When to use L2 (pragmatic)

| Situation | Why L2 |
|-----------|--------|
| Neural networks (default) | Stable training, weight decay in AdamW |
| Many correlated features | Shrinks together, unlike L1 picking one |
| You want smooth decisions | No hard zeros, all features contribute a little |
| Logistic regression with separable data | Prevents weights exploding (sklearn `C` = inverse λ) |
| Ridge regression | Classic high-dimensional linear model |

**Real example:** 500 sensor features, most weakly useful → Ridge keeps all but small weights, stable predictions.

---

## When to use L1 (pragmatic)

| Situation | Why L1 |
|-----------|--------|
| Feature selection | Many $w_j = 0$ → sparse model |
| Interpretability | "Which 10 features matter?" |
| High $p$, suspect many irrelevant inputs | Text classification with huge vocab |
| Lasso path for screening | See which features survive as λ increases |

**Real example:** 2000 genomic markers, only ~20 causal → Lasso picks a sparse subset for reporting.

---

## L1 vs L2 — geometry intuition

| | L2 | L1 |
|---|----|----|
| Constraint region | Circle (smooth) | Diamond (corners on axes) |
| Optimum often | Shrinks all weights | Hits corner → some weights **exactly 0** |
| Correlated features | Shares weight | Often picks one, ignores others |

**Elastic Net:** L1 + L2 together when you want sparsity *and* stability with correlated features.

---

## Choosing $\lambda$

| $\lambda$ | Effect |
|-----------|--------|
| Too small | Still overfits (high variance) |
| Too large | Underfits (high bias) |
| Right | Minimum **validation** error |

Tune on validation or CV — **never** on the test set.

---

## Common traps

| Trap (wrong) | Correct |
|--------------|---------|
| "L1 and L2 do the same thing" | L1 → sparsity; L2 → small weights everywhere |
| "Regularization fixes high bias" | Regularization **increases** bias — use when variance is the problem |
| "Use test set to pick λ" | Use validation / CV only |
| "Bigger λ always helps" | Too large → underfitting |
| "Only for linear models" | Weight decay in deep nets is L2 |

---

## 30-second interview answer

> "If validation shows overfitting — train error low, test high — I add regularization. L2 weight decay is my default in neural nets because it stabilizes training. I'd choose L1 when I need feature selection or a sparse interpretable model, for example high-dimensional tabular data with many irrelevant columns. I tune λ on cross-validation."

---

## Related

| Context | Name |
|---------|------|
| Linear regression | Ridge ($L_2$), Lasso ($L_1$), Elastic Net |
| Neural nets | Weight decay (AdamW) |
| SVM | Large $C$ = **less** regularization |

---

**Next:** [[05 - Dropout]]
