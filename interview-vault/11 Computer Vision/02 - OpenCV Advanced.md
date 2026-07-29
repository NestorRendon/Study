# OpenCV Advanced

**Prev:** [[01 - OpenCV Fundamentals]] · **Next:** [[03 - Image Preprocessing]]

---

## In plain English

After basics, interviews and production pipelines often need **geometry** (warp, homography), **motion** (optical flow), **matching** (templates, features), and **classical detectors** (HOG). This note is **code-first** for those patterns.

**3D point clouds:** see [[OPEN 3D]] · [Open3D tutorials](https://www.open3d.org/docs/release/tutorial/geometry/pointcloud.html)

---

## Example 1 — Perspective warp (document / lane ROI)

```python
import cv2
import numpy as np

img = cv2.imread("aerial.jpg")
h, w = img.shape[:2]

# Four source points (click in real tools; here hard-coded)
src = np.float32([[50, 50], [w - 50, 40], [w - 20, h - 20], [30, h - 30]])
dst = np.float32([[0, 0], [400, 0], [400, 400], [0, 400]])

M = cv2.getPerspectiveTransform(src, dst)
bird = cv2.warpPerspective(img, M, (400, 400))
```

| Input | Output |
|-------|--------|
| 4 point pairs | $3 \times 3$ homography $M$ |
| `warpPerspective` | Rectified view |

---

## Example 2 — Homography between two views
A **homography** is ==a geometric transformation that maps the points of one planar surface in an image to another==. Represented mathematically as a 

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
![[Pasted image 20260525164751.png]]
![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

 matrix, it aligns images taken from different perspectives.
```python
# ORB features (free; SIFT may need opencv-contrib)
orb = cv2.ORB_create(1000)
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda m: m.distance)[:50]

pts1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
pts2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

H, inliers = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)
aligned = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))
```

**Use:** image stitching, align camera frames, map ground plane.

---

## Example 3 — Optical flow (motion between frames)
![[Pasted image 20260525164818.png]]

```python
prev_gray = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
next_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

flow = cv2.calcOpticalFlowFarneback(
    prev_gray, next_gray, None,
    pyr_scale=0.5, levels=3, winsize=15,
    iterations=3, poly_n=5, poly_sigma=1.2, flags=0,
)
# flow[y,x] = (dx, dy) per pixel
mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
```

| Method | Speed | Use |
|--------|-------|-----|
| **Farneback** | Medium | Dense flow, general |
| **Lucas-Kanade** | Fast | Sparse points (`goodFeaturesToTrack`) |

**Use:** action cues, camera motion, simple tracking.

---

## Example 4 — Template matching
![[Pasted image 20260525164842.png]]
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = gray[100:160, 200:280]

res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
h_t, w_t = template.shape
cv2.rectangle(img, top_left, (top_left[0] + w_t, top_left[1] + h_t), (0, 0, 255), 2)
```

**Limit:** fails under scale/rotation change — use **feature matching** or a CNN detector instead.

---

## Example 5 — Connected components & stats

```python
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)

for i in range(1, num_labels):  # skip background 0
    x, y, bw, bh, area = stats[i]
    if area < 200:
        continue
    cv2.rectangle(img, (x, y), (x + bw, y + bh), (255, 0, 0), 2)
```

| Output | Meaning |
|--------|---------|
| `labels` | H×W integer mask per blob |
| `stats` | bbox + area per label |

---

## Example 6 — HOG + linear SVM (classical detector sketch)

```python
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
boxes, weights = hog.detectMultiScale(img, winStride=(8, 8), padding=(8, 8), scale=1.05)
for (x, y, bw, bh) in boxes:
    cv2.rectangle(img, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
```

**Interview:** HOG = hand-crafted gradients; **YOLO** replaced this for most detection tasks.

---

## Example 7 — Remap & undistort (calibrated cameras)

```python
# After chessboard calibration → mtx, dist
undist = cv2.undistort(img, camera_matrix, dist_coeffs)
```

**Use:** robotics, metrology, AR — reduces lens barrel distortion before measuring sizes.

---

## When to use advanced OpenCV vs deep learning

| Task | OpenCV advanced | Deep learning |
|------|-----------------|---------------|
| Document scan warp | ✅ | Overkill |
| Pedestrian detect (2010) | HOG | ✅ YOLO |
| Instance seg | ❌ | ✅ Mask R-CNN / SAM |
| Rare defect on texture | Maybe morphology + rules | ✅ + synthetic data [[05 - Synthetic Image Generation]] |

---

## Resources

| Resource | URL |
|----------|-----|
| OpenCV docs | [docs.opencv.org](https://docs.opencv.org/4.x/) |
| OpenCV Python tutorials | [docs.opencv.org/4.x/d6/d00/tutorial_py_root.html](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) |
| Open3D (3D) | [open3d.org](https://www.open3d.org/) |

---

## Common traps

| Trap | Correct |
|------|---------|
| Homography with < 4 good matches | Need RANSAC + enough inliers |
| Template matching on different scale | Multi-scale search or learned detector |
| Optical flow on compressed video | Compression artifacts break brightness constancy |

---

**Next:** [[03 - Image Preprocessing]]
