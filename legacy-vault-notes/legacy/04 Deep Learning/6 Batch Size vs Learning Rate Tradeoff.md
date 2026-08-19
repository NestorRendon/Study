# 6. Batch Size vs Learning Rate Tradeoff

**Small batch (8–64):**  
* Noisy gradients → acts as regularizer  
* Escapes local minima more easily  
* Slower per epoch, but often better generalization  
**Large batch (512–4096):**  
* Stable, accurate gradients  
* Faster training (parallelism)  
* Tends to converge to sharp minima → worse generalization  
* Needs a **larger learning rate** to compensate  
  
  
Linear scaling rule:  
If you multiply batch size by k → multiply learning rate by k  
  
Batch 256, lr=0.1  →  Batch 1024, lr=0.4
