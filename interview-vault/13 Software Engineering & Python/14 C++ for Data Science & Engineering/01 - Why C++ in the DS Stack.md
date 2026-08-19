# Why C++ in the DS Stack?

**Prev:** [[13 Software Engineering & Python/14 C++ for Data Science & Engineering/00 - Chapter Overview]] · **Next:** [[02 - C++ Core Cheatsheet]]

---

## In plain English

Python trains models; **C++ runs them fast** at scale. Many production systems (OpenCV internals, TensorRT, game engines, industrial controllers) are C++ — your gambling-machines / embedded experience is relevant for **ML Engineer** roles that touch deployment.

---

## When C++ matters in DS interviews

| Situation | Why C++ |
|-----------|---------|
| Real-time inference | Low latency, no GC pauses |
| Edge / embedded | Resource limits |
| Existing C++ codebase | Integration with sensors, PLCs |
| OpenCV / TensorRT custom ops | C++ APIs |
| High-throughput feature pipelines | Multi-threading control |

---

## vs Python

| | Python | C++ |
|---|--------|-----|
| Speed of development | Fast | Slower |
| Runtime performance | Slower (unless native libs) | Fast |
| ML training | Default choice | Rare (LibTorch) |
| Production inference | Often C++ or Rust backend | Common |

---

## 30-second interview answer

> "I use Python for modeling and experimentation. I use C++ when latency, memory, or integration with industrial systems matters — for example deploying vision pipelines or working close to hardware. I follow RAII and smart pointers to keep memory safe."

---

**Next:** [[02 - C++ Core Cheatsheet]]
