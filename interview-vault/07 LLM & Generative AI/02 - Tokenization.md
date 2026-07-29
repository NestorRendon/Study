# Tokenization

**Prev:** [[01 - LLM Foundations Encoder and Decoder]] · **Next:** [[03 - Prompting Techniques]]

---

## In plain English

LLMs do not read letters or words directly — they read **tokens** (integer IDs from a fixed vocabulary). **Tokenization** splits text into those IDs and back. Token count drives **API cost**, **context limits**, and **latency**.

---

## Words vs tokens (examples)

| Text | Words (rough) | Tokens (GPT-4 class, ~) | Note |
|------|---------------|-------------------------|------|
| `Hello world` | 2 | 2 | Often 1 token per common word |
| `ChatGPT` | 1 | 1–2 | May be one merged subword |
| `unhappiness` | 1 | 2–3 | `un` + `happy` + `ness` style splits |
| `PostgreSQL` | 1 | 2–4 | Rare words split more |
| `résumé` | 1 | 2+ | Unicode can add tokens |
| `def train():` | 3 | 4–8 | Code punctuation = extra tokens |
| `🙂👍` | 1–2 emojis | 2–6+ | Often multiple tokens each |

**Interview line:** *"Token count ≠ word count — always measure on the target model."*

---

## Walkthrough: BPE intuition

**Byte Pair Encoding** starts with characters (or bytes), then repeatedly merges the **most frequent pair**.

| Step | Vocabulary (simplified) | Merge |
|------|----------------------|-------|
| 0 | `l`, `o`, `w`, `e`, `r`, `s`, `t` | — |
| 1 | … frequent pair `l`+`o` → `lo` | `lo` |
| 2 | … `lo`+`w` → `low` | `low` |
| 3 | … `low`+`e` → `lowe` | `lowe` |
| 4 | … | eventually `lower`, `newest`, etc. |

**Corpus:** `"lower"`, `"newest"`, `"wider"`  
After training merges, encoding `"lower"` might be **one** token ID; `"widest"` (unseen) might be `wid` + `est` (known pieces).

| Word | BPE pieces (illustrative) |
|------|---------------------------|
| `lower` | `lower` |
| `newest` | `new` + `est` |
| `widest` | `wid` + `est` |

**Why subwords:** open vocabulary — rare words decompose into known pieces instead of `<UNK>`.

---

## Method comparison

| Method | Idea | Used in |
|--------|------|---------|
| **BPE** | Merge frequent pairs | GPT-2/3/4, Llama (variant) |
| **WordPiece** | Merge pair that maximizes likelihood | BERT |
| **SentencePiece** | Treats text as raw Unicode; no English-only pre-split | T5, Llama, multilingual models |
| **Unigram** | Start large, prune low-impact tokens | Some multilingual pipelines |

---

## Same sentence, different tokenizers

Text:

```text
The refund policy applies within 30 days.
```

| Tokenizer (model family) | ~Token count | Why differ |
|--------------------------|--------------|------------|
| `cl100k_base` (GPT-4) | ~10 | English-optimized merges |
| `llama-3` | ~11–14 | Different vocab size / merges |
| `bert-base-uncased` | ~12–15 | WordPiece + `[CLS]`/`[SEP]` if you add them |

**Production rule:** count tokens with the **same encoder** you deploy.

---

## Special tokens (examples)

| Token (concept) | Role |
|-----------------|------|
| `<|endoftext|>` / `<eos>` | End of sequence |
| `<|im_start|>`, `<|user|>`, etc. | Chat template boundaries (model-specific) |
| PAD | Batch padding (BERT training) |
| `[MASK]` | BERT masked LM |
| `<unk>` | Unknown (rare with subword tokenizers) |

**Chat prompt** (what you type) ≠ **what the model sees** — the API adds template tokens:

```text
You write:     "Summarize this PDF."

Model may see:  <|system|>...<|user|>Summarize this PDF.<|assistant|>
                ^^^^^^^^^^^^^^^^^ extra tokens — billable
```

→ [[03 - Prompting Techniques]]

---

## Worked examples with code

### OpenAI (`tiktoken`)

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "The refund policy applies within 30 days."

ids = enc.encode(text)
print(len(ids), ids[:8])           # token count + first IDs
print(enc.decode(ids))               # round-trip text
print(enc.decode([ids[0]]))         # single token piece
```

| Output (illustrative) | Meaning |
|-----------------------|---------|
| `len(ids) == 10` | Bill 10 tokens for this string |
| `decode([ids[0]])` | Might show `"The"` or `"The "` |

### Hugging Face (`transformers`)

```python
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("bert-base-uncased")
text = "unhappiness"
print(tok.tokenize(text))           # ['un', '##happiness']  (WordPiece)
print(tok.encode(text))             # [101, ...]  # includes special ids if added

tok_gpt2 = AutoTokenizer.from_pretrained("gpt2")
print(tok_gpt2.tokenize("unhappiness"))  # different splits than BERT
```

---

## Cost example (API pricing)

Assume **$3 / 1M input tokens** (illustrative).

| Prompt | Tokens | Input cost |
|--------|--------|------------|
| Short question (50 tokens) | 50 | $0.00015 |
| 10-page doc (~8k tokens) | 8,000 | $0.024 |
| 100k context fill | 100,000 | $0.30 |

Adding **10 system lines** of instructions × 1000 requests/day → measure tokens once, multiply.

---

## Multilingual & messy text

| Input | Token behavior |
|-------|----------------|
| `"Bonjour le monde"` | Often **more tokens per character** than English |
| `"你好世界"` | CJK: frequently **1–2 tokens per character** |
| JSON `{"id": 1, "name": "Ada"}` | Brackets, quotes each cost tokens |
| Base64 / long URLs | Very token-heavy — avoid in prompts |
| Repeated spaces | May waste tokens — normalize in preprocessing |

---

## Context window (why tokens matter)

| Model class | Context (tokens, order of magnitude) |
|-------------|----------------------------------------|
| GPT-3.5 | 4k–16k |
| GPT-4 / Llama 3 | 8k–128k+ |

If your RAG injects **6k tokens** of context + **2k** history, you have **8k** before truncation — count everything:

```
system prompt + tools + retrieved chunks + user message + assistant history
```

→ [[08 RAG & Retrieval/06 - Basic RAG Pipeline]]

---

## Decode: tokens → text

| Step | Input | Output |
|------|-------|--------|
| `encode` | string | `List[int]` token IDs |
| model forward | IDs | logits per position |
| `sample` / `argmax` | logits | next token ID |
| `decode` | ID list | string |

Generation stops at **EOS token** or max length.

---

## Interview impacts (summary)

| Factor | Effect |
|--------|--------|
| More tokens | Higher cost, slower, fills context |
| Wrong tokenizer for counting | Underestimate bill on production model |
| Long retrieved docs | RAG eats context — **chunk** smartly |
| Chat templates | Hidden tokens in every request |

---

## Common traps

| Trap | Correct |
|------|---------|
| `len(text.split())` for API billing | Use model **tokenizer** |
| Same English sentence = same tokens everywhere | **Per-model** vocab |
| "100k context = unlimited memory" | Still finite; quality may drop in middle |
| Ignore special/chat tokens in budget | Count **full** rendered prompt |

---

## Interview one-liner

> "Tokenization maps text to subword IDs via BPE or similar; rare words split into pieces, token count sets cost and context, and you must measure with the deployment model's encoder including chat template overhead."

---

**Next:** [[03 - Prompting Techniques]]
