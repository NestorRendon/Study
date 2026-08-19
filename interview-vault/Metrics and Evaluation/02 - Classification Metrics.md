# Classification Metrics

**Prev:** [[01 - Regression Metrics]] · **Next:** [[03 - Ranking Clustering and Quality Metrics]]

---

## Interview one-liner

Accuracy lies on imbalanced data. Everything else in this note exists to answer one question more honestly: **precision** asks "of what I flagged positive, how much was right?"; **recall** asks "of what was actually positive, how much did I catch?" — and the right metric is whichever one matches the cost of being wrong.

---

## In plain English

Imagine a model that screens for a rare disease that affects 1 in 1,000 people. A model that always says "healthy" is **99.9% accurate** — and completely useless. This is why accuracy alone is a trap the moment classes are imbalanced, which is most of the time in the real world (fraud, churn, disease, spam, defects).

*The basics also live at [[01 Statistics & Probability/06 - Classification Metrics]] — this note adds the metrics you'll get asked about beyond the first four.*

---

## Confusion matrix

|  | Predicted + | Predicted − |
|--|--------------|--------------|
| **Actual +** | TP (true positive) | FN (false negative) |
| **Actual −** | FP (false positive) | TN (true negative) |

Every metric below is just a different ratio of these four numbers.

---

## Core equations

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

$$\text{Precision} = \frac{TP}{TP + FP} \qquad \text{Recall (Sensitivity, TPR)} = \frac{TP}{TP + FN} \qquad \text{Specificity (TNR)} = \frac{TN}{TN + FP}$$

$$F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} \qquad F_\beta = (1+\beta^2) \cdot \frac{\text{Precision} \cdot \text{Recall}}{\beta^2 \cdot \text{Precision} + \text{Recall}}$$

$$\text{MCC} = \frac{TP \cdot TN - FP \cdot FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$$

$$\text{Log Loss} = -\frac{1}{n}\sum_{i=1}^n \left[y_i \log(\hat{p}_i) + (1-y_i)\log(1-\hat{p}_i)\right]$$

---

## What each one is actually for

| Metric | What it answers | Real example |
|--------|--------------------|----------------|
| **Precision** | Of everything I flagged positive, how much was actually positive? | Spam filter: you'd rather miss some spam than block a real email — optimize precision |
| **Recall** | Of everything actually positive, how much did I catch? | Cancer screening: missing a real case is far worse than a false alarm — optimize recall |
| **Specificity** | Of everything actually negative, how much did I correctly clear? | Rarely reported alone, but pairs with recall to draw the ROC curve |
| **$F_1$** | A single number balancing precision and recall equally | Default "how good is this classifier" number when both error types matter similarly |
| **$F_\beta$** | Same idea, but weighted — $\beta > 1$ favors recall, $\beta < 1$ favors precision | $F_2$ for a fraud model where missing fraud is costlier than a false alarm |
| **MCC (Matthews Correlation Coefficient)** | A single, balanced score even under severe imbalance — ranges $-1$ to $+1$ | Often preferred over $F_1$ on very imbalanced datasets, because it uses all four confusion-matrix cells |
| **Log loss (cross-entropy)** | Not just "right or wrong," but **how confident** was the wrong answer | Penalizes a model that says "99% sure" and is wrong far more than one that says "51% sure" and is wrong |

---

## Threshold-independent metrics: ROC-AUC vs PR-AUC

A classifier outputs a *probability*, not a label — you pick a threshold (commonly 0.5) to turn it into a decision. ROC-AUC and PR-AUC measure quality **across every possible threshold at once**.

$$\text{ROC curve: } \text{TPR (Recall)} \text{ vs } \text{FPR} = \frac{FP}{FP+TN}, \text{ at every threshold}$$

$$\text{AUC} = \int_0^1 \text{TPR}(\text{FPR})\, d(\text{FPR}) \quad \text{— probability a random positive scores higher than a random negative}$$

| | ROC-AUC | PR-AUC |
|---|---------|--------|
| **Plots** | TPR vs FPR | Precision vs Recall |
| **Good default when** | Classes are roughly balanced | Classes are **imbalanced** — ROC-AUC can look deceptively high while precision is terrible, because FPR is diluted by a huge number of true negatives |
| **Real example** | Comparing two models on a balanced A/B test | Fraud detection, where positives are <1% of traffic |

---

## Multiclass averaging

When there are more than 2 classes, precision/recall/F1 need to be combined somehow:

| Averaging | How it's computed | When to use |
|-----------|------------------------|---------------|
| **Macro** | Compute per-class, then average unweighted | Every class matters equally, even rare ones |
| **Weighted** | Compute per-class, average weighted by class support (frequency) | Care about overall performance, but classes are imbalanced |
| **Micro** | Pool all TP/FP/FN across classes first, then compute once | Care about overall correctness across every prediction equally — dominated by the most frequent class |

---

## Common traps

| Trap | Why it's wrong | What to say instead |
|------|------------------|----------------------|
| "My model is 99% accurate" on a 1%-positive-rate dataset | A model that always predicts negative gets the same score | "I'd check precision/recall/F1 per class, or PR-AUC, not accuracy" |
| Reporting ROC-AUC on a heavily imbalanced dataset without also reporting PR-AUC | ROC-AUC can stay high even when precision is unusable, because FPR is diluted by the huge number of negatives | "I'd lead with PR-AUC here, and mention ROC-AUC only as a secondary number" |
| Picking $F_1$ by default without asking about costs | $F_1$ assumes precision and recall matter equally — rarely true in practice | "I'd ask which error is more expensive first, then pick $F_\beta$ or a cost-weighted metric" |
| Optimizing accuracy but evaluating with a probability threshold no one chose deliberately | The default 0.5 threshold is rarely the business-optimal cutoff | "I'd tune the threshold on a validation set against the actual cost of FP vs FN" |

---

**Next:** [[03 - Ranking Clustering and Quality Metrics]]
