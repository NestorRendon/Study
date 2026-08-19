# The Problem

Fine-tuning all weights of a 7B parameter model is expensive — requires storing gradients and optimizer states for 7 billion parameters. PEFT (Parameter-Efficient Fine-Tuning) updates only a tiny fraction of weights.
