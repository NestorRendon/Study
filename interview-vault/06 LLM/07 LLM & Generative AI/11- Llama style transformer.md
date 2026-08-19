# Llama

**Prev:** [[10 -Ststable difussion models]] · **Next:** [[12 - Transformers MoE Diffusion Metrics and SOTA]]

---

[Llama](https://huggingface.co/papers/2302.13971) is a family of large language models ranging from 7B to 65B parameters. These models are focused on efficient inference (important for serving language models) by training a smaller model on more tokens rather than training a larger model on fewer tokens. The Llama model is based on the GPT architecture, but it uses pre-normalization to improve training stability, replaces ReLU with SwiGLU to improve performance, and replaces absolute positional embeddings with rotary positional embeddings (RoPE) to better handle longer sequence lengths.

![[Pasted image 20260728201833.png]]
### **GPT: LayerNorm**

GPT normally uses Layer Normalization. Think of it like this: for a token’s hidden state, you compute the mean and standard deviation across its components, subtract the mean, divide by the std, then optionally scale and shift with learned parameters. If your vector is [2.0, -1.0, 1.0], you find its mean (≈ 0.667), std (≈ 1.247), then do (x — mean)/std. You might end up with something like [1.07, -1.34, 0.27]

### **LLaMA: RMSNorm**

LLaMA uses RMSNorm. Instead of subtracting the mean, you just divide by the root mean square of the vector and multiply by a learnable scale. If [2.0, -1.0, 1.0] has an RMS around 1.414, dividing gives [1.414, -0.707, 0.707]. No shift or bias in RMSNorm. It’s lighter and typically stable for large-scale models.




![[Pasted image 20260728200206.png]]