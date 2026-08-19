# Cross Validation

[[MOC - Statistics & Probability|← Statistics]]

Technique to estimate **generalization** by training on subsets and validating on held-out folds (k-fold, stratified k-fold, leave-one-out).

![Train/validation split](assets/23A616A6-E722-4A6C-8BAE-0B9F38B80FFA.webp)

## Data leakage

Using information in training that would **not** be available at prediction time (e.g. fitting scalers on the full dataset before splitting). Inflates metrics; fails in production.

**Always:** split first → fit preprocessing only on train → apply to val/test.

## Related

- [[Classification Metrics]]
- [[Overfitting]] (see Machine Learning notes)
