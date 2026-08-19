# Softmax Function

**Prev:** [[05 - Convexity]] · **Next:** [[04 Machine Learning/00 - Chapter Overview|Machine Learning (Ch 4)]]

---

## In plain English

**Softmax** turns a vector of **raw scores** (logits) into a **probability distribution** over $K$ classes:

- every value is between 0 and 1  
- all values **sum to 1**  
- larger logit → larger probability  

Used in: **multi-class classification** (with cross-entropy), **attention weights** (over keys), **MoE routing**, **language model** next-token distribution.

---

## Definition

For logits $\mathbf{z} = (z_1, z_2, \ldots, z_K)$:

$$\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}} = p_i$$

| Symbol | Name | Meaning |
|--------|------|---------|
| $z_i$ | logit | Unnormalized score for class $i$ |
| $p_i$ | probability | $P(y = i \mid \mathbf{x})$ after softmax |
| $K$ | num classes | Or num tokens (vocab) in LLMs |

**Vector form:** $\mathbf{p} = \text{softmax}(\mathbf{z})$ where $\sum_i p_i = 1$.

---

## Tiny example ($K=3$)

Logits: $\mathbf{z} = (2.0,\; 1.0,\; 0.1)$

| Step | Class 0 | Class 1 | Class 2 |
|------|---------|---------|---------|
| $e^{z_i}$ | 7.39 | 2.72 | 1.11 |
| Sum | | | 11.22 |
| $p_i = e^{z_i}/\sum$ | **0.66** | 0.24 | 0.10 |

Class 0 wins — softmax **amplifies** the largest score but keeps others non-zero.

---

## Why not just normalize scores?

| Approach | Problem |
|----------|---------|
| Divide by sum of raw $z_i$ | Negative logits break; not invariant to adding constants |
| Argmax only | Not differentiable — can't train with gradient descent |
| **Softmax** | Smooth, differentiable, invariant to $\mathbf{z} + c$ (same $p$) |

**Invariance:** $\text{softmax}(\mathbf{z}) = \text{softmax}(\mathbf{z} + c)$ for any constant $c$ — only **relative** differences matter.

---

## Binary case: softmax = sigmoid

Two classes with logit $z$:

$$p_1 = \frac{e^z}{e^z + e^0} = \frac{1}{1 + e^{-z}} = \sigma(z)$$

So **sigmoid** is softmax with 2 classes (one logit).

→ [[04 Machine Learning/02 - Logistic Regression]]

---

## Where softmax appears

| Use | Input | Output | Softmax over |
|-----|-------|--------|--------------|
| Classifier head | $K$ logits | $K$ class probs | classes |
| LLM next token | $V$ logits | $V$ token probs | vocabulary |
| Attention | $S$ scores per row | $S$ weights | **keys** (one row per query) |
| MoE router | $E$ expert scores | $E$ gate weights | experts |

---

## Cross-entropy loss (training)

True one-hot label $\mathbf{y}$, predicted $\mathbf{p} = \text{softmax}(\mathbf{z})$:

$$L = -\sum_{k=1}^{K} y_k \log p_k$$

For correct class $c$ only: $L = -\log p_c$ — **punishes** low probability on the right class.

**Why pair them:** gradient of CE + softmax has a clean form → stable training.

→ [[05 Deep Learning/03 - Loss Functions]]

---

## Numerical stability (implementation)

$e^{z_i}$ overflows for large $z_i$. Standard trick — subtract max:

$$\text{softmax}(z_i) = \frac{e^{z_i - \max(\mathbf{z})}}{\sum_j e^{z_j - \max(\mathbf{z})}}$$

In PyTorch: `F.softmax(z, dim=-1)` or `F.log_softmax` + NLLLoss (avoids log of tiny $p$).

---

## Temperature scaling

$$\text{softmax}(z_i / T)$$

| $T$ | Effect |
|-----|--------|
| $T = 1$ | Default |
| $T > 1$ | Softer distribution (more uncertain) |
| $T < 1$ | Sharper (more peaky, closer to argmax) |

Used in: LLM sampling, **calibration** of classifier confidence.

---

## Attention: softmax on a different axis

In transformers, for **one query row** $i$:

$$\alpha_{ij} = \frac{e^{s_{ij}}}{\sum_{j'} e^{s_{ij'}}}$$

| | Classification | Attention |
|---|----------------|-------------|
| Input | $K$ logits | $S$ attention scores |
| Output | $K$ class probs | $S$ weights summing to 1 |
| Meaning | $P(\text{class})$ | how much token $i$ listens to token $j$ |

→ [[03 - Self-Attention Step by Step]]

---

## Common traps

| Trap | Correct |
|------|---------|
| "Softmax output is logits" | Output is **probabilities**; logits are **before** softmax |
| "Softmax and sigmoid unrelated" | Sigmoid is 2-class softmax |
| Softmax over wrong dimension | Specify **dim** (classes, keys, vocab) |
| Compute $p$ then `log(p)` in code | Use **log-softmax** for stability |

---

## Interview one-liner

> "Softmax maps logits to a valid probability simplex — differentiable, emphasizes the largest score, and pairs with cross-entropy for classification and with dot-product scores for attention weights."

---

**Next:** [[04 Machine Learning/00 - Chapter Overview]] · Training: [[05 Deep Learning/08 - Optimizers SGD Adam]] · Similarity: [[02 - Similarity Correlation and Convolution]]
