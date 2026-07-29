# Boosting vs Bagging

**Prev:** [[09 - Class Imbalance]] · **Next:** [[05 Deep Learning/00 - Chapter Overview]]

---

## In plain English

**Bagging** trains many models on random subsets and **averages** — reduces **variance** (Random Forest).  
**Boosting** trains models **sequentially**, each fixing previous errors — reduces **bias** (AdaBoost, XGBoost, LightGBM).

---

## Comparison

| | Bagging (RF) | Boosting (XGBoost) |
|---|--------------|---------------------|
| Training | Parallel trees | Sequential |
| Main effect | ↓ Variance | ↓ Bias |
| Overfitting risk | Moderate | Can overfit if not tuned |
| Tabular Kaggle classic | Strong baseline | Often wins |

---

## Random Forest (bagging)

- Bootstrap samples + random feature subsets at splits
- **Interview:** "decorrelates trees, averages reduce variance"

---

## Gradient boosting (concept)

Fit weak learner $h_1$, compute residuals, fit $h_2$ on residuals, …

$$F_m(x) = F_{m-1}(x) + \eta \cdot h_m(x)$$

| Symbol | Meaning |
|--------|---------|
| $\eta$ | Learning rate (shrinkage) |
| $h_m$ | Weak tree (shallow) |

**XGBoost / LightGBM:** regularized, efficient — default for structured/tabular data in industry.

---

## When to use (pragmatic)

| Data | Try first |
|------|-----------|
| Tabular, heterogeneous features | XGBoost / LightGBM |
| Need interpretability | Single tree or linear + SHAP |
| High-dimensional sparse text | Linear / logistic + regularization |
| Images | CNN (not XGBoost) |

---

## Common traps

| Trap | Correct |
|------|---------|
| "RF reduces bias" | RF reduces **variance** |
| "Boosting can't overfit" | Can — tune trees, η, early stopping |
| Use test set for early stopping | Use **validation** set |

---

**Next chapter:** [[05 Deep Learning/00 - Chapter Overview]]
