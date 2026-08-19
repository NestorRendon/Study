# Cons

* **Doesn't scale** — training is O(n²) to O(n³), painful beyond ~100k samples  
* **No probability output** natively — needs Platt scaling as a post-hoc fix, which is slow  
* Kernel and C choice requires careful tuning  
* Hard to interpret — especially with RBF kernel  
* **Doesn't handle noise well** with hard margin  
* Multi-class requires workarounds (one-vs-one or one-vs-rest)
