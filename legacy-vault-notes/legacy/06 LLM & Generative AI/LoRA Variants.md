# LoRA Variants

**QLoRA** — LoRA + quantize the base model to 4-bit. Fine-tune a 65B model on a single GPU. The quantization reduces memory, LoRA reduces trainable parameters.  
**AdaLoRA** — adaptively allocates rank r across layers. Important layers get higher rank, minor layers get lower rank.  
**DoRA** — decomposes weights into magnitude + direction, applies LoRA to direction only. Often better than vanilla LoRA.
