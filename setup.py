
from setuptools import setup
from opencvutils import __version__ as VERSION
import os
from setuptools.command.test import test as TestCommand


class PublishCommand(TestCommand):
	def run_tests(self):
		print('Publishing to PyPi ...')
		os.system("python setup.py sdist")
		os.system("python setup.py bdist_wheel")
		os.system("twine upload dist/opencvutils-{}*.whl".format(VERSION))


setup(
	name='opencvutils',
	# packages=['imutils', 'imutils.video', 'imutils.io'],
	packages=['opencvutils', 'opencvutils.video', 'opencvutils.io'],
	version=VERSION,
	description='A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3.',
	author='Kevin Walchko',
	long_description=open('README.rst').read(),
	author_email='kevin.walchko@outlook.com',
	url='https://github.com/walchko/opencvutils',
	keywords=['ipython', 'jupyter', 'notebook', 'computer vision', 'image processing', 'opencv', 'matplotlib'],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2.7',
		'Topic :: Software Development :: Libraries',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Software Development :: Libraries :: Application Frameworks'
	],
	# install_requires=['matplotlib', 'numpy', 'scipy'],
	# install_requires=['numpy', 'scipy'],
	install_requires=['numpy'],
	# scripts=['bin/range-detector.py'],
	scripts=['bin/camera_calibrate.py', 'bin/mjpeg_server.py']
	license='MIT',
	cmdclass={
		# 'test': NoseTestCommand,
		'publish': PublishCommand,
		# 'tag': GitTagCommand,
		# 'clean': CleanCommand
	},
)
