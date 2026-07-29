# Chapter 16 — DevOps, CI/CD & Kubernetes

**What this chapter is:** how code moves from **commit → tested artifact → running service** in production. Organized for data/ML engineers who ship models and APIs, not only pure SRE roles.

**Overview = story only.** Detail notes hold concepts, YAML patterns, traps, and interview lines.

**Prerequisite:** [[13 Software Engineering & Python/02 - Git Essentials]] · [[13 Software Engineering & Python/04 - APIs FastAPI and Flask]]

---

## The story (production path)

1. **DevOps mindset** — culture + automation goals ([[01 - DevOps Mindset]])
2. **CI vs CD** — integration, delivery, deployment ([[02 - CI CD Concepts]])
3. **Pipeline stages** — lint → test → build → deploy ([[03 - Pipeline Stages]])
4. **CI in practice** — GitHub Actions / GitLab patterns ([[04 - CI CD in Practice]])
5. **Docker** — image, container, why K8s needs it ([[05 - Docker and Containers]])
6. **Kubernetes architecture** — control plane, nodes, etcd ([[06 - Kubernetes Architecture]])
7. **K8s workloads** — Pod, Deployment, Service, Ingress ([[07 - Kubernetes Workloads]])
8. **Config, ops & ML deploy** — Secrets, probes, model serving ([[08 - Kubernetes Ops and ML Deploy]])

---

## Big picture (one diagram)

```mermaid
flowchart LR
    subgraph dev [Developer]
        CODE[Code + tests]
        GIT[Git push]
    end
    subgraph ci [CI/CD]
        LINT[Lint]
        TEST[Test]
        BUILD[Build image]
        PUSH[Push registry]
    end
    subgraph run [Runtime]
        K8S[Kubernetes]
        POD[Pods]
        SVC[Service / Ingress]
    end
    CODE --> GIT --> LINT --> TEST --> BUILD --> PUSH --> K8S --> POD --> SVC
```

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | DevOps mindset | [[01 - DevOps Mindset]] |
| 2 | CI/CD concepts | [[02 - CI CD Concepts]] |
| 3 | Pipeline stages | [[03 - Pipeline Stages]] |
| 4 | CI/CD in practice | [[04 - CI CD in Practice]] |
| 5 | Docker & containers | [[05 - Docker and Containers]] |
| 6 | K8s architecture | [[06 - Kubernetes Architecture]] |
| 7 | K8s workloads | [[07 - Kubernetes Workloads]] |
| 8 | Ops & ML on K8s | [[08 - Kubernetes Ops and ML Deploy]] |

---

## CI/CD vs Kubernetes (one table)

| | CI/CD pipeline | Kubernetes |
|---|----------------|--------------|
| **When** | On every commit / release | Always running |
| **Job** | Build, test, publish artifact | Schedule containers, heal, scale |
| **Output** | Image in registry, passing tests | Pods serving traffic |
| **Tool examples** | GitHub Actions, GitLab CI | `kubectl`, Helm, Argo CD |

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **GitOps** | Git = source of truth; Argo CD / Flux sync cluster |
| **OIDC to cloud** | CI pipelines assume roles without long-lived keys |
| **ML platforms** | Kubeflow, KServe, BentoML on K8s |
| **Serverless GPUs** | Some teams skip K8s for batch; K8s still default for APIs |

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| "CI = deploy to prod" | CI = **integrate**; CD = **deliver/deploy** (definitions vary by team) |
| "Kubernetes = Docker" | K8s **orchestrates** containers; Docker **builds/runs** them |
| No health checks | **Liveness** vs **readiness** probes |
| Latest tag in prod | Pin **image digest** or semver tag |
| Secrets in Git | Use **Secrets** / vault / CI secret store |

---

**Prev:** [[14 C++ for Data Science & Engineering/00 - Chapter Overview]] · **Next:** [[15 Interview & Career/00 - Chapter Overview]]

[[Home|← Home]]
