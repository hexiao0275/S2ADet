import cv2

from PIL import Image

image1=cv2.imread("real_rgb_0083.tiff",-1)
image2=cv2.merge([image1,image1,image1,image1,image1,image1])
iimage3=image1