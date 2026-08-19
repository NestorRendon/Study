# 7. Layer Normalization

Like Batch Norm but normalizes *across features* for a single sample, not across the batch.  
  
  
Batch Norm:  normalize across the batch dimension  
Layer Norm:  normalize across the feature dimension  
**Use:** Transformers and RNNs — where batch size may be 1 or sequences vary in length. Batch Norm breaks in those settings; Layer Norm doesn't.
