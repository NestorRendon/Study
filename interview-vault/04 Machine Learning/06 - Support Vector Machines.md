# Support Vector Machines (SVM)

**Prev:** [[05 - K-Means]] · **Next:** [[07 - Feature Engineering]]

---

## Interview one-liner

Find the **maximum-margin** hyperplane separating classes. **Kernel trick** maps data to higher dimensions for non-linear boundaries without computing coordinates explicitly.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Hard-margin (separable)

$$\min_{\mathbf{w}, b} \frac{1}{2}\|\mathbf{w}\|^2 \quad \text{s.t.} \quad y_i(\mathbf{w}^T\mathbf{x}_i + b) \ge 1$$

| Symbol | Meaning |
|--------|---------|
| Margin | $2/\|\mathbf{w}\|$ |
| Support vectors | Points on margin boundary |

---

## Soft-margin (non-separable)

$$\min \frac{1}{2}\|\mathbf{w}\|^2 + C \sum_i \xi_i$$

- $C$ **large** → narrow margin, fewer errors, **more overfitting**
- $C$ **small** → wider margin, more slack → **more regularization**

---

## Kernel trick

$$K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j)$$

Common: RBF $K(\mathbf{x},\mathbf{x}') = \exp(-\gamma\|\mathbf{x}-\mathbf{x}'\|^2)$.

![SVM](assets/8FAF55BE-204F-40D9-A3C1-C5134B2B3748.png)

---

## vs Logistic Regression

| | Logistic | SVM |
|---|----------|-----|
| Focus | Probabilities | Margin |
| Outliers | All points influence | Support vectors dominate |
| Kernels | Less common | Native strength |

---

**Next:** [[07 - Feature Engineering]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Random Forest reduces bias | RF reduces **variance** (bagging); boosting reduces **bias** |
| Logistic regression needs linearly separable data | Separable data can cause huge weights — use **regularization** |
| k-means always finds global optimum | k-means finds **local** optima; restart with different inits |
