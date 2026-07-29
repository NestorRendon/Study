# Structure Learning

**Prev:** [[04 - ANOVA vs ANCOVA]] · **Next:** [[06 - Bayesian Machine Learning]]

---

## In plain English

Learn **who causes whom** from data — the graph structure (DAG), not just correlation strengths.

---

## Structure vs parameters

| | Structure learning | Parameter learning |
|---|-------------------|-------------------|
| Finds | Which edges exist | Strength of known edges |
| Example | "Smoking → Cancer?" | "Effect size given graph" |

---

## Causal caution

Observational data alone cannot prove causation without assumptions (no unmeasured confounders, correct DAG).

**Tools:** do-calculus, instrumental variables, RCTs.

---

## Common traps

| Trap | Correct |
|------|---------|
| "ML feature importance = causation" | Importance ≠ causal effect |
| Learn DAG without domain input | Combine data + **expert constraints** |

---

**Next:** [[06 - Bayesian Machine Learning]]
