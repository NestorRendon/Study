# Applaudo Data Scientist — Study Notes (Bain Engagement)

**Related:** [[02 - Quick Reference]]

---

> [!abstract] El rol en una frase
> Eres un investigador senior autónomo que construye y evalúa (no despliega) enfoques de **matching de entidades de empresas** — ML, embeddings, LLMs — contra un motor de matching que ya existe en producción, a una escala de **cientos de millones de entidades** desde 15+ fuentes de datos distintas.

---

## Índice

1. [[#1. El contexto — quién, para quién, qué]]
2. [[#2. Entity Resolution — los fundamentos]]
3. [[#3. El problema de la escala — blocking y candidate generation]]
4. [[#4. Embeddings y similaridad semántica]]
5. [[#5. LLM vs. baseline más barato]]
6. [[#6. Diseño experimental y evaluación]]
7. [[#7. Clasificación, NLP y mantenimiento en producción]]
8. [[#8. Diseño consciente del costo y la escala]]
9. [[#9. Comunicar trade-offs y resultados negativos]]
10. [[#10. Cómo posicionar tus 3-4 historias]]
11. [[#11. Los 7 escenarios — cómo pensarlos]]
12. [[#12. Frameworks y herramientas del mundo real]]
13. [[#13. Algoritmos útiles, explicados]]
14. [[#14. Buenas prácticas]]
15. [[#15. ¿Knowledge Graphs ayudan aquí?]]

---

## 1. El contexto — quién, para quién, qué

- **Applaudo** = empresa de ingeniería/producto digital. Tú serías **talento embebido senior** en el equipo del cliente — se espera ownership real, no ejecutar tickets aislados.
- **Cliente: Bain & Company** (consultora de gestión global). El proyecto: un **grafo unificado de entidades de empresa**, construido a partir de 15+ fuentes de datos de terceros.
- **Ya existe un motor de matching en producción** — cualquier cosa que propongas se compara contra ese baseline real, no contra "nada".
- **Cadencia de investigación, no sprints fijos** — el entregable es razonamiento bien documentado y defendible, no un feature shippeable cada 2 semanas.
- **División clara research vs. engineering**: tú construyes y evalúas; un equipo de ingeniería del lado del cliente productiviza lo que se valida. **No es tu responsabilidad llevarlo a producción.**
- **Datos genuinamente sucios**: nombres, alias, dominios, sitios web, atributos firmográficos, registros multilingües, jerarquías inconsistentes — esto es el día a día, no un caso extremo.

> **Firmográfico (firmographic)** — es el equivalente de "demográfico" pero para empresas en vez de personas: industria, tamaño, ingresos, ubicación, año de fundación, etc. Un atributo firmográfico es cualquier dato descriptivo sobre una empresa como entidad de negocio.

**Lo que este rol NO es:** no vas a diseñar la arquitectura de la plataforma de matching, no vas a hacer adjudicación manual de matches a volumen, no vas a hacer gestión de producto. Tu accountability es el **rigor y la honestidad del experimento**, no el shipping.

---

## 2. Entity Resolution — los fundamentos

**Entity Resolution (ER)**, también llamado **record linkage** o **deduplication**, es el problema de decidir si dos registros distintos (con formato, idioma o completitud diferentes) se refieren a la **misma entidad real** — en este caso, la misma empresa.

```text
Registro A: "Acme Corp.", acme.com, USA
Registro B: "ACME Corporation Inc.", www.acme.com, United States
                              ↓
                  ¿Es la misma empresa? → SÍ (match)
```

Por qué es difícil en la práctica:
- **Variaciones de nombre**: "Acme Corp." vs "ACME Corporation Inc." vs "Acme" (abreviaturas, sufijos legales, mayúsculas)
- **Alias**: nombres comerciales distintos al nombre legal
- **Multilingüe**: el mismo negocio reportado en inglés, español, alemán...
- **Jerarquías inconsistentes**: ¿es una subsidiaria, una división, o una entidad separada?
- **Sin ground truth claro** — a diferencia de un dataset de benchmark limpio, aquí "la respuesta correcta" muchas veces hay que construirla tú mismo con labeling

**Terminología clave que debes usar con soltura:**

| Término | Qué significa |
|---|---|
| **Match** | Dos registros son la misma entidad real |
| **Non-match** | Dos registros son entidades distintas |
| **Possible match** | Ambiguo — necesita revisión (humana o de un modelo más caro) |
| **Golden record** | El registro "canónico" resultante después de fusionar duplicados |
| **Canonicalización** | Normalizar variantes a una forma estándar antes de comparar (ej. "Corp." → "Corporation") |
| **Blocking** | Reducir el espacio de comparación antes de comparar en detalle (ver sección 3) |

---

## 3. El problema de la escala — blocking y candidate generation

### 3.1 Por qué "comparar todo contra todo" es literalmente imposible

Imagina que tienes solo **4 registros**: A, B, C, D. Para saber si hay duplicados, comparas cada par una vez: A-B, A-C, A-D, B-C, B-D, C-D → **6 comparaciones**. La fórmula de cuántos pares únicos hay entre `n` elementos es:

```text
pares = n × (n-1) / 2
```

Con 4 elementos: 4×3/2 = 6 ✓. Ahora escala esto a la realidad del proyecto:

```text
n = 100,000,000 (cien millones de entidades)

pares = 100,000,000 × 99,999,999 / 2
      ≈ 5,000,000,000,000,000
      = 5 × 10^15  (5 mil billones, "5 quadrillion" en inglés)
```

Para que el número tenga sentido: si tu computadora pudiera evaluar **mil millones de pares por segundo** (extremadamente rápido, poco realista), igual tardaría:

```text
5 × 10^15 pares ÷ 10^9 pares/segundo = 5,000,000 segundos ≈ 58 días
```

Y eso asumiendo que cada comparación es prácticamente gratis — en la realidad, cada comparación implica calcular similaridad de texto, quizás llamar a un modelo, etc., lo que la hace miles de veces más lenta que "un cálculo simple". **Por eso el enfoque de fuerza bruta (comparar todo con todo) no es "lento", es directamente inviable.**

Esto es lo que en notación de complejidad algorítmica se llama **O(n²)** — el trabajo crece con el **cuadrado** del número de elementos. Si duplicas los datos, el trabajo no se duplica, se **cuadruplica**. Es la misma idea de "por qué usar una lista en vez de un hash table para buscar un elemento" que seguramente ya conoces — aquí el mismo principio aplica a nivel de sistema completo, no a una sola búsqueda.

### 3.2 La solución: reducir el candidate set ANTES de comparar en detalle

La idea central es simple: **no necesitas comparar A contra los 100 millones de registros — solo contra un puñado que YA sabes que son plausiblemente parecidos.** Ese proceso de reducir el universo de comparación se llama **blocking** o **candidate generation**.

```text
TODOS los pares posibles → 5 × 10^15 (inviable)
         ↓
   BLOCKING / CANDIDATE GENERATION
   (reduce a un subconjunto pequeño de candidatos plausibles,
    ej. de 100M de comparaciones posibles por registro a ~50)
         ↓
   COMPARACIÓN DETALLADA solo de esos candidatos
   (ahora sí, algo preciso y caro: embeddings finos, cross-encoder, LLM)
         ↓
   Match / Non-match / Possible match
```

El objetivo del blocking **no es tener 0% de error** — es tener **alto recall** (no perder matches reales) aceptando algo de ruido, porque ese ruido se filtra después en la etapa de comparación fina. Si el blocking pierde un match real, ya no hay forma de recuperarlo después — por eso se optimiza para no perder candidatos, no para ser exacto.

### 3.3 Técnicas de blocking, explicadas una por una con ejemplo

**a) Blocking por clave exacta**

La técnica más simple: agrupas los registros por un campo que asumes que los duplicados van a compartir, y solo comparas dentro de cada grupo.

```text
Ejemplo: agrupar por país + primeras 3 letras del nombre

Grupo "USA-ACM":
  - "Acme Corp"      (USA)
  - "ACME Corporation Inc" (USA)
  - "Acme Trading"    (USA)   ← falso candidato, pero ok, se descarta después

Grupo "MEX-ACM": (vacío o distinto)
```

En vez de comparar el registro "Acme Corp" contra 100 millones de registros, solo lo comparas contra los ~5-10 que cayeron en el mismo grupo. **Problema:** si hay un typo o el campo clave está mal capturado (ej. el país está vacío o mal escrito), el registro nunca cae en el grupo correcto y el match se pierde para siempre — de ahí que el guide diga "genuinely messy data" es el reto central, no un caso raro.

**b) Sorted Neighborhood**

En vez de agrupar por una clave exacta (todo o nada), **ordenas** todos los registros por una clave (ej. alfabéticamente por nombre normalizado), y solo comparas cada registro contra los que están **cerca en esa lista ordenada** (una ventana deslizante de tamaño fijo, ej. 10 registros antes y después).

```text
Lista ordenada alfabéticamente:
  ...
  "Acer Inc"
  "Acme Corp"        ← ventana de comparación (tamaño 3)
  "Acme Corporation"  ← se compara con los 3 antes y 3 después
  "Acme Trading Co"
  "Acorn Systems"
  ...
```

Es más tolerante que el blocking exacto porque nombres parecidos quedan cerca al ordenar alfabéticamente aunque no compartan exactamente la misma clave — pero sigue fallando si la variación ocurre justo al inicio del nombre (ej. "The Acme Company" ordena muy lejos de "Acme Company" porque empieza con "The").

**c) LSH — Locality-Sensitive Hashing**

Esta es más sofisticada, vale la pena entenderla bien porque suena a "caja negra" si no la explicas con ejemplo.

Un hash normal (como los que usa un `dict`/`set` de Python) está diseñado a propósito para que inputs parecidos den **hashes completamente distintos** — eso evita colisiones. **LSH hace lo contrario a propósito**: está diseñado para que inputs *parecidos* tengan **alta probabilidad de caer en el mismo bucket** (mismo hash), y los inputs distintos caigan en buckets distintos.

```text
Hash normal:        "Acme Corp" → hash A347F2   |   "Acme Corp." → hash 9B21D8  (totalmente distintos)
LSH:                 "Acme Corp" → bucket 17     |   "Acme Corp." → bucket 17   (mismo bucket, alta probabilidad)
```

Mecánicamente (versión simplificada): se generan varias "firmas" del texto (ej. usando n-gramas o funciones hash aleatorias específicas), y si suficientes de esas firmas coinciden entre dos registros, caen en el mismo bucket. Así, en vez de comparar contra todo el dataset, solo comparas contra los registros que cayeron en tu mismo bucket LSH — igual que el blocking por clave exacta, pero la "clave" es una firma diseñada matemáticamente para tolerar variación de texto, no un campo literal como país o código postal.

**d) Embeddings + ANN search — el estándar moderno**

Esta es la técnica que se conecta directamente con la sección 4 (embeddings). En vez de una clave o una firma hash, cada registro se convierte en un **vector numérico** (embedding) que representa su significado. Registros parecidos quedan **geométricamente cerca** en ese espacio vectorial.

El problema: encontrar los vecinos *exactos* más cercanos a un vector, entre 100 millones de vectores, sigue siendo lento (fuerza bruta otra vez, aunque en espacio vectorial en vez de texto). Aquí es donde entra **ANN**.

> **ANN — Approximate Nearest Neighbor.** En vez de garantizar que encuentras los k vecinos *exactamente* más cercanos, ANN usa una estructura de índice que encuentra vecinos **casi siempre correctos** (ej. 95-99% de las veces el vecino real top-1 está en tu resultado), a cambio de ser órdenes de magnitud más rápido que la búsqueda exacta. Es una decisión consciente de sacrificar un poco de precisión por velocidad — totalmente razonable a esta escala, porque de todas formas la comparación fina de la Etapa 2 va a filtrar los falsos positivos que se cuelen.
>
> Dos implementaciones que vale la pena poder nombrar:
> - **HNSW (Hierarchical Navigable Small World)** — construye un grafo en capas donde cada nodo (vector) está conectado a sus vecinos aproximados; buscar es "navegar" el grafo desde arriba (capas dispersas, saltos grandes) hacia abajo (capas densas, saltos finos), como buscar una palabra en un diccionario usando pestañas en vez de leer página por página.
> - **FAISS** (de Meta) — una librería que implementa varios algoritmos de ANN, incluyendo variantes de HNSW e IVF (índices que dividen el espacio vectorial en "celdas" y solo buscan dentro de las celdas más prometedoras). Es lo que probablemente usarías en la práctica, no reimplementarías el algoritmo tú mismo.

```text
Embeddings + ANN, ejemplo concreto:

"Acme Corp, acme.com, USA"           → vector [0.12, -0.44, 0.81, ...]
"ACME Corporation Inc, acme.com"     → vector [0.13, -0.42, 0.79, ...]  ← muy cerca del anterior
"Totally Different LLC, xyz.com"     → vector [-0.9, 0.3, -0.1, ...]    ← lejos

ANN search("Acme Corp, acme.com, USA", top_k=20)
   → devuelve los 20 vectores más cercanos, incluyendo el de "ACME Corporation Inc"
   → NO devuelve "Totally Different LLC" porque está lejos en el espacio vectorial
```

### 3.4 Bi-encoder vs. Cross-encoder — la distinción más importante de esta sección

Esta distinción es la razón técnica de por qué el pipeline tiene DOS etapas y no una sola. Explícala siempre con el ejemplo de abajo, no solo con la definición.

**Bi-encoder** ("bi" = dos, cada texto pasa por el encoder **por separado**):

```text
Registro A ("Acme Corp")           → [modelo de embeddings] → vector_A
Registro B ("ACME Corporation")     → [modelo de embeddings] → vector_B   (calculado de forma INDEPENDIENTE)

similaridad(A, B) = cosine_similarity(vector_A, vector_B)
```

La clave: como cada vector se calcula de forma independiente, **puedes calcular el vector de cada uno de los 100 millones de registros UNA SOLA VEZ, guardarlos en un índice (ANN), y reusarlos para comparar contra cualquier query nueva.** Esto es lo que lo hace escalable — el costo de "embeber" ya está pagado de antemano (offline), y la búsqueda en el índice es rápida.

**Cross-encoder** ("cross" = el par se cruza, se procesa **junto**, no por separado):

```text
[Registro A + Registro B] → [modelo, ve AMBOS textos a la vez] → score de similaridad directo (ej. 0.94)
```

El modelo puede prestar atención a la relación específica entre A y B (ej. "el nombre difiere pero el dominio es idéntico, eso pesa mucho") de una forma que un bi-encoder no puede, porque el bi-encoder nunca "ve" ambos textos al mismo tiempo — solo compara vectores ya calculados por separado. Por eso el cross-encoder es **más preciso**.

**El costo:** como el score depende del PAR específico, no puedes pre-calcularlo de antemano ni guardarlo en un índice reusable — tienes que correr el modelo de nuevo para cada par que quieras evaluar. Si intentaras usar un cross-encoder para los 5×10^15 pares posibles, sería aún más lento que la fuerza bruta original, porque el modelo es más pesado que un simple cálculo de distancia.

```text
                  Bi-encoder              Cross-encoder
Se calcula por    cada registro           cada PAR
Se puede indexar  SÍ (ANN)                NO
Velocidad         Rápido (miles/seg)      Lento (requiere correr el modelo por par)
Precisión         Buena, no perfecta      Alta — ve la relación específica
Uso en el pipeline Etapa 1 (candidatos)   Etapa 2 (los pocos que sobrevivieron)
```

**Por qué las dos etapas juntas resuelven el problema completo:**

```text
100,000,000 registros
        ↓ (bi-encoder, calculado una vez, offline)
Índice ANN con 100M vectores
        ↓ (ANN search por cada query, muy rápido)
~20-50 candidatos por registro   ← de 100M bajaste a docenas
        ↓ (cross-encoder o LLM, ahora sí es viable computacionalmente)
Score preciso de match/non-match solo sobre esos ~20-50
```

El bi-encoder resuelve el problema de **escala** (recall alto, rápido, barato). El cross-encoder resuelve el problema de **precisión** (exacto, pero solo viable en un conjunto ya pequeño). Ninguno de los dos por sí solo resuelve el problema completo — por eso se usan en conjunto, en ese orden.

Esto conecta directamente los tres temas "Critical" del study guide (embeddings, LLM cost-aware, experimental design) en una sola arquitectura coherente: el LLM (sección 5) normalmente jugaría el rol del "modelo caro" en la Etapa 2, nunca de la Etapa 1.

---

## 4. Embeddings y similaridad semántica

**Qué es un embedding**: una representación numérica (vector) de un texto/registro tal que registros semánticamente similares quedan **cerca** en el espacio vectorial, medido típicamente con **cosine similarity**.

**Cómo se aplica a matching de empresas:**
- Concatenar campos relevantes (nombre, dirección, dominio) en un texto único y embeberlo, o
- Embeber campos por separado y combinar los scores (ej. similaridad de nombre + similaridad de dirección con pesos distintos)

**Cómo validar que las similarity scores son realmente significativas** (esto es lo que el study guide marca como "strong senior-level evidence"):
- No basta con "compute embeddings and compare" — hay que verificar que un score alto de verdad corresponde a un match real, con un **conjunto etiquetado** (labeled set) de pares conocidos match/non-match.
- Mirar la **distribución** de scores para matches conocidos vs. non-matches conocidos — ¿hay separación clara, o se solapan mucho? Si se solapan, un solo umbral (threshold) no va a funcionar bien y hace falta un clasificador más sofisticado sobre el score.

**String similarity clásica (complementaria a embeddings, útil para nombres):**
- **Jaro-Winkler** / **Levenshtein distance** — miden similitud carácter por carácter, buenas para typos y variaciones cortas de nombres, pero no capturan sinónimos/alias (ej. "IBM" vs "International Business Machines" tienen distancia de edición enorme pero son la misma empresa — ahí embeddings semánticos ganan).

---

## 5. LLM vs. baseline más barato

Este es el tema #1 marcado como "Critical". El error que el study guide explícitamente advierte no cometer: **"defaulting to 'use an LLM' without justification."**

**Framework de decisión (adapta esto igual que ya tienes en tu propio cheat sheet de RAG vs. fine-tuning):**

```text
¿El baseline más barato (embeddings + threshold, reglas) ya funciona razonablemente bien?
        ↓ NO
¿El LLM mejora la calidad lo suficiente para justificar su costo/latencia?
        ↓
Diseña una comparación JUSTA:
   - Mismo conjunto de test para ambos enfoques
   - Mide más que accuracy: costo por comparación, latencia, throughput
   - ¿Cuánto mejor tiene que ser el LLM para justificar Nx el costo?
```

**Tres roles legítimos para un LLM en este problema (no son excluyentes):**
1. **Técnica de matching directa** — el LLM decide match/non-match para un par (caro, solo viable en candidatos ya filtrados).
2. **Quality ceiling / techo de calidad** — usar el LLM como "el mejor resultado posible" contra el cual medir qué tan cerca llega un enfoque más barato.
3. **Paso de revisión asistida** — el LLM revisa casos ambiguos (possible matches) donde el modelo barato no está seguro, no todos los pares.

**Costo en escala real:** a cientos de millones de entidades, incluso después de blocking puedes tener millones de pares candidatos — correr un LLM sobre TODOS esos pares puede ser prohibitivo. Esto es exactamente el "fixed inference budget" del Escenario 6.

> **Interview line:** "Trato el LLM como una herramienta más, no como el default — lo evalúo contra un baseline más barato en el mismo test set, midiendo no solo accuracy sino costo y latencia por comparación. Muchas veces el rol correcto del LLM no es hacer todo el matching, sino revisar solo los casos ambiguos que el modelo barato no puede resolver con confianza."

---

## 6. Diseño experimental y evaluación

Este es el tema que más "follow-up" va a recibir — "cómo mides que realmente mejoró" es la pregunta central de todo el guide.

**Componentes de un framework de evaluación defendible:**

```text
Baseline        → el motor de matching que YA está en producción
Métricas        → no solo accuracy — ver tabla abajo
Test/benchmark set → un conjunto fijo, representativo, con labels confiables
Error analysis   → mirar los casos donde falló, no solo el número agregado
```

**Métricas específicas de matching de pares (más allá de accuracy genérico):**

| Métrica | Qué mide | Por qué importa aquí |
|---|---|---|
| **Precision (a nivel de pares)** | De los pares que marqué como match, ¿cuántos son match real? | Falsos positivos = fusionar empresas distintas por error |
| **Recall (a nivel de pares)** | De los matches reales que existen, ¿cuántos encontré? | Falsos negativos = duplicados que nunca se detectan |
| **Pairs completeness** | Después del blocking, ¿qué % de los matches reales sobrevivieron a esa etapa? | Mide si tu candidate generation está perdiendo matches antes de llegar a la comparación fina |
| **Reduction ratio** | Cuánto redujiste el espacio de comparación respecto al pairwise completo | Mide qué tan eficiente es tu blocking, no solo qué tan preciso |

> Precision y recall aquí se calculan sobre **pares de registros**, no sobre registros individuales — un error común es olvidar esta distinción al hablar de métricas en entity resolution.

**Error analysis real** (lo que el guide pide explícitamente, no solo "until accuracy"):
- Agrupar los errores por **tipo de fallo** — ¿son alias no reconocidos? ¿nombres multilingües? ¿jerarquías padre-subsidiaria confundidas con duplicados?
- Esto es lo que te permite decir "aprendí que el modelo falla específicamente en X" en vez de "el accuracy fue 87%".

---

## 7. Clasificación, NLP y mantenimiento en producción

Aunque tú no productivizas, sí se espera que entiendas el ciclo de vida completo — el guide es explícito: **"not just notebook experimentation."**

**Qué dispara un retrain:**
```text
Data drift          → la distribución de los datos de entrada cambió
Concept drift        → la relación entre input y la etiqueta correcta cambió
Nuevas categorías     → aparecen tipos de entidades no vistas en entrenamiento
Performance decay     → las métricas en producción se degradan con el tiempo
```

**Cómo diagnosticar cuál de estos es (Escenario 5):**
- Revisar si la **distribución de features de entrada** cambió (drift de datos) vs. si el modelo sigue prediciendo igual pero el mundo cambió (concept drift) vs. si el problema es de **etiquetas** (labeling issue — quizás los labels nuevos son inconsistentes con los viejos).
- Retraining seguro sin romper consumidores downstream: versionado del modelo, comparación shadow (correr el nuevo modelo en paralelo sin reemplazar el viejo todavía), backward compatibility del formato de output.

---

## 8. Diseño consciente del costo y la escala

El guide pide explícitamente razonar sobre esto **desde el inicio del proyecto**, no como algo que se ajusta después.

**Con un presupuesto de inferencia fijo, ¿qué se sacrifica primero?** (Escenario 6)

```text
Opciones de trade-off, en orden típico de "qué tocar primero":
1. Tamaño del candidate set (k en top-k)     → más barato de reducir, impacto directo en costo
2. Complejidad del modelo de reranking        → cross-encoder pequeño vs. LLM grande
3. Frecuencia de reprocesamiento completo      → ¿todo el grafo cada vez, o incremental?
4. Cobertura (qué % de pares se revisan con el método más caro)
```

Razonamiento cuantitativo esperado: *"si tengo X pares candidatos después de blocking y un presupuesto de $Y, ¿cuánto puedo gastar por par? Eso determina directamente qué técnicas son viables."* — no "esto debería funcionar", sino un número.

---

## 9. Comunicar trade-offs y resultados negativos

Esto es evaluado tan fuerte como la parte técnica — literalmente aparece dos veces en el guide como señal de "intellectual honesty".

**Regla central:** un resultado negativo (tu hipótesis no se confirmó) es un **resultado legítimo y útil**, no un fracaso a esconder.

```text
Estructura para reportar un resultado negativo:
Hipótesis → qué esperabas
Experimento → qué hiciste para probarla
Resultado → no confirmó la hipótesis (sé específico, no evasivo)
Por qué (si lo sabes) → qué reveló el error analysis
Qué sigue → siguiente experimento, o decisión de abandonar esa línea
```

**Frase mala:** "el enfoque no funcionó como esperaba, pero aprendimos mucho" (vago, suena a estar minimizando).
**Frase fuerte:** "la hipótesis era que embeddings de nombre + dominio bastarían; el error analysis mostró que fallaba específicamente en subsidiarias con nombres muy distintos al padre — así que la conclusión fue que se necesita una señal jerárquica adicional, no solo similaridad textual."

---

## 10. Cómo posicionar tus 3-4 historias

El guide pide distinguir explícitamente 4 niveles de ownership — el entrevistador **escucha activamente** por esta distinción, así que sé preciso con el lenguaje que usas:

| Nivel | Qué significa | Frase típica |
|---|---|---|
| **Participating** | Contribuiste a un esfuerzo más amplio, sin un experimento propio | "Formé parte del equipo que..." |
| **Implementing** | Ejecutaste un método que alguien más diseñó | "Implementé el enfoque que habíamos definido..." |
| **Independently designing** | Tú definiste la hipótesis, el baseline y la evaluación | "Diseñé el experimento completo, desde la hipótesis hasta..." |
| **Owning production maintenance** | Reentrenaste/monitoreaste/evolucionaste un modelo vivo en el tiempo | "Fui responsable de mantener el modelo en producción durante..." |

**Estructura de cada historia (úsala literalmente, calca el orden):**
```text
Context → Problem → Your responsibility → Hypothesis/approach → Experiment → Result → Measurable impact → Lessons learned
```

**Las 5-6 historias que idealmente cubres** (mapea tus proyectos reales — xTrap, xAgent, UF-CIVI — a estos huecos):
- Un enfoque de ML que construiste y evaluaste end-to-end
- Un modelo de clasificación en producción que reentrenaste/mantuviste (no solo notebook)
- Un problema de datos sucios/multilingües que resolviste
- Un trade-off de costo/escala que navegaste deliberadamente
- Un experimento que **refutó** tu hipótesis, y cómo lo reportaste
- Una recomendación que defendiste ante un stakeholder escéptico

**Si no puedes cuantificar el impacto con un número real, describe el resultado observable — no inventes una métrica que no puedas defender.** (Esto está escrito literalmente en el guide — tómalo en serio.)

---

## 11. Los 7 escenarios — cómo pensarlos

No son para memorizar respuestas — son para practicar el razonamiento. Aquí el ángulo clave de cada uno:

1. **Matching a escala masiva** → candidate generation primero (blocking/embeddings+ANN), la escala es una restricción de diseño desde el día 1, no un ajuste posterior.
2. **Datos sucios/multilingües** → dónde usar normalización basada en reglas (sufijos legales, formato de dirección) vs. dónde embeddings semánticos manejan mejor la variación (alias, traducciones).
3. **LLM vs. baseline barato** → comparación justa, medir más que accuracy, presentar el trade-off sin hype.
4. **Hipótesis refutada** → reportar con la misma claridad que un resultado positivo, explicar qué sigue.
5. **Reentrenar un clasificador en producción** → diagnosticar drift vs. labeling issue primero, luego retraining seguro sin romper consumidores.
6. **Presupuesto de inferencia fijo** → razonamiento cuantitativo de qué se sacrifica primero (ver sección 8).
7. **Explicar a stakeholders escépticos** → traducir trade-offs técnicos a términos que ellos puedan evaluar, sostener tu posición sin ponerte a la defensiva.

---

## 12. Frameworks y herramientas del mundo real

Nombrar la herramienta correcta con criterio (no solo el nombre) es una señal senior fuerte — y saber su costo real es parte de ese criterio, porque en este rol el costo es explícitamente parte del diseño (sección 5 y 8). "Gratis" aquí siempre significa *sin licencia que pagar*, no *sin costo de cómputo/infraestructura* — correr algo tú mismo en un servidor grande también cuesta, solo que es costo de infraestructura en vez de licencia.

### 12.1 Librerías dedicadas a Entity Resolution

| Herramienta | Costo | Ventajas | Desventajas |
|---|---|---|---|
| **Splink** (UK Ministry of Justice) | **Gratis**, open-source (MIT). Solo pagas el cómputo donde corre (Spark/DuckDB/Athena) | Diseñado exactamente para este problema (millones de registros, múltiples fuentes); modelo probabilístico **explicable** — puedes justificar cada score, no es caja negra; escala bien vía Spark/DuckDB; documentación fuerte y desarrollo activo | Curva de aprendizaje para configurar el modelo tipo Fellegi-Sunter; menos "plug-and-play" que un enfoque puramente ML; el soporte nativo de embeddings/ML es más nuevo que su parte probabilística clásica |
| **Zingg** | **Gratis** en su edición community (Apache 2.0); existe **Zingg Enterprise** de paga con soporte y features adicionales | Active learning reduce mucho el esfuerzo de etiquetado; pensado para datos sucios desde el diseño; escala en Spark | Requiere cluster Spark para sacarle provecho real (más pesado de levantar); comunidad más pequeña que Splink |
| **dedupe** (Python, DataMade) | **Gratis**, open-source (MIT) | Muy simple de prototipar; buena experiencia de active learning; rápido para validar una idea | **No está pensado para 100M+ registros** — corre en una sola máquina, no distribuido; te quedarías corto para la escala real de este proyecto |
| **recordlinkage** (Python) | **Gratis**, open-source (BSD) | Modular — ves y controlas cada pieza (blocking, comparación, clasificación) por separado, bueno para entender/enseñar el pipeline | No optimizado para escala masiva; más trabajo manual que Splink; desarrollo menos activo |

> **Active learning** — en vez de etiquetar miles de pares al azar, el sistema te muestra primero los pares donde el modelo está **más inseguro** (score ambiguo, ni claramente match ni claramente no-match). Etiquetar esos casos "difíciles" mejora el modelo mucho más rápido que etiquetar casos obvios donde el modelo ya acertaría igual. Relevante porque construir el benchmark set etiquetado es explícitamente parte del trabajo de este rol.

### 12.2 Motores de búsqueda vectorial / ANN (Etapa 1 del pipeline, sección 3.4)

| Herramienta | Costo | Ventajas | Desventajas |
|---|---|---|---|
| **FAISS** (Meta) | **Gratis**, open-source (MIT). Es una librería, no un servidor — corre dentro de tu propio proceso | Extremadamente rápido; muy probado en producción e investigación; varios tipos de índice (flat exacto, IVF, HNSW, compresión PQ) para distintos trade-offs | No es una base de datos — sin persistencia/replicación/filtrado de metadata robusto de fábrica; tú construyes esa capa encima si la necesitas |
| **pgvector** | **Gratis**, extensión open-source de Postgres | Reusas infraestructura que ya conoces (Postgres, como en xAgent); consistencia transaccional; fácil de operar si ya tienes Postgres | Rendimiento ANN a escala muy grande (100M+) no tan optimizado como FAISS/Milvus especializados; construir el índice puede ser lento a esa escala |
| **Pinecone** | **De pago**, SaaS gestionado, precio por uso (existe tier gratuito limitado) | Cero ops — totalmente gestionado, escala sin que tú administres servidores | Costo puede crecer mucho a esta escala; **tus datos salen de tu infraestructura hacia un tercero** — relevante tratándose de datos de cliente (Bain); vendor lock-in |
| **Weaviate** | **Gratis** self-hosted (open-source, BSD); o **de pago** en su nube gestionada | Búsqueda híbrida (vector + keyword) integrada; opción open-source evita lock-in total | Self-hosting requiere esfuerzo de operación; la nube gestionada sí cuesta |
| **Milvus** | **Gratis** self-hosted (Apache 2.0); **Zilliz Cloud** (su nube gestionada) es de pago | Diseñado para escala de billones de vectores; maduro | Operar tu propio cluster es pesado (requiere componentes adicionales tipo etcd/MinIO); curva de aprendizaje mayor |
| **Qdrant** | **Gratis** self-hosted (Apache 2.0); **Qdrant Cloud** de pago | API simple, buen rendimiento, filtrado por metadata sólido | Ecosistema/comunidad más pequeño que FAISS/Milvus, proyecto más joven |
| **Annoy** (Spotify) | **Gratis**, open-source (Apache 2.0) | Simple, memory-mapped (eficiente en RAM), bueno para datasets estáticos de solo lectura | El índice es **inmutable** una vez construido — agregar puntos nuevos requiere reconstruir todo; ya no tiene desarrollo activo |
| **ScaNN** (Google) | **Gratis**, open-source (Apache 2.0) | Muy buen balance velocidad/precisión, viene de investigación de Google | Comunidad más chica, menos "plug-and-play" que FAISS |

**Criterio de cuál elegir:** para *investigación/experimentación* (el foco explícito de este rol), FAISS local es lo más simple y barato de iterar — no necesitas pagar por una vector DB gestionada solo para validar una hipótesis. Una vector DB dedicada (Pinecone/Milvus/Qdrant) tiene más sentido del lado de productionización, que aquí es responsabilidad del equipo de engineering del cliente, no tuya.

### 12.3 Modelos de embeddings y comparación

| Herramienta | Costo | Ventajas | Desventajas |
|---|---|---|---|
| **Sentence-Transformers / SBERT** | **Gratis** (modelos open-weight) — el costo real es el cómputo para correrlos tú mismo (CPU/GPU) | Sin costo recurrente por llamada; **control total y privacidad de los datos** (no salen a un tercero — relevante con datos de cliente); muchos modelos pre-entrenados disponibles | Necesitas hostear/servir el modelo tú mismo; para buen throughput a escala conviene GPU, lo cual es una inversión de infraestructura |
| **Cross-encoders de Hugging Face** | **Gratis** (open-weight), mismo modelo de costo que arriba | Listos para usar en la Etapa 2 (reranking); mismo beneficio de privacidad/control | Más pesados computacionalmente que un bi-encoder — por diseño, ya que procesan el par completo (sección 3.4) |
| **APIs de embeddings** (OpenAI, Cohere) | **De pago**, por uso (típicamente por token) | Cero infraestructura que mantener; arrancar es inmediato; calidad competitiva | Costo recurrente que escala con volumen — a 100M+ registros puede ser significativo; **tus datos (de cliente) salen hacia un tercero**, un punto que vale la pena mencionar activamente dado que el proyecto maneja datos firmográficos de empresas; latencia de red y rate limits a considerar |

### 12.4 Búsqueda léxica / fuzzy (complementaria a embeddings, no reemplazo)

| Herramienta | Costo | Ventajas | Desventajas |
|---|---|---|---|
| **OpenSearch** (fork open-source de Elasticsearch, mantenido por AWS) | **Gratis** self-hosted (Apache 2.0); AWS managed OpenSearch es de pago | Verdaderamente open-source sin ambigüedad de licencia; búsqueda léxica (BM25) madura + soporte de búsqueda vectorial híbrida | Operar/tunear un cluster tiene curva de aprendizaje y costo operativo |
| **Elasticsearch** | **Gratis** con funcionalidad limitada (licencia Elastic, no OSI-open desde v7.11+); **Elastic Cloud** de pago para funcionalidad completa gestionada | Estándar de la industria, muy documentado, búsqueda híbrida moderna | La licencia no es open-source puro (vale la pena saber esto si preguntan) — por eso muchos proyectos usan OpenSearch en su lugar |
| **rapidfuzz** (Python) | **Gratis**, open-source (MIT), sin servidor — es una librería local | Muy rápido (implementado en C++ por debajo); cero infraestructura; simple de integrar como feature adicional | Solo similaridad de string — no entiende sinónimos/semántica; no resuelve por sí solo el problema de escala (necesita combinarse con blocking) |

---

## 13. Algoritmos útiles, explicados

### 13.1 MinHash — la versión concreta de LSH para texto (sección 3.3c)

Antes en la sección de LSH quedó a nivel de intuición ("firmas que coinciden con alta probabilidad") — MinHash es el algoritmo concreto más usado para lograr eso con texto.

**Paso 1 — convertir texto en un conjunto de "shingles" (n-gramas):**
```text
"Acme Corp" → shingles de 3 caracteres:
  {"Acm", "cme", "me ", "e C", " Co", "Cor", "orp"}
```

**Paso 2 — Jaccard similarity entre dos conjuntos** (la métrica que MinHash aproxima):
```text
Jaccard(A, B) = |intersección(A, B)| / |unión(A, B)|
```
Si "Acme Corp" y "Acme Corporation" comparten muchos shingles de 3 caracteres, su Jaccard similarity es alta, aunque los strings completos no sean idénticos.

**Paso 3 — MinHash aproxima Jaccard sin comparar los conjuntos completos:** aplicas varias funciones hash distintas a cada shingle, te quedas con el **valor mínimo** de cada función por conjunto — eso da una "firma" corta (ej. 100 números) por registro. Dos registros con conjuntos de shingles parecidos tendrán, con alta probabilidad, el mismo valor mínimo en varias de esas funciones. Cuantas más funciones coincidan, más alta la similaridad estimada — **sin tener que comparar los shingles completos uno por uno**, lo cual es mucho más rápido a escala.

### 13.2 SimHash — la variante para vectores de alta dimensión

Similar en espíritu a MinHash pero pensado para aproximar **cosine similarity** en vez de Jaccard — relevante porque los embeddings (sección 4) viven en ese tipo de espacio. Genera un hash donde vectores con ángulo pequeño entre ellos (alta similaridad coseno) tienden a producir el mismo hash. Es una de las técnicas detrás de algunas implementaciones de LSH para embeddings.

### 13.3 Union-Find / Connected Components — el paso que casi nadie menciona pero es crítico

Hasta ahora todo el pipeline decide **pares**: ¿A y B son match? Pero el objetivo final no son pares sueltos — es agrupar todos los registros que representan la **misma entidad** en un solo golden record. Ahí aparece un problema sutil:

```text
Match(A, B) = SÍ
Match(B, C) = SÍ
Match(A, C) = NO   ← ¿esto puede pasar? SÍ, con clasificadores imperfectos
```

Si tratas esto ingenuamente, tienes una inconsistencia: ¿A, B, C son la misma entidad o no? La solución estándar es tratar los matches como **aristas de un grafo** y encontrar sus **componentes conectados**: si A-B están conectados y B-C están conectados, A, B, C terminan en el mismo grupo aunque A-C individualmente no se haya marcado como match directo (transitividad).

```text
Grafo de matches:
   A --- B --- C

Componente conectado: {A, B, C}  → un solo golden record
```

**Union-Find** (también llamado *Disjoint Set Union*) es la estructura de datos clásica y eficiente para calcular esto a gran escala: cada registro empieza en su propio grupo, y cada match confirmado "une" dos grupos. Es casi O(n) en la práctica (con las optimizaciones estándar de path compression y union by rank), muy barato comparado con el resto del pipeline.

**El gotcha que vale la pena mencionar en la entrevista:** esta transitividad puede generar **cadenas de match incorrectas** — si B es un match débil/ambiguo tanto de A como de C, pero A y C en realidad son entidades distintas, terminas fusionando cosas que no debían fusionarse ("match drift"). Por eso el threshold de similaridad y la calidad del reranking (Etapa 2) importan más de lo que parece — un error individual de un par puede contaminar todo un cluster.

### 13.4 Fellegi-Sunter — el modelo estadístico clásico detrás del record linkage

Vale la pena poder nombrarlo porque es *el* framework probabilístico histórico del campo (1969, todavía es la base conceptual de herramientas como Splink). La idea:

```text
Para cada campo comparado (nombre, dirección, dominio...):
  m-probability = P(campos coinciden | SON la misma entidad)
  u-probability = P(campos coinciden | NO son la misma entidad, por azar)

  peso del campo = log( m-probability / u-probability )
```

Cada campo que coincide suma su peso a un score total; campos que además son "raros" (poco probable que coincidan por azar — ej. un dominio web idéntico) pesan mucho más que campos comunes (ej. mismo país, que coincide por azar todo el tiempo). Es, conceptualmente, el ancestro estadístico de lo que hoy hacen los modelos de ML/embeddings de forma más automática — mencionarlo demuestra que entiendes el problema más allá de "usar el modelo de moda".

---

## 14. Buenas prácticas

### Construcción del benchmark/golden set
- Que incluya casos **fáciles y difíciles** a propósito (no solo pares obvios) — si tu test set es 95% casos obvios, cualquier modelo mediocre saca buen score y no aprendes nada.
- Sampling **estratificado**: asegúrate de tener suficientes ejemplos de cada tipo de dificultad (multilingüe, alias, subsidiarias) en vez de una muestra puramente aleatoria que podría no capturar los casos raros pero importantes.
- Revisión humana con **doble anotación** en al menos una muestra — mide qué tan de acuerdo están dos anotadores humanos entre sí (inter-annotator agreement); si los humanos no concuerdan, tu "ground truth" tiene un techo de calidad que ningún modelo puede superar.

### Reglas de canonicalización (para construir el golden record final)
Cuando ya sabes que A, B, C son la misma entidad, ¿qué valores usas para el registro final fusionado? Define reglas explícitas, no ad-hoc:
```text
Campo más completo gana   (ej. dirección con más detalle sobre una más corta)
Fuente más confiable gana  (si sabes que una fuente es más autoritativa)
Más reciente gana          (para campos que cambian con el tiempo, ej. tamaño de empresa)
```

### Versionado de embeddings (gotcha operacional real)
Si cambias el modelo de embeddings, **los vectores viejos y nuevos no son comparables entre sí** — no puedes mezclar embeddings de dos modelos distintos en el mismo índice ANN. Cambiar de modelo implica reindexar TODO el corpus desde cero, lo cual a 100M de registros no es trivial ni barato. Por eso decidir el modelo de embeddings no es un detalle menor — es una decisión con costo de cambio alto.

### Shadow testing antes de reemplazar el baseline
No reemplazas el motor de matching en producción de un día para otro. Corres el nuevo enfoque **en paralelo** (shadow) sobre tráfico/datos reales sin que sus resultados se usen todavía, comparas contra el baseline en producción, y solo migras cuando tienes suficiente evidencia.

### Ahorro de costo práctico
- **Cachea embeddings** — no reembebas un registro que no ha cambiado.
- **Batchea llamadas** a APIs de embeddings/LLM en vez de una request por registro — reduce overhead de red y suele ser más barato por unidad.
- **Registra metadata suficiente para hacer error analysis después** (en qué bucket de blocking cayó, qué score de cada etapa recibió) — si no la guardas al momento, no la puedes reconstruir después.

---

## 15. ¿Knowledge Graphs ayudan aquí?

Sí — pero como **complemento** al pipeline de matching, no como reemplazo. Conecta directo con 13.3 (Union-Find) y con "inconsistent hierarchies", que el project guide nombra explícitamente como parte del problema.

**Dónde sí ayuda:**

1. **Jerarquías de empresa son datos de grafo, no tabulares.** "¿Es subsidiaria, marca, o entidad separada?" no se responde comparando texto — se responde con relaciones explícitas: `Empresa A --es_subsidiaria_de--> Empresa B`. Un KG modela esto de forma nativa.

2. **Previene el "match drift" de Union-Find.** Si A y B se parecen textualmente pero el grafo muestra que son subsidiarias *distintas* del mismo padre, esa relación evita fusionarlas incorrectamente — el contexto que el texto solo no puede dar.

3. **Como señal adicional de matching**, no como base de datos final. **Graph embeddings** (ej. Node2Vec) representan una entidad por su posición en la red de relaciones (directores compartidos, domicilio fiscal compartido, dominio compartido) — útil cuando el texto es débil pero la señal relacional es fuerte. Mismo principio que GraphRAG: vectores encuentran "texto parecido", grafos siguen "relaciones explícitas".

**Dónde NO es la herramienta correcta:** construir un KG completo desde cero para 100M+ entidades es infraestructura adicional no trivial — y la entity resolution es **prerequisito** de un KG limpio (necesitas resolver qué nodos son la misma entidad antes de construir el grafo bien), no al revés. Proponerlo como primera respuesta sin justificar por qué embeddings/reglas no bastan repite el mismo error que "usar LLM por default" (sección 5) — herramienta de moda sin comparación justificada.

> **Interview line:** "Un knowledge graph no reemplaza el pipeline de matching — lo complementa. Lo usaría como señal adicional cuando el texto es ambiguo, especialmente para jerarquías padre-subsidiaria, y para prevenir errores de transitividad al agrupar matches en clusters. No lo propondría como primer paso sin evidencia de que la señal relacional mueve la aguja sobre el baseline de embeddings."

---

[[02 - Quick Reference|→ Ir a la referencia rápida]]
