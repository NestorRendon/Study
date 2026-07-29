# Shapes & Variable Reference

**Prev:** [[06 - Encoder Decoder and Masks]] · **Next:** [[08 - End-to-End Inputs and Outputs]]

---

## In plain English

Use this note as a **cheat sheet** while studying or whiteboarding. Trace one batch through with concrete shapes.

---

## Hyperparameters

| Symbol | Name | Typical | If you increase… |
|--------|------|---------|------------------|
| $V$ | Vocab size | 32k–128k | Bigger embedding table |
| $S$ | Sequence length | 2k–128k+ | Attention cost $\sim S^2$ |
| $D$ | $d_{model}$ | 768, 4096 | Richer vectors, more memory |
| $H$ | Num heads | 8–32 | More relation types; $d_k = D/H$ |
| $d_k$ | Key/query dim per head | $D/H$ | Usually fixed by $D$ and $H$ |
| $d_{ff}$ | FFN hidden | $4D$ | Heavier MLP |
| $N$ | Num layers | 12–80+ | Deeper abstractions |
| $B$ | Batch size | varies | Throughput vs memory |

---

## One forward pass (decoder-only, shapes)

Batch size $B$, sequence $S$, model dim $D$.

| Tensor | Shape | Notes |
|--------|-------|-------|
| Input IDs | $B \times S$ | integers |
| Embeddings $X$ | $B \times S \times D$ | + PE |
| $Q, K, V$ (per head) | $B \times S \times d_k$ | $h$ heads, concat → $D$ |
| Attention scores | $B \times H \times S \times S$ | causal mask applied |
| Attention out | $B \times S \times D$ | after $W_O$ |
| FFN inner | $B \times S \times d_{ff}$ | then back to $D$ |
| Logits | $B \times S \times V$ | per-token vocab scores |

---

## Learned weight matrices (conceptual)

| Matrix | Maps | Role |
|--------|------|------|
| $W_Q^{(i)}, W_K^{(i)}, W_V^{(i)}$ | $D \to d_k$ | Head $i$ projections |
| $W_O$ | $D \to D$ | Merge heads |
| $W_1, W_2$ | FFN | $D \to d_{ff} \to D$ |
| $W_{\text{out}}$ | $D \to V$ | Language model head |

---

## Complexity

→ Full Big O breakdown: [[09 - Complexity Big O]] (paper Table 1, attention vs FFN, inference)

---

## Training symbols

| Symbol | Role |
|--------|------|
| $\mathcal{L}$ | Cross-entropy on next token (shifted labels) |
| $\eta$ | Learning rate (warmup + decay common) |
| Dropout | On attention weights and FFN |

---

## Study checklist

- [ ] Explain why position is added **before** layer 1
- [ ] Draw $QK^\top$ and softmax direction
- [ ] State causal vs bidirectional mask
- [ ] Give shapes: $X$, scores, output
- [ ] Encoder-only vs decoder-only vs both

---

## Common traps

| Trap | Correct |
|------|---------|
| $S \times S$ matrix in encoder **and** decoder | Decoder uses **causal** mask |
| $d_k = D$ always | Usually $d_k = D / H$ per head |
| Logits shape $B \times V$ only | Often $B \times S \times V$ for each position |

---

**Next:** [[08 - End-to-End Inputs and Outputs]]
