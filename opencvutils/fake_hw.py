import numpy as np
import platform


class BGR(object):
	"""Fake class"""
	array = np.random.rand(240, 320)

	def truncate(self, num):
		self.array = np.random.rand(240, 320)


class picamera(object):
	"""Fake class"""
	class PiCamera(object):
		"""Fake class"""
		resolution = (0, 0)

		def __init__(self):
			print('WARNING: Cannot run PiCamera on {}'.format(platform.system().lower()))

		def close(self):
			pass

		def capture(self, image, format, use_video_port):
			pass

	class array(object):
		"""Fake class"""

		@staticmethod
		def PiRGBArray(cam, size):
			return BGR()
