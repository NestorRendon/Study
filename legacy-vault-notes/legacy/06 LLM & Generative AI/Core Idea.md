# Core Idea

Instead of running the **entire network** for every token, MoE splits the feed-forward layers into N **expert sub-networks** and only activates K of them per token. Same model capacity, fraction of the compute cost.  
  
  
Standard FFN:     every token goes through one big FFN  
MoE FFN:          every token goes through 2 of 8 experts (for example)  
  
Active params per token << Total params in model
