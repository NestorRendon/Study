# Gradients & Partial Derivatives

**Prev:** [[02 - Similarity Correlation and Convolution]] · **Next:** [[04 - Gradient Descent]]

---

## Partial derivative

$$\frac{\partial f}{\partial x_i}$$

Rate of change of $f$ w.r.t. $x_i$ while **other variables are fixed**.

---

## Gradient

For scalar $f(\mathbf{w})$ with $\mathbf{w} \in \mathbb{R}^p$:

$$\nabla f(\mathbf{w}) = \begin{bmatrix} \frac{\partial f}{\partial w_1} \\ \vdots \\ \frac{\partial f}{\partial w_p} \end{bmatrix}$$

| Symbol | Meaning |
|--------|---------|
| $\nabla f$ | Gradient vector (direction of steepest **ascent**) |
| $-\nabla f$ | Direction of steepest **descent** |

**In ML:** loss $L(\mathbf{w})$ → update weights opposite to gradient.

---

## Common derivatives

| Function | Derivative |
|----------|------------|
| $\frac{1}{2}(y - \mathbf{w}^T\mathbf{x})^2$ w.r.t. $\mathbf{w}$ | $-(y - \mathbf{w}^T\mathbf{x})\mathbf{x}$ |
| $\sigma(z) = \frac{1}{1+e^{-z}}$ | $\sigma(z)(1-\sigma(z))$ |
| $\| \mathbf{w} \|_2^2$ | $2\mathbf{w}$ |

---

## Jacobian & Hessian (senior topics)

| Object | Order | Use |
|--------|-------|-----|
| **Jacobian** $\mathbf{J}$ | First, vector-valued $f$ | Multi-output networks |
| **Hessian** $\mathbf{H}$ | Second | Curvature, Newton methods |

---

**Next:** [[04 - Gradient Descent]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Gradient = derivative of loss only | Gradient is vector of partial derivatives; points uphill |
| Convex = always global minimum in DL | Deep nets are non-convex; convexity matters more for linear models |
