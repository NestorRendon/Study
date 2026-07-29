# CI/CD in Practice

**Prev:** [[03 - Pipeline Stages]] · **Next:** [[05 - Docker and Containers]]

---

## In plain English

Tools differ; **patterns** repeat. Below: **GitHub Actions** (common in startups) — same ideas apply to GitLab CI, Azure Pipelines, CircleCI.


![[Pasted image 20260724093506.png]]
---

## Key concepts (any CI)

| Concept | Meaning |
|---------|---------|
| **Workflow / pipeline** | YAML file defining triggers + jobs |
| **Trigger** | `push`, `pull_request`, `schedule`, `workflow_dispatch` |
| **Job** | Group of steps on one runner |
| **Step** | Single command or action |
| **Runner** | VM/container that executes jobs |
| **Secret** | Encrypted env var (API keys, registry password) |
| **Cache** | Speed up `pip install` / Docker layers |

---

## Minimal GitHub Actions (Python test)

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: ruff check .
      - run: pytest tests/
```

| Trigger | Input | Output |
|---------|-------|--------|
| PR opened | branch code | pass → merge allowed |

---

## Build & push Docker image

```yaml
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v6
        with:
          push: true
          tags: ghcr.io/org/my-api:${{ github.sha }}
```

| Output | Why `github.sha` tag |
|--------|----------------------|
| Immutable image | Traceable to exact commit |

---

## Deploy to Kubernetes (pattern)

| Step | Tool | Action |
|------|------|--------|
| Update manifest | Helm / Kustomize | Set image tag to `${{ github.sha }}` |
| Apply | `kubectl` / Argo CD | Roll out Deployment |
| Verify | CI step | `kubectl rollout status` |

**GitOps variant:** pipeline only updates Git repo; **Argo CD** syncs cluster from Git.

---

## Secrets (never in YAML values)

| Store | Use |
|-------|-----|
| GitHub Secrets | `secrets.AWS_ROLE`, `secrets.KUBE_CONFIG` |
| Vault / cloud SM | Prod credentials |
| OIDC | CI assumes AWS/GCP role without static keys |

---

## Monorepo vs polyrepo

| Layout | CI trick |
|--------|----------|
| Monorepo | `paths:` filter — only run ML job when `models/` changes |
| Polyrepo | One pipeline per service |

---

## DS interview talking points

- "We run **pytest** + **contract tests** on the FastAPI app before image build."
- "Model weights live in **S3**; image pins **version env var** — not 2GB in Git."
- "Staging deploy on every main merge; prod needs **approval** or tag."

---

## Common traps

| Trap | Correct |
|------|---------|
| `latest` tag in CI push | Tag with **git SHA** or semver |
| Secrets in repo | CI secret store only |
| No `needs:` between jobs | Deploy before tests finish |

---

**Next:** [[05 - Docker and Containers]]
