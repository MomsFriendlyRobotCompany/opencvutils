from IPython.display import HTML
import matplotlib.pyplot as plt
from math import ceil
from opencvutils import opencv2matplotlib


def showVideo(filename, width=None):
	# from IPython.display import HTML
	video = open(filename, "rb").read()
	video_encoded = video.encode("base64")
	if width:
		video_tag = '<video width={} controls src="data:video/x-m4v;base64,{}">'.format(width, video_encoded)
	else:
		video_tag = '<video controls src="data:video/x-m4v;base64,{}">'.format(video_encoded)
	return HTML(video_tag)


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
