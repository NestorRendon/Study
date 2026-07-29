# Embeddings & Positional Encoding

**Prev:** [[01 - Why Transformers]] · **Next:** [[03 - Self-Attention Step by Step]]

---

## In plain English

The model does not see words — it sees **vectors**. First turn tokens into embeddings, then **add position** so order matters. Only after that does attention run.

---

## Step 1 — Token → embedding

| Stage | Input | Output | Shape |
|-------|-------|--------|-------|
| Tokenize | raw text | token strings | length $S$ |
| IDs | strings | integers | $S$ (or $B \times S$) |
| Embedding lookup | IDs | vectors | $B \times S \times D$ |

$$X \in \mathbb{R}^{S \times D} \quad \text{(or } B \times S \times D \text{ with batch)}$$

Each row is one token's meaning **before** context (static table + learned).  
Paper scales embeddings by $\sqrt{D}$ before adding PE.

---

## Step 2 — Why position is required

Self-attention treats input as a **set** of vectors unless you tell it order:

- `"dog bites man"` and `"man bites dog"` would look the same
- Attention is **permutation-invariant** on $X$ alone

**Fix:** add positional information to each row before layer 1.

---

## Step 3 — Add positional encoding

$$\mathbf{x}'_i = \mathbf{x}_i + PE(i)$$

### Sinusoidal (original paper)

$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/D}}\right), \quad
PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/D}}\right)$$

Different dimensions oscillate at different frequencies → model can learn relative distances.

### Modern alternatives

| Method | Used in | Idea |
|--------|---------|------|
| **Learned absolute** | BERT | Train one vector per position index |
| **RoPE** | Llama, many LLMs | Rotate Q/K by position (relative) |
| **ALiBi** | Some long-context models | Bias attention scores by distance |

You do not need to derive RoPE for most interviews — know **"position is injected before attention"** and RoPE is the common LLM choice.

---

## Step 3 — Combined input/output before layer 1

| Step | Input | Output |
|------|-------|--------|
| Embed | token IDs $B \times S$ | $B \times S \times D$ |
| + PE | embed, position table | $B \times S \times D$ |
| **$X^{(0)}$ (block 0 input)** | — | $B \times S \times D$ |

```
Token IDs  →  Embedding lookup  →  + Positional encoding  →  X⁽⁰⁾  (B × S × D)
                                                              ↓
                                                    Multi-head self-attention
                                                              ↓
                                                    still B × S × D  (then residual, FFN…)
```

---

## Common traps

| Trap | Correct |
|------|---------|
| "Position is optional" | Without it, word order is lost |
| "Embedding = final representation" | Early layer; context added by attention |
| "PE replaces embedding" | **Add** to embedding, don't replace |

---

**Next:** [[03 - Self-Attention Step by Step]]
