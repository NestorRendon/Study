# IA en el Ciclo de Vida del Software: Más Allá de Generar Código

Este cubre las **metodologías** que están redefiniendo cómo se diseña, planifica, valida y evoluciona software cuando la IA deja de ser solo "autocompletado" y pasa a ser un participante activo del ciclo de vida (SDLC).

---

## Panorama general

| Metodología | ¿Qué escribes primero? | Rol principal de la IA | Ideal para |
| --- | --- | --- | --- |
| Vibe Coding | Un prompt en lenguaje natural | Generar código completo por sensación/iteración | Prototipos descartables, exploración rápida |
| Specs-Driven Development (SDD) | Especificaciones | Generar código, pruebas y documentación desde la spec | Equipos que quieren trazabilidad y consistencia |
| Model-Driven Development (MDD) | Modelos (UML, entidades) | Generar código a partir de modelos | Sistemas empresariales tradicionales |
| Domain-Driven Design (DDD) | Modelo del negocio | Ayudar a descubrir dominios y mantener lenguaje ubicuo | Dominios complejos (finanzas, salud, logística) |
| Behavior-Driven Development (BDD) | Escenarios Given/When/Then | Generar y validar pruebas | Equipos con QA y requisitos funcionales claros |
| Test-Driven Development (TDD) | Tests | Escribir y corregir código hasta pasar las pruebas | Alta calidad y refactorización segura |
| Contract/API-First | Contratos o API | Generar clientes, servidores y documentación | Microservicios e integraciones |
| Documentation-Driven Development | Documentación | Mantener docs y código sincronizados | Proyectos con fuerte necesidad de documentación |
| Intent-Driven Development (IDD) | Objetivos de alto nivel (intención) | Diseñar e implementar la solución completa | Prototipos rápidos y apps aceleradas por IA |
| Constraint-Driven Development (CDD) | Restricciones / reglas de negocio | Optimizar y generar la solución dentro de límites no negociables | Sistemas con requisitos de costo, seguridad o cumplimiento |
| Agentic Software Development | Planes y tareas | Coordinar múltiples agentes especializados por rol | Automatización de flujos de desarrollo complejos, equipos con varios agentes |

---

## 1. El punto de partida: Vibe Coding

Término acuñado por Andrej Karpathy: describir en lenguaje natural lo que quieres y dejar que el agente genere el código, iterando "por sensación" hasta que funciona.

- **Ventaja**: velocidad de descubrimiento y prototipado.
- **Problema (2025)**: a medida que los proyectos escalan, el código generado se desvía del intento original, alucina APIs, y cada iteración grande termina en "regenerar desde cero". No hay artefacto estable que capture *qué* debía construirse, solo el prompt efímero.
- Este fallo es el que da origen directo a la mayoría de las metodologías nativas de IA que siguen.

---

## 2. Metodologías clásicas, reinterpretadas por IA

Estas no nacieron con la IA generativa, pero llevan años establecidas en ingeniería de software y hoy tienen una capa de IA que las acelera:

- **Model-Driven Development (MDD)**: se modela primero el sistema (UML, diagramas de entidades) y el código se genera a partir del modelo. Hoy los agentes de IA leen esos modelos y generan directamente clases, servicios y migraciones — útil en sistemas empresariales grandes donde el modelo de datos es más estable que la implementación.
- **Domain-Driven Design (DDD)**: el foco es modelar el dominio del negocio y mantener un "lenguaje ubicuo" compartido entre negocio e ingeniería. La IA ahora ayuda a *descubrir* límites de contexto (bounded contexts) analizando conversaciones y documentos de negocio, y a mantener ese lenguaje consistente en código y specs — valioso en dominios complejos como finanzas o salud.
- **Behavior-Driven Development (BDD)**: se escriben escenarios Given/When/Then antes de codificar. Los agentes de IA generan esos escenarios a partir de requisitos en lenguaje natural y luego generan y validan las pruebas correspondientes — buen punto de encuentro entre QA, negocio e IA.
- **Test-Driven Development (TDD)**: se escribe el test antes que el código. Con IA, el agente escribe el test, escribe el código, y itera automáticamente hasta que el test pasa — reduce el ciclo rojo-verde-refactor a supervisión humana en lugar de ejecución manual.
- **Contract/API-First**: se define el contrato (OpenAPI, GraphQL schema, protobuf) antes de implementar. La IA genera clientes, servidores mock, SDKs y documentación directamente del contrato — central en arquitecturas de microservicios donde múltiples equipos consumen la misma API.
- **Documentation-Driven Development**: la documentación se escribe primero y guía la implementación. La IA ahora mantiene automáticamente docs y código sincronizados, detectando cuándo un cambio de código invalida una sección de la documentación.

---

## 3. Specs-Driven Development (SDD)

**Definición**: metodología donde la especificación escrita —no el código— es el artefacto primario y ejecutable del proyecto. El código se convierte en una salida regenerable derivada de esa spec, producida por humanos, agentes de IA, o ambos.

### Flujo de trabajo
```text
Spec (qué debe hacer el sistema)
    |
Plan de implementación (cómo)
    |
Tareas atómicas
    |
Generación de código (humano y/o agente)
    |
Validación contra la spec
```

La especificación se trata como un **contrato operacional ejecutable**: no es documentación que se desactualiza, es la fuente de verdad contra la que se valida y regenera el código.

### Por qué importó en 2025-2026
Surgió como respuesta directa al *vibe coding*: GitHub reporta que equipos usando Spec Kit internamente tienen un orden de magnitud menos ciclos de "regenerar desde cero" frente a prompting ad-hoc. AWS documenta casos donde features de 40 horas se entregaron en menos de 8 horas de tiempo humano al escribirse primero como spec.

### Ecosistema de herramientas (2026)

| Categoría | Herramientas | Enfoque |
| --- | --- | --- |
| Spec-as-source | Tessl, OpenSpec | La spec vive en el repo como fuente viva, con tracking de deltas; el código es 100% derivado |
| Spec-first scaffolding | GitHub Spec Kit, AWS Kiro, GSD, Traycer | Se escribe la spec primero, luego se anda hacia el código paso a paso |
| Agentic-agile orchestration | BMAD-METHOD | La spec se combina con un equipo de agentes especializados (ver sección 5) |

### Una variante relevante: Constitutional Spec-Driven Development (CSDD)
Embebe restricciones de seguridad no negociables directamente en la capa de especificación, de modo que el código generado por IA sea seguro *por construcción* y no por verificación posterior. Reportado con una reducción del 73% en defectos de seguridad frente a generación sin restricciones — es el punto de contacto entre SDD y Constraint-Driven Development (sección 4).

---

## 4. Metodologías nativas de la era de IA

### Intent-Driven Development (IDD)
Un paso más allá de SDD: en lugar de escribir una especificación estructurada, se describe la **intención de alto nivel** (el objetivo) y el agente razona sobre la arquitectura, genera la implementación en múltiples archivos, escribe las pruebas correspondientes y abre un pull request para revisión. Se la describe como una evolución de Agile/SDD moderno: alinear la intención primero, construir iterativamente, y documentar la realidad ya construida ("build-first documentation") en lugar de documentar antes de construir.

### Constraint-Driven Development (CDD)
En vez de partir de una especificación completa, se parte de las **restricciones del negocio** (reglas, límites de costo, cumplimiento normativo) codificadas como restricciones inmutables en un motor de validación. La IA genera y optimiza la solución *dentro* de esos límites — el ingeniero deja de escribir código línea por línea y pasa a definir y mantener las restricciones. Define típicamente 10 tipos de restricción (cuantitativas, temporales, invariantes, condicionales, causales, de recursos, de autorización, de patrón, blandas y probabilísticas). Ideal cuando el riesgo de que la IA "se salga de los rieles" (costos, seguridad, cumplimiento) es inaceptable.

### Agentic Software Development
La categoría más amplia: agentes autónomos colaboran a través de **todo** el SDLC (análisis, diseño, construcción, pruebas, entrega), no solo generando código más rápido sino operando como miembros de equipo digitales con roles definidos, memoria compartida y una capa de observabilidad unificada. Dos instancias concretas y documentadas de esta categoría:

- **BMAD-METHOD** (sección 3): 21 agentes especializados (product owner, arquitecto, QA, etc.) colaborando sobre una spec compartida.
- **Agentsway** (paper arXiv:2510.23664, oct. 2025): metodología académica donde un **orquestador humano único** supervisa un equipo de agentes con roles fijos (planning, prompting, coding, testing, fine-tuning), con un loop autosuperante donde los insights de cada iteración refinan el ciclo siguiente vía fine-tuning continuo — no solo vía retrospectivas humanas. Su premisa central: Agile, Kanban y ShapeUp asumen que los colaboradores son personas; cuando los agentes son colaboradores de primera clase, esas metodologías se quedan cortas.

---

## 5. Comparación profunda: los tres extremos del espectro

| Dimensión | Vibe Coding | Specs-Driven Development (SDD) | Agentic Software Development (Agentsway/BMAD) |
| --- | --- | --- | --- |
| Artefacto fuente de verdad | El prompt (efímero) | La especificación escrita (persistente, versionada) | La especificación + el historial de iteraciones del equipo de agentes |
| Rol de la IA | Generador de código bajo demanda | Co-autor que deriva código y valida contra la spec | Colaborador de primera clase con roles fijos (planning, coding, testing, fine-tuning) |
| Rol humano | Prompter e iterador "por sensación" | Autor de spec + revisor arquitectónico | Orquestador único que supervisa y valida, no produce directamente |
| Fases donde interviene la IA | Solo implementación | Diseño (spec), planificación (tareas), implementación, validación | Diseño, planificación, implementación, validación y evolución (aprendizaje continuo) |
| Riesgo principal | Deriva de intención, alucinación de APIs, "regenerar desde cero" | Sobrecarga de mantener specs sincronizadas; requiere disciplina de autoría | Gobernanza y confianza: validar que agentes autónomos no se desvíen sin supervisión humana suficiente |
| Cuándo usarlo | Prototipos descartables, exploración rápida | Software de producción que debe mantenerse en el tiempo | Equipos que ya operan con múltiples agentes especializados y necesitan un ciclo de vida formal para coordinarlos |

**Lectura del panorama**: no son alternativas mutuamente excluyentes sino una progresión de madurez. *Vibe coding* resuelve velocidad de descubrimiento; las metodologías clásicas (MDD, DDD, BDD, TDD, API-First, Documentation-Driven) aportan la disciplina que ya existía y que la IA ahora acelera; *SDD* e *IDD* resuelven durabilidad en producción al fijar la spec o la intención como contrato; *CDD* añade la capa de gobernanza cuando las restricciones son innegociables; y *Agentic Software Development* (Agentsway, BMAD) resuelve la coordinación cuando ya no hay un solo agente sino un equipo con roles, y la evolución del software se vuelve parte del propio método.

---

## Fuentes

- [Spec-Driven Development (SDD): The Definitive 2026 Guide](https://www.thebcms.com/blog/spec-driven-development/)
- [6 Best Spec-Driven Development Tools for AI Coding in 2026 — Augment Code](https://www.augmentcode.com/tools/best-spec-driven-development-tools)
- [Spec-Driven Development in 2026: The end of code as the center of development? — Devoteam](https://www.devoteam.com/expert-view/spec-driven-development-2026/)
- [BMAD vs Spec Kit vs OpenSpec: Choosing Your Spec-Driven AI Framework — Reenbit](https://reenbit.com/bmad-vs-spec-kit-vs-openspec-choosing-your-spec-driven-ai-framework/)
- [spec-compare: research comparing 6 spec-driven development tools — GitHub](https://github.com/cameronsjo/spec-compare)
- [Agentsway — Software Development Methodology for AI Agents-based Teams (arXiv:2510.23664)](https://arxiv.org/abs/2510.23664)
- [Beyond vibe coding: the case for spec-driven AI development — The New Stack](https://thenewstack.io/vibe-coding-spec-driven/)
- [Vibe Coding vs. Spec-Driven Development in 2026 — InterCode](https://intercode.com/blog/vibe-coding-vs-spec-driven-development-in-2026)
- [Intent-Driven Development (IDD) — intentdrivendevelopment.org](https://intentdrivendevelopment.org/)
- [Intent-Driven Development: A Modern SDLC for AI-Accelerated Teams — Keyhole Software](https://keyholesoftware.com/intent-driven-development-build-first-documentation/)
- [Constraint-Driven Development: A New Paradigm for AI-Assisted Software Engineering — Gray Beam Technology](https://www.graybeam.tech/constraint-driven-development/)
- [Constitutional Spec-Driven Development: Enforcing Security by Construction (arXiv:2602.02584)](https://arxiv.org/html/2602.02584v1)
- [Agentic Software Development Takes The Lead — Forrester](https://www.forrester.com/blogs/agentic-software-development-takes-the-lead-from-code-assistants-to-orchestrated-sdlc-agents/)
- [Assistance to Autonomy: A Systematic Literature Review of Agentic AI across the SDLC (arXiv:2605.15245)](https://arxiv.org/pdf/2605.15245)
