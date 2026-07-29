# LLM Foundations (Encoder vs Decoder)

**Prev:** [[00 - Chapter Overview]] · **Next:** [[02 - Tokenization]]

---

## In plain English

**LLMs** are large neural networks trained on text. Two families matter in interviews:

- **Encoders (BERT)** — understand text (classification, embeddings)
- **Decoders (GPT)** — generate text token by token
![[Pasted image 20260728200721.png]]

![[Pasted image 20260723123727.png]]
---
# Transformer Architecture

Every text-generative Transformer consists of these **three key components**:

1. **Embedding**: Text input is divided into smaller units called tokens, which can be words or subwords. These tokens are converted into numerical vectors called embeddings, which capture the semantic meaning of words.
2. **Transformer Block** is the fundamental building block of the model that processes and transforms the input data. Each block includes:
    - **Attention Mechanism**, the core component of the Transformer block. It allows tokens to communicate with other tokens, capturing contextual information and relationships between words. (**Queries (Q)**, **Keys (K)**, and **Values (V)**)
    - **MLP (Multilayer Perceptron) Layer**, a feed-forward network that operates on each token independently. While the goal of the attention layer is to route information between tokens, the goal of the MLP is to refine each token's representation.
3. **Output Probabilities**: The final linear and softmax layers transform the processed embeddings into probabilities, enabling the model to make predictions about the next token in a sequence.
4. **Positional Encoding):**
- Adding extra data numbers to each token.
- Teaching the model which word comes first, second, or
- 
In the original (translation) paper there are three attentions (orange blocks):  

[![image](https://global.discourse-cdn.com/dlai/optimized/3X/e/c/ec3663032fb3eafe3d91fc0e25b27d88232c9c2b_2_395x500.png)

image482×609 55.7 KB

](https://global.discourse-cdn.com/dlai/original/3X/e/c/ec3663032fb3eafe3d91fc0e25b27d88232c9c2b.png "image")

- the leftmost is usually called “Self Attention”
- the right-bottom is usually called “Causal Attention”
- the right-top is usually called “Cross Attention”

So intuitively each attention “has different goals”. _On top of that_ each head (in multi-head) focuses on its own specialty.

![[Pasted image 20260727111924.png]]
The self-attention  It evaluates relationships by computing three primary vectors—**Queries (Q)**, **Keys (K)**, and **Values (V)**

![[Pasted image 20260727112039.png]]
https://medium.com/machine-intelligence-and-deep-learning-lab/transformer-the-self-attention-mechanism-d7d853c2c621
## Comparison

| | Encoder (BERT) | Decoder (GPT, Llama) |
|---|----------------|----------------------|
| Attention | Bidirectional | Causal (left → right) |
| Training | Masked words | Next-token prediction |
| Output | Embeddings / classes | Generated text |
| Example use | Search, NER, RAG embeddings | Chat, code, agents |

**Seq2seq (T5):** encoder reads input, decoder writes output (translation).

---

## How GPT generates

```
Prompt tokens → model → probability over next token → sample/pick → append → repeat
```

That's **autoregressive** generation.

---

## Link to previous chapters

| Ch | Link |
|----|------|
| NLP | [[06 NLP & Text Mining/06 - BERT and Contextual NLP]] |
| Transformers | [[10 Transformers & Attention/06 - Encoder Decoder and Masks]] |
| RNN history | [[05 Deep Learning/11 - RNN LSTM and GRU]] |

---

**Next:** [[02 - Tokenization]]
