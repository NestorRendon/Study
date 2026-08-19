# Summary

| Retrieval Type   | Representation  | Matching            |
| ---------------- | --------------- | ------------------- |
| TF-IDF           | sparse          | keyword             |
| BM25             | sparse          | keyword ranking     |
| Dense retrieval  | embeddings      | semantic similarity |
| Vector DB        | embedding index | nearest neighbor    |
| Hybrid retrieval | sparse + dense  | combined score      |
  
✅ **One-sentence intuition**  
* **Keyword retrieval** finds documents with the same words.  
* **Vector retrieval** finds documents with the same **meaning**.  
  
  
Documento  
   ↓  
Chunking (bloques de texto)  
   ↓  
Tokenization  
   ↓  
Embedding  
   ↓  
Vector DB  
  
  
ONLINE STAGE  
user query  
     ↓  
embedding  
     ↓  
vector search  
     ↓  
top-k documents  
     ↓  
(optional reranker)  
     ↓  
LLM prompt  
     ↓  
generated answer
