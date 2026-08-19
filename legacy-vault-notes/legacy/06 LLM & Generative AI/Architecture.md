# Architecture

Token → Router (gating network) → selects Top-K experts  
                                 → Expert 1 (FFN)  ┐  
                                 → Expert 3 (FFN)  ┤ → weighted sum → output  
                                 (others ignored)  ┘  
  
Router score:  gᵢ = softmax(W_router · x)  
Final output:  y = Σ gᵢ · Expertᵢ(x)   for top-K experts only  
**ELI5:** A hospital where every patient goes to triage first. Triage decides: send this patient to cardiology + neurology, ignore all other departments. The hospital has 100 specialist departments but only 2 are activated per patient.
