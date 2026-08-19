# Key Hyperparameters

r      = rank of the update (4, 8, 16, 32 — higher r = more capacity)  
alpha  = scaling factor, ΔW is scaled by α/r  
         common to set alpha = r (or 2r)  
  
target modules = which layers to apply LoRA to  
                 typically: Q, V attention matrices  
                 sometimes: K, O, FFN layers too
