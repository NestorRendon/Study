# 7. Learning Rate — The Most Important Hyperparameter

**Too high** → loss explodes, overshoots minimum **Too low** → training is slow, gets stuck  
**Learning Rate Schedules**  
**Step decay** — reduce LR by factor every N epochs  
  
  
α ← α × 0.1   every 30 epochs  
**Cosine annealing** — smooth decay following a cosine curve. Very common, works well.  
  
  
αₜ = αₘᵢₙ + ½(αₘₐₓ - αₘᵢₙ)(1 + cos(πt/T))  
**Warmup** — start with very small LR, ramp up, then decay. Standard for Transformers.  
  
  
Epochs 0→5:   LR ramps up (warmup)  
Epochs 5→N:   LR decays (cosine or linear)  
**Cyclical LR** — oscillates between min and max. Can escape local minima.
