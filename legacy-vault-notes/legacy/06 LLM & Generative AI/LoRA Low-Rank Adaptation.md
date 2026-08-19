# LoRA — Low-Rank Adaptation

**Core math idea:** weight updates during fine-tuning tend to have **low intrinsic rank** — they live in a small subspace. So instead of updating the full weight matrix W, approximate the update with two small matrices.  
  
Original weight matrix:    W  ∈ ℝ^(d×d)     (frozen, not updated)  
LoRA adds a bypass:        ΔW = A · B  
  
A ∈ ℝ^(d×r)    B ∈ ℝ^(r×d)    r << d  
  
Forward pass:   y = (W + A·B) · x  
                    ↑ frozen   ↑ trained  
**Parameter savings example:**  
  
  
W is 1024 × 1024 = 1,048,576 parameters   (frozen)  
r = 8:  
  A is 1024 × 8  =    8,192  
  B is    8 × 1024 =  8,192  
  Total trainable:   16,384  ← 64× fewer parameters  
**ELI5:** Instead of repainting the entire wall, you put a thin sticker on top. The sticker is the low-rank update — tiny but enough to change the behavior.
