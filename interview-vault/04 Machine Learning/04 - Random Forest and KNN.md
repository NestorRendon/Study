# Random Forest & KNN

**Prev:** [[03 - Decision Trees]] · **Next:** [[05 - K-Means]]

---

## Random Forest

**Idea:** Train many trees on **bootstrap samples** + random feature subsets at each split → **average** predictions.

| Effect | Why |
|--------|-----|
| ↓ Variance | Decorrelated trees |
| Slight ↑ bias | Individual trees still biased |

**Interview line:** "Bagging reduces variance without increasing bias as much as boosting increases complexity."

![Ensemble overview](assets/5887B2B8-6F43-4D70-AF42-0DB3B3AC9248.png)

---

## K-Nearest Neighbors (KNN)

**Classification:** majority vote of $k$ nearest points.  
**Regression:** average of $k$ neighbors' targets.

**Distance (Euclidean):** $d(\mathbf{x},\mathbf{x}') = \|\mathbf{x} - \mathbf{x}'\|_2$

| Hyperparameter | Effect |
|----------------|--------|
| $k$ small | Low bias, **high variance** (overfit) |
| $k$ large | High bias, low variance (underfit) |

**Always scale features** — KNN is distance-based.

![KNN context](assets/57A8D45A-CED8-4838-AFE9-340A987DD8E0.png)

---

## Bias–variance snapshot

| Model | Bias | Variance |
|-------|------|----------|
| Full tree | Low | High |
| Random Forest | Low | Medium |
| KNN ($k$ small) | Low | High |

→ Full framework: [[05 Deep Learning/01 - Bias-Variance Tradeoff]]

---

**Next:** [[05 - K-Means]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Random Forest reduces bias | RF reduces **variance** (bagging); boosting reduces **bias** |
| Logistic regression needs linearly separable data | Separable data can cause huge weights — use **regularization** |
| k-means always finds global optimum | k-means finds **local** optima; restart with different inits |
