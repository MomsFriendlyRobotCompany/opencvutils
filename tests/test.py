#!/usr/bin/env python

import opencvutils as cvu
# from opencvutils import Camera


def test_version():
	assert cvu.is_cv2() is False
	assert cvu.is_cv3() is True
	assert cvu.get_opencv_version() == (3, 2, 0), 'This should be true of Travis.ci'


def test_url():
	url = 'https://avatars0.githubusercontent.com/u/918960?v=3&s=460'
	im = cvu.url_to_image(url)
	assert im.shape == (460, 460, 3)


def test_files():
	path = './cal_images'
	gen = cvu.list_images(path)
	for i in range(9):
		im = './cal_images/shot_00{}.png'.format(i)
		assert gen.next() == im


def test_dummy():
	# c = Camera('pi')
	# c.init()
	# ret, im = c.read()
	# if ret:
	# 	im = cvu.translate(im, 10, 10)
	assert True
