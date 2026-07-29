# Class Imbalance

**Prev:** [[08 - Overfitting]] · **Next:** [[10 - Boosting vs Bagging]]

---

## In plain English

95% negative, 5% positive → a model predicting **always negative** gets 95% accuracy but is **useless**. You must change metrics or training.

---

## Interview one-liner

Never trust accuracy alone. Use **precision, recall, F1, PR-AUC**, and align metric with business cost of FP vs FN.

---

## Strategies (pragmatic)

| Strategy | When |
|----------|------|
| **Class weights** | sklearn `class_weight='balanced'` |
| **Resampling** | SMOTE (synthetic minority), undersample majority |
| **Threshold tuning** | Move decision threshold on validation set |
| **Different metric** | Optimize F1 or cost-weighted loss |
| **Anomaly detection** | Extreme rarity — treat minority as anomalies |

---

## Confusion matrix reminder

| Business cost | Optimize |
|---------------|----------|
| Missing fraud (FN) costly | **Recall** |
| False alarm (FP) costly | **Precision** |

→ [[01 Statistics & Probability/06 - Classification Metrics]]

---

## Common traps

| Trap | Correct |
|------|---------|
| Accuracy 99% on imbalanced data | Check **confusion matrix** |
| SMOTE on test set | Resample **train only** |
| Random split for time series | Time-based split |

---

**Next:** [[10 - Boosting vs Bagging]]
