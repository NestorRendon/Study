# LLM Agents — Quick Overview

Agents extend LLMs beyond text generation by giving them **tools** and a **decision loop**:  
  
Loop:  
  1. LLM receives task + context  
  2. LLM decides: think / use tool / respond  
  3. If tool → execute (search, code, API call)  
  4. Result added to context  
  5. Repeat until task complete  
**Key components:**  
* **Reasoning** — chain-of-thought, ReAct (reason + act interleaved)  
* **Memory** — in-context (limited), vector DB (long-term retrieval)  
* **Tools** — web search, code interpreter, APIs, databases  
* **Planning** — task decomposition (ReAct, Tree of Thought, AutoGPT-style)  
**RAG (Retrieval-Augmented Generation)** — instead of memorizing all facts, retrieve relevant documents at inference time and inject into context. Reduces hallucination, keeps knowledge fresh.
