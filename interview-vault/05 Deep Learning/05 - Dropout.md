# Dropout

**Prev:** [[04 - Regularization L1 and L2]] · **Next:** [[06 - Early Stopping]]

---

## Interview one-liner

**Dropout** is regularization for neural nets: randomly zero neurons during training so no single unit memorizes the data. Works **after** you understand bias–variance — it reduces **variance**.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Training

Each neuron active with probability $p$ (e.g. $p = 0.8$ means drop rate 0.2).

$$\tilde{h}_i = \begin{cases} h_i / p & \text{with prob } p \\ 0 & \text{with prob } 1-p \end{cases}$$

(Inverted dropout: scale activations so inference needs no scaling.)

---

## Inference

Use **all** neurons; weights already scaled during training (inverted dropout) or multiply outputs by $p$.

---

## Why it works

- Prevents **co-adaptation** of neurons
- Approximates **ensemble** of thinned networks
- Reduces overfitting (variance)

| Typical $p$ | Drop rate |
|-------------|-----------|
| Hidden layers | 0.2 – 0.5 |
| Input layer | Lower or none |
| Final layer | Often none |

**Avoid:** tiny datasets only, or when model already underfits.

---

**Next:** [[06 - Early Stopping]]
