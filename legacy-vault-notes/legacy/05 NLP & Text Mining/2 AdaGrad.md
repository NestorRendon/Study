# 2. AdaGrad

Adapts learning rate **per parameter** — parameters updated frequently get smaller steps, rare ones get bigger steps.  
  
  
G ← G + (∇L)²          (accumulated squared gradients)  
w ← w - α / √G · ∇L  
**Problem:** G keeps growing → learning rate shrinks to near zero and training stops. Bad for deep networks.  
**Good for:** sparse data, NLP with rare words.
