# Chunking Strategy

**Prev:** [[01 - What is RAG]] · **Next:** [[03 - Embedding Model Choice]]

---

## In plain English

You cannot stuff a whole manual into the model. **Chunking** cuts documents into pieces small enough to retrieve and fit in the context window — but large enough to keep meaning.

**This is step 1 of the index build** — before embeddings or vector DB.

---

## Chunk size guide

| Size | Effect |
|------|--------|
| **Too small** (~50 tokens) | Pronouns lose context ("it", "the policy") |
| **Sweet spot** (256–512 tokens) | Default for most doc Q&A |
| **Too large** (2000+ tokens) | Retrieval imprecise; noisy prompt |
| **Overlap** 10–20% | Same sentence in two chunks → better **recall** |

---

## Strategies

| Strategy | When to use |
|----------|-------------|
| **Fixed size + overlap** | Fast baseline |
| **By section / header** | Markdown, Confluence, legal |
| **Parent–child** | Retrieve small chunk, show **parent** to LLM |
| **Semantic boundaries** | Split when embedding similarity drops between sentences |

---

## Metadata (always store)

```json
{
  "chunk_id": "uuid",
  "source": "handbook.pdf",
  "page": 42,
  "section": "Refund policy",
  "updated_at": "2024-06-01"
}
```

Needed for: filtering, citations, debugging wrong answers.

---

## Special cases

| Content | Tip |
|---------|-----|
| Tables | Row-aware chunking or table summaries |
| Code | Keep functions intact |
| FAQs | One Q&A pair per chunk |

---

## Common traps

| Trap | Correct |
|------|---------|
| Chunk before cleaning HTML/PDF noise | **Preprocess** text first |
| No overlap on long policies | Add overlap at boundaries |
| Huge chunks because "more context" | Hurts **retrieval precision** |

---

**Next:** [[03 - Embedding Model Choice]]
