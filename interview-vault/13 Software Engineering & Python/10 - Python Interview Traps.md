# Python Interview Traps & Patterns

**Prev:** [[11 - PyTorch Essentials]] · **Next:** [[Home|Home]]

---

## Mutable default arguments

```python
# TRAP
def add(item, lst=[]):
    lst.append(item)
    return lst

add(1)  # [1]
add(2)  # [1, 2]  ← same list object!

# CORRECT
def add(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## `is` vs `==`

| | Use |
|---|-----|
| `==` | Equal **value** |
| `is` | Same **object** in memory (only for `None`, `True`, `False`) |

---

## List comprehension vs generator

```python
[x**2 for x in range(10**6)]   # list — all in memory
(x**2 for x in range(10**6))   # generator — lazy
```

---

## `*args` / `**kwargs`

```python
def f(a, b=0, *args, **kwargs):
    pass
# args = extra positional tuple
# kwargs = extra keyword dict
```

---

## Context managers

```python
with open("f.txt") as f:
    data = f.read()
# file closed automatically
```

---

## `__name__ == "__main__"`

Runs block only when script executed directly — not when imported as module.

---

## GIL (one sentence)

CPython **GIL** = one thread executes Python bytecode at a time → CPU-bound threads don't parallelize; use **multiprocessing** or native libs (NumPy releases GIL in C ops).

---

## DS-specific traps

| Trap | Correct |
|------|---------|
| Train/test leak via `fit` on full data | Pipeline: split → fit on train |
| `df.append` in loop | `pd.concat` list once |
| Pickle model from untrusted source | Security risk — trust source |
| Not setting `random_state` | Non-reproducible interviews/demo |

---

## Quick patterns interviewers like

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000)),
])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
```

---

[[Home|← Home]]
---

## Common traps

| Trap | Correct |
|------|---------|
| pandas iterrows for speed | Use vectorized ops or apply; iterrows is slow |
| SQL SELECT * in production | Select only needed columns; reduces shuffle in Spark too |
