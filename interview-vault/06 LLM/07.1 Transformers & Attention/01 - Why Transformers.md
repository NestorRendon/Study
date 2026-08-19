# Why Transformers?

**Prev:** [[06 LLM/07.1 Transformers & Attention/00 - Chapter Overview]] · **Next:** [[02 - Embeddings and Positional Encoding]]

---

## In plain English

Before transformers, most NLP used **RNNs/LSTMs**: read tokens **one by one**, pass a hidden state forward. That worked but had three big problems transformers fix.

---

## What was wrong with RNNs?

| Problem | Why it hurts |
|---------|----------------|
| **Sequential** | Step $t$ waits for $t-1$ — hard to parallelize on GPUs |
| **Long-range memory** | Gradients fade → early words forgotten |
| **Bottleneck** | All context squeezed through one hidden vector |

→ RNN recap: [[05 Deep Learning/11 - RNN LSTM and GRU]]

---

## The transformer idea (2017, *Attention Is All You Need*)

> **Stop recurrence. Let every token look at every other token in one parallel step.**

| Old (RNN) | New (Transformer) |
|-----------|-------------------|
| Hidden state carries history | **Attention** mixes all positions each layer |
| $O(\text{length})$ sequential steps | $O(1)$ depth per layer, but $O(n^2)$ attention over length |
| Hard to scale context | Stack many attention layers → rich representations |

**Trade-off:** attention cost grows as **sequence length squared** — why long-context models need Flash Attention, sparse attention, etc.

---

## What you will build in this chapter

```
Tokens → embeddings + position
       → self-attention (who talks to whom)
       → multi-head (many relationship types)
       → FFN + residuals (per-token processing)
       → repeat N layers
       → logits → next token (GPT) or pooled output (BERT)
```

Read in order: each note adds one layer of the stack.

---

## Interview one-liner

> "Transformers replaced RNNs because self-attention gives direct paths between any two tokens, trains in parallel, and scales with depth — at the cost of quadratic memory in sequence length."

---

**Next:** [[02 - Embeddings and Positional Encoding]]
