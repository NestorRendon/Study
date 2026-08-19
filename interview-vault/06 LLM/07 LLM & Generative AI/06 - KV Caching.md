# KV Caching

**Prev:** [[05 - LoRA and PEFT]] · **Next:** [[07 - Guardrails and Alignment]]

---

## Interview one-liner

During autoregressive generation, **cache past Key and Value** matrices so each new token does not recompute attention over the full history — massive speedup for long outputs.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Without cache

Token $t$ recomputes attention over positions $1 \ldots t$ → $O(t^2)$ per step.

---

## With cache

1. First pass: store $K, V$ for all positions.
2. New token: compute $Q$ for new position only; attend to cached $K, V$ + new.
3. Append new $K, V$ to cache.

| Trade-off | |
|-----------|---|
| Benefit | Lower latency, higher throughput |
| Cost | GPU memory grows with sequence length |

Critical for chat APIs and long-context agents.

---

**Next:** [[07 - Guardrails and Alignment]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Lower temperature = smarter | Temperature controls **randomness**, not intelligence |
| Fine-tune full 70B on one GPU without QLoRA | Use LoRA/QLoRA or API |
| Context window = model memory forever | Context is **limited**; older tokens may be lost in long chats |
