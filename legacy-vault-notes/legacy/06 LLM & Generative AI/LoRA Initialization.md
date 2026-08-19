# LoRA Initialization

A initialized with random Gaussian    → breaks symmetry  
B initialized with zeros              → ΔW = A·B = 0 at start  
                                        model starts identical to base  
This is critical — training starts from the pretrained model's behavior, not random noise.
