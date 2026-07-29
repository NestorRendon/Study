# Cross-Validation & Data Leakage

**Prev:** [[07 - Regression Metrics]] · **Next:** [[09 - PCA and Factor Analysis]]

---

## Interview one-liner

**Cross-validation** estimates how well a model **generalizes** by training on some folds and validating on held-out data. **Leakage** means training used information that would not exist at prediction time — metrics look great, production fails.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## k-fold CV

1. Split data into $k$ folds.
2. For each fold $i$: train on other $k-1$, validate on fold $i$.
3. Average validation score.

**Stratified k-fold:** preserves class proportions in each fold (classification).

![Train/validation split](assets/23A616A6-E722-4A6C-8BAE-0B9F38B80FFA.webp)

---

## Why partition?

| Goal | Method |
|------|--------|
| Tune hyperparameters | Validation set or inner CV loop |
| Final unbiased estimate | **Held-out test set** never used during tuning |
| Time series | **Time-based split** — no future in train |

---

## Data leakage (common causes)

| Leakage | Fix |
|---------|-----|
| Fit scaler on full data before split | `fit` on train only, `transform` val/test |
| Target encoding using test labels | Compute stats inside train fold only |
| Duplicate users in train and test | Group split by entity |
| Future data in time series | Rolling / expanding window validation |

---

## Rule

$$\text{split first} \rightarrow \text{fit preprocessing on train} \rightarrow \text{train model} \rightarrow \text{evaluate on val/test}$$

---

**Next:** [[09 - PCA and Factor Analysis]]
