# Text Preprocessing Pipeline

**Prev:** [[01 - What is NLP]] · **Next:** [[03 - TF-IDF and Bag of Words]]

---

## In plain English

Models do not read PDFs — they read **tokens**. Preprocessing turns messy human text into a **clean sequence** your features or neural net can consume.

---

## Standard pipeline

```
Raw text
  → normalize (lowercase, unicode, HTML strip)
  → tokenize (words or subwords)
  → optional: stopword removal (careful with negations!)
  → optional: lemmatize / stem
  → feature step (TF-IDF or embeddings)
```

---

## Tokenization types

| Type | Used in |
|------|---------|
| Whitespace / regex | Classical NLP |
| **BPE / SentencePiece** | GPT, Llama (Ch 7) |

---

## Pragmatic rules

| Do | Avoid |
|----|--------|
| Keep negations ("not good") | Blind stopword removal that drops "not" |
| Normalize URLs, emails consistently | Destroying rare entity strings you need |
| Language detection first | Mixing languages in one index |

---

## Common traps

| Trap | Correct |
|------|---------|
| Preprocess train+test together | Fit rules/stats on **train only** |
| Stemming for modern transformers | Often **not needed** for BERT/GPT — use their tokenizer |

---

**Next:** [[03 - TF-IDF and Bag of Words]]
