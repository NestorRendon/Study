# Agents & Workflows

**Prev:** [[08 - LLM Evaluation Metrics]] · **Next:** [[08 RAG & Retrieval/00 - Chapter Overview|RAG]]

---

## Interview one-liner

**Workflow:** fixed steps (A→B→C). **Agent:** LLM chooses actions dynamically toward a goal (ReAct, tool use). **Agentic AI:** AI embedded across business processes, not a single script.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Comparison

| | Workflow | Agent |
|---|----------|-------|
| Control | Deterministic | Adaptive |
| Debugging | Easier | Harder (non-deterministic) |
| Use case | ETL, training pipelines | Research, customer support bots |

---

## Agent loop

1. Observe task + context (+ retrieved memory)
2. Reason (CoT / ReAct)
3. Act: call tool (search, SQL, code, API)
4. Observe result → repeat until done

**Frameworks:** LangChain, LangGraph, AutoGen, CrewAI, Google ADK.

---

## Evaluation (agents)

| Metric | Measures |
|--------|----------|
| Trajectory success | Efficient tool path? |
| Outcome | Business goal achieved? |
| Transcript | Loops, wasted tokens? |

---

**Next chapter:** [[08 RAG & Retrieval/00 - Chapter Overview]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Lower temperature = smarter | Temperature controls **randomness**, not intelligence |
| Fine-tune full 70B on one GPU without QLoRA | Use LoRA/QLoRA or API |
| Context window = model memory forever | Context is **limited**; older tokens may be lost in long chats |
