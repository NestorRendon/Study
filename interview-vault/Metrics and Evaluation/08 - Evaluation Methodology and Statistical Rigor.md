# Evaluation Methodology and Statistical Rigor

**Prev:** [[07 - Knowledge Graph and Embedding Metrics]] · **Next:** [[11 Computer Vision/00 - Chapter Overview|Computer Vision (Ch 11)]]

---

## Interview one-liner

A single number from a single test set isn't a result — it's a sample. Every metric in this chapter needs an answer to one more question before you trust it: **is this improvement real, or is it noise?**

---

## In plain English

Two models score 0.842 and 0.847 accuracy on your test set. Is model B actually better? If the test set has 200 examples, that 0.005 gap could easily flip on a different random sample of the same size — you can't tell from the point estimate alone. This note is about the machinery that turns "here's a number" into "here's a number, and here's how much I trust it."

---

## Splitting data correctly

| Split | Purpose | Rule |
|-------|---------|------|
| **Train** | Fit model parameters | Never touched for decisions |
| **Validation** | Tune hyperparameters, pick the best model/checkpoint | Touched many times — risk of overfitting *to the validation set itself* if you tune too much |
| **Test** | Final, one-time, honest estimate of real-world performance | Touched **once**, at the very end — if you go back and change the model after seeing the test score, it's no longer a valid test score |

**Full treatment of cross-validation (k-fold, stratified, time-series splits) is in [[01 Statistics & Probability/08 - Cross Validation]]** — the short version: k-fold CV replaces a single validation split with $k$ splits, averaged, giving a more stable estimate and, critically, a **spread** (standard deviation across folds) instead of just one number.

---

## Confidence intervals for a metric (bootstrapping)

Resample your test set **with replacement** $B$ times (e.g. $B=1000$), recompute the metric on each resample, and look at the distribution of results:

$$\hat{\theta}_b = \text{metric computed on bootstrap resample } b, \quad b = 1, \dots, B$$

$$\text{95% CI} = \left[\hat{\theta}_{(2.5\%)},\ \hat{\theta}_{(97.5\%)}\right] \quad \text{(the 2.5th and 97.5th percentiles of the } B \text{ resampled scores)}$$

This turns "accuracy = 0.847" into "accuracy = 0.847, 95% CI [0.81, 0.88]" — and if two models' confidence intervals overlap heavily, you don't have strong evidence one is actually better.

---

## Is the difference between two models real? (significance testing)

| Test | When to use | What it compares |
|------|-------------|-----------------------|
| **Paired t-test** | Comparing two models' scores on the *same* set of examples (e.g. per-fold accuracy from k-fold CV) | Whether the mean difference is significantly different from zero |
| **McNemar's test** | Comparing two *classifiers* on the exact same test set | Specifically looks at the examples where the two models **disagree** — ignores the ones both get right or both get wrong, which don't carry information about which model is better |
| **Bootstrap hypothesis test** | Any metric, no distributional assumptions needed | Resample and check how often model B beats model A by chance alone |

*The general hypothesis-testing machinery (p-values, significance levels, Type I/II error) is covered in [[01 Statistics & Probability/04 - Hypothesis Testing]] — this is that machinery applied specifically to comparing model metrics.*

---

## Always compare against a baseline

A metric means nothing in isolation — it means something relative to a baseline:

| Baseline | Example |
|----------|---------|
| **Dummy/majority-class predictor** | Always predict the most common class — if your fancy model barely beats this, something's wrong |
| **Simple heuristic** | "Predict yesterday's value" for a forecasting task |
| **Previous production model** | The real bar to clear — did the new model actually improve over what's already live? |
| **Human performance** (where available) | For some tasks (medical diagnosis, translation), this is the ceiling worth comparing against |

---

## The silent killer: data leakage

No statistical test saves you from this — it invalidates the metric before the math even starts.

| Leakage type | Example | Fix |
|---------------|---------|-----|
| **Train/test contamination** | Duplicate or near-duplicate rows end up in both splits | Deduplicate before splitting; group-aware splits (e.g. by user ID, not by row) |
| **Target leakage** | A feature that's only available *after* the outcome is known sneaks into training (e.g. "cancellation_reason" predicting churn) | Audit feature timing — would this value actually exist at prediction time? |
| **Preprocessing leakage** | Fitting a scaler/imputer on the full dataset *before* splitting | Fit only on train, apply to val/test |
| **Temporal leakage** | Random split on time-series data lets the model "see the future" | Split by time — train on the past, test on the future |

---

## Common traps

| Trap | Why it's wrong | What to say instead |
|------|------------------|----------------------|
| Reporting one test-set number with no spread | A single sample doesn't tell you if a competing model's difference is real | "I'd report a confidence interval (bootstrap or k-fold std) alongside the point estimate" |
| Tuning hyperparameters using the test set | The test set is no longer an honest, unseen estimate — it becomes a second validation set | "I'd only touch the test set once, at the very end" |
| "Model B is better, it scored 0.847 vs 0.842" with no significance test | A 0.5-point gap on a small test set is often just noise | "I'd run a paired significance test before claiming the difference is real" |
| Skipping a baseline comparison | A model can look impressive in isolation and still be barely better than guessing the majority class | "I'd always report a baseline number next to the model's score" |

---

**Next:** [[11 Computer Vision/00 - Chapter Overview|Computer Vision (Ch 11)]]
