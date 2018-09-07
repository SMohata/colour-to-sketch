import cv2

# reading the image
img = cv2.imread('ranveer.jpg', 1)
# converting the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# inverting the image
img_invert = cv2.bitwise_not(img_gray)
# bluring or smoothing the inverted image with the kernel size (10,10)
img_blur = cv2.blur(img_invert, (10, 10))

"""The Dodge blend function divides the bottom layer by the inverted top layer. This lightens the bottom layer depending on the value of the top layer. We have the blurred image, which highlights the boldest edges."""
def dodgeV2(image, mask):
    return cv2.divide(image, 255 - mask, scale=256)


final_img = dodgeV2(img_gray, img_blur)

# displaying the sketch image
cv2.imshow('image', final_img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('viratsketch.png', final_img)
    cv2.destroyAllWindows()
