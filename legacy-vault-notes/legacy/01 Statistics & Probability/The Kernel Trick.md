# The Kernel Trick

SVMs can find **non-linear boundaries** without explicitly computing new features — by mapping data to higher dimensions implicitly via a kernel function:  
  
  
Linear kernel:      K(x,z) = x·z  
Polynomial kernel:  K(x,z) = (x·z + c)^d  
RBF / Gaussian:     K(x,z) = exp(-γ‖x-z‖²)   ← most common  
**ELI5:** Data not separable in 2D? Project it into 100D where it is — but do the math without actually going there. That's the kernel trick.
