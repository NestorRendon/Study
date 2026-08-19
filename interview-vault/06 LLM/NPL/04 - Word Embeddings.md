# Word Embeddings

**Prev:** [[03 - TF-IDF and Bag of Words]] · **Next:** [[05 - Topic Modeling and LDA]]

---

## In plain English

Map each word to a **dense vector** so similar meaning → nearby points. Fixes the synonym problem of TF-IDF.

---

## Word2Vec (classic)

**Skip-gram:** predict context from center word.

**Negative sampling:** train on a few random negatives — scalable.

**Famous property:** king − man + woman ≈ queen (linear structure).

---

## Static vs contextual

| | Word2Vec, GloVe | BERT, GPT |
|---|-----------------|-----------|
| One vector per word | Vector **depends on context** |
| "bank" always same | river bank vs money bank differ |

→ Contextual: [[06 - BERT and Contextual NLP]]

---

## Link to RAG

Embedding models (OpenAI, sentence-transformers) power **vector retrieval** → [[03 - Embedding Model Choice]]

---

**Next:** [[05 - Topic Modeling and LDA]]
