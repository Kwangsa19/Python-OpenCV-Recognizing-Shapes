# Python-OpenCV-Recognizing-Shapes
> This project is based on Coursera project course("Recognizing shapes in images with OpenCV"). For full explanation and information, please visit this [link](https://www.coursera.org/projects/recognizing-shapes-images-opencv) to enroll the course. 
> Here, I used OpenCV to load and compute an image from file, detect edges, recognize lines, blurred mode and circles. 

## Tasks

The following are what I did in this project: 
* Load an image from file.
* Compute image gradients.
* Detect edges in an image using Canny edge detection.
* Recognize lines in an image using Hough transforms.
* Recognize circles in an image using Hough transforms.

## Requirements

The following modules and knowledge you have to prepare: 
* OpenCV module (cv2).
* Numpy module (numpy).
* Os (os).
* Hough transform theory.

## Implementation

* Importing libraries: 
```
import cv2
import numpy as np
import os
```
After this, we find the image filenames and define the function for viewing images. Please see the attached code. 

* Load an image from file
```
i = cv2.imread(f)
view_image(i) 
```
![python_abutr7s7qk](https://github.com/Kwangsa19/Python-OpenCV-Recognizing-Shapes/assets/135963482/f2a3fe6e-2c2f-42bc-af3d-bfbb498290b4)
 
* Compute image gradients
```
# grayscale
i_gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
print(i_gray.shape)
print(i_gray[0,0])
view_image(i_gray) # (640 , 427) 18
```
![python_9uCUXPy56Y](https://github.com/Kwangsa19/Python-OpenCV-Recognizing-Shapes/assets/135963482/f53297c3-8571-486a-9d97-980e8238a950)

```
# X gradient
sobelx = cv2.Sobel(i_gray, cv2.CV_64F, 1, 0)
abs_sobelx = np.absolute(sobelx)
view_image(abs_sobelx / np.max(abs_sobelx))
```
![python_2xIJErMVUc](https://github.com/Kwangsa19/Python-OpenCV-Recognizing-Shapes/assets/135963482/907e3716-a289-4a60-92b0-5f371088ddfe)

```
# Y gradient
sobely = cv2.Sobel(i_gray, cv2.CV_64F, 0 , 1)
abs_sobely = np.absolute(sobely)
view_image(abs_sobely / np.max(abs_sobely))
```
![python_ZMtBNHjbDx](https://github.com/Kwangsa19/Python-OpenCV-Recognizing-Shapes/assets/135963482/1dba7363-8f6d-476c-97d2-d975d5d07ee9)

```
# Magnitute of gradient vector
magnitute = np.sqrt(sobelx**2 + sobely **2)
view_image(magnitute / np.max(magnitute))
```
![python_PBRfNc3KMm](https://github.com/Kwangsa19/Python-OpenCV-Recognizing-Shapes/assets/135963482/39ae75ef-ce58-4d30-add3-c941d1d861e5)

```
# Canny edge detection
edges = cv2.Canny(i_gray, 200, 250)
view_image(edges)
```
![python_YcE07Caq0u](https://github.com/Kwangsa19/Python-OpenCV-Recognizing-Shapes/assets/135963482/a3f49ede-43d6-4fb3-a2a6-a601e5c2c90a)

```
# Hough transform for lines
lines = cv2.HoughLinesP(edges, rho=1, theta=1. * np.pi/180.0, threshold=20, minLineLength=25, maxLineGap=5)
i_lines = i.copy()
for l in lines:
    x1,y1,x2,y2 = l[0]
    cv2.line(i_lines, (x1,y1), (x2,y2), (0,0,255), thickness=3)
view_image(i_lines)
```
![python_L7etccn5F7](https://github.com/Kwangsa19/Python-OpenCV-Recognizing-Shapes/assets/135963482/9fb7d919-5136-484f-96b8-3be5302e7173)

```
# Hough transform for circles
# Assuming everything else is correct
circles = cv2.HoughCircles(i_gray, method=cv2.HOUGH_GRADIENT, dp=2, minDist=35, param1=150, param2=40, minRadius=15, maxRadius=25)

# Check if circles is not None and has at least one circle
if circles is not None and circles.shape[1] > 0:
    # Convert the circles to integers
    circles = np.uint16(np.around(circles))

    i_circles = i.copy()

    for circle in circles[0, :]:
        x, y, r = circle
        cv2.circle(i_circles, (x, y), r, (0, 0, 255), thickness=3)

    view_image(i_circles)
else:
    print("No circles detected.")

```
![python_loq0k1JjHI](https://github.com/Kwangsa19/Python-OpenCV-Recognizing-Shapes/assets/135963482/a3138d58-5f3f-482a-9ae8-8be1e38d6c9b)

```
# Blurred
i_blurred = cv2.GaussianBlur(i_gray, ksize=(21,21), sigmaX=0,)
view_image(i_blurred)
```
![python_Um4Qi7gkVa](https://github.com/Kwangsa19/Python-OpenCV-Recognizing-Shapes/assets/135963482/30e3d000-e35e-4761-972c-01c3c3f90666)

```
circles = cv2.HoughCircles(i_blurred, method=cv2.HOUGH_GRADIENT, dp=2, minDist=35, param1=150, param2=40, minRadius=15, maxRadius=25)

# Check if circles is not None and has at least one circle
if circles is not None and circles.shape[1] > 0:
    # Convert the circles to integers
    circles = np.uint16(np.around(circles))

    i_circles = i.copy()

    for circle in circles[0, :]:
        x, y, r = circle
        cv2.circle(i_circles, (x, y), r, (0, 0, 255), thickness=3)

    view_image(i_circles)
else:
    print("No circles detected.")
```
![python_uhE9sCppBH](https://github.com/Kwangsa19/Python-OpenCV-Recognizing-Shapes/assets/135963482/98a33afb-629f-47fc-b21b-1e74ce0df16e)

## Future Works
* Provide an input prompt to select an image.
* Provide GUI using Tkinter with buttons to choose photo modes (grayscale, X & Y gradients, canny edge, shape detections, and blurred mode).



