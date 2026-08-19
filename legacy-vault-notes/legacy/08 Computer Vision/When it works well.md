# When it works well

* LLMs trained on large datasets  
* simple tasks  
* general reasoning  
  
**2. Few-Shot Prompting**  
**Idea**  
Provide **a few examples** of input-output pairs so the model learns the pattern.  
**Structure**  
  
Example 1  
Example 2  
Example 3  
New query  
  
**Example**  
  
Sentence: I love this product.  
Sentiment: Positive  
  
Sentence: This is terrible.  
Sentiment: Negative  
  
Sentence: The service was amazing.  
Sentiment:  
  
The model infers the pattern and answers.  
  
**Why it works**  
The model learns **the task format and reasoning pattern** from examples.  
  
  
**Chain-of-Thought Prompting (CoT)**  
**Idea**  
Ask the model to **show intermediate reasoning steps**.  
**Example**  
Prompt:  
```

Solve step by step:

If a train travels 60 km/h for 2 hours, how far does it go?


```
Output:  
```

Distance = speed × time
Distance = 60 × 2
Distance = 120 km


```
Why it works:  
* encourages structured reasoning  
* improves performance on complex tasks
