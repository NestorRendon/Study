# PEFT Methods Comparison

| Method | Trainable Params | Approach | Best For |
| -------------- | ---------------- | ------------------------- | ------------------------ |
| Full fine-tune | 100% | Update all weights | Lots of data, compute |
| LoRA | ~0.1–1% | Low-rank weight update | General fine-tuning |
| QLoRA | ~0.1–1% | LoRA + 4-bit quantization | Single GPU, large models |
| Prefix tuning | <1% | Learn soft prompt tokens | Few-shot, frozen model |
| Adapters | ~1–5% | Small bottleneck layers | Multi-task learning |
