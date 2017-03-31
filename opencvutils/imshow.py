# import numpy as np
import cv2
# import sys
import matplotlib.pyplot as plt
from math import ceil


def opencv2matplotlib(image):
	# OpenCV represents images in BGR order; however, Matplotlib
	# expects the image in RGB order, so simply convert from BGR
	# to RGB and return
	return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def imshow(images, bgr=True, width=4, titles=None, figsize=None, showaxes=False):
	"""
	Make an array of plots.

	exmaple:
		imshow([im1,im2], bgr=True, width=1, titles=['one', 'two'], figsize=(4,2), showaxes=True)

	params:
		images - array of images
		bgr - if a color image, assume it is opencv and switch it rgb format
		width - how many images wide
		figsize - a tuple (width,height) of how wide the figure should be in inches (this is depended on your dpi setting)
		titles - an array of titles for each subplot
		showaxes - True/False to show axes
	"""
	# edit the size of the figures
	if figsize:
		fs = figsize
		plt.figure(figsize=fs)
	else:
		plt.figure()

	# figure out the number of subplots
	num = len(images)
	if num > width:
		col = width
	else:
		col = num
	row = int(ceil(num/col))

	# draw the plots
	for i, im in enumerate(images):
		plt.subplot(row, col, i+1)

		# plot RGB images
		if len(im.shape) > 2:
			if bgr:
				im = opencv2matplotlib(im)
			plt.imshow(im)
		# plot grayscale images
		else:
			plt.imshow(im, cmap='gray')

		# do we want axes?
		if showaxes:
			pass
		else:
			plt.xticks(())
			plt.yticks(())

		# do we want titles?
		if titles:
			plt.title(titles[i])

	# clean up and make pretty
	plt.tight_layout()
