# Classification Metrics

Accuracy    = correct / total           → misleading on imbalanced data  
  
Precision   = TP / (TP + FP)           → "of predicted positives, how many real?"  
Recall      = TP / (TP + FN)           → "of real positives, how many caught?"  
F1          = 2 · P·R / (P + R)        → harmonic mean, balances both  
  
AUC-ROC     = area under TPR vs FPR curve  
              0.5 = random, 1.0 = perfect  
              Good for imbalanced classes, threshold-independent  
  
AUC-PR      = area under Precision-Recall curve  
              Better than ROC when positives are very rare  
**When to use what:**  
* Fraud detection → Recall (missing fraud is costly)  
* Spam filter → Precision (false positives annoy users)  
* Medical diagnosis → F1 or AUC-PR  
* Imbalanced classes → AUC-ROC or AUC-PR, never raw accuracy
