import cv2
import numpy as np
import os

files = (
    'subway.jpg',
)
f = os.path.join('images', files[0])

def view_image(i):
    cv2.imshow('view', i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# view the image
i = cv2.imread(f)
view_image(i) 

print(i.shape)
print(i[0,0,:]) # (640 , 427, 3) [22 24 4]

# grayscale
i_gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
print(i_gray.shape)
print(i_gray[0,0])
view_image(i_gray) # (640 , 427) 18 

# X gradient
sobelx = cv2.Sobel(i_gray, cv2.CV_64F, 1, 0)
abs_sobelx = np.absolute(sobelx)
view_image(abs_sobelx / np.max(abs_sobelx))

# Y gradient
sobely = cv2.Sobel(i_gray, cv2.CV_64F, 0 , 1)
abs_sobely = np.absolute(sobely)
view_image(abs_sobely / np.max(abs_sobely))

# Magnitute of gradient vector
magnitute = np.sqrt(sobelx**2 + sobely **2)
view_image(magnitute / np.max(magnitute))

# Canny edge detection
edges = cv2.Canny(i_gray, 200, 250)
view_image(edges)

# Hough transform for lines
lines = cv2.HoughLinesP(edges, rho=1, theta=1. * np.pi/180.0, threshold=20, minLineLength=25, maxLineGap=5)
i_lines = i.copy()
for l in lines:
    x1,y1,x2,y2 = l[0]
    cv2.line(i_lines, (x1,y1), (x2,y2), (0,0,255), thickness=3)
view_image(i_lines)

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

# Blurred
i_blurred = cv2.GaussianBlur(i_gray, ksize=(21,21), sigmaX=0,)
view_image(i_blurred)

# Blurred circle
circles = cv2.HoughCircles(i_blurred, method=cv2.HOUGH_GRADIENT, dp=2, minDist=35, param1=150, param2=40, minRadius=15, maxRadius=25)

# Check if circles is not None and has at least one circle
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
