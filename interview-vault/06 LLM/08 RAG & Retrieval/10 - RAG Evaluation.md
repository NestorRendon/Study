# RAG Evaluation

**Prev:** [[09 - GraphRAG]] · **Next:** [[06 LLM/09 Knowledge Graphs/00 - Chapter Overview|Knowledge Graphs (Ch 9)]]

---

## In plain English

**Step 10** — close the loop: measure if the system works. Evaluate **retrieval** and **generation** separately. A fluent, confident wrong answer is almost always a **retrieval bug** (wrong chunk fetched), not an LLM bug.

> **Interview line:** "A fluent wrong answer usually means the retriever fetched the wrong chunk, not that the LLM reasoned badly — so I debug retrieval before touching the prompt."

---

## Two-stage checklist

### Stage 1 — Retrieval (RAGAS-style metrics)

| Metric | Question | How it's scored |
|--------|----------|------------------|
| **Context precision** | Any irrelevant chunks in top-k? | LLM judges each retrieved chunk: relevant to the question or not |
| **Context recall** | Is the gold passage in top-k? | Compare retrieved chunks against a labeled "correct passage" set |
| **MRR** | How high is the *first* relevant chunk ranked? | `1 / rank of first relevant result`, averaged over queries |
| **nDCG** | How good is the *whole ranking*, not just the first hit? | Rewards relevant chunks near the top, penalizes them buried low |

### Stage 2 — Generation

| Metric | Question | How it's scored |
|--------|----------|------------------|
| **Faithfulness** | Every claim supported by context? | Decompose the answer into claims → check each against retrieved context |
| **Answer relevance** | Does it address the question? | Generate a question from the answer, compare embedding similarity to the original question |
| **Hallucination rate** | Claims not in context? | `1 − faithfulness`, tracked over the eval set |

Context precision, context recall, faithfulness and answer relevance are the four core metrics in **RAGAS**, the most common open-source RAG eval library — name it if asked "how would you evaluate this."

---

## Worked example

```text
Question: "What's the max irrigation the system allows per day?"

Retrieved chunks (top-3):
  1. "Irrigation limits are set per crop type..."          ✓ relevant
  2. "Soil moisture sensors report every 15 min..."         ✗ irrelevant
  3. "Maximum daily irrigation is 40mm unless override..."  ✓ relevant (has the answer)

Generated answer: "The system allows up to 40mm of irrigation per day."
```

```text
Context precision  → 2/3 chunks relevant              = 0.67
Context recall      → gold passage (#3) was retrieved  = 1.0
Faithfulness        → the "40mm" claim IS in chunk #3  = 1.0 (grounded)
Answer relevance    → directly answers the question    = high
```

If the answer had said "50mm" instead, faithfulness would drop even though retrieval was perfect — that mismatch is exactly the signal that tells you it's a **generation bug**, not a **retrieval bug**.

---

## Agent-specific (your experience)

| Metric | Measures |
|--------|----------|
| Trajectory success | Efficient tool path? |
| Outcome | Business task completed? |
| Token waste | Loops / redundant retrieval? |

→ [[06 LLM/07 LLM & Generative AI/08 - LLM Evaluation Metrics|08 - LLM Evaluation Metrics]]

---

## The 4 test layers (interview framing)

```text
1. Unit        → retriever only: recall@k against a labeled query→doc set
2. Integration → full pipeline (API → retriever → LLM → response) works end-to-end
3. Evaluation  → faithfulness / relevance (RAGAS, LLM-as-judge)
4. Regression  → compare metrics vs. previous version on a fixed golden set
```

Same structure as [[15 Interview & Career/Technical Interview — Problem Solving Cheat Sheet#7. Testing|the Testing section of your interview cheat sheet]].

---

## Minimal eval set (pragmatic)

1. 50–100 real user questions
2. Human labels: which doc has the answer (your "gold" set)
3. Track **recall@k** before touching prompts — if the chunk isn't retrieved, no prompt can fix it
4. Add LLM-judge (faithfulness/relevance) only after retrieval is solid

---

## Common traps

| Trap | Correct |
|------|---------|
| Only BLEU/ROUGE on the final answer | Measure **retrieval** first — BLEU/ROUGE barely correlate with answer quality |
| One metric | Precision/recall/faithfulness trade off — track several |
| Blaming the LLM for a wrong answer | Check faithfulness first — a wrong answer with perfect faithfulness IS a retrieval bug |
| Skipping a labeled gold set | Without ground truth, recall@k can't be measured at all |

---

**Next chapter:** [[06 LLM/09 Knowledge Graphs/00 - Chapter Overview]]
