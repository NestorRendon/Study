# Frontend Performance Debugging

**Prev:** [[10 - Python Interview Traps]] · **Next:** [[Home|Home]]

---

## Regla de oro

> [!important]
> **Measure first, optimize second.** No cambies código de UI hasta confirmar dónde se va el tiempo.

"El dashboard está lento" puede significar cosas muy distintas — red, backend, o render. Adivinar y optimizar el componente equivocado quema horas.

```text
Slow UI
   ↓
Measure
   ↓
Browser DevTools
   ↓
Network · Performance · Memory · Rendering
   ↓
Identificar el bottleneck real
```

---

## 1. Network tab — el primer sospechoso

Antes de tocar un solo componente, revisa:

```text
¿Cuántos requests?
¿De qué tamaño es cada respuesta?
¿Cuánto tarda el TTFB (Time To First Byte)?
¿Hay requests en cascada (uno espera al otro) en vez de paralelos?
```
Time To First Byte (TTFB) is ==a metric that measures the time a browser takes to receive the very first byte of page data from a server after a user requests it==. A good TTFB is 0.8 seconds or less, while anything above 1.8 seconds is poor

**Caso típico:** el frontend "se ve lento" pero el problema real es que el backend devuelve más datos de los necesarios.

```text
API response = 5 MB
      ↓
cuando solo necesitas
      ↓
100 KB
```

En ese caso, el fix no es frontend — es paginar, filtrar campos en el backend, o comprimir la respuesta. Optimizar React ahí no serviría de nada.

---

## 2. Performance tab — si el problema es render, no red

Si el Network tab está limpio (requests rápidos, payloads razonables) pero la UI sigue lenta, ahí sí es un problema de renderizado:

```text
Causas comunes
   ├── Re-renders innecesarios (estado mal estructurado, props que cambian de referencia cada render)
   ├── Listas grandes sin virtualización (renderizar 10,000 filas del DOM a la vez)
   ├── Cálculos pesados en el hilo principal (bloquean la UI)
   └── JS bundle muy grande (tarda en parsear/ejecutar antes de que la página sea interactiva)
```

Herramientas: React DevTools Profiler (qué componentes re-renderizan y por qué), Chrome Performance tab (flame graph de JS/rendering).

---

## 3. Memory tab — leaks

Síntoma: la app se pone más lenta cuanto más tiempo lleva abierta (no es lenta desde el inicio).

```text
Heap snapshot en el tiempo 0
       ↓
Interactuar con la app
       ↓
Heap snapshot en el tiempo N
       ↓
¿Objetos que deberían haberse liberado siguen ahí?
```

Causas típicas: event listeners no removidos, closures reteniendo referencias, timers/intervals no limpiados en el unmount de un componente.

---

## 4. Checklist de diagnóstico (orden recomendado)

```text
1. Network tab   → ¿es tamaño de payload / número de requests / latencia de red?
2. Performance   → si red está bien, ¿es render/JS bloqueando el hilo principal?
3. Memory        → ¿empeora con el tiempo? posible leak
4. Backend       → si el payload es grande o hay muchos requests, el fix real
                    puede estar en la API, no en el frontend
```

---

## Frase para la entrevista

> "Antes de tocar código, mido con las DevTools del navegador — Network para tamaño de payload y número de requests, Performance para renderizado. Muchas veces 'el frontend está lento' es en realidad la API devolviendo más datos de los necesarios; optimizar componentes sin medir primero es apostar a ciegas."

---

## Common traps

| Trap | Correct |
|------|---------|
| Empezar a optimizar componentes sin medir | DevTools primero: Network → Performance → Memory |
| Asumir que "lento" = problema de frontend | Puede ser payload de API, N+1 requests, o backend lento |
| Renderizar listas grandes completas | Virtualización (react-window, react-virtualized) |
| Ignorar re-renders innecesarios | React DevTools Profiler para ver qué re-renderiza y por qué |

---

[[Home|← Home]]
