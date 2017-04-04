
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
	packages=['opencvutils'],
	version=VERSION,
	description='Simple OpenCV 3 image processing functions',
	author='Kevin Walchko',
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
		'publish': PublishCommand
	},
)
