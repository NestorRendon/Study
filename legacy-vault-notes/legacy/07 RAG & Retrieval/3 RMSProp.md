# 3. RMSProp

Fixes AdaGrad by using an **exponential moving average** of squared gradients instead of accumulating forever.  
  
  
G ← β·G + (1-β)·(∇L)²     (β ≈ 0.9, decaying average)  
w ← w - α / √G · ∇L  
Learning rate stays alive throughout training. Good for RNNs.
