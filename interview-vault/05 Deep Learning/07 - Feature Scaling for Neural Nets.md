# Feature Scaling for Neural Nets

**Prev:** [[06 - Early Stopping]] · **Next:** [[08 - Optimizers SGD Adam]]

---

## Interview one-liner

Neural nets train faster and more stably when inputs are **zero-mean, comparable scale**. Always fit the scaler on **training data only**.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Standardization

$$x'_j = \frac{x_j - \mu_j}{\sigma_j}$$

Fit $\mu_j, \sigma_j$ on train; apply to val/test.

---

## Why it matters

| Without scaling | With scaling |
|-----------------|--------------|
| Ill-conditioned loss landscape | Rounder contours, easier GD |
| Some weights dominate | Balanced gradient magnitudes |
| Slow / unstable convergence | Faster, more stable training |

Also required before **PCA**, **kNN**, **SVM** with RBF.

---

**Next:** [[08 - Optimizers SGD Adam]]
