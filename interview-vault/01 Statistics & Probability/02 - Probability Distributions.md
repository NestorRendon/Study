# Probability Distributions

**Prev:** [[01 - Descriptive Statistics]] · **Next:** [[03 - Central Limit Theorem]]

---

## Interview one-liner

A distribution tells you **which values are likely** and how probability mass/spread is shaped. Pick the model that matches the data-generating process (counts → Poisson, waiting times → Exponential/Weibull, etc.).

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Continuous distributions

### Gaussian (Normal)

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

| Variable | Meaning |
|----------|---------|
| $\mu$ | Mean (center) |
| $\sigma$ | Standard deviation (spread) |

**Arises from:** CLT, measurement noise, many aggregated effects.

![[Pasted image 20260728204756.png]]
### Log-Normal

$\log X \sim \mathcal{N}(\mu, \sigma^2)$. **Right-skewed:** prices, incomes, latency.

### Weibull

Flexible shape for **failure times**, survival, reliability ($k$ = shape, $\lambda$ = scale).

### Uniform

All values in $[a,b]$ equally likely. Baseline / ignorance prior.

### Gamma / Beta

- **Gamma:** sum of exponentials, waiting times, Bayesian prior on rates.
- **Beta:** probabilities on $[0,1]$; conjugate prior for Binomial.

---

## Discrete distributions

### Binomial

$X \sim \text{Bin}(n, p)$: number of successes in $n$ independent trials.

$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

| Variable | Meaning |
|----------|---------|
| $n$ | Number of trials |
| $p$ | Success probability per trial |

### Poisson

$X \sim \text{Poi}(\lambda)$: count of events in fixed interval.

$$P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

**Key property:** $\mathbb{E}[X] = \text{Var}(X) = \lambda$. Use for rare events (defects per hour, clicks per minute).

---

## Sampling strategies

| Method | Idea | Trade-off |
|--------|------|-----------|
| Random | Equal chance per unit | Simple; poor spatial coverage |
| Stratified | Sample within subgroups | Lower variance; need strata labels |
| Systematic | Every $k$-th unit | Even coverage; bias if periodic pattern |

---

**Next:** [[03 - Central Limit Theorem]]
