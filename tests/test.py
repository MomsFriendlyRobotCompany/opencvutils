#!/usr/bin/env python

import opencvutils as cvu
# from opencvutils import Camera


def test_version():
	assert cvu.is_cv2() is False
	assert cvu.is_cv3() is True
	assert cvu.get_opencv_version() == (3, 2, 0)


def test_dummy():
	# c = Camera('pi')
	# c.init()
	# ret, im = c.read()
	# if ret:
	# 	im = cvu.translate(im, 10, 10)
	assert True


# def test_tempfile():
# 	t = TempFile(ext='.png')
# 	# f = t.get()
# 	t.close()
# 	assert True
