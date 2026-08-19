# 6. Batch Normalization

Normalizes the activations of each layer across the mini-batch. Applied *before or after* the activation function.  
  
  
x̂ = (x - μ_batch) / σ_batch     ← normalize  
y  =  γ·x̂ + β                   ← scale and shift (learned)  
![Normalize ine outputs](assets/019842ED-DD48-46AF-B521-B215CE3B6ACD.png)  
**Why it helps:**  
* Reduces internal covariate shift  
* Allows higher learning rates  
* Acts as mild regularizer  
* Makes training much more stable  
**Use:** almost always after Conv or Dense layers in deep networks.  
  
![Sentence Length](assets/8BE791E1-FE81-49F2-9648-636BC419F83F.png)
