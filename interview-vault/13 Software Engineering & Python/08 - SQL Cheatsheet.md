# SQL Cheatsheet

**Prev:** [[07 - Pandas Cheatsheet]] · **Next:** [[08.1 - SQL from Scratch How a Query Executes]]

**Want the full deep dive?** This note is the quick reference — a dedicated 5-note arc covers SQL from scratch (query execution), indexes & execution plans, transactions/ACID, engine comparisons, and schema design: start at [[08.1 - SQL from Scratch How a Query Executes]].

---

## In plain English

SQL asks questions of **tables**: filter rows, join datasets, aggregate groups. Same logic as pandas groupby/merge — essential for data engineering interviews.

---

## Core query pattern

```sql
SELECT
    department,
    COUNT(*) AS n,
    AVG(salary) AS avg_sal
FROM employees
WHERE hire_date >= '2020-01-01'   -- filter rows BEFORE group
GROUP BY department
HAVING AVG(salary) > 50000      -- filter groups AFTER aggregate
ORDER BY avg_sal DESC
LIMIT 10;
```

| Clause | Runs when | Think |
|--------|-----------|-------|
| WHERE | Before grouping | Row filter |
| HAVING | After grouping | Aggregate filter |
| GROUP BY | — | One row per group key |

---

## Joins

```sql
SELECT a.id, b.order_total
FROM users a
INNER JOIN orders b ON a.id = b.user_id;

-- LEFT: keep all users even without orders
-- RIGHT / FULL: less common
```

| Join | Keeps |
|------|-------|
| INNER | Only matching rows |
| LEFT | All left + matched right |
| OUTER | All from both |

---

## Window functions (very common in interviews)

```sql
SELECT
    user_id,
    order_date,
    amount,
    SUM(amount) OVER (PARTITION BY user_id ORDER BY order_date) AS running_total,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_date DESC) AS rn
FROM orders;
```

**Use:** rankings, running totals, "last event per user" (`WHERE rn = 1`).

---

## CTE (readable pipelines)

```sql
WITH active AS (
    SELECT user_id FROM events WHERE event_date > CURRENT_DATE - 30
)
SELECT u.name FROM users u INNER JOIN active a ON u.id = a.user_id;
```

---

## Common traps

| Trap | Correct |
|------|---------|
| `WHERE avg(salary) > X` | Use **HAVING** for aggregates |
| `COUNT(*)` vs `COUNT(col)` | `COUNT(col)` ignores NULLs |
| `NULL = NULL` is unknown | Use `IS NULL` / `IS NOT NULL` |
| Join without ON → Cartesian product | Always check row count explosion |
| `SELECT *` in pipelines | Name columns explicitly |

---

## 30-second interview answer

> "I structure queries as filter → join → group → having. For per-user rankings or running metrics I use window functions with PARTITION BY instead of correlated subqueries when possible."

---

## Interview coding drills (4 classics)

Schema for all examples:

```sql
-- employees(id, name, dept, salary, hire_date)
-- orders(id, user_id, order_date, amount)
```

### 1. Second highest salary

```sql
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

**Variant (dedupe ties):** use `DENSE_RANK()` or `OFFSET` in window functions.

**Trap:** `LIMIT 1 OFFSET 1` without `DISTINCT` breaks when many share top salary.

---

### 2. Last order per user

```sql
WITH ranked AS (
    SELECT
        user_id,
        order_date,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY order_date DESC
        ) AS rn
    FROM orders
)
SELECT user_id, order_date, amount
FROM ranked
WHERE rn = 1;
```

**Trap:** `MAX(order_date)` alone loses which `amount` belonged to that row.

---

### 3. Running total per user

```sql
SELECT
    user_id,
    order_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY user_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM orders;
```

**Trap:** Missing `ORDER BY` in window → undefined running order.

---

### 4. Departments with avg salary above company avg

```sql
WITH dept_avg AS (
    SELECT dept, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY dept
)
SELECT dept, avg_sal
FROM dept_avg
WHERE avg_sal > (SELECT AVG(salary) FROM employees);
```

**Trap:** Filtering with `WHERE avg_salary > ...` instead of **HAVING** after `GROUP BY` (or use CTE as above).

---

**Next:** [[08.1 - SQL from Scratch How a Query Executes]]
