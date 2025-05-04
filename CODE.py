import cv2
import numpy as np
import cv2 as cv

img = None


path = r"C:\user\Desktop\image.jpg"
img =  cv.imread(path,1)
window = "Image"
cv.imshow(window,img)
cv.waitKey(0)
cv.destroyAllWindows()
