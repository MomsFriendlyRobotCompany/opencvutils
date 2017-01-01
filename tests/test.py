#!/usr/bin/env python

import opencvutils as cvu
from opencvutils.video import Camera

def test_dummy():
	c = Camera('pi')
	c.init()
	ret, im = c.read()
	if ret:
		im = cvu.translate(im, 10, 10)
	assert True
