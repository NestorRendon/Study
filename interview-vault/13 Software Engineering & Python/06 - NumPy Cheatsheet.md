# NumPy Cheatsheet

**Prev:** [[05 - Agile for Data Science]] · **Next:** [[07 - Pandas Cheatsheet]]

---

## In plain English

NumPy = fast **arrays** and math on whole columns at once (vectorization). Foundation for pandas, sklearn, **PyTorch** ([[11 - PyTorch Essentials]]).

---

## Create arrays

```python
import numpy as np

np.array([1, 2, 3])
np.zeros((3, 4))          # 3×4 zeros
np.ones((2, 3))
np.arange(0, 10, 2)       # [0,2,4,6,8]
np.linspace(0, 1, 5)      # 5 evenly spaced
np.random.randn(1000)     # standard normal
np.random.seed(42)        # reproducibility
```

---

## Shape & reshape

```python
a.shape                   # (rows, cols)
a.reshape(4, 5)           # must match total size
a.flatten()
a.T                       # transpose
```

---

## Indexing (interview favorites)

```python
a[0]                      # first row
a[:, 0]                   # first column
a[a > 0]                  # boolean mask
a[[0, 2]]                 # fancy index rows
np.where(a > 0, 1, 0)     # ifelse vectorized
```

---

## Math (vectorized)

```python
a.mean(), a.std(), a.sum(axis=0)
np.dot(a, b)              # matrix multiply
a @ b                     # same (2D)
np.linalg.inv(A)          # inverse (careful: ill-conditioned)
np.linalg.norm(v)
```

---

## Broadcasting

```python
# (3,1) + (1,4) → (3,4) without explicit loops
col = np.array([[1], [2], [3]])
row = np.array([10, 20, 30, 40])
col + row
```

---

## Common traps

| Trap | Correct |
|------|---------|
| `for` loop over rows for math | **Vectorize** — 10–100× faster |
| `a.T` on 1D array | 1D transpose does nothing; reshape explicitly |
| `==` on floats | Use `np.isclose(a, b)` |
| View vs copy | Slicing may be a **view**; use `.copy()` if mutating |
| `np.array` of mixed types | Becomes `dtype=object` — slow |

---

## Interview one-liner

> "NumPy gives contiguous typed arrays and vectorized C-backed ops. I use boolean masking, broadcasting, and axis arguments instead of Python loops."

---

**Next:** [[07 - Pandas Cheatsheet]]
