# Morphological Operations

* In short: A set of operations that process images based on shapes. Morphological operations apply a *structuring element* to an input image and generate an output image.  
* The most basic morphological operations are: Erosion and Dilation. They have a wide array of uses, i.e. :  
    * Removing noise  
    * Isolation of individual elements and joining disparate elements in an image.  
    * Finding of intensity bumps or holes in an image  
* We will explain dilation and erosion briefly, using the following image as an example:
  
* ![Morphology_1_Tutorial_Theory_Original_Image.png.webp](assets/DE8D7D35-3E5F-490F-B79A-C455BAA4C34D.webp)  
**Dilation**  
* This operations consists of convolving an image *A*
 with some kernel ( *B*
), which can have any shape or size, usually a square or circle.  
* The kernel *B*
 has a defined *anchor point*, usually being the center of the kernel.  
* As the kernel *B*
 is scanned over the image, we compute the maximal pixel value overlapped by *B*
 and replace the image pixel in the anchor point position with that maximal value. As you can deduce, this maximizing operation causes bright regions within an image to "grow" (therefore the name *dilation*).  
  
* Take the above image as an example. Applying dilation we can get:
  
* ![Morphology_1_Tutorial_Theory_Dilation.png.webp](assets/AACD623B-4F58-433B-9212-EA9FD9738FE3.webp)  
* The bright area of the letter dilates around the black regions of the background.  
**Erosion**  
* This operation is the sister of dilation. It computes a local minimum over the area of given kernel.  
* As the kernel *B*
 is scanned over the image, we compute the minimal pixel value overlapped by *B*
 and replace the image pixel under the anchor point with that minimal value.  
  
* Analagously to the example for dilation, we can apply the erosion operator to the original image (shown above). You can see in the result below that the bright areas of the image get thinner, whereas the dark zones gets bigger.
  
* ![Morphology_1_Tutorial_Theory_Erosion.png.webp](assets/1ECA79FD-BD2C-499D-A05A-51EE58F80993.webp)  
  
  
** Opening**  
Opening is just another name of **erosion followed by dilation**. It is useful in removing noise, as we explained above. Here we use the function, **[cv.morphologyEx()](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f)**  
  
opening = [cv.morphologyEx](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f)(img, cv.MORPH_OPEN, kernel)  
Result:  
![opening.png.webp](assets/5220BE5E-D089-4DF0-8AB4-6D5AB3281A6B.webp)  
**image**  
**4. Closing**  
Closing is reverse of Opening, **Dilation followed by Erosion**. It is useful in closing small holes inside the foreground objects, or small black points on the object.  
  
closing = [cv.morphologyEx](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f)(img, cv.MORPH_CLOSE, kernel)  
Result:  
![closing.png.webp](assets/D0067A73-E7CC-4A03-825C-942A404B1E5D.webp)  
**image**  
**5. Morphological Gradient**  
It is the difference between dilation and erosion of an image.  
The result will look like the outline of the object.  
  
gradient = [cv.morphologyEx](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f)(img, cv.MORPH_GRADIENT, kernel)  
Result:  
![gradient.png.webp](assets/824F3F8C-635F-49E7-A988-3DEB6DD247E9.webp)  
**image**  
  
  
cv2.matchTemplate()  
![unknown.jpg](assets/7AC85BFF-DACC-4057-BA3D-37CD832D2AB7.jpg)  
  
  
  
SIFT usually stands for **Scale-Invariant Feature Transform** in computer vision.  
It’s an algorithm used to detect and describe distinctive points/features in images so they can be matched across different images—even if the object is:  
* resized (scale changes),  
* rotated,  
* partially viewed from another angle,  
* or under somewhat different lighting.
