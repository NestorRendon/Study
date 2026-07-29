# Gradient Descent

**Prev:** [[03 - Gradients and Partial Derivatives]] · **Next:** [[05 - Convexity]]

---

## In plain English

You have a **loss** $L(\mathbf{w})$ that measures error. The **gradient** $\nabla L$ points uphill. To train, walk **downhill**:

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L(\mathbf{w}_t)$$

| Symbol | Meaning |
|--------|---------|
| $\mathbf{w}$ | Parameters (weights) |
| $\eta$ | Learning rate — step size |
| $t$ | Iteration number |

![Gradient descent](assets/FA60656B-DCF4-4668-9B82-7CE3986F42A0.png)

---

## One iteration (training loop)

| Step | Input | Output |
|------|-------|--------|
| 1. Forward | data $\mathbf{x}$, labels $y$, current $\mathbf{w}$ | prediction $\hat{y}$, loss $L$ |
| 2. Backward | $L$ | gradients $\nabla L$ per parameter |
| 3. Update | $\mathbf{w}$, $\nabla L$, $\eta$ | new $\mathbf{w}$ |

Example: classifier → logits → **softmax** → probs → cross-entropy $L$ → gradients.

→ [[06 - Softmax Function]]

---

## Batch GD vs SGD vs mini-batch

| Method | Gradient uses | Cost per step | Gradient quality |
|--------|---------------|---------------|------------------|
| **Batch GD** | **All** $n$ training points | High | Exact, low noise |
| **SGD (classic)** | **1** random point | Very low | Noisy |
| **Mini-batch SGD** | **$B$** random points (e.g. 32) | Medium | Noisy but stable — **deep learning default** |

### Why "stochastic"?

Each step uses a **random subset** of data → gradient $\nabla L_{\text{batch}}$ is an **estimate** of the true full-data gradient. That randomness:

- makes each step **cheap**
- adds **noise** that can help escape bad local minima (in non-convex nets)

**Interview:** "SGD" in papers often means **mini-batch**, not literally one sample.

### Mini-batch update

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \cdot \frac{1}{B} \sum_{i \in \text{batch}} \nabla L_i(\mathbf{w}_t)$$

---

## Learning rate $\eta$

| $\eta$ too… | What you see | Fix |
|-------------|--------------|-----|
| **Large** | Loss jumps, NaN, diverges | Decrease $\eta$, warmup |
| **Small** | Loss creeps down slowly | Increase $\eta$ |
| Wrong for landscape | Zig-zag in valleys | Momentum, Adam, batch norm |

---

## Beyond vanilla GD (detail in DL chapter)

| Extension | What it adds |
|-----------|--------------|
| **Momentum** | Velocity — smoother path through noisy gradients |
| **RMSProp / Adam** | Different effective $\eta$ per parameter |
| **Weight decay** | Penalty on large weights ($L_2$) |

Full optimizers walkthrough: [[05 Deep Learning/08 - Optimizers SGD Adam]]

---

## Interview one-liner

> "Gradient descent updates weights opposite to the loss gradient; mini-batch SGD uses $B$ random examples per step for efficiency and is what powers virtually all deep learning training."

---

## Common traps

| Trap | Correct |
|------|---------|
| Gradient points to minimum | Points to **steepest ascent** — subtract for minimization |
| "SGD = full dataset" | **Stochastic** = subset (batch) of data |
| Zero gradient = optimum | Could be saddle point or plateau |

---

**Next:** [[05 - Convexity]]
