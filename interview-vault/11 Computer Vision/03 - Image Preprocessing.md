# Image Preprocessing

**Prev:** [[02 - OpenCV Advanced]] · **Next:** [[04 - Detection and Segmentation]]

---

## In plain English

Classical **preprocessing** cleans images before rules or neural nets: threshold, morphology, normalize, extract keypoints.

---

## Example 1 — Otsu + morphology pipeline

```python
import cv2

img = cv2.imread("cells.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

_, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
clean = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
clean = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, kernel)

cv2.imwrite("mask_clean.png", clean)
```

| Step | Input | Output |
|------|-------|--------|
| Otsu | gray | binary mask |
| Opening | binary | removes speckle |
| Closing | opened | fills holes |

![Morphology example](assets/DE8D7D35-3E5F-490F-B79A-C455BAA4C34D.webp)

---

## Example 2 — Normalize for PyTorch / torchvision

```python
import cv2
import torch
from torchvision import transforms

img_bgr = cv2.imread("photo.jpg")
rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

tf = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),  # [0,1], CHW
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
    ),
])
tensor = tf(rgb)  # shape (3, 224, 224) — ready for ResNet
```

**Trap:** ImageNet mean/std only if using ImageNet-pretrained backbone.

---

## Example 3 — SIFT keypoints (classical matching)

```python
import cv2

img1 = cv2.imread("img1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("img2.jpg", cv2.IMREAD_GRAYSCALE)

sift = cv2.SIFT_create()  # opencv-contrib if needed
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append(m)

vis = cv2.drawMatches(img1, kp1, img2, kp2, good, None,
                      flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imwrite("sift_matches.jpg", vis)
```

→ Advanced matching + homography: [[02 - OpenCV Advanced#Example 2 — Homography between two views]]

---

## Example 4 — Histogram equalization (lighting)

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(gray)
# CLAHE — local contrast (often better)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl = clahe.apply(gray)
```

---

## When to use classical vs generate new data

| Need | Approach |
|------|----------|
| Clean mask from photo | This note |
| 1000 new field images | [[05 - Synthetic Image Generation]] |

---

**Next:** [[04 - Detection and Segmentation]]
