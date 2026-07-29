# Logistic Regression

**Prev:** [[01 - Linear Regression]] · **Next:** [[03 - Decision Trees]]

---

## Interview one-liner

**Binary classification** via a linear score passed through a **sigmoid** → probability, then threshold at 0.5. Linear **decision boundary** in feature space.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Model

$$z = \mathbf{w}^T\mathbf{x} + b, \quad \hat{p} = \sigma(z) = \frac{1}{1 + e^{-z}}$$

$$\hat{y} = \mathbb{1}[\hat{p} \ge 0.5]$$

**2-class softmax** is the same as sigmoid → multi-class: [[03 Mathematics/06 - Softmax Function]]

| Symbol | Meaning |
|--------|---------|
| $z$ | Log-odds (logit) |
| $\hat{p}$ | $P(y=1 \mid \mathbf{x})$ |

---

## Loss (binary cross-entropy)

$$L = -\frac{1}{n}\sum_i \left[ y_i \log \hat{p}_i + (1-y_i)\log(1-\hat{p}_i) \right]$$

Optimized with gradient descent (no closed form like OLS).

---

## Linear separability

| Data | Behavior |
|------|----------|
| Linearly separable | Weights can grow large → sharp boundary; use **$L_2$ regularization** (parameter `C` in sklearn = inverse reg strength) |
| Not separable | Sigmoid fits soft probabilities |

![Goal — classification](assets/729A6829-BAD9-4DD0-82FF-2EE1445A7CD3.png)

![Linear vs Logistic](assets/71A61510-8C72-4A8E-94FC-5F77CD8A8638.png)

---

**Next:** [[03 - Decision Trees]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Random Forest reduces bias | RF reduces **variance** (bagging); boosting reduces **bias** |
| Logistic regression needs linearly separable data | Separable data can cause huge weights — use **regularization** |
| k-means always finds global optimum | k-means finds **local** optima; restart with different inits |
