# ReAG = Add Explicit Reasoning / Smarter Context Selection

**Idea:** Instead of blindly using retrieved chunks, the model/reasoning layer:  
* evaluates which evidence is actually relevant,  
* may reason over multiple pieces of evidence,  
* may iteratively refine retrieval,  
* may filter noisy context before answering.  
Depending on the paper/framework, ReAG can also mean letting the model reason directly over raw docs instead of a basic retrieve-then-generate pipeline. The exact implementation varies by author/tool
