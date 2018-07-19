#!/usr/bin/env python3

from opencvutils import CameraCalibration
from opencvutils import list_images
import matplotlib.pyplot as plt
import time
import cv2
import numpy as np


def test_checkerboard_calibrate():
    cal = CameraCalibration(show_markers=True)  # change this to True to see the images with markers found

    if False:
        marker = (9,6,)
        imgs = cal.getImages('./cal_images/*.png')
    else:
        marker = (7,5,)
        imgs = cal.getImages('./cal_images2/*.png')

    if True:
        imgs2 = []
        for im in imgs:
            sim = cv2.pyrDown(im)
            imgs2.append(sim)
        imgs = imgs2
    
    cal.marker_checkerboard = True
    cal.save_file = 'calibration.npy'
    mx = cal.calibrate(imgs, marker_size=marker)
    print('rms', mx['rms'])
    cal.printMatrix()
    # assert (mx['rms'] - 0.5882563398961391) < 1e-6

    for im in (cal.save_cal_imgs):
        plt.imshow(im)
        plt.pause(0.5)
    plt.close()


test_checkerboard_calibrate()


def test_stereo():
    # Grab some data
    # left_img = cv2.imread('stereo/00/image_0/000000.png', 0)
    # right_img = cv2.imread('stereo/00/image_1/000000.png', 0)
    left_img = cv2.imread('stereo_cal/left.png', 0)
    right_img = cv2.imread('stereo_cal/right.png', 0)

    print('image shape:', left_img.shape)

    # Do some stereo processing
    stereo = cv2.StereoBM_create(numDisparities=32, blockSize=13)
    # disp_gray = stereo.compute(np.array(left_img), np.array(right_img))
    disp_gray = stereo.compute(left_img, right_img)
    # disp_rgb = stereo.compute(
    #     cv2.cvtColor(np.array(first_rgb[0]), cv2.COLOR_RGB2GRAY),
    #     cv2.cvtColor(np.array(first_rgb[1]), cv2.COLOR_RGB2GRAY))

    # Display some data
    plt.subplot(2, 1, 1)
    plt.imshow(left_img, cmap='gray')
    plt.title('Left Gray Image (cam0)')

    plt.subplot(2,1,2)
    plt.imshow(disp_gray, cmap='viridis')
    plt.title('Gray Stereo Disparity')

    # ax[1, 0].imshow(first_rgb[0])
    # ax[1, 0].set_title('Left RGB Image (cam2)')
    #
    # ax[1, 1].imshow(disp_rgb, cmap='viridis')
    # ax[1, 1].set_title('RGB Stereo Disparity')

    plt.show()

# test_stereo()
