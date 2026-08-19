# 🧪 BLEU (n-gram overlap)

BLEU only counts **exact word matches**.  
**Unigrams in common**:
cat, on, the  
Words that do **not** match:  
* *sitting* ≠ *sits*  
* *mat* ≠ *rug*  
* *The* ≠ *A*  
**Bigrams in common**: almost none.  
So precisions are very low:  
* P1 ≈3/6
p_1 \approx 3/6
p1 ≈3/6  
* p2≈0
p_2 \approx 0
p2 ≈0  
* p3 ≈0  
* p4 ≈0  
  
BLEU \approx 0  
BLEU≈0  
👉 BLEU concludes: **bad translation**
👉 Human concludes: **perfectly fine**  
  
**🟢 BERTScore (semantic token similarity)**  
BERTScore embeds words using **BERT** and compares cosine similarity.  
What it “sees” in embedding space:  

| Candidate word | Best match in reference | Cosine similarity (conceptual) |
| -------------- | ----------------------- | ------------------------------ |
| cat            | cat                     | 1.00                           |
| sits           | sitting                 | 0.92                           |
| rug            | mat                     | 0.89                           |
| on             | on                      | 1.00                           |
| a              | the                     | 0.75                           |
  
Average similarity ≈ **0.91**  
BERTScore  
≈  
0.9  
\text{BERTScore} \approx 0.9  
BERTScore≈0.9
