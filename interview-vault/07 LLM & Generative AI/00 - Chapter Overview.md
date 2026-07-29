# Chapter 7 — LLM & Generative AI

> **Note:** Old fragment notes (`Answer A`, `Judge prompt`, etc.) were moved to `Archive/legacy-vault-notes/` — they are **not** part of this chapter.

---

## The story

1. **Foundations** — encoder vs decoder, GPT family ([[01 - LLM Foundations Encoder and Decoder]])
2. **Tokenize** — BPE, context limits ([[02 - Tokenization]])
3. **Prompt** — few-shot, chain-of-thought ([[03 - Prompting Techniques]])
4. **Scale cheaply** — mixture of experts ([[04 - Mixture of Experts MoE]])
5. **Specialize** — LoRA, quantization, QLoRA ([[05 - LoRA and PEFT]])
6. **Infer fast** — KV cache ([[06 - KV Caching]])
7. **Stay safe** — guardrails, alignment ([[07 - Guardrails and Alignment]])
8. **Evaluate** — quality metrics ([[08 - LLM Evaluation Metrics]])
9. **Act** — agents and workflows → then **Ch 8 RAG** for your data ([[09 - Agents and Workflows]])


![[Pasted image 20260723125503.png]]
---

![[Pasted image 20260724093356.png]]

[![AI Model Releases May 2026 — GPT-5.5, Gemma 4, Claude & Grok Updates |  AIToolsRecap](https://aitoolsrecap.com/ArticleImages/ai-model-releases-may-2026-what-to-expect-1777534004.jpg)![AI Model Releases May 2026 — GPT-5.5, Gemma 4, Claude & Grok Updates |  AIToolsRecap](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdDQusC41Og8BmuBJEZT-tMG3v-Hl77iaJntyOBl_Jxg&s=10)1,280 × 853](https://aitoolsrecap.com/Blog/ai-model-releases-may-2026-what-to-expect)

![[Pasted image 20260724093057.png]]


## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | LLM foundations (BERT vs GPT) | [[01 - LLM Foundations Encoder and Decoder]] |
| 2 | Tokenization | [[02 - Tokenization]] |
| 3 | Prompting | [[03 - Prompting Techniques]] |
| 4 | MoE (scale efficiently) | [[04 - Mixture of Experts MoE]] |
| 5 | LoRA / PEFT (specialize) | [[05 - LoRA and PEFT]] |
| 6 | KV caching (fast inference) | [[06 - KV Caching]] |
| 7 | Guardrails & alignment | [[07 - Guardrails and Alignment]] |
| 8 | Evaluation | [[08 - LLM Evaluation Metrics]] |
| 9 | Agents & workflows | [[09 - Agents and Workflows]] |

---

## SOTA & trends (2024–2026)

| Trend | Interview line |
|-------|----------------|
| **MoE models** | Mixtral, GPT-4 class — many params, few active per token |
| **Small models + LoRA** | 7B–70B fine-tunes beat generic giants on domain |
| **Long context** | 128k–1M tokens; RAG still needed for private data |
| **Agents** | LangGraph, ADK, tool-use — your xFarm stack |
| **Alignment** | RLHF, DPO, LlamaGuard classifiers |
| **Open weights** | Llama 3, Mistral, Qwen — on-prem option |

---
![[Pasted image 20260723130400.png]]
## Common traps

| Trap | Correct |
|------|---------|
| "RAG replaces fine-tuning" | **Complementary** |
| "Temperature = intelligence" | Controls **randomness** |
| "Context window = perfect memory" | Lost-in-the-middle, truncation |

![[Pasted image 20260723154900.png]]
---


Métricas de Entrenamiento y Validación

- **Pérdida (_Loss_ / _Cross-Entropy Loss_):** Mide qué tan bien predice el modelo el siguiente token en los datos de entrenamiento; debe disminuir de forma estable. [[1](https://ecosistemastartup.com/como-entrenar-un-llm-desde-cero-guia-completa-de-optimizacion/)]

- **Perplejidad (_Perplexity_):** Calcula la exponenciudad o incertidumbre del modelo ante una secuencia de texto; un valor menor indica que el modelo comprende y anticipa mejor el lenguaje del dominio. [[1](https://dev.to/gcjordi/evaluacion-y-metricas-en-la-evaluacion-de-modelos-de-ia-no4)]

Métricas de Evaluación de Texto

- **BLEU y ROUGE:** Comparan la respuesta generada por el modelo con una respuesta de referencia ideal usando la coincidencia de palabras.

- **Exactitud (_Accuracy_ / _Precision_, _Recall_, _F1-Score_):** Útiles en tareas de clasificación o extracción donde la respuesta esperada es categórica o estructurada. [[1](https://es.linkedin.com/pulse/como-evaluar-la-calidad-de-las-respuestas-un-chatbot-creado-c%C3%A1ceres-fooqe), [2](https://www.datacamp.com/es/tutorial/flan-t5-tutorial), [3](https://www.youtube.com/watch?v=1Jr4QOFI0qw)]

Marcos de Evaluación con IA (_LLM-as-a-Judge_)

- **Ragas y G-Eval:** Evalúan la calidad, fidelidad y relevancia de las respuestas utilizando otro modelo como juez.

- **Precisión de instrucción:** Mide si el modelo sigue de manera correcta las reglas y restricciones del prompt tras el reentrenamiento.




**Prev:** [[06 NLP & Text Mining/06 - BERT and Contextual NLP]] · **Next:** [[08 RAG & Retrieval/00 - Chapter Overview]]

[[Home|← Home]]
