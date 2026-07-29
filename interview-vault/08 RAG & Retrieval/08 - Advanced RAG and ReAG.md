# Advanced RAG & ReAG

**Prev:** [[07 - Hallucination Control]] · **Next:** [[09 - GraphRAG]]

---

## In plain English

**Basic RAG** = one search, one answer. **Advanced RAG** = rewrite the question, search multiple times, rerank, or let the model **decide** what to fetch. **ReAG** adds explicit **reasoning** before and after retrieval.

**Step 7** — after the baseline pipeline works and grounding is in place.

---

## Pattern menu

| Pattern | What it does | When |
|---------|--------------|------|
| **Query rewriting** | LLM reformulates vague user query | Chatty questions |
| **HyDE** | Generate fake answer, embed *that* | Abstract queries |
| **Multi-query** | 3 paraphrases → merge results | Recall boost |
| **Reranking** | Cross-encoder scores top-20 → keep top-5 | Precision boost |
| **Agentic RAG** | LLM chooses tools (search, SQL, calc) | Complex tasks |

---

## ReAG vs basic RAG

| | Basic RAG | ReAG |
|---|-----------|------|
| Retrieval | Once | Loop: plan → search → check |
| Reasoning | Mostly at generation | Before + after retrieval |
| Cost | Lower | Higher (more LLM calls) |
| Best for | FAQ, single-doc Q&A | Analytics, multi-step |

**ReAG loop:**

```
1. Decompose question into sub-questions
2. Retrieve for each sub-question
3. Evaluate: "Do I have enough context?"
4. If not → search again with refined query
5. Generate final answer
```

---

## Evaluator–optimizer (agent pattern)

```
Generator → draft answer
Evaluator  → scores / finds gaps
Optimizer  → revises or triggers new retrieval
```

Used in production agent stacks (LangGraph-style).

---

## Your xFarm context (interview)

- **pgvector** for retrieval
- **Guardrails** on outputs
- **LLM-as-judge** + trajectory metrics for agents
- Problems: hallucinations, language switching → fix with retrieval quality + eval loops

---

## Common traps

| Trap | Correct |
|------|---------|
| "More LLM calls = always better" | Measure latency + $ + accuracy |
| Skip reranker to save cost | Often best ROI for precision |

---

**Next:** [[09 - GraphRAG]]
