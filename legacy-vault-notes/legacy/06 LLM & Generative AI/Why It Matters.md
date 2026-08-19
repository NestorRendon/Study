# Why It Matters

GPT-4 (rumored):   ~8 experts, 2 active per token  
Mixtral 8x7B:      8 experts of 7B params each, 2 active  
                   Total params: ~47B  
                   Active params per token: ~13B  ← inference cost of 13B model  
You get the quality of a large model at the inference cost of a small one.  
**Load balancing problem:** without extra regularization, the router collapses — sends everything to 1-2 experts, ignoring the rest. Fix: auxiliary loss that penalizes uneven expert usage.
