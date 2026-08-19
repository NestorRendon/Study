# 1. SGD — Stochastic Gradient Descent

Compute gradient on a **random mini-batch**, update weights.  
  
  
w ← w - α · ∇L(mini-batch)  
**Vanilla SGD problems:**  
* Same learning rate for all parameters  
* Slow in flat regions, oscillates in narrow valleys  
* Sensitive to learning rate choice  
**SGD + Momentum** — adds a velocity term, accumulates past gradients. Smooths oscillations, speeds up flat regions.  
  
  
v ← β·v + ∇L        (β ≈ 0.9)  
w ← w - α·v  
**ELI5:** Like a ball rolling downhill — momentum carries it through flat spots and small bumps.
