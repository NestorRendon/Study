#   
# OPENCV  
#   
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
  
  
![What is the HSV color space?](Attachments/E0A894FC-D02F-4EDF-986B-65B325710CFC.png)  
  
![Shadows](Attachments/6191DE03-D098-4DC1-AA30-52B3A0598AA4.webp)  
## Otsu’s Thresholding Concept  
Otsu's thresholding is an automatic, global image binarization technique that segments an image into foreground and background by finding a threshold value that minimizes within-class variance (or maximizes inter-class variance). It works best on bimodal histograms, efficiently separating pixels into two classes.   
##   
Automatic global thresholding algorithms usually have following steps.  
1. Process the input image  
2. Obtain image histogram (distribution of pixels)  
3. Compute the threshold value T  
4. Replace image pixels into white in those regions, where saturation is greater than T  
5.  and into the black in the opposite cases.  
  
  
## Morphological Operations  
* In short: A set of operations that process images based on shapes. Morphological operations apply a *structuring element* to an input image and generate an output image.  
* The most basic morphological operations are: Erosion and Dilation. They have a wide array of uses, i.e. :  
    * Removing noise  
    * Isolation of individual elements and joining disparate elements in an image.  
    * Finding of intensity bumps or holes in an image  
* We will explain dilation and erosion briefly, using the following image as an example:   
* ![Morphology_1_Tutorial_Theory_Original_Image.png.webp](Attachments/DE8D7D35-3E5F-490F-B79A-C455BAA4C34D.webp)  
**Dilation**  
* This operations consists of convolving an image *A*  with some kernel ( *B* ), which can have any shape or size, usually a square or circle.  
* The kernel *B*  has a defined *anchor point*, usually being the center of the kernel.  
* As the kernel *B*  is scanned over the image, we compute the maximal pixel value overlapped by *B*  and replace the image pixel in the anchor point position with that maximal value. As you can deduce, this maximizing operation causes bright regions within an image to "grow" (therefore the name *dilation*).  
  
* Take the above image as an example. Applying dilation we can get:   
* ![Morphology_1_Tutorial_Theory_Dilation.png.webp](Attachments/AACD623B-4F58-433B-9212-EA9FD9738FE3.webp)  
* The bright area of the letter dilates around the black regions of the background.  
**Erosion**  
* This operation is the sister of dilation. It computes a local minimum over the area of given kernel.  
* As the kernel *B*  is scanned over the image, we compute the minimal pixel value overlapped by *B*  and replace the image pixel under the anchor point with that minimal value.  
  
* Analagously to the example for dilation, we can apply the erosion operator to the original image (shown above). You can see in the result below that the bright areas of the image get thinner, whereas the dark zones gets bigger.   
* ![Morphology_1_Tutorial_Theory_Erosion.png.webp](Attachments/1ECA79FD-BD2C-499D-A05A-51EE58F80993.webp)  
  
  
** Opening**  
Opening is just another name of **erosion followed by dilation**. It is useful in removing noise, as we explained above. Here we use the function, **[cv.morphologyEx()](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f)**  
  
opening = [cv.morphologyEx](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f)(img, cv.MORPH_OPEN, kernel)  
Result:  
![opening.png.webp](Attachments/5220BE5E-D089-4DF0-8AB4-6D5AB3281A6B.webp)  
**image**  
**4. Closing**  
Closing is reverse of Opening, **Dilation followed by Erosion**. It is useful in closing small holes inside the foreground objects, or small black points on the object.  
  
closing = [cv.morphologyEx](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f)(img, cv.MORPH_CLOSE, kernel)  
Result:  
![closing.png.webp](Attachments/D0067A73-E7CC-4A03-825C-942A404B1E5D.webp)  
**image**  
**5. Morphological Gradient**  
It is the difference between dilation and erosion of an image.  
The result will look like the outline of the object.  
  
gradient = [cv.morphologyEx](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f)(img, cv.MORPH_GRADIENT, kernel)  
Result:  
![gradient.png.webp](Attachments/824F3F8C-635F-49E7-A988-3DEB6DD247E9.webp)  
**image**  
  
  
cv2.matchTemplate()  
![unknown.jpg](Attachments/7AC85BFF-DACC-4057-BA3D-37CD832D2AB7.jpg)  
  
  
  
SIFT usually stands for **Scale-Invariant Feature Transform** in computer vision.  
It’s an algorithm used to detect and describe distinctive points/features in images so they can be matched across different images—even if the object is:  
* resized (scale changes),  
* rotated,  
* partially viewed from another angle,  
* or under somewhat different lighting.  
## What SIFT does  
It finds **keypoints** (interesting image locations like corners/blobs) and computes a **descriptor** for each one so you can compare them between images.  
## Common uses  
* Image stitching / panoramas  
* Object recognition  
* Feature matching between frames  
* 3D reconstruction / SLAM  
## Why it’s popular  
Because the features are robust to scale and rotation changes.  
  
  
  
OPTICAL Flow   
  
  
  
  

| FUNCTION / MODULE | CATEGORY | WHAT IT DOES | PRACTICAL EXAMPLE | KEY TERMS EXPLAINED |
| ---------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cv2.dnn.readNet() | Deep learning | Loads any ONNX / TensorFlow / Caffe / Darknet model for inference via OpenCV's DNN module | Load a YOLOv8 model exported to ONNX and run object detection on a webcam feed — no PyTorch needed at runtime | ONNX — Open Neural Network Exchange: a universal file format that lets you train in PyTorch/TF and deploy anywhere. Caffe / Darknet — older deep-learning frameworks; Darknet is the original home of YOLO. DNN module — OpenCV's built-in inference engine that runs models on CPU or GPU without a full framework installed. |
| cv2.dnn.blobFromImage() | Deep learning | Pre-processes an image into a 4D blob (NCHW) ready for a neural network forward pass | Resize a photo to 640×640, normalize pixel values to [0,1], and package it as a batch of 1 before passing it to YOLO | Blob — a packed multi-dimensional array; neural networks expect this exact structure. NCHW — the 4 dimensions: N = number of images (batch size), C = color channels (3 for RGB), H = height, W = width. Forward pass — running data through the network from input to output to get a prediction (no training involved). |
| cv2.SIFT_create() | Features | Scale- and rotation-invariant keypoint detector and descriptor — gold standard for matching | Match a product photo taken at different zoom levels and angles to identify it in a store shelf image | Keypoint — a distinctive point in an image (corner, blob) that is easy to find again in another image. Descriptor — a numeric fingerprint (vector of numbers) that describes the region around a keypoint. Scale-invariant — finds the same keypoints whether the image is zoomed in or out. Rotation-invariant — works even if the object is tilted. |
| cv2.ORB_create() | Features | When you create it:

orb = cv2.ORB_create()

you get an object that can:

Detect keypoints in an image
Compute descriptors for those keypointReal-time binary descriptor combining FAST + BRIEF; rotation-invariant and license-free.  | Track a logo on a mobile device in real time — ORB runs fast enough for 30+ FPS on a phone CPU | FAST — Features from Accelerated Segment Test: a very quick corner detector that checks a ring of pixels around each candidate point.                                                                         BRIEF — Binary Robust Independent Elementary Features: describes a keypoint as a string of 0s and 1s by comparing pixel pairs, making it tiny and fast to compare.                               Binary descriptor — uses bits instead of floats, so matching is done with XOR (extremely fast). License-free — SIFT was patented until 2020; ORB was designed as a free alternative. |
|  cv2.AKAZE_create() | Features | Nonlinear scale-space detector — strong on textured and blurred images | Match aerial drone photos where parts of the scene are motion-blurred or have varying sharpness | Nonlinear scale-space — instead of blurring the image with a simple Gaussian (which smears edges), AKAZE uses a PDE that respects edges while still smoothing noise — giving better keypoints near object boundaries. Scale-space — a pyramid of the image at progressively lower resolutions, used to find features that are stable across zoom levels. |
| cv2.BFMatcher / FlannBasedMatcher | Features | Match feature descriptors between two images with brute force or approximate nearest-neighbor search | After detecting SIFT keypoints in two photos of the same building, find which keypoints correspond to the same physical point | BFMatcher — Brute-Force Matcher: compares every descriptor in image A against every descriptor in image B; slow but exact. FLANN — Fast Library for Approximate Nearest Neighbors: uses clever data structures (KD-trees, etc.) to find close-enough matches much faster — ideal when you have thousands of descriptors. Nearest-neighbor — the descriptor in B whose values are most similar (smallest distance) to a given descriptor in A. |
| cv2.findHomography() | Geometry | Estimates a homography from point correspondences using RANSAC | Stitch two overlapping photos of a whiteboard into a single flat image, correcting for the camera angle | Homography — a 3×3 matrix that maps points from one flat plane to another (e.g., one camera view to another).    RANSAC — Random Sample Consensus: an algorithm that ignores outliers (wrong matches) by repeatedly picking a small random subset of matches, fitting a model, and keeping the model that explains the most matches. Robust to noise and false matches. |
| cv2.estimateAffinePartial2D() | Geometry | Robust partial-affine estimation with RANSAC — used in video stabilization and face alignment | Compute the shift+rotation+scale between consecutive video frames to cancel out camera shake | Affine transform — a transformation that preserves parallel lines: allows translation (move), rotation, scaling, and shear — but not perspective distortion. Partial affine — restricts to rotation + uniform scale + translation (4 parameters instead of 6), which is more stable when you have few points. RANSAC — see above; here it discards moving objects so only the background (camera motion) drives the estimate. |
| cv2.Stitcher_create() | Geometry | Full panorama stitching pipeline: detect → match → homography → blend | Combine 6 overlapping photos taken by rotating a phone into a seamless 360° panorama | Stitching pipeline — a sequence of steps (feature detection → matching → homography estimation → warping → exposure compensation → seam finding → blending) automated into one object. Seam finding — choosing where one image ends and the next begins so the boundary is invisible.                           Blending — smoothly fading between images near the seam to avoid harsh edges. |
| cv2.StereoSGBM_create() | 3D vision | Semi-global block matching for dense stereo disparity maps | Use a calibrated stereo camera (like on a robot or car) to produce a depth map of the scene — each pixel gets a distance value | Stereo — using two cameras (like human eyes) to infer depth from the difference in position of objects between the two views. Disparity map — an image where each pixel's value encodes how far that object point shifted between left and right camera (larger shift = closer object). SGBM — Semi-Global Block Matching: matches small patches of pixels across both images along multiple scan directions, producing smoother depth maps than simple block matching. |
| cv2.reprojectImageTo3D() | 3D vision | Converts a disparity map to a 3D point cloud using a calibrated Q matrix | Turn a stereo depth map of a room into a 3D point cloud that can be visualized or fed to a robot planner | Point cloud — a set of (X, Y, Z) coordinates in 3D space, one per pixel. Q matrix — a 4×4 reprojection matrix produced during stereo calibration that encodes the camera baseline and focal length; it converts (x, y, disparity) pixel values into real-world (X, Y, Z) meters. |
| cv2.solvePnP() | 3D vision | Estimates object pose (6-DOF) from 2D–3D point correspondences | Given 4 corners of a printed AR marker and their known 3D positions, compute exactly where and how the camera is oriented in 3D space | PnP — Perspective-n-Point: the problem of finding camera pose from n known 3D points and their 2D projections. 6-DOF — 6 Degrees of Freedom: 3 for position (X, Y, Z) + 3 for rotation (roll, pitch, yaw) — fully describing where an object is in 3D. Pose — the combination of position and orientation of an object or camera. |
| cv2.calibrateCamera() | 3D vision | Computes intrinsic matrix and distortion coefficients from chessboard calibration images | Take 20 photos of a chessboard from different angles to characterize a webcam's lens — necessary before any 3D measurement | Intrinsic matrix — a 3×3 matrix encoding the camera's internal properties: focal length (how zoomed in) and principal point (where the optical axis hits the sensor). Distortion coefficients — numbers that describe lens warping (barrel or pincushion distortion) so it can be mathematically corrected. Chessboard — used because its corners can be found precisely and their 3D positions on the flat board are exactly known. |
| cv2.CascadeClassifier | Detection | Real-time sliding-window detector for faces and rigid objects using Haar or LBP features | Detect all faces in a video frame in real time on a Raspberry Pi — fast enough without a GPU | Cascade — a series of fast filters arranged from simplest to most complex; a region is rejected early if it fails a simple test, so most of the image is discarded quickly. Haar features — simple rectangular filters (like "the eye area is darker than the forehead") learned from training data. LBP — Local Binary Pattern: describes texture by comparing each pixel to its neighbors; faster than Haar but slightly less accurate. Sliding window — the detector moves a fixed-size box across the image at every position and scale to check for the object. |
| cv2.HOGDescriptor + SVM | Detection | HOG features fed to SVM — the classic pedestrian detector | Detect people in surveillance camera footage using only CPU — still used in embedded systems and drones | HOG — Histogram of Oriented Gradients: divides the image into small cells and counts how many edges point in each direction; produces a feature vector that describes local shape well. SVM — Support Vector Machine: a classical ML classifier that finds the optimal boundary between "person" and "not person" in HOG-feature space. Oriented gradients — the direction (angle) and strength of intensity changes (edges) at each pixel. |
| cv2.TrackerCSRT / TrackerKCF | Tracking | Single-object discriminative correlation filter trackers | After clicking on a car in frame 1 of a video, keep a bounding box locked onto that specific car through the whole clip | Correlation filter — learns a template of the target in the frequency domain and finds where it best matches in the next frame; very fast because multiplication in frequency domain = convolution in image domain. CSRT — Channel and Spatial Reliability Tracking: uses more channels and a reliability mask — more accurate but slower. KCF — Kernelized Correlation Filter: simpler, faster, works well for small/non-rotating targets. Discriminative — the tracker learns what the target looks like AND what the background looks like, so it isn't fooled by similar-looking distractors. |
| cv2.calcOpticalFlowPyrLK() | Tracking | Lucas-Kanade sparse optical flow with pyramids — tracks keypoints across frames | Track the tips of a surgeon's fingers across video frames to measure hand motion without attaching any markers | Optical flow — the apparent motion of pixels between two frames caused by movement of objects or the camera. Sparse — only tracks a chosen set of points (e.g., corners), not every pixel. Lucas-Kanade — assumes pixels in a small neighborhood all move together; solves a least-squares system to find the best (dx, dy) shift. Pyramids (PyrLK) — computes flow at multiple image scales so large, fast motions (which would be invisible at fine scale) are captured at coarser levels first. |
| cv2.calcOpticalFlowFarneback() | Tracking | Dense optical flow — estimates motion for every pixel | Visualize crowd flow in a stadium, or compute a motion mask to separate moving objects from a static background | Dense optical flow — unlike sparse, this computes a motion vector (dx, dy) for every single pixel in the frame. Farneback — approximates the image locally with a polynomial and finds the shift that best explains the change between frames; more accurate than block matching. Motion vector — a 2D arrow showing where each pixel moved from one frame to the next. |
| cv2.BackgroundSubtractorMOG2 / KNN | Segmentation | Adaptive Gaussian mixture background model; detects foreground blobs in video | In a parking lot camera, automatically detect any vehicle or person that enters the scene — everything else is "background" | Background subtraction — learns what the static scene looks like over time, then flags anything that doesn't fit as foreground. MOG2 — Mixture of Gaussians v2: models each pixel as a mixture of Gaussian distributions to handle gradual lighting changes and small background motion (swaying trees). KNN — K-Nearest Neighbors variant: instead of Gaussians, stores recent pixel values and classifies a new pixel as background if it's close to enough stored samples. Foreground blob — a connected group of pixels detected as belonging to a moving object. |
| cv2.grabCut() | Segmentation | Graph-cut interactive foreground segmentation seeded by a bounding box | Draw a rectangle around a product in a photo and let GrabCut automatically cut it out from the background for an e-commerce listing | Graph cut — represents the image as a graph where pixels are nodes and edges encode similarity; "cutting" the graph separates foreground from background at minimum cost. GMM — inside GrabCut, both foreground and background colors are modeled as Gaussian Mixture Models that are iteratively refined. Seed / bounding box — the user provides a rough rectangle; pixels outside it are forced background, pixels inside are classified iteratively. |
| cv2.watershed() | Segmentation | Marker-based morphological segmentation for touching/overlapping objects | Separate individual cells that are touching each other in a microscopy image — a task where simple thresholding merges them all into one blob | Watershed — treats pixel intensities like a topographic map (peaks and valleys); "floods" the map from user-provided seed markers until regions meet, drawing boundaries at the meeting lines. Markers — small labeled seeds (one per object and one for background) that tell the algorithm where each region starts. Over-segmentation — a common problem where watershed creates too many tiny regions; solved by pre-processing or distance-transform markers. |
| cv2.face.LBPHFaceRecognizer | Recognition | LBP Histogram face recognizer — lightweight, works without a GPU | Build a door access system that recognizes 10 employees from a dataset of 5 photos each, running on a Raspberry Pi | LBPH — Local Binary Pattern Histograms: divides the face into a grid of cells, computes LBP texture codes in each cell, and concatenates their histograms into one feature vector. LBP — for each pixel, compares it to its 8 neighbors and writes a 1 if the neighbor is brighter, 0 otherwise — producing an 8-bit |
  
  
  
Homography:   
A homography is a 3x3 invertible matrix transformation, commonly used in computer vision to map points from one planar scene to another,   
![Rotating camera, arbitrary world](Attachments/719C46FE-68E8-4A1C-A261-89222BCCFC2D.jpg)  
  
cv2.Stitcher_create()  
  
![image_stitching_opencv_header.jpg](Attachments/F69EB09B-80D0-4F57-B831-0585C3E28688.jpg)  
  
  
# hough line transform  
  
![maxresdefault.jpg](Attachments/02CE6F81-6FDB-4D23-8E63-0479F3589626.jpg)  
  
  
Harrys corner detection:  
  
![Corner Detection: Basic idea](Attachments/4453B6DE-8A2E-4FF0-826C-26E00993DC1E.png)  
  
  
  
SIFT Detector :   
  
![sift_keypoints.jpg](Attachments/91F4317F-5792-4FFC-B781-16768BF0F282.jpg)  
  
  
## Comparison Table  

| Feature | TensorRT | ONNX Runtime | OpenVINO | TensorFlow Lite | TorchScript / PyTorch |
| ------------------ | ----------------------- | ------------------------- | -------------------- | ------------------- | --------------------- |
| Best For | Max speed on NVIDIA GPU | Cross-platform deployment | Intel hardware | Mobile/Edge | Fastest prototyping |
| Hardware | NVIDIA only | CPU/GPU/Many backends | Intel CPUs/GPUs/VPUs | Mobile/Embedded | Wherever PyTorch runs |
| Speed | Fastest on NVIDIA | Very good | Excellent on Intel | Excellent on mobile | Usually slowest |
| Portability | Low | High | Medium | Medium | Low |
| Optimization Depth | Very deep | Moderate | Deep for Intel | Deep for mobile | Minimal |
| Setup Complexity | High | Medium | Medium | Medium | Low |
  
Sources:  
  
## When To Use What  
## Use TensorRT if:  
* You deploy on **NVIDIA GPUs only**  
* You need **lowest latency / highest FPS**  
* You care about **production optimization**  
* Example: Real-time object detection on RTX/A100  
  
## Use ONNX Runtime if:  
* You need **portability**  
* You deploy on **different hardware**  
* You want **easy deployment from PyTorch**  
* Example: Same model on laptop CPU, cloud GPU, edge device  
  
![JpenMP + AVX |](Attachments/4AD172C7-99B0-4865-A194-555B2312F8F6.webp)  
  
![Bicubic](Attachments/C1CB0BEE-A509-42B6-AB61-8BE615E065BD.jpg)  
  
 slicing, indexing, mathematical operations, linear algebra, reductions. And they are fast!  
Dynamic Neural Networks: Tape-Based Autograd  
computation graph  
  
