# 5. AdamW

Adam + proper **weight decay** (L2 regularization decoupled from the gradient update). Fixes a subtle bug in Adam where L2 reg doesn't behave correctly.  
  
  
w ← w - α · (m̂ / (√v̂ + ε) + λ·w)  
**Default choice for Transformers and LLMs.** Almost always better than vanilla Adam.
