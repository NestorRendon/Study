# 2. Cross-Entropy (Classification)

Cross-entropy loss is the standard loss function for classification tasks in machine learning, used to measure the difference between predicted probability distributions and true labels.   
  
**Binary Cross-Entropy**  
  
  
L = -[y·log(ŷ) + (1-y)·log(1-ŷ)]  
  
y = true label (0 or 1)    ŷ = predicted probability  
* Heavily penalizes confident wrong predictions (log blows up near 0)  
* **Use:** logistic regression, binary classifiers, last layer sigmoid  
**Categorical Cross-Entropy**  
  
  
L = -Σ yᵢ · log(ŷᵢ)       (sum over classes)  
* yᵢ is one-hot encoded, so only the true class term survives  
* **Use:** multi-class classification, last layer softmax  
**ELI5:** If you're 99% sure it's a cat and it's actually a dog, cross-entropy punishes you enormously. If you said 60% cat, punishment is moderate. It rewards calibrated confidence.  
**KL Divergence** — related to cross-entropy, measures how much distribution P differs from Q.  
  
  
KL(P‖Q) = Σ P(x) · log(P(x)/Q(x))  
  
Cross-entropy H(P,Q) = H(P) + KL(P‖Q)  
**Use:** VAEs, knowledge distillation, distribution matching.
