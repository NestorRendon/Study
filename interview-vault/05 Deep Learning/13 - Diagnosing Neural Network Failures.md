# Diagnosing Neural Network Failures

**Prev:** [[12 - Convolutional Neural Networks]] · **Next:** [[06 NLP & Text Mining/00 - Chapter Overview|Chapter 6 — NLP]]

---

## Interview one-liner

When a NN underperforms, check **data**, **capacity**, **optimization**, and **generalization** in that order — use learning curves and bias–variance logic.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Decision checklist

| Symptom | Likely cause | Try |
|---------|--------------|-----|
| Train & val loss high | High **bias** | Bigger model, better features, train longer |
| Train low, val high | High **variance** | [[04 - Regularization L1 and L2]], [[05 - Dropout]], more data, [[06 - Early Stopping]] |
| Loss NaN / explodes | LR too high, bad scaling | Lower $\eta$, [[07 - Feature Scaling for Neural Nets]], grad clipping |
| Train loss not decreasing | Bug, wrong labels, LR too low | Check pipeline, increase $\eta$ |
| Great offline, bad production | Distribution shift, leakage | Monitor drift, fix train/serve skew |

---

## Error analysis (senior)

1. **Slice metrics** — which subgroups fail?
2. **Confusion patterns** — systematic mislabels?
3. **Data quality** — label noise, imbalance
4. **Fairness** — disparate impact across demographics (e.g. object detection bias)

---

## Options when NN fails (summary)

| Lever | Examples |
|-------|----------|
| Data | More samples, augmentation, cleaning |
| Model | Architecture, depth, width, pretraining |
| Training | Optimizer, LR schedule, batch size |
| Regularization | $L_2$, dropout, early stopping |
| Post-hoc | Calibration, threshold tuning, ensemble |

---

**Next chapter:** [[06 NLP & Text Mining/00 - Chapter Overview]]
