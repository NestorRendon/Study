# 1. L-Based Distance Losses (Regression)

**MSE — Mean Squared Error (L2 Loss)**  
  
  
L = (1/n) Σ (yᵢ - ŷᵢ)²  
* Penalizes large errors heavily (squaring amplifies outliers)  
* Smooth gradient → easy to optimize  
* **Use when:** outliers are rare and should be penalized hard  
  
**MAE — Mean Absolute Error (L1 Loss)**  
L = (1/n) Σ |yᵢ - ŷᵢ|  
* Treats all errors linearly, robust to outliers  
* Gradient is constant → can oscillate near minimum  
* **Use when:** outliers are common (house prices, demand forecasting)  
**Huber Loss (smooth L1)**  
  
  
L = (1/2)(y - ŷ)²           if |y - ŷ| ≤ δ  
L = δ·|y - ŷ| - (1/2)δ²    otherwise  
* L2 for small errors, L1 for large errors — best of both  
* δ is a tunable threshold  
* **Use when:** you want robustness but smooth gradients  
**RMSE** — just √MSE. Same behavior as MSE, but interpretable in original units.  

| Loss  | Outlier Sensitivity | Gradient | Use Case                      |
| ----- | ------------------- | -------- | ----------------------------- |
| MSE   | High                | Smooth   | Clean data, Gaussian noise    |
| MAE   | Low                 | Constant | Noisy data, robust regression |
| Huber | Medium              | Smooth   | General purpose regression    |
  
  
Entropu   
![(x) 0801(x)d]-=H](assets/3A1F0391-AE84-4CED-B402-440C1626525E.avif)  
  
Cross entropy ,:
