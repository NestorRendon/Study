# When Convexity Does Not Matter Much

Convexity matters less in **large overparameterized models**.  
Examples:  
* Deep neural networks  
* Large transformer models  
* CNNs  
Reasons:  
1. High-dimensional spaces contain many **good minima**  
2. Most local minima have similar loss  
3. SGD noise helps escape poor minima  
4. Saddle points are more common than bad minima  
  
  
**When Gradient Descent Fails**  
Problems occur when:  

| Problem                 | Explanation        |
| ----------------------- | ------------------ |
| Learning rate too large | Divergence         |
| Learning rate too small | Very slow training |
| Non-smooth loss         | Gradient unstable  |
| Poor conditioning       | Zig-zag updates    |
  
  
  
**Modern Improvements**  
To solve gradient descent limitations, optimizers were developed:  

| Optimizer | Idea                        |
| --------- | --------------------------- |
| Momentum  | Smooth updates              |
| RMSProp   | Adaptive learning rates     |
| Adam      | Momentum + adaptive scaling |
  
  

What is a convolution?  
Convolution is a fundamental mathematical operation that combines two functions to produce a third, expressing how the shape of one is modified by the other.  

Hypothesis generation.  
Hypothesis generation is the crucial initial step in research and analysis, involving the formulation of testable, educated, and tentative answers to research questions  

Error analysis.  
  

Explain how the autocorrelation of a positive-trend line can be negative.  
  
Autocorrelation measures the relationship (correlation) between a variable's current value and its past values (lagged versions) over time, indicating how similar a dataset is to a delayed copy of itself.   
**5. Geometric Interpretation**  
For a trend:  
  
time →  
1 2 3 4 5  
  
Centered around the mean:  
  
-2 -1 0 1 2  
  
Large shifts align:  
  
-2 with 2  
-1 with 1  
  
Opposite signs → **negative correlation**.  
  

ANOVA, multivariate analysis, PCA / Factor Analysis, population tests and comparison.  
  
  
[Analysis of Variance](https://www.google.com/search?q=Analysis+of+Variance&oq=anova+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTINCAEQABiRAhiABBiKBTINCAIQABiRAhiABBiKBTIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDExNDJqMGo5qAIGsAIB8QVMvRxiOQtSow&sourceid=chrome&ie=UTF-8&ved=2ahUKEwib74qQu5OTAxW-hP0HHYLAOcoQgK4QegQIARAD) (ANOVA) is a statistical method used to compare the means of three or more independent groups to determine if at least one is significantly different  
  
Factor analysis is a multivariate statistical method used to reduce a large number of observed, correlated variables into a smaller, more manageable set of unobserved "latent factors"  
FA tries to reduce the number of variables while still being able to reproduce the original correlation matrix as best as possible.  
  
Population tests compare sample data to a standard value (single sample) or compare two distinct populations to determine if differences are statistically significant. Common methods include t-tests for means (paired or independent), ANOVA for multiple groups, z-tests for proportions, and non-parametric tests like Wilcoxon/Mann-Whitney for skewed dat  
  
  
  
**2. What if Regression Has Heteroskedasticity?**  
**Heteroskedasticity**  
The **variance of the error changes across observations**.  

| Robust standard errors | Correct inference |
| ---------------------- | ----------------- |
  

| Transform variables | e.g., log transform |
| ------------------- | ------------------- |
  

| Model variance explicitly | GLS |
| ------------------------- | --- |
  
  
Heteroskedasticity occurs in regression analysis when the variance of the error terms (residuals) is not constant across all levels of the independent variables. It violates the [homoscedasticity](https://www.google.com/search?q=homoscedasticity&oq=Heteroskedasticity&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg70gEHMjQ5ajBqOagCBrACAfEFbEJ0K_f1hk0&sourceid=chrome&ie=UTF-8&ved=2ahUKEwiflt6nl9uTAxWN7AIHHcT-IiYQgK4QegYIAQgAEAQ) assumption of [Ordinary Least Squares (OLS) regression](https://www.google.com/search?q=Ordinary+Least+Squares+%28OLS%29+regression&oq=Heteroskedasticity&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg70gEHMjQ5ajBqOagCBrACAfEFbEJ0K_f1hk0&sourceid=chrome&ie=UTF-8&ved=2ahUKEwiflt6nl9uTAxWN7AIHHcT-IiYQgK4QegYIAQgAEAU), causing standard errors to be inaccurate, which renders hypothesis tests and confidence intervals unreliable, though coefficient estimates remain unbiased  
  
![cfa2_reading3_img1.jpg](assets/14FEB281-8D66-4B08-BB34-0480B8A7654A.jpg)  
  
To fix heteroscedasticity, transform the dependent variable (e.g., using natural logs or square roots) t  
  
  
  
**How Do You Avoid Overfitting?**  
**Overfitting**  
The model **memorizes training data** but performs poorly on new data.  
Mathematically:  
Training error ↓
Test error ↑  
  
**Main techniques**  

| Method           | Idea                             |
| ---------------- | -------------------------------- |
| Regularization   | Penalize large weights           |
| Cross-validation | Estimate generalization          |
| Early stopping   | Stop training before overfitting |
| More data        | Reduces variance                 |
| Simpler models   | Reduce complexity                |
| Dropout (NN)     | Randomly disable neurons         |
  
  
  
![Method 1 - Logistic Regression](assets/483310A4-DA0E-42A9-A308-40C35C84AFE3.png)  
  
![et of all](assets/7AA1F882-8D9C-4324-AC27-53F039D6AF77.webp)  
![Set of all](assets/9501541B-5DB6-402D-A24C-B41848CD98FE.webp)  
  
- Handling "too many features" (Is that a problem? When? What would you do about it?)  
How can you choose the value of k on k-means?  
  
  
Transformer Basics: Understands the "Encoder-only" (BERT) vs. "Decoder-only" (GPT)  
Understands Embeddings as an extension to "Feature Engineering."  
LLM  
Workflow vs. Agent: Understands the difference between a fixed Workflow (Step A -> Step  
B) and a dynamic Agent (Goal -> Reason -> Action).  
  
**Workflow vs Agent**  

| Aspect | Workflow | Agent |
| ----------- | -------------------------------------------------------- | ----------------------------------------------------- |
| Definition | A predefined sequence of steps executed in a fixed order | An autonomous system that decides actions dynamically |
| Control | Deterministic | Adaptive / decision-based |
| Execution | Follows a fixed pipeline | Chooses next step based on state or goal |
| Flexibility | Low | High |
| Complexity | Easier to design and debug | More complex behavior |
| Use case | Data pipelines, ML training | Autonomous AI systems |
  
  
-Vector DB & other types of Retrieval: identifying when to use each based on trade-offs in latency, scale, and metadata filtering requirements.  
  
**One-sentence intuition**  
* **Keyword retrieval** finds documents with the same words.  
* **Vector retrieval** finds documents with the same **meaning**.  
  
Encoding & Token Awareness: Understands how different models "count" tokens and how that impacts both cost and performance.  
- Context Precision & Recall: Did we retrieve only relevant documents? Did the retrieval step actually include the document containing the answer?
