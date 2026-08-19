# Multi-Head Attention

**Prev:** [[03 - Self-Attention Step by Step]] · **Next:** [[05 - The Transformer Block]]

---

## In plain English

One attention pass = one way to relate tokens. **Multi-head** runs $h$ attentions in parallel, then **concatenates** and projects — so the model can attend to syntax, coreference, position, etc. in parallel.

---

## Inputs and outputs

| | Shape (batch) | Description |
|---|---------------|-------------|
| **Input** $X$ | $B \times S \times D$ | Same as single-head input |
| **Per head** output | $B \times S \times d_k$ | $d_k = D / h$ typically |
| **Concat** | $B \times S \times (h \cdot d_k) = B \times S \times D$ | All heads side by side |
| **After $W_O$** | $B \times S \times D$ | **Module output** |

**In = Out shape** ($B \times S \times D$) — ready for residual connection.

---

## Data flow (per head $i$)

| Step | Input | Output |
|------|-------|--------|
| $Q^{(i)} = X W_Q^{(i)}$ | $B \times S \times D$ | $B \times S \times d_k$ |
| $K^{(i)} = X W_K^{(i)}$ | $B \times S \times D$ | $B \times S \times d_k$ |
| $V^{(i)} = X W_V^{(i)}$ | $B \times S \times D$ | $B \times S \times d_v$ |
| $\text{head}_i = \text{Attn}(Q^{(i)},K^{(i)},V^{(i)})$ | three tensors | $B \times S \times d_v$ |
| $\text{Concat}(\text{head}_1..\text{head}_h)$ | $h$ tensors | $B \times S \times D$ |
| $W_O$ | concat | $B \times S \times D$ |

$$\text{MultiHead}(X) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h) \, W_O$$

---

## Paper Figure 2 (multi-head side)

![Multi-head attention (Vaswani et al. 2017)](assets/transformer-paper-figure2-multihead.png)

| Block | Input | Output |
|-------|-------|--------|
| $h$ parallel Attentions | $X$ (via different $W$) | $h$ × $(S \times d_v)$ |
| Concat | $h$ heads | $S \times (h \cdot d_v)$ |
| Linear $W^O$ | concat | $S \times D$ |

---

## Shape check (interview)

| Setting | Value |
|---------|-------|
| $d_{model}$ $D$ | 768 |
| $h$ | 12 |
| $d_k$ per head | $768 / 12 = 64$ |

Each head builds a **$S \times S$** attention map (still $O(S^2)$ per head, but smaller $d_k$ in dot product).

---

## In the transformer block

```
Input X  (B × S × D)
    ↓
MultiHeadAttn(X)  →  (B × S × D)
    ↓
Dropout
    ↓
X + residual  →  (B × S × D)   ← still same shape
```

→ FFN next: [[05 - The Transformer Block]]

---

## Interview one-liner

> "Split $D$ into $h$ subspaces; run attention in each; concat back to $D$; multiply by $W_O$ — input and output shapes stay $B \times S \times D$."

---

## Common traps

| Trap | Correct |
|------|---------|
| Heads share $W_Q$ | **Separate** weights per head |
| Output dim $h \cdot d_k$ without $W_O$ | $W_O$ maps concat → $D$ |

---

**Next:** [[05 - The Transformer Block]]
