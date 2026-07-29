# RDF & Turtle

**Prev:** [[01 - Knowledge Graph Core Concepts]] · **Next:** [[03 - RDFS and OWL]]

---

## In plain English

**RDF** is the standard way to write graph facts. **Turtle** is the human-friendly **file format** for RDF (like JSON for APIs).

---

## One fact in Turtle

```turtle
@prefix ex: <http://example.org/> .

ex:Alice  ex:teaches  ex:MachineLearning .
ex:Alice  ex:age      42 .
```

| Piece | Meaning |
|-------|---------|
| `@prefix` | Short nickname for long URIs |
| `ex:Alice` | Subject (entity URI) |
| `ex:teaches` | Predicate (relationship URI) |
| `ex:MachineLearning` | Object (another entity) |
| `42` | Object (literal number) |

---

## Why URIs?

Global unique IDs — merge graphs from different teams without name collisions.

---

## RDF vs property graph (Neo4j)

| | RDF (semantic web) | Property graph (Neo4j) |
|---|-------------------|------------------------|
| Standard | W3C, SPARQL | De facto Cypher |
| Facts | Triples | Nodes + labeled edges + properties |
| Best for | Linked data, ontologies | Apps, analytics, GraphRAG tools |

---

## Common traps

| Trap | Correct |
|------|---------|
| "Turtle is a different graph model" | Turtle **serializes** RDF |
| Confuse URL and string | Literals need quotes; entities are URIs |

---

**Next:** [[03 - RDFS and OWL]]
