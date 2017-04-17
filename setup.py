from __future__ import print_function
from setuptools import setup
from opencvutils.version import __version__ as VERSION
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution


PACKAGE_NAME = 'opencvutils'
BuildCommand.pkg = PACKAGE_NAME
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION


setup(
	name=PACKAGE_NAME,
	packages=[PACKAGE_NAME],
	version=VERSION,
	description='Simple OpenCV 3 image processing functions',
	author='Kevin J. Walchko',
	long_description=open('README.rst').read(),
	author_email='kevin.walchko@outlook.com',
	url='https://github.com/walchko/{}'.format(PACKAGE_NAME),
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
	install_requires=['numpy', 'pyyaml', 'build_utils', 'fake_rpi'],
	scripts=['bin/camera_calibrate.py', 'bin/mjpeg_server.py', 'bin/video_capture.py'],
	license='MIT',
	cmdclass={
		'make': BuildCommand,
		'publish': PublishCommand
	},
)
