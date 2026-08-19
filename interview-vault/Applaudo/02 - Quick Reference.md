# Applaudo Data Scientist — Quick Reference (durante la entrevista)

**Related:** [[01 - Study Notes]]

---

> [!important] El rol en una frase
> Investigador senior autónomo: construyes y evalúas matching de entidades de empresa (ML/embeddings/LLM) contra un baseline que ya está en producción, a **cientos de millones de entidades**. **NO productivizas** — eso es del equipo de engineering del cliente (Bain).

---

## Glosario de 10 segundos (si te preguntan, explica así)

| Término | Explicación en una línea |
|---|---|
| **Entity Resolution / Record Linkage** | Decidir si dos registros distintos son la misma entidad real |
| **Blocking / Candidate generation** | Reducir de billones de pares posibles a un subconjunto pequeño plausible, antes de comparar en detalle |
| **Firmográfico** | "Demográfico" pero de empresas: industria, tamaño, ingresos, ubicación |
| **Bi-encoder** | Embebe cada registro por separado → rápido, indexable con ANN |
| **Cross-encoder** | Embebe el PAR junto → más preciso, más caro, solo para candidatos ya filtrados |
| **ANN (Approximate Nearest Neighbor)** | Búsqueda de vecinos "casi exactos" en un espacio vectorial, rápida a gran escala (FAISS, HNSW) |
| **Golden record** | El registro canónico resultante tras fusionar duplicados |
| **Pairs completeness** | % de matches reales que sobrevivieron la etapa de blocking |
| **Reduction ratio** | Cuánto redujo el blocking el espacio total de comparación |
| **Data drift vs. concept drift** | Cambió la distribución de entrada, vs. cambió la relación input→respuesta correcta |

---

## La respuesta técnica central (tenla lista de memoria)

```text
ETAPA 1 — Candidate generation (barato, alto recall)
  Bi-encoder → embeddings → ANN search → top-k candidatos

ETAPA 2 — Reranking fino (caro, alta precisión)
  Cross-encoder o LLM → solo sobre los candidatos filtrados
```

> "A esta escala, comparar todo contra todo es matemáticamente inviable — con 100M de entidades son ~10^15 pares. Por eso primero reduzco el espacio con blocking/embeddings+ANN (candidate generation, optimizado para recall), y solo después aplico un método más caro y preciso (cross-encoder o LLM) sobre ese subconjunto reducido."

---

## LLM vs. baseline — el framework de una frase

> "Trato el LLM como una herramienta más, no el default. Lo comparo contra un baseline más barato en el mismo test set, midiendo costo y latencia además de accuracy. Muchas veces el mejor rol del LLM no es hacer todo el matching, sino revisar solo los casos ambiguos."

3 roles legítimos del LLM: **(1)** técnica de matching directa en candidatos filtrados, **(2)** quality ceiling para medir enfoques baratos, **(3)** revisión asistida de casos ambiguos.

---

## Métricas — no digas solo "accuracy"

| Métrica | Qué mide |
|---|---|
| Precision (a nivel de **pares**) | De los que marqué match, ¿cuántos son reales? |
| Recall (a nivel de **pares**) | De los matches reales, ¿cuántos encontré? |
| Pairs completeness | ¿El blocking perdió matches antes de comparar? |
| Reduction ratio | ¿Qué tan eficiente fue el blocking? |

Siempre menciona el **error analysis**: agrupa fallos por tipo (alias no reconocidos, multilingüe, jerarquía padre-subsidiaria) — no solo el número agregado.

---

## Costo/escala fijo — qué se sacrifica primero

```text
1. Tamaño del candidate set (top-k)
2. Complejidad del modelo de reranking (cross-encoder chico vs. LLM)
3. Frecuencia de reprocesamiento (todo vs. incremental)
4. Cobertura del método caro (% de pares revisados)
```

---

## Resultado negativo — cómo reportarlo (evaluado activamente)

```text
Hipótesis → Experimento → Resultado (específico, no evasivo) → Por qué (error analysis) → Qué sigue
```

> Frase fuerte de ejemplo: "La hipótesis era que embeddings de nombre+dominio bastarían; el error analysis mostró que fallaba en subsidiarias con nombres muy distintos al padre — la conclusión fue que hace falta una señal jerárquica adicional."

Un resultado negativo bien reportado = fortaleza, no debilidad. **No lo minimices ni lo escondas.**

---

## Los 4 niveles de ownership — sé preciso con cuál usas

| Nivel | Frase típica |
|---|---|
| Participating | "Formé parte del equipo que..." |
| Implementing | "Implementé el enfoque que ya habíamos definido..." |
| Independently designing | "Diseñé el experimento completo, desde la hipótesis..." |
| Owning production maintenance | "Fui responsable de mantener el modelo en producción..." |

**Estructura de cada historia:** Context → Problem → Your responsibility → Hypothesis/approach → Experiment → Result → Measurable impact → Lessons learned.

Si no tienes un número real de impacto: describe el resultado observable, **no inventes una métrica**.

---

## Los 7 escenarios — ángulo clave de cada uno

1. **Escala masiva** → candidate generation primero, escala como restricción desde el día 1
2. **Datos sucios/multilingües** → reglas para lo estructurado (sufijos legales), embeddings para lo semántico (alias)
3. **LLM vs. barato** → comparación justa, medir costo+latencia, no solo accuracy
4. **Hipótesis refutada** → reportar igual de claro que un resultado positivo
5. **Reentrenar clasificador** → diagnosticar drift vs. labeling issue antes de retrainear
6. **Presupuesto fijo** → razonamiento cuantitativo de qué sacrificar primero
7. **Stakeholder escéptico** → traducir trade-offs a términos evaluables, sin ponerte a la defensiva

---

## Preguntas para hacer tú (elige 2-3)

- ¿Cómo es el baseline actual y dónde falla más hoy?
- ¿Cómo es la cadencia de research — sprints o ciclos experimentales más largos?
- ¿Cómo es el handoff a engineering una vez validado un enfoque?
- ¿Cuál ha sido el problema de matching/escala más difícil que ha enfrentado el equipo?

---

## Mentalidad durante la respuesta (checklist mental de 5 segundos)

```text
1. Restablece el problema con tus palabras antes de responder
2. Si es ambiguo, declara tus supuestos en voz alta
3. Explica el POR QUÉ, no solo el qué
4. Menciona el trade-off — casi nunca hay una única respuesta correcta
5. Separa tu contribución individual de la del equipo
6. Cuantifica si puedes; si no, describe el resultado observable
```

---

[[01 - Study Notes|→ Ver notas de estudio completas]]
