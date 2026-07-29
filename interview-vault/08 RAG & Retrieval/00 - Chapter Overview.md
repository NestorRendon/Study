# Chapter 8 — RAG & Retrieval

**What this chapter is:** how to give an LLM **external knowledge** (your PDFs, wiki, database) so it answers with facts instead of guessing.

**Overview = story only.** Each numbered step links to a detail note with depth, traps, and interview lines.

---

## The story (production pipeline)

1. **What is RAG** — why retrieve before generate ([[01 - What is RAG]])
2. **Chunking strategy** — cut docs into retrievable pieces ([[02 - Chunking Strategy]])
3. **Embedding model choice** — same model for index + query ([[03 - Embedding Model Choice]])
4. **Indexing & vector stores** — ANN search at scale ([[04 - Indexing and Vector Stores]])
5. **Retrieval quality** — hybrid, rerank, recall@k ([[05 - Retrieval Quality]])
6. **Basic RAG pipeline** — prompt + generate ([[06 - Basic RAG Pipeline]])
7. **Hallucination control** — grounding, abstention, faithfulness ([[07 - Hallucination Control]])
8. **Advanced RAG / ReAG** — multi-step, agentic retrieval ([[08 - Advanced RAG and ReAG]])
9. **GraphRAG** — vectors + graph hops → **Ch 9** ([[09 - GraphRAG]])
10. **RAG evaluation** — measure retrieval and generation separately ([[10 - RAG Evaluation]])

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | What is RAG | [[01 - What is RAG]] |
| 2 | Chunking strategy | [[02 - Chunking Strategy]] |
| 3 | Embedding model choice | [[03 - Embedding Model Choice]] |
| 4 | Indexing & vector stores | [[04 - Indexing and Vector Stores]] |
| 5 | Retrieval quality | [[05 - Retrieval Quality]] |
| 6 | Basic RAG pipeline | [[06 - Basic RAG Pipeline]] |
| 7 | Hallucination control | [[07 - Hallucination Control]] |
| 8 | Advanced RAG & ReAG | [[08 - Advanced RAG and ReAG]] |
| 9 | GraphRAG (bridge to Ch 9) | [[09 - GraphRAG]] |
| 10 | Evaluation | [[10 - RAG Evaluation]] |

---

## RAG vs Knowledge Base vs Knowledge Graph

| | **Knowledge base** | **Vector RAG** | **Knowledge graph** |
|---|-------------------|----------------|---------------------|
| **Stores** | Documents, FAQs, structured entries | Text **chunks** + embeddings | **Triples** (subject–relation–object) |
| **Finds answers by** | Search / browse / rules | **Similar meaning** to question | **Following relationships** |
| **Best for** | Product docs, SOPs | Unstructured text Q&A | Multi-hop facts ("who reports to whom in country X") |
| **Chapter** | (concept) | **This chapter (8)** | **Next chapter (9)** |

**Your xFarm work:** pgvector + agents = **RAG (Ch 8)**. Landscape ontology paper = **KG (Ch 9)**.

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Hybrid search** | BM25 + dense default in production |
| **Rerankers** | Cross-encoders (Cohere, bge-reranker) |
| **GraphRAG** | Microsoft-style KG + vectors |
| **Agentic RAG** | Multi-step retrieval loops |

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| "RAG = no hallucinations" | Reduces errors; still evaluate **faithfulness** |
| "Bigger chunks = better" | Tune size (≈256–1024 tokens) + overlap |
| "Different embedding models for index vs query" | Use the **same** model both sides |
| "top-k = 1 is enough" | Often k=3–10 + optional **reranker** |
| "RAG replaces fine-tuning" | **Complementary** — RAG for facts, FT for style/behavior |
| "Vector DB stores full documents" | Stores **vectors** + IDs; text in blob/DB |

---

**Prev:** [[07 LLM & Generative AI/00 - Chapter Overview]] · **Next:** [[09 Knowledge Graphs/00 - Chapter Overview]]

[[Home|← Home]]
