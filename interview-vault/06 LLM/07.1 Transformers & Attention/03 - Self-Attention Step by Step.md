# Self-Attention Step by Step

**Prev:** [[02 - Embeddings and Positional Encoding]] · **Next:** [[04 - Multi-Head Attention]]

---

## In plain English

For **each token**, attention answers: *"Which other tokens should I listen to right now, and how much?"*

**Output** of self-attention = a new $S \times D$ matrix where every row is a **context-aware** vector (mixed from all tokens).

---

## Inputs and outputs (whole module)

| | Tensor | Shape (no batch) | Shape (with batch) |
|---|--------|------------------|---------------------|
| **Input** | $X$ (embed + position) | $S \times D$ | $B \times S \times D$ |
| **Output** | $\text{Attention}(X)$ | $S \times D$ | $B \times S \times D$ |

Same rank in and out — attention **replaces** representations with contextualized ones (before residual add in the full block).

---

## The Q, K, V intuition

From each row of $X$, three learned linear maps:

| Vector | Role | Analogy |
|--------|------|---------|
| **Query (Q)** | What am I looking for? | Your question |
| **Key (K)** | What do I advertise? | Index on a filing cabinet |
| **Value (V)** | What content do I pass if selected? | Document inside |

$$\mathbf{q}_i = W_Q \mathbf{x}_i, \quad \mathbf{k}_i = W_K \mathbf{x}_i, \quad \mathbf{v}_i = W_V \mathbf{x}_i$$

| Projection | Input | Output (per batch) |
|------------|-------|---------------------|
| $W_Q$ | $B \times S \times D$ | $B \times S \times d_k$ |
| $W_K$ | $B \times S \times D$ | $B \times S \times d_k$ |
| $W_V$ | $B \times S \times D$ | $B \times S \times d_v$ |

**Trap:** Q, K, V are **not** the embedding — separate learned matrices.

![QKV intuition](assets/F4069321-F883-4073-AC4E-57CA33AC9DAE.png)

---

## Six steps — inputs & outputs per step

Example sentence: `"The cat sat"` ($S=3$). Fix one **query position** (e.g. **cat**).

| Step | What you compute | Input(s) | Output | Shape |
|------|------------------|----------|--------|-------|
| **1** | Project Q, K, V | $X$ | $Q, K, V$ | $S \times d_k$ (each) |
| **2** | Scores for position *cat* | $\mathbf{q}_{cat}$, all $\mathbf{k}_j$ | 3 scores | $S$ (one row) |
| **3** | Scale | scores | scaled | $S$ |
| **4** | Softmax | scaled scores | weights $\alpha$ | $S$, sum to 1 (see [[03 Mathematics/06 - Softmax Function]]) |
| **5** | Weight values | $\alpha_j$, all $\mathbf{v}_j$ | weighted vectors | $S \times d_v$ then sum |
| **6** | Sum | weighted Vs | $\mathbf{o}_{cat}$ | $d_v$ (one row of output) |

Repeat step 2–6 for **every** query position → full output matrix $S \times d_v$ (then $W_O$ → $S \times D$ in multi-head).

---

## Matrix form (all positions at once)

$$\text{Attention}(Q, K, V) = \underbrace{\text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)}_{\text{weights } A \;\; (S \times S)} \underbrace{V}_{S \times d_v}$$

| Symbol | Shape | Meaning |
|--------|-------|---------|
| $Q$ | $S \times d_k$ | All queries (one per token) |
| $K$ | $S \times d_k$ | All keys |
| $V$ | $S \times d_v$ | All values |
| $QK^\top$ | $S \times S$ | Score: row $i$ = how much token $i$ attends to each key |
| $A$ (after softmax) | $S \times S$ | Row $i$ sums to 1 |
| $AV$ | $S \times d_v$ | New contextualized vectors |
| Final (single head) | $S \times d_v$ | Often $d_v = d_k$ |

**Softmax axis:** each **row** $i$ of $QK^\top$ → distribution over **keys** (columns).

![Matrix attention](assets/DCBD8174-C5BD-4936-87AC-F32FAA491676.png)

### Paper Figure 2 (scaled dot-product)

![Scaled dot-product attention (Vaswani et al. 2017)](assets/transformer-paper-figure2-attention.png)

| Box in figure | Input | Output |
|---------------|-------|--------|
| MatMul | $Q$, $K$ | $S \times S$ |
| Scale | scores | $S \times S$ |
| Mask (opt.) | scores | $S \times S$ |
| SoftMax | scores | $S \times S$ |
| MatMul | weights, $V$ | $S \times d_v$ |

---

## Tiny numeric sketch ($S=2$, $d_k=2$)

$$Q = K = \begin{bmatrix}1&0\\0&1\end{bmatrix},\quad V = \begin{bmatrix}1\\2\end{bmatrix}$$

| Step | Result |
|------|--------|
| $QK^\top$ | $\begin{bmatrix}1&0\\0&1\end{bmatrix}$ |
| Softmax(rows) | identity weights |
| Output rows | $(1, 2)^\top$ — each position only attends to itself |

If off-diagonal scores were large, row $i$ would **blend** other rows of $V$.

---

## Why scale by $\sqrt{d_k}$?

| Without scale | With scale |
|---------------|------------|
| Dot products grow with $d_k$ | Variance stabilized |
| Softmax → one-hot | Softer weights, trainable gradients |

---

## Self-attention vs cross-attention (I/O difference)

| Type | Q from | K, V from | Attention matrix shape |
|------|--------|-----------|-------------------------|
| **Self** | same seq $S$ | same seq $S$ | $S \times S$ |
| **Cross** | decoder $T$ | encoder $S$ | $T \times S$ |

---

## Interview one-liner

> "Input $S \times D$ embeddings; project to Q, K, V; form $S \times S$ attention weights via softmax of scaled $QK^\top$; output $S \times D$ contextualized vectors as weighted sums of V."

---

## Common traps

| Trap | Correct |
|------|---------|
| Output shape changes rank | Still $S \times D$ (before residual) |
| Softmax over query dimension | Softmax over **key** dimension (columns per row) |
| QKV are embeddings | **Projections** of embeddings |

---

**Next:** [[04 - Multi-Head Attention]] · Big O: [[09 - Complexity Big O]]
