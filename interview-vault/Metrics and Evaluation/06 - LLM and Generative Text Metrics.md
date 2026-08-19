# LLM and Generative Text Metrics

**Prev:** [[05 - Neural Network RNN and LSTM Metrics]] · **Next:** [[07 - Knowledge Graph and Embedding Metrics]]

---

## Interview one-liner

There's no confusion matrix for "was this a good paragraph." LLM evaluation is a ladder: cheap n-gram overlap metrics (BLEU/ROUGE) at the bottom, embedding-based similarity in the middle, and LLM-as-judge / human evaluation at the top — each step more expensive and closer to what a human would actually say.

---

## In plain English

Grading generated text is fundamentally different from classification: there's rarely one correct output, two good answers can share zero words, and "correct" isn't even well-defined for open-ended generation. So the field uses a mix of cheap automatic proxies (fast, reproducible, but shallow) and expensive judgment-based methods (slower/costlier, but actually track quality).

*This note is the equations/cheat-sheet layer. For the fuller strategic picture (when to use which, agent-specific eval, a pragmatic minimal eval set), see [[06 LLM/07 LLM & Generative AI/08 - LLM Evaluation Metrics]] and [[06 LLM/08 RAG & Retrieval/10 - RAG Evaluation]].*

---

## Perplexity — how confused is the model?

$$\text{Perplexity} = \exp\left(-\frac{1}{N}\sum_{i=1}^N \log P(w_i \mid w_{<i})\right)$$

The exponentiated average negative log-likelihood the model assigns to the *actual* next tokens in a held-out text. Lower is better. It measures how well the model predicts real language — **not** whether a generated answer is factually correct or helpful, which is why it's used mainly to compare base/pretrained language models, not to grade chatbot answers.

---

## Reference-based n-gram overlap (BLEU, ROUGE)

These compare generated text against one or more human-written reference texts, by counting overlapping word sequences (n-grams).

$$\text{BLEU} = \text{BP} \cdot \exp\left(\sum_{n=1}^{N} w_n \log p_n\right), \qquad \text{BP} = \min\left(1,\ e^{1 - r/c}\right)$$

$p_n$ = precision of $n$-grams (what fraction of generated $n$-grams appear in the reference), $\text{BP}$ = brevity penalty ($r$ = reference length, $c$ = candidate length) that stops the model from gaming the score by generating very short, "safe" text. **Precision-oriented** — built for translation.

$$\text{ROUGE-N} = \frac{\sum_{\text{gram}_n \in \text{ref}} \text{Count}_{\text{match}}(\text{gram}_n)}{\sum_{\text{gram}_n \in \text{ref}} \text{Count}(\text{gram}_n)}$$

**Recall-oriented** — "how much of the reference's content did the generated text capture." Built for summarization. `ROUGE-L` uses longest common subsequence instead of fixed n-grams, so it tolerates word reordering better.

| | BLEU | ROUGE |
|---|------|-------|
| **Orientation** | Precision (don't say things the reference didn't) | Recall (don't miss what the reference said) |
| **Classic use case** | Machine translation | Summarization |
| **Shared weakness** | Both are surface n-gram overlap — a perfectly good paraphrase with different wording scores low |

---

## Embedding-based: BERTScore

Instead of exact word overlap, embed each token in both the candidate and reference with a model like BERT, then match tokens by **cosine similarity** rather than exact string match:

$$\text{BERTScore}_{P} = \frac{1}{|\hat{x}|}\sum_{\hat{x}_j \in \hat{x}} \max_{x_i \in x} \cos(\hat{x}_j, x_i)$$

This captures paraphrases and synonyms that BLEU/ROUGE would score as wrong, at the cost of needing another model to compute the score.

---

## LLM-as-a-judge and human evaluation

The most reliable methods, also the most expensive:

| Method | How it works | Tradeoff |
|--------|-------------------|-----------|
| **LLM-as-a-judge** | A strong LLM scores or compares outputs against a rubric (e.g. G-Eval) | Fast, scalable, correlates well with humans — but inherits the judge model's own biases (e.g. favoring longer answers) |
| **Pairwise preference / Elo** | Humans (or a judge LLM) pick the better of two outputs; aggregate into an Elo-style ranking | More reliable than absolute scoring (humans are better at "A vs B" than "rate this 1-10"), used by leaderboards like Chatbot Arena |
| **Human evaluation (rubric-scored)** | Human raters score against defined criteria (helpfulness, factuality, tone) | Gold standard, but slow and costly — used to *validate* that cheaper automatic/LLM-judge metrics still track reality |

---

## Task-specific: benchmark accuracy, hallucination, safety

| Metric | What it measures | Real example |
|--------|----------------------|----------------|
| **Benchmark accuracy** | % correct on a fixed multiple-choice/QA set | MMLU, GSM8K — standard way models get compared on leaderboards |
| **Hallucination rate** | Fraction of factual claims in the output that are unsupported/false | Checked by fact-verification against a source document or knowledge base |
| **Toxicity / safety score** | Probability output contains harmful content, scored by a classifier | Used as a gate before showing output to users, ties to guardrails in [[Architecture/02 - LLM and RAG Architecture]] |

---

## RAG-specific metrics

Because a RAG system has two stages, it needs metrics for each (RAGAS-style):

| Stage | Metric | Question it answers |
|-------|--------|--------------------------|
| **Retrieval** | Context Precision | Of the chunks retrieved, how many were actually relevant? |
| **Retrieval** | Context Recall | Of everything relevant that exists, how much did retrieval find? (same idea as Recall@K in [[03 - Ranking Clustering and Quality Metrics]]) |
| **Generation** | Faithfulness | Is the answer actually supported by the retrieved context, or did the model add unsupported claims? |
| **Generation** | Answer Relevancy | Does the answer actually address the question asked? |

*Full worked example and the two-stage checklist: [[06 LLM/08 RAG & Retrieval/10 - RAG Evaluation]].*

---

## Common traps

| Trap | Why it's wrong | What to say instead |
|------|------------------|----------------------|
| Using BLEU/ROUGE to grade open-ended chatbot answers | They were built for translation/summarization with a "correct" reference — a good chatbot answer can be entirely different words from any reference | "I'd use LLM-as-a-judge or human eval for open-ended generation, and reserve BLEU/ROUGE for tasks with a clear reference" |
| Trusting perplexity as a proxy for output quality | Perplexity measures fluency/predictability of text, not correctness or helpfulness | "A model can have great perplexity and still hallucinate or refuse to answer — I'd check task-specific metrics too" |
| Using only one LLM-as-judge with no human-eval validation | Judge models have known biases (verbosity bias, position bias in pairwise comparisons) | "I'd validate the judge against a small human-labeled sample before trusting it at scale" |
| Reporting one RAG number ("accuracy") | Hides whether the failure was retrieval (wrong chunks) or generation (right chunks, bad answer) | "I'd always split retrieval metrics from generation metrics to know what to fix" |

---

**Next:** [[07 - Knowledge Graph and Embedding Metrics]]
