# Knowledge Graph Core Concepts

**Prev:** [[06 LLM/09 Knowledge Graphs/00 - Chapter Overview]] · **Next:** [[02 - RDF and Turtle]]

---

## In plain English

A **knowledge graph** is a map of **things** (entities) and **how they relate**.  
Example: `Paris → capital_of → France → located_in → Europe`.

A **vector database** asks: *"Which paragraphs look like my question?"*  
A **knowledge graph** asks: *"What is connected to X through relationship Y?"*

---

## The triple (atomic fact)

```
(Subject)  —[Predicate]→  (Object)

(Paris)    —[capital_of]→ (France)
(Alice)    —[teaches]→    (MachineLearning)
```

| Part | Meaning | Example |
|------|---------|---------|
| **Subject** | Entity | `Paris` |
| **Predicate** | Relationship type | `capital_of` |
| **Object** | Entity or literal | `France` or `"42"` |

---

## Ontology vs knowledge base vs knowledge graph

| Term | Plain English | Analogy |
|------|---------------|---------|
| **Ontology** | Allowed types & rules | Database **schema** |
| **Knowledge base** | All stored knowledge | The **database** |
| **Knowledge graph** | KB as nodes + edges | **Graph** view of the KB |

**Open world assumption (OWL):** "If we don't know, it might still be true" — vs SQL closed world.

---

## Multi-hop query (why graphs win)

**Question:** *Authors born in France who influenced Picasso?*

```
Vector RAG:  hope one paragraph mentions all facts
Graph:       Person → bornIn → France
             Person → influenced → Picasso
             (traverse 2 hops)
```

---

## When to use (pragmatic)

| Use KG | Skip KG (vectors enough) |
|--------|--------------------------|
| Org charts, supply chain | Single-doc FAQ |
| Drug–gene–disease | Pure sentiment on tweets |
| Your landscape taxonomy / species relations | Simple keyword search |

→ Combine with RAG: [[09 - GraphRAG]]

---

## Common traps

| Trap | Correct |
|------|---------|
| "KG = knowledge base" | KG is a **structured** KB as graph |
| "Build KG from scratch day 1" | Start with RAG; add KG when multi-hop pain appears |

---

## 30-second interview answer

> "A knowledge graph stores facts as subject–predicate–object triples and supports multi-hop queries over relationships. Vector RAG is better for unstructured text similarity. In enterprise I combine them: vectors find entry points, graphs expand structured context — GraphRAG."

---

**Next:** [[02 - RDF and Turtle]]
