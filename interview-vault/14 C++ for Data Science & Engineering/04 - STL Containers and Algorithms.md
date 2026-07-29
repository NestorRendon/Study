# STL Containers & Algorithms

**Prev:** [[03 - OOP Essentials]] · **Next:** [[05 - Memory and Pointers]]

---

## Containers (pick the right one)

| Container | Use | Access |
|-----------|-----|--------|
| `vector<T>` | Default sequential | O(1) index |
| `deque<T>` | Queue both ends | O(1) ends |
| `map<K,V>` | Sorted keys | O(log n) |
| `unordered_map<K,V>` | Fast lookup avg | O(1) avg |
| `set<T>` | Unique elements | O(log n) |

```cpp
std::vector<int> v = {3, 1, 4};
v.push_back(1);
std::sort(v.begin(), v.end());
auto it = std::find(v.begin(), v.end(), 4);
```

---

## Useful algorithms

```cpp
std::transform(v.begin(), v.end(), out.begin(), [](int x){ return x*x; });
std::accumulate(v.begin(), v.end(), 0);
std::copy_if(v.begin(), v.end(), std::back_inserter(out), pred);
```

---

## Common traps

| Trap | Correct |
|------|---------|
| `vector` iterator after `push_back` | May invalidate — re-acquire |
| `map[]` creates missing key | Use `.find()` or `.at()` |

---

**Next:** [[05 - Memory and Pointers]]
