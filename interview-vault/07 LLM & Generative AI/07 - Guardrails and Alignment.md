# Guardrails & Alignment

**Prev:** [[06 - KV Caching]] · **Next:** [[08 - LLM Evaluation Metrics]]

---

## Interview one-liner

**Guardrails** filter unsafe inputs/outputs. **Alignment** trains models to follow human intent and safety policies (RLHF, DPO, classifier filters like LlamaGuard).

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Guardrail pipeline

```
User input → Input guardrail → LLM → Output guardrail → Response
```

| Layer | Blocks |
|-------|--------|
| Input | Jailbreaks, PII injection |
| Output | Toxicity, violence, policy violations |

**LlamaGuard:** safety classifier on categories (violence, self-harm, illegal activity, harassment).

---

## Alignment problem

Base LLM optimizes **next-token prediction**, not **human values**.

| Approach | Idea |
|----------|------|
| RLHF | Reward model from human preferences |
| DPO | Direct preference optimization without explicit RM |
| Constitutional AI | Model critiques its own outputs |

---

**Next:** [[08 - LLM Evaluation Metrics]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Lower temperature = smarter | Temperature controls **randomness**, not intelligence |
| Fine-tune full 70B on one GPU without QLoRA | Use LoRA/QLoRA or API |
| Context window = model memory forever | Context is **limited**; older tokens may be lost in long chats |
