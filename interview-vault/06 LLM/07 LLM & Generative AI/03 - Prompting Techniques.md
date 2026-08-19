# Prompting Techniques

**Prev:** [[02 - Tokenization]] · **Next:** [[04 - Mixture of Experts MoE]]

---

## Zero-shot

Instruction only — no examples.

```
Classify sentiment as positive or negative:
"The product exceeded expectations."
```

Works when task is simple and model is strong.

---

## Few-shot

Provide input–output examples; model infers the pattern.

```
Sentence: I love it. → Positive
Sentence: Terrible.   → Negative
Sentence: Amazing service. →
```

---

## Chain-of-Thought (CoT)

Ask model to **reason step by step** before the final answer — improves math and multi-step logic.

---

## Prompt chaining

Output of step 1 becomes input of step 2 — decompose complex pipelines.

---

## Prompt hygiene (avoid)

- Vague instructions
- Contradictory constraints
- No output format spec when structure matters
- Stuffing irrelevant context (dilutes attention)

→ Used heavily in [[06 - Basic RAG Pipeline|RAG]] systems

---

**Next:** [[04 - Mixture of Experts MoE]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Lower temperature = smarter | Temperature controls **randomness**, not intelligence |
| Fine-tune full 70B on one GPU without QLoRA | Use LoRA/QLoRA or API |
| Context window = model memory forever | Context is **limited**; older tokens may be lost in long chats |
