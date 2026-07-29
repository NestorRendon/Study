# What is RAG?

**Prev:** [[00 - Chapter Overview]] · **Next:** [[02 - Chunking Strategy]]

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

**Next:** [[02 - Chunking Strategy]] — start building the index
