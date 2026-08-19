# Indexing & Vector Stores

**Prev:** [[03 - Embedding Model Choice]] · **Next:** [[05 - Retrieval Quality]]

---

## In plain English

Indexing in Retrieval-Augmented Generation (RAG) is ==the pipeline step that structures and organizes external data so an AI model can quickly search and retrieve relevant context==. It involves gathering source files, splitting them into small text chunks, converting those chunks into vector embeddings via machine learning models, and saving them into a vector database. [[1](https://www.meilisearch.com/blog/rag-indexing), [2](https://www.youtube.com/shorts/dtS8PjOHObI)]

Key Stages of the Indexing Pipeline

- **Data Collection**: Gather raw content from external files like PDFs, databases, or websites.

- **Text Cleaning**: Remove unparseable symbols, fix spacing, and clear out repetitive headers.

- **Document Chunking**: Break large files into smaller segments so they fit inside token limits while retaining local context.

- **Metadata Tagging**: Attach labels (such as dates, categories, or source URLs) to each chunk for precise filtering.

- **Embedding Generation**: Convert text chunks into numerical vectors that represent semantic meaning.

- **Vector Storage**: Save vectors into specialized systems like Pinecone or Milvus. [[1](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation), [2](https://www.youtube.com/watch?v=NytKzh8avhw&t=9), [3](https://www.meilisearch.com/blog/rag-indexing)]
**Step 3** — after chunks exist and embeddings are computed.

---

## Index build (offline)

```
Chunks + embeddings + metadata  →  ANN index (HNSW, IVF, etc.)  →  Vector DB
```

| Index type | Trade-off |
|------------|-----------|
| **HNSW** | High recall, good default |
| **IVF** | Faster at very large scale |
| **Flat** | Exact, small corpora only |
Common Vector Indexing Algorithms

- **Flat Indexing**: A complete brute-force search comparing queries against every vector; highly accurate but slow.

- **HNSW (Hierarchical Navigable Small World)**: Organizes vectors into a multi-layered graph for very fast, high-accuracy searches.

- **IVF (Inverted File Index)**: Groups vectors into clusters using centroids to narrow down the search space over massive datasets.

- **Product Quantization (PQ)**: Compresses vector sizes heavily to minimize memory usage during large-scale retrieval. [[1](https://www.ai-bites.net/rag-7-indexing-methods-for-vector-dbs-similarity-search/), [2](https://machinelearningmastery.com/understanding-rag-part-vii-vector-databases-indexing-strategies/), [3](https://www.youtube.com/watch?v=NytKzh8avhw&t=9)]
---

## Query (online)

```
User question → embed q → ANN search → top-k chunk IDs → fetch text from store
```

---

## Vector DB options

| Tool | When |
|------|------|
| **pgvector** | Already on Postgres (your xFarm stack) |
| Pinecone / Weaviate / Qdrant | Managed, scale-out |
| Milvus | Large self-hosted |

**Store:** `id`, `embedding`, `metadata`, `content` or blob pointer.

---

## pgvector example (conceptual)

```sql
SELECT id, content, embedding <=> query_embedding AS distance
FROM document_chunks
WHERE department = 'legal'
ORDER BY distance
LIMIT 10;
```

---

## Common traps

| Trap | Correct |
|------|---------|
| Vectors only, no text stored | Keep **content** or retrievable pointer |
| No metadata filters | Add dept, date, ACL fields at index time |
| Index once, never update | Plan **incremental** re-index on doc changes |

---

**Want the full deep dive?** This note is the quick version — a dedicated 5-note arc covers vector DBs from scratch, similarity metrics, ANN index internals, framework comparisons, and a full query/command cheat sheet: start at [[04.1 - Vector Databases from Scratch]].

---

**Next:** [[04.1 - Vector Databases from Scratch]]
