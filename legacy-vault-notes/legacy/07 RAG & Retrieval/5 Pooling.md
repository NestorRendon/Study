# 5. Pooling

Downsamples the spatial dimensions. Reduces computation and adds position invariance.  
  
  
Max Pooling 2×2:   takes the MAX value in each 2×2 region  
Avg Pooling 2×2:   takes the AVERAGE value in each 2×2 region  
**Max pooling** — keeps the strongest signal (most common). **Global average pooling** — collapses entire feature map to one number per channel. Used before final dense layer.  
![Average Pooling](assets/49924540-1C34-46A2-A2CD-638F8AF04AB6.png)
