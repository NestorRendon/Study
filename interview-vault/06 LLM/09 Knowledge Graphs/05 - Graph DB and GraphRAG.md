# Graph DB & GraphRAG

**Prev:** [[04 - SPARQL]] · **Next:** [[06 LLM/07.1 Transformers & Attention/00 - Chapter Overview|Transformers (Ch 10)]]

---

## In plain English

**Neo4j** (and similar) store graphs for fast traversal. **GraphRAG** builds (or uses) a graph from documents, then combines **vector search** + **graph walk** to feed the LLM.

---

## Neo4j + Cypher (quick)

```cypher
// Create
CREATE (a:Person {name: 'Alice'})-[:TEACHES]->(c:Course {title: 'ML'})

// Query
MATCH (p:Person)-[:TEACHES]->(c:Course)
WHERE c.title CONTAINS 'Machine'
RETURN p.name, c.title
```

---

## GraphRAG pipeline (Microsoft-style)

```
Documents
    → extract entities & relations (LLM or NLP)
    → build community summaries (optional)
    → store graph + text units
Query
    → vector search (entry points)
    → expand along edges
    → LLM answer with graph + text context
```

Paper: https://arxiv.org/pdf/2404.16130

---

## Link to your research

| Project | KG angle |
|---------|----------|
| Soundscape taxonomy | Species / site relationships |
| GCN landscape paper | Graph convolution on ecological network |
| Landscape ontology KB | Formal definitions (ontology) |

---

## Embeddings on graphs (bonus)

**TransE:** $\mathbf{h} + \mathbf{r} \approx \mathbf{t}$ for triple $(h,r,t)$ — used for link prediction.

---

## 30-second interview answer

> "I use vector RAG for unstructured text and knowledge graphs when questions require chained relationships. GraphRAG uses vectors to find entry entities, traverses the graph for structured context, and generates with grounded prompts. I've worked with ontology-style knowledge in landscape ecology and graph models like GCNs."

---

**Next chapter:** [[06 LLM/07.1 Transformers & Attention/00 - Chapter Overview]]
