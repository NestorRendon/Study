# Mixed-Integer Programming (MIP)

**Prev:** [[01 - Mathematical Optimization]] · **Next:** [[03 - Simulation Types]]

---

## Interview one-liner

Some variables are **integer** (binary decisions, counts). MIP is NP-hard — solver speed depends on formulation quality.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Speed up solving

| Lever | Effect |
|-------|--------|
| Tighter constraints | Smaller feasible region → faster prune |
| Better variable bounds | Same |
| Simpler objective | Sometimes easier landscape |
| Good initial solution | Warm start helps heuristics |

**Interview:** "I'd first check if the formulation is tight — adding valid inequalities often beats changing the objective."

---

**Next:** [[03 - Simulation Types]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Heuristics always worse | Heuristics trade optimality for **speed** at scale |
