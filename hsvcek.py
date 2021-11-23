import cv2 as cv
import numpy as np

colour = np.uint8([[[0,0,255 ]]]) # Blue Color
hsv_colour = cv.cvtColor(colour,cv.COLOR_BGR2HSV)
print( hsv_colour )