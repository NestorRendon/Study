# PCA & Factor Analysis

**Prev:** [[08 - Cross Validation]] · **Next:** [[03 Mathematics/00 - Chapter Overview]]

---

## Interview one-liner

**PCA** finds orthogonal directions of **maximum variance** (dimensionality reduction). **Factor analysis** models observed variables as linear functions of fewer **latent factors** (interpret structure in correlations).

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## PCA

![[Pasted image 20260723080713.png|650]]
Given centered data matrix $\mathbf{X}$ ($n \times p$):

1. Compute covariance $\mathbf{S} = \frac{1}{n-1}\mathbf{X}^T\mathbf{X}$.
2. Eigen-decompose: $\mathbf{S} = \mathbf{V}\mathbf{\Lambda}\mathbf{V}^T$.
3. Project: $\mathbf{Z} = \mathbf{X}\mathbf{V}_k$ (first $k$ eigenvectors).

| Symbol | Meaning |
|--------|---------|
| $p$ | Original features |
| $k$ | Kept components ($k \ll p$) |
| Explained variance ratio | $\lambda_i / \sum_j \lambda_j$ |

**Use:** visualization, noise reduction, speed up downstream models, multicollinearity.

![[Pasted image 20260723080843.png]]
---

## Factor analysis (vs PCA)

| | PCA | Factor analysis |
|---|-----|-----------------|
| Goal | Max variance directions | Explain **correlation** structure |
| Noise | Part of components | Explicit uniqueness / error terms |
| Rotation | Optional | Often rotated for interpretability |



![[Pasted image 20260723081153.png]]
---

## Population comparison (related)

- **t-tests / ANOVA:** compare means across groups.
- **Non-parametric** (Mann-Whitney): when normality fails.

---

**Next chapter:** [[03 Mathematics/00 - Chapter Overview]]
