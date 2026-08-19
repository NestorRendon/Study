# Gradient Descent

[[MOC - Mathematics|← Mathematics]]

Iterative **first-order** optimizer: update parameters in the direction of steepest loss decrease.

![Gradient descent](assets/FA60656B-DCF4-4668-9B82-7CE3986F42A0.png)

| Method | Idea |
|--------|------|
| Batch | Full dataset per step |
| SGD | One sample per step |
| Mini-batch | Small batches (common in DL) |

**Optimizers:** Momentum, RMSProp, Adam.

## Convexity

Does **not** require convexity; convex problems have stronger guarantees. Less critical for large neural nets (many good minima, saddle points).

## Related

- [[Linear Regression]]
- [[Soft Requirement on Convexity]] (Transformers folder — consider moving)
