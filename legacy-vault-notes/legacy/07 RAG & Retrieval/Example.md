# Example

Task: write a research summary.  
Steps:  
1. LLM writes summary  
2. Evaluator checks:  
    * accuracy  
    * clarity  
    * completeness  
3. Model revises based on feedback.  
Example prompt flow:  
```

Draft summary → Evaluate → Improve → Final summary


```
  
**Routing Pattern**  
**Idea**  
A **router model decides which tool, model, or workflow should handle the request**.  
This is common in **multi-agent systems**.  
**Workflow**  
  
User query  
    ↓  
Router LLM  
    ↓  
Select specialized tool/agent  
    ↓  
Execute task  
  
**Example**  
User asks:  
  
"What is the derivative of x²?"  
  
Router decides:  

| Query type | Route            |
| ---------- | ---------------- |
| math       | math solver      |
| coding     | code agent       |
| search     | retrieval system |
  
  
**Parallelization Pattern**  
**Idea**  
Multiple agents **run tasks simultaneously**, then results are **combined**.  
This reduces latency and improves coverage.  
**Workflow**  
  
User query  
    ↓  
Split into subtasks  
    ↓  
Agent A     Agent B     Agent C  
   ↓           ↓           ↓  
Results combined  
  
**Example**  
Task: analyze a research paper.  
Parallel tasks:  

| Agent   | Task                 |
| ------- | -------------------- |
| Agent 1 | summarize            |
| Agent 2 | extract key results  |
| Agent 3 | identify limitations |
  
Final step merges outputs.  
  
**Comparison of the Patterns**  

| Pattern             | Main Goal                        | When to Use        |
| ------------------- | -------------------------------- | ------------------ |
| Evaluator–Optimizer | improve output quality           | writing, reasoning |
| Routing             | choose best tool                 | multi-tool systems |
| Parallelization     | reduce latency / expand analysis | complex tasks      |
  
**Combined Architecture (Typical Agent System)**  
Real systems often combine all three:  
  
User query  
    ↓  
Router  
    ↓  
Parallel agents  
    ↓  
Evaluator  
    ↓  
Final answer  
  
This architecture is common in **modern AI assistants and autonomous agents**.  
  
  
**Example: Research Assistant Agent**  
Step-by-step system:  
  
1. Router → classify question  
2. Parallel agents → search papers, summarize, extract results  
3. Evaluator → check consistency  
4. Final answer generator  
  
**Example: Research Assistant Agent**  
Step-by-step system:  
  
1. Router → classify question  
2. Parallel agents → search papers, summarize, extract results  
3. Evaluator → check consistency  
4. Final answer generator
