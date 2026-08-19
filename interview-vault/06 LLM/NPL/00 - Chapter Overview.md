# Chapter 6 — NLP & Text Mining

---

## The story

1. **What is NLP** — tasks and pipeline mental model ([[01 - What is NLP]])
2. **Preprocess** — clean, tokenize, normalize ([[02 - Text Preprocessing Pipeline]])
3. **Classical features** — TF-IDF, bag of words ([[03 - TF-IDF and Bag of Words]])
4. **Dense meaning** — word embeddings ([[04 - Word Embeddings]])
5. **Topics** — LDA ([[05 - Topic Modeling and LDA]])
6. **Contextual models** — BERT bridge to Ch 7 ([[06 - BERT and Contextual NLP]])

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | What is NLP? | [[01 - What is NLP]] |
| 2 | **Preprocessing first** | [[02 - Text Preprocessing Pipeline]] |
| 3 | TF-IDF & bag of words | [[03 - TF-IDF and Bag of Words]] |
| 4 | Word embeddings | [[04 - Word Embeddings]] |
| 5 | Topic modeling (LDA) | [[05 - Topic Modeling and LDA]] |
| 6 | BERT & contextual NLP | [[06 - BERT and Contextual NLP]] |

---

## SOTA & trends (2024–2026)

| Trend | What to say |
|-------|-------------|
| **Transformers everywhere** | BERT/RoBERTa for understanding; GPT-style for generation |
| **Embeddings API** | OpenAI/Cohere/voyage — retrieval standard for RAG |
| **Small language models** | Fine-tuned 7B–13B on domain beat giant general models |
| **RAG over fine-tune** | Default for enterprise Q&A on private docs |
| Classical TF-IDF | Still strong baseline for search, legal keyword match |

---

## Common traps

| Trap | Correct |
|------|---------|
| Skip preprocessing | Cleaning + tokenization affects everything downstream |
| TF-IDF = semantics | **Lexical** only — use embeddings |
| LDA topics without human read | Topics need **interpretation** |

---

**Prev:** [[05 Deep Learning/00 - Chapter Overview]] · **Next:** [[06 LLM/07 LLM & Generative AI/00 - Chapter Overview]]

[[Home|← Home]]
