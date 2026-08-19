# Regression Metrics

**Prev:** [[00 - Chapter Overview]] · **Next:** [[02 - Classification Metrics]]

---

## Interview one-liner

Regression metrics all measure **distance between prediction and truth** — they differ in how harshly they punish *big* errors, and whether they're in the target's original units or a unitless percentage. Pick the one that matches which errors actually hurt in your business.

---

## In plain English

Say you're predicting house prices. Some days you're off by \$500, some days by \$50,000. A regression metric has to compress "here's every one of those misses" into one number — and the choice of metric decides whether that one \$50,000 miss dominates the score or gets averaged away.

*A quick refresher on the basics also lives at [[01 Statistics & Probability/07 - Regression Metrics]] — this note goes a level deeper, with more of the metrics you'll actually get asked about.*

---

## Notation

| Symbol | Meaning |
|--------|---------|
| $y_i$ | True value for point $i$ |
| $\hat{y}_i$ | Predicted value for point $i$ |
| $n$ | Number of data points |
| $\bar{y}$ | Mean of the true values |
| $p$ | Number of predictors (features) in the model |

---

## Core equations

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$$

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2 \qquad \text{RMSE} = \sqrt{\text{MSE}}$$

$$\text{MAPE} = \frac{100\%}{n}\sum_{i=1}^n \left|\frac{y_i - \hat{y}_i}{y_i}\right| \qquad \text{SMAPE} = \frac{100\%}{n}\sum_{i=1}^n \frac{|y_i - \hat{y}_i|}{(|y_i| + |\hat{y}_i|)/2}$$

$$R^2 = 1 - \frac{\sum_i (y_i - \hat{y}_i)^2}{\sum_i (y_i - \bar{y})^2} \qquad \text{Adjusted } R^2 = 1 - (1 - R^2)\frac{n - 1}{n - p - 1}$$

---

## What each one actually does

| Metric | What it punishes | Units | Real example |
|--------|----------------------|-------|----------------|
| **MAE** | Every error equally, linearly | Same as $y$ (e.g. dollars) | "On average, my price prediction is off by \$3,200" |
| **MSE / RMSE** | Big errors *much* harder (squared) — one huge miss dominates the score | MSE: squared units; RMSE: same as $y$ | Useful when a single catastrophic miss (predicting \$50k too low) is far worse than ten small ones |
| **MAPE** | Errors relative to the size of the true value | % (scale-free, comparable across products) | "My forecast is off by 8% on average" — comparable whether predicting a \$10 item or a \$10,000 item |
| **SMAPE** | Same idea as MAPE, but symmetric | % | Fixes MAPE's bias toward *under*-prediction, and is more stable near small $y$ |
| **$R^2$** | Nothing directly — it's a **relative** score: how much better than just guessing the mean | Unitless, 0 to 1 (can go negative on test data) | "My model explains 82% of the variance in price" |
| **Adjusted $R^2$** | Same as $R^2$, but penalizes adding useless predictors | Unitless | Use when comparing models with a **different number of features** — plain $R^2$ never decreases from adding a feature, even a useless one |

---

## Worked example

True prices: $[100, 200, 300]$ (in \$k). Predictions: $[110, 180, 340]$.

Errors: $[-10, 20, -40]$

$$\text{MAE} = \frac{10 + 20 + 40}{3} = 23.3$$

$$\text{MSE} = \frac{10^2 + 20^2 + 40^2}{3} = \frac{100+400+1600}{3} = 700 \qquad \text{RMSE} = \sqrt{700} \approx 26.5$$

Notice **RMSE (26.5) > MAE (23.3)** — that gap is exactly the signature of one large error (the 40) being squared and dominating. If your errors were all the same size, MAE and RMSE would be equal.

---

## Which one should I report?

| Situation | Use |
|-----------|-----|
| Stakeholders need "typical error in dollars" | MAE |
| A few huge misses are much worse than many small ones (e.g. inventory shortfalls) | RMSE |
| Comparing forecast accuracy across products at very different scales | MAPE / SMAPE |
| "How much of the variation did my model actually capture?" | $R^2$ |
| Comparing two models with different numbers of features | Adjusted $R^2$ |
| Training loss function (needs to be differentiable and robust) | Often **Huber loss** — behaves like MSE for small errors, MAE for large ones, so outliers don't dominate training the way plain MSE does |

---

## Common traps

| Trap | Why it's wrong | What to say instead |
|------|------------------|----------------------|
| Reporting only $R^2$ | Says nothing about the actual size of errors, in real units, and can be misleadingly high with autocorrelated data | "I'd pair $R^2$ with RMSE or MAE for an interpretable error size" |
| Using MAPE with values near zero | Division by a near-zero $y_i$ blows up or becomes undefined | "I'd use SMAPE or MAE instead when the target can be near zero" |
| Comparing RMSE across two different datasets | RMSE is in the target's units — not comparable if the targets have different scales | "I'd normalize first, or compare MAPE / $R^2$ instead" |
| Assuming lower RMSE always means a better model for the business | RMSE optimizes for squared error, which may not match the real cost function (e.g. underpredicting inventory might cost more than overpredicting) | "I'd check whether the errors are costly asymmetrically, and consider a custom loss" |

---

**Next:** [[02 - Classification Metrics]]
