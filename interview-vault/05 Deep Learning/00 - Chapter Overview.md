# Chapter 5 — Deep Learning

---

## The story

1. **Diagnose** — bias vs variance ([[01 - Bias-Variance Tradeoff]])
2. **Read learning curves** — under/overfit signals ([[02 - Learning Curves]])
3. **Pick loss** — match task ([[03 - Loss Functions]])
4. **Regularize weights** — L1/L2 ([[04 - Regularization L1 and L2]])
5. **Regularize activations** — dropout ([[05 - Dropout]])
6. **Stop early** — validation-based ([[06 - Early Stopping]])
7. **Scale inputs** — stable training ([[07 - Feature Scaling for Neural Nets]])
8. **Optimize** — SGD, Adam ([[08 - Optimizers SGD Adam]]) · code: [[13 Software Engineering & Python/11 - PyTorch Essentials]]
9. **Tune batch vs LR** — throughput vs stability ([[09 - Batch Size vs Learning Rate]])
10. **Normalize batches** — batch norm ([[10 - Batch Normalization]])
11. **Sequences** — RNN/LSTM/GRU ([[11 - RNN LSTM and GRU]])
12. **Images** — CNNs ([[12 - Convolutional Neural Networks]])
13. **Debug failures** — systematic fixes ([[13 - Diagnosing Neural Network Failures]])

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | Bias–variance | [[01 - Bias-Variance Tradeoff]] |
| 2 | Learning curves | [[02 - Learning Curves]] |
| 3 | Loss functions | [[03 - Loss Functions]] |
| 4 | Regularization L1/L2 | [[04 - Regularization L1 and L2]] |
| 5 | Dropout | [[05 - Dropout]] |
| 6 | Early stopping | [[06 - Early Stopping]] |
| 7 | Feature scaling | [[07 - Feature Scaling for Neural Nets]] |
| 8 | Optimizers | [[08 - Optimizers SGD Adam]] |
| 9 | Batch size vs LR | [[09 - Batch Size vs Learning Rate]] |
| 10 | Batch normalization | [[10 - Batch Normalization]] |
| 11 | **RNN / LSTM / GRU** | [[11 - RNN LSTM and GRU]] |
| 12 | CNNs | [[12 - Convolutional Neural Networks]] |
| 13 | Diagnosing failures | [[13 - Diagnosing Neural Network Failures]] |

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Transformers** replaced RNNs for most NLP | Still know RNN for series + interviews |
| **Vision transformers (ViT)** | CNN + transformer hybrids common |
| **Foundation models** | Pretrain huge, fine-tune small (LoRA, Ch 7) |
| **Efficient inference** | Quantization (INT8/4), distillation, TensorRT |
| **Mamba / SSM** | Long-sequence alternative to attention |

---

## Common traps

| Trap | Correct |
|------|---------|
| Regularization fixes underfitting | Reg targets **overfitting** |
| Dropout at inference | Off or scaled weights |
| "RNNs are obsolete" | Wrong for streaming/time series narrative |

---

**Prev:** [[04 Machine Learning/00 - Chapter Overview]] · **Next:** [[06 NLP & Text Mining/00 - Chapter Overview]]

[[Home|← Home]]
