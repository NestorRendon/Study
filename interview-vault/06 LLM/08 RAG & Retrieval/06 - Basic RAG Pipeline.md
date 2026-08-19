# Basic RAG Pipeline

**Prev:** [[05 - Retrieval Quality]] · **Next:** [[07 - Hallucination Control]]

---

## In plain English

**Step 5** — assemble everything: user question → retrieve chunks → build prompt → LLM answers. This is the **minimum viable RAG** every interview expects you to draw.

---

## End-to-end diagram

```
┌──────────────┐
│ User question│
└──────┬───────┘
       ▼
┌──────────────┐     Steps 1–3 already done offline:
│ Embed query  │     chunk → embed → index
└──────┬───────┘
       ▼
┌──────────────┐
│ Retrieve k   │  ← Step 4: quality / hybrid / rerank
│   chunks     │
└──────┬───────┘
       ▼
┌──────────────┐
│ Prompt =     │
│  system rules│
│  + CONTEXT   │
│  + question  │
└──────┬───────┘
       ▼
┌──────────────┐
│ LLM generate │
└──────────────┘
```

---

## Prompt template

```
Answer ONLY from the context below. If unknown, say "I don't know."
Cite the source section when possible.

### Context
{chunk_1}
---
{chunk_2}

### Question
{user_question}
```

---

## Token budget

| Piece | Typical share |
|-------|-----------------|
| System + question | Fixed |
| Retrieved chunks | Fill remaining window |
| Leave room for answer | Don't use 100% on context |

---

## When basic RAG fails

| Symptom | Go to |
|---------|-------|
| Multi-hop questions | [[08 - Advanced RAG and ReAG]] |
| Relationship queries | [[09 - GraphRAG]] → Ch 9 |
| Answer not grounded | [[07 - Hallucination Control]] |

---

**Next:** [[07 - Hallucination Control]]
