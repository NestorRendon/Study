# Transformers, MoE & Diffusion — Metrics, Comparison & SOTA

**Prev:** [[11- Llama style transformer]] · **Next:** [[08 - LLM Evaluation Metrics]]

---

## Read this first (the whole story)

You already know **what** a transformer does — it reads text and predicts the next token ([[01 - LLM Foundations Encoder and Decoder]]). This note answers three study questions:

1. **How do we measure if a model is learning?** (training metrics)
2. **How do we measure if a model is useful?** (evaluation metrics)
3. **How do dense transformers, MoE, and diffusion differ** — and which metrics matter for each?

Read in order. Each section builds on the previous one. Skip to the comparison tables only after Section 5.

---

## In plain English

Imagine three different ways to create something:

| Analogy | Architecture | What it produces |
|---------|--------------|------------------|
| A student writing an essay **one word at a time**, using their whole brain every word | **Dense transformer** | Text, code, chat |
| A team of **specialists** — only 2 of 8 experts help per word, but the team is huge | **MoE** (Mixture of Experts) | Text, code (frontier scale) |
| An artist **slowly removing blur** from a canvas in 30 passes until a sharp image appears | **Diffusion** | Images, video, audio |

**Metrics** are just **rulers**. Different architectures need different rulers. Comparing a chatbot on FID (an image metric) makes no sense — like grading an essay with a stopwatch alone.

---

## Section 0 — What is a “metric”? (absolute basics)

A **metric** is a number that tells you something about model behavior.

Three families — learn these names:

| Family | When you measure | Question it answers | Example |
|--------|------------------|---------------------|---------|
| **Training** | During training | Is the model learning the data? | Loss ↓, perplexity ↓ |
| **Efficiency** | At deployment | Is it fast and cheap enough? | Tokens/sec, GB VRAM, latency |
| **Evaluation** | After training, on benchmarks | Is it good at real tasks? | MMLU, HumanEval, FID |

```
Training          Efficiency           Evaluation
────────          ──────────           ──────────
"Is it learning?" "Can we afford it?"  "Is it actually good?"
     ↓                  ↓                    ↓
  loss, PPL         params, FLOPs        MMLU, FID, BLEU
```

**Study rule:** Always ask *which family* before quoting a number.

→ Deeper eval rubrics: [[08 - LLM Evaluation Metrics]]

---

## Section 1 — Dense Transformer: the baseline

Start here. Everything else is a variation or a different paradigm.

### 1.1 What it is (30-second recap)

A **dense decoder-only transformer** (GPT, Llama, Mistral):

1. Takes tokens as input
2. Runs **every layer** and **every parameter** on every token
3. Outputs a probability for the **next token**
4. Repeats until done — this is **autoregressive** generation

```
Prompt: "The capital of France is"
         ↓
Model runs ALL weights → predicts " Paris"
         ↓
Append " Paris" → predict " ." → …
```

**Dense** = **all parameters active, all the time.** No shortcuts.

→ Architecture details: [[01 - LLM Foundations Encoder and Decoder]] · [[11- Llama style transformer]]

---

### 1.2 How it learns — training metrics (explained slowly)

#### Loss (Cross-Entropy Loss)

**Intuition:** The model assigns a probability to each possible next token. **Loss** measures how "surprised" it is by the correct answer.

- High loss → model guessed wrong tokens often
- Low loss → model predicts the right next token confidently

**Tiny example:**

| Step | Context | True next token | Model's top guess | Surprised? |
|------|---------|-----------------|-------------------|------------|
| 1 | `"The cat sat on the"` | `mat` | `mat` (60%) | No — low loss |
| 2 | `"Quantum florp"` | `??` | `the` (5%) | Yes — high loss |

Formula (for reference — understand the idea first):

$$\text{Loss} = -\log P(\text{correct token} \mid \text{context})$$

**What you want to see in training:** loss curve goes **down smoothly**. Spikes or flat lines = something wrong (bad data, learning rate, etc.).

---

#### Perplexity (PPL)

**Intuition:** "On average, how many equally likely choices did the model think it had?"

| Perplexity | Meaning in plain English |
|------------|--------------------------|
| **1** | Perfect — always certain of the exact right token |
| **10** | Model felt like choosing among ~10 equally likely tokens |
| **100+** | Very confused — random-ish |

$$\text{PPL} = \exp(\text{average loss})$$

**Example:** PPL = 20 on a news corpus → model behaves like it had a 20-way coin flip at each step.

**Important for study:**
- ✅ Good for **comparing two language models** on the same text
- ❌ **Not enough alone** for chatbot quality — a model can have low PPL but still hallucinate or ignore instructions

---

#### Parameters (the "size" everyone cites)

**Parameter** = one learnable number inside the network (weight or bias).

| Name | What it means |
|------|---------------|
| **7B model** | ~7 billion parameters |
| **70B model** | ~10× larger — generally smarter, but 10× heavier |

**Rough memory rule (inference, FP16):**

$$\text{VRAM for weights} \approx 2 \text{ bytes} \times \text{params}$$

| Model | Params | Weight memory only |
|-------|--------|--------------------|
| Llama 8B | 8B | ~16 GB |
| Llama 70B | 70B | ~140 GB |

Add more VRAM for **KV cache** (past context memory) → [[06 - KV Caching]]

---

### 1.3 Dense transformer — efficiency metrics

These matter when you **deploy** a model (API, app, on-prem).

| Metric | Plain English | Typical goal |
|--------|---------------|--------------|
| **TTFT** (time to first token) | How long until the user sees the first word? | Low — feels responsive |
| **TPOT** (time per output token) | Speed after the first token | High tokens/sec |
| **Tokens/sec** | Throughput | Higher = cheaper at scale |
| **Context length** | Max tokens in prompt + answer | 8k, 128k, 1M… |
| **KV cache memory** | RAM to remember past tokens | Grows with conversation length |

**Worked intuition — TTFT vs TPOT:**

```
User sends long prompt (1000 tokens)
  → TTFT: process all 1000 tokens (slow first response)
  → Then model generates answer token by token (TPOT)
```

---

### 1.4 Dense transformer — evaluation metrics (is it smart?)

Training metrics (loss, PPL) ≠ real-world usefulness. Benchmarks test **tasks**:

| Benchmark | What it tests | Simple analogy |
|-----------|---------------|----------------|
| **MMLU** | Knowledge across 57 subjects (history, law, math…) | Final exam with multiple choice |
| **GSM8K** | Grade-school word problems | Math word problems |
| **HumanEval** | Write Python functions from docstrings | Coding interview |
| **MATH** | Hard competition math | Olympiad-level |
| **MT-Bench** | Multi-turn conversation quality | Chat scored by another LLM |
| **Arena Elo** | Humans pick better answer (A vs B) | Tournament ranking |

**Example scores to anchor your intuition (approximate, 2024–2026 era):**

| Model class | MMLU (rough) | HumanEval (rough) |
|-------------|--------------|-------------------|
| Small (7B–8B) | ~60–75 | ~40–60 |
| Strong open (70B) | ~80–86 | ~70–80 |
| Frontier closed (GPT-4 class) | ~86–90+ | ~85–92 |

**Study tip:** Don't memorize exact numbers — memorize **what each benchmark measures** and **which model size tier** belongs where.

---

### 1.5 Dense transformer — summary card

| | Dense Transformer |
|---|-------------------|
| **Generation** | One token at a time, left → right |
| **Training metric** | Loss ↓, perplexity ↓ |
| **Size metric** | Total parameters (all active) |
| **Speed metric** | Tokens/sec, TTFT, TPOT |
| **Quality metric** | MMLU, HumanEval, Arena Elo |
| **Best for** | Chat, code, RAG, agents — the default text LLM |
| **Examples** | Llama 3, Mistral, GPT-3.5/4 class |

---

## Section 2 — MoE: many experts, few active (building on Section 1)

MoE is still a **transformer** — same autoregressive text generation. What changes is **inside the FFN layers**.

### 2.1 The problem MoE solves

A **70B dense model** is excellent but:
- Expensive to train
- Every token uses all 70B parameters

**Idea:** Build a **much larger** model, but only run a **slice** of it per token.

**Analogy — hospital vs GP clinic:**
- **Dense 7B** = one general doctor handles every patient (whole team always on duty)
- **MoE 8×7B** = eight specialists; each patient sees **two** specialists + shared nurses (reception, triage = shared layers)

→ Full architecture: [[04 - Mixture of Experts MoE]]

---

### 2.2 How MoE works (step by step)

For each token, inside one MoE layer:

```
Token vector x
      ↓
  [Router]  → scores 8 experts → pick Top-2
      ↓
  Expert 3 (math?)  × weight 0.6  ─┐
  Expert 7 (code?)  × weight 0.4  ─┼→ sum → output
  Experts 1,2,4,5,6,8  SKIPPED     ┘
```

**Key numbers (Mixtral 8×7B — memorize this example):**

| | Value | Meaning |
|---|-------|---------|
| **Total params** | ~47B | Full "brain size" stored on disk/GPU |
| **Active params / token** | ~13B | Actually computed per token |
| **Experts** | 8 FFN experts | Specialized sub-networks |
| **Top-K** | 2 | Only 2 experts run per token |

**Interview line:** *"47 billion capacity, 13 billion compute — but you still load all 47B into memory."*

---

### 2.3 MoE — metrics that are NEW (vs dense)

Everything from Section 1 still applies (loss, MMLU, tokens/sec). **Plus these:**

| Metric | What it measures | Why it matters |
|--------|------------------|----------------|
| **Total params** | Full model size | Memory / disk — **all experts loaded** |
| **Active params** | Params used per forward pass | Actual compute cost |
| **Expert utilization** | % of tokens each expert handles | Collapse = one expert does everything |
| **Load-balance loss** | Extra training term | Forces router to spread work evenly |

**Expert collapse (common failure):**

```
BAD:  90% tokens → Expert 1 only   (others wasted)
GOOD: ~12–15% tokens per expert     (balanced)
```

Without load-balance loss, the router gets "lazy" and routes everything to one expert.

---

### 2.4 MoE vs Dense — same metrics, different interpretation

| Metric | Dense 7B | MoE Mixtral 8×7B |
|--------|----------|------------------|
| Total params | 7B | ~47B |
| Active params/token | 7B | ~13B |
| VRAM needed | ~14 GB (weights) | ~90+ GB (all experts) |
| MMLU (approx) | ~62–65 (7B tier) | ~70+ (beats many 70B dense) |
| Compute per token | All 7B | ~13B worth |

**Advantages of MoE:**
- More **capacity** (knowledge) for similar **compute** per token
- Can beat larger dense models on benchmarks

**Disadvantages of MoE:**
- **Memory hungry** — all experts must sit in VRAM
- Harder to train (router instability)
- Harder to fine-tune (which experts to adapt?)

---

### 2.5 MoE — summary card

| | MoE Transformer |
|---|-----------------|
| **Same as dense** | Autoregressive text, loss, MMLU, KV cache |
| **Different** | Router + experts; total ≠ active params |
| **New metrics** | Active params, expert utilization, load-balance loss |
| **Best for** | Frontier models at datacenter scale |
| **Examples** | Mixtral 8×7B, Mixtral 8×22B, DeepSeek-V3, Grok-1 |

---

## Section 3 — Diffusion: a different way to generate (not token-by-token)

This is **not** a small tweak like MoE. Diffusion is a **different learning paradigm**.

### 3.1 The core idea (no math yet)

**Autoregressive (GPT):** build output piece by piece, each step depends on previous pieces.

**Diffusion:** start from **pure noise** and **remove noise step by step** until a clean sample appears.

**Image analogy:**

```
Step 50: ████████  (TV static — pure noise)
Step 40: ░░▒▒░░▒▒  ( vague shapes )
Step 20: 🌫️ blurry cat outline
Step  1: 🐱 sharp cat photo
```

**Text analogy (less common in production):** start with noisy token embeddings, denoise into readable sentences. Research exists (Diffusion-LM) but **GPT-class models dominate chat** because streaming and speed are better.

→ Intro: [[10 -Ststable difussion models]]

---

### 3.2 How diffusion learns — training metrics

Instead of "predict next token," the model learns: **"given noisy data at step t, predict the noise (or the clean version)."**

| Metric | Intuition | Good signal |
|--------|-----------|-------------|
| **Noise prediction MSE** | How wrong is the noise guess? | Goes down steadily |
| **Velocity loss** (flow models) | Variant used in Flux / SD3 class | Same idea — predict correction |

$$\mathcal{L} = \|\epsilon - \epsilon_\theta(x_t, t)\|^2$$

Read as: *"The true noise added minus what the model guessed — minimize the gap."*

**You do NOT use perplexity** as the main training metric for image diffusion.

---

### 3.3 How diffusion generates — efficiency metrics

| Metric | Plain English |
|--------|---------------|
| **Denoising steps (T)** | How many passes from noise → clean (20–50 typical) |
| **Steps/sec** | Speed of generation |
| **Seconds per image** | What the user feels |
| **Latent space** | Compress image before denoising — **8× cheaper** than pixel space (Stable Diffusion trick) |

**Cost formula (intuition):**

$$\text{Total compute} \approx T \text{ steps} \times \text{cost of one forward pass}$$

A 1B-param diffusion model with 50 steps can be **slower** than a 7B transformer generating 100 tokens — because 50 full forward passes add up.

**No KV cache** for classic diffusion — each step is a different noise level, not "append one token."

---

### 3.4 Diffusion — evaluation metrics (completely different rulers)

Do **not** use MMLU for images. Use:

| Metric | Direction | Plain English |
|--------|-----------|---------------|
| **FID ↓** | Lower is better | Do generated images **look real** compared to real photos? (distribution match) |
| **CLIP score ↑** | Higher is better | Does the image **match the text prompt**? |
| **IS ↑** (Inception Score) | Higher | Quality + diversity (older metric, use with FID) |
| **GenEval / T2I-CompBench** | Higher | Can it draw "two red balls left of a blue square"? (composition) |
| **FVD ↓** | Lower | Video version of FID — temporal consistency |
| **Human preference** | — | People pick A vs B (like Arena Elo for images) |

**FID intuition:**

```
Real photos  →  embed in feature space  →  cloud A
Fake images  →  embed in feature space  →  cloud B
FID = distance between cloud A and cloud B
```

Low FID = clouds overlap = realistic.

**CLIP intuition:**

```
Prompt: "a dog wearing sunglasses"
Image → CLIP embedding
Text  → CLIP embedding
Score = cosine similarity (how aligned?)
```

---

### 3.5 Diffusion — summary card

| | Diffusion |
|---|-----------|
| **Generation** | Noise → many denoise steps → sample |
| **Training metric** | Noise MSE (not cross-entropy) |
| **Speed metric** | Steps, seconds/image |
| **Quality metric** | FID, CLIP, GenEval, FVD (video) |
| **Best for** | Images, video, audio |
| **NOT best for** | Production chat (use dense/MoE transformer) |
| **Examples** | Stable Diffusion, Flux, Sora, DALL·E 3 |

---

## Section 4 — Text quality metrics (shared by Dense & MoE)

Both dense and MoE transformers use these when you evaluate **generated text** (not images).

### 4.1 Reference-based (compare to a gold answer)

| Metric | Best for | Weakness |
|--------|----------|----------|
| **BLEU** | Translation | Counts word overlap — ignores meaning |
| **ROUGE** | Summarization | Same |
| **BERTScore** | Semantic similarity | Needs reference text |

**Example — BLEU limitation:**

| Reference | Generated | BLEU |
|-----------|-----------|------|
| `"The cat is on the mat"` | `"A feline sits on the rug"` | Low — but meaning is correct! |

---

### 4.2 LLM-as-a-Judge (modern default for chat)

A stronger model scores your model using a rubric:

| Dimension | Question |
|-----------|----------|
| Correctness | Factually right? |
| Helpfulness | Solves the user's problem? |
| Safety | Policy violations? |

→ [[08 - LLM Evaluation Metrics]]

---

## Section 5 — Now compare all three (you have the foundation)

Read this table **after** Sections 1–3.

### 5.1 Master comparison

| Question | Dense Transformer | MoE | Diffusion |
|----------|-------------------|-----|-----------|
| **How does it generate?** | 1 token at a time | 1 token at a time | T denoise steps |
| **What does it learn?** | Next token (cross-entropy) | Next token + routing | Remove noise (MSE) |
| **All params used?** | Yes — 100% | No — ~20–40% typical | Yes — each step |
| **Main training metric** | Loss, perplexity | Same + load balance | Noise MSE |
| **Main quality metric** | MMLU, HumanEval | Same benchmarks | FID, CLIP |
| **Main speed metric** | Tokens/sec | Tokens/sec (+ routing) | Steps/sec |
| **Streaming chat?** | ✅ Yes | ✅ Yes | ❌ Not natural |
| **KV cache?** | ✅ Yes | ✅ Yes | ❌ No |
| **Dominant use (2026)** | Text, code, agents | Frontier text | Images, video |

### 5.2 Visual flow comparison

```
DENSE / MoE (text)                    DIFFUSION (image)
──────────────────                    ──────────────────

"Write a poem"                        "A cat on a mat"
      ↓                                      ↓
 Token 1 → Token 2 → …               Noise ──→ step 50
      ↓                                       → step 40
 "Roses are red…"                            → …
                                             → sharp image
```

### 5.3 When to pick which (decision guide)

| Your goal | Pick | Because |
|-----------|------|---------|
| Chatbot, RAG, agents | **Dense** 7B–70B | Streaming, ecosystem, fine-tune with LoRA |
| Max quality, big GPU cluster | **MoE** | More capacity per FLOP |
| Single GPU, edge deploy | **Small dense** | MoE still loads all experts |
| Text-to-image product | **Diffusion** | FID/CLIP optimized for pixels |
| Video generation | **Video diffusion** | Sora, Runway class |
| Compare chatbots | MMLU + task eval | Never FID |
| Compare image models | FID + CLIP + human | Never perplexity |

---

## Section 6 — Advantages & disadvantages (study deep)

### Dense Transformer

| ✅ Advantages | ❌ Disadvantages |
|--------------|-----------------|
| Simple to train and deploy | Every param runs every token — costly at huge scale |
| Predictable: size ≈ cost | Quality scales with params + data + compute |
| KV cache, vLLM, LoRA — mature tools | Long context eats VRAM (KV cache grows) |

### MoE

| ✅ Advantages | ❌ Disadvantages |
|--------------|-----------------|
| Huge capacity, moderate compute/token | **All experts in memory** |
| Can beat bigger dense on same FLOPs | Router can collapse without careful training |
| Experts may specialize (code, math…) | Fine-tuning and serving are harder |

### Diffusion

| ✅ Advantages | ❌ Disadvantages |
|--------------|-----------------|
| Beautiful, diverse images/video | Slow — many sequential steps |
| Stable training on pixels/latents | Not the standard for text chat |
| Strong prompt control (guidance scale) | FID alone misses prompt alignment |

---

## Section 7 — State of the art (2024–2026)

> Rankings change every month. Learn **families and trade-offs**, not a frozen leaderboard.

### 7.1 Dense transformers (text)

| Model | Size | Strength |
|-------|------|----------|
| **Llama 3.1** | 8B / 70B / 405B | Best open-weight baseline |
| **Mistral / Ministral** | 7B–123B | Efficient, strong per size |
| **Qwen 2.5** | 0.5B–72B | Multilingual, code |
| **Gemma 2** | 2B–27B | Small models for edge |

### 7.2 MoE (text)

| Model | Total / Active | Note |
|-------|----------------|------|
| **Mixtral 8×7B** | 47B / ~13B | Classic open MoE reference |
| **Mixtral 8×22B** | 141B / ~39B | Larger open MoE |
| **DeepSeek-V3** | ~671B class MoE | Strong open frontier |
| **GPT-4 / 4o** | Undisclosed (likely MoE) | Closed API leader |

### 7.3 Diffusion (multimodal)

| Model | Type | Key metrics |
|-------|------|-------------|
| **Stable Diffusion 3 / SDXL** | Text-to-image | FID, CLIP |
| **Flux** | DiT + flow matching | GenEval, human preference |
| **Sora / Runway / Kling** | Video | FVD |
| **DALL·E 3** | Closed text-to-image | Human eval |

### 7.4 Efficiency tricks (make any model cheaper)

| Trick | Helps | Effect |
|-------|-------|--------|
| **KV caching** | Dense, MoE | Much faster decode |
| **Quantization (INT4/FP8)** | Dense, MoE | 2–4× less memory |
| **LoRA** | Dense, MoE | Cheap fine-tune |
| **Fewer diffusion steps** | Diffusion | SDXL Turbo: 50 → 4 steps |

→ [[05 - LoRA and PEFT]] · [[06 - KV Caching]]

---

## Section 8 — Interview prep (after you understand the basics)

### One-liner

**Dense** = all params every token. **MoE** = many params, few active. **Diffusion** = many steps from noise. Different metrics — never one number.

### Four questions before comparing models

1. **Task?** Text → MMLU/HumanEval. Image → FID/CLIP.
2. **Budget?** VRAM, $/1M tokens, latency.
3. **Deploy?** Single GPU → dense 8B. Cluster → MoE.
4. **Eval?** Task metric + human spot-check — not one benchmark.

### Strong answer example

> "For a RAG chatbot I'd use a **dense 8B** model: one GPU, **KV cache** for streaming, **LoRA** fine-tune. I'd eval **faithfulness** (RAGAS), not BLEU. **Mixtral** would give better MMLU per FLOP but needs ~90 GB for all experts. **Diffusion** is for images — I'd track **FID and CLIP**, not perplexity."

---

## Common traps (memorize these)

| Trap | Correct |
|------|---------|
| "MoE is always faster" | Faster **per active param** — but all experts sit in memory |
| "70B beats 8B always" | Fine-tuned 8B on your domain often wins |
| "Perplexity = good chatbot" | PPL is corpus metric — use task eval |
| "FID = good prompt match" | Add **CLIP score** |
| "Diffusion will replace GPT" | AR transformers win for **text speed + tools** |
| "One MMLU number = best model" | Match benchmark to **your task** |

---

## Key formulas (reference — read concepts first)

**Perplexity:**
$$\text{PPL} = \exp\left(-\frac{1}{N}\sum_i \log P(w_i \mid w_{<i})\right)$$

**MoE output (Top-K routing):**
$$\mathbf{y} = \sum_{i \in \text{TopK}} g_i \cdot \text{Expert}_i(\mathbf{x})$$

**Diffusion training loss:**
$$\mathcal{L} = \mathbb{E}\left[\|\epsilon - \epsilon_\theta(x_t, t)\|^2\right]$$

**Inference cost (intuition):**
- Dense/MoE: $N_{\text{tokens}} \times \text{FLOPs per forward}$
- Diffusion: $T_{\text{steps}} \times \text{FLOPs per step}$

---

## Study path (recommended order)

| Step | Read | You will understand |
|------|------|---------------------|
| 1 | Section 0–1 | Metrics families + dense transformer rulers |
| 2 | Section 2 | Why MoE exists + active vs total params |
| 3 | Section 3 | Why diffusion is different + FID/CLIP |
| 4 | Section 5 | Full comparison table |
| 5 | Section 7 | SOTA landscape |
| 6 | [[08 - LLM Evaluation Metrics]] | RAG, agents, LLM-as-judge |

---

## Related notes

| Topic | Link |
|-------|------|
| Transformer foundations | [[01 - LLM Foundations Encoder and Decoder]] |
| MoE architecture | [[04 - Mixture of Experts MoE]] |
| Diffusion intro | [[10 -Ststable difussion models]] |
| Llama tweaks | [[11- Llama style transformer]] |
| Evaluation deep dive | [[08 - LLM Evaluation Metrics]] |
| Fast inference | [[06 - KV Caching]] |

---

**Prev:** [[11- Llama style transformer]] · **Next:** [[08 - LLM Evaluation Metrics]]
