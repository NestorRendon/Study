# Topic Modeling & LDA

**Prev:** [[04 - Word Embeddings]] · **Next:** [[06 - BERT and Contextual NLP]]

---

## In plain English

Discover **hidden themes** in a pile of documents without labels. Each doc = mixture of topics; each topic = distribution over words.

---

## LDA (Latent Dirichlet Allocation)

Generative story:
1. Pick topic mixture $\theta_d$ for document $d$
2. For each word: pick topic $z$, then pick word from topic's word distribution

![Topics](assets/0C77E5B5-4F14-4AD4-A3C1-80C102E5FC93.jpg)

---

## When to use

| Use LDA | Skip LDA |
|---------|----------|
| Explore corpus themes | Need precise QA |
| Tag thousands of docs cheaply | Need SOTA generation |

**Modern alt:** embedding + clustering, or LLM summarization of clusters.

---

**Next:** [[06 - BERT and Contextual NLP]]
