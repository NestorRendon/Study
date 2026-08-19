# SVM vs Logistic Regression

|                     | SVM                   | Logistic Regression          |
| ------------------- | --------------------- | ---------------------------- |
| Objective           | Maximize margin       | Maximize likelihood          |
| Output              | Decision boundary     | Calibrated probabilities     |
| Outlier sensitivity | Low (only SVs matter) | High (all points contribute) |
| Non-linearity       | Kernel trick          | Feature engineering          |
| Scalability         | Poor (large n)        | Good                         |
| Interpretability    | Low (RBF)             | High                         |
