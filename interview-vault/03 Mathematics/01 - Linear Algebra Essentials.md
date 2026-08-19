# Linear Algebra Essentials

**Prev:** [[03 Mathematics/00 - Chapter Overview]] · **Next:** [[02 - Similarity Correlation and Convolution]]

---

## Interview one-liner

ML is mostly **matrix operations**: features as vectors, datasets as matrices, weights as parameters to optimize.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Core objects

| Object | Shape | Role in ML |
|--------|-------|------------|
| Vector $\mathbf{x}$ | $p \times 1$ | One sample, $p$ features |
| Matrix $\mathbf{X}$ | $n \times p$ | $n$ samples |
| Weight $\mathbf{w}$ | $p \times 1$ | Linear model parameters |

**Linear prediction:** $\hat{y} = \mathbf{w}^T\mathbf{x} + b$

---

## Key operations

| Operation | Formula / fact |
|-----------|----------------|
| Dot product | $\mathbf{a}^T\mathbf{b} = \sum_i a_i b_i$ → cosine, RAG: [[02 - Similarity Correlation and Convolution]] |
| Matrix multiply | $(\mathbf{AB})_{ij} = \sum_k A_{ik}B_{kj}$ |
| Identity $\mathbf{I}$ | $\mathbf{A}\mathbf{I} = \mathbf{A}$ |
| Inverse $\mathbf{A}^{-1}$ | $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$ (if invertible) |
| Determinant | Volume scaling; $\det(\mathbf{A})=0$ → singular |

**Systems:** $\mathbf{A}\mathbf{x} = \mathbf{b}$ → OLS solution involves $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$ when full rank.

![[Pasted image 20260520080042.png]]

![[Pasted image 20260520080335.png]]
---
![[Pasted image 20260520080503.png]]
## Chain rule (preview for backprop)

If $L = f(g(\mathbf{w}))$, then $\frac{\partial L}{\partial \mathbf{w}} = \frac{\partial L}{\partial g}\frac{\partial g}{\partial \mathbf{w}}$.

---

**Next:** [[02 - Similarity Correlation and Convolution]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Gradient = derivative of loss only | Gradient is vector of partial derivatives; points uphill |
| Convex = always global minimum in DL | Deep nets are non-convex; convexity matters more for linear models |
