# 3. Other Important Losses

**Hinge Loss (SVM)**  
  
  
L = max(0, 1 - y·ŷ)       y ∈ {-1, +1}  
* Zero loss if prediction is correct AND confident (margin > 1)  
* **Use:** SVMs, max-margin classifiers  
**Focal Loss**  
  
  
L = -α(1 - ŷ)^γ · log(ŷ)  
* Down-weights easy examples, focuses on hard ones  
* **Use:** class imbalance problems (object detection, fraud detection)  
**Contrastive / Triplet Loss**  
  
  
L = max(0, d(anchor, positive) - d(anchor, negative) + margin)  
* Pulls similar samples together, pushes different ones apart  
* **Use:** embeddings, face recognition, recommendation systems  
**ELBO (Evidence Lower Bound)**  
  
  
L = E[log P(x|z)] - KL(Q(z|x) ‖ P(z))  
  = reconstruction loss + regularization  
* **Use:** Variational Autoencoders (VAEs)
