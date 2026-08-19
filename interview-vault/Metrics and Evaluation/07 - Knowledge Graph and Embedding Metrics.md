# Knowledge Graph and Embedding Metrics

**Prev:** [[06 - LLM and Generative Text Metrics]] · **Next:** [[08 - Evaluation Methodology and Statistical Rigor]]

---

## Interview one-liner

Knowledge graph models are graded the same way a search ranking is: given an incomplete fact, **how highly did the model rank the true missing piece** among every candidate? That's link prediction, and it borrows its metrics almost directly from ranking (see [[03 - Ranking Clustering and Quality Metrics]]), applied to triples instead of documents.

---

## In plain English

A knowledge graph stores facts as triples: `(head, relation, tail)` — e.g. `(Paris, capital_of, France)`. The classic evaluation task is **link prediction**: hide the tail (or head), ask the model to rank every possible entity as the answer, and check where the true answer landed. A model that always ranks the true fact #1 is perfect; one that buries it at #50,000 out of a million entities is useless — accuracy alone can't capture that gradient, which is why ranking-based metrics are the standard here.

---

## The link-prediction setup

Given `(Paris, capital_of, ?)`, the model scores **every entity in the graph** as a candidate for the missing tail, then ranks them by score. The **rank** of the true answer (`France`) in that sorted list is the raw signal every metric below is built from.

---

## Core equations

$$\text{Mean Rank (MR)} = \frac{1}{|Q|}\sum_{q=1}^{|Q|} \text{rank}_q$$

$$\text{MRR} = \frac{1}{|Q|}\sum_{q=1}^{|Q|} \frac{1}{\text{rank}_q}$$

$$\text{Hits@K} = \frac{1}{|Q|}\sum_{q=1}^{|Q|} \mathbb{1}\left[\text{rank}_q \le K\right]$$

| Metric | What it means | Note |
|--------|-------------------|------|
| **Mean Rank** | Average position of the true answer | Lower is better — but sensitive to outliers (one terrible rank of 900,000 skews the average badly) |
| **MRR** | Average of $1/\text{rank}$ | Higher is better (max 1.0) — dominated by how often the *top* answer is right, robust to occasional bad outliers |
| **Hits@K** | Fraction of queries where the true answer was in the top $K$ | The most commonly reported number — usually Hits@1, Hits@3, Hits@10 |

---

## Filtered vs raw ranking — the trap every KG paper handles carefully

If the graph already contains other **true** facts that would also rank highly (e.g. `(Paris, capital_of, France)` AND a duplicate/related true triple), a "raw" ranking unfairly penalizes the model for ranking another *correct* fact above the one you happened to be testing.

**Filtered ranking** removes all other known-true candidates from consideration before computing rank — so the model is only penalized for ranking *actually wrong* answers above the target. Filtered scores are always ≥ raw scores, and it's what's reported in essentially every modern KG embedding paper (TransE, DistMult, ComplEx, RotatE benchmarks).

---

## Worked example

Query: `(Paris, capital_of, ?)`, true answer `France`. The model ranks `France` at position 3 out of 10,000 entities (after filtering out other true facts).

$$\text{Reciprocal Rank for this query} = \frac{1}{3} = 0.33$$

Average this over every test triple to get MRR. If in this same test set another query gets the true answer at rank 1, and another at rank 50, MRR $= \frac{1}{3}\left(\frac{1}{3} + \frac{1}{1} + \frac{1}{50}\right) \approx 0.45$ — notice how the rank-50 miss barely dents MRR, while it would have dragged Mean Rank up a lot. This is exactly why MRR is preferred as the headline metric in most KG papers.

---

## Where this connects in the vault

- The KG concepts these metrics evaluate: [[06 LLM/09 Knowledge Graphs/01 - Knowledge Graph Core Concepts]]
- GraphRAG combines a knowledge graph with retrieval — its retrieval quality is evaluated the same way as any RAG system: [[06 - LLM and Generative Text Metrics]]
- The ranking math (MRR, Hits@K) is the exact same formula family as document ranking — see [[03 - Ranking Clustering and Quality Metrics]]

---

## Common traps

| Trap | Why it's wrong | What to say instead |
|------|------------------|----------------------|
| Reporting raw (unfiltered) rankings | Penalizes the model for correctly ranking *other true facts* highly | "I'd use filtered ranking, which is the standard in the literature" |
| Leading with Mean Rank as the headline number | One catastrophically bad query (rank 900,000 out of a million) skews the average heavily | "I'd lead with MRR or Hits@K, and report Mean Rank only as a secondary diagnostic" |
| Only reporting Hits@10 | A model can look strong at Hits@10 while rarely getting the exact top answer right | "I'd report Hits@1, Hits@3, and Hits@10 together to see the full shape" |
| Treating link-prediction metrics as measuring graph *quality* | They measure how well an embedding model predicts missing links — not whether the graph's facts are correct or complete in the first place | "Data quality of the graph itself is a separate concern — see [[07 Data engineering/Data Quality and Integration Problems]]" |

---

**Next:** [[08 - Evaluation Methodology and Statistical Rigor]]
