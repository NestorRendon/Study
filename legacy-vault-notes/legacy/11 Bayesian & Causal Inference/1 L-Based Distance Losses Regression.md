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
  
  
[Credible intervals](https://www.google.com/search?q=Credible+intervals&oq=What+is+a+credible+interval+vs+a+confidence+interval%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyCggEEAAYgAQYogQyCggFEAAYogQYiQUyCggGEAAYgAQYogQyCggHEAAYgAQYogTSAQc0NzJqMGo5qAIGsAIB8QUTzzqL7XnKOg&sourceid=chrome&ie=UTF-8&ved=2ahUKEwj71vyr8ZeTAxXn9LsIHcK5MAYQgK4QegQIARAC) (Bayesian) provide a direct probability range for a parameter based on data and prior beliefs (e.g., "there is a 95% chance the true value is here"). [Confidence intervals](https://www.google.com/search?q=Confidence+intervals&oq=What+is+a+credible+interval+vs+a+confidence+interval%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyCggEEAAYgAQYogQyCggFEAAYogQYiQUyCggGEAAYgAQYogQyCggHEAAYgAQYogTSAQc0NzJqMGo5qAIGsAIB8QUTzzqL7XnKOg&sourceid=chrome&ie=UTF-8&ved=2ahUKEwj71vyr8ZeTAxXn9LsIHcK5MAYQgK4QegQIARAD) (Frequentist) represent the frequency with which an interval calculated from repeated, random sampling contains the fixed true parameter
