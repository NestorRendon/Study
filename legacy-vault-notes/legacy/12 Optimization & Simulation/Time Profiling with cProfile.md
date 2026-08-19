# Time Profiling with cProfile

Example:  
```

import cProfile

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

cProfile.run("slow_function()")


```
Output shows:  
* number of calls  
* total time  
* cumulative time per function  
Example result (simplified):  

| Function      | Calls | Time   |
| ------------- | ----- | ------ |
| slow_function | 1     | 0.12 s |
  
**Memory Profiling**  
Library: memory_profiler  
Example:  
  
from memory_profiler import profile  
  
@profile  
def allocate():  
    a = [i for i in range(1000000)]  
    return a  
  
Shows **memory usage per line**.  
  
  
  

| Category | Technique | What it does | Example | Benefit |
| ----------------- | --------------------------- | ---------------------------------------- | -------------------------------- | ------------------------------ |
| Profiling | cProfile | Measures execution time of functions | cProfile.run("func()") | Finds slow functions |
| Profiling | line_profiler | Measures execution time per line | @profile decorator | Detects exact bottleneck lines |
| Profiling | memory_profiler | Tracks memory usage | @profile on functions | Identifies memory leaks |
| Benchmarking | timeit | Tests performance of small code snippets | timeit.timeit(stmt, number=1000) | Accurate microbenchmarks |
| Loop Optimization | List comprehensions | Replace loops with compact expressions | [x*x for x in range(10)] | Faster and cleaner |
| Built-ins | Use built-in functions | Replace manual loops | sum(data) instead of loop | Faster (C-optimized) |
| Data Structures | Choose efficient structures | Use sets/dicts for lookup | x in my_set | (O(1)) lookup vs (O(n)) |
| Memory | Generators | Produce values lazily | (x*x for x in range(n)) | Lower memory usage |
| Vectorization | Use NumPy operations | Replace Python loops with vector ops | arr * 2 | Huge speed improvement |
| Caching | Memoization | Store previous results | @lru_cache() | Avoid recomputation |
| Algorithms | Better algorithm complexity | Reduce computational complexity | binary search | Major speed improvements |
| Parallelism | Multiprocessing | Run tasks on multiple CPUs | Pool.map() | Faster CPU tasks |
| Concurrency | Async / threading | Handle I/O efficiently | asyncio | Faster I/O workflows |
  
  
  

Basic Python Engineering: Able to write clean functions that can be used as "Tools" by an Al.  
  
-   Basic Agent Tool: LangChain, Smolagents, etc  

| Principle | Description | Example |
| ---------------------- | ------------------------------------- | --------------------------------- |
| Single responsibility | Function should do one clear task | get_weather(city) |
| Clear inputs | Use explicit parameters | def convert_temp(celsius: float) |
| Structured output | Return predictable format (dict/JSON) | {"temperature": 20} |
| Deterministic behavior | Same input → same output | Avoid randomness unless needed |
| Error handling | Validate inputs | if city is None: raise ValueError |
| Type hints | Improve readability and tooling | city: str -> dict |
| Docstrings | Explain what the tool does | describe inputs and outputs |
| No side effects | Avoid modifying global state | pure functions preferred |
| Small functions | Easier for AI systems to compose | keep logic short |
  
  
LLM and Generative Al  
  
-Knows and use of generative Al-based tools.  
Basic prompting techniques. Prompt Hygiene.
