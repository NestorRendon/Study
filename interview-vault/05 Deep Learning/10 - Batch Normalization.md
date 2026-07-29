# Batch Normalization

**Prev:** [[09 - Batch Size vs Learning Rate]] · **Next:** [[11 - RNN LSTM and GRU]]

---

## Interview one-liner

Normalize activations **within each mini-batch** to stabilize training — allows higher learning rates and acts as mild regularization.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Per feature (simplified)

$$\hat{x} = \frac{x - \mu_{\text{batch}}}{\sqrt{\sigma^2_{\text{batch}} + \epsilon}}$$

$$y = \gamma \hat{x} + \beta$$

| Parameter | Learned? | Role |
|-----------|----------|------|
| $\gamma, \beta$ | Yes | Restore representational capacity |
| $\mu, \sigma$ | From batch (train) | Normalize |

**Inference:** use running averages of $\mu, \sigma$ from training.

---

## Benefits

- Reduces internal covariate shift
- Smoother loss landscape
- Often faster convergence

**Layer norm** (transformers): normalize across features per token instead of batch.

---

**Next:** [[11 - RNN LSTM and GRU]]
