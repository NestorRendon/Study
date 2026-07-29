# Simulation Types

**Prev:** [[02 - Mixed Integer Programming]] · **Next:** [[13 Software Engineering & Python/00 - Chapter Overview|Software]]

---

| Type | Idea | DS use |
|------|------|--------|
| **Discrete-event** | System jumps between events in time | Queues, supply chain, operations |
| **Agent-based** | Many agents with local rules | Epidemics, markets, ecology |
| **System dynamics** | ODEs on aggregate stocks/flows | Policy modeling, churn |

**Discrete-event:** state constant between events; clock jumps to next event (efficient for sparse dynamics).

---

**Next chapter:** [[13 Software Engineering & Python/00 - Chapter Overview]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Heuristics always worse | Heuristics trade optimality for **speed** at scale |
