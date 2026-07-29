# APIs (FastAPI & Flask)

**Prev:** [[03 - SQL Essentials]] · **Next:** [[05 - Agile for Data Science]] · Deploy: [[16 DevOps CI CD & Kubernetes/00 - Chapter Overview]]

---

## Interview one-liner

Expose models as **REST** endpoints. **FastAPI** = modern, async, auto OpenAPI docs. **Flask** = lightweight, flexible.

| | FastAPI | Flask |
|---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*
|---------|-------|
| Async | Native | Via extensions |
| Validation | Pydantic types | Manual |
| Docs | Auto Swagger | Add-on |

**Serving:** Gunicorn/Uvicorn workers behind reverse proxy; **WSGI/ASGI** interfaces.

**DS use:** model scoring API, RAG backend, agent tool endpoints.

---

**Next:** [[05 - Agile for Data Science]]
---

## Common traps

| Trap | Correct |
|------|---------|
| pandas iterrows for speed | Use vectorized ops or apply; iterrows is slow |
| SQL SELECT * in production | Select only needed columns; reduces shuffle in Spark too |
