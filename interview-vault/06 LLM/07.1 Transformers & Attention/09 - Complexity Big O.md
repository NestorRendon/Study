# Complexity & Big O

**Prev:** [[08 - End-to-End Inputs and Outputs]] · **Next:** [[Metrics and Evaluation/00 - Chapter Overview|Metrics & Evaluation]]

---

## In plain English

Transformers are fast to **parallelize** but expensive in **sequence length** because attention compares every token to every token. Interviews ask: *"What scales quadratically?"* and *"When does FFN dominate?"*

Use $n$ or $S$ = sequence length, $d$ = $d_{model}$, $d_{ff}$ = FFN hidden, $h$ = heads, $N$ = layers, $B$ = batch.

---

## Paper Table 1 (per layer, one sequence)

From *Attention Is All You Need* — compare layer types:

| Layer type | Complexity per layer | Sequential ops | Max path length |
|------------|---------------------|----------------|-----------------|
| **Self-attention** | $O(n^2 \cdot d)$ | $O(1)$ | $O(1)$ |
| **Recurrent** | $O(n \cdot d^2)$ | $O(n)$ | $O(n)$ |
| **Convolutional** | $O(k \cdot n \cdot d^2)$ | $O(1)$ | $O(\log_k n)$ |

**Interview takeaway:** attention has **short paths** between any two positions (good for learning) but **$n^2$** cost (bad for very long $n$).

---

## Self-attention — operation by operation

| Operation | Time (FLOPs, order) | Memory (typical) |
|-----------|---------------------|------------------|
| $Q = XW_Q$ | $O(n \cdot d \cdot d_k)$ | $O(n \cdot d_k)$ |
| $K = XW_K$ | $O(n \cdot d \cdot d_k)$ | $O(n \cdot d_k)$ |
| $V = XW_V$ | $O(n \cdot d \cdot d_v)$ | $O(n \cdot d_v)$ |
| $QK^\top$ | $O(n^2 \cdot d_k)$ | $O(n^2)$ attention scores |
| Softmax | $O(n^2)$ | $O(n^2)$ |
| $\text{Attn} \cdot V$ | $O(n^2 \cdot d_v)$ | $O(n \cdot d_v)$ |
| Multi-head ($h$ heads) | $\approx h \times$ per-head* | $h$ heads or fused |
| $W_O$ projection | $O(n \cdot d^2)$ | $O(n \cdot d)$ |

\* Heads share the same $n$; total often written $O(n^2 \cdot d)$ with $d_k = d/h$.

**Dominant term for long sequences:** $O(n^2 \cdot d)$ from the $n \times n$ attention matrix.

---

## FFN — per layer

Applied to each of $n$ positions independently:

| Operation | Time |
|-----------|------|
| $W_1$: $d \to d_{ff}$ | $O(n \cdot d \cdot d_{ff})$ |
| $W_2$: $d_{ff} \to d$ | $O(n \cdot d \cdot d_{ff})$ |
| **Total FFN** | $O(n \cdot d \cdot d_{ff})$ |

With $d_{ff} = 4d$ → $O(n \cdot d^2)$.

---

## When does attention vs FFN dominate?

| Condition | Bottleneck |
|-----------|------------|
| $n$ large (long context) | **Attention** ($n^2$) |
| $d_{ff} \gg d$ and moderate $n$ | **FFN** |
| Rule of thumb | Compare $n^2 d$ vs $n d \cdot d_{ff}$ → $n$ vs $d_{ff}$ |

Example: $n=8192$, $d=4096$, $d_{ff}=16384$ → attention $\propto n^2 d$ wins.

Example: $n=512$, $d=768$, $d_{ff}=3072$ → both matter; attention still $n^2$.

---

## Full encoder stack

| Component | Time | Parameters |
|-----------|------|------------|
| Embedding | $O(n \cdot d)$ lookup | $O(V \cdot d)$ |
| One encoder layer | $O(n^2 d + n d \cdot d_{ff})$ | $O(d^2 + d \cdot d_{ff})$ |
| $N$ layers | $N \times$ per layer | $N \times$ per layer |
| **Total forward (enc.)** | $O(N \cdot (n^2 d + n d \cdot d_{ff}))$ | $O(N d^2)$ dominant |

With batch $B$: multiply compute by $B$ (roughly).

---

## Encoder–decoder (translation)

| Piece | Extra cost vs encoder-only |
|-------|----------------------------|
| Decoder masked self-attn | $O(n_{tgt}^2 \cdot d)$ per layer |
| Cross-attention | $O(n_{tgt} \cdot n_{src} \cdot d)$ per layer |
| Two stacks of $N$ layers | $\approx 2N$ layer cost + cross terms |

**Cross-attention** is $O(S \cdot T \cdot d)$ — linear in both lengths, not $S^2$ if only decoder queries encoder once per position.

---

## Inference (GPT) — per new token

Without KV cache: recompute full $n \times n$ attention each step → $O(N \cdot n^2 \cdot d)$ per token → **$O(N \cdot n^3 \cdot d)$** for length-$n$ generation.

**With KV cache:** store past $K,V$ → each step only computes new query against all keys → $O(N \cdot n \cdot d)$ per token → **$O(N \cdot n^2 \cdot d)$** total for $n$ tokens (linear in $n$ per step, $n$ steps).

→ [[06 - KV Caching]]

---

## Memory summary

| Object | Size (order) |
|--------|----------------|
| Activations $X$ | $B \cdot n \cdot d$ |
| Attention weights | $B \cdot h \cdot n^2$ |
| FFN activations | $B \cdot n \cdot d_{ff}$ |
| Model weights | $O(N d^2 + V d)$ |

**Flash Attention:** same Big O FLOPs, **lower memory** by not materializing full $n \times n$ on GPU HBM.

---

## Practical levers (interview)

| Goal | Technique |
|------|-----------|
| Longer context | Sparse attention, ring attention, sliding window |
| Cheaper inference | KV cache, quantization, smaller $d$ |
| Cheaper training | Gradient checkpointing, mixed precision |
| Less $n^2$ pain | Flash Attention, fused kernels |

---

## Quick quiz (answers in headings above)

1. Why is Transformer parallelizable across sequence positions during training?  
2. What is $O(n^2)$ in memory?  
3. Why does GPT slow down as context grows even with KV cache?  
4. When is RNN $O(n \cdot d^2)$ cheaper than attention?

**Answers:** (1) Attention layers need $O(1)$ sequential steps per layer vs RNN's $O(n)$. (2) Attention score matrix. (3) Each new token still attends over longer $n$. (4) When $n \gg d$ (very long seq vs moderate dim) — rare in modern LLM regimes.

---

**Next chapter:** [[11 Computer Vision/00 - Chapter Overview]]
