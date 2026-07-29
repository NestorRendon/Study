# GraphRAG

**Prev:** [[08 - Advanced RAG and ReAG]] · **Next:** [[10 - RAG Evaluation]]

---

## In plain English

Some questions need **connecting dots** across documents:

> "Which suppliers in region A also deliver to factories owned by subsidiaries of company B?"

Vectors find similar **paragraphs**; **graphs** follow explicit **relationships**. **GraphRAG** uses both.

**Step 8** — when vector-only RAG is not enough; full KG stack in **Chapter 9**.

---

## How it works (simplified)

```
1. Build knowledge graph from corpus (entities + relations)
2. User question → vector search finds entry entities/chunks
3. Graph traversal collects related facts (multi-hop)
4. LLM answers with structured + text context
```

---

## When to add a graph (pragmatic)

| Signal | Action |
|--------|--------|
| Questions need 2+ hops | Consider KG |
| Many "who is related to X" | KG |
| Pure "what does paragraph say" | Vector RAG enough |
| Enterprise compliance / audit | KG + citations on edges |

→ Full KG stack: **[[09 Knowledge Graphs/00 - Chapter Overview|Chapter 9]]**

---

## vs vector-only RAG

| Vector RAG | GraphRAG |
|------------|----------|
| "Find similar text" | "Walk known relationships" |
| Great for prose | Great for org charts, supply chain, biology |

---

## Common traps

| Trap | Correct |
|------|---------|
| Build KG for everything | High cost — use when multi-hop need is proven |
| Graph without text evidence | Combine graph facts + source chunks for LLM |

---

**Next:** [[10 - RAG Evaluation]] · then **[[09 Knowledge Graphs/00 - Chapter Overview]]**
