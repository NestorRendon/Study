# Object Detection and Segmentation Metrics

**Prev:** [[03 - Ranking Clustering and Quality Metrics]] · **Next:** [[05 - Neural Network RNN and LSTM Metrics]]

---

## Interview one-liner

Detection is classification **plus location** — getting the class right isn't enough if the box is in the wrong place. Every metric here exists to answer: "was the box close enough, and was it confident enough to count?"

---

## In plain English

A detector for "find every car in this image" can fail in more ways than a plain classifier: it can miss a car entirely (false negative), hallucinate a car that isn't there (false positive), find the right car but draw the box too loosely (localization error), or find the same car twice (duplicate). IoU handles "was the box close enough," and mAP rolls confidence, precision, recall, and localization all into one number.

---

## IoU (Intersection over Union) — the foundation

$$\text{IoU} = \frac{\text{Area of Overlap}}{\text{Area of Union}} = \frac{|A \cap B|}{|A \cup B|}$$

Where $A$ is the predicted box and $B$ is the ground-truth box. Ranges 0 (no overlap) to 1 (perfect match).

**A prediction only "counts" as a true positive if IoU exceeds a threshold** (commonly 0.5) — below that, it's treated as a false positive, even if the class label was correct.

---

## Worked example

Ground-truth box: $(x_1, y_1, x_2, y_2) = (10, 10, 50, 50)$ → area $= 40 \times 40 = 1600$.
Predicted box: $(20, 20, 60, 60)$ → area $= 40 \times 40 = 1600$.

Overlap region: $(20, 20)$ to $(50, 50)$ → area $= 30 \times 30 = 900$.

Union $= 1600 + 1600 - 900 = 2300$.

$$\text{IoU} = \frac{900}{2300} \approx 0.39$$

At an IoU threshold of 0.5, this prediction would be counted as a **false positive** — close, but not close enough.

---

## From IoU to Average Precision (AP)

Once you have an IoU threshold, every predicted box becomes a TP or FP, ranked by the model's confidence score. Then:

1. Sort predictions by confidence, high to low.
2. Walk down the list, computing precision and recall at each point.
3. Plot the precision-recall curve.

$$\text{AP} = \int_0^1 p(r)\, dr \quad \text{(area under the precision-recall curve, for one class)}$$

$$\text{mAP} = \frac{1}{C}\sum_{c=1}^{C} \text{AP}_c \quad \text{(mean AP across all } C \text{ classes)}$$

**COCO's mAP@[.5:.95]** takes this further: it computes AP at IoU thresholds $0.5, 0.55, 0.6, \dots, 0.95$ and averages them — a much stricter, more localization-sensitive score than the older "mAP@0.5" (used by PASCAL VOC), because it also rewards *tight* boxes, not just roughly-correct ones.

| Metric | What it rewards |
|--------|----------------------|
| **mAP@0.5** | Loose localization is fine — just be roughly in the right place |
| **mAP@[.5:.95]** | Tight, precise boxes — the modern standard (COCO benchmark, YOLO papers) |
| **AP per class** | Reveals which classes the model is actually bad at, hidden by the mean |

---

## Non-Max Suppression (NMS) — why it matters for evaluation

A raw detector often predicts many overlapping boxes for the same object. **NMS** removes duplicates: keep the highest-confidence box, discard any other box with IoU above a threshold against it. This runs *before* metrics are computed — a bad NMS threshold (too loose = duplicate false positives, too tight = suppresses genuinely separate nearby objects) will distort every metric downstream, so it's worth mentioning explicitly when discussing detector evaluation.

---

## Segmentation metrics

For pixel-level tasks (semantic/instance segmentation), IoU generalizes directly:

$$\text{Pixel IoU (Jaccard)} = \frac{|A \cap B|}{|A \cup B|} \qquad \text{Dice coefficient} = \frac{2|A \cap B|}{|A| + |B|}$$

| | IoU | Dice |
|---|-----|------|
| **Relationship** | $\text{Dice} = \frac{2 \cdot \text{IoU}}{1 + \text{IoU}}$ — Dice is always ≥ IoU | |
| **Common in** | General detection/segmentation benchmarks | Medical imaging (tumor/organ segmentation) — more forgiving of small overlaps, common as a loss function too |
| **Pixel Accuracy** | Fraction of all pixels correctly classified — misleading with class imbalance (e.g. huge background class), same trap as accuracy in [[02 - Classification Metrics]] | |

---

## Other task-specific metrics worth knowing

| Task | Metric | Idea |
|------|--------|------|
| Keypoint detection (pose estimation) | **PCK** (Percentage of Correct Keypoints) | A predicted keypoint counts as correct if within a distance threshold of the ground truth (often scaled by object size) |
| Multi-object tracking | **MOTA** | Combines false positives, misses, and identity switches across frames into one score |

---

## Common traps

| Trap | Why it's wrong | What to say instead |
|------|------------------|----------------------|
| Reporting mAP@0.5 as if it's the modern standard | It's a loose threshold — a model can score well with sloppy boxes | "I'd report mAP@[.5:.95] (COCO-style) for a stricter, more informative number" |
| Ignoring per-class AP | The mean can hide a class the model completely fails on | "I'd break down AP by class to find weak spots, especially for rare classes" |
| Comparing detectors evaluated with different NMS thresholds | NMS settings change the FP/duplicate rate independent of the model's real quality | "I'd fix the same NMS and confidence threshold before comparing mAP across models" |
| Using pixel accuracy for segmentation with a huge background class | A model that predicts "background" everywhere still scores high | "I'd use IoU or Dice per class instead, same reasoning as the accuracy trap in classification" |

---

**Next:** [[05 - Neural Network RNN and LSTM Metrics]]
