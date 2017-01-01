__version__ = '0.5.1'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2016 Kevin Walchko'
__author__ = 'Kevin J. Walchko'
__version__ = '0.5.7'

# import the necessary packages
from .convenience import translate
from .convenience import rotate
from .convenience import resize
from .convenience import skeletonize
from .convenience import opencv2matplotlib
# from .convenience import url_to_image
from .convenience import auto_canny
from .convenience import is_cv2
from .convenience import is_cv3
from .convenience import get_opencv_version
# from .convenience import imshow
from .meta import find_function
import contours
# from paths import list_images, list_files
import paths
import video
import io
from object_detection import non_max_suppression
