# Memory & Pointers

**Prev:** [[04 - STL Containers and Algorithms]] · **Next:** [[06 - C++ Interview Patterns]]

---

## In plain English

You control **where** data lives (stack vs heap). **RAII** = resource acquired in constructor, released in destructor — no leaks.

---

## Stack vs heap

```cpp
int a = 5;                          // stack
auto p = std::make_unique<int>(5);  // heap, owned by smart ptr
```

| | Stack | Heap |
|---|-------|------|
| Lifetime | Function scope | Until freed |
| Speed | Fast | Slower |
| Size | Limited | Large |

---

## Smart pointers (modern C++)

```cpp
std::unique_ptr<Model> m = std::make_unique<LinearModel>();  // single owner
std::shared_ptr<Buffer> buf = std::make_shared<Buffer>(1024); // shared ownership
```

**Rule:** prefer smart pointers over raw `new`/`delete`.

---

## Common traps

| Trap | Correct |
|------|---------|
| Dangling reference | Don't return reference to local variable |
| Double delete | Use smart pointers |
| Memory leak in loop | RAII or smart ptr |

---

**Next:** [[06 - C++ Interview Patterns]]
