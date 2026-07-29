# Kubernetes Ops & ML Deploy

**Prev:** [[07 - Kubernetes Workloads]] · **Next:** [[15 Interview & Career/00 - Chapter Overview|Career (Ch 15)]]

---

## In plain English

Running in prod means **health checks**, **resources**, **observability**, and **safe rollouts**. ML adds **GPU nodes**, **large artifacts**, and **batch jobs**.

---

## Probes (liveness vs readiness)

| Probe | Question | Fail action |
|-------|----------|-------------|
| **Liveness** | Is process deadlocked? | **Restart** Pod |
| **Readiness** | Can it take traffic? | Remove from Service endpoints |
| **Startup** | Slow boot (big model load)? | Delay liveness until OK |

```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 10
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 30
```

**ML API:** readiness until model loaded; liveness lighter (process up).

---

## Resources (requests & limits)

```yaml
resources:
  requests:
    cpu: "500m"
    memory: "1Gi"
  limits:
    memory: "2Gi"
```

| Field | Scheduler uses | kubelet enforces |
|-------|----------------|------------------|
| **requests** | Placement | minimum guaranteed |
| **limits** | — | OOM kill if memory exceeded |

**GPU:** `resources.limits.nvidia.com/gpu: 1` on GPU node pools.

---

## Horizontal Pod Autoscaler (HPA)

| Input metric | Scale |
|--------------|-------|
| CPU % | More replicas |
| Custom metric | e.g. requests/sec, queue depth |

**ML caveat:** GPU scaling is harder — often queue-based workers.

---

## ML deployment patterns

| Pattern | K8s object | When |
|---------|------------|------|
| **Real-time API** | Deployment + Service + Ingress | FastAPI, TorchServe, Triton |
| **Batch scoring** | Job or CronJob | Nightly predictions |
| **Training** | Job / Kubeflow / cloud notebook | Heavy GPU, ephemeral |
| **Vector DB** | StatefulSet | pgvector, Qdrant with PVC |

### Serving flow (your interview story)

```
CI: test → build image → push registry
CD: update Deployment image tag → rolling update
Pod: download weights from S3 on start OR sidecar refresh
Ingress: HTTPS to /predict
```

Link: [[08 RAG & Retrieval/06 - Basic RAG Pipeline]] · [[13 Software Engineering & Python/04 - APIs FastAPI and Flask]]

---

## Observability trio

| Pillar | Tool examples | DS use |
|--------|---------------|--------|
| **Logs** | CloudWatch, Loki, ELK | Request errors, retrieval misses |
| **Metrics** | Prometheus + Grafana | Latency p99, GPU util |
| **Traces** | OpenTelemetry, Jaeger | Agent tool-call chains |

---

## GitOps (modern CD)

| Piece | Role |
|-------|------|
| Git repo | Desired manifests (Helm/Kustomize) |
| Argo CD / Flux | Sync cluster ↔ Git |
| CI | Build image + bump tag in Git |

**Benefit:** auditable rollbacks (`git revert`).

---

## Security basics

| Practice | Why |
|----------|-----|
| RBAC | Limit prod `kubectl` access |
| NetworkPolicy | Pod-to-pod firewall |
| Non-root container | Smaller blast radius |
| Scan images in CI | CVE gate |

---

## End-to-end I/O (whole system)

| Step | Input | Output |
|------|-------|--------|
| Developer | code commit | Git SHA |
| CI | SHA + Dockerfile | image `my-api:SHA` in registry |
| CD / GitOps | manifest with tag SHA | Deployment rollout |
| K8s | Deployment spec | Running Pods |
| Service | Pod endpoints | stable cluster DNS |
| Ingress | HTTP request | routed to Pod |
| User | HTTPS | JSON response |

---

## Interview one-liner

> "CI builds and tags an immutable image; Kubernetes Deployment rolls it out with readiness probes; Service and Ingress expose it; for ML I separate large weights in object storage and autoscale on CPU or queue depth, with logs and metrics for retrieval quality in prod."

---

## Common traps (chapter recap)

| Trap | Correct |
|------|---------|
| Liveness hits `/predict` with heavy model | Cheap `/health` endpoint |
| No resource requests | Pods evicted or starve node |
| Train in Deployment | Training = **Job**; serving = **Deployment** |

---

**Next chapter:** [[15 Interview & Career/00 - Chapter Overview]]
