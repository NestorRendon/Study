# Chapter — Metrics & Evaluation

**What this chapter is:** the equations behind every "how good is this model?" question — regression, classification, clustering/ranking quality, object detection, neural nets & sequence models, LLMs, knowledge graphs, and how to trust the number you got. Read the ones relevant to your interview; each note stands alone.

**Overview = story only.** Detail notes have full **LaTeX equations**, worked examples, and a table of when to reach for each metric.

---

## The story

Every chapter in this vault trains something. This chapter answers the question that comes right after: **how do you know it's any good?** — and the honest answer changes completely depending on what "it" is.

1. **A number vs a number** — regression metrics ([[01 - Regression Metrics]])
2. **A class vs a class** — classification metrics ([[02 - Classification Metrics]])
3. **A ranked list, or a group, with no single "correct" label** — ranking, clustering & quality metrics ([[03 - Ranking Clustering and Quality Metrics]])
4. **A box in the right place, not just the right class** — object detection & segmentation metrics ([[04 - Object Detection and Segmentation Metrics]])
5. **Is the network actually learning** — NN, RNN & LSTM training metrics ([[05 - Neural Network RNN and LSTM Metrics]])
6. **Generated text, judged by more text** — LLM & generative metrics ([[06 - LLM and Generative Text Metrics]])
7. **A fact, in a graph of facts** — knowledge graph & embedding metrics ([[07 - Knowledge Graph and Embedding Metrics]])
8. **Can you actually trust that number** — evaluation methodology & statistical rigor ([[08 - Evaluation Methodology and Statistical Rigor]])

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | Regression metrics | [[01 - Regression Metrics]] |
| 2 | Classification metrics | [[02 - Classification Metrics]] |
| 3 | Ranking, clustering & quality metrics | [[03 - Ranking Clustering and Quality Metrics]] |
| 4 | Object detection & segmentation metrics | [[04 - Object Detection and Segmentation Metrics]] |
| 5 | Neural network, RNN & LSTM metrics | [[05 - Neural Network RNN and LSTM Metrics]] |
| 6 | LLM & generative text metrics | [[06 - LLM and Generative Text Metrics]] |
| 7 | Knowledge graph & embedding metrics | [[07 - Knowledge Graph and Embedding Metrics]] |
| 8 | Evaluation methodology & statistical rigor | [[08 - Evaluation Methodology and Statistical Rigor]] |

---

## One-page map: task → metric family

| If you're evaluating... | Go to |
|---------------------------|-------|
| Price, demand, any continuous target | [[01 - Regression Metrics]] |
| Spam/not-spam, fraud, disease, multiclass labels | [[02 - Classification Metrics]] |
| Search results, recommendations, customer segments | [[03 - Ranking Clustering and Quality Metrics]] |
| Bounding boxes, instance/semantic segmentation | [[04 - Object Detection and Segmentation Metrics]] |
| "Is my model training correctly," sequence models | [[05 - Neural Network RNN and LSTM Metrics]] |
| Chatbot answers, summarization, translation, RAG | [[06 - LLM and Generative Text Metrics]] |
| Link prediction, entity embeddings, GraphRAG | [[07 - Knowledge Graph and Embedding Metrics]] |
| "Is this improvement real or noise" | [[08 - Evaluation Methodology and Statistical Rigor]] |

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| Reporting accuracy on an imbalanced dataset | Report precision/recall/F1 per class, or PR-AUC — see [[02 - Classification Metrics]] |
| Picking a metric because it's the default in the library | Pick it because it matches the **cost of being wrong** for your actual use case |
| One offline number, no confidence interval | A metric without a spread (bootstrap CI, k-fold std) isn't trustworthy — see [[08 - Evaluation Methodology and Statistical Rigor]] |
| Comparing two models on different test sets | Same test set, same preprocessing, or the comparison is meaningless |
| Treating a metric as the goal | The metric is a **proxy** for the business goal — always sanity-check against it |

---

**Prev:** [[06 LLM/07.1 Transformers & Attention/00 - Chapter Overview]] · **Next:** [[11 Computer Vision/00 - Chapter Overview]]

[[Home|← Home]]
