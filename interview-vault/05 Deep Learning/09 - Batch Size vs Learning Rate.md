# Batch Size vs Learning Rate

**Prev:** [[08 - Optimizers SGD Adam]] · **Next:** [[10 - Batch Normalization]]

---

## Interview one-liner

**Batch size** and **learning rate** are coupled: larger batches give lower-noise gradients → often need larger $\eta$. Wrong pairing causes slow training or divergence.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Trade-offs

| Batch size | Gradient noise | Typical $\eta$ | Throughput |
|------------|----------------|----------------|------------|
| Small | High | Smaller | More updates, less parallel |
| Large | Low | Larger | GPU-efficient, fewer updates |

**Linear scaling rule (heuristic):** if batch ×$k$, try $\eta \times k$ (up to a point).

---

## Practical guidance

- Start with defaults (e.g. Adam $\eta = 10^{-3}$, batch 32–128).
- If loss diverges → lower $\eta$.
- If loss flat → higher $\eta$ or check data pipeline.
- Use learning rate **warmup** + **decay** for transformers.

---

**Next:** [[10 - Batch Normalization]]
