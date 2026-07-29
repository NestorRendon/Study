# Detection & Segmentation

**Prev:** [[03 - Image Preprocessing]] · **Next:** [[05 - Synthetic Image Generation]]

---

## In plain English

| Task | Output | Example |
|------|--------|---------|
| **Classification** | One label per image | "dog" |
| **Detection** | Boxes + classes | YOLO, RT-DETR |
| **Semantic segmentation** | Class per pixel | FCN, DeepLab |
| **Instance segmentation** | Mask per object | Mask R-CNN, SAM |

---

## Example 1 — YOLO inference (Ultralytics)

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # or your best.pt after train
results = model.predict("field.jpg", conf=0.25, imgsz=640)

for r in results:
    boxes = r.boxes  # xyxy, conf, cls
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        print(model.names[cls_id], conf, x1, y1, x2, y2)
    r.save("pred.jpg")  # drawn boxes
```

| Input | Output |
|-------|--------|
| Image path / array | `Boxes` tensor + annotated image |

Train on synthetic + real mix → [[05 - Synthetic Image Generation]]

---

## Example 2 — Draw predictions with OpenCV

```python
import cv2
from ultralytics import YOLO

img = cv2.imread("field.jpg")
model = YOLO("best.pt")
results = model(img)[0]

for box in results.boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cls = model.names[int(box.cls[0])]
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(img, cls, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
cv2.imwrite("out.jpg", img)
```

---

## Example 3 — SAM 2 mask from point (segmentation)

```python
# pip install sam2  (see official repo for checkpoint download)
import torch
import cv2
from sam2.build_sam import build_sam2
from sam2.sam2_image_predictor import SAM2ImagePredictor

checkpoint = "./checkpoints/sam2_hiera_large.pt"
model_cfg = "configs/sam2/sam2_hiera_l.yaml"
predictor = SAM2ImagePredictor(build_sam2(model_cfg, checkpoint))

image = cv2.cvtColor(cv2.imread("scene.jpg"), cv2.COLOR_BGR2RGB)
predictor.set_image(image)

# One foreground click (x, y)
masks, scores, _ = predictor.predict(
    point_coords=[[420, 310]],
    point_labels=[1],
    multimask_output=True,
)
best = masks[scores.argmax()]
cv2.imwrite("mask.png", (best * 255).astype("uint8"))
```

**Use:** mask → copy-paste synthetic data or training labels.

**Resources:** [SAM 2 GitHub](https://github.com/facebookresearch/segment-anything-2)

---

## Example 4 — torchvision classifier (transfer learning sketch)

```python
import torch
from torchvision import models, transforms
from PIL import Image

weights = models.ResNet18_Weights.IMAGENET1K_V1
model = models.resnet18(weights=weights)
model.eval()

preprocess = weights.transforms()
img = Image.open("crop.jpg").convert("RGB")
batch = preprocess(img).unsqueeze(0)

with torch.no_grad():
    logits = model(batch)
    prob = torch.softmax(logits, dim=1)
    top5 = prob.topk(5)
```

Replace head for your classes after fine-tune on real + synthetic images.

---

## Deep learning stack

→ [[05 Deep Learning/12 - Convolutional Neural Networks]]  
→ [[03 Mathematics/02 - Similarity Correlation and Convolution]]

---

## Metrics (interview)

| Task | Metric |
|------|--------|
| Detection | mAP @ IoU 0.5:0.95 (COCO) |
| Segmentation | mIoU, pixel accuracy |
| Imbalanced | per-class precision/recall |

---

## Common traps

| Trap | Correct |
|------|---------|
| mAP on synthetic val only | **Real** val set |
| `conf` too low | Floods false positives |
| Semantic vs instance | Same class touching → one blob in semantic |

---

**Next:** [[05 - Synthetic Image Generation]]
