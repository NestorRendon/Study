# Chapter 11 — Computer Vision

**Placed after Transformers** — classical OpenCV → deep models → synthetic data → edge deploy.

**Overview = story only.** Detail notes include **runnable code** and **resource links**.

---

## The story

1. **OpenCV basics** — I/O, color, edges, contours, draw boxes ([[01 - OpenCV Fundamentals]])
2. **OpenCV advanced** — homography, optical flow, HOG, calibration ([[02 - OpenCV Advanced]])
3. **Preprocess** — Otsu, morphology, SIFT ([[03 - Image Preprocessing]])
4. **Detection & segmentation** — YOLO, SAM, task types ([[04 - Detection and Segmentation]])
5. **Synthetic images** — augment, copy-paste, **SD / ControlNet / inpaint** (9 code examples) ([[05 - Synthetic Image Generation]])
6. **Deploy** — ONNX, TensorRT ([[06 - ONNX and TensorRT]])

---

## Reading path

| # | Topic | Note |
|---|--------|------|
| 1 | OpenCV fundamentals + examples | [[01 - OpenCV Fundamentals]] |
| 2 | OpenCV advanced | [[02 - OpenCV Advanced]] |
| 3 | Image preprocessing | [[03 - Image Preprocessing]] |
| 4 | Detection & segmentation (+ YOLO, SAM examples) | [[04 - Detection and Segmentation]] |
| 5 | Image generation & synthetic data | [[05 - Synthetic Image Generation]] |
| 6 | ONNX & TensorRT | [[06 - ONNX and TensorRT]] |

**3D / point clouds:** [[OPEN 3D]] · [Open3D](https://www.open3d.org/)

---

## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Vision transformers** | ViT, DINOv2 |
| **YOLO / RT-DETR** | Real-time detection |
| **SAM 2** | Promptable segmentation |
| **Synthetic data** | Diffusion + ControlNet + sim engines |
| **Edge deploy** | ONNX, TensorRT, INT8 |

---

## Common traps (chapter)

| Trap | Correct |
|------|---------|
| OpenCV loads RGB | Default is **BGR** |
| Train/test on synthetic only | **Real** holdout for metrics |
| OpenCV replaces CNN | Classical prep vs **learned** features |
| Accuracy alone on rare events | Precision/recall per class |

---

**Prev:** [[Metrics and Evaluation/00 - Chapter Overview]] · **Next:** [[12 Optimization & Simulation/00 - Chapter Overview]]

[[Home|← Home]]
