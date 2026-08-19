# Complete variable table

**Complete variable table (all variables)**  

| Variable | Name | What it is | How it's determined | Example value |
| -------- | -------------------- | --------------------------------------------- | --------------------------------- | ------------------------- |
| V | Vocabulary size | Total number of tokens the model knows | Chosen by researchers | 50,000 |
| S | Sequence length | Number of tokens in the input | Chosen by researchers | 3 |
| D | Embedding dimension | Length of each token's vector | Chosen by researchers | 4 |
| H | Number of heads | How many attention heads run in parallel | Chosen by researchers | 2 |
| d_k | Key/Query dimension | Size of Q and K vectors per head | Calculated: D ÷ H | 4 ÷ 2 = 2 |
| d_v | Value dimension | Size of V vectors per head | Calculated: D ÷ H | 4 ÷ 2 = 2 |
| d_ff | FFN hidden dimension | Size of expanded vector inside FFN | Calculated: D × 4 | 4 × 4 = 16 |
| N | Number of blocks | How many Transformer blocks stack | Chosen by researchers | 2 |
| E | Embedding table | Matrix storing all token vectors | Learned during training | [50,000 × 4] |
| W_Q | Query weight matrix | Projects embedding into Q space | Learned during training | [4 × 2] |
| W_K | Key weight matrix | Projects embedding into K space | Learned during training | [4 × 2] |
| W_V | Value weight matrix | Projects embedding into V space | Learned during training | [4 × 2] |
| Q | Query matrix | "What am I looking for?" — per token | Calculated: E × W_Q | [S × d_k] = [3 × 2] |
| K | Key matrix | "What do I offer?" — per token | Calculated: E × W_K | [S × d_k] = [3 × 2] |
| V | Value matrix | "What info do I carry?" — per token | Calculated: E × W_V | [S × d_v] = [3 × 2] |
| A | Attention matrix | Attention weights between all token pairs | Calculated: softmax(Q·K^T ÷ √d_k) | [S × S] = [3 × 3] |
| W_O | Output weight matrix | Projects concatenated heads back to D | Learned during training | [D × D] = [4 × 4] |
| W1 | FFN first layer | Expands dimension inside FFN | Learned during training | [D × d_ff] = [4 × 16] |
| W2 | FFN second layer | Compresses back to D | Learned during training | [d_ff × D] = [16 × 4] |
| b1 | FFN first bias | Bias added after W1 | Learned during training | [d_ff] = [16] |
| b2 | FFN second bias | Bias added after W2 | Learned during training | [D] = [4] |
| W_out | Output projection | Projects final vector to vocabulary scores | Learned during training | [D × V] = [4 × 50,000] |
| lr | Learning rate | Step size during weight updates | Chosen by researchers | 0.001 |
| Loss | Cross entropy loss | How wrong the prediction was | Calculated during training | scalar number |
| ∇ | Gradient | Direction and magnitude to adjust each weight | Calculated via backpropagation | same shape as each matrix |
  
   
**How these choices affect the model**  

| If you increase... | Effect | Cost |
| ------------------ | ------------------------------------ | -------------------------------------------------------- |
| D | Richer token representations | More memory, more compute |
| H | More types of relationships captured | More compute |
| N | Deeper reasoning, more abstraction | Much more compute |
| S | Longer context window | Quadratic cost — doubling S quadruples attention compute |
| V | More expressive vocabulary | More memory for embedding table |
  
  
**Part 1 — Training example**  
We will use tiny numbers so every calculation is visible.  
  
  
Hyperparameters:  
S = 3, D = 4, H = 2, d_k = 2, d_v = 2, d_ff = 16, N = 1  
Training sentence:  
  
  
Input:    "The cat sat"  
Expected: "on"  (token index = 8 in our tiny vocabulary)  
  
**Step 1 — Tokenize**  
  
  
"The" → index 1  
"cat" → index 2  
"sat" → index 3  
  
Tokens = [1, 2, 3]     shape: [S] = [3]  
  
**Step 2 — Embedding lookup**  
Embedding table E shape: [V × D] = [50,000 × 4]  
We look up rows 1, 2, 3:  
  
  
e1("The") = [ 0.1,  0.2, -0.3,  0.5]  
e2("cat") = [ 0.2, -0.5,  0.8,  0.1]  
e3("sat") = [ 0.5,  0.1,  0.2, -0.4]  
   
E_input shape: [S × D] = [3 × 4]  
  
**Step 3 — Create Q, K, V (Head 1)**  
Initial random W_Q, W_K, W_V each shape [D × d_k] = [4 × 2]:  
  
  
W_Q = [ 0.1,  0.2]     W_K = [ 0.3, -0.1]     W_V = [ 0.2,  0.1]  
      [-0.3,  0.4]           [ 0.2,  0.5]           [-0.1,  0.3]  
      [ 0.5, -0.2]           [-0.4,  0.1]           [ 0.4, -0.2]  
      [ 0.1,  0.3]           [ 0.1,  0.2]           [ 0.1,  0.5]  
Calculate Q = E_input × W_Q:  
  
  
Q1("The") = [0.1×0.1 + 0.2×(-0.3) + (-0.3)×0.5 + 0.5×0.1,  
             0.1×0.2 + 0.2×0.4  + (-0.3)×(-0.2) + 0.5×0.3]  
          = [0.01 - 0.06 - 0.15 + 0.05,  
             0.02 + 0.08 + 0.06 + 0.15]  
          = [-0.15,  0.31]  
  
Q2("cat") = [ 0.09,  0.21]  
Q3("sat") = [ 0.18, -0.14]  
  
Q shape: [3 × 2]  
Same process for K and V:  
  
  
K1("The") = [ 0.12, -0.08]  
K2("cat") = [-0.21,  0.34]  
K3("sat") = [ 0.15,  0.07]  
  
V1("The") = [ 0.11,  0.28]  
V2("cat") = [ 0.31, -0.14]  
V3("sat") = [ 0.22,  0.18]  
  
**Step 4 — Attention scores**  
Calculate Q × K^T:  
  
  
Q × K^T shape: [3 × 2] × [2 × 3] = [3 × 3]  
Each cell = dot product of one Q row with one K row:  
  
  
A_raw[1,1] = Q1·K1 = (-0.15×0.12) + (0.31×-0.08) = -0.018 - 0.025 = -0.043  
A_raw[1,2] = Q1·K2 = (-0.15×-0.21) + (0.31×0.34) =  0.032 + 0.105 =  0.137  
A_raw[1,3] = Q1·K3 = (-0.15×0.15) + (0.31×0.07)  = -0.023 + 0.022 = -0.001  
  
A_raw[2,1] = Q2·K1 = (0.09×0.12)  + (0.21×-0.08) =  0.011 - 0.017 = -0.006  
A_raw[2,2] = Q2·K2 = (0.09×-0.21) + (0.21×0.34)  = -0.019 + 0.071 =  0.052  
A_raw[2,3] = Q2·K3 = (0.09×0.15)  + (0.21×0.07)  =  0.014 + 0.015 =  0.029  
  
A_raw[3,1] = Q3·K1 = (0.18×0.12)  + (-0.14×-0.08) = 0.022 + 0.011 =  0.033  
A_raw[3,2] = Q3·K2 = (0.18×-0.21) + (-0.14×0.34)  = -0.038 - 0.048 = -0.086  
A_raw[3,3] = Q3·K3 = (0.18×0.15)  + (-0.14×0.07)  = 0.027 - 0.010 =  0.017  
  
A_raw = [[-0.043,  0.137, -0.001]  
         [-0.006,  0.052,  0.029]  
         [ 0.033, -0.086,  0.017]]  
  
**Step 5 — Scale by √d_k**  
  
  
√d_k = √2 = 1.414  
  
A_scaled = A_raw ÷ 1.414  
  
A_scaled = [[-0.030,  0.097, -0.001]  
            [-0.004,  0.037,  0.021]  
            [ 0.023, -0.061,  0.012]]  
  
**Step 6 — Softmax per row**  
  
  
softmax(x_i) = e^x_i ÷ Σ(e^x_j)  
Row 1: [-0.030, 0.097, -0.001]  
  
  
e^-0.030 = 0.970  
e^0.097  = 1.102  
e^-0.001 = 0.999  
sum      = 3.071  
  
A[1] = [0.970/3.071, 1.102/3.071, 0.999/3.071]  
     = [0.316, 0.359, 0.325]   ← adds up to 1.0 ✅  
Row 2: [-0.004, 0.037, 0.021]  
  
  
e^-0.004 = 0.996  
e^0.037  = 1.038  
e^0.021  = 1.021  
sum      = 3.055  
  
A[2] = [0.326, 0.340, 0.334]   ← adds up to 1.0 ✅  
Row 3: [0.023, -0.061, 0.012]  
  
  
e^0.023  = 1.023  
e^-0.061 = 0.941  
e^0.012  = 1.012  
sum      = 2.976  
  
A[3] = [0.344, 0.316, 0.340]   ← adds up to 1.0 ✅  
Final attention matrix:  
  
  
A = [[0.316, 0.359, 0.325]  
     [0.326, 0.340, 0.334]  
     [0.344, 0.316, 0.340]]  
  
**Step 7 — Weighted sum of V**  
Output = A × V, shape: [3 × 3] × [3 × 2] = [3 × 2]  
  
  
Out1("The") = 0.316×V1 + 0.359×V2 + 0.325×V3  
            = 0.316×[0.11, 0.28] + 0.359×[0.31,-0.14] + 0.325×[0.22, 0.18]  
            = [0.035, 0.088] + [0.111,-0.050] + [0.072, 0.059]  
            = [0.218, 0.097]  
  
Out2("cat") = 0.326×[0.11,0.28] + 0.340×[0.31,-0.14] + 0.334×[0.22,0.18]  
            = [0.036,0.091] + [0.105,-0.048] + [0.073,0.060]  
            = [0.214, 0.103]  
  
Out3("sat") = 0.344×[0.11,0.28] + 0.316×[0.31,-0.14] + 0.340×[0.22,0.18]  
            = [0.038,0.096] + [0.098,-0.044] + [0.075,0.061]  
            = [0.211, 0.113]  
  
Head1_output shape: [3 × 2]  
  
**Step 8 — Multi-head concatenation**  
We have 2 heads. Head 2 runs the same process with its own W_Q2, W_K2, W_V2 (different random initialization). Let's say Head 2 produces:  
  
  
Head2_output = [[0.15, 0.09],  
                [0.12, 0.11],  
                [0.18, 0.07]]   shape: [3 × 2]  
Concatenate Head 1 and Head 2:  
  
  
Concat = [[0.218, 0.097, 0.15, 0.09],  
          [0.214, 0.103, 0.12, 0.11],  
          [0.211, 0.113, 0.18, 0.07]]   shape: [3 × 4] = [S × D] ✅  
Then multiply by W_O [D × D] = [4 × 4] to mix the heads:  
  
  
Attention_output = Concat × W_O    shape: [3 × 4]  
  
**Step 9 — Add & Normalize**  
**Residual connection** (add original embedding back):  
  
  
X = Attention_output + E_input     shape: [3 × 4]  
**Layer normalization** (keeps values stable, not going to expand here to keep focus):  
  
  
X_norm = LayerNorm(X)              shape: [3 × 4]  
  
**Step 10 — FFN**  
  
  
W1 shape: [4 × 16],  b1 shape: [16]  
W2 shape: [16 × 4],  b2 shape: [4]  
For each token independently:  
  
  
h  = GELU(X_norm × W1 + b1)    shape: [3 × 16]  
FFN_output = h × W2 + b2        shape: [3 × 4]  
**Add & Normalize again:**  
  
  
X_final = LayerNorm(FFN_output + X_norm)    shape: [3 × 4]  
This completes **one Transformer block**. With N=2 this whole process repeats once more.  
  
**Step 11 — Output projection**  
Take only the **last token** vector ("sat"):  
  
  
last = X_final[3]     shape: [1 × 4]  
Multiply by W_out [4 × 50,000]:  
  
  
scores = last × W_out     shape: [1 × 50,000]  
Apply softmax:  
  
  
probs = softmax(scores)   shape: [1 × 50,000]  
With random weights the result might be:  
  
  
"on"    → 0.00003   ← correct answer, but nearly zero probability  
"dog"   → 0.00821  
"pizza" → 0.00614  
...  
  
**Step 12 — Loss**  
  
  
correct token = "on" = index 8  
probability assigned to "on" = 0.00003  
  
Loss = -log(0.00003) = 10.41   ← very high, model is very wrong  
  
**Step 13 — Backpropagation**  
Calculate gradient of Loss with respect to **every weight**:  
  
  
∇W_out  shape: [4 × 50,000]  
∇W2     shape: [16 × 4]  
∇W1     shape: [4 × 16]  
∇W_O    shape: [4 × 4]  
∇W_V    shape: [4 × 2]  
∇W_K    shape: [4 × 2]  
∇W_Q    shape: [4 × 2]  
∇E      shape: [50,000 × 4]  
  
**Step 14 — Gradient descent**  
Update every weight:  
  
  
W_Q = W_Q - lr × ∇W_Q  
W_K = W_K - lr × ∇W_K  
W_V = W_V - lr × ∇W_V  
...all matrices updated...  
  
**Step 15 — Repeat**  
Next training example runs the same pipeline with the **updated weights**. After billions of steps the loss gets very small and the model predicts correctly.  
  
**Part 2 — Inference example**  
Inference is **exactly the same as the forward pass in training** — Steps 1 through 11 — but with two key differences:  
  
  
1. Weights are FROZEN — no backpropagation, no updates  
2. We generate token by token in a loop  
  
**Inference loop: "The cat sat" → generate response**  
**Iteration 1:**  
  
  
Input:  ["The", "cat", "sat"]  
↓ full forward pass (steps 1-11)  
↓ softmax over 50,000 tokens  
Output: "on" (highest probability)  
**Iteration 2:**  
  
  
Input:  ["The", "cat", "sat", "on"]   ← append predicted token  
↓ full forward pass  
Output: "the"  
**Iteration 3:**  
  
  
Input:  ["The", "cat", "sat", "on", "the"]  
↓ full forward pass  
Output: "mat"  
**Iteration 4:**  
  
  
Input:  ["The", "cat", "sat", "on", "the", "mat"]  
↓ full forward pass  
Output: "<END>"   ← special end token, stop generating  
Final output: "The cat sat on the mat" ✅  
  
**Training vs Inference — side by side**  

| Step                | Training      | Inference |
| ------------------- | ------------- | --------- |
| Tokenize            | ✅             | ✅         |
| Embedding lookup    | ✅             | ✅         |
| Q, K, V calculation | ✅             | ✅         |
| Attention           | ✅             | ✅         |
| FFN                 | ✅             | ✅         |
| Output projection   | ✅             | ✅         |
| Softmax             | ✅             | ✅         |
| Calculate Loss      | ✅             | ❌         |
| Backpropagation     | ✅             | ❌         |
| Update weights      | ✅             | ❌         |
| Loop token by token | ❌             | ✅         |
| Weights state       | Being learned | Frozen    |
  
Does this give you the complete picture with no missing steps? 🎯  
  
  
  
INPUT TEXT  
"The cat sat"  
        │  
        ▼  
┌───────────────────┐  
│    TOKENIZER      │  
│                   │  
│  "The" → index 1  │  
│  "cat" → index 2  │  
│  "sat" → index 3  │  
└────────┬──────────┘  
         │  [1, 2, 3]  
         ▼  
┌───────────────────────────────────────────┐  
│           EMBEDDING TABLE                 │  
│           [V × D] = [50,000 × 4]          │  
│                                           │  
│  row 1 → e1 = [ 0.1,  0.2, -0.3,  0.5]  │  
│  row 2 → e2 = [ 0.2, -0.5,  0.8,  0.1]  │  
│  row 3 → e3 = [ 0.5,  0.1,  0.2, -0.4]  │  
└────────┬──────────────────────────────────┘  
         │  E = [3 × 4]  ← static, no context yet  
         │  
         │  ┌─────────────────────────────────────┐  
         │  │  each token has same vector          │  
         │  │  regardless of surrounding words     │  
         │  └─────────────────────────────────────┘  
         ▼  
╔═══════════════════════════════════════════════════════╗  
║              TRANSFORMER BLOCK 1 of N                ║  
║                                                       ║  
║  ┌─────────────────────────────────────────────────┐ ║  
║  │              ATTENTION LAYER                    │ ║  
║  │                                                 │ ║  
║  │  E × W_Q → Q [3×2]  "what am I looking for?"   │ ║  
║  │  E × W_K → K [3×2]  "what do I offer?"         │ ║  
║  │  E × W_V → V [3×2]  "what info do I carry?"    │ ║  
║  │                                                 │ ║  
║  │         Q × K^T                                 │ ║  
║  │         ────────  =  A_raw  [3×3]               │ ║  
║  │           √d_k                                  │ ║  
║  │                                                 │ ║  
║  │         softmax(A_raw) = A  [3×3]               │ ║  
║  │                                                 │ ║  
║  │    "The" → [0.316, 0.359, 0.325]                │ ║  
║  │    "cat" → [0.326, 0.340, 0.334]                │ ║  
║  │    "sat" → [0.344, 0.316, 0.340]                │ ║  
║  │              ↑       ↑       ↑                  │ ║  
║  │            "The"  "cat"   "sat"                 │ ║  
║  │                                                 │ ║  
║  │  every token looks at every other token         │ ║  
║  │                                                 │ ║  
║  │         A × V = Out [3×2]                       │ ║  
║  │                                                 │ ║  
║  │  Out1("The") = [0.218, 0.097]                   │ ║  
║  │  Out2("cat") = [0.214, 0.103]  ← now knows      │ ║  
║  │  Out3("sat") = [0.211, 0.113]     about others  │ ║  
║  └───────────────────┬─────────────────────────────┘ ║  
║                      │                               ║  
║          ┌───────────▼───────────┐                   ║  
║          │  ADD & NORMALIZE      │                   ║  
║          │  Out + E  → [3×4]     │                   ║  
║          └───────────┬───────────┘                   ║  
║                      │                               ║  
║  ┌───────────────────▼─────────────────────────────┐ ║  
║  │                  FFN      [Feedforward neural network](https://en.wikipedia.org/wiki/Feedforward_neural_network)                      │ ║  
║  │                                                 │ ║  
║  │  each token independently:                      │ ║  
║  │                                                 │ ║  
║  │  h      = GELU(X × W1 + b1)  [3×16]            │ ║  
║  │  output = h × W2 + b2         [3×4]             │ ║.   **Decompose** the vector into more fine-grained features  
**											Apply non-linear transformations** that would be impossible in 4 dimensions  
**											Store and retrieve knowledge** learned during training  
  
║  │                                                 │ ║  
║  │  "The" → processes its context-aware vector     │ ║  
║  │  "cat" → processes its context-aware vector     │ ║  
║  │  "sat" → processes its context-aware vector     │ ║  
║  └───────────────────┬─────────────────────────────┘ ║  
║                      │                               ║  
║          ┌───────────▼───────────┐                   ║  
║          │  ADD & NORMALIZE      │                   ║  
║          │  X_final [3×4]        │                   ║  
║          └───────────┬───────────┘                   ║  
╚══════════════════════╪═══════════════════════════════╝  
                       │  
                       │  repeat N times  
                       │  each block refines vectors further  
                       ▼  
╔═══════════════════════════════════════════════════════╗  
║              TRANSFORMER BLOCK 2 of N                ║  
╚══════════════════════╪═══════════════════════════════╝  
                       │  
                       ▼  
                      ...  
╔═══════════════════════════════════════════════════════╗  
║              TRANSFORMER BLOCK N of N                ║  
╚══════════════════════╪═══════════════════════════════╝  
                       │  
                       │  X_final [3×4]  
                       ▼  
┌───────────────────────────────────────────────────────┐  
│                  OUTPUT LAYER                         │  
│                                                       │  
│  take ONLY last token vector                          │  
│  "sat" → [0.211, 0.113, ...]   [1×4]                 │  
│                                                       │  
│  × W_out [4 × 50,000]                                 │  
│  = scores [1 × 50,000]                                │  
│                                                       │  
│  softmax → probabilities [1 × 50,000]                 │  
│                                                       │  
│  "on"     → 0.40  ←── highest                        │  
│  "down"   → 0.25                                      │  
│  "there"  → 0.15                                      │  
│  "pizza"  → 0.00001                                   │  
│  ...                                                  │  
└───────────────────────┬───────────────────────────────┘  
                        │  
                        ▼  
                 NEXT TOKEN: "on"  
                        │  
                        ▼  
┌───────────────────────────────────────────────────────┐  
│              GENERATION LOOP                          │  
│                                                       │  
│  iter 1: "The cat sat"         → predicts "on"        │  
│  iter 2: "The cat sat on"      → predicts "the"       │  
│  iter 3: "The cat sat on the"  → predicts "mat"       │  
│  iter 4: "The cat sat on the mat" → predicts <END>    │  
│                                                       │  
│  each iteration runs the FULL pipeline again          │  
└───────────────────────────────────────────────────────┘  
  
WITHOUT attention:  
"bank" in any sentence → same vector [−0.3, 0.9, −0.1, 0.6]  
→ model cannot distinguish river bank vs financial bank  
  
WITH attention:  
"bank" + "fishing" nearby → vector shifts toward river meaning  
"bank" + "deposit" nearby → vector shifts toward financial meaning  
→ same word, different context, different vector  
  
E (embeddings)          "I know what each word IS"  
        ↓  
Attention output        "I know what each word MEANS here"  
        ↓  
Add & Normalize         "stabilize the vectors"  
        ↓  
FFN input               "context-aware, needs deeper processing"  
        ↓  
FFN output              "context-aware + knowledge applied"  
        ↓  
Add & Normalize         "stabilize again"  
        ↓  
Next block or           "refined understanding, ready for  
output layer             next level of abstraction"  
  
  
ENCODER         DECODER         ENCODER-DECODER  
                ONLY            ONLY            (original)  
────────────────────────────────────────────────────────────────  
Attention:      Bidirectional   Causal          Bidirectional +  
                (sees all)      (sees past      Causal +  
                                only)           Cross-attention  
  
Best for:       Understanding   Generation      Transformation  
  
Input:          full sequence   partial         full sequence  
                                sequence  
  
Output:         vectors         next token      full sequence  
  
Examples:       BERT            GPT, Claude     T5, BART  
                RoBERTa         LLaMA           Original (2017)  
  
Used in         Classification  Chatbots        Translation  
practice for:   Sentiment       Code gen        Summarization  
                NER             Creative text   Q&A  
  
  
  
![Positional](assets/AD8059F8-5D6C-493E-90C9-F2E0A1444519.png)  
  
Reinforcement Learning from Human Feedback  
  
  
  
Pretraining:   MASSIVE data, no human labels → learns language  
SFT:           SMALL data, human labels      → learns to follow instructions  
RLHF:          SMALL data, human preferences → learns to be helpful and safe  
  
  
**Concrete dataset sizes used in practice**  

| Model              | Stage             | Dataset size                    |
| ------------------ | ----------------- | ------------------------------- |
| GPT-3 pretraining  | Raw text          | 570 GB of text (~300B tokens)   |
| InstructGPT SFT    | Conversations     | ~13,000 human written examples  |
| InstructGPT RLHF   | Preference pairs  | ~33,000 human comparisons       |
| Claude pretraining | Raw text          | Trillions of tokens (estimated) |
| Claude fine tuning | Constitutional AI | Proprietary                     |
  
**The core idea of Attention**  
For each token, the model asks **3 questions**:  

| Letter | Name  | Question                               |
| ------ | ----- | -------------------------------------- |
| Q      | Query | "What am I looking for?"               |
| K      | Key   | "What do I contain / offer?"           |
| V      | Value | "What do I actually give if selected?" |
