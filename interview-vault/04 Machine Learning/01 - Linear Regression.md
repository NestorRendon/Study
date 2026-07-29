# Linear Regression

**Prev:** [[00 - Chapter Overview]] · **Next:** [[02 - Logistic Regression]]

---

## Interview one-liner

Predict a **continuous** target as a linear combination of features. Fit $\mathbf{w}$ by minimizing squared error (OLS) or with regularization (Ridge/Lasso).

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Model

$$\hat{y} = \mathbf{w}^T\mathbf{x} + b = \sum_{j=1}^{p} w_j x_j + b$$

| Symbol | Meaning |
|--------|---------|
| $\mathbf{x}$ | Feature vector |
| $\mathbf{w}$ | Weights |
| $b$ | Bias (intercept) |
| $\hat{y}$ | Predicted value |

---

## Loss (MSE)

$$L(\mathbf{w}) = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$

**OLS closed form:** $\hat{\mathbf{w}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$ (if $\mathbf{X}^T\mathbf{X}$ invertible).

---

## Assumptions (Gauss-Markov)

Linearity, independence, homoscedasticity, no perfect multicollinearity.  
**Heteroskedasticity:** variance of errors changes → use robust SE, transforms, or WLS.

---

## Diagrams

![Linear Regression](assets/674A1B11-5D5B-486B-80E7-C7FC60EFCEE6.png)

![Training — Gradient Descent](assets/14AFD94B-1FF1-45CF-9CD6-62867647A452.png)

---

## Extensions

| Issue | Approach |
|-------|----------|
| Non-linearity | Polynomial features, splines, GAMs |
| Many correlated features | Ridge ($L_2$) → [[05 Deep Learning/04 - Regularization L1 and L2]] |
| Interpretability | Lasso ($L_1$) → sparse $\mathbf{w}$ |

---

**Next:** [[02 - Logistic Regression]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Random Forest reduces bias | RF reduces **variance** (bagging); boosting reduces **bias** |
| Logistic regression needs linearly separable data | Separable data can cause huge weights — use **regularization** |
| k-means always finds global optimum | k-means finds **local** optima; restart with different inits |
