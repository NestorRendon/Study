# What is NLP?

**Prev:** [[00 - Chapter Overview]] · **Next:** [[02 - Text Preprocessing Pipeline]]

---

## In plain English

**NLP** teaches computers to work with human language: read, understand, classify, translate, summarize, generate.

---

## The pipeline you should picture

```
Raw text → preprocess → represent (TF-IDF or embeddings) → model → output
```

Each next note adds one step. **Do not skip preprocessing** ([[02 - Text Preprocessing Pipeline]]).

---

## Task map

| Task | Example |
|------|---------|
| Classification | Sentiment, spam |
| NER | Extract person, org, location |
| Translation | EN → ES |
| Summarization | Long doc → short |
| Question answering | Reading comprehension |
| Generation | Chatbots (→ Ch 7 LLM) |

---

## Historical arc (interview narrative)

| Era | Representation | Models |
|-----|----------------|--------|
| Classical | TF-IDF, n-grams | Logistic, SVM |
| Neural embeddings | Word2Vec, GloVe | + shallow nets |
| Contextual | BERT | Encoder transformers |
| Generative LLM | GPT, Llama | Decoder transformers (Ch 7) |

---

**Next:** [[02 - Text Preprocessing Pipeline]]
