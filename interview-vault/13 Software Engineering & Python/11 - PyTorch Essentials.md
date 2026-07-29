# PyTorch Essentials

**Prev:** [[09 - Spark Essentials]] · **Next:** [[10 - Python Interview Traps]]

**Links:** [[06 - NumPy Cheatsheet]] · [[05 Deep Learning/08 - Optimizers SGD Adam]] · [[03 Mathematics/06 - Softmax Function]]

---

## In plain English

**PyTorch** = NumPy-like **tensors** on CPU/GPU + **automatic gradients** (autograd) + **neural network** building blocks (`torch.nn`). This is how most DL models are trained in research and industry.

---

## Tensor basics

```python
import torch

x = torch.tensor([1.0, 2.0, 3.0])           # from list
x = torch.zeros(3, 4)                       # shape 3×4
x = torch.randn(2, 3)                       # standard normal
x = torch.arange(0, 10, 2)                  # [0,2,4,6,8]

x.shape, x.dtype, x.device                  # metadata
```

| | NumPy | PyTorch |
|---|-------|---------|
| Object | `ndarray` | `Tensor` |
| GPU | No | `tensor.to("cuda")` |
| Gradients | No | `requires_grad=True` |
| DL modules | External | `torch.nn` built-in |

---

## Shapes & broadcasting

Same rules as NumPy — align trailing dimensions:

```python
a = torch.randn(32, 10)    # batch 32, features 10
b = torch.randn(10, 5)      # linear: 10 → 5
c = a @ b                   # (32, 5)  matrix multiply
```

| Op | Code |
|----|------|
| Reshape | `x.view(32, -1)` or `x.reshape(...)` |
| Transpose | `x.T` or `x.transpose(0, 1)` |
| Concat | `torch.cat([a, b], dim=1)` |
| Batch dim | usually `dim=0` |

---

## GPU

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
x = x.to(device)
```

**Interview:** move **model and data** to the same device before forward pass.

---

## Autograd (why PyTorch trains nets)

```python
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2
y.backward()                  # compute dy/dx
x.grad                        # tensor([4.])
```

| Concept | Meaning |
|---------|---------|
| `requires_grad=True` | track ops for gradient |
| `.backward()` | backprop from scalar loss |
| `.grad` | accumulated $\partial L / \partial x$ |
| `torch.no_grad()` | inference — no graph, less memory |

Training: loss must be a **scalar** for `.backward()` (or `loss.mean()`).

→ Math: [[03 Mathematics/03 - Gradients and Partial Derivatives]]

---

## `nn.Module` — define a model

```python
import torch.nn as nn
import torch.nn.functional as F

class MLP(nn.Module):
    def __init__(self, in_dim=784, hidden=128, n_classes=10):
        super().__init__()
        self.fc1 = nn.Linear(in_dim, hidden)
        self.fc2 = nn.Linear(hidden, n_classes)

    def forward(self, x):
        x = x.view(x.size(0), -1)      # flatten (B, 784)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)                # logits (B, 10)
        return x

model = MLP()
```

| Piece | Role |
|-------|------|
| `__init__` | layers with learnable weights |
| `forward` | computation graph |
| `model.parameters()` | all weights for optimizer |

---

## Training loop (mini-batch SGD)

```python
import torch.optim as optim

model = MLP().to(device)
optimizer = optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()   # softmax + CE inside

for epoch in range(num_epochs):
    model.train()
    for x_batch, y_batch in train_loader:
        x_batch, y_batch = x_batch.to(device), y_batch.to(device)

        optimizer.zero_grad()       # clear old gradients
        logits = model(x_batch)     # forward
        loss = criterion(logits, y_batch)
        loss.backward()             # backward
        optimizer.step()            # w <- w - eta * grad

    model.eval()
    with torch.no_grad():
        # validation...
```

| Step | Why |
|------|-----|
| `zero_grad()` | grads **accumulate** if you forget |
| `model.train()` / `eval()` | dropout/batchnorm behavior |
| `torch.no_grad()` | faster inference, no graph |

→ Optimizers: [[05 Deep Learning/08 - Optimizers SGD Adam]]

---

## DataLoader

```python
from torch.utils.data import DataLoader, TensorDataset

dataset = TensorDataset(X_tensor, y_tensor)
loader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2)

for x_b, y_b in loader:
    ...
```

| Arg | Effect |
|-----|--------|
| `batch_size` | Mini-batch $B$ |
| `shuffle=True` | Random batches each epoch |
| `num_workers` | Parallel data loading |

---

## Loss & softmax

```python
# Multi-class: logits (B, K) + integer labels (B,)
loss = nn.CrossEntropyLoss()(logits, y)

# Equivalent manual:
loss = F.cross_entropy(logits, y)   # log-softmax + NLL inside
```

Do **not** apply softmax before `CrossEntropyLoss` — it's included.

→ [[03 Mathematics/06 - Softmax Function]]

---

## Save / load

```python
torch.save(model.state_dict(), "model.pt")
model.load_state_dict(torch.load("model.pt", map_location=device))
```

**Interview:** save **`state_dict`** (weights), not whole object, for portability.

---

## Interview coding drills (4 classics)

### 1. Tensor shapes after one linear layer

```python
B, in_dim, out_dim = 32, 784, 10
x = torch.randn(B, in_dim)
layer = nn.Linear(in_dim, out_dim)
y = layer(x)
assert y.shape == (B, out_dim)
```

---

### 2. Manual training step (no loop)

```python
model = nn.Linear(5, 1)
x = torch.randn(8, 5)
y_true = torch.randn(8, 1)
opt = optim.SGD(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

opt.zero_grad()
y_pred = model(x)
loss = loss_fn(y_pred, y_true)
loss.backward()
opt.step()
```

---

### 3. Freeze backbone, train head only

```python
for param in backbone.parameters():
    param.requires_grad = False

optimizer = optim.Adam(head.parameters(), lr=1e-3)
```

**Use:** transfer learning / fine-tuning (LoRA is a smarter variant → [[07 LLM & Generative AI/05 - LoRA and PEFT]]).

---

### 4. Predict with `eval` + `no_grad`

```python
model.eval()
with torch.no_grad():
    logits = model(x_test.to(device))
    preds = logits.argmax(dim=1)
```

**Trap:** leaving `model.train()` during inference → dropout still random.

---

## Common traps

| Trap | Correct |
|------|---------|
| Forget `zero_grad()` | Gradients **sum** across steps |
| Softmax then `CrossEntropyLoss` | Pass **logits** only |
| Tensor on CPU, model on GPU | `.to(device)` both |
| `loss.backward()` on non-scalar | Use `.mean()` or `.sum()` |
| Huge graph in eval loop | Wrap inference in `torch.no_grad()` |
| `view` on non-contiguous tensor | Use `.reshape()` or `.contiguous()` |

---

## Interview one-liner

> "PyTorch tensors plus autograd give mini-batch training: forward → loss → backward → optimizer.step; `nn.Module` encapsulates layers, DataLoader feeds batches, and eval mode plus no_grad for inference."

---

**Next:** [[10 - Python Interview Traps]]
