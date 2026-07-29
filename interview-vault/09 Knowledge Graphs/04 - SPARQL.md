# SPARQL

**Prev:** [[03 - RDFS and OWL]] · **Next:** [[05 - Graph DB and GraphRAG]]

---

## In plain English

**SPARQL** is the query language for RDF graphs — like SQL, but you match **patterns of triples** instead of tables.

---

## SELECT example

**Question:** Who teaches Machine Learning?

```sparql
PREFIX ex: <http://example.org/>

SELECT ?person
WHERE {
  ?person  ex:teaches  ex:MachineLearning .
}
```

| Part | Role |
|------|------|
| `?person` | Variable (binding) |
| `WHERE { ... }` | Graph pattern to match |
| `SELECT` | Columns to return |

---

## More patterns

```sparql
# Optional match (like LEFT JOIN)
OPTIONAL { ?person ex:email ?email }

# Filter
FILTER(CONTAINS(STR(?name), "Smith"))

# Count
SELECT ?dept (COUNT(?p) AS ?n)
WHERE { ?p ex:worksIn ?dept }
GROUP BY ?dept
```

---

## SPARQL vs Cypher (Neo4j)

| | SPARQL | Cypher |
|---|--------|--------|
| Data model | RDF triples | Property graph |
| Syntax | `?var` patterns | `(a)-[:REL]->(b)` |
| Ecosystem | Semantic web | Neo4j, GraphRAG libs |

---

## Common traps

| Trap | Correct |
|------|---------|
| "SPARQL queries tables" | Queries **graph patterns** |
| Forget PREFIX | URIs must resolve |

---

**Next:** [[05 - Graph DB and GraphRAG]]
