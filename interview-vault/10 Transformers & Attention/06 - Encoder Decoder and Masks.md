# Encoder, Decoder & Masks

**Prev:** [[05 - The Transformer Block]] · **Next:** [[07 - Shapes and Variable Reference]]

---

## In plain English

The **same building block** appears in three setups. Interviews want you to name **which mask** is used and **what each stack reads/writes**.

---

## Three architectures

| Model | Stacks | Attention pattern | Example |
|-------|--------|-------------------|---------|
| **Encoder-only** | Encoder | Bidirectional (all tokens see all) | BERT |
| **Decoder-only** | Decoder | Causal (token sees past only) | GPT, Llama |
| **Encoder–decoder** | Both | Enc: bidirectional; Dec: causal + cross | Original translation Transformer, T5 |

→ Product view: [[07 LLM & Generative AI/01 - LLM Foundations Encoder and Decoder]]

---

## Encoder (BERT-style)

- **Self-attention:** full $S \times S$ matrix — every token sees every token
- **Use:** classification, embeddings, NER (fine-tune head on top)
- **Training:** often masked language modeling (predict hidden tokens)

---

## Decoder (GPT-style)

### Causal (autoregressive) mask

Token at position $i$ may **only attend to positions $\leq i$**.

```
      The  cat  sat
The    ✓   ✗   ✗
cat    ✓   ✓   ✗
sat    ✓   ✓   ✓
```

Scores for future positions → $-\infty$ before softmax → weight 0.

**Why:** at generation time you do not know future tokens; training must match inference.

### Training objective

Predict **next token**: cross-entropy on $P(x_{t+1} \mid x_1, \ldots, x_t)$.

### Inference

Generate one token at a time; append to sequence; repeat (KV cache speeds this up).

---

## Encoder–decoder (seq2seq)

| Sub-layer | Q from | K, V from | Mask | Attention map |
|-----------|--------|-----------|------|----------------|
| Encoder self-attn | encoder $S$ | encoder $S$ | none | $S \times S$ |
| Decoder self-attn | decoder $T$ | decoder $T$ | causal | $T \times T$ |
| **Cross-attention** | decoder $T$ | encoder $S$ | — | $T \times S$ |

| Stack I/O | Shape |
|-----------|-------|
| Encoder in/out | $B \times S \times D$ |
| Decoder in/out | $B \times T \times D$ |
| Final logits | $B \times T \times V$ |

**Use:** translation, summarization (T5 frames everything as text-to-text).

→ Paper Figure 1 walkthrough: [[08 - End-to-End Inputs and Outputs]]

---

## Mask summary table

| Mask type | Effect | Model |
|-----------|--------|-------|
| **None** (bidirectional) | Full context | BERT encoder |
| **Causal** | Upper triangle blocked | GPT |
| **Padding** | Ignore pad tokens | Batched training |
| **Cross** | Decoder queries encoder | Translation |

---

## Interview one-liner

> "GPT is a stack of causal masked decoder blocks; BERT is bidirectional encoder blocks; seq2seq adds cross-attention so the decoder can read the encoder's output."

---

**Next:** [[07 - Shapes and Variable Reference]]
