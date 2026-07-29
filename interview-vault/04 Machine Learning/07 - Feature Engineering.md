# Feature Engineering

**Prev:** [[06 - Support Vector Machines]] · **Next:** [[08 - Overfitting]]

---

## Interview one-liner

Turn raw data into **informative inputs**: scaling, encoding, creating interactions, selecting relevant variables. Often beats switching algorithms.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Scaling

| Method | Formula | When |
|--------|---------|------|
| Standardize | $x' = (x - \mu)/\sigma$ | SVM, kNN, neural nets, PCA |
| Min-max | $x' = (x - \min)/(\max - \min)$ | Bounded inputs needed |
| Log transform | $\log(1+x)$ | Right-skewed counts, prices |

**Fit scaler on train only** → [[01 Statistics & Probability/08 - Cross Validation|Cross-validation]]

---

## Too many features?

| Problem | Symptom | Actions |
|---------|---------|---------|
| Curse of dimensionality | kNN, distance methods degrade | Reduce $p$, PCA, selection |
| Multicollinearity | Unstable linear coefficients | Ridge, drop correlated cols |
| Overfitting | Train great, test poor | Regularization, more data, simpler model |

**Variable selection:** filter (correlation), wrapper (RFE), embedded (Lasso, tree importance).

---

## Heteroskedasticity (regression)

Variance of residuals changes with $x$ → unreliable SE.  
**Fixes:** log-transform $y$, robust SE, weighted least squares (WLS).

---

**Next:** [[08 - Overfitting]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Random Forest reduces bias | RF reduces **variance** (bagging); boosting reduces **bias** |
| Logistic regression needs linearly separable data | Separable data can cause huge weights — use **regularization** |
| k-means always finds global optimum | k-means finds **local** optima; restart with different inits |
