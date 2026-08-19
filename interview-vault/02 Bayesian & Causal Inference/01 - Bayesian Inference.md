# Bayesian Inference

**Prev:** [[02 Bayesian & Causal Inference/00 - Chapter Overview]] · **Next:** [[02 - Priors and Posteriors Practical]]

---

## In plain English

You start with a **belief** (prior). You see **data**. You update to a new belief (posterior). That's Bayesian thinking — probability describes **uncertainty about parameters**, not just long-run frequencies.

---

## Interview one-liner

**Posterior ∝ Likelihood × Prior** — combine what the data say with what you believed before.

---

## Bayes' rule

$$P(\theta \mid \mathcal{D}) = \frac{P(\mathcal{D} \mid \theta)\, P(\theta)}{P(\mathcal{D})}$$

$$P(\theta \mid \mathcal{D}) \propto P(\mathcal{D} \mid \theta)\, P(\theta)$$

| Term | Meaning | Practical |
|------|---------|-----------|
| $P(\theta)$ | **Prior** | Expert knowledge, historical data, weak default |
| $P(\mathcal{D} \mid \theta)$ | **Likelihood** | How well θ explains observed data |
| $P(\theta \mid \mathcal{D})$ | **Posterior** | Updated belief after data |
| $P(\mathcal{D})$ | Evidence | Normalizer (often hard — use MCMC or conjugate forms) |

---

## Classic interview example (base rate)

- Disease prevalence: 1% → $P(\text{sick}) = 0.01$
- Test sensitivity: 90% → $P(+ \mid \text{sick}) = 0.9$
- False positive: 10% → $P(+ \mid \text{healthy}) = 0.1$

$$P(\text{sick} \mid +) = \frac{0.9 \times 0.01}{0.9 \times 0.01 + 0.1 \times 0.99} \approx 8.3\%$$

**Trap:** "Test is 90% accurate so positive means 90% sick." **Wrong** — rare disease dominates.

---

## When to use Bayesian (pragmatic)

| Situation | Why Bayesian |
|-----------|--------------|
| Small sample size | Prior stabilizes estimates |
| Sequential data | Update posterior as new data arrive |
| Need full uncertainty | Posterior distribution, not just point estimate |
| A/B tests with stopping rules | Frequentist p-values can mislead; Bayesian more coherent |
| Hierarchical models | Partial pooling across groups (e.g. hospitals, stores) |

---

## Common traps

| Trap | Correct |
|------|---------|
| "Subjective = unscientific" | Priors can be **weak**, sensitivity analysis shows robustness |
| "Bayesian always better" | Frequentist tools are fine with large clean RCT data |
| Ignore prior in reporting | State prior assumptions explicitly |

---

## 30-second interview answer

> "I use Bayes when I need to combine prior knowledge with limited data and report uncertainty as a distribution. The key equation is posterior proportional to likelihood times prior. The classic trap is ignoring base rates — a positive test on a rare condition still often means the patient is healthy."

---

**Next:** [[02 - Priors and Posteriors Practical]]
