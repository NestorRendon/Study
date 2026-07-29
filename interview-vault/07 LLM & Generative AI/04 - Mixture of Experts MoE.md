# Mixture of Experts (MoE)

**Prev:** [[03 - Prompting Techniques]] · **Next:** [[05 - LoRA and PEFT]]

---

## Interview one-liner

MoE activates only **K of N expert FFNs** per token — large total capacity, **smaller compute** per forward pass (e.g. Mixtral, rumored GPT-4).

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Architecture

$$\mathbf{g} = \text{softmax}(\mathbf{W}_{router}\mathbf{x})$$

$$\mathbf{y} = \sum_{i \in \text{TopK}(\mathbf{g})} g_i \cdot \text{Expert}_i(\mathbf{x})$$

| Symbol | Meaning |
|--------|---------|
| $\mathbf{x}$ | Token hidden state |
| $\mathbf{g}$ | Router scores over experts |
| TopK | Only K experts run (e.g. 2 of 8) |

**Example:** Mixtral 8×7B — ~47B total params, ~13B **active** per token.

---

## Load balancing

Router may collapse to 1–2 experts → **auxiliary loss** penalizes uneven routing.

| Pros | Cons |
|------|------|
| High capacity, lower inference FLOPs | All experts in memory |
| Specialized experts | Training instability |

---

**Next:** [[05 - LoRA and PEFT]]
---

## Common traps

| Trap | Correct |
|------|---------|
| Lower temperature = smarter | Temperature controls **randomness**, not intelligence |
| Fine-tune full 70B on one GPU without QLoRA | Use LoRA/QLoRA or API |
| Context window = model memory forever | Context is **limited**; older tokens may be lost in long chats |
