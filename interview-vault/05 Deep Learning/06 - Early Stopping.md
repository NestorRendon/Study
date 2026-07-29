# Early Stopping

**Prev:** [[05 - Dropout]] · **Next:** [[07 - Feature Scaling for Neural Nets]]

---

## Interview one-liner

Stop training when **validation loss** stops improving — cheapest regularization: prevents overfitting without changing the architecture.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Procedure

1. Split: train / validation (keep test untouched).
2. Each epoch: train on train, evaluate on val.
3. Save best weights when val loss improves.
4. Stop after `patience` epochs without improvement.

---

## Relation to bias–variance

| Stop point | Effect |
|------------|--------|
| Too early | High bias (underfit) |
| Too late | High variance (overfit) |
| Optimal | Best val performance |

Works with [[02 - Learning Curves]].

---

**Next:** [[07 - Feature Scaling for Neural Nets]]
