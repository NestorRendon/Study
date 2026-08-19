# 🧪COMET (learned human judgment)

COMET also sees the **source sentence** (important).  
Assume source (Spanish):  
“El gato está sentado en la alfombra.”  
COMET processes:  
* source  
* candidate  
* reference  
It has been trained on human ratings and has learned that:  
* *rug* ≈ *mat*  
* *sits* ≈ *is sitting*  
COMET outputs something like:  
COMET  
=  
0.96  
\text{COMET} = 0.96  
COMET=0.96  
👉 COMET concludes: **excellent translation (human-level)**  
  
  
  

| Metric | What it notices | Verdict (example) | Advantages | Disadvantages | Common alternatives |
| ------ | --------------- | ----------------- | ---------- | ------------- | ------------------- |
  

| BLEU | Exact n-gram word overlap | ❌ Bad | Very fast; no model needed; language-agnostic; historic MT benchmark | Fails on paraphrase/synonyms; ignores meaning; poor for LLM outputs, summarization, QA | ROUGE, BERTScore |
| ---- | ------------------------- | ----- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------- |
  

| ROUGE | Overlap of n-grams / longest common subsequence (recall-oriented) | ❌ Bad | Good for summarization; simple; fast; recall focus (did we capture key words?) | Still lexical; misses paraphrase; can reward verbosity | BERTScore, MoverScore |
| ----- | ----------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------ | ------------------------------------------------------ | --------------------- |
  

| BERTScore | Semantic similarity via embeddings | ✅ Very good | Handles synonyms/paraphrase; strong human correlation; works across tasks (MT, QA, summarization) | Slower; needs a model; token-level (limited reasoning) | MoverScore, Sentence-Transformers cosine |
| --------- | ---------------------------------- | ----------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------- |
  

| COMET | Learned human judgment using source + ref | ✅ Excellent | State-of-the-art for MT; uses source context; best human correlation | Heavy model; mainly MT-focused; slower | BLEURT, UniTE |
| ----- | ----------------------------------------- | ----------- | -------------------------------------------------------------------- | -------------------------------------- | ------------- |
  
  

| Method | Needs reference? | Understands meaning? | Human-aligned? | Best use |
| -------------- | ---------------- | -------------------- | -------------- | ------------------------- |
| BLEU | ✅ | ❌ | ❌ | Legacy MT |
| ROUGE | ✅ | ❌ | ❌ | Summarization baseline |
| BERTScore | ❌ | ✅ | 🟡 medium | semantic similarity |
| COMET | ✅ (often) | ✅ | 🟢 high | MT evaluation |
| G-Eval | ❌ | ✅ | 🟢 very high | general LLM eval |
| LLM-as-a-Judge | ❌ | ✅ | 🟢 very high | production LLM evaluation |
