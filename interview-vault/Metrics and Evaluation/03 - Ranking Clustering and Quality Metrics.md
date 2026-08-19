# Ranking, Clustering and Quality Metrics

**Prev:** [[02 - Classification Metrics]] · **Next:** [[04 - Object Detection and Segmentation Metrics]]

---

## Interview one-liner

Not everything has a single correct label. A search engine returns a **ranked list**, and a clustering algorithm produces **groups with no ground-truth name** — both need their own kind of metric, and both show up constantly in recommender systems, search, and RAG.

---

## In plain English

Two very different "there's no single right answer" problems live in this note:

1. **Ranking quality** — you retrieved 10 documents; some are relevant, some aren't, and *order matters* (a relevant result at position 1 is worth more than one at position 10).
2. **Clustering quality** — you grouped customers into 5 segments; there's no "correct" segment ID to compare against, so you need to measure whether the groups are *good* on their own terms (tight, well-separated), or how well they match a known grouping if you have one.

---

## Part 1 — Ranking metrics

**Notation:** for a query, you get a ranked list of results; each one is either relevant (1) or not (0).

$$\text{Precision@K} = \frac{\text{relevant items in top } K}{K} \qquad \text{Recall@K} = \frac{\text{relevant items in top } K}{\text{total relevant items}}$$

$$\text{MRR} = \frac{1}{|Q|}\sum_{q=1}^{|Q|} \frac{1}{\text{rank}_q} \quad \text{— average of "1 / position of the first relevant result"}$$

$$\text{AP} = \sum_{k=1}^{n} P(k) \cdot \text{rel}(k) \Big/ \text{(number of relevant items)} \qquad \text{MAP} = \frac{1}{|Q|}\sum_{q=1}^{|Q|} \text{AP}_q$$

$$\text{DCG@K} = \sum_{k=1}^{K} \frac{\text{rel}_k}{\log_2(k+1)} \qquad \text{NDCG@K} = \frac{\text{DCG@K}}{\text{IDCG@K}}$$

| Metric | What it captures | Real example |
|--------|----------------------|----------------|
| **Precision@K** | Of the top K results shown, how many were actually relevant | "8 of the top 10 search results were relevant" |
| **Recall@K** | Of everything relevant that exists, how much did the top K catch | Used heavily in **RAG retrieval** — did the top-5 chunks include the one with the answer? |
| **MRR** | How high up was the *first* correct answer | Great for "one right answer" tasks — chatbot FAQ matching, autocomplete |
| **MAP** | Precision averaged across all relevant items' positions, then across queries | Standard for search/IR benchmark comparisons |
| **NDCG** | Like DCG, but normalized against the best possible ordering, and rewards relevant items being **near the top** (log discount) | Handles **graded** relevance (not just relevant/not) — e.g. relevance scored 0-3, as in recommender systems |

---

## Part 2 — Clustering quality metrics

**Without ground-truth labels** (you don't know the "true" groups):

$$\text{Silhouette}(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

where $a(i)$ = average distance from point $i$ to other points in its own cluster, $b(i)$ = average distance to points in the *nearest other* cluster. Ranges $-1$ to $+1$; higher means tighter, better-separated clusters.

$$\text{Davies-Bouldin} = \frac{1}{k}\sum_{i=1}^k \max_{j \neq i} \left(\frac{\sigma_i + \sigma_j}{d(c_i, c_j)}\right)$$

Ratio of within-cluster scatter ($\sigma$) to between-cluster distance ($d$) — **lower is better** (unlike most metrics in this chapter).

**With ground-truth labels** (comparing your clustering to a known correct grouping):

| Metric | What it measures |
|--------|----------------------|
| **Adjusted Rand Index (ARI)** | Agreement between your clustering and the true labels, corrected for chance — 1.0 is perfect, 0 is random |
| **Normalized Mutual Information (NMI)** | How much information the clustering shares with the true labels, normalized to 0-1 |
| **Purity** | For each cluster, what fraction belongs to its most common true class — simple, but rewards over-splitting into many tiny clusters |

---

## Worked example — NDCG

Ranked results with relevance scores $[3, 2, 0, 1]$ (graded 0-3):

$$\text{DCG@4} = \frac{3}{\log_2 2} + \frac{2}{\log_2 3} + \frac{0}{\log_2 4} + \frac{1}{\log_2 5} = 3 + 1.26 + 0 + 0.43 = 4.69$$

Ideal order would be $[3, 2, 1, 0]$:

$$\text{IDCG@4} = \frac{3}{\log_2 2} + \frac{2}{\log_2 3} + \frac{1}{\log_2 4} + \frac{0}{\log_2 5} = 3 + 1.26 + 0.5 + 0 = 4.76$$

$$\text{NDCG@4} = \frac{4.69}{4.76} \approx 0.985$$

Very close to 1 — the ranking is nearly optimal, just one small swap away from perfect.

---

## When to use which

| Situation | Use |
|-----------|-----|
| RAG retrieval — did we get the right chunk in the top K? | Recall@K, sometimes Precision@K |
| Search engine / recommender ranking quality | NDCG (graded relevance), MAP (binary relevance) |
| "One right answer" retrieval (FAQ matching, first correct doc) | MRR |
| Picking the number of clusters $k$, no ground truth | Silhouette score (higher, peak over $k$) or Davies-Bouldin (lower) |
| Validating clustering against a known segmentation | ARI or NMI |

---

## Common traps

| Trap | Why it's wrong | What to say instead |
|------|------------------|----------------------|
| Using accuracy-style metrics on ranked output | Ignores *order* — a relevant result at rank 1 vs rank 10 scores the same | "I'd use NDCG or MRR, which are position-aware" |
| Trusting a high silhouette score blindly | Silhouette assumes convex, roughly equal-sized clusters — misleading on elongated or nested shapes (e.g. DBSCAN-style clusters) | "I'd sanity-check with a visualization (PCA/t-SNE) alongside the score" |
| Using Purity to pick the best clustering | Purity trivially hits 1.0 if every point is its own cluster | "I'd pair it with a metric that penalizes over-fragmentation, like NMI" |
| Reporting Recall@K alone for RAG | Says nothing about whether *irrelevant* chunks are also crowding the context window | "I'd report Precision@K alongside it, since both cost context budget and can hurt generation" |

---

**Next:** [[04 - Object Detection and Segmentation Metrics]]
