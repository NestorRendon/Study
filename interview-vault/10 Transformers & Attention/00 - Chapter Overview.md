# Chapter 10 — Transformers & Attention

**What this chapter is:** how transformers work from **motivation → math → full architecture → I/O shapes → Big O**. Read in order — each note is one step in the stack.

**Overview = story only.** Detail notes have **input/output tables** at every step, original paper figures, and complexity.

**Prerequisite:** [[05 Deep Learning/11 - RNN LSTM and GRU]] · [[06 NLP & Text Mining/06 - BERT and Contextual NLP]]

---
https://medium.com/@RobuRishabh/how-transformers-work-b08627a300cb
## The story (study path)

1. **Why transformers** — RNN limits, parallel attention ([[01 - Why Transformers]])
2. **Embeddings + position** — IDs → $B \times S \times D$, inject order ([[02 - Embeddings and Positional Encoding]])
3. **Self-attention** — Q/K/V, six steps with I/O per step ([[03 - Self-Attention Step by Step]])
4. **Multi-head** — $h$ heads, concat, $W_O$, same in/out shape ([[04 - Multi-Head Attention]])
5. **Transformer block** — attn + FFN + residual, stack $N$ layers ([[05 - The Transformer Block]])
6. **Encoder / decoder / masks** — BERT vs GPT vs seq2seq ([[06 - Encoder Decoder and Masks]])
7. **Shapes reference** — hyperparameters cheat sheet ([[07 - Shapes and Variable Reference]])
8. **End-to-end I/O** — **Figure 1 & 2 from the paper**, full pipeline ([[08 - End-to-End Inputs and Outputs]])
9. **Big O complexity** — $O(n^2 d)$, FFN, inference, memory ([[09 - Complexity Big O]])

---

## Original architecture (Figure 1)

![Transformer — Figure 1 (Vaswani et al. 2017)](assets/transformer-paper-figure1-architecture.png)

*Full step-by-step I/O for every box:* [[08 - End-to-End Inputs and Outputs]]

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | Why transformers | [[01 - Why Transformers]] |
| 2 | Embeddings & positional encoding | [[02 - Embeddings and Positional Encoding]] |
| 3 | Self-attention (I/O per step) | [[03 - Self-Attention Step by Step]] |
| 4 | Multi-head attention | [[04 - Multi-Head Attention]] |
| 5 | Transformer block | [[05 - The Transformer Block]] |
| 6 | Encoder, decoder & masks | [[06 - Encoder Decoder and Masks]] |
| 7 | Shapes & variables | [[07 - Shapes and Variable Reference]] |
| 8 | End-to-end I/O + paper figures | [[08 - End-to-End Inputs and Outputs]] |
| 9 | Complexity & Big O | [[09 - Complexity Big O]] |

---

## After this chapter

| Go to | For |
|-------|-----|
| [[07 LLM & Generative AI/00 - Chapter Overview]] | LoRA, agents, RAG |
| [[11 Computer Vision/00 - Chapter Overview]] | ViT |

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Decoder-only dominance** | GPT, Llama |
| **RoPE + long context** | 128k+ tokens |
| **Flash Attention** | Same $O(n^2)$ FLOPs, less memory |
| **MoE FFN** | [[07 LLM & Generative AI/04 - Mixture of Experts MoE]] |

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| "Attention = memory bank" | Mix of **current sequence** only |
| "Q, K, V = embedding" | **Projections** of embedding |
| "Softmax over time" | Softmax over **keys** (per query row) |
| "Block changes shape" | $B \times S \times D$ **in = out** per block |
| "Position optional" | Order lost without PE |

---

**Prev:** [[09 Knowledge Graphs/00 - Chapter Overview]] · **Next:** [[11 Computer Vision/00 - Chapter Overview]]

[[Home|← Home]]
