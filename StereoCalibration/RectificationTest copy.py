import numpy as np
import cv2 as cv
import glob, os
from matplotlib import pyplot as plt

# Camera parameters to undistort and rectify images
cv_file = cv.FileStorage()
cv_file.open('stereoMap.xml', cv.FileStorage_READ)

stereoMapL_x = cv_file.getNode('stereoMapL_x').mat()
stereoMapL_y = cv_file.getNode('stereoMapL_y').mat()
stereoMapR_x = cv_file.getNode('stereoMapR_x').mat()
stereoMapR_y = cv_file.getNode('stereoMapR_y').mat()
####################################################

print(stereoMapL_x.shape)

imagesLeft = sorted(glob.glob('left_camera/*.png'))
imagesRight = sorted(glob.glob('right_camera/*.png'))

i = 0

for imgLeft, imgRight in zip(imagesLeft, imagesRight): 

    left_read_img  = cv.imread(imgLeft)
    right_read_img = cv.imread(imgRight)

    frame_left_rect  = cv.remap(left_read_img,  stereoMapL_x, stereoMapL_y, cv.INTER_LANCZOS4, cv.BORDER_CONSTANT, 0)
    frame_right_rect = cv.remap(right_read_img, stereoMapR_x, stereoMapR_y, cv.INTER_LANCZOS4, cv.BORDER_CONSTANT, 0)

    camera_images = np.hstack((frame_left_rect, frame_right_rect)) 

    cv.imwrite('rectified\\' + str(i) + '.png' ,camera_images)

    #cv.imshow('rectified_L', frame_left_rect)
    #cv.imshow('rectified_R', frame_right_rect)
    #cv.waitKey(50)

    i+=1

cv.destroyAllWindows()