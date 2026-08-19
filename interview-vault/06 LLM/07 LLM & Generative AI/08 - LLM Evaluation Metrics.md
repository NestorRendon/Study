# LLM Evaluation Metrics

**Prev:** [[07 - Guardrails and Alignment]] · **See also:** [[12 - Transformers MoE Diffusion Metrics and SOTA]] · **Next:** [[09 - Agents and Workflows]]

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
## In plain English

There is **no single score** for “good chatbot.” Pick metrics for the **task**: summarization, RAG, agents. Evaluate **retrieval** and **generation** separately when using RAG.

---

## Reference-based (n-gram overlap)

| Metric | Best for | Weakness |
|--------|----------|----------|
| **BLEU** | Machine translation | Ignores meaning |
| **ROUGE** | Summarization | Same |
| **COMET** | Semantic MT quality | Needs model |

---

## LLM-as-a-Judge (G-Eval)

Use a **rubric** + judge LLM to score:

| Dimension | Example question |
|-----------|------------------|
| Correctness | Factually right? |
| Coherence | Well structured? |
| Safety | Policy violations? |

**Judge prompt structure (conceptual):**

```
Task: Rate the answer 1-5 on correctness.
Criteria: ...
Context: ...
Answer to evaluate: ...
```

**Trap:** judge bias — calibrate against human labels on a golden set.

---

## RAG metrics (always split stages)

| Stage | Metrics |
|-------|---------|
| Retrieval | Context precision, context recall |
| Generation | Faithfulness, answer relevance |

→ [[10 - RAG Evaluation]]

---

## Agent metrics (your xFarm experience)

| Metric | Measures |
|--------|----------|
| Trajectory success | Efficient tool path? |
| Outcome | Task actually completed? |
| Token cost | Waste / loops? |

---

## Perplexity

$$\text{PPL} = \exp\left(-\frac{1}{N}\sum_i \log P(w_i \mid w_{<i})\right)$$

Useful for **model comparison** on a corpus — not enough alone for product quality.

---

## Common traps

| Trap | Correct |
|------|---------|
| BLEU for chat quality | Task-specific rubrics |
| One automated metric | Human eval on critical samples |

---

**Next:** [[09 - Agents and Workflows]]
