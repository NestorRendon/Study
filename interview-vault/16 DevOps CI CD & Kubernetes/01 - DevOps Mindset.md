# DevOps Mindset

**Prev:** [[16 DevOps CI CD & Kubernetes/00 - Chapter Overview]] · **Next:** [[02 - CI CD Concepts]]

---

## In plain English

**DevOps** is not one tool — it is how **dev** and **ops** work together so software ships **faster, safer, and repeatably**. Automation replaces manual server clicking; monitoring tells you when prod breaks.

---

## What problem it solves

| Before | After (DevOps) |
|--------|----------------|
| "Works on my machine" | Same **container image** everywhere |
| Manual deploy Friday night | **Pipeline** deploys with tests |
| Blame between teams | Shared ownership of **uptime + velocity** |

---

## Core practices (memorize)

| Practice | Meaning |
|----------|---------|
| **IaC** | Infrastructure as Code — Terraform, Helm (reproducible envs) |
| **CI** | Every change is built and tested automatically |
| **CD** | Tested artifacts promoted toward production |
| **Observability** | Logs, metrics, traces — know failures fast |
| **Small batches** | Small PRs, frequent deploys, easier rollback |

---

## CALMS (interview acronym)

| Letter | Idea |
|--------|------|
| **C**ulture | Collaboration, no silos |
| **A**utomation | Pipelines, not runbooks |
| **L**ean | Small work in progress |
| **M**easurement | DORA metrics: deploy frequency, lead time, MTTR, change fail % |
| **S**haring | Tools and knowledge across teams |

---

## Where DS/ML fits

| You build | DevOps wraps it |
|-----------|-----------------|
| Training notebook | Scheduled **job** on K8s / cloud |
| FastAPI model API | **Container** + **Deployment** + autoscale |
| Batch scoring | **CronJob** or workflow (Airflow, Argo) |
| RAG service | CI tests retrieval; CD rolls out new index |

→ Your stack: agents + pgvector at xFarm = **service in cluster** + **pipeline** for releases.

---

## Interview one-liner

> "DevOps is shared ownership of delivery: automate build/test/deploy, use containers for consistency, and measure lead time and failure rate — not a separate team that only runs servers."

---

**Next:** [[02 - CI CD Concepts]]
