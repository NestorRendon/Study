# Similarity, Correlation & Convolution

**Prev:** [[01 - Linear Algebra Essentials]] · **Next:** [[03 - Gradients and Partial Derivatives]]

---

## In plain English

ML constantly asks: *"How alike are two things?"* — two vectors (RAG), two variables (EDA), or a **pattern sliding over a signal** (CNN). This note ties **dot product**, **cosine**, **Pearson correlation**, and **convolution** on one map.

---

## Family tree

| Idea | Compares | Scale-sensitive? | Typical use |
|------|----------|------------------|-------------|
| **Dot product** | $\mathbf{a} \cdot \mathbf{b}$ | **Yes** (magnitude matters) | Attention scores $QK^\top$ |
| **Cosine similarity** | angle between vectors | **No** (length normalized) | Embeddings, RAG retrieval |
| **Pearson correlation** | linear relationship | Standardized (unitless) | Features, EDA, multicollinearity |
| **Convolution** | local pattern match | Learned kernel weights | CNNs, time series |

---

## Dot product (baseline)

$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{d} a_i b_i = \|\mathbf{a}\| \|\mathbf{b}\| \cos\theta$$

| Input | Output |
|-------|--------|
| Two vectors $\mathbb{R}^d$ | One scalar |

**Interpretation:** large when vectors point the same direction **and** are long.

→ [[01 - Linear Algebra Essentials]]

---

## Cosine similarity

$$\cos(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \, \|\mathbf{b}\|}$$

| Property | Value |
|----------|-------|
| Range | $[-1, 1]$ (often $[0,1]$ for non-negative embeddings) |
| $\cos = 1$ | Same direction |
| $\cos = 0$ | Orthogonal (unrelated in angle) |
| $\cos = -1$ | Opposite direction |

### Why RAG uses cosine

Embedding APIs often **normalize** vectors to unit length. Then:

$$\|\mathbf{a}\| = \|\mathbf{b}\| = 1 \quad \Rightarrow \quad \mathbf{a} \cdot \mathbf{b} = \cos(\mathbf{a}, \mathbf{b})$$

| Metric | When lengths matter |
|--------|---------------------|
| Dot product | Raw attention, unnormalized features |
| **Cosine** | Semantic search — "meaning direction" not document length |

→ [[08 RAG & Retrieval/03 - Embedding Model Choice]] · [[08 RAG & Retrieval/04 - Indexing and Vector Stores]]

### Tiny example

$\mathbf{a} = (1, 2),\; \mathbf{b} = (2, 4)$ — same direction, $b = 2a$:

$$\cos = \frac{1\cdot2 + 2\cdot4}{\sqrt{5}\sqrt{20}} = 1$$

$\mathbf{c} = (2, -1)$ — different direction → $\cos < 1$.

### NumPy / PyTorch

```python
import numpy as np
a, b = np.array([1.0, 2.0]), np.array([2.0, 4.0])
cos = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
# sklearn: cosine_similarity([a], [b])
```

---

## Pearson correlation

For paired samples $(x_i, y_i)$, $i = 1..n$:

$$r = \frac{\sum_i (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_i (x_i - \bar{x})^2}\sqrt{\sum_i (y_i - \bar{y})^2}}$$

| Property | Meaning |
|----------|---------|
| $r \in [-1, 1]$ | Linear association strength |
| $r = 1$ | Perfect positive linear |
| $r = 0$ | No **linear** correlation (nonlinear can still exist) |
| Invariant | Adding constants / scaling (linear) does not change $r$ |

### Cosine vs Pearson (interview)

| | Cosine | Pearson |
|---|--------|---------|
| **Objects** | Two vectors (same dim) | Two **aligned** sequences of measurements |
| **Centering** | No (uses raw dot + norms) | **Yes** — subtract means |
| **Same formula?** | On **mean-centered** vectors, cosine = Pearson |

### When to use in ML

| Use | Tool |
|-----|------|
| Feature redundancy | $|r| > 0.9$ → consider dropping one |
| EDA | Linear relationships |
| **Not** causation | Correlation ≠ cause → [[02 Bayesian & Causal Inference/05 - Structure Learning]] |

---

## Other similarity metrics (brief)

| Metric | Formula idea | Use |
|--------|--------------|-----|
| **Euclidean distance** | $\|\mathbf{a} - \mathbf{b}\|_2$ | k-NN, clustering (lower = closer) |
| **Manhattan** | $\sum |a_i - b_i|$ | Robust sparse |
| **Jaccard** | intersection / union | Sets, tokens (not vectors) |
| **Hamming** | bit differences | Binary codes |

**RAG note:** pgvector supports `<->` L2 and `<=>` cosine — pick one and stay consistent.

---

## Convolution (1D)

Discrete convolution of signal $f$ with kernel $k$:

$$(f * k)(t) = \sum_s f(s)\, k(t - s)$$

| Symbol | Role |
|--------|------|
| $f$ | Input (audio, time series, 1D feature map) |
| $k$ | **Kernel** — small pattern to detect |
| $*$ | Slide, multiply, sum |

### CNN view (cross-correlation in practice)

Deep learning frameworks use **cross-correlation** (no kernel flip); still called "conv":

$$(f \star k)(t) = \sum_s f(s)\, k(t + s)$$

| Hyperparameter | Effect |
|----------------|--------|
| **Kernel size** $k$ | Receptive field width |
| **Stride** $s$ | Downsample speed |
| **Padding** $p$ | Keep spatial size |

**Output length (1D):**

$$\text{out} = \left\lfloor \frac{n - k + 2p}{s} \right\rfloor + 1$$

### 2D (images)

Kernel slides over **height × width**; learns edges, textures, then deeper patterns.

```
Input H×W  *  Kernel k×k  →  Feature map
```

| CNN idea | Convolution gives |
|----------|-------------------|
| **Local connectivity** | Each output pixel sees only a patch |
| **Weight sharing** | Same kernel everywhere → translation equivariance |

→ [[05 Deep Learning/12 - Convolutional Neural Networks]] · [[11 Computer Vision/00 - Chapter Overview]]

### Dot product vs convolution

| | Dot product | Convolution |
|---|-------------|-------------|
| **Compare** | One pair of vectors | Pattern vs **every local patch** |
| **Output** | Single scalar | **Map** of responses |
| **Weights** | Fixed vectors | **Learned** kernel |

One conv output cell ≈ dot product between kernel and one local patch.

---

## Where each appears (cheat sheet)

| Domain | Metric / op |
|--------|-------------|
| RAG / embeddings | **Cosine** |
| Transformer attention | **Dot product** + scale + softmax |
| Feature EDA | **Pearson** |
| Images / audio CNN | **Convolution** |
| k-NN clustering | **Euclidean** |

---

## Common traps

| Trap | Correct |
|------|---------|
| "Cosine and dot always rank the same" | Longer vectors boost dot product |
| "Correlation 0 = independent" | Only **linear** unrelated |
| "Convolution = correlation" | DL uses cross-correlation; different flip convention |
| Mix cosine index with L2 query | **Same metric** for index and query |

---

## Interview one-liner

> "Cosine measures directional similarity for embeddings; Pearson measures linear association with mean-centering; convolution slides a learned kernel to build translation-aware feature maps in CNNs."

---

**Next:** [[03 - Gradients and Partial Derivatives]]
