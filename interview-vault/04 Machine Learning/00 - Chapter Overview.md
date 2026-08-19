# Chapter 4 — Machine Learning (Classical)

---

## The story

1. **Predict numbers** — linear regression ([[01 - Linear Regression]])
2. **Predict classes** — logistic regression ([[02 - Logistic Regression]])
3. **Split with rules** — decision trees ([[03 - Decision Trees]])
4. **Ensemble & neighbors** — random forest, KNN ([[04 - Random Forest and KNN]])
5. **Find clusters** — K-means (unsupervised) ([[05 - K-Means]])
6. **Max-margin classifier** — SVM ([[06 - Support Vector Machines]])
7. **Engineer features** — transforms, encoding ([[07 - Feature Engineering]])
8. **Fight overfitting** — bias–variance in practice ([[08 - Overfitting]])
9. **Imbalanced labels** — real-world skew ([[09 - Class Imbalance]])
10. **Boost vs bag** — how ensembles differ ([[10 - Boosting vs Bagging]])

---
![[Pasted image 20260730072418.png]]
## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | Linear regression | [[01 - Linear Regression]] |
| 2 | Logistic regression | [[02 - Logistic Regression]] |
| 3 | Decision trees | [[03 - Decision Trees]] |
| 4 | Random Forest & KNN | [[04 - Random Forest and KNN]] |
| 5 | K-Means | [[05 - K-Means]] |
| 6 | SVM | [[06 - Support Vector Machines]] |
| 7 | Feature engineering | [[07 - Feature Engineering]] |
| 8 | Overfitting | [[08 - Overfitting]] |
| 9 | **Class imbalance** | [[09 - Class Imbalance]] |
| 10 | **Boosting vs bagging** | [[10 - Boosting vs Bagging]] |

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Gradient boosting** | XGBoost/LightGBM still king on tabular |
| **AutoML** | Feature tools + HPO for baselines |
| **Interpretability** | SHAP for regulated industries |

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| "High R² on train = good" | Check **test** R² / RMSE |
| "Linear regression for classification" | Use **logistic** or other classifiers |
| "Random Forest always beats one tree" | RF reduces variance; still tune depth |
| "k-means gives global optimum" | **Restart** with different seeds |
| "SVM always needs kernel" | Linear SVM fine for high-dimensional sparse text |
| "Normalize after train-test split wrong order" | Split → fit scaler on train |
| "Correlation features = causation" | Feature importance ≠ causal |

---

**Next chapter:** [[05 Deep Learning/00 - Chapter Overview]] (bias–variance → regularization)

[[Home|← Home]]
