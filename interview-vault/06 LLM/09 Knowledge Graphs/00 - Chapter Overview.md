# Chapter 9 — Knowledge Graphs

**What this chapter is:** how to store **facts and relationships** explicitly (not just similar text). Read **after [[06 LLM/08 RAG & Retrieval/00 - Chapter Overview|Chapter 8 RAG]]** — they work together in GraphRAG.

**Overview = story only.** Detail notes hold RDF syntax, SPARQL, traps.

---

## The story

1. **Why graphs** — when vectors are not enough ([[01 - Knowledge Graph Core Concepts]])
2. **Write facts** — RDF & Turtle ([[02 - RDF and Turtle]])
3. **Schema & logic** — RDFS & OWL ([[03 - RDFS and OWL]])
4. **Query** — SPARQL ([[04 - SPARQL]])
5. **Production** — Neo4j & GraphRAG with Ch 8 ([[05 - Graph DB and GraphRAG]])

---

## Knowledge base vs knowledge graph vs RAG

| | Knowledge **base** (KB) | Knowledge **graph** (KG) | **RAG** (Ch 8) |
|---|-------------------------|--------------------------|----------------|
| **What it is** | Repository of organized knowledge | KB where facts are **nodes + edges** | Retrieve text → LLM |
| **Example** | Company wiki, FAQ DB | `(Alice)-[worksAt]->(Acme)` | Embed handbook chunks |
| **Query** | Search, browse, SQL | Traverse relationships | Vector similarity |
| **Strength** | Central source of truth | Multi-hop reasoning | Natural language prose |
| **Your work** | Landscape ecology KB (paper) | GCN / ontology for soundscapes | pgvector agents at xFarm |

**Interview line:** *"KB is the container; KG is the structured graph inside; RAG injects retrieved text into the LLM. GraphRAG combines KG traversal with vector entry points."*

---

## Stack mnemonic (memorize)

```
RDF      → stores facts (triples)
Turtle   → writes RDF nicely
RDFS     → simple schema (classes, domains)
OWL      → rich logic (constraints, equivalence)
SPARQL   → queries the graph
SHACL    → validates data shape
Neo4j    → popular property graph DB (Cypher)
```

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | Core concepts | [[01 - Knowledge Graph Core Concepts]] |
| 2 | RDF & Turtle | [[02 - RDF and Turtle]] |
| 3 | RDFS & OWL | [[03 - RDFS and OWL]] |
| 4 | SPARQL | [[04 - SPARQL]] |
| 5 | Neo4j & GraphRAG | [[05 - Graph DB and GraphRAG]] |

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **GraphRAG + LLM extraction** | Auto-build KGs from docs |
| **Property graphs** | Neo4j, Amazon Neptune |
| **Vector + graph** | Enterprise search stacks |

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| "KG replaces vector DB" | Use **together** (GraphRAG) |
| "Ontology = database" | Ontology = **schema**; instances = data |
| "SPARQL is SQL" | Graph **pattern** matching on triples |
| "Every project needs OWL" | RDFS enough for many schemas |
| "KG is only for Google-scale" | Domain KGs (finance, bio, agronomy) are common |

---

**Prev:** [[06 LLM/08 RAG & Retrieval/00 - Chapter Overview]] · **Next:** [[06 LLM/07.1 Transformers & Attention/00 - Chapter Overview]]

[[Home|← Home]]
