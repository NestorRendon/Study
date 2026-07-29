# Chapter 3 — Mathematics for ML

---

## The story

1. **Linear algebra** — vectors, matrices, dot product ([[01 - Linear Algebra Essentials]])
2. **Similarity & convolution** — cosine, correlation, CNN math ([[02 - Similarity Correlation and Convolution]])
3. **Gradients** — which direction increases loss ([[03 - Gradients and Partial Derivatives]])
4. **Gradient descent** — batch vs SGD vs mini-batch ([[04 - Gradient Descent]])
5. **Convexity** — when you can trust a single minimum ([[05 - Convexity]])
6. **Softmax** — logits → probabilities ([[06 - Softmax Function]])

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | Linear algebra | [[01 - Linear Algebra Essentials]] |
| 2 | Cosine, correlation, convolution | [[02 - Similarity Correlation and Convolution]] |
| 3 | Gradients | [[03 - Gradients and Partial Derivatives]] |
| 4 | Gradient descent | [[04 - Gradient Descent]] |
| 5 | Convexity | [[05 - Convexity]] |
| 6 | Softmax | [[06 - Softmax Function]] |

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Automatic differentiation** | PyTorch/JAX — all deep learning |
| **Second-order methods** | Rare at LLM scale; Adam family dominates |

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| "Gradient points to minimum" | Gradient points to **steepest ascent**; go **opposite** for minimization |
| "Cosine = Pearson always" | Pearson **centers** data; cosine on raw vectors differs |
| "Correlation = causation" | Need design / DAG / RCT |
| "Convolution in DL = textbook conv" | Frameworks use **cross-correlation** (no kernel flip) |

---

**Prev:** [[01 Statistics & Probability/00 - Chapter Overview]] · **Next:** [[04 Machine Learning/00 - Chapter Overview]]

[[Home|← Home]]
