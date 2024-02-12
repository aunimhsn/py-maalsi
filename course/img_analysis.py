import cv2

img_src = cv2.imread('./images/src/porche.jpg')


gray_image = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

print(gray_image)

# Inverting the Imge
invert_image = cv2.bitwise_not(gray_image)

# Blur Image
blur_image = cv2.GaussianBlur(invert_image, (21,21), 0)

# Inverting the Blured Image
invert_blur = cv2.bitwise_not(blur_image)

# Convert Image Into sketch
sketch = cv2.divide(gray_image, invert_blur, scale=256.0)

# Generating the Sketch Image Named as Sketch.png
cv2.imwrite('./images/dist/001.png', sketch)