# Chapter 14 — C++ for Data Science & Engineering

For **embedded**, **high-performance** pipelines, gaming/industrial systems (your 2017 background), and interviews that mix DS with production C++.

---

## The story

1. **Why C++** — where it sits in the DS stack ([[01 - Why C++ in the DS Stack]])
2. **Syntax** — core language cheatsheet ([[02 - C++ Core Cheatsheet]])
3. **OOP** — classes, inheritance ([[03 - OOP Essentials]])
4. **STL** — containers and algorithms ([[04 - STL Containers and Algorithms]])
5. **Memory** — pointers, RAII ([[05 - Memory and Pointers]])
6. **Interview patterns** — common DS/C++ questions ([[06 - C++ Interview Patterns]])

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | Why C++ in DS stack | [[01 - Why C++ in the DS Stack]] |
| 2 | Core syntax cheatsheet | [[02 - C++ Core Cheatsheet]] |
| 3 | OOP essentials | [[03 - OOP Essentials]] |
| 4 | STL containers & algorithms | [[04 - STL Containers and Algorithms]] |
| 5 | Memory & pointers | [[05 - Memory and Pointers]] |
| 6 | DS interview patterns | [[06 - C++ Interview Patterns]] |

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **ONNX Runtime / TensorRT** | C++ inference serving |
| **Rust alternative** | Some teams pick Rust over C++ for safety |

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| `vector` after invalidation | Iterator invalidation on `push_back` reallocate |
| Raw `new` without `delete` | Prefer **RAII**, smart pointers |
| Pass huge object by value | Pass by `const&` or move |
| `==` on `float` | Use epsilon comparison |
| Ignore `const` correctness | `const` = contract for callers |

---

**Prev:** [[13 Software Engineering & Python/00 - Chapter Overview]] · **Next:** [[16 DevOps CI CD & Kubernetes/00 - Chapter Overview]]

[[Home|← Home]]
