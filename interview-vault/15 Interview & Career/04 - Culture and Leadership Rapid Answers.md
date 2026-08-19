# Culture & Leadership — Respuestas Rápidas

**Prev:** [[03 - Industry Experience]] · **Related:** [[Projects]] · [[Technical Interview — Problem Solving Cheat Sheet]]

---

> [!warning] Cómo usar esto
> No son guiones para memorizar — se nota cuando suena a libreto. Son esqueletos que completas con TU verdad en 10-15 segundos, en voz alta, antes de entrar. Las de motivación/fit no las puedo responder por ti — nadie puede.

---

## 1. Trabajo en equipo / colaboración

**¿Cómo es trabajar con equipos multidisciplinarios?**
> "En xFarm trabajo constantemente con agrónomos, producto e ingeniería — el reto es traducir una necesidad de negocio (ej. cuándo regar, qué plaga es prioritaria) en una decisión técnica concreta. En xAgent tuve que entender qué necesitaban los agrónomos de las tools de clima/plagas/riego antes de diseñar la arquitectura del agente."

**Cuéntame de una vez que convenciste a alguien de tu enfoque técnico.**
- Framework: Entender sus restricciones → Definir criterios → Comparar alternativas → Decisión con datos (sección 13 del cheat sheet).
- [completa con: ¿quién, qué proponía la otra persona, qué datos usaste?]

**¿Cómo manejas no estar de acuerdo con una decisión del equipo?**
> "Expreso mi punto una vez, con claridad y datos. Si el equipo decide distinto, ejecuto igual y me comprometo — no repito la discusión después de decidida." [completa con ejemplo real]

---

## 2. Liderazgo (sin autoridad formal)

**Cuéntame de una vez que lideraste algo sin autoridad formal.**

> ⚠️ Borrador basado en lo que ya está documentado — verifica el detalle antes de usarlo.
> "En xAgent, propuse y impulsé la decisión arquitectónica de tratar el LLM como componente de razonamiento, manteniendo las operaciones críticas de negocio detrás de interfaces controladas en vez de dejar que el LLM las ejecutara directamente. No tenía autoridad formal sobre esa decisión — tuve que explicar concretamente qué podía salir mal (acciones irreversibles disparadas por una alucinación) para alinear al equipo."
> **Verifica:** ¿tuviste que convencer activamente a alguien, o fue consenso desde el inicio? Ajusta la frase a lo que realmente pasó — si fue consenso, usa otra: ¿alguna vez impulsaste tú solo/a una práctica (ej. guardrails, evaluación con LLM-as-judge) que el equipo adoptó después?

**¿Cómo mentoreas o ayudas a alguien más junior?**
[completa — puede ser mentoría formal o simplemente ayudar a un colega a resolver algo técnico / code review / explicar un concepto]

**Cuéntame de una decisión técnica difícil que comunicaste al equipo.**
- Reusa la historia de xAgent (arriba) o la de RAG vs. fine-tuning 
---

## 3. Manejo de conflicto

**Desacuerdo técnico fuerte con un colega.**
- Ya tienes el framework completo: [[Technical Interview — Problem Solving Cheat Sheet#13. Comunicación técnica]] (el ejemplo de microservicios vs. monolito modular que practicamos).

**Alguien no cumple su parte en un proyecto conjunto.**
> "Primero hablo directamente y en privado para entender la causa — falta de contexto, sobrecarga, algo bloqueándolo — antes de asumir mala intención." [completa con ejemplo real]

---

## 4. Fracaso / error propio

**Cuéntame de una vez que te equivocaste técnicamente.**
- Candidato real: el bug de *language switching* en xAgent (ya mencionado en [[03 - Industry Experience]] junto con hallucinations y comportamiento inesperado del agente). Nos quedó pendiente completar detección → causa raíz → fix → prevención — vale la pena terminarlo cuando tengas 10 minutos, es tu historia de "Production Incident" (Story 5 del cheat sheet, la única de las 5 que aún no tienes armada).
- Si no alcanzas a completarla, usa cualquier bug real de xTrap/xAgent que recuerdes de memoria, aunque sea sin todos los detalles.

**¿Qué proyecto no salió como esperabas?**
[completa — cierra siempre con la lección, no solo con el fallo]

---

## 5. Motivación / fit — estas son 100% tuyas

No puedo responderlas por ti sin inventar — y notarán si suena inventado. Anota ahora mismo 2-3 palabras clave reales para cada una:



---

## 6. Ambigüedad / prioridades

**Requisitos poco claros.**
> Candidato fuerte: UF-CIVI (tu PhD) — no había ground truth claro de cuántos clusters eran "correctos", tuviste que definir tú mismo el criterio de validación. [completa con el resto de la historia si hay tiempo]

**Priorizar con más trabajo del que puedes hacer.**
[completa]

---

## 7. Feedback

**Feedback difícil que recibiste.**
[completa]

**Cómo das feedback sobre el código/enfoque de un colega.**
> "Específico y accionable, en privado si es sensible, enfocado en el código o la decisión, no en la persona."

---

[[Home|← Home]]
