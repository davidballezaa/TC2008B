import cv2
import numpy as np

def create_color_blend(width, height, color_a, color_b):
    gradient = np.zeros((height, width, 3), dtype='uint8')

    for x in range(width):
        alpha = x / width
        color = (1 - alpha) * np.array(color_a) + alpha * np.array(color_b)

        gradient[:, x] = color
    
    return gradient

width, height = 800, 400

color_a = (255, 0, 0)
color_b = (0, 255, 0)

gradient_image = create_color_blend(width, height, color_a, color_b)

cv2.imshow('Color Blend', gradient_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
