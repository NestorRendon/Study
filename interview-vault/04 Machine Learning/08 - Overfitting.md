# Overfitting (Classical ML)

**Prev:** [[07 - Feature Engineering]] · **Next:** [[05 Deep Learning/01 - Bias-Variance Tradeoff|Chapter 5 — Bias-Variance]]

---

## Interview one-liner

Model **memorizes training data** (low train error) but fails on new data (high test error). Fix with more data, simpler models, or **regularization**.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Signature

| Split | Error |
|-------|-------|
| Training | Low ↓ |
| Test | High ↑ |

---

## Techniques (classical)

| Method | Mechanism |
|--------|-----------|
| More data | Reduces variance |
| Simpler model | Fewer DOF (shallow tree, smaller $k$ in KNN) |
| **Regularization** | Penalize large weights → next chapter |
| Cross-validation | Tune complexity without leaking |
| Pruning (trees) | Stop splits early |
| Ensemble (RF) | Average high-variance learners |

---

## Bridge to Deep Learning

Classical overfitting → same **bias–variance** language, plus:

- Dropout, batch norm, early stopping
- $L_1$ / $L_2$ weight decay

**Read next (in order):**

1. [[05 Deep Learning/01 - Bias-Variance Tradeoff]]
2. [[05 Deep Learning/02 - Learning Curves]]
3. [[05 Deep Learning/04 - Regularization L1 and L2]]

---

**Next:** [[09 - Class Imbalance]] · then [[05 Deep Learning/00 - Chapter Overview|Deep Learning]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Random Forest reduces bias | RF reduces **variance** (bagging); boosting reduces **bias** |
| Logistic regression needs linearly separable data | Separable data can cause huge weights — use **regularization** |
| k-means always finds global optimum | k-means finds **local** optima; restart with different inits |
