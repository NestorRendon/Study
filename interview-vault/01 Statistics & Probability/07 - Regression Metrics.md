# Regression Metrics

**Prev:** [[06 - Classification Metrics]] · **Next:** [[08 - Cross Validation]]

---

## Interview one-liner

Regression metrics measure **distance between $\hat{y}$ and $y$**. MAE is robust; MSE penalizes large errors; MAPE is scale-relative but breaks near $y=0$.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Notation

| Symbol | Meaning |
|--------|---------|
| $y_i$ | True value |
| $\hat{y}_i$ | Prediction |
| $n$ | Number of points |
| $\bar{y}$ | Mean of $y$ |

---

## Metrics

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$$

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2, \quad \text{RMSE} = \sqrt{\text{MSE}}$$

$$\text{MAPE} = \frac{100\%}{n}\sum_{i=1}^n \left|\frac{y_i - \hat{y}_i}{y_i}\right|$$

$$R^2 = 1 - \frac{\sum_i (y_i - \hat{y}_i)^2}{\sum_i (y_i - \bar{y})^2}$$

| Metric | Pros | Cons |
|--------|------|------|
| MAE | Interpretable, robust | No heavy penalty on outliers |
| RMSE | Differentiable, penalizes large errors | Sensitive to outliers |
| MAPE | % error | Undefined / unstable if $y_i \approx 0$ |
| $R^2$ | Fraction of variance explained | Can be negative on test set |

---

**Next:** [[08 - Cross Validation]]
