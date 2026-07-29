# SQL Essentials

**Prev:** [[02 - Git Essentials]] · **Next:** [[04 - APIs FastAPI and Flask]]

---

## Four main clauses

```sql
SELECT column, AGG(column)
FROM   table
WHERE  condition
GROUP BY column
HAVING aggregate_condition
ORDER BY column;
```

| Clause | Role |
|--------|------|
| SELECT | Columns / aggregates |
| FROM | Tables |
| WHERE | Row filter (before group) |
| GROUP BY | Buckets for aggregation |
| HAVING | Filter on aggregates |
| JOIN | Combine tables on keys |

---

**Next:** [[04 - APIs FastAPI and Flask]]
---

## Common traps

| Trap | Correct |
|------|---------|
| pandas iterrows for speed | Use vectorized ops or apply; iterrows is slow |
| SQL SELECT * in production | Select only needed columns; reduces shuffle in Spark too |
