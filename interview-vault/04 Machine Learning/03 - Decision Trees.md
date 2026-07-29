# Decision Trees

**Prev:** [[02 - Logistic Regression]] · **Next:** [[04 - Random Forest and KNN]]

---

## Interview one-liner

Recursively split features to **maximize purity** in each node. Interpretable, handles non-linear boundaries, but **high variance** (overfits) alone.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Split criteria

**Classification — Gini impurity:**

$$G = 1 - \sum_{k=1}^{K} p_k^2$$

**Classification — Entropy:**

$$H = -\sum_k p_k \log p_k$$

**Regression:** minimize MSE or MAE in children.

| Symbol | Meaning |
|--------|---------|
| $p_k$ | Proportion of class $k$ in node |
| $K$ | Number of classes |

---

## Diagrams

![Decision Tree](assets/ADBFD7BD-983B-4BB4-B8B8-FD529249D665.png)

![Gini Impurity](assets/3A7153DA-FDE6-4878-B16F-991CEC141B5A.png)

---

## Pros & cons

| Pros | Cons |
|------|------|
| No feature scaling needed | Unstable (small data change → different tree) |
| Handles mixed types | Overfits without pruning/ensembles |
| Easy to explain | Axis-aligned splits only |

---

**Next:** [[04 - Random Forest and KNN]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Random Forest reduces bias | RF reduces **variance** (bagging); boosting reduces **bias** |
| Logistic regression needs linearly separable data | Separable data can cause huge weights — use **regularization** |
| k-means always finds global optimum | k-means finds **local** optima; restart with different inits |
