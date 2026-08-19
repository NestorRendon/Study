# Mathematical Optimization

**Prev:** [[12 Optimization & Simulation/00 - Chapter Overview]] · **Next:** [[02 - Mixed Integer Programming]]

---

## General form

$$\min_{\mathbf{x}} f(\mathbf{x}) \quad \text{s.t.} \quad g_i(\mathbf{x}) \le 0,\; h_j(\mathbf{x}) = 0$$

| Symbol | Meaning |
|--------|---------|
| $f$ | Objective (cost / loss to minimize) |
| $\mathbf{x}$ | Decision variables |
| $g_i, h_j$ | Constraints |

**ML connection:** training = minimize loss subject to optional constraints (e.g. fairness).

---

## Heuristics trade-off

| Exact solver | Heuristic |
|--------------|-----------|
| Optimal (given time) | Approximate, faster |
| Slow on large MIP | Scales to industry size |

**Interview:** heuristics sacrifice optimality guarantee for speed — document gap when it matters.

---

**Next:** [[02 - Mixed Integer Programming]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Heuristics always worse | Heuristics trade optimality for **speed** at scale |
