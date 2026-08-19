# What is RAG?

**Prev:** [[06 LLM/08 RAG & Retrieval/00 - Chapter Overview]] · **Next:** [[02 - Chunking Strategy]]

---

## In plain English

**RAG** = **R**etrieve your documents → **A**ugment the LLM prompt with them → **G**enerate an answer. The model uses **your data at question time**, not only what it memorized in training.

---

## The full pipeline (preview)

```
Documents → CHUNK → EMBED → INDEX → RETRIEVE → PROMPT → GENERATE → CONTROL hallucinations
```

Each step has its own note in this chapter.

---

## Why RAG exists

| Problem | RAG helps |
|---------|-----------|
| Stale training data | Fresh docs in the index |
| Private / proprietary info | Your corpus, not the public web |
| Hallucinated facts | Ground answer in retrieved text |
| No citations | Metadata → source links |

---

## RAG vs fine-tuning (one line)

| | RAG | Fine-tuning (LoRA) |
|---|-----|-------------------|
| Updates | Re-index documents | Retrain weights |
| Best for | Changing facts, many docs | Style, format, task behavior |

---

## RAG vs. long-context prompting ("just put it all in the prompt")

With 200K–1M+ token context windows now common, the obvious question: why retrieve at all — why not paste every document straight into the prompt?

| | Long-context prompt | RAG |
|---|---|---|
| **Corpus size** | Fits one context window (dozens of docs) | Millions of docs, unbounded |
| **Cost per query** | Pay for **every token, every request** — even irrelevant ones | Pay only for the **retrieved chunks** |
| **Latency** | Grows with context size — prefill on 500K tokens is slow | Stays flat — same k chunks regardless of corpus size |
| **"Lost in the middle"** | LLMs attend worse to facts buried in the middle of a huge context | Retrieval surfaces only the relevant chunks near the top |
| **Freshness** | New document → re-send the whole context every time | New document → just re-index it |
| **Citations / traceability** | Harder to point to which part of a giant blob was used | Natural — you know exactly which chunk was retrieved |
| **Best for** | Small, fixed doc set; tasks needing **holistic** cross-document reasoning (e.g. "summarize this whole 40-page contract") | Large/growing corpus; most facts live in a **small relevant subset** per query |

**Interview line:** *"Long-context is great when the model genuinely needs to reason over everything at once — a single long contract, for example. RAG is better when the corpus is large and only a small, changing subset is relevant to any given question; sending everything every time is wasteful in cost and latency, and retrieval also gives you traceability for free."*

They are not mutually exclusive: a common production pattern is RAG to narrow millions of docs down to a manageable set, then feed a **larger** relevant chunk (not just top-3 tiny snippets) into a longer context window.

---

**Next:** [[02 - Chunking Strategy]] — start building the index
