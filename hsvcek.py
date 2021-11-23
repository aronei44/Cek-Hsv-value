import cv2 as cv
import numpy as np


print("Insert RGB. example : 0,0,255 ")
color = input("insert RGB: ")
color = color.split(',')
color = np.array([int(i) for i in color])
colour = np.uint8([[color]]) # Blue Color
hsv_colour = cv.cvtColor(colour,cv.COLOR_BGR2HSV)
print( hsv_colour )