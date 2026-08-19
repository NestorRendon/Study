# 3. Recurrent (RNN / LSTM / GRU)

Has a hidden state — a memory that carries information across time steps.  
  
  
hₜ = f(Wₓ·xₜ + Wₕ·hₜ₋₁ + b)  
     ↑ current input    ↑ previous memory  
**Vanilla RNN** — suffers from vanishing gradients (forgets early steps). **LSTM** — adds gates (forget, input, output) to control memory. Solves vanishing gradient. **GRU** — simpler than LSTM, fewer parameters, similar performance.  
**Use:** text, speech, time series sequences.  
  
![Recurrent Neural Network](assets/CCA3EB31-DB34-42A2-80E8-75FD47D5757F.webp)  
  
**Intuition**  
A recurrent network processes sequences step by step.  
At each step it keeps a summary of what it has seen so far:  
```

previous hidden state + current input → new hidden state


```
That hidden state is the network’s memory.  
  
**Why Is It Called “Hidden”?**  
Because it is:  
* **internal to the model**  
* not directly part of the input/output  
* a latent representation learned during training  
So “hidden” means:  
**Internal representation not directly observed**  
  

| Model | Purpose | Advantages | Disadvantages | Better / Modern Alternatives |
| ------------------------------------ | -------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------- |
| Vanilla RNN | Basic sequential modeling | Very simple, lightweight, easy to learn | Severe vanishing/exploding gradients, poor long-term memory | GRU, LSTM |
| LSTM | Capture long-term dependencies in sequences | Strong memory mechanism, robust, proven in many domains | More parameters, slower training/inference, sequential (not parallelizable) | GRU (lighter), Transformer, TCN |
| GRU | Efficient long/medium-range sequence modeling | Similar performance to LSTM with fewer parameters, faster | Sometimes slightly less expressive than LSTM | Transformer, TCN |
| Bidirectional LSTM/GRU | Use past + future context for each token/time step | Better context understanding, improved accuracy in offline tasks | Cannot be used causally/online, doubles compute | Transformer encoders |
| Seq2Seq RNN/LSTM | Map input sequences to output sequences | Flexible encoder-decoder structure | Bottlenecked by fixed hidden state, weaker than attention methods | Transformer Seq2Seq |
| Temporal Convolutional Network (TCN) | Sequence modeling with dilated convolutions | Parallelizable, stable gradients, handles long receptive fields well | Less intuitive memory mechanism, architecture tuning can be tricky | Transformer, SSMs (depending on task) |
| Transformer | Attention-based global sequence modeling | Excellent long-range modeling, parallel training, SOTA in many tasks | Computationally expensive, memory-heavy, data-hungry | Long-context transformer variants, SSMs |
| State Space Models (e.g. Mamba/S4) | Efficient very-long-sequence modeling | Scales better on long contexts, efficient inference | Newer/less mature ecosystem, more specialized | Transformer (if compute not an issue) |
