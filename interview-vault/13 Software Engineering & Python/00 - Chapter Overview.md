# Chapter 13 — Software Engineering & Python

---

## The story

1. **Python for DS** — idioms and patterns ([[01 - Python for Data Science]])
2. **Version control** — Git workflow ([[02 - Git Essentials]])
3. **Query data** — SQL ([[03 - SQL Essentials]])
4. **Expose models** — APIs ([[04 - APIs FastAPI and Flask]])
5. **Ship in teams** — Agile for DS ([[05 - Agile for Data Science]])
6. **NumPy** — array cheatsheet ([[06 - NumPy Cheatsheet]])
7. **Pandas** — cheatsheet + **4 coding drills** ([[07 - Pandas Cheatsheet]])
8. **SQL** — cheatsheet + **4 query drills** ([[08 - SQL Cheatsheet]])
9. **Spark** — essentials + **4 PySpark drills** ([[09 - Spark Essentials]])
10. **PyTorch** — tensors, autograd, training loop + **4 drills** ([[11 - PyTorch Essentials]])
11. **Trap questions** — Python gotchas ([[10 - Python Interview Traps]])

**Coding drills:** [[01 - Python for Data Science]] (4) · [[07 - Pandas Cheatsheet]] (4) · [[08 - SQL Cheatsheet]] (4) · [[09 - Spark Essentials]] (4) · [[11 - PyTorch Essentials]] (4)

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | Python for DS | [[01 - Python for Data Science]] |
| 2 | Git essentials | [[02 - Git Essentials]] |
| 3 | SQL essentials | [[03 - SQL Essentials]] |
| 4 | APIs | [[04 - APIs FastAPI and Flask]] |
| 5 | Agile for DS | [[05 - Agile for Data Science]] |
| 6 | **NumPy cheatsheet** | [[06 - NumPy Cheatsheet]] |
| 7 | **Pandas cheatsheet** | [[07 - Pandas Cheatsheet]] |
| 8 | **SQL cheatsheet** | [[08 - SQL Cheatsheet]] |
| 9 | **Spark** | [[09 - Spark Essentials]] |
| 10 | **PyTorch** | [[11 - PyTorch Essentials]] |
| 11 | **Python traps** | [[10 - Python Interview Traps]] |

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **PyTorch 2.x** | `torch.compile`, FSDP for scale |
| **Polars / DuckDB** | Faster than pandas for analytics |
| **uv / rye** | Modern Python packaging |
| **dbt + Spark** | Lakehouse ETL standard |

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| Loops over DataFrame rows | **Vectorize** (NumPy/pandas native ops) |
| Forget `optimizer.zero_grad()` | Gradients accumulate — clear each step |
| `CrossEntropyLoss` + manual softmax | Pass **logits** only |
| `fit` scaler on train+test | **Split first**, fit on train only |
| `SELECT *` in production SQL | Name columns; reduces I/O |
| Spark `collect()` on big data | Aggregate/write first; collect small samples |
| Git `commit` without `add` | Stage changes explicitly |
| REST = only JSON POST | GET read, PUT update, DELETE remove — idempotent GET |

---

[[Home|← Home]]
