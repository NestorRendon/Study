# Docker & Containers

**Prev:** [[04 - CI CD in Practice]] · **Next:** [[06 - Kubernetes Architecture]]

---

## In plain English

A **container** is a running process isolated with its own filesystem. A **Docker image** is the **snapshot recipe** CI builds once; K8s runs many copies of it as **Pods**.

---

## Image vs container

| | Image | Container |
|---|-------|-----------|
| **What** | Read-only template (layers) | Running instance |
| **Analogy** | Class | Object |
| **Built by** | `docker build` | `docker run` / K8s |
| **Stored in** | Registry (ECR, GCR, ghcr.io) | Node disk (ephemeral) |

---

## Dockerfile basics (Python API)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

| Instruction | Role |
|-------------|------|
| `FROM` | Base image |
| `COPY` | Add files (order matters for cache) |
| `RUN` | Build-time command |
| `CMD` | Default start command |

---

## Essential commands

| Command | Does |
|---------|------|
| `docker build -t my-api:v1 .` | Build image |
| `docker run -p 8000:8000 my-api:v1` | Run locally |
| `docker ps` | Running containers |
| `docker logs <id>` | Stdout/stderr |
| `docker push registry/my-api:v1` | Publish for K8s |

---

## Why Kubernetes needs containers

| Without K8s | With K8s |
|-------------|----------|
| Run container on one VM manually | Scheduler places Pods on **cluster** |
| Restart by hand | **Controller** restarts crashed Pods |
| Scale = bigger VM | **ReplicaSet** → N Pods |

K8s does **not** replace Docker build — it **runs** images at scale.

---

## Volumes & ML

| Pattern | Use |
|---------|------|
| **Baked-in model** | Small model inside image |
| **Mount S3 / PVC** | Large weights at runtime |
| **Env vars** | `MODEL_VERSION=3` |

---

## Common traps

| Trap | Correct |
|------|---------|
| Run as root in prod | `USER` non-root in Dockerfile |
| Huge context in build | `.dockerignore` for data/, `.git` |
| Mutable `latest` in prod | Pin SHA or semver tag |

---

**Next:** [[06 - Kubernetes Architecture]]
