# Descriptive Statistics

**Prev:** [[01 Statistics & Probability/00 - Chapter Overview]] · **Next:** [[02 - Probability Distributions]]

---

## Interview one-liner

Summarize data with **location** (where values sit) and **spread** (how much they vary). Choose mean vs median based on skew and outliers.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Central tendency

| Measure | Formula | Use when |
|---------|---------|----------|
| **Mean** $\bar{x}$ | $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$ | Symmetric data, no heavy outliers |
| **Median** | Middle value after sorting | Skewed data, outliers (income, house prices) |
| **Mode** | Most frequent value | Categorical or multimodal data |

**When mean is misleading:** long right tail → mean pulled up; median is more representative.

---

## Dispersion

| Measure | Formula | Notes |
|---------|---------|-------|
| **Variance** $s^2$ | $\frac{1}{n-1}\sum_i (x_i - \bar{x})^2$ | Squared units |
| **Std dev** $s$ | $\sqrt{s^2}$ | Same units as $x$ |
| **MAD (L1)** | median$(\|x_i - \text{median}(x)\|)$ | Robust to outliers |
| **IQR** | $Q_3 - Q_1$ | Box-plot spread; robust |

**Kurtosis:** tail heaviness. High kurtosis → more extreme values than Normal; std dev alone can understate risk.

---

## Visualizations (when to use)

| Plot | Shows | Use for |
|------|--------|---------|
| Histogram | Frequency distribution | Continuous variable shape |
| Box plot | Median, IQR, outliers | Compare groups |
| Scatter | $(x, y)$ pairs | Correlation, trends |
| Bar chart | Category counts | **Discrete** categories only |
| CDF | $P(X \le x)$ | Percentiles, comparing distributions |

**Multimodal:** more than one peak → mixture of sub-populations (e.g. two customer segments).

---

## Variables

| Symbol | Meaning |
|--------|---------|
| $n$ | Sample size |
| $x_i$ | $i$-th observation |
| $\bar{x}$ | Sample mean |

---

**Next:** [[02 - Probability Distributions]]
