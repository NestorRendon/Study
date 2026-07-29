# RAG Evaluation

**Prev:** [[09 - GraphRAG]] · **Next:** [[09 Knowledge Graphs/00 - Chapter Overview|Knowledge Graphs (Ch 9)]]

---

## In plain English

**Step 9** — close the loop: measure if the system works. Evaluate **retrieval** and **generation** separately. A fluent wrong answer is often a **retrieval bug**, not an LLM bug.

---

## Two-stage checklist

### Stage 1 — Retrieval

| Metric | Question |
|--------|----------|
| Context precision | Any irrelevant chunks in top-k? |
| Context recall | Is the gold passage in top-k? |
| MRR / nDCG | Ranking quality |

### Stage 2 — Generation

| Metric | Question |
|--------|----------|
| Faithfulness | Every claim supported by context? |
| Answer relevance | Does it address the question? |
| Hallucination rate | Claims not in context? |

---

## Agent-specific (your experience)

| Metric | Measures |
|--------|----------|
| Trajectory success | Efficient tool path? |
| Outcome | Business task completed? |
| Token waste | Loops / redundant retrieval? |

→ [[07 LLM & Generative AI/08 - LLM Evaluation Metrics]]

---

## Minimal eval set (pragmatic)

1. 50–100 real user questions
2. Human labels: which doc has answer
3. Track recall@k before touching prompts
4. Add LLM-judge only after retrieval is solid

---

## Common traps

| Trap | Correct |
|------|---------|
| Only BLEU/ROUGE on final answer | Measure **retrieval** first |
| One metric | Precision/recall/faithfulness trade off |

---

**Next chapter:** [[09 Knowledge Graphs/00 - Chapter Overview]]
