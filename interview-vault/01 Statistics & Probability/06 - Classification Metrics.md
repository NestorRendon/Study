# Classification Metrics

**Prev:** [[05 - ANOVA]] · **Next:** [[07 - Regression Metrics]]

---

## Interview one-liner

Accuracy is misleading on **imbalanced** data. Pick precision, recall, or F1 based on the **cost of false positives vs false negatives**.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Confusion matrix

|  | Pred + | Pred − |
|--|--------|--------|
| **Actual +** | TP | FN |
| **Actual −** | FP | TN |

![Metrics cheat sheet](assets/2CAA96F3-6F43-42AE-8E5B-FB1DA138EA18.png)

---

## Metrics

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

$$\text{Precision} = \frac{TP}{TP + FP} \quad \text{(of predicted positives, how many correct?)}$$

$$\text{Recall} = \frac{TP}{TP + FN} \quad \text{(of actual positives, how many found?)}$$

$$F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

| Metric | Optimize when |
|--------|----------------|
| **Precision** | False positives costly (spam filter: don't block good mail) |
| **Recall** | False negatives costly (cancer screening: don't miss cases) |
| **F1** | Need balance, single number |

**ROC-AUC:** trade-off of TPR vs FPR across thresholds — threshold-independent ranking quality.

---

**Next:** [[07 - Regression Metrics]]
