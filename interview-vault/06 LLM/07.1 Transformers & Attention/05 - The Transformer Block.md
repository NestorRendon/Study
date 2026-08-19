# The Transformer Block

**Prev:** [[04 - Multi-Head Attention]] · **Next:** [[06 - Encoder Decoder and Masks]]

---

## In plain English

One **block** = mix tokens (attention) + process each token (FFN) + **residuals** + **LayerNorm**. Stack $N$ blocks. **Shape is preserved** end-to-end: $B \times S \times D$ in and out of each block.

---

## One encoder block — I/O summary

| Stage | Input shape | Output shape |
|-------|-------------|--------------|
| Block input $X$ | $B \times S \times D$ | — |
| After masked/bidir self-attn + residual + LN | $B \times S \times D$ | $B \times S \times D$ |
| After FFN + residual + LN | $B \times S \times D$ | $B \times S \times D$ |
| **Block output** | — | $B \times S \times D$ → next layer |

---

## Sub-layer 1 — Multi-head self-attention (detailed I/O)

| Step | Input | Output |
|------|-------|--------|
| $X$ (incoming) | $B \times S \times D$ | — |
| LayerNorm($X$) | $B \times S \times D$ | $B \times S \times D$ |
| MultiHeadAttn | $B \times S \times D$ | $B \times S \times D$ |
| Dropout | $B \times S \times D$ | $B \times S \times D$ |
| Add residual $X + \ldots$ | $B \times S \times D$ | $B \times S \times D$ |

$$\mathbf{y} = X + \text{Dropout}(\text{MultiHead}(\text{LayerNorm}(X)))$$

---

## Sub-layer 2 — Feed-forward network (detailed I/O)

Per token (same weights for every position):

| Step | Input | Output |
|------|-------|--------|
| LayerNorm($\mathbf{y}$) | $B \times S \times D$ | $B \times S \times D$ |
| $W_1$ linear | $B \times S \times D$ | $B \times S \times d_{ff}$ |
| GELU/ReLU | $B \times S \times d_{ff}$ | $B \times S \times d_{ff}$ |
| $W_2$ linear | $B \times S \times d_{ff}$ | $B \times S \times D$ |
| Dropout + residual | $B \times S \times D$ | $B \times S \times D$ |

$$\text{FFN}(\mathbf{x}) = W_2 \cdot \text{GELU}(W_1 \mathbf{x} + b_1) + b_2$$

| Typical | Value |
|---------|-------|
| $d_{ff}$ | $4 \times D$ |

**Role:** attention **mixes** tokens; FFN **transforms** each position's vector.

![Feed-forward](assets/AA4D6DF3-5615-4525-9E36-0A032655C61C.png)

---

## Stack $N$ layers

| | Layer 1 | Layer 2 | … | Layer $N$ |
|---|---------|---------|---|-----------|
| Input | $X^{(0)}$ embed+PE | $X^{(1)}$ | | $X^{(N-1)}$ |
| Output | $X^{(1)}$ | $X^{(2)}$ | | $X^{(N)}$ → encoder memory |

Each layer: **same shape** $B \times S \times D$, richer semantics.

---

## Block diagram

```
Input X  (B × S × D)
        │
        ▼
┌───────────────────────────────────────┐
│  LN → Multi-Head Self-Attention       │  in: B×S×D  out: B×S×D
│  + Residual                           │
└───────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────┐
│  LN → FFN (D → d_ff → D)              │  in: B×S×D  out: B×S×D
│  + Residual                           │
└───────────────────────────────────────┘
        │
        ▼
   To layer ℓ+1  (still B × S × D)
```

![Encoder layer stack (illustrated)](assets/FF89DF47-EEB4-453D-A985-F3DADC02216F.png)

Full paper diagram with encoder + decoder: [[08 - End-to-End Inputs and Outputs]]

---

## Complexity (per block)

| Sub-layer | Time | See |
|-----------|------|-----|
| Attention | $O(S^2 \cdot D)$ | [[09 - Complexity Big O]] |
| FFN | $O(S \cdot D \cdot d_{ff})$ | [[09 - Complexity Big O]] |

---

## Interview one-liner

> "Each block outputs the same tensor shape it receives: attention mixes across $S$, FFN refines each of the $S$ vectors, residuals and LayerNorm keep training stable."

---

**Next:** [[06 - Encoder Decoder and Masks]]
