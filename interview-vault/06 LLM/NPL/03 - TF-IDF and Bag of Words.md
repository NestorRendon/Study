# TF-IDF & Bag of Words

**Prev:** [[02 - Text Preprocessing Pipeline]] · **Next:** [[04 - Word Embeddings]]

---

## In plain English

Turn each document into a **vector of word counts or weights**. Documents with similar words score as similar — but **synonyms** are missed.

---

## Bag of Words

$$x_j = \text{count of word } j \text{ in document}$$

Order is ignored — "dog bites man" = "man bites dog".

---

## TF-IDF

$$\text{TF-IDF}(t,d) = \text{TF}(t,d) \times \log\frac{N}{\text{df}(t)}$$

| Term | Meaning |
|------|---------|
| TF | How often term appears in doc |
| IDF | Down-weights terms in many docs |

![TF-IDF](assets/1BEDB9CD-CA68-44B6-8D18-93246609AA6E.png)

---

## When to use (pragmatic)

| Use TF-IDF/BM25 | Use embeddings instead |
|-----------------|------------------------|
| Keyword search, legal cites | Paraphrase questions |
| Baseline classifier | Semantic similarity |
| Hybrid RAG (with dense) | [[05 - Retrieval Quality]] |

---

**Next:** [[04 - Word Embeddings]]
