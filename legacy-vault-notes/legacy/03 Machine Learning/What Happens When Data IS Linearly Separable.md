# What Happens When Data IS Linearly Separable

This is actually a **problem**, not a benefit:  
  
  
If classes are perfectly separable →  
  weights w grow toward infinity  
  sigmoid pushes probabilities to 0 and 1  
  model never converges  
  coefficients are undefined (MLE doesn't exist)  
The optimizer keeps increasing weights forever trying to make the boundary sharper. You must use **regularization (L2)** to constrain this — which is why sklearn's LogisticRegression has C (inverse regularization) on by default.
