# Embedding Model Choice

**Prev:** [[02 - Chunking Strategy]] · **Next:** [[04 - Indexing and Vector Stores]]

---

## In plain English

Each chunk becomes a **vector** (list of numbers). Similar **meaning** → vectors close together. The **embedding model** you pick defines that geometry — and you must use the **same model** for indexing and querying.

**Step 2** after chunking.

---

## How embeddings work (minimal math)

$$\text{similarity}(\mathbf{q}, \mathbf{d}) = \frac{\mathbf{q} \cdot \mathbf{d}}{\|\mathbf{q}\| \|\mathbf{d}\|}$$

→ Full treatment: [[03 Mathematics/02 - Similarity Correlation and Convolution]]

| Symbol | Meaning |
|--------|---------|
| $\mathbf{q}$ | Query vector |
| $\mathbf{d}$ | Chunk vector |

---

## Choosing a model (pragmatic)

| Criterion | Question to ask |
|-----------|-----------------|
| **Language** | Multilingual? Domain jargon? |
| **Dimension** | 384 vs 1536 — affects storage & speed |
| **Latency** | API vs local (sentence-transformers) |
| **Cost** | Per 1M tokens for re-indexing |
| **Same model always** | Index + query must match |

**Common choices:** OpenAI `text-embedding-3-*`, Cohere embed, `bge-large`, voyage-ai.

---

## Lexical vs dense (when embeddings are not enough alone)

| Need | Add |
|------|-----|
| SKUs, legal cites, exact codes | **BM25 / hybrid** → [[05 - Retrieval Quality]] |
| Paraphrased questions | Dense embeddings |

---

## Re-index rule

If you **change** the embedding model → **re-embed all chunks** and rebuild the index. Old vectors are incompatible.

---

## Common traps

| Trap | Correct |
|------|---------|
| Different models for index vs query | **Same** model both sides |
| Embed dirty chunks | Clean text in [[02 - Chunking Strategy]] first |

---

**Next:** [[04 - Indexing and Vector Stores]]
