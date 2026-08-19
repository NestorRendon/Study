# 8. Attention

Lets the model focus on the most relevant parts of the input dynamically, instead of treating all positions equally.  
  
> **Look at all parts of the sequence and weigh which ones matter most right now.**  
>   
> **In One Sentence**  
> 
> **Attention = dynamic focus over relevant information**  
  
  
Attention(Q, K, V) = softmax(Q·Kᵀ / √dₖ) · V  
  
Q = Query   "what am I looking for?"  
K = Key     "what do I have?"  
V = Value   "what do I return?"  
**Self-attention** — each token attends to every other token in the sequence. Foundation of Transformers. **Multi-head attention** — run attention h times in parallel, each learning different relationships.  
**ELI5:** Translating "bank" — attention looks at surrounding words to decide if it means river bank or financial bank.  
  
[Self-attention ](https://www.geeksforgeeks.org/nlp/self-attention-in-nlp/)allows the model to consider all positions in the input sequence when producing the output for a specific position. The most widely known example of this is the Transformer model, which uses self-attention to process sequences in parallel, unlike traditional RNNs or LSTMs.
