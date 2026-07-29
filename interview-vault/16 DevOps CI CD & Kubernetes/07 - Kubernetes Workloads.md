# Kubernetes Workloads & Networking

**Prev:** [[06 - Kubernetes Architecture]] · **Next:** [[08 - Kubernetes Ops and ML Deploy]]

---

## In plain English

You rarely create bare **Pods**. You declare **Deployments** (replicas + updates), expose them with **Services**, and route HTTP with **Ingress**.

---

## Object hierarchy (inputs → outputs)

| Object | You specify | Controller creates | Stable network? |
|--------|-------------|-------------------|-----------------|
| **Pod** | 1+ containers, image, env | (ephemeral) | No — IP changes on restart |
| **ReplicaSet** | replicas + pod template | N Pods | No |
| **Deployment** | ReplicaSet + rollout strategy | ReplicaSet + Pods | No (use Service) |
| **Service** | selector + port | virtual IP / DNS name | **Yes** — `my-api:8000` |
| **Ingress** | host, path, TLS | routes to Service | External URL |

---

## Pod (smallest unit)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: api-pod
spec:
  containers:
    - name: api
      image: ghcr.io/org/my-api:abc123
      ports:
        - containerPort: 8000
```

| Field | Meaning |
|-------|---------|
| `containers[]` | One or more (sidecar pattern) |
| `containerPort` | Port process listens on |
| `resources` | CPU/memory requests & limits |

**Trap:** Pod dies → new Pod, **new IP**. Don't point clients at Pod IP.

---

## Deployment (what you use in prod)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-api
  template:
    metadata:
      labels:
        app: my-api
    spec:
      containers:
        - name: api
          image: ghcr.io/org/my-api:abc123
          ports:
            - containerPort: 8000
```

| Input | Output |
|-------|--------|
| `replicas: 3` | 3 Pods with load shared by Service |
| New `image` tag | **Rolling update** — gradual replace |

```bash
kubectl rollout status deployment/my-api
kubectl rollout undo deployment/my-api   # rollback
```

---

## Service (stable internal endpoint)

| Type | Use |
|------|-----|
| **ClusterIP** | Internal only (default) |
| **NodePort** | Open port on each node (dev) |
| **LoadBalancer** | Cloud LB in front |
| **Ingress** | HTTP routing + TLS (most common external) |

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-api
spec:
  selector:
    app: my-api
  ports:
    - port: 80
      targetPort: 8000
```

**Flow:** `Ingress` → `Service:80` → `Pod:8000`

---

## ConfigMap & Secret (config, not image)

| Object | Holds | Mounted as |
|--------|-------|------------|
| **ConfigMap** | Non-secret config | env vars or files |
| **Secret** | passwords, API keys | env vars or files (base64 at rest) |

```yaml
env:
  - name: DATABASE_URL
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: url
```

**Never** bake prod secrets into Docker image.

---

## Labels & selectors

| Label on Pod | `app: my-api` |
| Service `selector` | routes traffic to Pods with matching labels |

---

## Quick reference table

| I need… | K8s object |
|---------|------------|
| Run container | Pod (via Deployment) |
| 3 copies + rolling update | Deployment |
| Stable DNS inside cluster | Service |
| HTTPS public URL | Ingress |
| Non-secret config | ConfigMap |
| API keys | Secret |
| Run once (migration) | Job |
| Cron retrain | CronJob |

---

## Common traps

| Trap | Correct |
|------|---------|
| Expose Pod directly | Use **Service** |
| `replicas: 1` with no PDB | Plan HA for prod APIs |
| Wrong `targetPort` | Must match `containerPort` |

---

**Next:** [[08 - Kubernetes Ops and ML Deploy]]
