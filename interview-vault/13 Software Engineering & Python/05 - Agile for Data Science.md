# Agile for Data Science

**Prev:** [[04 - APIs FastAPI and Flask]] · **Next:** [[15 Interview & Career/00 - Chapter Overview|Interview]]

---

## Interview one-liner

Agile fits DS when you deliver **incremental value**: working code, documented insights, or validated hypotheses each sprint — not only final models.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Principles adapted for DS

| Principle | DS interpretation |
|-----------|-------------------|
| Small iterations | MVP model, baseline metrics first |
| Planning matters | Roadmap even if plans change |
| Knowledge is a deliverable | Document findings, not just notebooks |
| Early returns | Quick wins that de-risk the project |

**Analogy:** gradient descent — small steps toward value, avoid rabbit holes on "cool" algorithms without business impact.

---

**Next chapter:** [[15 Interview & Career/00 - Chapter Overview]]
---

## Common traps

| Trap | Correct |
|------|---------|
| pandas iterrows for speed | Use vectorized ops or apply; iterrows is slow |
| SQL SELECT * in production | Select only needed columns; reduces shuffle in Spark too |
