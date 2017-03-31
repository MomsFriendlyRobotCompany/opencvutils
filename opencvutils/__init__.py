__version__ = '0.7.0'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2016 Kevin Walchko'
__author__ = 'Kevin J. Walchko'


# from __future__ import print_function

# import the necessary packages
from .convenience import translate
from .convenience import rotate
from .convenience import resize
from .convenience import skeletonize
from .convenience import auto_canny
from .imshow import imshow
from .imshow import opencv2matplotlib
from .Camera import Camera
from .CameraCalibrate import CameraCalibration
from .meta import find_function
from .contours import sort_contours
from .contours import label_contours
from .paths import list_images, list_files
from .path import url_to_image
from .object_detection import non_max_suppression
import cv2


def get_opencv_version():
	return cv2.__version__.split('.')


def is_cv2():
	# if we are using OpenCV 2, then our cv2.__version__ will start
	# with '2.'
	return True if get_opencv_version()[0] == '2' else False


def is_cv3():
	# if we are using OpenCV 3.X, then our cv2.__version__ will start
	# with '3.'
	return True if get_opencv_version()[0] == '3' else False


if is_cv2():
	print 'WARNING: OpenCV 2.x is detected, this library is designed to work with OpenCV 3.x'
