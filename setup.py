from __future__ import print_function
from setuptools import setup
from opencvutils import __version__ as VERSION
import os
from setuptools.command.test import test as TestCommand
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
	def is_pure(self):
		return False


class BuildCommand(TestCommand):
	"""Build binaries/packages"""
	def run_tests(self):
		print('Delete dist directory and clean up binary files')
		os.system('rm -fr dist')
		os.system('rm opencvutils/*.pyc')
		os.system('rm opencvutils/__pycache__/*.pyc')

		print('Run Nose tests')
		print('Python2 tests')
		ret = os.system("python2 -m nose -v -w tests test.py")
		if ret > 0:
			print('<<< Python2 nose tests failed >>>')
			return
		print('Python3 tests')
		ret = os.system("python3 -m nose -v -w tests test.py")
		if ret > 0:
			print('<<< Python3 nose tests failed >>>')
			return

		print('Building packages ...')
		print('>> Python source ----------------------------------------------')
		os.system("python setup.py sdist")
		print('>> Python 2.7 -------------------------------------------------')
		os.system("python2 setup.py bdist_wheel")
		print('>> Python 3.6 -------------------------------------------------')
		os.system("python3 setup.py bdist_wheel")


class PublishCommand(TestCommand):
	"""Publish to Pypi"""
	def run_tests(self):
		print('Publishing to PyPi ...')
		os.system("twine upload dist/opencvutils-{}*".format(VERSION))


setup(
	name='opencvutils',
	packages=['opencvutils'],
	version=VERSION,
	description='Simple OpenCV 3 image processing functions',
	author='Kevin J. Walchko',
	long_description=open('README.rst').read(),
	author_email='kevin.walchko@outlook.com',
	url='https://github.com/walchko/opencvutils',
	keywords=['computer vision', 'image processing', 'opencv'],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.6',
		'Topic :: Software Development :: Libraries',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Software Development :: Libraries :: Application Frameworks'
	],
	# install_requires=['matplotlib', 'numpy', 'scipy'],
	# install_requires=['numpy', 'scipy'],
	# install_requires=['numpy', 'pyyaml'],
	install_requires=['numpy', 'pyyaml'],
	scripts=['bin/camera_calibrate.py', 'bin/mjpeg_server.py', 'bin/video_capture.py'],
	license='MIT',
	cmdclass={
		'make': BuildCommand,
		'publish': PublishCommand
	},
)
