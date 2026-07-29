# Python for Data Science

**Prev:** [[00 - Chapter Overview]] · **Next:** [[02 - Git Essentials]]

---
![[Pasted image 20260520085004.png]]

## Core libraries

| Library | Role |
|---------|------|
| **NumPy** | Arrays, linear algebra |
| **pandas** | Tables, joins, groupby |
| **PyTorch** | Deep learning — tensors, autograd, GPU ([[11 - PyTorch Essentials]]) |
| **scikit-learn** | Classical ML pipelines |
| **matplotlib / seaborn** | Static plots |
| **plotly / bokeh** | Interactive viz |

---

## Types (interview)

| Type | Mutable | Use |
|------|---------|-----|
| list | Yes | Sequences |
| dict | Yes | Key–value |
| tuple | No | Fixed records |
| set | Yes | Unique elements |
| `ndarray` | Yes | Numeric tensors |
| `DataFrame` | Yes | Tabular data |

**Aliasing:** two names, same object → mutation side effects. Copy with `.copy()`.

---

## Engineering habits

- `if __name__ == "__main__":` — script vs import
- **venv / conda / uv** — isolate dependencies
- Context managers (`with`) for files/DB connections
- Generators for large data streams
- Write **pure functions** as LLM tools (clear I/O)

---

## Interview coding drills (4 classics)

Practice without libraries first, then with `collections` / `heapq` where noted.

### 1. Two Sum — find indices with target sum

**Prompt:** Given `nums` and `target`, return indices of two numbers that add to `target` (exactly one solution).

```python
def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    raise ValueError("no pair")

# O(n) time, O(n) space
```

**Trap:** Returning values instead of indices; nested loops O(n²) when hash map is expected.

---

### 2. Top-K frequent elements

**Prompt:** Return the `k` most frequent integers in `nums`.

```python
from collections import Counter
import heapq

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    # min-heap of size k on frequency
    return [x for x, _ in heapq.nlargest(k, counts.items(), key=lambda t: t[1])]

# Alternative: Counter.most_common(k)
```

**Trap:** Sorting full unique list O(u log u) when heap is O(n log k).

---

### 3. Precision, recall, F1 from label lists

**Prompt:** Implement metrics for binary classification (`1` = positive).

```python
def precision_recall_f1(y_true: list[int], y_pred: list[int]) -> dict[str, float]:
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)

    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
    return {"precision": prec, "recall": rec, "f1": f1}
```

**Trap:** Using accuracy on imbalanced data; dividing by zero when no predicted positives.

---

### 4. Train / test split (no sklearn)

**Prompt:** Split rows into train and test with fraction `test_size`, optional `random_state`.

```python
import random

def train_test_split(
    rows: list,
    test_size: float = 0.2,
    random_state: int | None = None,
) -> tuple[list, list]:
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1")
    rng = random.Random(random_state)
    idx = list(range(len(rows)))
    rng.shuffle(idx)
    n_test = int(len(rows) * test_size)
    test_idx = set(idx[:n_test])
    train = [rows[i] for i in range(len(rows)) if i not in test_idx]
    test = [rows[i] for i in test_idx]
    return train, test
```

**Trap:** Splitting after scaling on full data — split **first**, then fit transforms on train only.

---
#### Exercise 2 — Vectorized distance matrix

**Task:** Given two sets of 2D points `A (shape 5,2)` and `B (shape 3,2)`, compute the Euclidean distance between every pair — output shape should be `(5, 3)`. No loops.

python

```python
A = np.random.rand(5, 2)
B = np.random.rand(3, 2)

# Your solution here
```

**Solution:**

python

```python
# Expand dims to enable broadcasting
# A[:,None,:] → (5,1,2)
# B[None,:,:] → (1,3,2)
diff = A[:, None, :] - B[None, :, :]  # (5,3,2)
distances = np.sqrt((diff ** 2).sum(axis=2))  # (5,3)

print(distances.shape)  # (5, 3)
```

#### Exercise 3 — Vectorized softmax

**Task:** Implement softmax over a batch of logits `(batch_size, num_classes)` in a numerically stable way, without loops.

python

```python
logits = np.array([
    [2.0, 1.0, 0.1],
    [0.5, 2.5, 1.0],
    [1.0, 1.0, 3.0],
])

# Your solution here
```

**Solution:**

python

```python
def softmax(x):
    # Subtract max per row for numerical stability (prevents exp overflow)
    x_shifted = x - x.max(axis=1, keepdims=True)  # (batch, classes)
    exp_x = np.exp(x_shifted)
    return exp_x / exp_x.sum(axis=1, keepdims=True)

probs = softmax(logits)
print(probs)
print(probs.sum(axis=1))  # [1. 1. 1.] — each row sums to 1
```

**Key interview point:** Always mention `keepdims=True` — without it the shape collapses and broadcasting breaks. And always mention the numerical stability trick (`- max`).

---

#### Exercise 4 — Vectorized one-hot encoding

**Task:** Convert an integer label array `[2, 0, 1, 2, 0]` into a one-hot matrix of shape `(5, 3)`. No loops, no sklearn.

python

```python
labels = np.array([2, 0, 1, 2, 0])
num_classes = 3

# Your solution here
```

**Solution:**

python

```python
# Method 1 — eye indexing (cleanest)
one_hot = np.eye(num_classes)[labels]
print(one_hot)
# [[0. 0. 1.]
#  [1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [1. 0. 0.]]

# Method 2 — zeros + arange (shows deeper understanding)
one_hot2 = np.zeros((len(labels), num_classes))
one_hot2[np.arange(len(labels)), labels] = 1
```

**Why it matters:** One-hot encoding is needed before cross-entropy loss. Knowing both methods shows you understand NumPy indexing deeply.

---

#### Exercise 5 — Vectorized batch cross-entropy loss

**Task:** Given a batch of predicted probabilities and true one-hot labels, compute the mean cross-entropy loss. No loops.

python

```python
y_true = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])

y_pred = np.array([
    [0.8, 0.1, 0.1],
    [0.2, 0.6, 0.2],
    [0.1, 0.2, 0.7],
])

# Your solution here
```

**Solution:**

python

```python
def cross_entropy(y_true, y_pred, eps=1e-9):
    # Clip predictions to avoid log(0)
    y_pred = np.clip(y_pred, eps, 1 - eps)

    # Element-wise: y_true * log(y_pred) → sum across classes → mean across batch
    per_sample_loss = -np.sum(y_true * np.log(y_pred), axis=1)  # (batch,)
    return per_sample_loss.mean()

loss = cross_entropy(y_true, y_pred)
print(f"Loss: {loss:.4f}")  # Loss: 0.3227
```

**Key interview points to mention:**

- `np.clip` prevents `log(0) = -inf` which would break training
- `axis=1` sums across classes, not across the batch
- This is exactly what `nn.CrossEntropyLoss` does internally in PyTorch


## Common traps

| Trap | Correct |
|------|---------|
| pandas iterrows for speed | Use vectorized ops or apply; iterrows is slow |
| SQL SELECT * in production | Select only needed columns; reduces shuffle in Spark too |
| Mutable default `def f(x, lst=[])` | Use `lst=None` and create inside |




---

**Next:** [[02 - Git Essentials]]
