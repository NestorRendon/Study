# 4. Dropout

During training, randomly sets a fraction of neurons to zero. Forces the network to not rely on any single neuron.  
he primary purpose of dropout in neural networks is to **prevent overfitting** by acting as a regularization technique, forcing the network to learn more robust and generalizable features  
  
Training:   each neuron active with probability p (e.g. 0.8)  
Inference:  all neurons active, weights scaled by p  
**It's a regularizer** — reduces overfitting. Equivalent to training an ensemble of subnetworks.  
**Typical values:** 0.2–0.5. Don't use on small datasets or final layers.
