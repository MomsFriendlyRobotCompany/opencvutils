from __future__ import print_function
import numpy as np
import cv2
from glob import glob
import yaml
import json


class CameraCalibration(object):
    '''
    Simple calibration class.
    '''
    marker_checkerboard = True
    marker_size = None
    save_cal_imgs = []

    def __init__(self, show_markers=True):
        self.show_markers = show_markers
        self.save_cal_imgs = []

    def __del__(self):
        pass

    # write camera calibration file out
    def save(self, save_file, handle=yaml):
        with open(save_file, 'w') as f:
            handle.dump(self.data, f)
                
    # read camera calibration file in
    def read(self, matrix_name, handle=yaml):
        with open(matrix_name, 'r') as f:
            self.data = handle.load(f)
        return self.data

    # print the estimated camera parameters
    def printMatrix(self, data=None):
        # self.data = {'camera_matrix': mtx, 'dist_coeff': dist, 'newcameramtx': newcameramtx}
        # print 'mtx:',self.data['camera_matrix']
        # print 'dist:',self.data['dist_coeff']
        # print 'newcameramtx:',self.data['newcameramtx']
        if data is None:
            data = self.data

        m = data['camera_matrix']
        k = data['dist_coeff']
        print('focal length {0:3.1f} {1:3.1f}'.format(m[0][0], m[1][1]))
        print('image center {0:3.1f} {1:3.1f}'.format(m[0][2], m[1][2]))
        print('radial distortion {0:3.3f} {1:3.3f}'.format(k[0][0], k[0][1]))
        print('tangental distortion {0:3.3f} {1:3.3f}'.format(k[0][2], k[0][3]))
        print('RMS error:', data['rms'])

    # Pass a gray scale image and find the markers (i.e., checkerboard, circles)
    # TODO: make objpoints and imgpoints a class member
    def findMarkers(self, gray, objpoints, imgpoints):
        # objp = np.zeros((self.marker_size[0]*self.marker_size[1],3), np.float32)
        # objp[:,:2] = np.mgrid[0:self.marker_size[0],0:self.marker_size[1]].T.reshape(-1,2)
        objp = np.zeros((np.prod(self.marker_size), 3), np.float32)
        objp[:, :2] = np.indices(self.marker_size).T.reshape(-1, 2)  # make a grid of points

        # Find the chess board corners or circle centers
        if self.marker_checkerboard is True:
            ret, corners = cv2.findChessboardCorners(gray, self.marker_size)
        else:
            ret, corners = cv2.findCirclesGrid(gray, self.marker_size, flags=cv2.CALIB_CB_ASYMMETRIC_GRID)

        if ret:
            imgpoints.append(corners.reshape(-1, 2))
            objpoints.append(objp)
        else:
            corners = [] # didn't find any

        return ret, objpoints, imgpoints, corners

    # draw the detected corners on the image for display
    def draw(self, image, corners):
        if not self.show_markers:
            return image
        # Draw and display the corners
        if corners is not None:
            cv2.drawChessboardCorners(image, self.marker_size, corners, True)

        return image

    # use a calibration matrix to undistort an image
    def undistort(self, image, alpha):
        """
        image: an image

        alpha = 0: returns undistored image with minimum unwanted pixels (image
                    pixels at corners/edges could be missing)
        alpha = 1: retains all image pixels but there will be black to make up
                    for warped image correction
        """
        h,w = image.shape[:2]
        mtx = self.data['camera_matrix']
        dist = self.data['dist_coeff']
        # Adjust the calibrations matrix
        # alpha=0: returns undistored image with minimum unwanted pixels (image pixels at corners/edges could be missing)
        # alpha=1: retains all image pixels but there will be black to make up for warped image correction
        # returns new cal matrix and an ROI to crop out the black edges
        newcameramtx, _ = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), alpha)
        # undistort
        ret = cv2.undistort(image, mtx, dist, None, newcameramtx)
        return ret

    def getImages(self, path):
        """
        Given a path, it reads all images. This uses glob to grab file names
        and excepts wild cards *

        Ex. cal.getImages('./images/*.jpg')
        """
        imgs = []
        files = glob(path)

        print("Found: {}".format(len(tuple(files))))
        print('-'*40)

        for i, f in enumerate(files):
            img = cv2.imread(f, 0)
            if img is None:
                raise Exception('>> Could not read: {}'.format(f))
            else:
                if len(img.shape) > 2:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                print("[{}]:{} ({}, {})".format(i, f, *img.shape))
                imgs.append(img)
        print('-'*40)
        return imgs

    # run the calibration process on a series of images
    def calibrate(self, images, marker_size=(9, 6)):
        """
        images: an array of grayscale images, all assumed to be the same size
        """

        self.marker_size = marker_size
        self.save_cal_imgs = []

        # Arrays to store object points and image points from all the images.
        objpoints = []  # 3d point in real world space
        imgpoints = []  # 2d points in image plane.

        max_corners = self.marker_size[0]*self.marker_size[1]

        for cnt, gray in enumerate(images):
            orig = gray.copy()
            if len(gray.shape) > 2:
                gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

            ret, objpoints, imgpoints, corners = self.findMarkers(gray, objpoints, imgpoints)
            # If found, add object points, image points (after refining them)
            if ret:
                print('[{}] + found {} of {} corners'.format(cnt, corners.size / 2, max_corners))
                term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
                cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), term)

                # Draw the corners
                orig = self.draw(orig, corners)
                self.save_cal_imgs.append(orig)
            else:
                print('[{}] - Could not find markers'.format(cnt))

        # h, w = images[0].shape[:2]
        # rms, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, (w, h), None, None)

        # images size here is backwards: w,h
        rms, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

        # Adjust the calibrations matrix
        # alpha=0: returns undistored image with minimum unwanted pixels (image pixels at corners/edges could be missing)
        # alpha=1: retains all image pixels but there will be black to make up for warped image correction
        # returns new cal matrix and an ROI to crop out the black edges
        # newcameramtx, _ = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), alpha)
        # self.data = {'camera_matrix': mtx, 'dist_coeff': dist, 'newcameramtx': newcameramtx, 'rms': rms, 'rvecs': rvecs, 'tvecs': tvecs}
        self.data = {'camera_matrix': mtx, 'dist_coeff': dist, 'rms': rms}
        return self.data
