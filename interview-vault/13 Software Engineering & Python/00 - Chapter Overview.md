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
   - **8a. SQL deep dive** — from-scratch execution ([[08.1 - SQL from Scratch How a Query Executes]]) → indexes & execution plans ([[08.2 - SQL Indexes and Query Execution Plans]]) → transactions & ACID ([[08.3 - SQL Transactions ACID and Isolation Levels]]) → engine comparison ([[08.4 - SQL Database Engines Compared]]) → schema design & production tips ([[08.5 - SQL Schema Design Normalization and Production Tips]])
9. **Spark** — essentials + **4 PySpark drills** ([[09 - Spark Essentials]])
10. **PyTorch** — tensors, autograd, training loop + **4 drills** ([[11 - PyTorch Essentials]])
11. **Trap questions** — Python gotchas ([[10 - Python Interview Traps]])
12. **Frontend performance** — DevTools diagnosis, measure-first ([[12 - Frontend Performance Debugging]])

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
| 8a | ↳ SQL from scratch (query execution) | [[08.1 - SQL from Scratch How a Query Executes]] |
| 8b | ↳ Indexes & execution plans | [[08.2 - SQL Indexes and Query Execution Plans]] |
| 8c | ↳ Transactions, ACID & isolation levels | [[08.3 - SQL Transactions ACID and Isolation Levels]] |
| 8d | ↳ Engines compared (Postgres, MySQL...) | [[08.4 - SQL Database Engines Compared]] |
| 8e | ↳ Schema design & production tips | [[08.5 - SQL Schema Design Normalization and Production Tips]] |
| 9 | **Spark** | [[09 - Spark Essentials]] |
| 10 | **PyTorch** | [[11 - PyTorch Essentials]] |
| 11 | **Python traps** | [[10 - Python Interview Traps]] |
| 12 | **Frontend performance** | [[12 - Frontend Performance Debugging]] |

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
