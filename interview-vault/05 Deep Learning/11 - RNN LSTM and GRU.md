# RNN, LSTM & GRU

**Prev:** [[10 - Batch Normalization]] · **Next:** [[12 - Convolutional Neural Networks]]

---

## In plain English

**Sequences** (text, audio, time series) have **order**. A feedforward net sees one vector at a time. An **RNN** keeps a **hidden memory** $h_t$ that summarizes the past and updates at each time step.

**LSTM / GRU** fix the RNN problem of **forgetting** early steps (vanishing gradients).

**Today:** transformers dominate long text; RNNs still appear in **streaming**, **small edge models**, and interviews.

---

## Vanilla RNN

$$h_t = f(W_x x_t + W_h h_{t-1} + b)$$

| Symbol | Meaning |
|--------|---------|
| $x_t$ | Input at time $t$ |
| $h_t$ | Hidden state (“memory”) |
| $W_x, W_h$ | Learned weights |

**Problem:** vanishing/exploding gradients → poor **long-range** memory.

![RNN unrolled](assets/CCA3EB31-DB34-42A2-80E8-75FD47D5757F.webp)

---

## LSTM (Long Short-Term Memory)

Adds **gates** that control what to forget, store, and output:

| Gate | Role |
|------|------|
| **Forget** | Drop old memory |
| **Input** | Write new info |
| **Output** | What to expose |

**Use:** longer dependencies than vanilla RNN (speech, older NLP).

---

## GRU (Gated Recurrent Unit)

Simpler than LSTM (fewer parameters), often **similar accuracy**, faster training.

---

## Comparison table (interview)

| Model | Strength | Weakness | Today |
|-------|----------|----------|-------|
| Vanilla RNN | Simple | Forgets long context | Rare alone |
| LSTM | Long memory | Slow, sequential | Legacy NLP, audio |
| GRU | Efficient LSTM-like | Slightly less expressive | Same |
| **Transformer** | Parallel, global attention | Cost, data | **SOTA NLP** |
| **Mamba / SSM** | Long context, efficient inference | Newer stack | Rising trend |

---

## RNN vs CNN vs Transformer

| | RNN/LSTM | CNN | Transformer |
|---|----------|-----|-------------|
| Inductive bias | Order, local time | Local spatial patterns | Global pairwise attention |
| Parallelism | Sequential steps | Highly parallel | Parallel (training) |
| Best legacy use | Streaming series | Images | Language |

---

## Common traps

| Trap | Correct |
|------|---------|
| "LSTM is always best for text" | Transformers dominate; RNNs for constraints/streaming |
| "Bidirectional LSTM for live prediction" | BiLSTM needs **future** tokens — offline only |
| "Hidden state = unlimited memory" | Still bounded; degrades over very long sequences |

---

## 30-second interview answer

> "RNNs maintain a hidden state across time steps; LSTMs and GRUs use gates to mitigate vanishing gradients for longer sequences. In modern NLP, transformers replaced most RNN stacks because they parallelize and model long-range dependencies with attention. I still mention RNNs for time series, streaming, and understanding pre-transformer baselines."

---

**Next:** [[12 - Convolutional Neural Networks]] · Then transformers: [[01 - Why Transformers]]
