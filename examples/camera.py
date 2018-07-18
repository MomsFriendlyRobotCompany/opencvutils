#!/usr/bin/env python

from __future__ import print_function
import cv2
from opencvutils import Camera

cnt = 0


cam = Camera()
# cam.gray = True
cam.init(win=(320, 240), cameraNumber=0)

while True:
	ret, im = cam.read()

	if ret:
		cv2.imshow('image', im)
		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			break
		elif key == ord("s"):
			cv2.imwrite("image-{}.png".format(cnt), im)
			print('>> Wrote: {}'.format("image-{}.png".format(cnt)))
			cnt += 1
