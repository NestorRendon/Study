# OpenCV Fundamentals

**Prev:** [[00 - Chapter Overview]] · **Next:** [[02 - OpenCV Advanced]]

---

## In plain English

**OpenCV** (`cv2`) is the classic computer-vision toolkit on **NumPy arrays**. Default color order is **BGR** (not RGB). Use it for I/O, geometry, thresholds, contours, and drawing — usually **before** or **beside** a deep model.

**Install:** `pip install opencv-python` (or `opencv-python-headless` on servers without GUI).

---

## Setup pattern

```python
import cv2
import numpy as np

img = cv2.imread("photo.jpg")  # BGR, shape (H, W, 3) or None if missing
assert img is not None, "check path"
h, w = img.shape[:2]
```

| Function | Input | Output |
|----------|-------|--------|
| `imread(path)` | file path | `ndarray` BGR or `None` |
| `imwrite(path, img)` | array | bool success |

**For matplotlib:** convert BGR → RGB:

```python
import matplotlib.pyplot as plt
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
```

---

## Example 1 — Resize, crop, rotate

```python
# Resize to fixed width (keep aspect)
target_w = 640
scale = target_w / w
resized = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

# Center crop 224×224 (common for CNNs)
rh, rw = resized.shape[:2]
y0, x0 = (rh - 224) // 2, (rw - 224) // 2
crop = resized[y0:y0 + 224, x0:x0 + 224]

# Rotate 90° clockwise
rot = cv2.rotate(crop, cv2.ROTATE_90_CLOCKWISE)
```

| `interpolation` | When |
|-----------------|------|
| `INTER_AREA` | **Shrinking** — avoids moiré |
| `INTER_LINEAR` | Upscale / general |
| `INTER_CUBIC` | Slower, sharper upscale |

---

## Example 2 — Color spaces (HSV for color segmentation)

```python
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Green foliage mask (tune for your domain)
lower = np.array([35, 40, 40])
upper = np.array([85, 255, 255])
mask = cv2.inRange(hsv, lower, upper)

result = cv2.bitwise_and(img, img, mask=mask)
```

![HSV color space](assets/E0A894FC-D02F-4EDF-986B-65B325710CFC.png)

| Space | Channel | Use |
|-------|---------|-----|
| **BGR** | OpenCV default | I/O, drawing |
| **Gray** | single channel | Edges, threshold |
| **HSV** | Hue / Sat / Value | Color blobs under lighting change |

---

## Example 3 — Blur, edges, threshold

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny edges
edges = cv2.Canny(blur, threshold1=50, threshold2=150)

# Global binary (Otsu picks threshold)
_, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Uneven lighting → adaptive
adapt = cv2.adaptiveThreshold(
    blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, blockSize=11, C=2,
)
```

→ Deeper morphology: [[03 - Image Preprocessing]]

---

## Example 4 — Contours & bounding boxes

```python
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

vis = img.copy()
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 500:
        continue
    x, y, bw, bh = cv2.boundingRect(cnt)
    cv2.rectangle(vis, (x, y), (x + bw, y + bh), (0, 255, 0), 2)

cv2.imwrite("boxes.jpg", vis)
```

| `findContours` mode | Meaning |
|-------------------|---------|
| `RETR_EXTERNAL` | Outermost contours only |
| `RETR_TREE` | Full hierarchy |

---

## Example 5 — Draw annotations (labels for datasets)

```python
label = "weed"
conf = 0.92
x1, y1, x2, y2 = 120, 80, 280, 240

cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.putText(
    img, f"{label} {conf:.2f}", (x1, y1 - 8),
    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2,
)
```

Useful for visualizing detector output or building **weak labels**.

---

## Example 6 — Simple video frame loop

```python
cap = cv2.VideoCapture(0)  # webcam, or path to .mp4
while True:
    ok, frame = cap.read()
    if not ok:
        break
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
```

---

## Quick reference

| Task | Function |
|------|----------|
| Read / write | `imread`, `imwrite` |
| Resize | `resize` |
| Color convert | `cvtColor` |
| Blur | `GaussianBlur` |
| Edges | `Canny` |
| Threshold | `threshold`, `adaptiveThreshold` |
| Contours | `findContours`, `boundingRect` |
| Mask | `inRange`, `bitwise_and` |

---

## Common traps

| Trap | Correct |
|------|---------|
| `imread` → RGB for torchvision | Convert **BGR2RGB** before `ToTensor` |
| `imread` returns `None` | Always check path / permissions |
| Huge resize upscale | Use `INTER_AREA` when **down**scaling |
| Contours on raw color image | Usually **gray + threshold** first |

---

## Interview one-liner

> "OpenCV handles BGR I/O and classical geometry — I use it for masks, contours, and visualization; learned features come from CNNs or ViTs downstream."

---

**Next:** [[02 - OpenCV Advanced]]
