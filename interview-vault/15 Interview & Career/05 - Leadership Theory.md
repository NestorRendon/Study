# Leadership Theory — Cómo Piensan y Actúan los Líderes

**Prev:** [[04 - Culture and Leadership Rapid Answers]] · **Next:** [[Home|Home]]

---

> [!abstract] Para qué sirve esto
> Esto es teoría, no historias tuyas. Te da vocabulario y modelos mentales para responder preguntas de liderazgo con más profundidad que "trabajé en equipo" — y para reconocer estos patrones cuando el entrevistador los mencione.

---

## Índice rápido

| Bloque | Contiene |
|---|---|
| [[#1. Cómo piensan los líderes (mentalidad)]] | Ownership, servant leadership, systemic thinking |
| [[#2. Cómo resuelven problemas]] | OODA loop, first principles, 5 whys, disagree & commit |
| [[#3. Tácticas del día a día]] | Delegación, 1:1s, feedback, OKRs, priorización |
| [[#4. Toma de decisiones en equipo]] | RACI, DACI/RAPID, psychological safety |
| [[#5. Manejo de conflicto]] | Thomas-Kilmann |
| [[#6. Liderazgo sin autoridad formal]] | Influence without authority (el más relevante para ti) |
| [[#7. Buenas prácticas — resumen accionable]] | Checklist rápido |

---

## 1. Cómo piensan los líderes (mentalidad)

### Extreme Ownership (Jocko Willink)

> "No hay malos equipos, solo malos líderes."

Idea central: el líder asume responsabilidad total por los resultados, incluso los de otros — en vez de culpar a "el equipo", "el proceso" o "el cliente". Si algo falla, la primera pregunta es *"¿qué pude haber hecho yo diferente?"*, no *"¿quién falló?"*.

```text
Algo sale mal
     ↓
Reacción débil: "El equipo no ejecutó bien"
     ↓
Reacción de ownership: "¿Fui claro en las expectativas? ¿Di el contexto suficiente?"
```

### Servant Leadership (Robert Greenleaf)

El líder existe para **remover obstáculos** del equipo, no para que el equipo le sirva a él. Preguntas típicas de un servant leader: *"¿qué necesitas para hacer tu mejor trabajo?"*, *"¿qué te está bloqueando?"*.

Contraste útil para entrevista:
```text
Liderazgo tradicional     → el equipo ejecuta la visión del líder
Servant leadership        → el líder habilita al equipo para que ejecute su propia mejor versión
```

### Situational Leadership (Hersey-Blanchard)

No hay un solo estilo de liderazgo correcto — depende de la **competencia y compromiso** de la persona en esa tarea específica:

```text
Baja competencia, alto compromiso   → Dirigir (instrucciones claras)
Baja competencia, bajo compromiso   → Entrenar (explicar el por qué, motivar)
Alta competencia, bajo compromiso   → Apoyar (escuchar, dar autonomía con soporte)
Alta competencia, alto compromiso   → Delegar (dejarlo trabajar solo)
```

Útil para responder: *"¿cómo adaptas tu estilo según la persona?"* — un junior nuevo necesita dirección, un senior necesita autonomía, no el mismo trato para ambos.

### Systems thinking

Un líder técnico no optimiza un componente aislado — piensa en cómo una decisión afecta al sistema completo (equipo, producto, otros equipos). Ejemplo: elegir microservicios "porque escala mejor" sin pensar en el costo operativo para un equipo de 3 personas es *optimización local*, no *systems thinking*.

---

## 2. Cómo resuelven problemas

### OODA Loop (John Boyd) — decisiones bajo incertidumbre y velocidad

```text
Observe   → ¿qué está pasando realmente? (datos, no suposiciones)
Orient    → ¿qué significa esto dado el contexto?
Decide    → elegir un curso de acción
Act       → ejecutar, y volver a Observe
```

Originado en tácticas militares/de combate aéreo; en tech se usa para decisiones rápidas con información incompleta (ej. un incidente de producción) — el punto clave es que el ciclo se repite rápido, no se busca la decisión perfecta de una vez.

### First Principles Thinking

En vez de razonar por analogía ("lo hacemos así porque siempre se ha hecho así"), se descompone el problema hasta sus verdades fundamentales y se reconstruye desde ahí. Popularizado por Elon Musk, pero es una herramienta general de ingeniería: *"¿por qué creemos que esto es necesario? ¿qué pasaría si lo quitamos?"*

### Root Cause Analysis / 5 Whys

```text
El servicio se cayó
   → ¿Por qué? Se quedó sin memoria
      → ¿Por qué? Un proceso no liberaba conexiones
         → ¿Por qué? No había timeout configurado
            → ¿Por qué? No era parte del checklist de deploy
               → ¿Por qué? No había checklist de deploy
```

La causa raíz real casi nunca es la primera respuesta — por eso se pregunta "por qué" varias veces (típicamente 5, no es una regla estricta).

### Blameless postmortems

Después de un incidente, el análisis se enfoca en el **sistema y el proceso**, no en culpar a la persona que cometió el error. Razón: si la gente teme ser culpada, oculta información — y sin información completa no se puede prevenir que se repita. Práctica estándar en equipos de infraestructura/SRE (Google SRE book la popularizó).

### Disagree and Commit (Amazon Leadership Principle)

Un líder puede estar en desacuerdo con una decisión, expresar su desacuerdo con claridad **una vez**, y si el grupo decide diferente, comprometerse 100% con la ejecución — sin sabotear pasivamente ni repetir la discusión. Evita la parálisis por consenso perfecto.

---

## 3. Tácticas del día a día

### Delegación — no es "quitarte trabajo de encima"

```text
Tarea de bajo riesgo, alta repetición   → delega y no revises cada paso
Tarea de alto riesgo, poco explorada    → delega con checkpoints frecuentes
Tarea crítica y única                   → considera hacerla tú, o delega con mentoría cercana
```

Error común: delegar solo la tarea aburrida y quedarse con todo lo interesante — mata la motivación del equipo.

### Feedback — SBI Model (Situation-Behavior-Impact)

```text
Situation  → contexto específico ("en la reunión de ayer...")
Behavior   → comportamiento observable, no interpretación ("interrumpiste tres veces...")
Impact     → efecto real ("...y dos personas no terminaron de compartir su punto")
```

Evita el error común de dar feedback como juicio de carácter ("eres desorganizado") en vez de comportamiento observable y su impacto.

### Radical Candor (Kim Scott)

```text
                    Challenge Directly →
Care Personally  ┌─────────────────┬─────────────────┐
       ↓         │ Ruinous Empathy │ Radical Candor   │
                  │ (amable pero    │ (honesto Y       │
                  │  inútil)        │  cuidadoso)      │
                  ├─────────────────┼─────────────────┤
                  │ Manipulative    │ Obnoxious        │
                  │ Insincerity     │ Aggression       │
                  │ (ni honesto ni  │ (honesto pero    │
                  │  cuidadoso)     │  cruel)          │
                  └─────────────────┴─────────────────┘
```

El objetivo es el cuadrante superior derecho: decir la verdad directamente, pero desde un lugar de que te importa la persona.

### OKRs (Objectives and Key Results)

```text
Objective   → dirección cualitativa, inspiradora ("Mejorar la confiabilidad del agente")
Key Results → métricas concretas y verificables ("Reducir tasa de alucinación de 8% a 3%")
```

### Priorización — Eisenhower Matrix

```text
                Urgente              No urgente
Importante      Hacer ahora          Planificar
No importante   Delegar              Eliminar
```

---

## 4. Toma de decisiones en equipo

### RACI

Para cada decisión/tarea, define:
```text
R — Responsible   → quién hace el trabajo
A — Accountable   → quién responde por el resultado (solo una persona)
C — Consulted     → a quién se le pide opinión antes de decidir
I — Informed      → a quién se le avisa después de decidido
```

### DACI / RAPID — frameworks de decisión más rápidos que "consenso total"

```text
D — Driver      → lidera el proceso de decisión
A — Approver    → decide finalmente
C — Contributors → aportan input
I — Informed    → se enteran del resultado
```

Útil para responder *"¿cómo evitas que las decisiones se estanquen?"* — nombrar quién decide, no buscar que todos estén de acuerdo.

### Psychological Safety (Google — Project Aristotle)

Google estudió qué hace a un equipo de alto desempeño y encontró que el factor #1 no era talento individual, sino **seguridad psicológica**: que las personas sientan que pueden admitir un error, hacer una pregunta "obvia", o disentir, sin miedo a ser humilladas o penalizadas. Es la base que hace posible el feedback honesto y el "disagree and commit".

---

## 5. Manejo de conflicto — Thomas-Kilmann Conflict Modes

Dos ejes: qué tan **asertivo** eres (defender tu posición) y qué tan **cooperativo** eres (considerar la del otro).

```text
                     Alta asertividad
                          │
        Competir ─────────┼───────── Colaborar
                          │
Baja cooperación ─────────┼───────── Alta cooperación
                          │
         Evitar ─────────┼───────── Acomodar
                          │
                     Baja asertividad
                          │
                    (Comprometer = el centro,
                     equilibrio entre ambos ejes)
```

- **Competir**: defiendes tu posición sin ceder — útil en decisiones urgentes de seguridad, no para desacuerdos de opinión.
- **Colaborar**: buscas una solución que satisfaga a ambos — el modo ideal para desacuerdos técnicos importantes (requiere tiempo).
- **Comprometer**: cada uno cede algo — rápido, pero no siempre la mejor solución técnica.
- **Evitar**: pospones el conflicto — válido si el tema es trivial o necesitas más información antes de discutir.
- **Acomodar**: cedes a la posición del otro — válido cuando el tema importa más a la otra persona que a ti, o no es tu área de expertise.

Ningún modo es "el bueno" — un líder maduro elige el modo según la situación, no usa siempre el mismo.

---

## 6. Liderazgo sin autoridad formal (el más relevante para ti)

Como IC senior/PhD sin título de manager, esto es lo que un entrevistador realmente evalúa cuando pregunta "liderazgo":

```text
Autoridad formal    → "hazlo porque lo digo yo" (no la tienes, no la necesitas)
Influencia          → la gente te sigue porque confía en tu criterio
```

Tácticas concretas de influencia sin autoridad:
- **Evidencia sobre opinión** — traer datos/prototipos en vez de "creo que deberíamos".
- **Entender antes de proponer** — la gente se resiste menos a una idea si siente que ya la escuchaste primero (ver Thomas-Kilmann "colaborar").
- **Ganar aliados uno a uno antes de la reunión grupal** — es más fácil cambiar una opinión en una conversación 1:1 que frente a todo el equipo (donde defender la postura pública cuesta más).
- **Ser el que escribe el documento** — quien redacta la propuesta técnica (RFC/ADR) suele terminar guiando la discusión, sin necesidad de título.
- **Consistencia** — la influencia se construye con decisiones acertadas repetidas en el tiempo, no en una sola conversación brillante.

---

## 7. Buenas prácticas — resumen accionable

| Situación | Qué hacer |
|---|---|
| Alguien falla | Primero pregúntate qué pudiste hacer diferente (Extreme Ownership) |
| Vas a dar feedback difícil | Usa SBI: situación → comportamiento → impacto observable |
| Un desacuerdo técnico se extiende | Define quién decide (DACI), no busques consenso perfecto |
| Necesitas that alguien crezca | Ajusta tu estilo a su nivel (Situational Leadership), no repitas el mismo trato para todos |
| Perdiste una discusión pero no estás de acuerdo | Disagree and commit — exprésalo una vez, después ejecuta sin sabotear |
| Quieres influir sin autoridad formal | Trae datos, escucha primero, escribe la propuesta tú |
| Un incidente ocurrió | Postmortem sin culpar personas — la causa raíz casi nunca es la primera respuesta (5 Whys) |

---

[[Home|← Home]]
