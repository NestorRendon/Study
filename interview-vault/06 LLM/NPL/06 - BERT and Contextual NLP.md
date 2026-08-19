# BERT & Contextual NLP (Bridge to LLMs)

**Prev:** [[05 - Topic Modeling and LDA]] · **Next:** [[06 LLM/07 LLM & Generative AI/00 - Chapter Overview|Chapter 7 — LLMs]]

---

## In plain English

**BERT** reads the **full sentence** and builds a representation where each word depends on **context**. That replaced static Word2Vec for most understanding tasks — and led to **GPT** for generation.

---

## Encoder-only (BERT family)

| Property | Detail |
|----------|--------|
| Attention | **Bidirectional** — sees left and right |
| Pretraining | Masked language modeling (fill blanks) |
| Use cases | Classification, NER, embeddings for search |

**Examples:** BERT, RoBERTa, DeBERTa.

---

## Decoder-only (GPT family) — preview Ch 7

| Property | Detail |
|----------|--------|
| Attention | **Causal** — only past tokens |
| Pretraining | Predict next token |
| Use cases | Chat, code, generation |

---

## Why transformers replaced RNNs

| RNN/LSTM | Transformer |
|----------|-------------|
| Sequential (slow) | Parallel training |
| Hard long memory | Attention over all positions |

→ Math: [[03 - Self-Attention Step by Step]] · Architecture: [[06 - Encoder Decoder and Masks]]

---

## 30-second interview answer

> "Classical NLP used TF-IDF and static embeddings. BERT added contextual encoders for understanding tasks; GPT-style decoders scaled to generative LLMs. For interviews I position NLP as a pipeline ending at transformers, then RAG and agents in later chapters."

---

**Next chapter:** [[06 LLM/07 LLM & Generative AI/00 - Chapter Overview]]
