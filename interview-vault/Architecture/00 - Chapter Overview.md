# Architecture — Chapter Overview

---

## The story

1. **Predict & serve** — how an ML system is wired end to end ([[01 - ML System Architecture]])
2. **Talk to an LLM** — RAG, agents, guardrails ([[02 - LLM and RAG Architecture]])
3. **Serve a request** — gateway → microservices → data ([[03 - Backend Microservices and API Architecture]])
4. **Move & analyze data** — pipelines, lake vs warehouse ([[04 - Data and Analytics Platform Architecture]])
5. **Scale it** — events, CQRS, caching, sharding ([[05 - Event-Driven CQRS and Scalability Patterns]])

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | ML system architecture | [[01 - ML System Architecture]] |
| 2 | LLM & RAG architecture | [[02 - LLM and RAG Architecture]] |
| 3 | Backend / microservices / API | [[03 - Backend Microservices and API Architecture]] |
| 4 | Data & analytics platform | [[04 - Data and Analytics Platform Architecture]] |
| 5 | Event-driven, CQRS, scalability | [[05 - Event-Driven CQRS and Scalability Patterns]] |

---

## How interviewers actually use these

They rarely ask "draw me an architecture" cold. They give a scenario ("design a recommendation service", "our RAG chatbot hallucinates", "reads are slow at 10k QPS") and want to see you **pick the right building blocks and justify the tradeoff** — not recite a diagram from memory. Use these notes to recognize the pattern fast, then narrate: *what's the bottleneck, what are 2 options, why this one, what do you give up.*

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| Naming every tool you've heard of | Name the **bottleneck** first, then the component that fixes it |
| Treating microservices as always better | Monolith is the right default until you have a real scaling/team reason to split |
| RAG as a fix for everything | RAG fixes *knowledge freshness/grounding*, not reasoning quality — fine-tuning/prompting solve different problems |
| Ignoring the write path when asked about scale | Reads and writes scale differently (caching vs sharding/queues) |
| No monitoring/feedback loop in ML designs | Offline metrics ≠ production behavior — always mention drift/monitoring |

---

[[Home|← Home]]
