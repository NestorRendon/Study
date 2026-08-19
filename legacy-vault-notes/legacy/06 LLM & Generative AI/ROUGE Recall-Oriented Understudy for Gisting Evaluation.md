# 🧪ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

**ROUGE** is a metric used to evaluate **generated text** by comparing it to one or more **reference texts**.  
It is especially common for:  
* text summarization  
* machine translation (less common now)  
* general NLG evaluation  
Reference: The cat sat on the mat  
  
Generated: The cat is on mat  
  
ROUGE-1 overlap:  
Matched words:  
  
The, cat, on, mat  
  
  
**Limitations of ROUGE**  
Major limitation:  
It measures lexical overlap, not semantic quality.  
Example:  
Reference: The car is fast  
  
Generated: The automobile is quick  
  
ROUGE score may be low despite **same meaning**.  
  
**8. Modern Alternatives**  
Because of this limitation, newer metrics are often preferred:  

| Metric       | Improvement                        |
| ------------ | ---------------------------------- |
| BLEU         | Precision-based n-gram metric      |
| BERTScore    | Semantic similarity via embeddings |
| METEOR       | Synonym-aware matching             |
| LLM-as-Judge | Model-based evaluation             |
