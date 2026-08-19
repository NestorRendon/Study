# What Logistic Regression Actually Does

Logistic regression models the **probability** of a class, not a hard boundary. It finds the linear decision boundary that best separates classes *in probability space*:  
  
  
P(y=1 | x) = σ(w·x + b) = 1 / (1 + e^(-w·x - b))  
It doesn't need perfect separation — it needs a **linear relationship between features and log-odds**:  
  
  
log(P(y=1) / P(y=0)) = w·x + b     ← this is what must be linear
