# LoRA & PEFT

**Prev:** [[04 - Mixture of Experts MoE]] · **Next:** [[06 - KV Caching]]

---

## In plain English

**PEFT** (Parameter-Efficient Fine-Tuning) = adapt a huge pretrained model by training **only a small extra piece**, leaving the base weights frozen (or quantized). **LoRA** is the most common PEFT method. **Quantization** shrinks weight memory (FP16 → 4-bit). **QLoRA** = **4-bit base + LoRA** so you can fine-tune a 7B–70B model on one consumer GPU.

---

## The problem PEFT solves

| Approach                    | 7B model trainable weights                    | VRAM (order of magnitude)       |
| --------------------------- | --------------------------------------------- | ------------------------------- |
| **Full fine-tune**          | 7B params × 4 bytes ≈ **28 GB** weights alone | 40–80+ GB with optimizer states |
| **LoRA** (FP16 base frozen) | ~10–50M adapter params                        | ~14–20 GB                       |
| **QLoRA** (4-bit base)      | same adapters                                 | **~6–12 GB**                    |

**Interview line:** *"I don't update all 7B weights — I add a low-rank delta on attention layers, and with QLoRA the frozen base sits in 4-bit."*

---

## LoRA — math

Low rank adaptation 
A LoRA is a sort of finetune that is very very specific. It's **so efficient it can be done in half an hour on a consumer grade gaming computer.** And more importantly: instead of "teaching" the AI multiple concepts, you just teach it a few, typically a single on

![[Pasted image 20260727114652.png]]


Freeze original $W \in \mathbb{R}^{d_{out} \times d_{in}}$. Learn low-rank matrices:

$$W' = W + \Delta W, \quad \Delta W = \frac{\alpha}{r} \, B A$$

| Symbol | Typical shape | Role |
|--------|---------------|------|
| $A$ | $r \times d_{in}$ | Down-projection |
| $B$ | $d_{out} \times r$ | Up-projection |
| $r$ | 4, 8, 16, 32 | **Rank** — capacity of adaptation |
| $\alpha$ | 8, 16, 32 | Scales the update (often $\alpha = r$ or $2r$) |

**Forward:**

$$\mathbf{y} = W\mathbf{x} + \frac{\alpha}{r} \, B(A\mathbf{x})$$

**Init:** $A$ random, $B = 0$ → at step 0, $\Delta W = 0$ (same as base model).

### Tiny numeric sketch

$d_{in} = d_{out} = 1024$, $r = 4$, $\alpha = 8$:

| Piece               | Params                                     |
| ------------------- | ------------------------------------------ |
| Full $W$            | $1024 \times 1024 \approx 1M$              |
| LoRA $A + B$        | $4 \times 1024 + 1024 \times 4 \approx 8K$ |
| **Trainable ratio** | $\approx 0.8\%$ of that layer              |

Applied to **all** $Q, K, V, O$ (and sometimes FFN) across layers → still ≪ 1% of full model.

### Where to attach LoRA

| Module               | Common?           | Why                       |
| -------------------- | ----------------- | ------------------------- |
| Attention $W_Q, W_V$ | **Yes** (default) | Style, task, domain shift |
| $W_K, W_O$           | Sometimes         | Extra capacity            |
| FFN layers           | Optional          | Heavier adapters          |
![[Pasted image 20260723132350.png]]
![[Pasted image 20260723132304.png]]
---

## What is quantization?

**Quantization** = store (and sometimes compute) weights with **fewer bits** than full FP32, using a mapping that preserves approximate values.

### Precision ladder

| Format | Bits | Bytes / param | Typical use |
|--------|------|---------------|-------------|
| **FP32** | 32 | 4 | Training master weights (legacy) |
| **FP16** | 16 | 2 | Training / inference GPU |
| **BF16** | 16 | 2 | Training (wider exponent than FP16) |
| **INT8** | 8 | 1 | Inference speedups |
| **INT4 / NF4** | 4 | 0.5 | QLoRA base, edge inference |

### How weights are compressed (concept)

For each weight block (or tensor chunk):

1. Find scale (and sometimes zero-point):  
   $\text{scale} = \frac{\max(|w|)}{7}$ for 4-bit signed range  
2. Store integers: $w_{int} = \text{round}(w / \text{scale})$  
3. At runtime: $\hat{w} = w_{int} \times \text{scale}$ ( **dequantize** for matmul)

| | Full precision | Quantized |
|---|----------------|-----------|
| **Storage** | 16-bit float | 4-bit code + small scale tensor |
| **Error** | Exact | Small approximation noise |

**Inference-only quantization (GPTQ, AWQ):** compress after training for faster/cheaper **serving** — adapters may be merged or kept separate.

### Quantization vs LoRA (don't confuse)

| | Quantization | LoRA |
|---|--------------|------|
| **Changes** | How $W$ is **stored** | **Adds** trainable $\Delta W$ |
| **Goal** | Less memory / faster inference | Cheap **adaptation** |
| **Trainable** | Usually frozen quantized $W$ | Only $A, B$ |

**QLoRA** combines both: $W$ in 4-bit (frozen), $\Delta W$ in BF16/FP16 (trained).

---

## QLoRA (Quantized LoRA)

```
┌─────────────────────────────────────────┐
│  Base model weights W  →  4-bit (NF4)   │  frozen, ~4× smaller
│  LoRA adapters A, B    →  BF16/FP16     │  trained with AdamW
│  Optimizer states      →  on A, B only  │  tiny vs full model
└─────────────────────────────────────────┘
```

| Piece | Precision | Trained? |
|-------|-----------|----------|
| Frozen backbone $W$ | 4-bit NormalFloat (NF4) | No |
| LoRA $A, B$ | FP16/BF16 | **Yes** |
| Gradients | On adapters only | Yes |

**NF4:** 4-bit format tuned for **neural network weight distributions** (better than raw INT4 for LLMs).

**Double quantization (optional):** also quantize the scale constants — extra memory savings.

---

## PEFT method comparison

| Method | Trainable | Base weights | Best for |
|--------|-----------|--------------|----------|
| **Full fine-tune** | 100% | Updated | Lots of data + multi-GPU |
| **LoRA** | ~0.1–1% | Frozen FP16 | Domain style, tasks |
| **QLoRA** | ~0.1–1% | Frozen **4-bit** | 7B–70B on 1× 24GB GPU |
| **Prefix / prompt tuning** | Soft prompts only | Frozen | Light steering |
| **IA³** | Scales activations | Frozen | Very few params |

---

## Examples (Hugging Face)

### LoRA only (needs more VRAM)

```python
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM

base = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-1B",
    torch_dtype="auto",
    device_map="auto",
)

config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)
model = get_peft_model(base, config)
model.print_trainable_parameters()
# trainable params: ~0.5%  |  all: 1B
```

### QLoRA (4-bit base + LoRA)

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="bfloat16",
    bnb_4bit_use_double_quant=True,
)

base = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-7B",
    quantization_config=bnb_config,
    device_map="auto",
)
base = prepare_model_for_kbit_training(base)

lora_config = LoraConfig(r=8, lora_alpha=16, target_modules=["q_proj", "v_proj"])
model = get_peft_model(base, lora_config)
```

| Step | What happens |
|------|----------------|
| `load_in_4bit` | Weights stored as NF4 in GPU RAM |
| `prepare_model_for_kbit_training` | Enable stable training (layer norm, etc.) |
| `get_peft_model` | Insert LoRA modules; only adapters get grads |

### Training loop (same as normal LM)

```python
# Standard causal LM loss on your JSONL instructions
loss = model(input_ids=..., labels=...).loss
loss.backward()
optimizer.step()
```

### Merge adapters for deployment (optional)

```python
merged = model.merge_and_unload()  # W_eff = W + BA baked in
merged.save_pretrained("merged-llama-domain")
```

| Deploy option | Pros |
|---------------|------|
| **Merged FP16** | Single model, no PEFT runtime |
| **Base + adapter** | Swap LoRA per customer without duplicating base |
| **Quantized inference** | AWQ/GPTQ on merged model for cheap serving |

---

## When to use what (pragmatic)

| Situation | Choice |
|-----------|--------|
| Change tone/format on 7B, 1 GPU | **QLoRA** |
| Best quality, multi-GPU | Full fine-tune or LoRA on FP16 |
| Update facts on private docs | **RAG** first; LoRA if style/reasoning needed |
| Serve cheaply at scale | Quantized inference (INT4/8) + optional LoRA merge |
| Interview at xFarm | "We used agents + RAG; LoRA when we needed domain phrasing" |

→ [[06 LLM/08 RAG & Retrieval/00 - Chapter Overview]]

---

## Memory example (7B model, rough)

| Setup | Weight memory only |
|-------|-------------------|
| FP32 full | ~28 GB |
| FP16 full | ~14 GB |
| 4-bit base | ~3.5 GB |
| 4-bit + LoRA r=16 | ~3.5 GB + ~0.1 GB adapters + optimizer on adapters |

Still need activations for long context — QLoRA enables **training**, not infinite context.

---

## Interview one-liner

> "LoRA learns a low-rank delta on frozen attention weights; quantization stores those weights in fewer bits; QLoRA trains BF16 LoRA adapters on a 4-bit NF4 backbone so fine-tuning fits one GPU — RAG handles facts, LoRA handles behavior and domain language."

---

## Common traps

| Trap | Correct |
|------|---------|
| "QLoRA updates 4-bit weights directly" | Base is **frozen**; **LoRA** matrices are trained |
| "Quantization = LoRA" | Quantization = compression; LoRA = adaptation |
| LoRA rank $r$ = model quality always | Higher $r$ = more capacity but more VRAM |
| Merge LoRA without testing | Merged model can **drift** — eval before prod |
| Fine-tune instead of RAG for handbook Q&A | **RAG** for changing facts; LoRA for style/task |

---

**Next:** [[06 - KV Caching]]
