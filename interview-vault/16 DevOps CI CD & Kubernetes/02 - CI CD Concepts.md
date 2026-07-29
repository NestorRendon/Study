# CI/CD Concepts

**Prev:** [[01 - DevOps Mindset]] · **Next:** [[03 - Pipeline Stages]]

---

## In plain English

**CI** = merge code often and **prove it still works** (build + test).  
**CD** = get that proven build **to users** safely (staging → production).

People use "CD" for two different things — know both definitions.

---

## CI — Continuous Integration

| Input | Process | Output |
|-------|---------|--------|
| Git push / PR | Compile, lint, unit tests, maybe integration tests | ✅ green build or ❌ fail fast |

**Goal:** find bugs **minutes** after commit, not days later in prod.

---

## CD — two meanings (interview clarity)

| Term | Also called | What happens |
|------|-------------|--------------|
| **Continuous Delivery** | CD (safe) | Every green build is **release-ready**; human clicks deploy |
| **Continuous Deployment** | CD (full auto) | Green build **automatically** goes to production |

Most enterprises: **Continuous Delivery** to prod with approval gate.

---

## Artifact flow

```
Source code  →  CI pipeline  →  artifact (Docker image, wheel, jar)
                                    ↓
                              CD / GitOps  →  running service
```

| Artifact | Typical for Python/ML |
|----------|----------------------|
| Docker image | API + model weights baked in or mounted |
| Python wheel | Library publish to PyPI/private index |
| Model blob | Separate upload to S3 + config tag |

---

## Environments

| Env | Purpose | Data |
|-----|---------|------|
| **dev** | Experiment | Fake / sample |
| **staging** | Prod-like test | Anonymized copy |
| **prod** | Users | Real |

**Rule:** promote the **same image** staging → prod (don't rebuild).

---

## Branch strategies (brief)

| Strategy | Idea |
|----------|------|
| **Trunk-based** | Short-lived branches, main always deployable |
| **GitFlow** | develop / release branches — heavier |
| ML teams | Often trunk + **feature flags** for model versions |

---

## Common traps

| Trap | Correct |
|------|---------|
| "We have Jenkins so we have DevOps" | Culture + practices matter; tool is enabler |
| Skip tests on "hotfix" | Hotfix branch still runs **CI** |
| Different build per environment | Same artifact, different **config** |

---

**Next:** [[03 - Pipeline Stages]]
