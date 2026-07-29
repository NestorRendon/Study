# Convolutional Neural Networks (CNN)

**Prev:** [[11 - RNN LSTM and GRU]] · **Next:** [[13 - Diagnosing Neural Network Failures]]

---

## Interview one-liner

**CNNs** exploit spatial structure with **local filters** (kernels), **weight sharing**, and pooling — standard for images and spatial signals.

---

## In plain English

*(Read the sections below — each concept builds intuition before formulas.)*


## Convolution (1D/2D)

→ Math: [[03 Mathematics/02 - Similarity Correlation and Convolution]]

$$(f * k)(t) = \sum_s f(s)\, k(t - s)$$

| Symbol | Meaning |
|--------|---------|
| Kernel / filter | Small learned weights sliding over input |
| Stride | Step size |
| Padding | Border handling (`same` keeps size) |

**Output size (1D):** $\frac{n - k + 2p}{s} + 1$

---

## Typical stack

```
Input → Conv → ReLU → Pool → Conv → ReLU → Pool → Flatten → Dense → Output
```

| Layer | Role |
|-------|------|
| Conv | Detect local patterns (edges, textures) |
| ReLU | Non-linearity $\max(0, x)$ |
| Pooling | Downsample, translation tolerance |
| Dense | Global decision |

---

## CV tasks (links)

| Task | Output |
|------|--------|
| Classification | Class label |
| Detection | Boxes + classes |
| Semantic segmentation | Pixel class |
| Instance segmentation | Separate object masks |

→ [[11 Computer Vision/00 - Chapter Overview|Computer Vision chapter]]

---

**Next:** [[13 - Diagnosing Neural Network Failures]]
