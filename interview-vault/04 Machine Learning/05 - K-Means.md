# K-Means Clustering

**Prev:** [[04 - Random Forest and KNN]] · **Next:** [[06 - Support Vector Machines]]

---

## Interview one-liner

**Unsupervised:** partition points into $k$ clusters by minimizing within-cluster sum of squares. Iterate assign → update centroids.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Algorithm

1. Initialize $k$ centroids $\boldsymbol{\mu}_1, \ldots, \boldsymbol{\mu}_k$.
2. **Assign:** $c_i = \arg\min_j \|\mathbf{x}_i - \boldsymbol{\mu}_j\|^2$.
3. **Update:** $\boldsymbol{\mu}_j = \frac{1}{|C_j|}\sum_{i \in C_j} \mathbf{x}_i$.
4. Repeat until convergence.

**Objective:**

$$J = \sum_{j=1}^{k}\sum_{i \in C_j} \|\mathbf{x}_i - \boldsymbol{\mu}_j\|^2$$

---

## Choosing $k$

| Method | Idea |
|--------|------|
| **Elbow** | Plot $J$ vs $k$; look for knee |
| **Silhouette** | Cohesion vs separation |
| Domain knowledge | Business interpretability |

![K-Means](assets/8408EFFF-B431-4D80-94B4-5F2432197D9E.png)

---

**Next:** [[06 - Support Vector Machines]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Random Forest reduces bias | RF reduces **variance** (bagging); boosting reduces **bias** |
| Logistic regression needs linearly separable data | Separable data can cause huge weights — use **regularization** |
| k-means always finds global optimum | k-means finds **local** optima; restart with different inits |
