# ONNX & TensorRT

**Prev:** [[05 - Synthetic Image Generation]] · **Next:** [[12 Optimization & Simulation/00 - Chapter Overview|Optimization (Ch 12)]]

---

## Interview one-liner

Train in **PyTorch** → export **ONNX** (interoperable graph) → optimize with **TensorRT** (NVIDIA inference) for production latency.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## When to use what

| Tool | Use when |
|------|----------|
| **PyTorch** | Research, training, flexibility |
| **ONNX** | Cross-framework deployment, ONNX Runtime on CPU/cloud |
| **TensorRT** | Max GPU inference speed on NVIDIA hardware |

| | ONNX Runtime | TensorRT |
|---|--------------|----------|
| Hardware | CPU, GPU, cross-vendor | NVIDIA GPU |
| Portability | High | NVIDIA-specific |

---

**Next chapter:** [[12 Optimization & Simulation/00 - Chapter Overview]]
---

## Common traps

| Trap | Correct |
|------|---------|
| OpenCV and deep learning are interchangeable | OpenCV = preprocessing; DL = feature learning |
| Higher resolution always helps | Costs compute; may need resize + augmentation balance |
