# Git Essentials

**Prev:** [[01 - Python for Data Science]] · **Next:** [[03 - SQL Essentials]]

---

| Command | Role |
|---------|------|
| `git checkout -b` | Create/switch branch |
| `git add` | Stage changes |
| `git commit` | Snapshot staged |
| `git push` | Upload to remote |

**Branch:** parallel line of development; merge via PR after review.

→ Pipelines that run on push: [[16 DevOps CI CD & Kubernetes/04 - CI CD in Practice]]

---

**Next:** [[03 - SQL Essentials]]
---

## Common traps

| Trap | Correct |
|------|---------|
| pandas iterrows for speed | Use vectorized ops or apply; iterrows is slow |
| SQL SELECT * in production | Select only needed columns; reduces shuffle in Spark too |
