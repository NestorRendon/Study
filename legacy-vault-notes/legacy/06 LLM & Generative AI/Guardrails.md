# Guardrails

**Guardrails** are systems that **monitor, filter, or correct model inputs and outputs** to enforce safety policies.  
They act as **control layers around the LLM**.  
**Architecture**  
  
User Input  
    ↓  
Input Guardrails (safety check)  
    ↓  
LLM  
    ↓  
Output Guardrails (toxicity / safety filter)  
    ↓  
Final response
