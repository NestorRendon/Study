# 1. Fully Connected (Dense)

Every neuron connects to every neuron in the next layer.  
  
  
output = activation(W·x + b)  
  
W = weight matrix   b = bias   x = input vector  
**Use:** classification heads, final layers, tabular data. **Problem:** doesn't scale to images — too many parameters.
