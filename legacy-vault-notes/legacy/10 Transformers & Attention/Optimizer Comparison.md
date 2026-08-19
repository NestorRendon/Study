# Optimizer Comparison

| Optimizer      | Adaptive LR | Momentum | Best For                          |
| -------------- | ----------- | -------- | --------------------------------- |
| SGD            | No          | Optional | CV models, fine-tuned control     |
| SGD + Momentum | No          | Yes      | ImageNet-scale CNNs               |
| AdaGrad        | Yes         | No       | Sparse features, NLP              |
| RMSProp        | Yes         | No       | RNNs                              |
| Adam           | Yes         | Yes      | General purpose, fast prototyping |
| AdamW          | Yes         | Yes      | Transformers, LLMs                |
