# End-to-End Inputs & Outputs

**Prev:** [[07 - Shapes and Variable Reference]] · **Next:** [[09 - Complexity Big O]]

---

## In plain English

Every interview whiteboard question boils down to: **what tensor goes in, what tensor comes out?** This note traces **one training step** on the original encoder–decoder Transformer (translation), then summarizes **GPT (decoder-only)**.

Notation: batch $B$, source length $S$, target length $T$, model dim $D$, vocab $V$, FFN dim $d_{ff}$, heads $H$, layers $N$.

---

## Original paper — Figure 1 (full architecture)

From Vaswani et al., *Attention Is All You Need* (2017), **Figure 1: The Transformer — model architecture.**

![Figure 1 — Transformer architecture (Vaswani et al. 2017)](assets/transformer-paper-figure1-architecture.png)

**How to read the diagram (left = encoder, right = decoder):**

| Region | Input | Output |
|--------|-------|--------|
| Bottom left | Source token IDs | — |
| Input embedding + PE | IDs | $S \times D$ encoder input |
| Encoder stack ($N$×) | $S \times D$ | $S \times D$ memory |
| Bottom right | Target token IDs (shifted) | — |
| Output embedding + PE | IDs | $T \times D$ decoder input |
| Decoder stack ($N$×) | $T \times D$ + encoder memory | $T \times D$ |
| Linear + softmax | $T \times D$ | $T \times V$ logits → probabilities |

Cross-attention in the decoder (middle sub-layer) uses **queries from decoder**, **keys/values from encoder output**.

Paper: [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)

---

## Figure 2 — Attention modules (paper)

**Left:** Scaled dot-product attention. **Right:** Multi-head attention (parallel heads + output projection).

![Figure 2a — Scaled dot-product attention](assets/transformer-paper-figure2-attention.png)

![Figure 2b — Multi-head attention](assets/transformer-paper-figure2-multihead.png)

| Submodule | Input | Output |
|-----------|-------|--------|
| MatMul $QK^\top$ | $Q$, $K$ | $S \times S$ scores |
| Scale / Mask / Softmax | scores | $S \times S$ weights |
| MatMul with $V$ | weights, $V$ | $S \times d_v$ |
| Multi-head concat + $W^O$ | $H$ heads | $S \times D$ |

---

## Global I/O — encoder–decoder (training)

### Inputs to the whole model

| Input | Shape | Meaning |
|-------|-------|---------|
| `src_ids` | $B \times S$ | Source sentence token IDs |
| `tgt_ids` | $B \times T$ | Target sentence (teacher forcing) |
| `tgt_labels` | $B \times T$ | Next-token targets (shifted by 1) |

### Outputs of the whole model

| Output | Shape | Meaning |
|--------|-------|---------|
| `logits` | $B \times T \times V$ | Unnormalized score per vocab token |
| `probs` | $B \times T \times V$ | `softmax(logits)` |
| `loss` | scalar | Cross-entropy(`logits`, `tgt_labels`) |

---

## Step-by-step — encoder only

| Step | Input shape | Output shape | What changed |
|------|-------------|--------------|--------------|
| 1. Source IDs | $B \times S$ | — | integers |
| 2. Embedding lookup | $B \times S$ | $B \times S \times D$ | ID → vector |
| 3. × $\sqrt{D}$ (paper) | $B \times S \times D$ | same | scale embeddings |
| 4. + positional encoding | $B \times S \times D$ | same | inject order → $X_{enc}^{(0)}$ |
| 5. Encoder layer $\ell=1..N$ | $B \times S \times D$ | $B \times S \times D$ | contextualize |
| 5a. Sub-layer: MHA (self) | $B \times S \times D$ | $B \times S \times D$ | tokens attend to tokens |
| 5b. Residual + LayerNorm | two $B \times S \times D$ | $B \times S \times D$ | $x + \text{sub}(x)$ |
| 5c. Sub-layer: FFN | $B \times S \times D$ | $B \times S \times D$ | per-token MLP |
| 5d. Residual + LayerNorm | two $B \times S \times D$ | $B \times S \times D$ | → next layer or final |
| **Encoder out (memory)** | — | $B \times S \times D$ | $Z$ for decoder cross-attn |

---

## Step-by-step — one encoder layer (detail)

| Sub-step | Input | Output |
|----------|-------|--------|
| LayerNorm | $X$ | $\hat{X}$ |
| $Q,K,V$ projections | $\hat{X}$ | each $B \times S \times d_k$ per head |
| Attention | $Q,K,V$ | $B \times S \times D$ (after concat + $W_O$) |
| Dropout | attn out | same |
| Residual | $X$, attn out | $X + \text{dropout}(\text{attn})$ |
| LayerNorm | residual | $\hat{X}_2$ |
| FFN $W_1$ | $\hat{X}_2$ | $B \times S \times d_{ff}$ |
| ReLU/GELU | $B \times S \times d_{ff}$ | same |
| FFN $W_2$ | hidden | $B \times S \times D$ |
| Residual + LN | | $B \times S \times D$ |

---

## Step-by-step — decoder (one layer)

| Sub-layer | Q from | K, V from | Mask | Output |
|-----------|--------|-----------|------|--------|
| **Masked self-attention** | decoder | decoder | causal | $B \times T \times D$ |
| Residual + LN | | | | $B \times T \times D$ |
| **Cross-attention** | decoder | **encoder memory** | none on enc | $B \times T \times D$ |
| Residual + LN | | | | $B \times T \times D$ |
| **FFN** | decoder | — | — | $B \times T \times D$ |
| Residual + LN | | | | $B \times T \times D$ |

**Cross-attention I/O (critical):**

| | Shape |
|---|-------|
| $Q$ | $B \times T \times d_k$ (from decoder state) |
| $K, V$ | $B \times S \times d_k$ (from encoder output) |
| Attention map | $B \times T \times S$ (each target position looks at source positions) |
| Output | $B \times T \times D$ |

---

## Decoder-only (GPT) — simplified stack

No encoder. One stream:

| Step | Input | Output |
|------|-------|--------|
| Token IDs | $B \times S$ | — |
| Embed + PE | $B \times S$ | $B \times S \times D$ |
| $N$ × decoder blocks (masked self-attn + FFN) | $B \times S \times D$ | $B \times S \times D$ |
| LM head $W_{out}$ | $B \times S \times D$ | $B \times S \times V$ logits |
| Softmax (inference) | logits | $B \times S \times V$ probs |

**Generation:** only last position logits used for next token; KV cache stores past $K,V$ → see [[06 - KV Caching]].

---

## Self-attention — I/O per micro-step

For one head, sequence length $S$ (single batch item):

| Step | Input | Output | Shape |
|------|-------|--------|-------|
| 1. Input $X$ | token representations | — | $S \times D$ |
| 2. $Q = XW_Q$ | $X$ | $Q$ | $S \times d_k$ |
| 3. $K = XW_K$ | $X$ | $K$ | $S \times d_k$ |
| 4. $V = XW_V$ | $X$ | $V$ | $S \times d_v$ |
| 5. Scores | $Q, K$ | $QK^\top / \sqrt{d_k}$ | $S \times S$ |
| 6. Mask (optional) | scores | masked scores | $S \times S$ |
| 7. Weights | scores | $\text{softmax}$ | $S \times S$ |
| 8. Context | weights, $V$ | $\text{weights} \cdot V$ | $S \times d_v$ |

**Row $i$ of output** = new representation for token $i$ = mixture of all $V$ rows weighted by how much token $i$ attends to each key.

→ Full walkthrough: [[03 - Self-Attention Step by Step]]

---

## What the model “predicts” (output head)

| Setting | Final layer input | Final output | Loss |
|---------|-------------------|--------------|------|
| Translation | $B \times T \times D$ | $B \times T \times V$ | CE on target tokens |
| BERT MLM | $B \times S \times D$ | $B \times S \times V$ | CE on masked positions only |
| GPT LM | $B \times S \times D$ | $B \times S \times V$ | CE on next token (shifted) |

---

## Study exercise

Pick $B=2$, $S=4$, $D=512$, $H=8$, $N=6$. For each box in **Figure 1**, write the tensor shape entering and leaving. Then explain cross-attention shapes where $S \neq T$.

---

**Next:** [[09 - Complexity Big O]]
