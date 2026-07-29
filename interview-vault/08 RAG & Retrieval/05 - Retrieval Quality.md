# Retrieval Quality

**Prev:** [[04 - Indexing and Vector Stores]] · **Next:** [[06 - Basic RAG Pipeline]]

---

## In plain English

**Step 4** — at query time, did we fetch the **right chunks**? Bad retrieval → the LLM will hallucinate no matter how good the model is.

---

## Two families (recap)

| Type | Like | Best for |
|------|------|----------|
| **Lexical (BM25)** | Ctrl+F | SKUs, names, legal terms |
| **Dense (vectors)** | Meaning match | Paraphrases |
| **Hybrid** | Both scores fused | **Production default** |

---

## Metrics (measure before tuning the LLM)

| Metric | Question |
|--------|----------|
| **Context precision** | Are top-k chunks relevant? |
| **Context recall** | Is the gold passage in top-k? |
| **MRR / nDCG** | Is the best chunk ranked high? |

> **Interview line:** "I tune recall@k first — if the answer chunk isn't retrieved, generation cannot succeed."

---

## Improving quality (levers)

| Lever | Action |
|-------|--------|
| **k** | Increase top-k (e.g. 3 → 10) |
| **Hybrid** | BM25 + dense weighted sum |
| **Reranker** | Cross-encoder rescores top-20 → keep top-5 |
| **Query rewrite** | LLM reformulates vague question |
| **Metadata filter** | Narrow to right doc subset |

---

## Reranking (high impact)

```
ANN returns 20 candidates  →  cross-encoder scores (query, chunk)  →  top 5 to LLM
```

Models: `bge-reranker`, Cohere rerank API.

---

## When to use what

| Data | Start |
|------|-------|
| Exact tokens matter | BM25 or hybrid |
| Natural language only | Dense + rerank |
| Tables + prose | Structured filters + RAG on text |

---

## Common traps

| Trap | Correct |
|------|---------|
| k=1 always | Often need k=5–10 + rerank |
| High similarity score = correct answer | Read chunks — verify manually on eval set |
| Skip eval on retrieval | **Split** retrieval vs generation metrics |

---

**Next:** [[06 - Basic RAG Pipeline]]
