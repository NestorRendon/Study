# Hallucination Control

**Prev:** [[06 - Basic RAG Pipeline]] · **Next:** [[08 - Advanced RAG and ReAG]]

---

## In plain English

**Step 6** — RAG **reduces** hallucinations but does not eliminate them. You control risk with **prompting**, **retrieval quality**, **guardrails**, and **evaluation**.

---

## Sources of hallucination in RAG

| Cause | Fix |
|-------|-----|
| Wrong chunks retrieved | [[05 - Retrieval Quality]] |
| Right chunks, model ignores them | Stronger grounding prompt |
| Model adds outside knowledge | "Answer only from context" |
| Conflicting chunks | Rerank + dedupe |
| Long context, lost middle | Fewer, better chunks |

---

## Prompting controls

| Technique | Example |
|-----------|---------|
| **Strict grounding** | "Every claim must appear in context" |
| **Abstention** | "Say I don't know if not in context" |
| **Citations** | "Quote the sentence you use" |
| **Low temperature** | Less creative fabrication (0–0.3) |

---

## Post-generation checks

| Check | How |
|-------|-----|
| **Faithfulness** | LLM judge: is answer supported by context? |
| **Citation match** | String overlap with source chunk |
| **Guardrails** | Block policy violations → [[07 - Guardrails and Alignment]] |

---

## Your xFarm experience (interview)

- Hallucinations when retrieval missed agronomy docs
- Language switching → system prompt + guardrails
- **LLM-as-judge** + trajectory metrics on agent paths

---

## Common traps

| Trap | Correct |
|------|---------|
| "RAG = zero hallucination" | Measure **faithfulness** on eval set |
| Only tune the LLM prompt | Fix **retrieval** first |
| Huge context = better | More noise → more fabrication |

---

**Next:** [[08 - Advanced RAG and ReAG]]
