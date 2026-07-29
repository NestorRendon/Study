# Convexity

**Prev:** [[04 - Gradient Descent]] · **Next:** [[06 - Softmax Function]]

---

## Interview one-liner

A **convex** loss has one global minimum; gradient descent is guaranteed to find it. **Deep nets are non-convex** but still train well — many good minima and SGD noise help.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Convex function

$$f(\lambda \mathbf{a} + (1-\lambda)\mathbf{b}) \le \lambda f(\mathbf{a}) + (1-\lambda)f(\mathbf{b}), \quad \lambda \in [0,1]$$

Graph lies **below** any chord → single bowl-shaped minimum.

---

## Gradient descent & convexity

| Setting | Guarantee |
|---------|-----------|
| Convex + smooth | GD converges to global min (right $\eta$) |
| Non-convex | Local minima, saddle points possible |

**When convexity matters less:** large over-parameterized nets (transformers, CNNs) — empirical success despite non-convexity.

---

## Failure modes (non-convex / bad conditioning)

| Issue | Effect |
|-------|--------|
| Local minima | Stuck in suboptimal basin |
| Saddle points | Slow escape in high-D |
| Poor conditioning | Zig-zag updates |

**Fixes:** Adam, learning rate schedule, batch normalization → see Deep Learning chapter.

---

**Next chapter:** [[04 Machine Learning/00 - Chapter Overview]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Gradient = derivative of loss only | Gradient is vector of partial derivatives; points uphill |
| Convex = always global minimum in DL | Deep nets are non-convex; convexity matters more for linear models |
