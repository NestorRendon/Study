# GraphRAG — Combining Both

Standard RAG: embed documents → retrieve top-K chunks → feed to LLM.  
**GraphRAG** (Microsoft, 2024): build a knowledge graph from documents first, then use both graph traversal AND vector similarity for retrieval.  
  
Document ingestion:  
  Text → Entity extraction → Relation extraction → Knowledge Graph  
                                                  + Vector embeddings  
Query time:  
  1. Embed query → find relevant entities (vector search)  
  2. Traverse graph from those entities (multi-hop)  
  3. Collect subgraph + relevant chunks  
  4. Feed enriched context to LLM  
**Why it matters:** dramatically reduces hallucination on complex multi-entity questions. The LLM gets structured facts, not just similar-sounding text.  
  
  
  
Agentic frameworks organize **LLMs + tools + workflows** so models can **reason, act, and coordinate tasks**. Instead of a single prompt, they use **orchestration patterns** that control how multiple steps interact.  
Below are the **three key orchestration patterns** you mentioned.
