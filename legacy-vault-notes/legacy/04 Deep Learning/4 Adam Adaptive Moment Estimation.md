# 4. Adam — Adaptive Moment Estimation

Combines **momentum** (1st moment) + **RMSProp** (2nd moment). Most popular optimizer in practice.  
  
  
m ← β₁·m + (1-β₁)·∇L          (1st moment — mean of gradients)  
v ← β₂·v + (1-β₂)·(∇L)²       (2nd moment — variance of gradients)  
  
m̂ = m / (1 - β₁ᵗ)             (bias correction)  
v̂ = v / (1 - β₂ᵗ)  
  
w ← w - α · m̂ / (√v̂ + ε)  
**Defaults:** β₁=0.9, β₂=0.999, ε=1e-8, α=1e-3  
**ELI5:** Adam remembers which direction it's been going (momentum) AND how bumpy each parameter's landscape is (variance). It takes big steps on smooth parameters, small steps on noisy ones.  
  
  
Adam is essentially RMSprop with added momentum.
