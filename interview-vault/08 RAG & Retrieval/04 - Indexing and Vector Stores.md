# Indexing & Vector Stores

**Prev:** [[03 - Embedding Model Choice]] · **Next:** [[05 - Retrieval Quality]]

---

## In plain English

**Indexing** = store millions of chunk vectors so you can find the **nearest neighbors** to a query in milliseconds. The **vector database** holds vectors + metadata + pointers to raw text.

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

**Next:** [[05 - Retrieval Quality]]
