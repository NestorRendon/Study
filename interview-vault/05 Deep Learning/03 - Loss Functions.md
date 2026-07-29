# Loss Functions

**Prev:** [[02 - Learning Curves]] · **Next:** [[04 - Regularization L1 and L2]]

---

## Interview one-liner

The loss $L$ is what optimization **minimizes**. Choose it to match the task: MSE for regression, cross-entropy for classification.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Regression

$$L_{\text{MSE}} = \frac{1}{n}\sum_i (y_i - \hat{y}_i)^2$$

$$L_{\text{MAE}} = \frac{1}{n}\sum_i |y_i - \hat{y}_i|$$

| Loss | Property |
|------|----------|
| MSE | Smooth, penalizes large errors heavily |
| MAE | Robust to outliers |

**$L_p$ distance:** generalization of above.

---

## Classification

**Binary cross-entropy** (one output + sigmoid):

$$L = -\frac{1}{n}\sum_i \left[y_i \log \hat{p}_i + (1-y_i)\log(1-\hat{p}_i)\right]$$

**Categorical cross-entropy** ($K$ classes) — model outputs logits $\mathbf{z}$, then **softmax** gives $\hat{p}$:

$$\hat{p}_k = \text{softmax}(z_k) = \frac{e^{z_k}}{\sum_j e^{z_j}}$$

$$L = -\frac{1}{n}\sum_i \sum_{k=1}^{K} y_{ik} \log \hat{p}_{ik}$$

For one-hot true class $c$: $L = -\log \hat{p}_c$ (only the correct class probability matters).

→ Full softmax intuition, examples, stability: [[03 Mathematics/06 - Softmax Function]]

---

## Why cross-entropy with softmax?

| Reason | Detail |
|--------|--------|
| **Probabilities** | Softmax outputs valid $P(\text{class})$ |
| **Maximum likelihood** | CE loss = negative log-likelihood of labels |
| **Gradients** | Strong push when model is confident but wrong |
| **Implementation** | Use `log_softmax` + NLLLoss in PyTorch |

Training flow: logits → softmax → loss → backward → **SGD/Adam** updates weights → [[08 - Optimizers SGD Adam]]

---

**Next:** [[04 - Regularization L1 and L2]] — the main tool when variance is high
