# Technical Interview — Problem Solving Cheat Sheet

> [!abstract] Objetivo
> La entrevista busca evaluar principalmente **cómo piensas, cómo resuelves problemas y cómo tomas decisiones técnicas**.
>
> No se trata solamente de saber tecnologías. Lo importante es poder explicar:
>
> **Problema → Qué hice → Por qué → Resultado → Qué aprendí**

---

## 0. Metodología según el tipo de pregunta

> [!important]
> No todas las preguntas se responden con la misma estructura. Antes de contestar, identifica primero **qué tipo de pregunta es** — eso decide qué framework usar.

### A. Preguntas técnicas (algoritmos, sistemas, arquitectura, debugging)

Preguntas tipo "¿cómo diseñarías...?", "¿por qué fallaría...?", "¿cómo optimizarías...?".

```text
1. ¿Cuál es el problema exacto?
2. ¿Cuáles son las restricciones?
3. ¿A qué escala estamos hablando?
4. ¿Cuáles son las soluciones posibles?
5. ¿Cuáles son los trade-offs?
6. ¿Qué solución elegiría?
7. ¿Cómo mediría el éxito?
```

**Reglas de oro para este tipo:**
- Nombra el **mecanismo técnico concreto** (comando, estructura de datos, herramienta), nunca una palabra vaga ("seguro", "eficiente", "estructurado").
- Distingue qué **controlas y puedes escalar** vs. qué es un **límite externo fijo** (rate limit de una API, timeout de un gateway).
- Si te piden una estructura explícita (ej. "camina conmigo por el incidente"), **sigue las etapas literalmente**, no las mezcles en un párrafo.
- No inventes una tecnología que no aplica solo para sonar completo — resta más que suma.

→ Detalle completo en [[#3. Algorithms & Data Structures]] a [[#14. Speed vs Quality]].

---

### B. Preguntas de proyectos ("cuéntame de un proyecto en el que trabajaste")

```text
Problema
   ↓
Qué hice YO (no "el equipo", no "nosotros" — tu rol específico)
   ↓
Por qué (qué alternativas consideré)
   ↓
Resultado (medible si es posible)
   ↓
Qué aprendería / haría diferente hoy
```

**Reglas de oro para este tipo:**
- Empieza con la **versión de 30 segundos** (impacto + tu rol), deja que el entrevistador pida profundidad — no listes cada detalle desde el inicio.
- Usa tus proyectos reales documentados en [[Projects|Projects]] (xTrap, xAgent, UF-CIVI, FarmView, Plant Identification) — cada uno ya tiene su versión corta lista.
- Si te preguntan por algo que no hiciste tú directamente, sé honesto sobre el alcance real de tu contribución.

---

### C. Preguntas de cultura / comportamiento (equipo, conflictos, motivación, valores)

Preguntas tipo "cuéntame de un conflicto con un compañero", "cómo manejas el estrés/deadlines", "por qué quieres este rol", "cuál es tu mayor debilidad".

```text
Situación
   ↓
Tu rol/tarea específica
   ↓
Acción — enfocada en CÓMO te comunicaste/colaboraste, no solo en la solución técnica
   ↓
Resultado — incluye la relación/aprendizaje, no solo la métrica
```

**Diferencia clave con las preguntas técnicas:** aquí el foco no es la mejor solución de ingeniería, es **cómo trabajas con otras personas** — cómo escuchas, cómo manejas presión, cómo reaccionas cuando te equivocas. Ser honesto sobre un error propio suele valer más que aparentar que todo salió perfecto.

**Preguntas híbridas:** algunas mezclan ambos mundos (ej. "cuéntame de un desacuerdo técnico con un compañero" — ver [[#13. Comunicación técnica]]). Ahí usa primero C (entender al otro, escuchar) y después A (criterios objetivos, trade-offs) para decidir.

---

## Índice

### Marco general
- [[#0. Metodología según el tipo de pregunta]]
- [[#1. Estructura para responder cualquier pregunta]]
- [[#2. Las 5 historias que debes preparar]]
- [[#15. Cuando no sabes la respuesta]]
- [[#16. Senior Engineering Mindset]]
- [[#17. Palabras clave que debes utilizar]]
- [[#18. Trade-offs que debes conocer]]
- [[#21. La regla de oro]]
- [[#23. Mentalidad durante la entrevista]]

### Por tema técnico (orden de la lista de la reclutadora)
- [[#3. Algorithms & Data Structures]]
- [[#4. Backend & API Design]]
- [[#5. Frontend & Performance]] — ver también [[12 - Frontend Performance Debugging]]
- [[#6. Databases & Query Optimization]] (índices, EXPLAIN ANALYZE, VACUUM, partitioning, caching...)
- [[#7. Testing]]
- [[#8. AI / ML Applications]]
- [[#9. Architecture & Scalability]]
- [[#10. Docker / Infrastructure / CI-CD]]
- [[#11. Security]]
- [[#12. Monitoring & Production Incidents]]
- [[#13. Comunicación técnica]]
- [[#14. Speed vs Quality]]

### Antes de la entrevista
- [[#19. Tus 5 historias maestras]]
- [[#20. Preguntas que debes practicar]]
- [[#22. Checklist antes de la entrevista]]

---

## 1. Estructura para responder cualquier pregunta

Utiliza esta estructura:

```text
SITUATION
   ↓
¿Cuál era el problema?
   ↓
ACTION
   ↓
¿Qué hice yo?
   ↓
DECISION
   ↓
¿Qué alternativas consideré?
   ↓
WHY
   ↓
¿Por qué elegí esta solución?
   ↓
RESULT
   ↓
¿Qué mejoró?
   ↓
LESSON
   ↓
¿Qué haría diferente hoy?
```

### Ejemplo

> **Situation:** We had an API with increasing response times.
>
> **Action:** I profiled the service and identified that most of the latency came from a database query.
>
> **Decision:** I compared indexing, query restructuring and caching.
>
> **Why:** The query was highly selective, so adding an index was the simplest solution with the lowest operational complexity.
>
> **Result:** Response time decreased significantly.
>
> **Lesson:** I would introduce database performance monitoring earlier.

---

## 2. Las 5 historias que debes preparar

No necesitas preparar 20 historias.

Prepara **4–5 experiencias fuertes** que puedas reutilizar para diferentes preguntas.

| Historia | Puede responder preguntas sobre |
|---|---|
| **LLM / AI Agent** | AI, APIs, architecture, testing, scalability |
| **ML Pipeline** | ML, AWS, Docker, infrastructure |
| **Performance Optimization** | Databases, algorithms, scalability |
| **Architecture Decision** | Design, trade-offs, communication |
| **Production Incident** | Debugging, monitoring, reliability |

> [!tip]
> Una misma experiencia puede servir para responder muchas preguntas diferentes.

---

## 3. Algorithms & Data Structures

### Pregunta típica

> "Tell me about a time when you improved the performance of an algorithm."

#### Cómo responder

**Situation**

Un algoritmo estaba procesando grandes cantidades de datos y tenía una complejidad cercana a:

```text
O(n²)
```

**Action**

Identifiqué que realizábamos búsquedas repetidas dentro de una lista.

Reemplacé la lista por:

```python
dict
set
```

**Why**

Necesitábamos búsquedas rápidas y no necesitábamos mantener el orden.

Una búsqueda en un hash table es aproximadamente:

```text
List search → O(n)

Hash lookup → O(1) average
```

**Result**

La complejidad pasó aproximadamente de:

```text
O(n²)
```

a:

```text
O(n)
```

#### Lo que quieren evaluar

```text
¿Entiendes Big-O?
        ↓
¿Puedes encontrar un bottleneck?
        ↓
¿Sabes elegir una estructura?
        ↓
¿Puedes explicar el trade-off?
```

---

## 4. Backend & API Design

### Pregunta típica

> "How would you design an API for an AI service?"

Una arquitectura posible:

```text
Client
   ↓
API Gateway
   ↓
FastAPI
   ↓
AI / Agent Service
   ↓
LLM
```

Si el procesamiento tarda mucho:

```text
Client
   ↓
API
   ↓
Queue
   ↓
Worker
   ↓
LLM / ML Model
```

#### Ejemplo

```http
POST /v1/predictions
```

Request:

```json
{
  "customer_id": "123",
  "input": "..."
}
```

Respuesta:

```json
{
  "job_id": "abc123",
  "status": "processing"
}
```

Después:

```http
GET /v1/predictions/abc123
```

#### ¿Por qué?

Porque no quieres mantener una conexión HTTP abierta durante 30 segundos mientras el modelo trabaja.

Puedes utilizar:

```text
FastAPI
   ↓
SQS / Kafka
   ↓
Worker
   ↓
ML / LLM
```

#### Conceptos que demuestra

- REST APIs
- asynchronous processing
- queues
- scalability
- fault tolerance
- stateless services

---

## 5. Frontend & Performance

Aunque tu perfil sea principalmente backend/AI, pueden preguntarte:

> "How would you investigate a slow frontend?"

No empieces cambiando código.

Primero:

```text
Slow UI
   ↓
Measure
   ↓
Browser DevTools
   ↓
Network
Performance
Memory
Rendering
   ↓
Identify bottleneck
```

Por ejemplo:

```text
Frontend
   ↓
API
   ↓
Database
```

Puede parecer un problema del frontend, pero el verdadero problema puede ser:

```text
API response = 5 MB
```

cuando solamente necesitas:

```text
100 KB
```

Entonces optimizarías el backend/API antes de modificar el frontend.

> [!important]
> **Measure first, optimize second.**

---

## 6. Databases & Query Optimization

### Pregunta típica

> "A query went from 200 ms to 10 seconds. How would you investigate it?"

No respondas inmediatamente:

> "I would add more CPU."

Primero:

```text
Slow Query
    ↓
EXPLAIN / Query Profile
    ↓
Execution Plan
    ↓
Find bottleneck
```

Busca:

```text
Sequential Scan
JOIN
Sort
Aggregation
Large Scan
Network
Memory
```

#### Posibles soluciones

```text
Index
Partition pruning
Predicate pushdown
Better JOIN
Caching
Materialized View
Clustering
Incremental Processing
```

---

### 6.1 Index

Sin índice:

```text
Table
 ↓
Row 1
Row 2
Row 3
...
Row 10,000,000
```

Con índice:

```text
Index
 ↓
Relevant row
```

Ejemplo:

```sql
CREATE INDEX idx_users_email
ON users(email);
```

Pero recuerda:

> Los índices aceleran lecturas, pero tienen coste en storage y escrituras.

---

### 6.2 Query Plan (EXPLAIN / EXPLAIN ANALYZE)

**`EXPLAIN`** muestra el plan de ejecución **estimado** — qué va a hacer la base de datos, sin ejecutar la query.

**`EXPLAIN ANALYZE`** además **ejecuta la query de verdad** y da tiempos y filas **reales**, comparados con lo estimado.

```sql
EXPLAIN ANALYZE
SELECT *
FROM users
WHERE email = 'john@gmail.com';
```

Salida típica (Postgres):

```text
Seq Scan on users  (cost=0.00..18334.00 rows=1 width=120)
                    (actual time=0.02..142.31 rows=1 loops=1)
  Filter: (email = 'john@gmail.com'::text)
  Rows Removed by Filter: 999999
Planning Time: 0.15 ms
Execution Time: 142.40 ms
```

Qué mirar:

```text
Seq Scan          → está leyendo TODA la tabla (mala señal si la tabla es grande)
Index Scan        → está usando un índice (buena señal)
Index Only Scan   → mejor aún: no toca la tabla, solo el índice
Nested Loop       → JOIN fila por fila (ok en tablas pequeñas, lento en grandes)
Hash Join         → JOIN vía hash table (mejor para tablas grandes)
cost=X..Y         → estimación del planner (unidades arbitrarias, no ms)
actual time=X..Y  → tiempo real medido, en ms
rows (estimado) vs rows (actual) → si difieren mucho, las estadísticas están desactualizadas
```

**La señal más importante para diagnosticar "la query se volvió lenta al crecer la tabla":**

```text
estimated rows = 10
actual rows    = 999,000
```

Una diferencia enorme entre lo que el planner *esperaba* y lo que *encontró de verdad* casi siempre significa que las estadísticas de la tabla están obsoletas → el planner eligió mal la estrategia (ej. Seq Scan en vez de Index Scan) porque creía que había pocas filas que calificaban. La solución típica es correr `ANALYZE` (ver 6.10).

---

### 6.3 SELECT *

Evita:

```sql
SELECT *
FROM customers;
```

si solamente necesitas:

```sql
SELECT
    customer_id,
    country,
    revenue
FROM customers;
```

Esto reduce:

```text
Data scanned
     ↓
I/O
     ↓
Network
     ↓
Memory
```

---

### 6.4 Partition Pruning

Supongamos:

```text
sales/

2024/
2025/
2026/
```

Query:

```sql
SELECT *
FROM sales
WHERE year = 2026;
```

Idealmente:

```text
2024 → SKIP
2025 → SKIP
2026 → READ
```

Esto es:

> **Partition pruning**

---

### 6.5 Predicate Pushdown

Mala estrategia:

```text
Read everything
      ↓
Filter
```

Mejor:

```text
Filter
   ↓
Read only relevant data
```

Esto se conoce como:

> **Predicate pushdown / filter pushdown**

---

### 6.6 Snowflake

Snowflake utiliza **micro-partitions**.

Conceptualmente:

```text
Table
 │
 ├── Micro-partition 1
 ├── Micro-partition 2
 ├── Micro-partition 3
 ├── ...
 └── Micro-partition 10000
```

Snowflake mantiene metadata que permite evitar leer micro-partitions irrelevantes.

```text
Query
  ↓
Micro-partition metadata
  ↓
Pruning
  ↓
Read only relevant data
```

---

### 6.7 Caching

Si una query se repite:

```text
Query
 ↓
Cache?
 ├── YES → Return result
 └── NO  → Execute
```

El caching puede reducir:

- latency
- compute
- cost

---

### 6.8 Materialized Views

Si constantemente ejecutas:

```sql
SELECT
    customer_id,
    SUM(amount)
FROM sales
GROUP BY customer_id;
```

puedes materializar el resultado:

```text
Raw Sales
    ↓
Materialized View
    ↓
Precomputed result
```

Así evitas recalcular todo constantemente.

---

### 6.9 Incremental Processing

Mala estrategia:

```text
10 TB historical data
       ↓
Process 10 TB every day
```

Mejor:

```text
Historical = 10 TB
New data   = 20 GB

Process only:
20 GB
```

Esto es:

> **Incremental processing**

Tecnologías relacionadas:

- dbt incremental models
- Snowflake Streams
- Snowflake Tasks
- Dynamic Tables
- Spark Structured Streaming
- Delta Lake
- Apache Iceberg
- CDC

---

### 6.10 VACUUM y ANALYZE (Postgres)

Postgres usa **MVCC** (Multi-Version Concurrency Control): cuando actualizas o borras una fila, la fila vieja no se borra físicamente de inmediato — queda como una "dead tuple" por si otra transacción concurrente todavía la necesita ver.

```text
UPDATE / DELETE
       ↓
Fila vieja → "dead tuple" (no se borra al instante)
       ↓
Se acumulan con el tiempo
       ↓
Tabla "bloated" (ocupa más espacio del necesario, queries más lentas)
```

**`VACUUM`** limpia esas dead tuples y libera el espacio para reutilizarlo.

**`ANALYZE`** recalcula las **estadísticas** de la tabla (cuántas filas hay, distribución de valores, cuántos valores distintos por columna) que el **query planner** usa para decidir el plan de ejecución (ej. si usar un índice o hacer Seq Scan).

```sql
VACUUM ANALYZE users;
```

**Por qué esto explica el caso "200ms → 10s al crecer de 100K a 50M filas":**

```text
Tabla crece rápido
       ↓
Estadísticas viejas ya no representan la realidad
       ↓
Planner sigue usando el plan que era óptimo con 100K filas
       ↓
Ese plan es pésimo con 50M filas
       ↓
Query lenta
```

Postgres tiene **autovacuum**, un proceso en background que hace esto automáticamente — pero si el volumen de escritura es muy alto, o autovacuum está mal configurado/pausado, las estadísticas pueden quedar desactualizadas por mucho tiempo, y ahí toca correr `VACUUM ANALYZE` manualmente.

**Frase útil para la entrevista:** *"Si la query se degrada justo después de que la tabla creció mucho, sospecho primero de estadísticas desactualizadas — reviso `EXPLAIN ANALYZE` para comparar filas estimadas vs. reales, y si hay una diferencia grande, corro `ANALYZE` antes de tocar índices o reescribir la query."*

---

## 7. Testing

### Pregunta

> "How do you test an AI application?"

No respondas solamente:

> "I use unit tests."

Para una aplicación de AI tienes varias capas:

```text
AI Application
      │
 ┌────┼───────────────┐
 ▼    ▼               ▼
Unit Integration   Evaluation
Tests   Tests          │
                       ▼
                 LLM Evaluation
```

#### Unit tests

```text
¿El retriever devuelve los documentos correctos?
```

#### Integration tests

```text
API
 ↓
Retriever
 ↓
LLM
```

¿Todo funciona conjuntamente?

#### Evaluation

```text
¿La respuesta está basada en los documentos?
```

#### Regression testing

```text
Prompt v1
   ↓
Performance = 85%

Prompt v2
   ↓
Performance = 72%
```

Detectamos que un cambio empeoró el sistema.

---

## 8. AI / ML Applications

### Pregunta

> "Tell me about a time you used AI to solve a real business problem."

Estructura:

#### Situation

> We had a problem where users needed to interact with complex information or workflows more naturally.

#### Action

Diseñaste algo como:

```text
User
 ↓
API
 ↓
Agent
 ├── LLM
 ├── Tools
 ├── Retrieval
 └── State / Memory
       ↓
Business Systems
```

#### Why?

Un chatbot tradicional solamente genera texto.

Pero un Agent puede:

```text
Reason
   ↓
Retrieve
   ↓
Call tools
   ↓
Execute actions
   ↓
Return result
```

#### Result

Siempre intenta cuantificar:

```text
Response time ↓ X%

Manual work ↓ X%

Accuracy ↑ X%

Cost ↓ X%
```

Si no tienes números:

> Explica claramente el impacto operacional.

---

## 9. Architecture & Scalability

### Pregunta

> "How would you design a system that processes millions of events per day?"

Una arquitectura:

```text
Producers
    │
    ▼
 Kafka
    │
 ┌──┴─────────┐
 ▼            ▼
Stream      Storage
Processing     │
               ▼
             S3
               │
               ▼
           Warehouse
               │
          ┌────┴────┐
          ▼         ▼
         BI         ML
```

#### ¿Por qué Kafka?

Para desacoplar:

```text
Producer
    ≠
Consumer
```

y permitir escalar los consumidores independientemente.

#### Si un consumer falla

Puedes utilizar:

```text
Retries
Dead Letter Queue
Idempotency
```

para evitar perder mensajes o procesarlos incorrectamente.

---

## 10. Docker / Infrastructure / CI-CD

### Pregunta

> "How would you deploy an ML service?"

Una respuesta:

```text
Git
 ↓
Pull Request
 ↓
Tests
 ↓
Build Docker Image
 ↓
Security Scan
 ↓
Container Registry
 ↓
Deploy
 ↓
Monitoring
```

Ejemplo AWS:

```text
GitHub
   ↓
GitHub Actions
   ↓
Docker
   ↓
Amazon ECR
   ↓
ECS / Kubernetes
```

#### ¿Por qué Docker?

> To make the runtime environment reproducible and avoid differences between development, testing and production.

---

## 11. Security

### Pregunta

> "How would you secure an API?"

Arquitectura:

```text
Client
  ↓
HTTPS
  ↓
API Gateway
  ↓
Authentication
  ↓
Authorization
  ↓
Rate Limiting
  ↓
Application
  ↓
Database
```

Conceptos que debes conocer:

- OAuth2
- OIDC
- JWT
- IAM
- Least privilege
- Secrets management
- Encryption
- Input validation
- Rate limiting
- Audit logs

#### Authentication vs Authorization

**Authentication:**

> Who are you?

**Authorization:**

> What are you allowed to do?

Ejemplo:

```text
User
 ↓
Authenticated
 ↓
Role = Analyst
 ↓
Can read Sales
 ↓
Cannot access Payroll
```

---

## 12. Monitoring & Production Incidents

### Pregunta

> "Tell me about a production incident."

Nunca respondas solamente:

> "I fixed the bug."

Utiliza:

```text
Incident
   ↓
Detection
   ↓
Investigation
   ↓
Mitigation
   ↓
Root Cause
   ↓
Permanent Fix
   ↓
Prevention
```

#### Ejemplo

Un servicio de ML comienza a tener:

```text
Latency ↑
```

Investigas:

```text
CPU → normal
Memory → normal
Network → normal
Database → slow
```

Encuentras:

```text
Slow Database Query
```

#### Mitigation

```text
Caching
Reduce DB load
```

#### Root cause

Una query que funcionaba con poco volumen no escalaba con el crecimiento de los datos.

#### Permanent fix

```text
Query optimization
+
Index
+
Monitoring
```

#### Prevention

Agregar:

```text
Latency alerts
Database monitoring
Query performance metrics
```

---

## 13. Comunicación técnica

### Pregunta

> "Tell me about a technical disagreement."

No digas:

> "I convinced my colleague."

Mejor:

```text
Different opinions
       ↓
Understand constraints
       ↓
Define criteria
       ↓
Compare alternatives
       ↓
Prototype / Benchmark
       ↓
Decision
```

#### Ejemplo

Un compañero propone:

```text
Microservices
```

Tú propones:

```text
Modular Monolith
```

No debes discutir solamente sobre preferencias.

Define criterios:

| Criterio | Microservices | Modular Monolith |
|---|---|---|
| Complexity | High | Lower |
| Scalability | Excellent | Good |
| Deployment | Complex | Simple |
| Development speed | Lower initially | Higher |
| Operational overhead | High | Low |

Después decides basándote en las necesidades reales.

---

## 14. Speed vs Quality

### Pregunta

> "Tell me about a time you had to balance speed and quality."

Situación:

```text
Deadline
   ↓
Need MVP
```

Dos opciones:

```text
Perfect architecture
        ↓
3 months

MVP
        ↓
3 weeks
```

Una buena estrategia:

```text
MVP
 │
 ├── Simple architecture
 ├── Critical tests
 ├── Monitoring
 ├── Clear interfaces
 └── Documented limitations
```

La idea:

> **Move fast without creating uncontrolled technical debt.**

Una buena frase:

> "I focused on making the minimum architecture production-safe while keeping clear boundaries so we could evolve it later."

---

## 15. Cuando no sabes la respuesta

Esto es MUY importante.

Si no sabes algo:

❌ No inventes.

❌ No intentes aparentar experiencia que no tienes.

Mejor:

> **"I haven't worked directly with that technology, but I would approach the problem by..."**

Después explica tu razonamiento.

Ejemplo:

> "I haven't used that specific database engine in production, but I would first look at the execution plan, data distribution, indexes or clustering strategy, and I/O characteristics."

Esto demuestra:

```text
Honesty
   +
Problem solving
   +
Transferable knowledge
```

---

## 16. Senior Engineering Mindset

En preguntas técnicas intenta seguir este patrón:

```text
             PROBLEM
                ↓
        Understand requirements
                ↓
        Identify constraints
                ↓
       Generate alternatives
                ↓
        Compare trade-offs
                ↓
           Make decision
                ↓
          Implement
                ↓
            Measure
                ↓
            Improve
```

---

## 17. Palabras clave que debes utilizar

En lugar de decir:

> "This solution is faster."

Di:

> "This reduces latency because..."

En lugar de:

> "This architecture is better."

Di:

> "Given the constraints, I preferred this architecture because..."

En lugar de:

> "I used Kafka."

Di:

> "I used Kafka to decouple producers and consumers and allow independent scaling."

En lugar de:

> "I added an index."

Di:

> "The query was highly selective, so an index reduced the amount of data that needed to be scanned."

En lugar de:

> "I used caching."

Di:

> "The operation was read-heavy and the data did not change frequently, so caching reduced repeated computation and database load."

---

## 18. Trade-offs que debes conocer

Un ingeniero senior piensa constantemente en trade-offs.

| Decisión | Trade-off |
|---|---|
| Cache | Speed ↔ Freshness |
| Index | Read performance ↔ Write performance |
| Microservices | Scalability ↔ Complexity |
| Monolith | Simplicity ↔ Independent scaling |
| SQL | Flexibility ↔ Query complexity |
| NoSQL | Scalability ↔ Query flexibility |
| Sync processing | Simplicity ↔ Latency |
| Async processing | Scalability ↔ Complexity |
| Cloud managed service | Less operations ↔ Cost/vendor lock-in |
| Custom infrastructure | Control ↔ Maintenance |
| Larger model | Quality ↔ Cost/latency |
| Smaller model | Cost/latency ↔ Potential quality |
| RAG | Fresh knowledge ↔ Retrieval complexity |
| Fine-tuning | Specialized behavior ↔ Training/maintenance cost |

---

## 19. Tus 5 historias maestras

Prepara estas cinco historias con experiencias reales.

### Story 1 — AI / Agent

```text
Problem
   ↓
LLM / Agent solution
   ↓
Architecture
   ↓
Why this approach?
   ↓
Result
   ↓
What would you improve?
```

Debe poder responder:

- AI
- LLM
- Architecture
- API
- Testing
- Scalability

---

### Story 2 — ML Pipeline

```text
Data
 ↓
Pipeline
 ↓
Model
 ↓
Deployment
 ↓
Monitoring
```

Debe poder responder:

- ML
- AWS
- Docker
- CI/CD
- Infrastructure
- Monitoring

---

### Story 3 — Performance

```text
Slow system
     ↓
Measure
     ↓
Find bottleneck
     ↓
Optimize
     ↓
Benchmark
```

Debe poder responder:

- Algorithms
- Databases
- Performance
- Scalability

---

### Story 4 — Architecture Decision

```text
Problem
   ↓
Constraints
   ↓
Options
   ↓
Trade-offs
   ↓
Decision
   ↓
Result
```

Debe responder:

- Architecture
- Design
- Communication
- Decision making

---

### Story 5 — Production Incident

```text
Incident
   ↓
Detection
   ↓
Investigation
   ↓
Mitigation
   ↓
Root cause
   ↓
Fix
   ↓
Prevention
```

Debe responder:

- Debugging
- Monitoring
- Reliability
- Communication
- Production engineering

---

## 20. Preguntas que debes practicar

### Algorithms

- How would you optimize this algorithm?
- What is the time complexity?
- What data structure would you use?
- Why a hash map instead of a list?
- What are the trade-offs?

### Backend

- How would you design this API?
- REST vs asynchronous API?
- How would you handle millions of requests?
- How would you handle failures?
- How would you make the API idempotent?

### Databases

- Why is this query slow?
- How would you optimize it?
- What is an index?
- What is partition pruning?
- What is caching?
- What is a materialized view?
- How do you optimize JOINs?

### AI / ML

- When would you use RAG?
- When would you fine-tune?
- How do you evaluate an LLM application?
- How do you reduce inference cost?
- How do you handle hallucinations?
- How do you monitor an AI system?

### Architecture

- How would you scale this system?
- Monolith or microservices?
- Synchronous or asynchronous?
- How would you handle failures?
- Where would you put a queue?
- How would you design for high availability?

### Infrastructure

- Why Docker?
- How would you deploy this?
- How would you design CI/CD?
- How would you monitor it?
- What happens if one service goes down?

### Security

- Authentication vs authorization?
- How would you secure an API?
- How do you manage secrets?
- How would you implement least privilege?
- How do you protect sensitive data?

---

## 21. La regla de oro

> [!important]
> **Don't just explain WHAT you did. Explain WHY you did it.**

Una respuesta débil:

> "I used Redis."

Una respuesta fuerte:

> "The endpoint was read-heavy and the underlying data changed infrequently. I introduced Redis caching to avoid repeatedly querying the database. This reduced database load and improved latency. The trade-off was that we had to define an acceptable cache invalidation strategy."

La diferencia está en:

```text
WHAT
 ↓
WHY
 ↓
TRADE-OFF
 ↓
RESULT
```

---

## 22. Checklist antes de la entrevista

### Experiencias

- [ ] Tengo 5 historias concretas.
- [ ] Sé explicar qué problema había.
- [ ] Sé explicar qué hice YO.
- [ ] Sé explicar las alternativas.
- [ ] Sé justificar mi decisión.
- [ ] Tengo resultados medibles cuando sea posible.
- [ ] Sé explicar qué haría diferente hoy.

### Technical fundamentals

- [ ] Big-O
- [ ] Data structures
- [ ] APIs
- [ ] HTTP
- [ ] Databases
- [ ] Indexes
- [ ] Query optimization
- [ ] Partition pruning
- [ ] Caching
- [ ] Distributed systems
- [ ] Docker
- [ ] CI/CD
- [ ] Cloud
- [ ] Security
- [ ] Monitoring
- [ ] ML lifecycle
- [ ] MLOps
- [ ] LLM applications
- [ ] RAG
- [ ] Evaluation

---

## 23. Mentalidad durante la entrevista

Cuando te den un problema, no empieces inmediatamente a programar.

Piensa:

```text
1. What exactly is the problem?
              ↓
2. What are the constraints?
              ↓
3. What scale are we talking about?
              ↓
4. What are the possible solutions?
              ↓
5. What are the trade-offs?
              ↓
6. Which solution would I choose?
              ↓
7. How would I measure success?
```

Y si el problema cambia:

```text
"Now imagine traffic increases 100x..."
```

no cambies automáticamente de tecnología.

Primero pregunta:

```text
What is the new bottleneck?
```

Luego razona:

```text
Bottleneck
    ↓
Database?
Network?
CPU?
Memory?
Storage?
LLM?
External API?
    ↓
Solution
```

> **Ese proceso de razonamiento es probablemente más importante para la entrevista que memorizar una lista de herramientas.**