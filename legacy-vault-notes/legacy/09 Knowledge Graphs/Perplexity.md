# 🧪 Perplexity

is a fundamental evaluation metric in natural language processing (NLP) that measures how well a probability model, specifically a language model (LM), predicts a sample.   
  
  
  
Frameworks :   
  
  
  
Here's the plain text table — copy-paste ready:  

| Framework | Mental Model | RAG Support | Chunking | Embeddings | Vector DBs | Knowledge Graphs | Ontologies | Strengths | Weaknesses | Best For | Avoid When | Hybrid Arch |
| ---------- | -------------------------- | ------------------ | ------------------------------------------- | ------------- | -------------------- | ----------------------------------- | ------------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------- |
| LangChain | Pipeline / Chain | ⭐⭐⭐ Full stack | Via text splitters | 20+ providers | 50+ integrations | Partial — Neo4j plugin | No native | Huge ecosystem, fast prototyping, most integrations | Abstraction leaks, hard to debug, heavy deps | Prototyping, standard RAG, batteries-included teams | Need full control, low latency, minimal deps | Pairs with LangGraph for agents |
| LangGraph | Stateful Graph / DAG | ⭐⭐ Via LangChain | Via LangChain | Via LangChain | Via LangChain | Partial — flow graph only, not data | No | Complex agents, branching logic, human-in-the-loop, persistence | Steep learning curve, verbose, overkill for linear flows | Multi-agent systems, approval flows, long-running workflows | Simple Q&A, one-shot pipelines, LLM beginners | Orchestrates LangChain + LlamaIndex tools |
| LlamaIndex | Index / Retrieval Engine | ⭐⭐⭐⭐ Best-in-class | Advanced — semantic, sentence, hierarchical | 20+ providers | 40+ integrations | Strong — native KG Index | Partial — entity/relation extraction | RAG quality, query routing, hybrid search, re-ranking | Smaller agent ecosystem, less mature UI tooling | Production RAG, document Q&A, structured + unstructured data | Pure agent orchestration | Best RAG layer for any stack |
| Google ADK | Agent / Tool-use | ⭐⭐ Basic | Via Vertex AI | Via Vertex AI | Via Vertex AI Search | Partial — Google KG API | No | Native Gemini, GCP services, enterprise auth | GCP lock-in, weak RAG primitives, immature outside GCP | Google Cloud shops, Gemini-first, enterprise GCP | Multi-cloud, advanced RAG, non-GCP infra | Plugs into GCP data services |
| CrewAI | Role-based Multi-agent | ⭐ Minimal | No native | Via tools | Via tools | None | No | Intuitive role/task model, great DX, easy multi-agent | No RAG, no graph support, limited prod readiness | Task delegation, simulating team collaboration | Production RAG, complex state, enterprise deployments | Wrap LlamaIndex for retrieval tools |
| Haystack | Pipeline / Component Graph | ⭐⭐⭐ Strong | Modular preprocessors | 15+ providers | 30+ integrations | Partial — custom components | No | Production-grade, modular, type-safe, NLP-heavy apps | Smaller community, less agent tooling, steeper than LangChain | Enterprise search, document processing, on-prem | Quick prototyping, heavy agent needs | Good standalone or with LangGraph |
  
Neo4j es una base de datos orientada a grafos, específicamente clasificada como un sistema NoSQL de "propiedad de grafos" (property graph). +  
  

| Framework | Purpose | When to Use |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LangChain | Modular framework for building LLM-powered applications by chaining prompts, tools, memory, retrievers, and external integrations. | Use when building standard LLM pipelines, tool-calling workflows, RAG systems, or prototypes requiring broad ecosystem support. |
| LangGraph | Graph-based orchestration framework for designing stateful, multi-step, branching, and multi-agent workflows on top of LangChain. | Use when workflows require loops, branching logic, persistent state, human-in-the-loop steps, or complex agent orchestration. |
| LlamaIndex | Data framework specialized for connecting LLMs with external/private data sources through indexing, retrieval, and RAG pipelines. | Use when the primary challenge is retrieval over documents/data rather than agent orchestration; ideal for advanced RAG systems. |
| Google ADK | Framework for building production-grade AI agents with structured tool use, orchestration, evaluation, and deployment support in Google’s ecosystem. | Use when building enterprise or production agents, especially if leveraging Google infrastructure/tools or requiring structured agent deployment patterns. |
| CrewAI | Multi-agent framework focused on role-based autonomous agent collaboration and task delegation between specialized agents. | Use when modeling collaborative multi-agent systems where agents have distinct roles, responsibilities, and delegated subtasks. |
| Haystack | NLP/LLM orchestration framework focused on production search, retrieval, QA pipelines, and scalable RAG architectures. | Use when building production retrieval/search systems, document QA, or scalable enterprise-grade RAG pipelines. |
