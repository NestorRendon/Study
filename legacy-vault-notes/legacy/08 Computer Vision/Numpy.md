# Numpy:

numpy.fromfunction:   The resulting array therefore has a value fn(x, y, z) at coordinate (x, y, z).  
  
  
  

| FUNCTION | CATEGORY | WHAT IT DOES |
| -------------------------- | ------------ | ------------------------------------------------------------------------- |
| cv2.imread() | I/O | Loads an image from disk into a NumPy array (BGR by default) |
| cv2.imwrite() | I/O | Saves an image array to a file in the specified format |
| cv2.imshow() | I/O | Displays an image in a GUI window for quick inspection |
| cv2.VideoCapture() | I/O | Opens a video file or camera stream for frame-by-frame reading |
| cv2.cvtColor() | Color | Converts between color spaces (BGR↔Gray, BGR↔HSV, BGR↔Lab…) |
| cv2.resize() | Geometry | Scales an image to a target size using a chosen interpolation method |
| cv2.flip() | Geometry | Flips an image horizontally, vertically, or both |
| cv2.warpAffine() | Geometry | Applies a 2×3 affine transformation (rotate, translate, shear) |
| cv2.warpPerspective() | Geometry | Applies a full perspective (homography) warp — used for document scanning |
| cv2.GaussianBlur() | Filtering | Smooths noise with a Gaussian kernel; standard pre-processing step |
| cv2.medianBlur() | Filtering | Removes salt-and-pepper noise while preserving edges |
| cv2.Canny() | Edges | Multi-stage edge detector producing thin, single-pixel edges (uses sober) |
| cv2.Sobel() | Edges | Computes image gradient in x or y direction for edge analysis |
| cv2.threshold() | Segmentation | Binarizes an image using a fixed or Otsu-computed threshold |
| cv2.adaptiveThreshold() | Segmentation | Thresholds each region independently — handles uneven lighting |
| cv2.findContours() | Segmentation | Extracts object boundaries from a binary image as point lists |
| cv2.drawContours() | Segmentation | Renders contour shapes onto an image for visualization or masking |
| cv2.erode() / cv2.dilate() | Morphology | Shrink or expand foreground regions; base of morphological pipelines |
| cv2.morphologyEx() | Morphology | Opening, closing, gradient, top-hat operations in one call |
| cv2.matchTemplate() | Matching | Slides a template across an image and scores similarity at each position |
| cv2.calcHist() | Analysis | Computes color or intensity histograms for a region of interest |
| cv2.boundingRect() | Analysis | Returns the upright bounding box of a contour or point set |
  
  
   
  
Describe ONNX, tensor  Tensorflow, caffe, PyTorch, when use each one   
  
  
  
STATE-OF-THE-ART ALGORITHMS — HIGH-POWER VISION  
  
  
HSV  
  
  
![What is the HSV color space?](assets/E0A894FC-D02F-4EDF-986B-65B325710CFC.png)  
  
![Shadows](assets/6191DE03-D098-4DC1-AA30-52B3A0598AA4.webp)
