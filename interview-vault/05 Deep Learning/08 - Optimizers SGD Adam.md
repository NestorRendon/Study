# Optimizers (SGD & Adam)

**Prev:** [[07 - Feature Scaling for Neural Nets]] · **Next:** [[09 - Batch Size vs Learning Rate]]

**Math background:** [[03 Mathematics/04 - Gradient Descent]] · [[03 Mathematics/06 - Softmax Function]] · **Code:** [[13 Software Engineering & Python/11 - PyTorch Essentials]]

---

## In plain English

Training = repeatedly compute **how wrong** the model is (loss), compute **gradients** (direction to improve), then **update weights**. An **optimizer** decides exactly how big each update step is.

**SGD** (stochastic gradient descent) = use a **small random subset** of data per step instead of the full dataset. **Adam** = SGD plus **adaptive** step sizes and **momentum** per parameter.

---

## The core update (all optimizers)

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \cdot \mathbf{g}_t$$

| Symbol | Meaning |
|--------|---------|
| $\mathbf{w}$ | All model parameters (weights, biases) |
| $\eta$ | Learning rate (global step size) |
| $\mathbf{g}_t$ | Gradient of loss w.r.t. $\mathbf{w}$ at step $t$ |
| $t$ | Training step (iteration) |

**Gradient descent** moves opposite to the gradient because the gradient points **uphill** on the loss.

---

## Batch GD vs SGD vs mini-batch

| Method | Gradient computed on | Steps per epoch | Noise |
|--------|----------------------|-----------------|-------|
| **Batch (full) GD** | Entire dataset ($n$ samples) | 1 | None — exact gradient |
| **True SGD** | **1** random sample | $n$ | High |
| **Mini-batch SGD** | **$B$** random samples (e.g. 32, 256) | $n / B$ | Medium — **DL default** |

When people say "SGD" in deep learning, they almost always mean **mini-batch SGD**.

### Why mini-batch?

| Benefit | Explanation |
|---------|-------------|
| **Speed** | GPU processes $B$ examples in parallel |
| **Memory** | Full dataset gradient may not fit in GPU RAM |
| **Generalization** | Noise in $\mathbf{g}_t$ can help escape sharp minima |
| **Frequent updates** | Many steps per epoch → faster progress |

### One training step (mini-batch SGD)

```
1. Sample mini-batch B = {(x_1, y_1), …, (x_B, y_B)}
2. Forward pass  → predictions ŷ
3. Compute loss L on the batch (e.g. cross-entropy + softmax)
4. Backward pass → gradients ∇L w.r.t. each weight
5. w ← w - η * ∇L
```

**Batch loss** (not full-dataset loss):

$$L_{\text{batch}} = \frac{1}{B} \sum_{i \in \text{batch}} L_i$$

Gradient is the average (or sum) of per-example gradients in the batch.

---

## SGD update (mini-batch)

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L_{\text{batch}}(\mathbf{w}_t)$$

| Hyperparameter | Typical | Effect |
|----------------|---------|--------|
| $\eta$ | $10^{-3}$ to $10^{-1}$ (problem-dependent) | Too large → diverge; too small → slow |
| $B$ | 32–512 (NLP often 32–128) | Larger $B$ → stabler gradient, more memory |

### Learning rate schedule (common with SGD)

| Schedule | Idea |
|----------|------|
| Step decay | Multiply $\eta$ by 0.1 every N epochs |
| Cosine | Smooth decay to near zero |
| Warmup | Small $\eta$ early (transformers) |

→ [[09 - Batch Size vs Learning Rate]]

---

## SGD with momentum

Plain SGD zig-zags in narrow valleys. **Momentum** accumulates velocity:

$$\mathbf{v}_{t+1} = \beta \mathbf{v}_t + \nabla L_{\text{batch}}$$
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \mathbf{v}_{t+1}$$

| Symbol | Typical | Role |
|--------|---------|------|
| $\beta$ | 0.9 | How much past gradient direction is kept |
| $\mathbf{v}$ | velocity | Smoothes noisy batch gradients |

**Intuition:** a ball rolling downhill — keeps going through small bumps.

**Nesterov momentum:** evaluate gradient at **lookahead** position — often slightly better.

---

## Adam (Adaptive Moment Estimation)

Tracks **two** moving averages per parameter:

| Moment | Tracks | Symbol |
|--------|--------|--------|
| 1st | mean of gradients (momentum-like) | $m_t$ |
| 2nd | mean of **squared** gradients (scale) | $v_t$ |

$$m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$$

Bias correction (early steps):

$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

| Hyperparameter | Default | Meaning |
|----------------|---------|---------|
| $\beta_1$ | 0.9 | Gradient momentum |
| $\beta_2$ | 0.999 | Squared-gradient memory |
| $\epsilon$ | $10^{-8}$ | Avoid divide by zero |

**Effect:** parameters with **large** typical gradients get **smaller** effective steps; parameters with small gradients get larger steps.

### AdamW (transformers / LLMs)

**Weight decay decoupled** from the adaptive step — $L_2$ penalty applied directly to weights, not mixed into $m_t, v_t$. Standard for BERT, GPT fine-tuning.

---

## Comparison table

| | Batch GD | Mini-batch SGD | SGD + momentum | Adam / AdamW |
|---|----------|----------------|----------------|--------------|
| Gradient noise | None | Medium | Medium | Medium |
| Per-param $\eta$ | Same | Same | Same | **Adaptive** |
| Tuning effort | Low | Medium | Medium | Often easier |
| Generalization (CV) | — | Good | Often **best** with care | Good |
| Default in NLP/LLM | — | Rare alone | Sometimes fine-tune | **AdamW** |

---

## When to use what

| Situation | Optimizer |
|-----------|-------------|
| Quick NLP / transformer training | **AdamW** |
| Image classification (ResNet) | SGD + momentum + schedule |
| Fine-tuning LLM (LoRA) | Often AdamW, low $\eta$ |
| Small tabular MLP | Adam |

---

## Link to softmax + loss

Classifier outputs logits $\mathbf{z}$ → **softmax** → $\mathbf{p}$ → **cross-entropy** loss → **backward** → $\mathbf{g}_t$ → optimizer updates $\mathbf{w}$.

→ [[03 Mathematics/06 - Softmax Function]] · [[05 Deep Learning/03 - Loss Functions]]

---

## Common traps

| Trap | Correct |
|------|---------|
| "SGD always uses one sample" | In DL, **mini-batch** is standard |
| "Adam always beats SGD" | SGD+momentum can generalize better on some vision tasks |
| Same $\eta$ when batch size ×2 | Often scale $\eta$ with batch size (linear scaling rule) |
| No learning rate schedule | Transformers usually need **warmup + decay** |
| Weight decay in Adam vs AdamW | Use **AdamW** for proper decoupled decay |

---

## Interview one-liner

> "Mini-batch SGD estimates the gradient on $B$ samples per step for speed and noise; momentum smooths updates; Adam adapts the step size per parameter using running means of $g$ and $g^2 — AdamW is the go-to for transformers."

---

**Next:** [[09 - Batch Size vs Learning Rate]]
