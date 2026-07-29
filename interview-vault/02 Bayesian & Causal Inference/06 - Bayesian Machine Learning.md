# Bayesian Machine Learning (Brief)

**Prev:** [[05 - Structure Learning]] · **Next:** [[12 Optimization & Simulation/00 - Chapter Overview]]

---

## In plain English

Instead of one best weight vector, maintain a **distribution over weights** — predictions include uncertainty (useful in medicine, finance).

---

## Examples

| Method | Idea |
|--------|------|
| **Bayesian linear regression** | Posterior on weights |
| **Gaussian Processes** | Distribution over functions; great for small $n$ regression |
| **Bayesian neural nets** | Posterior on weights (expensive — MCMC / variational) |
| **Thompson sampling** | Bayesian bandits for A/B / ads |

---

## Uncertainty types

| | Aleatoric | Epistemic |
|---|-----------|-----------|
| Source | Noise in data | Lack of knowledge |
| Example | Sensor noise | "Never saw this region of input space" |
| Reducible? | No | Yes (more data) |

**Interview:** neural nets often overconfident — Bayesian / ensembles / calibration help.

---

## Common traps

| Trap | Correct |
|------|---------|
| "Softmax probability = true confidence" | Calibrate with temperature scaling / isotonic |
| Bayesian = always slow | GPs and conjugate models can be fast |

---

**Next chapter:** [[12 Optimization & Simulation/00 - Chapter Overview]]
