# Understanding how the model "remembers" previous tokens in a session to save compute power and reduce latency.

**How Does KV Caching Work?**  
  
**Step-by-Step Process**  
1. **First Generation**: When the model sees the first input, it calculates and stores its keys and values in the cache.⇓  
2. **Next Words**: For each new word, the model retrieves the stored keys and values and adds the new ones instead of starting over.  
3. **Efficient Attention Computation**: calculate attention using the cached K
*K* and V
*V* along with the new Q
*Q* (query) to compute the output.  
4. **Update Input**: add the newly generated token to the input and go back
to step  2 go back to step 2 until we finish generating.  
  
KV caching is a simple but powerful technique that helps AI models generate text faster and more efficiently. By remembering past calculations instead of repeating them, it reduces the time and effort needed to predict new words. While it does require extra memory, this method is especially useful for long conversations ensuring fast and efficient generation
