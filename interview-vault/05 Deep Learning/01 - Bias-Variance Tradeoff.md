# Bias–Variance Tradeoff

**Prev:** [[04 Machine Learning/08 - Overfitting|ML — Overfitting]] · **Next:** [[02 - Learning Curves]]

---

## In plain English

**Bias** = your model is too simple and misses real patterns (underfitting).  
**Variance** = your model is too sensitive to which training rows you got (overfitting).  
You want both low — but fixing one often worsens the other.

---

## Interview one-liner

Total error = **bias² + variance + noise**. High train & test error → bias problem. Low train, high test → variance problem → **regularization** next.

---

## Decomposition

$$\text{Expected Error} = \text{Bias}^2 + \text{Variance} + \sigma^2_{\text{noise}}$$

| Term | Plain meaning | Symptom |
|------|---------------|---------|
| **Bias** | Wrong assumptions / too simple | Train **high**, test **high** |
| **Variance** | Fits noise in training set | Train **low**, test **high** |
| **Noise** | Randomness in $y$ | Cannot remove |

---

## Diagnosis cheat sheet

| Train error | Test error | Diagnosis | First actions |
|-------------|------------|-----------|---------------|
| High | High | **High bias** | More features, deeper model, less regularization |
| Low | High | **High variance** | More data, **L2/L1**, dropout, simpler model |
| Low | Low (close) | Good fit | Monitor drift; don't over-tune |

---

## Model complexity intuition

```
Error
  |     \___ total error
  |      \__/^\__
  |     /    |    \
  |    bias  |   variance
  |__________|____________ complexity →
              sweet spot
```

| Model | Bias | Variance |
|-------|------|----------|
| Linear (few features) | High | Low |
| Deep neural net | Low | High |
| Random Forest | Low | Medium |
| kNN ($k$=1) | Low | Very high |

---

## What to do next (reading order)

1. Confirm with [[02 - Learning Curves]]
2. If **variance** → [[04 - Regularization L1 and L2]] then [[05 - Dropout]]
3. If **bias** → more capacity, features, train longer (carefully)

---

## Common traps

| Trap | Correct |
|------|---------|
| "Low training loss = success" | Check **validation** |
| "More complex model always helps" | Can increase variance |
| "Regularization fixes underfitting" | Reg **increases bias** — for overfitting |
| "Bias-variance only for ML class" | Applies to **any** supervised learner |

---

## 30-second interview answer

> "I decompose error into bias and variance. If both train and validation errors are high, the model is too simple — I add capacity or features. If train is low but validation is high, I'm overfitting — I add data, regularization with L2, dropout, or early stopping. The irreducible part is noise."

---

**Next:** [[02 - Learning Curves]] → [[04 - Regularization L1 and L2]]
