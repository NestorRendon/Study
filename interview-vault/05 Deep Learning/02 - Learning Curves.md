# Learning Curves

**Prev:** [[01 - Bias-Variance Tradeoff]] · **Next:** [[03 - Loss Functions]]

---

## Interview one-liner

Plot **error vs training set size** or **error vs epochs** to see if you need more data, a bigger model, or **regularization**.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Error vs dataset size

| Pattern | Diagnosis | Action |
|---------|-----------|--------|
| Train & val both high, close | **High bias** | Bigger model, better features |
| Train low, val high, large gap | **High variance** | More data, regularization, dropout |
| Val improves with more data | Data-limited | Collect more samples |
| Val flat with more data | Model/capacity limited | Change architecture or features |

---

## Error vs epochs (training)

| Phase | Train loss | Val loss |
|-------|------------|----------|
| Early | Decreasing | Decreasing |
| Overfitting starts | Still ↓ | Starts ↑ |

→ Use **early stopping** when val loss stops improving: [[06 - Early Stopping]]

---

## Epoch graph vs dataset size (senior topic)

**Epoch graph:** performance vs training iterations at fixed data size.  
**Dataset size graph:** performance vs $n$ at fixed architecture.

Together they tell you whether to train longer, get more data, or change model capacity.

---

**Next:** [[03 - Loss Functions]]
