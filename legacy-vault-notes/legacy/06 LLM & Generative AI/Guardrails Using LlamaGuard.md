# Guardrails Using LlamaGuard

LlamaGuard: https://huggingface.co/meta-llama/Llama-Guard-3-8B  
LlamaGuard is a **safety classification model** developed to detect **unsafe prompts and responses**.  
It classifies text according to **safety policies**.  
**Example Categories**  

| Category         | Description       |
| ---------------- | ----------------- |
| violence         | harmful actions   |
| self-harm        | suicide content   |
| illegal activity | criminal guidance |
| harassment       | abusive language  |
  
**Example**  
Input prompt:  
  
How can I break into a car?  
  
Classifier output:  
  
Unsafe: Criminal Activity  
  
Then the system **blocks the request**  
  
  

| Concept         | Meaning                                       |
| --------------- | --------------------------------------------- |
| Alignment       | ensuring AI behavior follows human values     |
| Guardrails      | safety controls around LLMs                   |
| NeMo Guardrails | rule-based conversation safety framework      |
| LlamaGuard      | classifier detecting unsafe prompts/responses |
