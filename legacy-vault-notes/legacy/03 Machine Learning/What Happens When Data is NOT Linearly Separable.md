# What Happens When Data is NOT Linearly Separable

This is the **normal, expected case**. Logistic regression handles it fine:  
* It finds the best linear boundary it can  
* Outputs calibrated probabilities, not just hard labels  
* Overlapping classes → probabilities stay away from 0/1, which is honest and useful
